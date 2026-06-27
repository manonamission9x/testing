#!/usr/bin/env python3
"""
Download product images and PDFs from Trimurti old site for new site migration.
Maps scraped products to the new site's crop categories.
"""
import json
import os
import subprocess
import re
import shutil

# Paths
JSON_PATH = r"C:\Users\kingo\trimurti-redesign\product-migration\raw-scrape.json"
IMG_DIR = r"C:\Users\kingo\trimurti-redesign\images\products"
PDF_DIR = r"C:\Users\kingo\trimurti-redesign\product-migration\pdfs"
LOG_FILE = r"C:\Users\kingo\trimurti-redesign\product-migration\download-log.txt"

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

# Load data
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

products = {p.get('code', '').upper(): p for p in data['products']}
# Also index by name
products_by_name = {}
for p in data['products']:
    name_lower = p['name'].lower()
    products_by_name[name_lower] = p

# ============================================================
# MAPPING: new site crop ID -> list of product identifiers to try
# We pick the most representative products
# ============================================================
IMAGE_MAP = {
    # Field Crops
    'maize': ['TMMH846', 'TMMH826', 'TMMH807', 'TMMH801', 'TMMH812'],
    'rice': ['TMRH2106', 'TMRH106', 'TMRH5544', 'TMRH129', 'TMRH124'],
    'mustard': ['TMMD99', 'TM914', 'TMMD92', 'TMMD2904'],
    'bajra': ['TMBH633', 'TMBH680', 'TMBH2652', 'TMBH2631', 'TMBH601'],
    'jowar': ['TMSH1201', 'TMFH1208', 'TMFH1276'],  # sorghum-related
    'sunflower': ['TMSF1701'],  # Jewel
    'cotton': [],  # No cotton products in scraped data
    'green-gram': [],  # Not found
    'black-gram': [],  # Not found
    
    # Vegetables
    'tomato': ['TMTH222', 'TMTH208', 'TMTH205'],  # Abeesh, Diya, Rype
    'brinjal': ['TMBI1314', 'TMBI1301', 'TMBI1304'],  # Ayesha, Ista, Rishta
    'chilli': ['TMPH424', 'TMPH404', 'TMPH401'],
    'okra': ['TMOH306', 'TMOH303', 'TMOH307'],
    'bottle-gourd': ['TMBG1409', 'TMBG3402', 'TMBG1401'],
    'ridge-gourd': ['TMSG1602', 'TMSG1601', 'TMSG3615'],
    'cabbage': [],  # Not found
    'cauliflower': ['TMCA21006', 'TMCA21009'],
    'cucumber': ['TMCU1101', 'TMCU1111', 'TMCU3102'],
    'watermelon': ['TMWH2786', 'TMWH2741', 'TMWH701'],
    
    # Fodder
    'maize-fodder': ['TMMH2838'],  # Fodder (TMMH2838)
    'sorghum-fodder': ['TMSH1201', 'TMFH1208', 'TMFH3211', 'TMFH3206'],
    'cowpea-fodder': [],  # Not found in scraped data
}

# Also add fallback by name matching
NAME_FALLBACKS = {
    'mustard': ['ustaad', 'ghungroo', 'julie', 'kaalia', 'kashinath'],
    'sunflower': ['jewel'],
    'tomato': ['abeesh', 'diya', 'chamki', 'holi', 'rype'],
    'brinjal': ['ayesha', 'ista', 'rishta', 'tanu'],
    'chilli': ['nagma', 'jhalak', 'klik', 'purvi'],
    'okra': ['nivi', 'shivi'],
    'bottle-gourd': ['ila', 'sarla', 'veena'],
    'ridge-gourd': ['rumi', 'tanya'],
    'cauliflower': ['white lily'],
    'cucumber': ['hema', 'inam'],
    'watermelon': ['aasma', 'balma', 'isha', 'ishq', 'kaabil', 'kaalia gold'],
    'maize-fodder': ['fodder'],
    'sorghum-fodder': ['charu', 'samata', 'sweet fora'],
    'cowpea-fodder': [],
}

log_lines = []

def log(msg):
    print(msg)
    log_lines.append(msg)

def get_full_url(thumb_url):
    """Try to get full-size URL by removing -300x300 from filename"""
    if not thumb_url:
        return None
    # Remove the -300x300 before file extension
    full_url = re.sub(r'-300x300(?=\.\w+)', '', thumb_url)
    # Also try removing query params and trying without them
    return full_url

def try_download(url, dest_path, timeout=30, follow_redirects=True):
    """Try to download a file, return True if successful"""
    if not url:
        return False
    try:
        cmd = ['curl', '-s', '-L' if follow_redirects else '', '--max-time', str(timeout), 
               '-o', dest_path, '-w', '%{http_code}', url]
        cmd = [c for c in cmd if c]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout+5)
        http_code = result.stdout.strip()
        if http_code.startswith('2'):
            # Check if it's actually an image (not HTML error page)
            size = os.path.getsize(dest_path) if os.path.exists(dest_path) else 0
            if size > 1000:  # At least 1KB
                return True
        return False
    except Exception as e:
        return False

