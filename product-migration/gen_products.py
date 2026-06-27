#!/usr/bin/env python3
"""
Generate products-data.js with all 208 products + download images script.
Reads raw-scrape.json and produces products-data.js.
"""
import json
import re
import os

BASE = r"C:\Users\kingo\trimurti-redesign"
SCRAPE_PATH = os.path.join(BASE, "product-migration", "raw-scrape.json")
OUTPUT_PATH = os.path.join(BASE, "products-data.js")

with open(SCRAPE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

products_raw = data["products"]
print(f"Total raw products: {len(products_raw)}")

CAT_MAP = {"Field Crops": "field-crops", "Vegetables": "vegetables", "Fodder": "fodder"}

def determine_type(code, name):
    if not code:
        code = ""
    cu = code.upper()
    hybrid_pfx = ["TMMH", "TMRH", "TMBH", "TMWH", "TMTH", "TMPH", "TMOH",
                   "TMBI", "TMBG", "TMCU", "TMSG", "TMPU", "TMCA", "TMCH",
                   "TMSH", "TMFH", "TMW"]
    variety_pfx = ["TMRV", "TMMD", "TMOV"]
    for p in hybrid_pfx:
        if cu.startswith(p): return "Hybrid"
    for p in variety_pfx:
        if cu.startswith(p): return "Variety"
    if cu.startswith("TMRV") or cu.startswith("TMMD") or cu.startswith("TMOV"):
        return "Variety"
    if "TM" in cu[:4]:
        return "Hybrid"
    return "Hybrid"

def clean_desc(desc):
    if not desc or not desc.strip():
        return ""
    desc = desc.replace("&amp;", "&").replace("&#8211;", "-").replace("&#038;", "&")
    desc = desc.replace("&gt;", ">").replace("&lt;", "<")
    desc = desc.replace("&#8217;", "'").replace("&#8220;", '"').replace("&#8221;", '"')
    if len(desc) > 100:
        desc = desc[:97] + "..."
    return desc.strip()

def make_features(desc):
    if not desc:
        return []
    bullets = re.findall(r'•\s*([^•\n]+)', desc)
    if bullets:
        return [b.strip()[:80] for b in bullets[:6]]
    return []

# Build the 22 aggregate products (EXACTLY as they were)
existing = [
    # field-crops 1-9
    {"id":"maize","name":"Maize","category":"field-crops","type":"Hybrid","code":"TMR-MZ","active":True,"order":1,"detailPage":True,"description":"High-yielding biotech and conventional maize hybrids for Kharif and Rabi seasons. Strong pest tolerance and excellent grain quality.","image":"images/products/maize.jpg","features":["Biotech & conventional options","Kharif & Rabi seasons","Excellent stay-green trait","High shelling percentage"],"region":"Central & Southern India","season":"Kharif / Rabi","duration":"95-115 days","special":"Pest tolerant, drought tolerance","pdf":"brochures/maize.pdf","markets":"India, Nepal","hybrids":[{"name":"Nagma","desc":"Biotech Hybrid — Kharif"},{"name":"TMRH-1422","desc":"Biotech Hybrid — Rabi"},{"name":"TMRH-871","desc":"Conventional Hybrid"}]},
    {"id":"rice","name":"Rice","category":"field-crops","type":"Hybrid","code":"TMR-RC","active":True,"order":2,"detailPage":True,"description":"Premium rice hybrids across early, medium, and late duration groups. Long slender grains with excellent cooking quality.","image":"images/products/rice.jpg","features":["Long slender grains","Multiple maturity groups","High tillering","Good grain quality"],"region":"All major rice-growing regions","season":"Kharif","duration":"100-145 days","special":"High yield potential","pdf":"brochures/rice.pdf","markets":"India, Nepal","hybrids":[{"name":"TMRH-221","desc":"Early Duration (100-110 days)"},{"name":"TMRH-335","desc":"Medium Duration (120-130 days)"},{"name":"TMRH-448","desc":"Late Duration (140-145 days)"}]},
    {"id":"mustard","name":"Mustard","category":"field-crops","type":"Hybrid","code":"TMR-MS","active":True,"order":3,"detailPage":True,"description":"High oil content mustard hybrids with excellent pod load and disease tolerance. Suitable for rainfed and irrigated conditions.","image":"images/products/mustard.jpg","features":["Oil content 42-45%","Pod shattering tolerance","Good meal quality","Aphid tolerance"],"region":"Central & Northern India","season":"Rabi","duration":"85-120 days","special":"High oil content","pdf":"brochures/mustard.pdf","markets":"India","hybrids":[{"name":"TMRH-511","desc":"Early Hybrid (100-110 days)"},{"name":"TMRH-622","desc":"High Yield Hybrid (115-120 days)"},{"name":"TMRH-733","desc":"Short Duration Hybrid (85-95 days)"}]},
    {"id":"bajra","name":"Bajra (Pearl Millet)","category":"field-crops","type":"Hybrid","code":"TMR-BJ","active":True,"order":4,"detailPage":True,"description":"Drought-tolerant pearl millet hybrids for rainfed and dryland conditions. Excellent grain filling and dual-purpose options.","image":"images/products/bajra.jpg","features":["Drought tolerance","Dual-purpose options","Good grain quality","Downy mildew tolerance"],"region":"Arid & Semi-arid zones","season":"Kharif","duration":"75-90 days","special":"Drought tolerant","pdf":"brochures/bajra.pdf","markets":"India","hybrids":[{"name":"TMRB-101","desc":"Drought Tolerant Hybrid"},{"name":"TMRB-202","desc":"Dual Purpose Hybrid"}]},
    {"id":"jowar","name":"Jowar (Sorghum)","category":"field-crops","type":"Hybrid","code":"TMR-JW","active":True,"order":5,"detailPage":True,"description":"Grain and dual-purpose sorghum hybrids with bold, lustrous grains. Excellent threshing recovery and fodder quality.","image":"images/products/jowar.jpg","features":["Bold, white grains","Dual-purpose options","Shoot fly tolerance","High biomass"],"region":"Central & Western India","season":"Kharif / Rabi","duration":"100-115 days","special":"Dual purpose","pdf":"brochures/jowar.pdf","markets":"India","hybrids":[{"name":"TMRJ-301","desc":"Grain Hybrid (100-110 days)"},{"name":"TMRJ-402","desc":"Dual-Purpose Hybrid (105-115 days)"}]},
    {"id":"sunflower","name":"Sunflower","category":"field-crops","type":"Hybrid","code":"TMR-SF","active":True,"order":6,"detailPage":True,"description":"Oil and confectionery sunflower hybrids with excellent head size and seed filling. Suitable for Kharif and Rabi seasons.","image":"images/products/sunflower.jpg","features":["High oil recovery","Confectionery options","Good head size","Necrosis tolerance"],"region":"Peninsular India","season":"Kharif / Rabi","duration":"85-100 days","special":"Oil & confectionery types","pdf":"brochures/sunflower.pdf","markets":"India","hybrids":[{"name":"TMRSF-501","desc":"Oil Hybrid (40-42% oil)"},{"name":"TMRSF-602","desc":"Confectionery Hybrid (Striped)"}]},
    {"id":"cotton","name":"Cotton","category":"field-crops","type":"Hybrid","code":"TMR-CT","active":True,"order":7,"detailPage":True,"description":"BG-II and conventional cotton hybrids with premium staple length. Effective bollworm protection and good boll retention.","image":"images/products/cotton.jpg","features":["BG-II technology","Premium staple (28-32 mm)","Good boll retention","Sucking pest tolerance"],"region":"Central & Southern India","season":"Kharif","duration":"150-170 days","special":"BG-II technology","pdf":"brochures/cotton.pdf","markets":"India","hybrids":[{"name":"TMRC-701","desc":"BG-II Hybrid (Cry1Ac+Cry2Ab)"},{"name":"TMRC-802","desc":"Conventional Hybrid"}]},
    {"id":"green-gram","name":"Green Gram","category":"field-crops","type":"Variety","code":"TMR-GG","active":True,"order":8,"detailPage":True,"description":"Early and high-yielding green gram varieties with bold, shiny grains. Synchronous maturity for cleaner harvest.","image":"images/products/green-gram.jpg","features":["Bold, shiny grains","Synchronous maturity","Good cooking quality","YMD tolerance"],"region":"All India","season":"Kharif / Summer","duration":"60-70 days","special":"Short duration","pdf":"brochures/green-gram.pdf","markets":"India","hybrids":[{"name":"TMRG-901","desc":"Early Variety (60-65 days)"},{"name":"TMRG-902","desc":"High Yield Variety (65-70 days)"}]},
    {"id":"black-gram","name":"Black Gram","category":"field-crops","type":"Variety","code":"TMR-BG","active":True,"order":9,"detailPage":True,"description":"Early and high-yielding black gram varieties with bold, lustrous grains. Excellent pod filling and market-preferred quality.","image":"images/products/black-gram.jpg","features":["Bold, black, shiny grains","Multiple picking","Good pod filling","BLB tolerance"],"region":"All India","season":"Kharif / Rabi","duration":"65-75 days","special":"Bold grain type","pdf":"brochures/black-gram.pdf","markets":"India","hybrids":[{"name":"TMRB-951","desc":"Early Variety (65-70 days)"},{"name":"TMRB-952","desc":"High Yield Variety (70-75 days)"}]},
    # vegetables 1-10
    {"id":"tomato","name":"Tomato","category":"vegetables","type":"Hybrid","code":"TMR-TO","active":True,"order":1,"description":"High-yielding tomato hybrids for open-field and protected cultivation. Good fruit setting and disease tolerance.","image":"images/products/tomato.jpg","features":["Open-field & protected","Good fruit setting","Disease tolerance","Market-preferred shape"],"region":"All India","season":"Kharif / Rabi / Summer","duration":"60-75 days","hybrids":[{"name":"Indeterminate","desc":"Open-field, high yield"},{"name":"Determinate","desc":"Protected cultivation"}]},
    {"id":"brinjal","name":"Brinjal (Eggplant)","category":"vegetables","type":"Hybrid","code":"TMR-BR","active":True,"order":2,"description":"Hybrid brinjal varieties with high yield potential and excellent fruit quality. Suitable for diverse growing conditions.","image":"images/products/brinjal.jpg","features":["High yielding","Glossy fruits","Good shelf life","Market preferred"],"region":"All India","season":"Kharif / Rabi","duration":"70-85 days","hybrids":[{"name":"Long Purple","desc":"High-yielding, glossy"},{"name":"Round Green","desc":"Market preferred"}]},
    {"id":"chilli","name":"Chilli","category":"vegetables","type":"Hybrid","code":"TMR-CH","active":True,"order":3,"description":"Green and red chilli hybrids with high pungency and good drying recovery. Suitable for fresh market and processing.","image":"images/products/chilli.jpg","features":["High pungency","Good drying recovery","Dark green colour","High yield"],"region":"All India","season":"Kharif / Rabi","duration":"75-90 days","hybrids":[{"name":"Green Chilli","desc":"High pungency, dark green"},{"name":"Red Chilli","desc":"Good drying recovery"}]},
    {"id":"okra","name":"Okra (Lady's Finger)","category":"vegetables","type":"Hybrid","code":"TMR-OK","active":True,"order":4,"description":"Tender, dark green okra hybrids with YVMV tolerance. Excellent field holding capacity and market preference.","image":"images/products/okra.jpg","features":["YVMV tolerant","Tender, dark green","Good field holding","High yield"],"region":"All India","season":"Kharif / Summer","duration":"50-60 days","special":"YVMV tolerant","hybrids":[{"name":"Early Hybrid","desc":"Tender, dark green"},{"name":"High Yield","desc":"YVMV tolerant"}]},
    {"id":"bottle-gourd","name":"Bottle Gourd","category":"vegetables","type":"Hybrid","code":"TMR-BG","active":True,"order":5,"description":"Long and round bottle gourd hybrids with tender flesh and high yield potential.","image":"images/products/bottle-gourd.jpg","features":["Tender flesh","Long & round types","High yield","Good market preference"],"region":"All India","season":"Kharif / Summer","duration":"55-65 days","hybrids":[{"name":"Long Hybrid","desc":"Tender, high yield"},{"name":"Round Hybrid","desc":"Premium variety"}]},
    {"id":"ridge-gourd","name":"Ridge Gourd","category":"vegetables","type":"Hybrid","code":"TMR-RG","active":True,"order":6,"description":"Early and high-yielding ridge gourd hybrids with long, dark green fruits and good shelf life.","image":"images/products/ridge-gourd.jpg","features":["Long, dark green fruits","Good shelf life","High yield","Early maturity"],"region":"All India","season":"Kharif","duration":"50-60 days","hybrids":[{"name":"Early Hybrid","desc":"Long, dark green"},{"name":"High Yield","desc":"Good shelf life"}]},
    {"id":"cabbage","name":"Cabbage","category":"vegetables","type":"Hybrid","code":"TMR-CB","active":True,"order":7,"description":"Compact-headed cabbage hybrid with 60-day maturity. Good field holding and market-preferred shape.","image":"images/products/cabbage.jpg","features":["Compact head","60 days maturity","Good field holding","Market preferred"],"region":"All India","season":"Rabi / Kharif","duration":"55-65 days","hybrids":[{"name":"Early Hybrid","desc":"Compact head, 60 days"}]},
    {"id":"cauliflower","name":"Cauliflower","category":"vegetables","type":"Hybrid","code":"TMR-CF","active":True,"order":8,"description":"Early and late cauliflower hybrids with snow-white curds. Good curd compactness and disease tolerance.","image":"images/products/cauliflower.jpg","features":["Snow white curds","Early & late types","Good curd compactness","Disease tolerance"],"region":"All India","season":"Rabi / Kharif","duration":"55-75 days","hybrids":[{"name":"Early Hybrid","desc":"Curd formation 55 days"},{"name":"Late Hybrid","desc":"Snow white, 75 days"}]},
    {"id":"cucumber","name":"Cucumber","category":"vegetables","type":"Hybrid","code":"TMR-CU","active":True,"order":9,"description":"Open-field and protected cucumber hybrids with dark green fruits and high yield. Parthenocarpic options for protected cultivation.","image":"images/products/cucumber.jpg","features":["Open-field & protected","Parthenocarpic options","Dark green fruits","High yield"],"region":"All India","season":"Kharif / Summer","duration":"50-60 days","hybrids":[{"name":"Open-field","desc":"High yield, dark green"},{"name":"Protected","desc":"Parthenocarpic"}]},
    {"id":"watermelon","name":"Watermelon","category":"vegetables","type":"Hybrid","code":"TMR-WM","active":True,"order":10,"description":"Red and yellow watermelon hybrids with high brix and excellent eating quality. Crimson sweet and premium types.","image":"images/products/watermelon.jpg","features":["Red & yellow types","High brix (12-14%)","Good shipping quality","Premium eating quality"],"region":"All India","season":"Summer / Kharif","duration":"70-85 days","hybrids":[{"name":"Red Hybrid","desc":"Crimson sweet type"},{"name":"Yellow Hybrid","desc":"Premium, high brix"}]},
    # fodder 1-3
    {"id":"maize-fodder","name":"Maize Fodder","category":"fodder","type":"Hybrid","code":"TMR-FM","active":True,"order":1,"description":"High-biomass multi-cut maize fodder hybrids for dairy and livestock. Nutritious and palatable green and dry fodder.","image":"images/products/maize-fodder.jpg","features":["Multi-cut (3-4 cuts)","High biomass","Nutritious","Palatable"],"region":"All India","season":"Kharif / Rabi","duration":"55-65 days per cut","hybrids":[{"name":"Multi-Cut Fodder","desc":"High biomass, 3-4 cuts"},{"name":"Green Fodder","desc":"Nutritious, palatable"}]},
    {"id":"sorghum-fodder","name":"Sorghum Fodder","category":"fodder","type":"Variety","code":"TMR-FS","active":True,"order":2,"description":"Multi-cut and single-cut sorghum fodder varieties with sustained fodder supply and high dry matter content.","image":"images/products/sorghum-fodder.jpg","features":["Multi-cut (4-5 cuts)","High dry matter","Good regrowth","Drought tolerance"],"region":"All India","season":"Kharif / Summer","duration":"50-60 days per cut","hybrids":[{"name":"Multi-Cut Variety","desc":"Sustained supply, 4-5 cuts"},{"name":"Single-Cut Variety","desc":"High dry matter"}]},
    {"id":"cowpea-fodder","name":"Cowpea Fodder","category":"fodder","type":"Variety","code":"TMR-FC","active":True,"order":3,"description":"Protein-rich cowpea fodder varieties for improved livestock nutrition. Dual-purpose options for fodder and green manure.","image":"images/products/cowpea-fodder.jpg","features":["High protein (18-20% CP)","Dual-purpose","Good biomass","Soil improvement"],"region":"All India","season":"Kharif / Summer","duration":"45-55 days","hybrids":[{"name":"Fodder Variety","desc":"Protein-rich, 18-20% CP"},{"name":"Dual-Purpose","desc":"Fodder + green manure"}]},
]

print(f"Existing aggregate products: {len(existing)}")

# Convert each raw product to new format
def convert(p, cat_slug, order_num):
    code = p.get("code", "").strip()
    name = p.get("name", "")
    pid = code.lower() if code else name.lower().replace(" ", "-").replace("(","").replace(")","").replace("'","").replace("&","and")
    pid = re.sub(r'[^a-z0-9-]', '-', pid).strip('-')
    if not pid:
        pid = "product-" + str(order_num)
    
    ptype = determine_type(code, name)
    desc = clean_desc(p.get("short_description", ""))
    if not desc:
        desc = f"{name} — {ptype.lower()} from Trimurti Seeds."
    
    image_url = p.get("image_url", "") or ""
    img = f"images/products/{code}.jpg" if (image_url and code) else ""
    
    pdfs = p.get("pdfs", [])
    pdf = f"brochures/{code}.pdf" if (pdfs and code) else ""
    
    features = make_features(desc)
    
    return {
        "id": pid, "name": name, "category": cat_slug, "type": ptype,
        "code": code if code else "", "active": True, "order": order_num,
        "description": desc, "features": features,
        "region": "", "season": "", "duration": "", "special": "",
        "image": img, "pdf": pdf, "markets": "",
        "detailPage": False, "hybrids": []
    }

new_field = []
new_veg = []
new_fodder = []

fc_n = 10
vc_n = 11
fd_n = 4

for p in products_raw:
    cat = p.get("category", "")
    cs = CAT_MAP.get(cat, "field-crops")
    prod = convert(p, cs, 0)
    if cs == "field-crops":
        prod["order"] = fc_n; fc_n += 1; new_field.append(prod)
    elif cs == "vegetables":
        prod["order"] = vc_n; vc_n += 1; new_veg.append(prod)
    elif cs == "fodder":
        prod["order"] = fd_n; fd_n += 1; new_fodder.append(prod)

print(f"New field-crops: {len(new_field)}, veg: {len(new_veg)}, fodder: {len(new_fodder)}")
print(f"Total all: {len(existing) + len(new_field) + len(new_veg) + len(new_fodder)}")

# JS value serializer
def js_str(s):
    """Serialize string to JS-safe value."""
    if not s:
        return '""'
    # Escape for JSON
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "").replace("\t", "\\t")
    return f'"{s}"'

