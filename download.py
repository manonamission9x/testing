#!/usr/bin/env python3
"""
Download product images from old site.
Reads raw-scrape.json, downloads full-size images to images/products/.
Runs up to 3 parallel downloads at a time.
"""
import json
import os
import subprocess
import sys

BASE = r"C:\Users\kingo\trimurti-redesign"
SCRAPE_PATH = os.path.join(BASE, "product-migration", "raw-scrape.json")
IMAGE_DIR = os.path.join(BASE, "images", "products")

os.makedirs(IMAGE_DIR, exist_ok=True)

with open(SCRAPE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

def get_full_size_url(url):
    """Convert Smush CDN thumbnail URL to full-size URL by removing size suffixes."""
    if not url:
        return None
    # Strip query params
    base = url.split("?")[0]
    parts = base.rsplit(".", 1)
    if len(parts) != 2:
        return base
    name, ext = parts
    # Remove common size suffixes
    for suffix in ["-300x300", "-150x150", "-600x600", "-1024x1024", "-768x768", "_optimized", "-50x50"]:
        if name.endswith(suffix):
            name = name[:-len(suffix)]
            break
    return name + "." + ext

# Collect download tasks
tasks = []
for p in products:
    code = p.get("code", "").strip()
    image_url = p.get("image_url", "") or ""
    if code and image_url:
        tasks.append((image_url, f"{code}.jpg"))

print(f"Found {len(tasks)} images to download")

# Process in batches of 3
parallel = 3
success = 0
failed = 0
skipped = 0

for i in range(0, len(tasks), parallel):
    batch = tasks[i:i+parallel]
    processes = []
    
    for url, filename in batch:
        filepath = os.path.join(IMAGE_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
            skipped += 1
            continue
        
        full_url = get_full_size_url(url)
        if not full_url:
            failed += 1
            print(f"  SKIP: {filename} - no URL")
            continue
        
        cmd = [
            "curl", "-s", "-S", "-L",
            "--connect-timeout", "15",
            "--max-time", "30",
            "--retry", "2",
            "--retry-delay", "3",
            "-o", filepath,
            full_url
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append((proc, filename, filepath))
    
    for proc, filename, filepath in processes:
        try:
            stdout, stderr = proc.communicate(timeout=35)
            if proc.returncode == 0 and os.path.exists(filepath):
                size = os.path.getsize(filepath)
                if size > 100:
                    success += 1
                    print(f"  OK: {filename} ({size} bytes)")
                else:
                    if os.path.exists(filepath):
                        os.remove(filepath)
                    failed += 1
                    print(f"  FAIL: {filename} - too small ({size} bytes)")
            else:
                if os.path.exists(filepath):
                    os.remove(filepath)
                err_msg = stderr.decode().strip()[:80] if stderr else ""
                failed += 1
                print(f"  FAIL: {filename} - curl rc={proc.returncode} {err_msg}")
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            if os.path.exists(filepath):
                os.remove(filepath)
            failed += 1
            print(f"  FAIL: {filename} - timeout")
        except Exception as e:
            if os.path.exists(filepath):
                try: os.remove(filepath)
                except: pass
            failed += 1
            print(f"  FAIL: {filename} - {e}")
    
    done = i + parallel
    if done % 9 == 0 or done >= len(tasks):
        print(f"Progress: {min(done, len(tasks))}/{len(tasks)} (OK:{success} Fail:{failed} Skip:{skipped})")

print(f"\n=== Download Complete ===")
print(f"Total candidates: {len(tasks)}")
print(f"Success: {success}")
print(f"Failed: {failed}")
print(f"Skipped (already exist): {skipped}")

# Count existing images
existing_count = sum(1 for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f)))
print(f"Total images in {IMAGE_DIR}: {existing_count}")

sys.exit(0 if failed == 0 else 1)
