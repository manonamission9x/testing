#!/usr/bin/env python3
"""Final comprehensive quality verification."""
import json, os

with open(r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json', 'r') as f:
    data = json.load(f)

size = os.path.getsize(r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json')
print(f'{"="*60}')
print(f'FINAL QUALITY REPORT')
print(f'{"="*60}')
print(f'Output file: {size:,} bytes ({size/1024:.0f} KB)')
print(f'Total products: {len(data["products"])}')
print()

# Field quality
fields = {
    'name': 'Product name',
    'url': 'Product URL',
    'category': 'Category',
    'full_description': 'Full description',
    'attributes': 'Product attributes',
    'tags': 'Tags',
    'features': 'Features list',
    'image_url': 'Image URL',
    'pdf_url': 'PDF URL',
    'has_real_pdf': 'Has real PDF flag',
    'scrape_status': 'Scrape status'
}

for field, label in fields.items():
    present = sum(1 for p in data['products'] if field in p)
    print(f'  {label}: {present}/208 ({present*100//208}%)')

print()

# Content quality
with_desc = sum(1 for p in data['products'] if p.get('full_description', '').strip())
with_pdf = sum(1 for p in data['products'] if p.get('has_real_pdf'))
with_attrs = sum(1 for p in data['products'] if p.get('attributes', {}))
with_tags = sum(1 for p in data['products'] if p.get('tags', []))
with_features = sum(1 for p in data['products'] if p.get('features', []))
with_duration = sum(1 for p in data['products'] if p.get('attributes', {}).get('Duration'))
with_season = sum(1 for p in data['products'] if p.get('attributes', {}).get('Season'))

print(f'  Non-empty descriptions: {with_desc}/208')
print(f'  Real PDF brochures: {with_pdf}/208')
print(f'  With attributes: {with_attrs}/208')
print(f'  With tags: {with_tags}/208')
print(f'  With features list: {with_features}/208')
print(f'  With Duration attribute: {with_duration}/208')
print(f'  With Season attribute: {with_season}/208')
print()

# Check for any anomalies
print(f'{"-"*60}')
print(f'ANOMALIES / NEEDS REVIEW')
print(f'{"-"*60}')

no_tags = [p['name'] for p in data['products'] if not p.get('tags', [])]
no_pdf = [p['name'] for p in data['products'] if not p.get('has_real_pdf') and p.get('scrape_status') == 'success']
no_attrs = [p['name'] for p in data['products'] if not p.get('attributes', {})]

if no_tags:
    print(f'\nProducts without tags ({len(no_tags)}):')
    for n in no_tags[:15]:
        print(f'  - {n}')
    if len(no_tags) > 15:
        print(f'  ... and {len(no_tags)-15} more')

if no_pdf:
    print(f'\nProducts without PDF brochure ({len(no_pdf)}):')
    for n in no_pdf[:15]:
        print(f'  - {n}')
    if len(no_pdf) > 15:
        print(f'  ... and {len(no_pdf)-15} more')

# Duration quality
bad_dur = [(p['name'], p.get('attributes', {}).get('Duration','')) for p in data['products'] if len(p.get('attributes', {}).get('Duration','')) > 100]
if bad_dur:
    print(f'\nProducts with overly long Duration ({len(bad_dur)}):')
    for n, d in bad_dur[:5]:
        print(f'  - {n}: {d[:100]}...')

print(f'\n{"="*60}')
print(f'SCRAPE COMPLETE')
print(f'{"="*60}')
