# TriMurti Plant Sciences — Complete Handoff

**Last updated:** June 22, 2026  
**GitHub:** `github.com/manonamission9x/testing` — branch `main`  
**Deploy:** GitHub → Vercel (set Root Directory to `trimurti-redesign`)  
**Location:** `C:\Users\kingo\trimurti-redesign\`  

---

## Project Overview

A 9-page static website for **TriMurti Plant Sciences Private Limited**, a Hyderabad-based seed company. Built with vanilla HTML, CSS, and JS — no frameworks. Light/cream farming-positive theme with dark green accents and gold highlights. Phosphor icons via CDN.

---

## File Structure

```
trimurti-redesign/
├── index.html              # Homepage — hero carousel, proof bar, crops, R&D, leadership, CTA
├── about.html              # Company story, Mission, Values (6), The Trimurti Pledge, Leadership
├── crops.html              # Data-driven product catalog (22 products) — filters, search, PDFs
│
├── crops/                  # Individual crop detail pages (9 field crops)
│   ├── maize.html          #   Nagma, TMRH-1422, TMRH-871 + image slots
│   ├── rice.html           #   TMRH-221, TMRH-335, TMRH-448
│   ├── mustard.html        #   TMRH-511, TMRH-622, TMRH-733
│   ├── bajra.html          #   TMRB-101, TMRB-202
│   ├── jowar.html          #   TMRJ-301, TMRJ-402
│   ├── sunflower.html      #   TMRSF-501, TMRSF-602
│   ├── cotton.html         #   TMRC-701, TMRC-802
│   ├── green-gram.html     #   TMRG-901, TMRG-902
│   └── black-gram.html     #   TMRB-951, TMRB-952
│
├── research.html           # R&D — breeding focus, priorities (YIELD centre removed)
├── contact.html            # Contact form (→ info@trimurti.in) + Google Maps embed
├── partner.html            # "Partner with TriMurti" — distributor inquiry form
├── careers.html            # "Join the TriMurti Team" — career application + resume upload
├── thank-you.html          # Post-submission confirmation page
│
├── products-data.js        # ★ ALL 22 products here — add/edit/remove from this one file
├── build.py                # Build script — generates pages from components/*
│
├── components/
│   └── subpage-header.html # Canonical header + nav (edit once, rebuild all)
│
├── brochures/              # Upload PDF brochures here (linked from products-data.js)
├── images/
│   ├── trimurti-logo.png   # Official TriMurti logo
│   ├── hero/               # Hero background carousel (hero-1.jpg, hero-2.jpg, hero-3.jpg)
│   └── products/           # Product photos (e.g. maize.jpg — linked from products-data.js)
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
| `--gold` | `#C9A227` | Accent — badges, special traits, decorative |
| `--cream` | `#FAFAF5` | Light section backgrounds |
| `--white` | `#FFFFFF` | Main background |
| Inter font | Google Fonts | All body and heading text |
| Phosphor icons | CDN (`@phosphor-icons/web@2.1.1`) | All utility icons |

---

## Products Page — Data-Driven System

**Key file:** `products-data.js` — All 22 products are defined here as a JS array.  
**Card rendering:** `crops.html` reads `PRODUCTS` and generates cards dynamically.

### Each product has these fields:

```javascript
{
  id:"maize",               // Unique slug
  name:"Maize",             // Display name
  category:"field-crops",   // "field-crops" | "vegetables" | "fodder"
  type:"Hybrid",            // "Hybrid" | "Variety"
  code:"TMR-MZ",            // Internal product code
  active:true,              // false = hidden without deleting
  order:1,                  // Display order within category
  detailPage:true,          // true = links to crops/maize.html
  description:"...",        // Short description
  image:"images/products/maize.jpg",  // Product photo (optional)
  features:[                // Feature tags (shown as green pills)
    "Biotech & conventional options",
    "Kharif & Rabi seasons"
  ],
  region:"Central & Southern India",
  season:"Kharif / Rabi",
  duration:"95-115 days",
  special:"Pest tolerant",  // Special trait badge (gold)
  pdf:"brochures/maize.pdf",// Brochure PDF (optional)
  markets:"India, Nepal",
  hybrids:[                 // Hybrid/variety sub-items
    { name:"Nagma", desc:"Biotech Hybrid — Kharif" }
  ]
}
```

### To add/update products:
1. Open `products-data.js`
2. Add/edit/remove objects in the `PRODUCTS` array
3. Save — cards render automatically

---

## Forms

| Form | Routes to | Features |
|---|---|---|
| **Contact** | `info@trimurti.in` | Subject dropdown, CAPTCHA, thank-you redirect |
| **Careers** | `info@trimurti.in` | Resume upload (PDF/DOC), CAPTCHA |
| **Distributor** | `info@trimurti.in` | Business details enquiry, CAPTCHA |