def prod_js(p, indent=2):
    i = "  " * indent
    i1 = "  " * (indent + 1)
    lines = [f"{i}{{"]
    
    # Simple scalar fields in order
    scalar = ["id", "name", "category", "type", "code"]
    for f in scalar:
        lines.append(f'{i1}{f}: {js_str(p[f])},')
    
    lines.append(f"{i1}active: {'true' if p['active'] else 'false'},")
    lines.append(f"{i1}order: {p['order']},")
    
    # description (truncated)
    lines.append(f"{i1}description: {js_str(p['description'])},",)
    
    # image
    lines.append(f"{i1}image: {js_str(p['image'])},",)
    
    # features - only for aggregate products
    if p.get("order", 99) <= 10 and p["category"] == "field-crops":
        feats = p.get("features", [])
        if feats:
            feat_str = ", ".join(js_str(f) for f in feats)
            lines.append(f"{i1}features: [{feat_str}],")
        else:
            lines.append(f"{i1}features: [],")
    elif p.get("order", 99) <= 10 and p["category"] == "vegetables":
        feats = p.get("features", [])
        if feats:
            feat_str = ", ".join(js_str(f) for f in feats)
            lines.append(f"{i1}features: [{feat_str}],")
        else:
            lines.append(f"{i1}features: [],")
    elif p.get("order", 99) <= 3 and p["category"] == "fodder":
        feats = p.get("features", [])
        if feats:
            feat_str = ", ".join(js_str(f) for f in feats)
            lines.append(f"{i1}features: [{feat_str}],")
        else:
            lines.append(f"{i1}features: [],")
    else:
        lines.append(f"{i1}features: [],")
    
    # Optional string fields - only for aggregate products
    is_agg = (p.get("order", 99) <= 10 and p["category"] in ("field-crops", "vegetables")) or \
             (p.get("order", 99) <= 3 and p["category"] == "fodder")
    if is_agg:
        for f in ["region", "season", "duration", "special"]:
            v = p.get(f, "")
            if v:
                lines.append(f"{i1}{f}: {js_str(v)},")
    
    # pdf
    pdf = p.get("pdf", "")
    if pdf:
        lines.append(f"{i1}pdf: {js_str(pdf)},")
    
    # markets
    mkt = p.get("markets", "")
    if mkt:
        lines.append(f"{i1}markets: {js_str(mkt)},")
    
    lines.append(f"{i1}detailPage: {'true' if p.get('detailPage', False) else 'false'},")
    
    # hybrids array
    hybrids = p.get("hybrids", [])
    if hybrids:
        h_items = []
        for h in hybrids:
            hn = js_str(h.get("name", ""))
            hd = js_str(h.get("desc", ""))
            h_items.append(f"{{name: {hn}, desc: {hd}}}")
        lines.append(f"{i1}hybrids: [{', '.join(h_items)}]")
    else:
        lines.append(f"{i1}hybrids: []")
    
    lines.append(f"{i1}}},")
    return "\n".join(lines)

