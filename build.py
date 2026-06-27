"""
BUILD SCRIPT — TriMurti Website
===============================
Generates all pages from component partials + content data.

Usage:  python build.py
        python build.py --watch  (auto-rebuild on changes)

This solves the header/footer duplication issue.
Edit components/header.html or components/footer.html once —
all pages get updated on next build.
"""

import os, re, json, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
COMPONENTS = os.path.join(ROOT, "components")
PAGES = {
    # (src_template, output_filename, title, description)
    "index":    ("index", "index.html", "TriMurti Plant Sciences — Transforming Lives Through Superior Seeds", "Transforming lives through superior seeds."),
    "about":    ("subpage", "about.html", "About Us — TriMurti Plant Sciences", "Learn about TriMurti Plant Sciences."),
    "crops":    ("subpage", "crops.html", "Crops — TriMurti Plant Sciences", "Explore TriMurti's product portfolio."),
    "research": ("subpage", "research.html", "Research & Development — TriMurti Plant Sciences", "TriMurti's breeding programs."),
    "contact":  ("subpage", "contact.html", "Contact Us — TriMurti Plant Sciences", "Get in touch with TriMurti."),
    "partner":  ("subpage", "partner.html", "Partner with TriMurti — Distributor Opportunities", "Become a TriMurti distributor."),
    "careers":  ("subpage", "careers.html", "Careers — Join the TriMurti Team", "Join the TriMurti team."),
}

def build():
    # Read component files
    header_html = open(os.path.join(COMPONENTS, "subpage-header.html")).read()
    footer_html = open(os.path.join(COMPONENTS, "footer.html")).read()
    
    for key, (template, output, title, desc) in PAGES.items():
        # Read page content
        content_path = os.path.join(COMPONENTS, f"content-{key}.html")
        if not os.path.exists(content_path):
            print(f"  ⚠ Missing content file: content-{key}.html")
            continue
        
        content = open(content_path).read()
        
        # Assemble
        page = header_html.replace("<!--PAGE_TITLE-->", title)
        page = page.replace("<!--PAGE_DESC-->", desc)
        page += content
        page += footer_html
        page += "\n</body>\n</html>"
        
        # Write
        out_path = os.path.join(ROOT, output)
        open(out_path, "w").write(page)
        print(f"  ✓ {output}")

if __name__ == "__main__":
    print("Building TriMurti website...")
    build()
    print("Done!")
