# Trimurti Plant Sciences — Complete Handoff

**Last updated:** June 28, 2026  
**GitHub:** `github.com/manonamission9x/testing` — branch `main`  
**Deploy:** GitHub → Vercel (set Root Directory to `trimurti-redesign`)  
**Location:** `C:\Users\kingo\trimurti-redesign\`  
**Live URL:** `https://testing-mu-bay.vercel.app`

---

## Project Overview

A 9-page static website for **Trimurti Plant Sciences Private Limited**, a Hyderabad-based seed company. Built with vanilla HTML, CSS, and JS — no frameworks. Light/cream farming-positive theme with dark green accents and gold highlights. Phosphor icons via CDN.

Brand name is **Trimurti** (not TriMurti) — all files use this spelling.

---

## File Structure

```
trimurti-redesign/
├── index.html              # Homepage — hero carousel, proof bar, crops, R&D, leadership, CTA
├── about.html              # Company story, Mission, Values (6), Trimurti Pledge (3 langs), Trimurti Values (5), Leadership
├── crops.html              # ★ Product catalog — 198 individual product cards, filters, quality filters, search
├── admin.html              # ★ Product management panel — add/edit/delete/export products
│
├── crops/                  # Individual crop detail pages (mostly placeholder now — individual cards on crops.html replace these)
│   ├── maize.html
│   ├── rice.html
│   ├── mustard.html
│   ├── bajra.html
│   ├── jowar.html
│   ├── sunflower.html
│   ├── cotton.html
│   ├── green-gram.html
│   └── black-gram.html
│
├── research.html           # R&D — breeding focus, priorities
├── contact.html            # Contact form (→ info@trimurti.in) + Google Maps embed
├── partner.html            # "Partner with Trimurti" — distributor inquiry form
├── careers.html            # "Join the Trimurti Team" — career application + resume upload
├── thank-you.html          # Post-submission confirmation page
│
├── products-data.js        # ★ ALL 198 products across 21 crop groups — THE data source
├── build.py                # Build script — generates pages from components/* (deprecated)
│
├── components/
│   └── subpage-header.html # Canonical header + nav (edit once, rebuild all)
│
├── brochures/              # Upload PDF brochures here (linked from products-data.js)
├── images/
│   ├── trimurti-logo.png   # Official Trimurti logo
│   ├── hero/               # Hero background carousel (hero-1.jpg, hero-2.jpg, hero-3.jpg)
│   └── products/           # 148 product images (20 group + 128 individual from WooCommerce scrape)
│
├── css/
│   ├── base.css            # Variables, typography, buttons, animations
│   ├── layout.css          # Header, nav, mobile nav, search, footer
│   ├── home.css            # Hero, proof bar, crop grid, partner CTA
│   ├── pages.css           # Inner page styles, product cards
│   ├── field-art.css       # Abstract field patterns
│   └── crops-detail.css    # Crop detail page variety cards
│
└── js/
    └── main.js             # Scroll-reveal, counter animation, sticky header, mobile nav
```

---

## Brand Palette

| Token | Value | Usage |
|---|---|---|
| `--bg-darker` | `#0A1A0F` | Footer, partner CTA |
| `--bg-dark` | `#0F2818` | Hero overlay, dark accents |
| `--green-600` | `#245C3C` | Primary buttons, active filters |
| `--logo-green` | `#40A040` | Logo brand green |
| `--gold` | `#C9A227` | Accent — badges, decorative |
| `--cream` | `#FAFAF5` | Light section backgrounds |
| `--white` | `#FFFFFF` | Main background |
| Inter font | Google Fonts | All body and heading text |
| Phosphor icons | CDN (`@phosphor-icons/web@2.1.1`) | All utility icons |

---

## Products Page (crops.html)

The product catalog was **rebuilt from scratch** with data scraped from the old `trimurti.in` WooCommerce site.

### Data Source

- **208 raw products** scraped via WooCommerce Store API (`/wp-json/wc/store/v1/products`)
- **Deduplicated to 198 unique** products (10 removed for being in multiple categories)
- Organized into **21 crop groups** (single group per crop — Rice is ONE group, not split by Hybrids/Varieties)

### The 21 Crop Groups

