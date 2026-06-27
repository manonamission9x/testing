#!/usr/bin/env python3
"""
Comprehensive product scraper for trimurti.in
Scrapes ALL 208 individual product pages for complete data.
"""
import json
import re
import subprocess
import sys
import os
import time
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

INPUT_FILE = r"C:\Users\kingo\trimurti-redesign\product-migration\raw-scrape.json"
OUTPUT_FILE = r"C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json"
PROGRESS_FILE = r"C:\Users\kingo\trimurti-redesign\product-migration\scrape_progress.json"
MAX_RETRIES = 3
BATCH_SIZE = 3
REQUEST_TIMEOUT = 45

class ProductHTMLParser(HTMLParser):
    """Extract product data from HTML."""
    def __init__(self):
        super().__init__()
        self.reset_state()
        
    def reset_state(self):
        self.in_short_desc = False
        self.short_desc_depth = 0
        self.in_title = False
        self.in_posted_in = False
        self.in_tagged_as = False
        self.in_product_meta = False
        self.product_meta_depth = 0
        self.collecting_meta = False
        self.short_description_parts = []
        self.title = ""
        self.categories = []
        self.tags = []
        self.pdf_urls = []
        self.current_tag = ""
        self.depth = 0
        self.in_body = False
        self.script_style_depth = 0
        self.in_script = False
        self.in_style = False
        self.collecting_short_desc = False
        self.active_tag = ""
        self.active_attrs = {}
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Skip script and style content
        if tag in ('script', 'style'):
            self.in_script = True
            self.script_style_depth = 1
            return
        
        class_attr = attrs_dict.get('class', '')
        id_attr = attrs_dict.get('id', '')
        
        # Product title
        if tag == 'h2' and 'product_title' in class_attr and 'entry-title' in class_attr:
            self.in_title = True
            self.title = ""
            
        # Short description
        if 'woocommerce-product-details__short-description' in class_attr:
            self.collecting_short_desc = True
            self.short_description_parts = []
            return
            
        if self.collecting_short_desc:
            if tag == 'a':
                href = attrs_dict.get('href', '')
                if href.lower().endswith('.pdf'):
                    self.pdf_urls.append(href)
            # Still collect text content
            if tag == 'br':
                self.short_description_parts.append('\n')
            elif tag == 'p':
                pass  # paragraph boundaries handled by text
            elif tag == 'ul':
                pass
            elif tag == 'li':
                self.short_description_parts.append('\n• ')
            return
            
        # Product meta
        if 'product_meta' in class_attr:
            self.collecting_meta = True
            return
            
        if self.collecting_meta:
            if 'posted_in' in class_attr:
                self.in_posted_in = True
            elif 'tagged_as' in class_attr:
                self.in_tagged_as = True
            # Collect links
            if tag == 'a' and self.collecting_meta:
                if self.in_posted_in:
                    self.categories.append(attrs_dict.get('rel', '') or attrs_dict.get('href', ''))
                elif self.in_tagged_as:
                    self.tags.append(attrs_dict.get('rel', '') or attrs_dict.get('href', ''))
                    
    def handle_endtag(self, tag):
        if self.in_script and tag in ('script', 'style'):
            self.in_script = False
            return
            
        if self.collecting_short_desc and tag in ('div',):
            # Check if we're closing the short description div
            self.collecting_short_desc = False
            return
            
        if self.collecting_meta and tag in ('div', 'span'):
            if self.in_posted_in:
                self.in_posted_in = False
            if self.in_tagged_as:
                self.in_tagged_as = False
            self.collecting_meta = False
            
        if self.in_title and tag == 'h2':
            self.in_title = False
            
    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
            
        data = data.strip()
        if not data:
            return
            
        if self.in_title:
            self.title += data
            
        if self.collecting_short_desc:
            self.short_description_parts.append(data)
            
        if self.collecting_meta:
            if self.in_posted_in:
                # Data might be "Categories: Field Crops" - extract just the name
                pass
            if self.in_tagged_as and data != 'Tag:':
                tag_name = data.strip()
                if tag_name and tag_name not in ('Tag:', ''):
                    self.tags.append(tag_name)


