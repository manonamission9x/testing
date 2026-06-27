#!/usr/bin/env python3
"""
Generate products-data.js with all 208 products + download images script.
Reads raw-scrape.json and produces:
1. products-data.js (complete catalog)
2. download.py (image downloader)
"""
import json
import re
import os

# Paths
BASE = r"C:\Users\kingo\trimurti-redesign"
SCRAPE_PATH = os.path.join(BASE, "product-migration", "raw-scrape.json")
OUTPUT_PATH = os.path.join(BASE, "products-data.js")
DOWNLOAD_SCRIPT_PATH = os.path.join(BASE, "download.py")

# Load scrape data
with open(SCRAPE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

products_raw = data["products"]
print(f"Total raw products: {len(products_raw)}")

# Category mapping
CAT_MAP = {
    "Field Crops": "field-crops",
    "Vegetables": "vegetables",
    "Fodder": "fodder",
}

def determine_type(code, name):
    """Determine if product is Hybrid or Variety based on code prefix or name."""
    if not code:
        code = ""
    code_upper = code.upper()
    
    # Hybrid indicators
    hybrid_prefixes = ["TMMH", "TMRH", "TMBH", "TMWH", "TMTH", "TMPH", "TMOH", 
                       "TMBI", "TMBG", "TMCU", "TMSG", "TMPU", "TMCA", "TMCH",
                       "TMSH", "TMFH", "TMW"]
    
    # Variety indicators
    variety_prefixes = ["TMRV", "TMMD", "TMOV", "TMMD"]
    
    for p in hybrid_prefixes:
        if code_upper.startswith(p):
            return "Hybrid"
    for p in variety_prefixes:
        if code_upper.startswith(p):
            return "Variety"
    
    # Check name clues
    name_lower = name.lower()
    if "variety" in name_lower:
        return "Variety"
    
    # Default based on common patterns
    if "TM" in code_upper[:4]:
        # Check if it's TMRV/TMMD etc (variety codes)
        if code_upper.startswith("TMRV") or code_upper.startswith("TMMD") or code_upper.startswith("TMOV"):
            return "Variety"
        return "Hybrid"
    
    return "Hybrid"

def make_id(name, code):
    """Create a unique slug/id for a product."""
    if code and code.strip():
        return code.strip().lower().replace(" ", "-")
    # Fallback: slugify name
    slug = name.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug)
    return slug

def clean_desc(desc):
    """Clean & truncate description."""
    if not desc or desc.strip() == "":
        return ""
    # Decode HTML entities
    desc = desc.replace("&amp;", "&").replace("&#8211;", "-").replace("&#038;", "&")
    desc = desc.replace("&gt;", ">").replace("&lt;", "<")
    desc = desc.replace("&#8217;", "'").replace("&#8220;", '"').replace("&#8221;", '"')
    # Limit to ~200 chars for size
    if len(desc) > 200:
        desc = desc[:197] + "..."
    return desc.strip()

def get_image_path(code, image_url):
    """Get image path from product code and image URL."""
    if not image_url or image_url.strip() == "":
        return ""
    if not code or code.strip() == "":
        # Try to extract from the name
        return ""
    return f"images/products/{code.strip()}.jpg"

def get_type_from_code(code):
    """Get type based on code prefix."""
    if not code:
        return ""
    code_upper = code.upper()
    # Last 2 chars of prefix for M/H/V/D
    hybrid_types = ["MH", "RH", "BH", "WH", "TH", "PH", "OH", "BI", "BG", "CU", "SG", "PU", "CA", "CH", "SH", "FH", "MW"]
    variety_types = ["RV", "MD", "OV", "MD", "MW"]
    return code_upper

# ============================================
# STEP 1: Build the existing 22 aggregate products
# ============================================

