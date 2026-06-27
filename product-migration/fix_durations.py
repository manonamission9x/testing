#!/usr/bin/env python3
"""Fix remaining Duration attribute issues and clean up one more time."""
import json, re

INPUT = r'C:\Users\kingo\trimurti-redesign\product-migration\detailed-scrape.json'

with open(INPUT, 'r', encoding='utf-8') as f:
    data = json.load(f)

def extract_clean_duration(desc):
    """Extract ONLY the specific duration text, not whole sentences."""
    if not desc:
        return ''
    
    # Strategy: find a compact "X-Y days" reference with context
    
    # Pattern: "Kharif: 120-125 days" or "Rabi: 125-130 days" or "Spring: 100-105 days"
    m = re.search(r'((?:Kharif|Rabi|Spring|Zaid)\s*:\s*\d+\s*[-–to]+\s*\d+\s*days)', desc, re.IGNORECASE)
    if m:
        return m.group(1)
    
    # Pattern: "Kharif: 105-110 days, Rabi: 120-130 days (AP & TG) and 140-150 days (Bihar) & Spring: 100-105 days"
    m = re.search(r'(Kharif\s*:\s*\d+\s*[-–to]+\s*\d+\s*days[^)]*?(?:Rabi|Spring)[^)]*?(?:\d+\s*[-–to]+\s*\d+\s*days))', desc, re.IGNORECASE)
    if m:
        result = m.group(1).strip()
        # Clean up
        result = re.sub(r'\s+', ' ', result)
        if len(result) < 150:
            return result
    
    # Pattern: "90-100 days" (simple case)
    m = re.search(r'(\d+\s*[-–to]+\s*\d+\s*days)', desc)
    if m:
        dur = m.group(1)
        # Find context: look behind up to 30 chars for maturity info
        start = max(0, desc.find(dur) - 40)
        context = desc[start:desc.find(dur) + len(dur)].strip()
        # Clean context
        context = re.sub(r'^[^a-zA-Z\d]*', '', context)
        context = context.strip('•-(').strip()
        if len(context) < 80:
            return context
        return dur
    
    # Pattern: "120-125 days" with maturity nearby
    m = re.search(r'(matur(?:ing|ity)[^.]*?\d+\s*[-–to]+\s*\d+\s*days)', desc, re.IGNORECASE)
    if m:
        result = m.group(1).strip()
        result = re.sub(r'\s+', ' ', result)
        if len(result) < 100:
            return result
    
    # Pattern: handle cases like "Maturity duration: Kharif- 120-125 days" where text before is "ld potential"
    m = re.search(r'(Maturity[^.]*\d+\s*[-–to]+\s*\d+\s*days)', desc, re.IGNORECASE)
    if m:
        result = m.group(1).strip()
        result = re.sub(r'\s+', ' ', result)
        if len(result) < 100:
            return result
    
    return ''

# Fix all durations
fixed_count = 0
for p in data['products']:
    if 'Duration' in p.get('attributes', {}):
        old_dur = p['attributes']['Duration']
        if len(old_dur) > 100:
            new_dur = extract_clean_duration(p.get('full_description', ''))
            if new_dur:
                p['attributes']['Duration'] = new_dur
                fixed_count += 1
            else:
                # Last resort: find any "X-Y days" in desc
                desc = p.get('full_description', '')
                m = re.search(r'(\d+\s*[-–to]+\s*\d+\s*days)', desc)
                if m:
                    p['attributes']['Duration'] = m.group(1)
                    fixed_count += 1

# Also fix products without Duration but with descriptions containing maturity info
for p in data['products']:
    if 'Duration' not in p.get('attributes', {}):
        desc = p.get('full_description', '')
        dur = extract_clean_duration(desc)
        if dur:
            if 'attributes' not in p:
                p['attributes'] = {}
            p['attributes']['Duration'] = dur
            fixed_count += 1

with open(INPUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Fixed {fixed_count} products')
print(f'Total with Duration: {sum(1 for p in data["products"] if p.get("attributes", {}).get("Duration"))}')

# Check remaining bad durations
bad = [(p['name'], p.get('attributes', {}).get('Duration','')) for p in data['products'] if len(p.get('attributes', {}).get('Duration','')) > 100]
print(f'Remaining bad durations: {len(bad)}')
for name, dur in bad[:10]:
    print(f'  {name}: {dur[:80]}... ({len(dur)} chars)')

# Show some fixed
print('\n=== FIXED DURATIONS ===')
with open(INPUT, 'r', encoding='utf-8') as f:
    data2 = json.load(f)
for p in data2['products']:
    dur = p.get('attributes', {}).get('Duration', '')
    if dur and len(dur) < 100 and len(dur) > 5:
        print(f'  {p["name"]}: {dur}')