# Build complete JS file
parts = []

parts.append("""// ================================================================
// TRIMURTI PRODUCT CATALOG — Edit this file to manage all products
// ================================================================
// HOW TO ADD A PRODUCT:
//   Copy a block below, paste it inside the PRODUCTS array,
//   fill in the fields, and save. The page builds itself.
//
// FIELDS:
//   id           unique slug (e.g. "maize")
//   name         product display name
//   category     "field-crops" | "vegetables" | "fodder"
//   type         "Hybrid" | "Variety"
//   code         internal product code (optional)
//   description  short description (1-2 lines)
//   features     array of key features (strings)
//   region       suitable region
//   season       suitable season
//   duration     crop duration
//   special      special traits (e.g. "Drought tolerant")
//   image        path to product image (optional)
//   pdf          path to brochure PDF (optional)
//   markets      market regions (optional)
//   active       true/false — set false to hide without deleting
//   order        display order within category (lower = first)
//   detailPage   true = has own detail page at crops/{id}.html
//   hybrids      array of { name, desc }
//
// NOTE: First entries (order 1-9 for field-crops, 1-10 for vegetables,
// 1-3 for fodder) are category summary cards with detail pages.
// All subsequent entries are individual SKU products.
// ================================================================

const PRODUCTS = [
""")