existing_field = [
    {
        "id":"maize", "name":"Maize", "category":"field-crops", "type":"Hybrid",
        "code":"TMR-MZ", "active":True, "order":1, "detailPage":True,
        "description":"High-yielding biotech and conventional maize hybrids for Kharif and Rabi seasons. Strong pest tolerance and excellent grain quality.",
        "image":"images/products/maize.jpg",
        "features":["Biotech & conventional options","Kharif & Rabi seasons","Excellent stay-green trait","High shelling percentage"],
        "region":"Central & Southern India", "season":"Kharif / Rabi", "duration":"95-115 days",
        "special":"Pest tolerant, drought tolerance", "pdf":"brochures/maize.pdf",
        "markets":"India, Nepal",
        "hybrids":[
            {"name":"Nagma", "desc":"Biotech Hybrid — Kharif"},
            {"name":"TMRH-1422", "desc":"Biotech Hybrid — Rabi"},
            {"name":"TMRH-871", "desc":"Conventional Hybrid"}
        ]
    },
    {
        "id":"rice", "name":"Rice", "category":"field-crops", "type":"Hybrid",
        "code":"TMR-RC", "active":True, "order":2, "detailPage":True,
        "description":"Premium rice hybrids across early, medium, and late duration groups. Long slender grains with excellent cooking quality.",
        "features":["Long slender grains","Multiple maturity groups","High tillering","Good grain quality"],
        "region":"All major rice-growing regions", "season":"Kharif", "duration":"100-145 days",
        "special":"High yield potential", "pdf":"brochures/rice.pdf",
        "markets":"India, Nepal",
        "hybrids":[
            {"name":"TMRH-221", "desc":"Early Duration (100-110 days)"},
            {"name":"TMRH-335", "desc":"Medium Duration (120-130 days)"},
            {"name":"TMRH-448", "desc":"Late Duration (140-145 days)"}
        ]
    },
    {
        "id":"mustard", "name":"Mustard", "category":"field-crops", "type":"Hybrid",
        "code":"TMR-MS", "active":True, "order":3, "detailPage":True,
        "description":"High oil content mustard hybrids with excellent pod load and disease tolerance. Suitable for rainfed and irrigated conditions.",
        "features":["Oil content 42-45%","Pod shattering tolerance","Good meal quality","Aphid tolerance"],
        "region":"Central & Northern India", "season":"Rabi", "duration":"85-120 days",
        "special":"High oil content", "pdf":"brochures/mustard.pdf",
        "markets":"India",
        "hybrids":[
            {"name":"TMRH-511", "desc":"Early Hybrid (100-110 days)"},
            {"name":"TMRH-622", "desc":"High Yield Hybrid (115-120 days)"},
            {"name":"TMRH-733", "desc":"Short Duration Hybrid (85-95 days)"}
        ]
    },
    {
        "id":"bajra", "name":"Bajra (Pearl Millet)", "category":"field-crops", "type":"Hybrid",
        "code":"TMR-BJ", "active":True, "order":4, "detailPage":True,
        "description":"Drought-tolerant pearl millet hybrids for rainfed and dryland conditions. Excellent grain filling and dual-purpose options.",
        "features":["Drought tolerance","Dual-purpose options","Good grain quality","Downy mildew tolerance"],
        "region":"Arid & Semi-arid zones", "season":"Kharif", "duration":"75-90 days",
        "special":"Drought tolerant", "pdf":"brochures/bajra.pdf",
        "markets":"India",
        "hybrids":[
            {"name":"TMRB-101", "desc":"Drought Tolerant Hybrid"},
            {"name":"TMRB-202", "desc":"Dual Purpose Hybrid"}
        ]
    },
    {
        "id":"jowar", "name":"Jowar (Sorghum)", "category":"field-crops", "type":"Hybrid",
        "code":"TMR-JW", "active":True, "order":5, "detailPage":True,
        "description":"Grain and dual-purpose sorghum hybrids with bold, lustrous grains. Excellent threshing recovery and fodder quality.",
        "features":["Bold, white grains","Dual-purpose options","Shoot fly tolerance","High biomass"],
        "region":"Central & Western India", "season":"Kharif / Rabi", "duration":"100-115 days",
        "special":"Dual purpose", "pdf":"brochures/jowar.pdf",
        "markets":"India",
        "hybrids":[
            {"name":"TMRJ-301", "desc":"Grain Hybrid (100-110 days)"},
            {"name":"TMRJ-402", "desc":"Dual-Purpose Hybrid (105-115 days)"}
        ]
    },
    {
        "id":"sunflower", "name":"Sunflower", "category":"field-crops", "type":"Hybrid",
        "code":"TMR-SF", "active":True, "order":6, "detailPage":True,
        "description":"Oil and confectionery sunflower hybrids with excellent head size and seed filling. Suitable for Kharif and Rabi seasons.",
        "features":["High oil recovery","Confectionery options","Good head size","Necrosis tolerance"],
        "region":"Peninsular India", "season":"Kharif / Rabi", "duration":"85-100 days",
        "special":"Oil & confectionery types", "pdf":"brochures/sunflower.pdf",
        "markets":"India",
        "hybrids":[
            {"name":"TMRSF-501", "desc":"Oil Hybrid (40-42% oil)"},
            {"name":"TMRSF-602", "desc":"Confectionery Hybrid (Striped)"}
        ]
    },
    {
        "id":"cotton", "name":"Cotton", "category":"field-crops", "type":"Hybrid",
        "code":"TMR-CT", "active":True, "order":7, "detailPage":True,
        "description":"BG-II and conventional cotton hybrids with premium staple length. Effective bollworm protection and good boll retention.",
        "features":["BG-II technology","Premium staple (28-32 mm)","Good boll retention","Sucking pest tolerance"],
        "region":"Central & Southern India", "season":"Kharif", "duration":"150-170 days",
        "special":"BG-II technology", "pdf":"brochures/cotton.pdf",
        "markets":"India",
        "hybrids":[
            {"name":"TMRC-701", "desc":"BG-II Hybrid (Cry1Ac+Cry2Ab)"},
            {"name":"TMRC-802", "desc":"Conventional Hybrid"}
        ]
    },
    {
        "id":"green-gram", "name":"Green Gram", "category":"field-crops", "type":"Variety",
        "code":"TMR-GG", "active":True, "order":8, "detailPage":True,
        "description":"Early and high-yielding green gram varieties with bold, shiny grains. Synchronous maturity for cleaner harvest.",
        "features":["Bold, shiny grains","Synchronous maturity","Good cooking quality","YMD tolerance"],
        "region":"All India", "season":"Kharif / Summer", "duration":"60-70 days",
        "special":"Short duration", "pdf":"brochures/green-gram.pdf",
        "markets":"India",
        "hybrids":[
            {"name":"TMRG-901", "desc":"Early Variety (60-65 days)"},
            {"name":"TMRG-902", "desc":"High Yield Variety (65-70 days)"}
        ]
    },
    {
        "id":"black-gram", "name":"Black Gram", "category":"field-crops", "type":"Variety",
        "code":"TMR-BG", "active":True, "order":9, "detailPage":True,
        "description":"Early and high-yielding black gram varieties with bold, lustrous grains. Excellent pod filling and market-preferred quality.",
        "features":["Bold, black, shiny grains","Multiple picking","Good pod filling","BLB tolerance"],
        "region":"All India", "season":"Kharif / Rabi", "duration":"65-75 days",
        "special":"Bold grain type", "pdf":"brochures/black-gram.pdf",
        "markets":"India",
        "hybrids":[
            {"name":"TMRB-951", "desc":"Early Variety (65-70 days)"},
            {"name":"TMRB-952", "desc":"High Yield Variety (70-75 days)"}
        ]
    },
]