def fetch_page(url, timeout=REQUEST_TIMEOUT):
    """Fetch a page using curl."""
    for attempt in range(MAX_RETRIES):
        try:
            result = subprocess.run(
                ['curl', '-sS', '--max-time', str(timeout), '-L', url],
                capture_output=True,
                text=True,
                timeout=timeout + 5
            )
            if result.returncode == 0 and len(result.stdout) > 1000:
                return result.stdout
            elif attempt < MAX_RETRIES - 1:
                print(f"  Retry {attempt+1} for {url} (size={len(result.stdout)})")
                time.sleep(2)
        except subprocess.TimeoutExpired:
            print(f"  Timeout for {url}, attempt {attempt+1}")
            time.sleep(2)
        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            time.sleep(2)
    return None


def check_is_404(html):
    """Check if the page is a 404."""
    if html is None:
        return True
    if 'Page not found' in html[:2000]:
        return True
    if '404' in html[:500]:
        return True
    return False


def has_real_pdf_header(pdf_url):
    """Check if URL actually returns a PDF (Content-Type) rather than redirecting to an image."""
    try:
        result = subprocess.run(
            ['curl', '-sS', '--max-time', '10', '-I', '-L', pdf_url],
            capture_output=True,
            text=True,
            timeout=15
        )
        headers = result.stdout.lower()
        if 'content-type: application/pdf' in headers or '.pdf' in pdf_url.lower():
            # Also check it's not an image in disguise
            if 'content-type: image' in headers:
                return False
            return True
        return '.pdf' in pdf_url.lower()
    except:
        return '.pdf' in pdf_url.lower()


def extract_tag_from_url(tag_url):
    """Extract tag name from URL."""
    if not tag_url:
        return ""
    parts = tag_url.rstrip('/').split('/')
    if parts:
        name = parts[-1].replace('-', ' ').title()
        return name
    return ""


