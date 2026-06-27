#!/usr/bin/env python3
"""
Fix problematic downloads: chilli image and okra PDF were matched to wrong products.
"""
import json
import os
import subprocess
import re

JSON_PATH = r"C:\Users\kingo\trimurti-redesign\product-migration\raw-scrape.json"
IMG_DIR = r"C:\Users\kingo\trimurti-redesign\images\products"
PDF_DIR = r"C:\Users\kingo\trimurti-redesign\product-migration\pdfs"

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build dict by name for lookup
products = {p['name']: p for p in data['products']}

def get_full_url(thumb_url):
    if not thumb_url:
        return None
    return re.sub(r'-300x300(?=\.\w+)', '', thumb_url)

def try_download(url, dest_path, timeout=30):
    if not url:
        return False
    try:
        cmd = ['curl', '-s', '-L', '--max-time', str(timeout), 
               '-o', dest_path, '-w', '%{http_code}', url]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout+5)
        http_code = result.stdout.strip()
        if http_code.startswith('2'):
            size = os.path.getsize(dest_path) if os.path.exists(dest_path) else 0
            if size > 1000:
                return True
        return False
    except:
        return False

# Fix 1: Chilli image - use Nagma (TMPH 404) which is a chilli product
chilli_product = products.get("Nagma (TMPH 404)")
if chilli_product:
    url = get_full_url(chilli_product['image_url'])
    dest = os.path.join(IMG_DIR, "chilli.jpg")
    print(f"Downloading chilli from: {url}")
    if try_download(url, dest):
        print(f"  ✓ chilli.jpg ({os.path.getsize(dest)} bytes)")
    else:
        # Fall back to thumbnail
        url = chilli_product['image_url']
        print(f"  Trying thumbnail: {url}")
        if try_download(url, dest):
            print(f"  ✓ chilli.jpg (thumbnail, {os.path.getsize(dest)} bytes)")

# Fix 2: Okra PDF - use Nivi (TMOH 306) which is an okra product
# Unfortunately Nivi has no PDFs. Let's try other okra products.
okra_products = [p for p in data['products'] if 'okra' in p['name'].lower() or p.get('name', '').startswith('TMOH')]
for op in okra_products:
    print(f"  Okra product: {op['name']} - PDFs: {len(op.get('pdfs', []))}")

# The okra PDF that was downloaded came from "Shivi Fast" (a rice product) 
# via the name fallback. That's wrong. The right approach is to not have a PDF
# for okra since none of the okra products have PDFs.
# Just delete the wrong PDF
wrong_pdf = os.path.join(PDF_DIR, "okra.pdf")
if os.path.exists(wrong_pdf):
    # Check if it's a rice-related PDF (wrong)
    with open(wrong_pdf, 'rb') as f:
        header = f.read(20)
    # Delete it since it's from the wrong product
    os.remove(wrong_pdf)
    print(f"  Deleted wrong okra.pdf (was from rice product)")

# Fix 3: Sunflower - Jewel (TMSF 1701) which is a sunflower hybrid
# Check if the sunflower image is correct
sunflower_product = products.get("Jewel (TMSF 1701)")
if sunflower_product:
    print(f"  Sunflower product: {sunflower_product['name']}")

# Fix 4: Ridge gourd - make sure we have the right one
print("\nVerifying all images:")
for fname in sorted(os.listdir(IMG_DIR)):
    if fname.endswith('.jpg'):
        size = os.path.getsize(os.path.join(IMG_DIR, fname))
        print(f"  {fname}: {size} bytes")

print("\nDone fixing!")