existing_veg = [
    {
        "id":"tomato", "name":"Tomato", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-TO", "active":True, "order":1,
        "description":"High-yielding tomato hybrids for open-field and protected cultivation. Good fruit setting and disease tolerance.",
        "features":["Open-field & protected","Good fruit setting","Disease tolerance","Market-preferred shape"],
        "region":"All India", "season":"Kharif / Rabi / Summer", "duration":"60-75 days",
        "hybrids":[
            {"name":"Indeterminate", "desc":"Open-field, high yield"},
            {"name":"Determinate", "desc":"Protected cultivation"}
        ]
    },
    {
        "id":"brinjal", "name":"Brinjal (Eggplant)", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-BR", "active":True, "order":2,
        "description":"Hybrid brinjal varieties with high yield potential and excellent fruit quality. Suitable for diverse growing conditions.",
        "features":["High yielding","Glossy fruits","Good shelf life","Market preferred"],
        "region":"All India", "season":"Kharif / Rabi", "duration":"70-85 days",
        "hybrids":[
            {"name":"Long Purple", "desc":"High-yielding, glossy"},
            {"name":"Round Green", "desc":"Market preferred"}
        ]
    },
    {
        "id":"chilli", "name":"Chilli", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-CH", "active":True, "order":3,
        "description":"Green and red chilli hybrids with high pungency and good drying recovery. Suitable for fresh market and processing.",
        "features":["High pungency","Good drying recovery","Dark green colour","High yield"],
        "region":"All India", "season":"Kharif / Rabi", "duration":"75-90 days",
        "hybrids":[
            {"name":"Green Chilli", "desc":"High pungency, dark green"},
            {"name":"Red Chilli", "desc":"Good drying recovery"}
        ]
    },
    {
        "id":"okra", "name":"Okra (Lady's Finger)", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-OK", "active":True, "order":4,
        "description":"Tender, dark green okra hybrids with YVMV tolerance. Excellent field holding capacity and market preference.",
        "features":["YVMV tolerant","Tender, dark green","Good field holding","High yield"],
        "region":"All India", "season":"Kharif / Summer", "duration":"50-60 days",
        "special":"YVMV tolerant",
        "hybrids":[
            {"name":"Early Hybrid", "desc":"Tender, dark green"},
            {"name":"High Yield", "desc":"YVMV tolerant"}
        ]
    },
    {
        "id":"bottle-gourd", "name":"Bottle Gourd", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-BG", "active":True, "order":5,
        "description":"Long and round bottle gourd hybrids with tender flesh and high yield potential.",
        "features":["Tender flesh","Long & round types","High yield","Good market preference"],
        "region":"All India", "season":"Kharif / Summer", "duration":"55-65 days",
        "hybrids":[
            {"name":"Long Hybrid", "desc":"Tender, high yield"},
            {"name":"Round Hybrid", "desc":"Premium variety"}
        ]
    },
    {
        "id":"ridge-gourd", "name":"Ridge Gourd", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-RG", "active":True, "order":6,
        "description":"Early and high-yielding ridge gourd hybrids with long, dark green fruits and good shelf life.",
        "features":["Long, dark green fruits","Good shelf life","High yield","Early maturity"],
        "region":"All India", "season":"Kharif", "duration":"50-60 days",
        "hybrids":[
            {"name":"Early Hybrid", "desc":"Long, dark green"},
            {"name":"High Yield", "desc":"Good shelf life"}
        ]
    },
    {
        "id":"cabbage", "name":"Cabbage", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-CB", "active":True, "order":7,
        "description":"Compact-headed cabbage hybrid with 60-day maturity. Good field holding and market-preferred shape.",
        "features":["Compact head","60 days maturity","Good field holding","Market preferred"],
        "region":"All India", "season":"Rabi / Kharif", "duration":"55-65 days",
        "hybrids":[
            {"name":"Early Hybrid", "desc":"Compact head, 60 days"}
        ]
    },
    {
        "id":"cauliflower", "name":"Cauliflower", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-CF", "active":True, "order":8,
        "description":"Early and late cauliflower hybrids with snow-white curds. Good curd compactness and disease tolerance.",
        "features":["Snow white curds","Early & late types","Good curd compactness","Disease tolerance"],
        "region":"All India", "season":"Rabi / Kharif", "duration":"55-75 days",
        "hybrids":[
            {"name":"Early Hybrid", "desc":"Curd formation 55 days"},
            {"name":"Late Hybrid", "desc":"Snow white, 75 days"}
        ]
    },
    {
        "id":"cucumber", "name":"Cucumber", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-CU", "active":True, "order":9,
        "description":"Open-field and protected cucumber hybrids with dark green fruits and high yield. Parthenocarpic options for protected cultivation.",
        "features":["Open-field & protected","Parthenocarpic options","Dark green fruits","High yield"],
        "region":"All India", "season":"Kharif / Summer", "duration":"50-60 days",
        "hybrids":[
            {"name":"Open-field", "desc":"High yield, dark green"},
            {"name":"Protected", "desc":"Parthenocarpic"}
        ]
    },
    {
        "id":"watermelon", "name":"Watermelon", "category":"vegetables", "type":"Hybrid",
        "code":"TMR-WM", "active":True, "order":10,
        "description":"Red and yellow watermelon hybrids with high brix and excellent eating quality. Crimson sweet and premium types.",
        "features":["Red & yellow types","High brix (12-14%)","Good shipping quality","Premium eating quality"],
        "region":"All India", "season":"Summer / Kharif", "duration":"70-85 days",
        "hybrids":[
            {"name":"Red Hybrid", "desc":"Crimson sweet type"},
            {"name":"Yellow Hybrid", "desc":"Premium, high brix"}
        ]
    },
]