def extract_with_regex(html):
    """Extract product data using regex patterns."""
    data = {
        'title': '',
        'short_description': '',
        'categories': [],
        'tags': [],
        'pdf_urls': [],
        'is_404': False
    }
    
    if not html:
        data['is_404'] = True
        return data
    
    # Check for 404
    if 'Page not found' in html[:3000]:
        data['is_404'] = True
        return data
    
    # Extract title
    title_match = re.search(r'<h2[^>]*class="[^"]*product_title[^"]*entry-title[^"]*"[^>]*>\s*(.*?)\s*</h2>', html, re.DOTALL)
    if title_match:
        data['title'] = title_match.group(1).strip()
    
    # Extract short description - get ALL text content between woocommerce-product-details__short-description divs
    desc_matches = re.findall(
        r'<div[^>]*class="[^"]*woocommerce-product-details__short-description[^"]*"[^>]*>(.*?)</div>\s*(?:</div>)?',
        html, re.DOTALL
    )
    
    if desc_matches:
        # Take the longest one (first occurrence is usually the main product description)
        desc_html = desc_matches[0]
        
        # Extract text, preserving line breaks
        # First, replace <br> with newlines
        desc_text = re.sub(r'<br\s*/?>', '\n', desc_html)
        # Remove remaining HTML tags
        desc_text = re.sub(r'<[^>]+>', '', desc_text)
        # Decode HTML entities
        desc_text = desc_text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        desc_text = desc_text.replace('&#8211;', '–').replace('&#038;', '&')
        desc_text = desc_text.replace('&nbsp;', ' ')
        # Clean up
        desc_text = re.sub(r'\n{3,}', '\n\n', desc_text)
        desc_text = desc_text.strip()
        data['short_description'] = desc_text
        
        # Extract PDF URLs from description
        pdf_links = re.findall(r'<a[^>]*href="([^"]*\.pdf)"[^>]*>', desc_html, re.IGNORECASE)
        data['pdf_urls'] = pdf_links
    
    # Extract categories from product_meta
    # Try all meta sections
    meta_sections = re.findall(
        r'<div[^>]*class="[^"]*product_meta[^"]*"[^>]*>(.*?)</div>',
        html, re.DOTALL
    )
    
    for meta_html in meta_sections:
        # Categories
        cat_matches = re.findall(
            r'<span[^>]*class="[^"]*posted_in[^"]*"[^>]*>.*?Categories?:(.*?)</span>',
            meta_html, re.DOTALL
        )
        for cm in cat_matches:
            cats = re.findall(r'<a[^>]*rel="tag"[^>]*>(.*?)</a>', cm)
            for c in cats:
                c_name = c.strip()
                if c_name and c_name not in data['categories']:
                    data['categories'].append(c_name)
        
        # Also try without "Categories:" prefix
        cat_matches2 = re.findall(
            r'<span[^>]*class="[^"]*posted_in[^"]*"[^>]*>(.*?)</span>',
            meta_html, re.DOTALL
        )
        for cm in cat_matches2:
            cats = re.findall(r'<a[^>]*rel="tag"[^>]*>(.*?)</a>', cm)
            for c in cats:
                c_name = c.strip()
                if c_name and c_name not in data['categories']:
                    data['categories'].append(c_name)
        
        # Tags
        tag_matches = re.findall(
            r'<span[^>]*class="[^"]*tagged_as[^"]*"[^>]*>(.*?)</span>',
            meta_html, re.DOTALL
        )
        for tm in tag_matches:
            tags = re.findall(r'<a[^>]*rel="tag"[^>]*>(.*?)</a>', tm)
            for t in tags:
                t_name = t.strip()
                if t_name and t_name not in data['tags']:
                    data['tags'].append(t_name)
    
    # Also try to find category from the product class
    class_match = re.search(r'class="product[^"]*product_cat-([^"\s]+)', html)
    if class_match and not data['categories']:
        cat_slug = class_match.group(1).replace('-', ' ').title()
        data['categories'].append(cat_slug)
    
    return data