def download_image_for_crop(crop_id, dest_filename):
    """Try to download a representative image for a crop"""
    dest_path = os.path.join(IMG_DIR, dest_filename)
    
    # 1. Try by product code
    codes = IMAGE_MAP.get(crop_id, [])
    for code in codes:
        if code in products:
            p = products[code]
            thumb_url = p.get('image_url', '')
            if thumb_url:
                # Try full size first
                full_url = get_full_url(thumb_url)
                log(f"  Trying full-size URL: {full_url}")
                if try_download(full_url, dest_path):
                    log(f"  ✓ Downloaded full-size to {dest_filename}")
                    return True
                # Fall back to thumbnail
                log(f"  Trying thumbnail: {thumb_url}")
                if try_download(thumb_url, dest_path):
                    log(f"  ✓ Downloaded thumbnail to {dest_filename}")
                    return True
    
    # 2. Try by name fallback
    names = NAME_FALLBACKS.get(crop_id, [])
    for name_key in names:
        for p_name, p in products_by_name.items():
            if name_key in p_name:
                thumb_url = p.get('image_url', '')
                if thumb_url:
                    full_url = get_full_url(thumb_url)
                    log(f"  Trying (name fallback) full-size: {full_url}")
                    if try_download(full_url, dest_path):
                        log(f"  ✓ Downloaded to {dest_filename}")
                        return True
                    if try_download(thumb_url, dest_path):
                        log(f"  ✓ Downloaded thumbnail to {dest_filename}")
                        return True
    
    log(f"  ✗ Could not download image for {crop_id}")
    return False

def download_pdf_for_crop(crop_id):
    """Try to download PDFs for a crop"""
    dest_filename = f"{crop_id}.pdf"
    dest_path = os.path.join(PDF_DIR, dest_filename)
    
    codes = IMAGE_MAP.get(crop_id, [])
    for code in codes:
        if code in products:
            p = products[code]
            pdfs = p.get('pdfs', [])
            if pdfs:
                pdf_url = pdfs[0]['url']
                log(f"  Trying PDF: {pdf_url}")
                if try_download(pdf_url, dest_path):
                    log(f"  ✓ Downloaded PDF to {dest_filename}")
                    return True
    
    # Try name fallback
    names = NAME_FALLBACKS.get(crop_id, [])
    for name_key in names:
        for p_name, p in products_by_name.items():
            if name_key in p_name:
                pdfs = p.get('pdfs', [])
                if pdfs:
                    pdf_url = pdfs[0]['url']
                    log(f"  Trying (name fallback) PDF: {pdf_url}")
                    if try_download(pdf_url, dest_path):
                        log(f"  ✓ Downloaded PDF to {dest_filename}")
                        return True
    
    log(f"  - No PDF found for {crop_id}")
    return False


# ============================================================
# Main download process
# ============================================================
log("=" * 70)
log("TRIMURTI PRODUCT IMAGE & PDF DOWNLOADER")
log("=" * 70)
log(f"Image target: {IMG_DIR}")
log(f"PDF target: {PDF_DIR}")
log("")

# Categories from new site
categories = {
    'field-crops': ['maize', 'rice', 'mustard', 'bajra', 'jowar', 'sunflower', 'cotton', 'green-gram', 'black-gram'],
    'vegetables': ['tomato', 'brinjal', 'chilli', 'okra', 'bottle-gourd', 'ridge-gourd', 'cabbage', 'cauliflower', 'cucumber', 'watermelon'],
    'fodder': ['maize-fodder', 'sorghum-fodder', 'cowpea-fodder']
}

total_images = 0
total_pdfs = 0
failed = []

for cat, crops in categories.items():
    log(f"\n--- {cat.upper()} ---")
    for crop_id in crops:
        img_filename = f"{crop_id}.jpg"
        log(f"\n[{crop_id}]")
        
        # Check if already exists
        img_path = os.path.join(IMG_DIR, img_filename)
        if os.path.exists(img_path) and os.path.getsize(img_path) > 1000:
            log(f"  Already exists, skipping image")
        else:
            success = download_image_for_crop(crop_id, img_filename)
            if success:
                total_images += 1
            else:
                failed.append(crop_id)
        
        pdf_path = os.path.join(PDF_DIR, f"{crop_id}.pdf")
        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
            log(f"  PDF already exists, skipping")
        else:
            if download_pdf_for_crop(crop_id):
                total_pdfs += 1

log("\n" + "=" * 70)
log("SUMMARY")
log("=" * 70)
log(f"Images downloaded: {total_images}")
log(f"PDFs downloaded: {total_pdfs}")
log(f"Failed: {len(failed)}")
for f in failed:
    log(f"  - {f}")

# Write log
with open(LOG_FILE, 'w') as f:
    f.write('\n'.join(log_lines))

log(f"\nLog written to: {LOG_FILE}")
print("\nDone!")