existing_fodder = [
    {
        "id":"maize-fodder", "name":"Maize Fodder", "category":"fodder", "type":"Hybrid",
        "code":"TMR-FM", "active":True, "order":1,
        "description":"High-biomass multi-cut maize fodder hybrids for dairy and livestock. Nutritious and palatable green and dry fodder.",
        "features":["Multi-cut (3-4 cuts)","High biomass","Nutritious","Palatable"],
        "region":"All India", "season":"Kharif / Rabi", "duration":"55-65 days per cut",
        "hybrids":[
            {"name":"Multi-Cut Fodder", "desc":"High biomass, 3-4 cuts"},
            {"name":"Green Fodder", "desc":"Nutritious, palatable"}
        ]
    },
    {
        "id":"sorghum-fodder", "name":"Sorghum Fodder", "category":"fodder", "type":"Variety",
        "code":"TMR-FS", "active":True, "order":2,
        "description":"Multi-cut and single-cut sorghum fodder varieties with sustained fodder supply and high dry matter content.",
        "features":["Multi-cut (4-5 cuts)","High dry matter","Good regrowth","Drought tolerance"],
        "region":"All India", "season":"Kharif / Summer", "duration":"50-60 days per cut",
        "hybrids":[
            {"name":"Multi-Cut Variety", "desc":"Sustained supply, 4-5 cuts"},
            {"name":"Single-Cut Variety", "desc":"High dry matter"}
        ]
    },
    {
        "id":"cowpea-fodder", "name":"Cowpea Fodder", "category":"fodder", "type":"Variety",
        "code":"TMR-FC", "active":True, "order":3,
        "description":"Protein-rich cowpea fodder varieties for improved livestock nutrition. Dual-purpose options for fodder and green manure.",
        "features":["High protein (18-20% CP)","Dual-purpose","Good biomass","Soil improvement"],
        "region":"All India", "season":"Kharif / Summer", "duration":"45-55 days",
        "hybrids":[
            {"name":"Fodder Variety", "desc":"Protein-rich, 18-20% CP"},
            {"name":"Dual-Purpose", "desc":"Fodder + green manure"}
        ]
    },
]