def extract_attributes_from_description(desc):
    """Extract product attributes (duration, season, region, etc.) from the description text."""
    attrs = {}
    
    if not desc:
        return attrs
    
    # Duration/maturity
    duration_patterns = [
        r'(?:maturing|maturity|duration)[:\s]*([^.]*?(?:\d+\s*[-–to]+\s*\d+[^.]*?days[^.]*)\.)',
        r'([Ff]ull\s+season[^.]*\d+\s*[-–to]+\s*\d+\s*days[^.]*\.)',
        r'([Mm]edium\s+matur(?:ing|ity)[^.]*\d+\s*[-–to]+\s*\d+\s*days[^.]*\.)',
        r'([Ee]arly\s+matur(?:ing|ity)[^.]*\d+\s*[-–to]+\s*\d+\s*days[^.]*\.)',
        r'([Mm]id[- ]early\s+matur(?:ing|ity)[^.]*\d+\s*[-–to]+\s*\d+\s*days[^.]*\.)',
    ]
    
    for pattern in duration_patterns:
        match = re.search(pattern, desc, re.IGNORECASE)
        if match:
            attrs['Duration'] = match.group(1).strip()
            break
    
    # If no explicit duration sentence, try simpler pattern
    if 'Duration' not in attrs:
        match = re.search(r'(\d+\s*[-–to]+\s*\d+\s*days)', desc)
        if match:
            # Find the context (season) around it
            start = max(0, match.start() - 60)
            end = min(len(desc), match.end() + 60)
            context = desc[start:end].strip()
            attrs['Duration'] = context
    
    # Season
    season_match = re.search(r'(Kharif|Rabi|Spring|Zaid)', desc)
    if season_match:
        seasons = re.findall(r'(Kharif|Rabi|Spring|Zaid)', desc)
        attrs['Season'] = ', '.join(sorted(set(seasons)))
    
    # Region / Area
    region_matches = re.findall(r'\b([A-Z]{2})\b', desc)
    india_states = ['AP', 'AS', 'BR', 'CG', 'GJ', 'HR', 'HP', 'JH', 'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UK', 'UP', 'WB', 'AN', 'CH', 'DN', 'DD', 'DL', 'LD', 'PY']
    found_states = [s for s in region_matches if s in india_states]
    if found_states:
        attrs['Region'] = ', '.join(found_states)
    
    # Look for "North India", "South India", etc.
    region_text = re.search(r'(North|South|East|West|Central)\s+India', desc)
    if region_text and 'Region' not in attrs:
        regions = re.findall(r'(North|South|East|West|Central)\s+India', desc)
        attrs['Region'] = ', '.join(set(regions))
    
    # "suitable for" info
    suitable_match = re.search(r'(?:Suitable for|Ideal for)[^.]*\.', desc)
    if suitable_match and 'Region' not in attrs:
        attrs['Suitability'] = suitable_match.group(0).strip()
    
    # Yield potential
    yield_match = re.search(r'(?:yield|yielding)[^.]*\.', desc)
    if yield_match:
        yield_text = yield_match.group(0).strip()
        if 'high' in yield_text.lower() or 'very high' in yield_text.lower():
            attrs['Yield'] = 'High'
        elif 'medium' in yield_text.lower():
            attrs['Yield'] = 'Medium'
    
    # Plant height
    height_match = re.search(r'(\d+\s*[-–to]+\s*\d+\s*cm\s+plant\s+height)', desc, re.IGNORECASE)
    if height_match:
        attrs['Plant Height'] = height_match.group(1).strip()
    
    # Grain type
    grain_match = re.search(r'(?:Long|Medium|Short|Extra[-\s]*long)\s+(?:bold|slender|fine|basmati)[^.]*grains?', desc, re.IGNORECASE)
    if grain_match:
        attrs['Grain Type'] = grain_match.group(0).strip()
    
    # Tillers
    tiller_match = re.search(r'(\d+\s*[-–to]+\s*\d+\s*(?:productive\s+)?tillers?)', desc, re.IGNORECASE)
    if tiller_match:
        attrs['Productive Tillers'] = tiller_match.group(1).strip()
    
    # Disease resistance
    disease_match = re.search(r'(?:Field tolerance|Tolerant|Resistant)[^.]*', desc)
    if disease_match:
        disease_text = disease_match.group(0).strip()
        if 'disease' in disease_text.lower() or 'pest' in disease_text.lower() or 'lodging' in disease_text.lower() or 'blast' in disease_text.lower() or 'blb' in disease_text.lower():
            attrs['Disease/Pest Resistance'] = disease_text
    
    # Lodging tolerance
    lodging_match = re.search(r'(?:Tolerant|tolerance)\s+to\s+lodging', desc, re.IGNORECASE)
    if lodging_match and 'Disease/Pest Resistance' not in attrs:
        attrs['Lodging Tolerance'] = 'Yes'
    elif lodging_match:
        if 'Lodging Tolerance' not in attrs:
            attrs['Lodging Tolerance'] = 'Yes'
    
    # Specific diseases
    diseases = []
    if re.search(r'blast', desc, re.IGNORECASE):
        diseases.append('Blast')
    if re.search(r'BLB', desc):
        diseases.append('BLB')
    if re.search(r'false\s+smut', desc, re.IGNORECASE):
        diseases.append('False Smut')
    if re.search(r'bacterial\s+leaf', desc, re.IGNORECASE):
        diseases.append('Bacterial Leaf Blight')
    if diseases and 'Disease/Pest Resistance' not in attrs:
        attrs['Disease/Pest Resistance'] = f"Field tolerance to {', '.join(diseases)}"
    
    return attrs


def extract_features_from_description(desc):
    """Extract feature bullets from description."""
    features = []
    if not desc:
        return features
    
    # Split by bullet points (•, -, *)
    lines = re.split(r'[•\n]', desc)
    for line in lines:
        line = line.strip().strip('•-*').strip()
        if line and len(line) > 5:
            # Skip PDF link text
            if line.lower().endswith('.pdf') or line.startswith('http'):
                continue
            features.append(line)
    
    return features