All forms use **FormSubmit.co** (no backend needed). Submissions land in the inbox.  
Optional: Create a `thank-you.html` page (already exists).

---

## Interactive Features

| Feature | Trigger | Details |
|---|---|---|
| Hero background carousel | Page load | 3 images cycle every 5 seconds with fade transition |
| Scroll-reveal animations | Page scroll | Sections fade + slide up on entering viewport |
| Counter animation | Scroll to proof bar | Numbers animate 0 → target (2.5Mn, 150+, 5000+, 200K+) |
| Sticky header | Page scroll | White header with shadow after 60px |
| Mobile navigation | Hamburger icon | Full-screen overlay, sub-menu expand/collapse |
| Product filters | Category buttons | Show/hide by category (All / Field Crops / Vegetables / Fodder) |
| Product search | Input field | Real-time card filtering |
| Brochure download | Card button | Links to PDF in `brochures/` folder |
| Enquire button | Card button | Links to contact page with product name pre-filled |

---

## Deployment

### Vercel (Recommended)
1. Push to `github.com/manonamission9x/testing` → `main` branch
2. Go to [vercel.com](https://vercel.com) → **Add New → Project**
3. Import the `testing` repo
4. Set **Root Directory** to `trimurti-redesign`
5. Click **Deploy**

### Build Pipeline (optional)
```bash
python build.py     # Rebuilds pages from components/* partials
```
Run before deploy if you edit `components/subpage-header.html`.  
If you only edit `products-data.js` or individual HTML files, no build step needed.

---

## What's Still TODO

### Before Launch
1. **Upload product images** — Place JPG/WebP files in `images/products/` and set the `image` field in `products-data.js`
2. **Upload PDF brochures** — Place in `brochures/` folder and set the `pdf` field in `products-data.js`
3. **Replace hero background images** — Drop your photos into `images/hero/hero-1.jpg` through `hero-3.jpg` (1600×900 recommended)
4. **Replace "Add image" placeholders** on crop detail pages (`crops/maize.html` etc.) — each variety has an image slot
5. **Replace certification placeholders** (index.html) — 5 "Logo space" boxes
6. **Add real testimonials** (index.html) — reserved section
7. **Upload real product photos** for all 22 products

### Enhancement Ideas
8. **Add Open Graph / Twitter Card meta tags** for social sharing
9. **Replace inline SVG favicon** with actual brand favicon
10. **Set up Google Analytics** or similar
11. **Create a real CMS** — Migrate to Decap CMS for non-technical editing

---

## Change Log

| Date | Change | Files |
|---|---|---|
| Jun 22 | Initial full redesign — 7 pages, CSS, JS, light theme | All files |
| Jun 22 | Logo replaced with actual TriMurti PNG | All HTML files |
| Jun 22 | Light theme → dark theme → light theme again | CSS + HTML |
| Jun 22 | Navigation rebuilt with dropdowns (About, Products, R&D, Careers, Distributor, Contact) | All HTML files |
| Jun 22 | Products page rebuilt with data-driven cards | `products-data.js`, `crops.html` |
| Jun 22 | About page: Mission + Values + Pledge added, Journey removed | `about.html` |
| Jun 22 | R&D nav renamed, research centres removed, facilities delinked | `research.html`, all navs |
| Jun 22 | Careers "Join the TriMurti Team", Distributor "Partner with TriMurti" | `careers.html`, `partner.html` |
| Jun 22 | Hero background carousel added | `index.html`, `images/hero/` |
| Jun 22 | Forms wired to `info@trimurti.in` + CAPTCHA + thank-you page | `contact.html`, `careers.html`, `partner.html`, `thank-you.html` |
| Jun 22 | Google Maps embed added | `contact.html` |
| Jun 22 | Resume upload added to Careers form | `careers.html` |
| Jun 22 | Phosphor icons added (CDN), SVGs replaced | All HTML files |
| Jun 22 | Build system created (header/footer partials) | `build.py`, `components/` |
| Jun 22 | Image field added to product cards | `products-data.js`, `crops.html` |
| Jun 22 | Unused files deleted (facilities.html, templates) | — |
| Jun 22 | Pushed to `github.com/manonamission9x/testing` → `main` | — |

---

## Tech Stack

- **HTML5** — Semantic markup with ARIA labels
- **CSS3** — Custom properties, Grid, Flexbox, backdrop-filter
- **JavaScript (vanilla)** — ~280 lines, ES6+, no dependencies
- **Phosphor Icons** — via CDN (`@phosphor-icons/web@2.1.1`)
- **Google Fonts** — Inter (400, 500, 600, 700)
- **Logo** — `images/trimurti-logo.png` (300×105, 3.3KB PNG)
- **Forms** — FormSubmit.co (no backend)
- **GitHub** — `github.com/manonamission9x/testing` → `main`
- **Deploy target** — Vercel (static)