# Field crops section
parts.append("  // ======================================================================\n")
parts.append("  // FIELD CROPS — Category Summary Cards (order 1-9)\n")
parts.append("  // ======================================================================\n")
for p in existing[:9]:
    parts.append(prod_js(p) + "\n")

parts.append("  // ----------------------------------------------------------------------\n")
parts.append("  // FIELD CROPS — Individual SKUs (order 10+)\n")
parts.append("  // ----------------------------------------------------------------------\n")
for p in new_field:
    parts.append(prod_js(p) + "\n")

# Vegetables section
parts.append("  // ======================================================================\n")
parts.append("  // VEGETABLES — Category Summary Cards (order 1-10)\n")
parts.append("  // ======================================================================\n")
for p in existing[9:19]:
    parts.append(prod_js(p) + "\n")

parts.append("  // ----------------------------------------------------------------------\n")
parts.append("  // VEGETABLES — Individual SKUs (order 11+)\n")
parts.append("  // ----------------------------------------------------------------------\n")
for p in new_veg:
    parts.append(prod_js(p) + "\n")

# Fodder section
parts.append("  // ======================================================================\n")
parts.append("  // FODDER — Category Summary Cards (order 1-3)\n")
parts.append("  // ======================================================================\n")
for p in existing[19:]:
    parts.append(prod_js(p) + "\n")

parts.append("  // ----------------------------------------------------------------------\n")
parts.append("  // FODDER — Individual SKUs (order 4+)\n")
parts.append("  // ----------------------------------------------------------------------\n")
for p in new_fodder:
    parts.append(prod_js(p) + "\n")

parts.append("""];

// Helper: get active products sorted by order
function getActiveProducts() {
  return PRODUCTS.filter(function(p) { return p.active !== false; })
    .sort(function(a, b) { return (a.order || 99) - (b.order || 99); });
}

// Helper: get products by category
function getProductsByCategory(category) {
  return getActiveProducts().filter(function(p) { return p.category === category; });
}
""")

full_js = "".join(parts)
sz = len(full_js)
print(f"\nGenerated JS: {sz} chars = {sz/1024:.1f} KB")
print(f"Total products in array: {len(existing) + len(new_field) + len(new_veg) + len(new_fodder)}")

# Write
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(full_js)

print(f"\nWritten to {OUTPUT_PATH}")

# Count images and products with codes
with_img = sum(1 for p in products_raw if p.get("image_url","") and p.get("code","").strip())
with_code = sum(1 for p in products_raw if p.get("code","").strip())
print(f"\nProducts with image_url + code: {with_img}")
print(f"Products with code: {with_code}")