| # | Group | Category | Products |
|---|---|---|---|
| 1 | Maize | field-crops | 31 |
| 2 | Rice | field-crops | 56 |
| 3 | Mustard | field-crops | 13 |
| 4 | Bajra (Pearl Millet) | field-crops | 5 |
| 5 | Jowar (Sorghum) | field-crops | 3 |
| 6 | Sunflower | field-crops | 1 |
| 7 | Wheat | field-crops | 2 |
| 8 | Nepal Products | field-crops | 5 |
| 9 | Tomato | vegetables | 12 |
| 10 | Chilli | vegetables | 17 |
| 11 | Okra (Lady Finger) | vegetables | 14 |
| 12 | Cucumber | vegetables | 4 |
| 13 | Bottle Gourd | vegetables | 4 |
| 14 | Bitter Gourd | vegetables | 4 |
| 15 | Sponge / Ridge Gourd | vegetables | 3 |
| 16 | Pumpkin | vegetables | 3 |
| 17 | Cabbage | vegetables | 3 |
| 18 | Cauliflower | vegetables | 2 |
| 19 | Watermelon | vegetables | 10 |
| 20 | Sweetcorn | vegetables | 1 |
| 21 | Maize & Sorghum Fodder | fodder | 5 |

### Page Features

- **Product cards:** Each of the 198 products gets its OWN card with individual image (from WooCommerce), name, description, season badges, duration badge, Enquire button
- **Category filter:** All / Field Crops / Vegetables / Fodder
- **Sub-category filter:** By crop type (Maize, Rice, Tomato, etc.)
- **Quality filters:** Season (Kharif / Rabi / Summer) + Type (Hybrid / Variety)
- **Search:** Real-time filtering by product name or code
- **Images:** 197/198 products have their own image; 1 Cabbage product shows no image (no broken placeholder)
- **localStorage:** NOT loaded from localStorage — always reads from the file to prevent stale admin data

---

## Admin Panel (admin.html)

A browser-based product manager. Open `admin.html` to use it.

### How It Works

1. Loads product data from `products-data.js` into memory
2. All edits are saved to the browser's **localStorage** (key: `trimurti_products`)
3. To publish: go to **🔧 Export / Import** tab → click **⬇ Download products-data.js**
4. Replace the file in the project → git commit → git push

### Tabs

| Tab | Purpose |
|---|---|
| **📋 Products** | Table with inline editing, search, filters, bulk actions |
| **➕ Add Product** | Form to add new products with all fields |
| **🏷️ Categories** | Manage field-crops / vegetables / fodder categories |
| **🔧 Export / Import** | Download updated products-data.js or import a replacement |
| **❓ Help** | Full documentation (updated) |

### Product Data Format

```javascript
{
  id:"maize",               // unique slug
  name:"Maize",             // display name for sub-filter tab
  category:"field-crops",   // "field-crops" | "vegetables" | "fodder"
  type:"Hybrid",            // "Hybrid" | "Variety"
  code:"TMMH",              // product code prefix
  active:true,              // false = hidden
  order:1,                  // display order within category
  description:"...",        // shown above the product grid
  image:"images/products/maize.png",  // group image (optional)
  features:[],              // feature tags
  region:"All India",
  season:"Kharif / Rabi",
  duration:"120-125days",
  special:"Hybrid Maize",   // special trait badge
  pdf:"brochures/maize.pdf",// brochure PDF (optional)
  markets:"India",
  hybrids:[                 // ★ each becomes an individual product card
    {name:"TMMH 846", desc:"Premium maize hybrid...", img:"https://..."},
    ...
  ]
}
```

The `hybrids[]` array is where individual products live. Each entry becomes a product card. Each hybrid has:
- `name` — product name (shown as card heading)
- `desc` — description (shown on the card)
- `img` — image URL (remote or local path)

---

## Images

### How Images Work

Two methods:

1. **Remote URLs (current):** 197/198 products use WooCommerce CDN URLs (`https://trimurti.in/wp-content/uploads/...`). These work as long as the old site stays online.

2. **Local files:** Save images to `images/products/` and reference as `images/products/your-file.jpg`. Commit the image file to GitHub. Works for all visitors once deployed.

### Currently on Disk

20 group images were downloaded to `images/products/` (maize.png, rice.png, mustard.png, etc.). These are referenced in the `image` field of each product group in products-data.js.

---

## About Page (about.html)

### Sections (in order)

1. **Page Banner** — "Seed professionals, not just seed sellers"
2. **Our Story (Inception)** — Founded 2011 by Raghu Vasu A
3. **Our Mission** — Text section
4. **Our Values** — 6 cards: Science First, Quality Without Compromise, Regional Relevance, Partner-Centric, Long-Term Horizon, Farmer Success
5. **The Trimurti Pledge** — Multilingual (Hindi / English / Telugu), no images
6. **Trimurti Values** — 5 cards with Phosphor icons: Farmer Centricity, Innovation & Quality, Responsibility & Ownership, Teamwork, Integrity
7. **Leadership Team** — 3 leaders with bios
8. **Partner CTA**