def process_product(product, index, total):
    """Process a single product page."""
    url = product.get('url', '')
    name = product.get('name', '')
    code = product.get('code', '')
    
    print(f"[{index+1}/{total}] {name} ({url})")
    
    html = fetch_page(url)
    
    if not html:
        print(f"  FAILED: Could not fetch {url}")
        return {
            **product,
            'full_description': '',
            'short_description': product.get('short_description', ''),
            'attributes': {},
            'tags': product.get('tags', []),
            'features': [],
            'image_url': product.get('image_url', ''),
            'pdf_url': '',
            'has_real_pdf': False,
            'pdf_urls': [],
            'scrape_status': 'failed',
            'scrape_error': 'Could not fetch page'
        }
    
    extracted = extract_with_regex(html)
    
    if extracted['is_404']:
        print(f"  404: {url}")
        return {
            **product,
            'full_description': '',
            'short_description': product.get('short_description', ''),
            'attributes': {},
            'tags': product.get('tags', []),
            'features': [],
            'image_url': product.get('image_url', ''),
            'pdf_url': '',
            'has_real_pdf': False,
            'pdf_urls': [],
            'scrape_status': '404',
            'scrape_error': 'Page not found'
        }
    
    desc = extracted.get('short_description', '')
    pdf_urls = extracted.get('pdf_urls', [])
    
    # Also check for PDF URLs in the description text
    if not pdf_urls and desc:
        pdf_matches = re.findall(r'(https?://[^\s<>"]+\.pdf)', desc, re.IGNORECASE)
        pdf_urls.extend(pdf_matches)
    
    # Determine the real PDF URL
    pdf_url = ''
    has_real_pdf = False
    
    for pu in pdf_urls:
        if pu.lower().endswith('.pdf'):
            # Check if it actually returns a PDF
            is_real = has_real_pdf_header(pu)
            if is_real:
                pdf_url = pu
                has_real_pdf = True
                break
    
    # If we found PDF URLs but none returned PDF content-type, still use the first one
    if not has_real_pdf and pdf_urls:
        pdf_url = pdf_urls[0]
        # Still check if it looks like a real PDF path
        if '/uploads/' in pdf_url and pdf_url.lower().endswith('.pdf'):
            has_real_pdf = True
    
    # Extract attributes from description
    attributes = extract_attributes_from_description(desc)
    
    # Extract features
    features = extract_features_from_description(desc)
    
    # Merge categories from original and scraped
    categories = product.get('subcategories', []) if not extracted['categories'] else extracted['categories']
    main_category = product.get('category', '')
    if main_category and main_category not in categories:
        categories.insert(0, main_category)
    
    # Tags
    tags = extracted.get('tags', []) or product.get('tags', [])
    
    result = {
        'name': product.get('name', extracted.get('title', '')),
        'code': product.get('code', ''),
        'url': url,
        'category': product.get('category', ''),
        'subcategories': categories,
        'full_description': desc,
        'short_description': desc[:200] + '...' if len(desc) > 200 else desc,
        'attributes': attributes,
        'tags': tags,
        'features': features[:50],  # limit features
        'image_url': product.get('image_url', ''),
        'pdf_url': pdf_url,
        'pdf_urls': pdf_urls,
        'has_real_pdf': has_real_pdf,
        'scrape_status': 'success'
    }
    
    print(f"  OK: desc={len(desc)}chars, categories={categories}, tags={tags}, pdf={'YES' if has_real_pdf else 'no'}")
    
    return result


def save_progress(products, processed_count, output_path):
    """Save progress to JSON file."""
    progress = {
        'processed_count': processed_count,
        'total': len(products),
        'products': products,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)
    print(f"\nProgress saved: {processed_count}/{len(products)} products")


