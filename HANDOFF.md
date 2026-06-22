# TriMurti Plant Sciences — Complete Handoff

## Project Overview

A 7-page static website redesign for **TriMurti Plant Sciences Private Limited**, a Hyderabad-based seed company. Built with vanilla HTML, CSS, and JS — no frameworks, no build step. Opens directly from the filesystem.

**Location:** `C:\Users\kingo\trimurti-redesign\`

---

## File Structure

```
trimurti-redesign/
├── index.html              # Homepage — hero, proof bar, crops, R&D, leadership, CTA
├── about.html              # Company story, 6 values, 3 leaders, timeline (2011→2021)
├── crops.html              # 3 catalog tables: field crops (9), vegetables (10), fodder (3)
├── facilities.html         # 4 facility cards + dark quality process section
├── research.html           # 4 R&D centres by agro-climatic zone + breeding priorities
├── contact.html            # Contact info + form + social links + map placeholder
├── partner.html            # Partner benefits (6 cards) + 3-step process + inquiry form
│
├── images/
│   └── trimurti-logo.png   # Official TriMurti logo (300×105 PNG)
│
├── css/
│   ├── base.css            # CSS variables, reset, typography, buttons, reveal animations
│   ├── layout.css          # Header, nav, mobile nav, search overlay, footer, responsive
│   ├── field-art.css       # Abstract field patterns, glow blobs, grain textures, card art
│   ├── home.css            # Hero, proof bar, cert strip, diff grid, crop grid, R&D, leadership, partner CTA
│   └── pages.css           # Inner page styles: banners, sub-nav, tables, facilities, contact, partner
│
└── js/
    └── main.js             # Scroll-reveal, counter animation, sticky header, mobile nav, search
```

**Total:** 14 files, ~4,300 lines, 220KB on disk.

---

## Brand Palette

| Token | Value | Usage |
|---|---|---|
| `--bg-darker` | `#161616` | Page banners, hero, crop section, footer |
| `--bg-dark` | `#1C1C1C` | Header, proof bar, partner CTA, quality cards |
| `--logo-green` | `#40A040` | Extracted from logo — available for future accents |
| `--gold` | `#C9A227` | Accent — buttons, highlights, decorative elements |
| `--bone` | `#F7F5EF` | Light section backgrounds, text on dark |
| `--green-700 / 800 / 900` | Dark greens | Button backgrounds, dropdowns, decorative elements |
| Inter font | Google Fonts | All body and heading text |

---

## Design Decisions

1. **Minimal header** — Only the logo image on desktop. Navigation is behind the hamburger menu (visible on mobile) and in the footer. Clean, brand-forward layout.

2. **Dark theme with green-gold accents** — Background references pulled from your screenshot (#1C1C1C range). Gold (#C9A227) provides contrast. Logo brand green (#40A040) available for future use.

3. **Local logo file** — `images/trimurti-logo.png` downloaded from the live site's CDN. All 4 logo instances (header, footer, mobile top, mobile bottom) reference this local file — no external URL dependency.

4. **SVG placeholder art** — Used throughout where photography is pending (leaders, facilities, hero visual). Marked with "photo pending" labels. Designed to be swapped with real images.

5. **Fully responsive** — Mobile, tablet, and desktop breakpoints. Mobile nav uses a full-screen overlay with sub-menu expand/collapse.

6. **No build step** — Pure HTML/CSS/JS. Open any `.html` file directly in a browser. Google Fonts loaded via CDN.

---

## Interactive Features

| Feature | Trigger | Details |
|---|---|---|
| Scroll-reveal animations | Page scroll | Sections fade + slide up on entering viewport |
| Counter animation | Scroll to proof bar | Numbers animate from 0 → target (2.5Mn, 150+, 5000+, 200K+) |
| Sticky header | Page scroll | Header darkens with blur backdrop after 60px |
| Mobile navigation | Hamburger icon | Full-screen overlay, sub-menu expand/collapse, close on Escape |
| Search overlay | Header search icon / Ctrl+K | Full-screen overlay with input, close on Escape |

---

## Key HTML Patterns

**Logo (header):**
```html
<a href="index.html" class="logo">
  <img class="logo-img" src="images/trimurti-logo.png" alt="TriMurti Plant Sciences">
</a>
```

**Logo (footer):**
```html
<div class="footer-brand-logo">
  <img class="logo-img" src="images/trimurti-logo.png" alt="TriMurti Plant Sciences" style="height:28px;width:auto;">
  <span class="logo-text">TriMurti</span>
</div>
```

**Mobile nav logo (top):**
```html
<img class="logo-img" src="images/trimurti-logo.png" alt="TriMurti" style="height:28px;width:auto;">
```

**Mobile nav logo (bottom):**
```html
<img class="logo-img" src="images/trimurti-logo.png" alt="TriMurti" style="height:32px;width:auto;">
```

---

## What's Still TODO

### Priority — Before Launch

1. **Replace "photo pending" SVGs** with actual photography:
   - Leader photos (about.html + index.html — 3 people)
   - Facility photos (facilities.html — 4 cards)
   - Hero visual art (index.html — SVG plant illustration)
   - R&D visual art (research.html + index.html — SVG lab building)
   - Story section art (about.html)

2. **Wire up contact forms** to a backend endpoint:
   - contact.html — general inquiry form
   - partner.html — distributor inquiry form
   - Currently uses `action="#"` — needs a real endpoint URL

3. **Replace certification placeholders** (index.html):
   - 5 "Logo space" boxes in `.cert-placeholder-row` → replace with actual certification logos

4. **Add real testimonials** (index.html):
   - `.testimonial-reserved` section — currently shows reserved placeholder

5. **No external URL dependencies remain** ✅ (logo is local)

### Enhancement Ideas

6. **Google Maps embed** — `contact.html` has a placeholder div `.map-placeholder` ready for an iframe

7. **Product images** — Add real photos to the crop cards (index.html) and crop tables (crops.html)

8. **SEO meta tags** — All pages have basic description; could add Open Graph / Twitter Card tags

9. **Favicon** — Currently an inline SVG favicon; replace with the actual brand favicon from the live site

---

## Deployment

The site is pure static HTML/CSS/JS — upload all files to any web server or static host:

1. Upload the entire `trimurti-redesign/` folder to your server's document root
2. No server-side processing needed (unless wiring up forms)
3. Update the logo path if deploying to a subdirectory (e.g., `/tri-murti/images/trimurti-logo.png`)

For local development: open any `.html` file directly in a browser at `file:///C:/Users/kingo/trimurti-redesign/index.html`.

---

## Tech Stack

- **HTML5** — Semantic markup with ARIA labels
- **CSS3** — Custom properties, Grid, Flexbox, backdrop-filter, Intersection Observer animations
- **JavaScript (vanilla)** — ~250 lines, ES6+, no dependencies
- **Google Fonts** — Inter (400, 500, 600, 700) via CDN
- **Logo** — `images/trimurti-logo.png` (300×105, 3.3KB PNG)

---

*Handoff prepared: June 22, 2026*
