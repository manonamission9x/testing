#!/usr/bin/env python3
"""Final cleanup of a few remaining messy Duration values."""
import json, re

INPUT = r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json'

with open(INPUT, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Manual fixes for products where Duration regex still gets messy
manual_fixes = {
    'PR 126': 'Maturity duration: Kharif- 120-125 days',
    'SUVEER (TMMH 2882)': 'Maturity duration: Rabi 140-150 days',
    'TMMH 8418': None,  # Remove - not enough context
}

# Also fix any remaining durations > 100 chars
for p in data['products']:
    name = p['name']
    dur = p.get('attributes', {}).get('Duration', '')
    
    # Manual fix
    if name in manual_fixes:
        if manual_fixes[name]:
            p['attributes']['Duration'] = manual_fixes[name]
        else:
            del p['attributes']['Duration']
        continue
    
    # If still too long, try one more extraction
    if len(dur) > 100:
        desc = p.get('full_description', '')
        # Look for "Maturity duration:" format
        m = re.search(r'(Maturity\s+duration[^.]*\d+\s*[-–to]+\s*\d+\s*days)', desc)
        if m:
            p['attributes']['Duration'] = m.group(1).strip()
        else:
            # Just grab a simple X-Y days pattern
            m = re.search(r'(\d+\s*[-–to]+\s*\d+\s*days)', desc)
            if m:
                p['attributes']['Duration'] = m.group(1)
            else:
                del p['attributes']['Duration']

with open(INPUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
print('=== FINAL DURATION QUALITY ===')
problems = 0
for p in data['products']:
    dur = p.get('attributes', {}).get('Duration', '')
    if len(dur) > 100:
        print(f'  PROBLEM: {p["name"]}: {dur[:80]}... ({len(dur)} chars)')
        problems += 1

if problems == 0:
    print('  All durations are clean!')
else:
    print(f'  {problems} remaining problems')

# Final stats
dur_count = sum(1 for p in data['products'] if p.get('attributes', {}).get('Duration'))
print(f'  Products with Duration: {dur_count}/208')

# Show clean sample
print('\n=== CLEAN DURATIONS SAMPLE (last 10 fixed) ===')
for p in data['products']:
    name = p['name']
    if name in manual_fixes:
        print(f'  {name}: {p.get("attributes", {}).get("Duration", "N/A")}')