def generate_report(products):
    """Generate a summary report."""
    total = len(products)
    success = sum(1 for p in products if p.get('scrape_status') == 'success')
    failed = sum(1 for p in products if p.get('scrape_status') == 'failed')
    notfound = sum(1 for p in products if p.get('scrape_status') == '404')
    has_pdf = sum(1 for p in products if p.get('has_real_pdf'))
    has_desc = sum(1 for p in products if p.get('full_description', '').strip())
    has_attrs = sum(1 for p in products if p.get('attributes', {}))
    has_tags = sum(1 for p in products if p.get('tags', []))
    has_features = sum(1 for p in products if p.get('features', []))
    
    # Products missing key data
    missing_desc = [p['name'] for p in products if not p.get('full_description', '').strip() and p.get('scrape_status') == 'success']
    missing_pdf = [p['name'] for p in products if not p.get('has_real_pdf') and p.get('scrape_status') == 'success']
    
    print("\n" + "="*60)
    print("SCRAPE REPORT")
    print("="*60)
    print(f"Total products: {total}")
    print(f"Successfully scraped: {success}")
    print(f"Failed (connection/timeout): {failed}")
    print(f"Not found (404): {notfound}")
    print(f"")
    print(f"With full description: {has_desc}")
    print(f"With real PDF brochure: {has_pdf}")
    print(f"With attributes: {has_attrs}")
    print(f"With tags: {has_tags}")
    print(f"With features list: {has_features}")
    print(f"")
    
    if missing_desc:
        print(f"Products WITHOUT description ({len(missing_desc)}):")
        for m in missing_desc[:20]:
            print(f"  - {m}")
        if len(missing_desc) > 20:
            print(f"  ... and {len(missing_desc)-20} more")
    
    if missing_pdf:
        print(f"\nProducts WITHOUT PDF brochure ({len(missing_pdf)}):")
        for m in missing_pdf[:20]:
            print(f"  - {m}")
        if len(missing_pdf) > 20:
            print(f"  ... and {len(missing_pdf)-20} more")
    
    print("="*60)


def main():
    # Load input data
    print(f"Loading input from {INPUT_FILE}")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        input_data = json.load(f)
    
    products = input_data.get('products', [])
    total = len(products)
    print(f"Loaded {total} products")
    
    # Check for existing progress
    start_index = 0
    results = []
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                progress = json.load(f)
            if progress.get('total') == total:
                results = progress.get('products', [])
                start_index = progress.get('processed_count', 0)
                print(f"Resuming from product {start_index}/{total}")
        except:
            pass
    
    if start_index == 0:
        # Initialize results from existing data
        for p in products:
            results.append({
                'name': p.get('name', ''),
                'code': p.get('code', ''),
                'url': p.get('url', ''),
                'category': p.get('category', ''),
                'subcategories': p.get('subcategories', []),
                'full_description': '',
                'short_description': p.get('short_description', ''),
                'attributes': {},
                'tags': p.get('tags', []),
                'features': [],
                'image_url': p.get('image_url', ''),
                'pdf_url': '',
                'pdf_urls': [],
                'has_real_pdf': False,
                'scrape_status': 'pending'
            })
    
    # Process products in batches
    batch = []
    for i in range(start_index, total):
        if products[i].get('url', '').endswith('/aasma-tmwh-2786/'):
            print(f"Skipping known 404: {products[i]['url']}")
            results[i]['scrape_status'] = 'skipped_404'
            continue
            
        batch.append(i)
        
        if len(batch) >= BATCH_SIZE or i == total - 1:
            for idx in batch:
                result = process_product(products[idx], idx, total)
                results[idx] = result
            
            save_progress(results, i + 1, PROGRESS_FILE)
            batch = []
            time.sleep(0.5)  # Small delay between batches
    
    # Final save
    output = {
        'total_products': total,
        'site': 'https://trimurti.in',
        'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'products': results
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\nFinal output saved to {OUTPUT_FILE}")
    
    # Generate report
    generate_report(results)
    
    # Clean up progress file
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)

if __name__ == '__main__':
    main()
