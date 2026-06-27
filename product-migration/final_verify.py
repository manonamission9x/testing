#!/usr/bin/env python3
"""Final verification of the detailed scrape output."""
import json, os

with open(r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json', 'r') as f:
    data = json.load(f)

size = os.path.getsize(r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json')
print(f'File size: {size:,} bytes ({size/1024:.0f} KB)')
print(f'Products: {len(data["products"])}')

all_have_name = all(p.get('name') for p in data['products'])
all_have_url = all(p.get('url') for p in data['products'])
all_have_desc = all(p.get('full_description') is not None for p in data['products'])
print(f'All have name: {all_have_name}')
print(f'All have url: {all_have_url}')
print(f'All have description field: {all_have_desc}')

with_desc = sum(1 for p in data['products'] if p.get('full_description', '').strip())
with_pdf_url = sum(1 for p in data['products'] if p.get('pdf_url'))
real_pdf = sum(1 for p in data['products'] if p.get('has_real_pdf'))
print(f'With non-empty description: {with_desc}')
print(f'With pdf_url set: {with_pdf_url}')
print(f'With has_real_pdf=True: {real_pdf}')

bad_durations = []
for p in data['products']:
    dur = p.get('attributes', {}).get('Duration', '')
    if dur and len(dur) > 100:
        bad_durations.append((p['name'], len(dur)))
if bad_durations:
    print(f'Bad (too long) durations: {len(bad_durations)}')
    for name, length in bad_durations[:5]:
        print(f'  {name}: {length} chars')
else:
    print('All durations are clean (under 100 chars)!')

print()
print('=== FINAL SAMPLE PRODUCTS ===')
for p in data['products'][:2]:
    print(f'Name: {p["name"]}')
    print(f'  URL: {p["url"]}')
    print(f'  Category: {p["category"]}')
    print(f'  Subcategories: {p["subcategories"]}')
    print(f'  Tags: {p["tags"]}')
    print(f'  PDF: {p["pdf_url"][:80] if p["pdf_url"] else "(none)"}')
    print(f'  Attributes: {json.dumps(p["attributes"], indent=4)}')
    print(f'  Features: {len(p["features"])} items')
    print(f'  Desc: {p["full_description"][:100]}...')
    print()