### Leadership Bios Updated

- **Raghu Vasu A:** "25 years of leadership experience in the seed industry"
- **Dr. Syamal Krishna Ghosh:** "was with Trimurti since Inception"
- **Dr. Pankaj Kumar Singh:** "with Trimurti since 2016"

---

## Forms

| Form | Routes to | Features |
|---|---|---|
| **Contact** | `info@trimurti.in` | Subject dropdown, CAPTCHA, thank-you redirect |
| **Careers** | `info@trimurti.in` | Resume upload (PDF/DOC), CAPTCHA |
| **Distributor** | `info@trimurti.in` | Business details enquiry, CAPTCHA |

All forms use **FormSubmit.co** (no backend needed).

---

## Interactive Features

| Feature | Trigger | Details |
|---|---|---|
| Hero background carousel | Page load | 3 images cycle every 5s with fade |
| Scroll-reveal animations | Page scroll | Sections fade + slide up |
| Counter animation | Scroll to proof bar | Numbers animate 0 → target |
| Sticky header | Page scroll | White header with shadow after 60px |
| Mobile navigation | Hamburger icon | Full-screen overlay |
| Product category filter | Buttons | All / Field Crops / Vegetables / Fodder |
| Product sub-category filter | Buttons | By crop type (Maize, Rice, etc.) |
| Quality filter (Season) | Buttons | Kharif / Rabi / Summer |
| Quality filter (Type) | Buttons | Hybrid / Variety |
| Product search | Input field | Real-time by name or code |
| Enquire button | Card button | → contact.html with product pre-filled |

---

## Deployment

### Vercel (Current)

1. Push to `github.com/manonamission9x/testing` → `main` branch
2. Vercel auto-deploys (connected to the repo)
3. Root Directory is set to `trimurti-redesign`
4. Deploy takes ~20 seconds after push

### To Update Products

1. Open `admin.html` in your browser
2. Make edits (auto-saves to browser)
3. Go to **🔧 Export / Import** → click **⬇ Download products-data.js**
4. Replace `products-data.js` in the project folder with the downloaded file
5. `git add products-data.js && git commit -m "update products" && git push`

---

## What's Still TODO

1. **Replace hero background images** — Drop your photos into `images/hero/hero-1.jpg` through `hero-3.jpg` (1600×900 recommended)
2. **Replace certification placeholders** (index.html) — 5 "Logo space" boxes
3. **Add real testimonials** (index.html) — reserved section
4. **Remove crop/ detail pages or update them** — The individual `crops/maize.html` etc. are deprecated since crops.html now shows all products as individual cards
5. **Add Open Graph / Twitter Card meta tags** for social sharing
6. **Replace inline SVG favicon** with actual brand favicon
7. **Set up Google Analytics** or similar

---

## Change Log

| Date | Change | Files |
|---|---|---|
| Jun 22 | Initial full redesign | All files |
| Jun 28 | Scraped 208 WooCommerce products → 198 unique across 21 groups | `products-data.js` |
| Jun 28 | Rebuilt crops.html with individual product cards + quality filters | `crops.html` |
| Jun 28 | Added admin.html product management panel | `admin.html` |
| Jun 28 | Removed localStorage loading from crops.html (public page = file only) | `crops.html` |
| Jun 28 | Multilingual Trimurti Pledge (Hindi/English/Telugu) added | `about.html` |
| Jun 28 | Trimurti Values section (5 values) with Phosphor icons added | `about.html` |
| Jun 28 | Leadership bios updated (Raghu: 25yr leadership, Ghosh: since Inception) | `about.html` |
| Jun 28 | Global TriMurti → Trimurti rename across all 9 pages | All HTML files |
| Jun 28 | 20 product group images downloaded to `images/products/` | 20 image files |
| Jun 28 | Updated admin.html Help tab with full workflow docs | `admin.html` |
| Jun 28 | This handoff document updated | `HANDOFF.md` |

---

## Tech Stack

- **HTML5** — Semantic markup with ARIA labels
- **CSS3** — Custom properties, Grid, Flexbox, backdrop-filter
- **JavaScript (vanilla)** — No frameworks, no dependencies
- **Phosphor Icons** — via CDN (`@phosphor-icons/web@2.1.1`)
- **Google Fonts** — Inter (400, 500, 600, 700)
- **Logo** — `images/trimurti-logo.png`
- **Forms** — FormSubmit.co (no backend)
- **GitHub** — `github.com/manonamission9x/testing` → `main`
- **Deploy target** — Vercel (static)