# ============================================
# STEP 2: Convert each raw product to new format
# ============================================

def convert_product(p, cat_slug, start_order):
    """Convert a raw scrape product to the new format."""
    code = p.get("code", "").strip()
    name = p.get("name", "")
    
    # Build ID from code or name
    if code:
        pid = code.lower()
    else:
        pid = make_id(name, "")
    
    ptype = determine_type(code, name)
    
    desc = clean_desc(p.get("short_description", ""))
    if not desc:
        if ptype == "Hybrid":
            desc = f"{name} hybrid from Trimurti Seeds."
        else:
            desc = f"{name} variety from Trimurti Seeds."
    
    image_url = p.get("image_url", "") or ""
    image_path = ""
    if image_url and code:
        image_path = f"images/products/{code}.jpg"
    
    pdf = ""
    pdfs = p.get("pdfs", [])
    if pdfs and code:
        pdf = f"brochures/{code}.pdf"
    
    features = []
    if desc:
        # Extract bullet points as features
        bullets = re.findall(r'•\s*([^•\n]+)', desc)
        if bullets:
            features = [b.strip()[:80] for b in bullets[:6]]
    
    return {
        "id": pid,
        "name": name,
        "category": cat_slug,
        "type": ptype,
        "code": code if code else "",
        "active": True,
        "order": start_order,
        "description": desc,
        "features": features,
        "region": "",
        "season": "",
        "duration": "",
        "special": "",
        "image": image_path,
        "pdf": pdf,
        "markets": "",
        "detailPage": False,
        "hybrids": []
    }

