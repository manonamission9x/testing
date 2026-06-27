#!/usr/bin/env python3
"""Verify the detailed scrape output."""
import json

with open(r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find a product with real PDF
for p in data['products']:
    if p['has_real_pdf'] and p['pdf_url']:
        print(f'=== {p["name"]} ===')
        print(f'PDF URL: {p["pdf_url"]}')
        print(f'Has real PDF: {p["has_real_pdf"]}')
        print(f'Categories: {p["subcategories"]}')
        print(f'Tags: {p["tags"]}')
        print(f'Attributes: {json.dumps(p["attributes"], indent=2)}')
        print(f'Features: {len(p["features"])} features')
        print(f'Desc length: {len(p["full_description"])}')
        print()
        break

# Count stats
has_pdf = sum(1 for p in data['products'] if p['has_real_pdf'])
no_pdf = sum(1 for p in data['products'] if not p['has_real_pdf'])
has_attrs = sum(1 for p in data['products'] if p.get('attributes', {}))
has_tags = sum(1 for p in data['products'] if p.get('tags', []))
has_features = sum(1 for p in data['products'] if p.get('features', []))

print('=== QUALITY STATS ===')
print(f'Total: {len(data["products"])}')
print(f'With PDF: {has_pdf}')
print(f'Without PDF: {no_pdf}')
print(f'With attributes: {has_attrs}')
print(f'With tags: {has_tags}')
print(f'With features: {has_features}')

# Check 404 products
not_found = [p for p in data['products'] if p.get('scrape_status') == '404' or p.get('scrape_status') == 'skipped_404']
print(f'404/skipped pages: {len(not_found)}')
for p in not_found:
    print(f'  - {p["name"]} ({p["url"]})')

# Check tag quality
all_tags = set()
for p in data['products']:
    for t in p.get('tags', []):
        all_tags.add(t)
print(f'Unique tags: {sorted(all_tags)}')

# Sample some attributes
print('\n=== SAMPLE ATTRIBUTES ===')
count = 0
for p in data['products']:
    if p.get('attributes', {}):
        attrs = p['attributes']
        if 'Duration' in attrs:
            duration = attrs['Duration']
            if len(duration) < 100:
                print(f'{p["name"]}: Duration={duration}')
            else:
                print(f'{p["name"]}: Duration=[too long: {len(duration)}chars]')
        count += 1
        if count >= 10:
            break

# Products where PDF == image
print('\n=== PDF-IMAGE COMPARISON ===')
count = 0
for p in data['products']:
    if p.get('pdf_url') and p.get('image_url'):
        # Check if PDF URL is actually an image
        pdf_lower = p['pdf_url'].lower()
        img_lower = p['image_url'].lower()
        # Extract paths
        from urllib.parse import urlparse
        pdf_path = urlparse(pdf_lower).path
        img_path = urlparse(img_lower).path
        if pdf_path == img_path:
            print(f'{p["name"]}: PDF == Image! {pdf_path}')
            count += 1

print(f'Products where PDF == Image URL: {count}')
