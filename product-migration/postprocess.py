#!/usr/bin/env python3
"""Post-process the detailed scrape: clean up attributes, deduplicate categories, improve data quality."""
import json
import re
from urllib.parse import urlparse

INPUT = r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json'
OUTPUT = r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json'

with open(INPUT, 'r', encoding='utf-8') as f:
    data = json.load(f)

def clean_duration(desc):
    """Extract a clean duration string from the description."""
    if not desc:
        return ''
    
    # Priority: look for specific duration patterns
    patterns = [
        # "Full season maturity [Kharif: 105-110 days, Rabi: 120-130 days ...]"
        r'(Full\s+season\s+matur(?:ity|ing)\s*[^.]*\d+\s*[-–to]+\s*\d+\s*days[^.]*\.)',
        # "Early maturing (Kharif: 115-120 days) ..."
        r'((?:Early|Medium|Mid[\s-]*early|Full\s+season|Mid[\s-]*late)\s+matur(?:ing|ity)\s*[^.]*\d+\s*[-–to]+\s*\d+\s*days[^.]*\.)',
        # "Maturity duration – Kharif: 120-125 days and Rabi: 125-130 days"
        r'(Maturity\s+duration[^.]*\d+\s*[-–to]+\s*\d+\s*days[^.]*\.)',
        # "Kharif: 90-100 days" or "Rabi: 120-130 days"
        r'((?:Kharif|Rabi|Spring)\s*:\s*\d+\s*[-–to]+\s*\d+\s*days)',
        # Just "90-100 days"
        r'((?:\d+\s*[-–to]+\s*\d+\s*days)\s+(?:hybrid|variety))',
        # "120-130 days" at start of a sentence
        r'(^\s*\d+\s*[-–to]+\s*\d+\s*days)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, desc, re.IGNORECASE | re.MULTILINE)
        if match:
            dur = match.group(1).strip()
            # Clean up
            dur = re.sub(r'\s+', ' ', dur)
            return dur
    
    # Fallback: find a clean "X-Y days" reference near "maturity" or "maturing"
    lines = desc.split('\n')
    for line in lines:
        if re.search(r'(matur|duration|:)\s*\d+\s*[-–]\s*\d+\s*days', line, re.IGNORECASE):
            return line.strip().strip('•- ').strip()
    
    # Last resort: find any "X-Y days" pattern
    match = re.search(r'(\d+\s*[-–to]+\s*\d+\s*days)', desc)
    if match:
        # Find the line containing it
        for line in lines:
            if match.group(1) in line:
                return line.strip().strip('•- ').strip()
    
    return ''

def clean_suitability(desc):
    """Extract clean suitability/region info."""
    if not desc:
        return ''
    match = re.search(r'(?:Suitable for|Ideal for|Widely adapted for|Recommended for)[^.]*\.', desc)
    if match:
        return match.group(0).strip()
    return ''

def clean_disease_resistance(desc):
    """Extract clean disease/pest resistance info."""
    if not desc:
        return ''
    # Try to find "Field tolerance" sentence
    for pattern in [
        r'(Field\s+tolerance\s+to[^.]*\.)',
        r'(Tolerant\s+to\s+(?:lodging|major|pests)[^.]*\.)',
        r'(Resistant\s+to[^.]*\.)',
    ]:
        match = re.search(pattern, desc, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ''

def clean_grain_type(desc):
    """Extract clean grain type."""
    if not desc:
        return ''
    match = re.search(r'((?:Extra[\s-]*long|Long|Medium|Short)\s+(?:slender|bold|fine|basmati)[^.]*grains?)', desc, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    # Simpler: "Medium bold grains"
    match = re.search(r'(Medium\s+(?:slender|bold|fine)\s+grains?)', desc, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ''

for p in data['products']:
    desc = p.get('full_description', '')
    
    # 1. Clean up Duration attribute
    if 'Duration' in p.get('attributes', {}):
        old_dur = p['attributes']['Duration']
        clean_dur = clean_duration(desc)
        if clean_dur:
            p['attributes']['Duration'] = clean_dur
        else:
            # Try to grab just the first line with days from description
            lines = desc.split('\n')
            for line in lines[:5]:
                if re.search(r'\d+\s*[-–to]+\s*\d+\s*days', line):
                    p['attributes']['Duration'] = line.strip().strip('•- ').strip()
                    break
    
    # 2. Clean up Suitability
    if 'Suitability' in p.get('attributes', {}):
        clean_suit = clean_suitability(desc)
        if clean_suit:
            p['attributes']['Suitability'] = clean_suit
    
    # 3. Clean up Disease/Pest Resistance
    if 'Disease/Pest Resistance' in p.get('attributes', {}):
        clean_dpr = clean_disease_resistance(desc)
        if clean_dpr:
            p['attributes']['Disease/Pest Resistance'] = clean_dpr
    
    # 4. Clean up Grain Type
    if 'Grain Type' in p.get('attributes', {}):
        clean_gt = clean_grain_type(desc)
        if clean_gt:
            p['attributes']['Grain Type'] = clean_gt
    
    # 5. Deduplicate subcategories (handle case-insensitive duplicates)
    if 'subcategories' in p:
        seen = set()
        deduped = []
        for cat in p['subcategories']:
            key = cat.lower().strip()
            if key not in seen:
                seen.add(key)
                deduped.append(cat)
        p['subcategories'] = deduped
    
    # 6. Ensure category field is populated
    if not p.get('category') and p.get('subcategories'):
        p['category'] = p['subcategories'][0]
    
    # 7. Clean up Plant Height
    if 'Plant Height' in p.get('attributes', {}):
        ph = p['attributes']['Plant Height']
        ph = ph.strip()
        if not re.search(r'\d+\s*cm', ph):
            # Try to find it in description
            match = re.search(r'(\d+\s*[-–to]+\s*\d+\s*cm\s+(?:plant\s+)?height)', desc, re.IGNORECASE)
            if match:
                p['attributes']['Plant Height'] = match.group(1).strip()
    
    # 8. Clean features (remove empty/duplicate)
    if 'features' in p:
        seen_feat = set()
        cleaned = []
        for feat in p['features']:
            key = feat.lower().strip()
            if key and key not in seen_feat:
                seen_feat.add(key)
                cleaned.append(feat)
        p['features'] = cleaned

# Save
with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Post-processed data saved to {OUTPUT}')

# Print quality summary
has_duration = sum(1 for p in data['products'] if p.get('attributes', {}).get('Duration'))
has_season = sum(1 for p in data['products'] if p.get('attributes', {}).get('Season'))
has_region = sum(1 for p in data['products'] if p.get('attributes', {}).get('Region'))
has_height = sum(1 for p in data['products'] if p.get('attributes', {}).get('Plant Height'))
has_grain = sum(1 for p in data['products'] if p.get('attributes', {}).get('Grain Type'))
has_disease = sum(1 for p in data['products'] if p.get('attributes', {}).get('Disease/Pest Resistance'))
has_yield = sum(1 for p in data['products'] if p.get('attributes', {}).get('Yield'))

print('\n=== POST-PROCESSED ATTRIBUTE STATS ===')
print(f'With Duration: {has_duration}')
print(f'With Season: {has_season}')
print(f'With Region: {has_region}')
print(f'With Plant Height: {has_height}')
print(f'With Grain Type: {has_grain}')
print(f'With Disease/Pest Resistance: {has_disease}')
print(f'With Yield: {has_yield}')

# Show some cleaned durations
print('\n=== CLEANED DURATIONS (sample) ===')
count = 0
for p in data['products']:
    if p.get('attributes', {}).get('Duration'):
        dur = p['attributes']['Duration']
        if len(dur) < 120:
            print(f'  {p["name"]}: {dur}')
            count += 1
            if count >= 15:
                break

# Products needing manual review (missing key data)
print('\n=== PRODUCTS NEEDING MANUAL REVIEW ===')
for p in data['products']:
    issues = []
    if not p.get('full_description', '').strip():
        issues.append('no description')
    if not p.get('has_real_pdf'):
        issues.append('no PDF')
    if not p.get('attributes', {}).get('Duration') and not p.get('attributes', {}).get('Season'):
        issues.append('no key attributes')
    if not p.get('tags'):
        issues.append('no tags')
    if issues:
        print(f'  {p["name"]}: {", ".join(issues)}')