# Categorize and convert
field_individuals = []
veg_individuals = []
fodder_individuals = []

fc_order = 10  # Start after existing 9 field-crops
vc_order = 11  # Start after existing 10 vegetables
fd_order = 4   # Start after existing 3 fodder

for p in products_raw:
    cat = p.get("category", "")
    cat_slug = CAT_MAP.get(cat, "field-crops")
    
    prod = convert_product(p, cat_slug, 0)
    
    if cat_slug == "field-crops":
        prod["order"] = fc_order
        fc_order += 1
        field_individuals.append(prod)
    elif cat_slug == "vegetables":
        prod["order"] = vc_order
        vc_order += 1
        veg_individuals.append(prod)
    elif cat_slug == "fodder":
        prod["order"] = fd_order
        fd_order += 1
        fodder_individuals.append(prod)

print(f"Field crops: {len(field_individuals)}")
print(f"Vegetables: {len(veg_individuals)}")
print(f"Fodder: {len(fodder_individuals)}")
print(f"Total new: {len(field_individuals) + len(veg_individuals) + len(fodder_individuals)}")

# ============================================
# STEP 3: Generate the JS file
# ============================================

def prod_to_js(p, indent=2):
    """Convert a product dict to JS object string."""
    i = "  " * indent
    i1 = "  " * (indent + 1)
    
    def js_val(v):
        if isinstance(v, bool):
            return "true" if v else "false"
        if isinstance(v, (int, float)):
            return str(v)
        if isinstance(v, str):
            # Escape backticks and quotes inside
            v = v.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
            # Use backtick strings for multi-line, regular quotes for single-line
            if "\n" in v:
                return "`" + v + "`"
            return json.dumps(v, ensure_ascii=False)
        if isinstance(v, list):
            if not v:
                return "[]"
            items = [json.dumps(item, ensure_ascii=False) if isinstance(item, str) else str(item) for item in v]
            return "[" + ", ".join(items) + "]"
        if isinstance(v, dict):
            return str(v)
        return json.dumps(v, ensure_ascii=False)
    
    lines = []
    lines.append(f"{i}{{")
    
    fields = ["id", "name", "category", "type", "code", "active", "order"]
    for f in fields:
        lines.append(f"{i1}{f}: {js_val(p[f])},")
    
    # Description (use backtick if multi-line)
    lines.append(f"{i1}description: {js_val(p['description'])},",)
    
    # Image
    lines.append(f"{i1}image: {js_val(p['image'])},",)
    
    # Features
    lines.append(f"{i1}features: {js_val(p['features'])},",)
    
    # Optional fields
    for f in ["region", "season", "duration", "special"]:
        val = p.get(f, "")
        if val:
            lines.append(f"{i1}{f}: {js_val(val)},")
    
    # PDF
    pdf = p.get("pdf", "")
    if pdf:
        lines.append(f"{i1}pdf: {js_val(pdf)},")
    
    # Markets
    mkt = p.get("markets", "")
    if mkt:
        lines.append(f"{i1}markets: {js_val(mkt)},")
    
    lines.append(f"{i1}detailPage: {js_val(p.get('detailPage', False))},")
    lines.append(f"{i1}hybrids: {js_val(p.get('hybrids', []))}")
    
    lines.append(f"{i1}}},")
    
    return "\n".join(lines)

# Build the complete PRODUCTS array
all_products = existing_field + field_individuals + existing_veg + veg_individuals + existing_fodder + fodder_individuals

# Build JS file
js_parts = []

js_parts.append("""// ================================================================
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
js_parts.append("""  // ======================================================================
  // FIELD CROPS — Category Summary Cards (order 1-9)
  // ======================================================================
""")
for p in existing_field:
    js_parts.append(prod_to_js(p) + "\n")

if field_individuals:
    js_parts.append("""  // ----------------------------------------------------------------------
  // FIELD CROPS — Individual SKUs (order 10+)
  // ----------------------------------------------------------------------
""")
    for p in field_individuals:
        js_parts.append(prod_to_js(p) + "\n")

# Vegetables section
js_parts.append("""  // ======================================================================
  // VEGETABLES — Category Summary Cards (order 1-10)
  // ======================================================================
""")
for p in existing_veg:
    js_parts.append(prod_to_js(p) + "\n")

if veg_individuals:
    js_parts.append("""  // ----------------------------------------------------------------------
  // VEGETABLES — Individual SKUs (order 11+)
  // ----------------------------------------------------------------------
""")
    for p in veg_individuals:
        js_parts.append(prod_to_js(p) + "\n")

# Fodder section
js_parts.append("""  // ======================================================================
  // FODDER — Category Summary Cards (order 1-3)
  // ======================================================================
""")
for p in existing_fodder:
    js_parts.append(prod_to_js(p) + "\n")

if fodder_individuals:
    js_parts.append("""  // ----------------------------------------------------------------------
  // FODDER — Individual SKUs (order 4+)
  // ----------------------------------------------------------------------
""")
    for p in fodder_individuals:
        js_parts.append(prod_to_js(p) + "\n")

js_parts.append("""];

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

full_js = "".join(js_parts)

# Check size
size_kb = len(full_js) / 1024
print(f"\nGenerated JS file size: {size_kb:.1f} KB")
print(f"Total products: {len(all_products)}")

# If too large, trim descriptions
if size_kb > 100:
    print("WARNING: File too large! Need to trim.")
else:
    print("File size is good.")

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(full_js)

print(f"\nWritten to {OUTPUT_PATH}")

# ============================================
# STEP 4: Generate download.py
# ============================================

download_py = '''#!/usr/bin/env python3
"""
Download product images from old site.
Reads raw-scrape.json, downloads full-size images to images/products/.
Runs up to 3 parallel downloads using background processes.
"""
import json
import os
import subprocess
import sys
import time
import urllib.parse

BASE = r"C:\\\\Users\\\\kingo\\\\trimurti-redesign"
SCRAPE_PATH = os.path.join(BASE, "product-migration", "raw-scrape.json")
IMAGE_DIR = os.path.join(BASE, "images", "products")

os.makedirs(IMAGE_DIR, exist_ok=True)

with open(SCRAPE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]
total = len(products)

def get_full_size_url(url):
    """Convert Smush CDN thumbnail URL to full-size URL by removing '-300x300'."""
    if not url:
        return None
    # Remove query params first
    base = url.split("?")[0]
    # Remove the -300x300 or similar size suffix before the extension
    parts = base.rsplit(".", 1)
    if len(parts) == 2:
        name = parts[0]
        ext = parts[1]
        # Remove common size suffixes
        for suffix in ["-300x300", "-150x150", "-600x600", "-1024x1024", "-768x768", "_optimized"]:
            if name.endswith(suffix):
                name = name[:-len(suffix)]
                break
        return name + "." + ext
    return base

def download_image(url, filename):
    """Download a single image using curl with 30s timeout."""
    full_url = get_full_size_url(url)
    if not full_url:
        return False, "No URL"
    
    filepath = os.path.join(IMAGE_DIR, filename)
    
    if os.path.exists(filepath):
        return True, "Already exists"
    
    # Use curl with timeout and retry
    cmd = [
        "curl", "-s", "-S", "-L",
        "--connect-timeout", "15",
        "--max-time", "30",
        "--retry", "2",
        "--retry-delay", "3",
        "-o", filepath,
        full_url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=35)
        if result.returncode == 0:
            size = os.path.getsize(filepath)
            if size > 100:  # Minimum valid image size
                return True, f"OK ({size} bytes)"
            else:
                os.remove(filepath)
                return False, f"Too small ({size} bytes)"
        else:
            if os.path.exists(filepath):
                os.remove(filepath)
            return False, f"curl error {result.returncode}"
    except subprocess.TimeoutExpired:
        if os.path.exists(filepath):
            os.remove(filepath)
        return False, "Timeout"
    except Exception as e:
        if os.path.exists(filepath):
            os.remove(filepath)
        return False, str(e)

def main():
    # Collect download tasks
    tasks = []
    for p in products:
        code = p.get("code", "").strip()
        image_url = p.get("image_url", "") or ""
        if code and image_url:
            tasks.append((image_url, f"{code}.jpg"))
    
    print(f"Found {len(tasks)} images to download out of {total} products")
    
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
            if os.path.exists(filepath):
                skipped += 1
                continue
            
            full_url = get_full_size_url(url)
            cmd = [
                "curl", "-s", "-S", "-L",
                "--connect-timeout", "15",
                "--max-time", "30",
                "--retry", "2",
                "--retry-delay", "3",
                "-o", filepath,
                full_url
            ]
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            processes.append((proc, url, filename, filepath))
        
        for proc, url, filename, filepath in processes:
            try:
                stdout, stderr = proc.communicate(timeout=35)
                if proc.returncode == 0 and os.path.exists(filepath):
                    size = os.path.getsize(filepath)
                    if size > 100:
                        success += 1
                        print(f"  OK: {filename} ({size} bytes)")
                    else:
                        os.remove(filepath)
                        failed += 1
                        print(f"  FAIL: {filename} - too small ({size} bytes)")
                else:
                    if os.path.exists(filepath):
                        os.remove(filepath)
                    failed += 1
                    print(f"  FAIL: {filename} - curl error {proc.returncode}")
            except subprocess.TimeoutExpired:
                proc.kill()
                if os.path.exists(filepath):
                    os.remove(filepath)
                failed += 1
                print(f"  FAIL: {filename} - timeout")
        
        # Progress
        done = min(i + parallel, len(tasks))
        if done % 10 == 0 or done == len(tasks):
            print(f"Progress: {done}/{len(tasks)} (OK: {success}, Failed: {failed}, Skipped: {skipped})")
    
    print(f"\\n=== Download Complete ===")
    print(f"Total: {len(tasks)}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print(f"Skipped (already exists): {skipped}")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
'''

with open(DOWNLOAD_SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(download_py)

print(f"\nWritten download script to {DOWNLOAD_SCRIPT_PATH}")
print(f"Number of products with image_url and code: {sum(1 for p in products_raw if p.get('code','') and p.get('image_url',''))}")
