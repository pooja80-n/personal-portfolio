#!/usr/bin/env python3
"""
Generates the 5 portfolio pages from shared header/footer/meta
components so every page stays structurally and accessibly
consistent. Run: python3 build.py
"""
import os

SITE_NAME = "Pooja N"
BASE_URL = "https://example.com"  # PLACEHOLDER — replace with the real deployed domain before publishing.
EMAIL = "poojan80500@gmail.com"
GITHUB = "https://github.com/pooja80-n"
LINKEDIN = "https://www.linkedin.com/in/pooja-n-74a72934a/"

PAGES = [
    ("index.html", "Home", "/"),
    ("about.html", "About", "/about.html"),
    ("skills.html", "Skills", "/skills.html"),
    ("projects.html", "Projects", "/projects.html"),
    ("contact.html", "Contact", "/contact.html"),
]

NAV_LABELS = [("index.html", "Home"), ("about.html", "About"),
              ("skills.html", "Skills"), ("projects.html", "Projects"),
              ("contact.html", "Contact")]


def build_nav(current_file):
    items = []
    for href, label in NAV_LABELS:
        current = ' aria-current="page"' if href == current_file else ''
        items.append(f'          <li><a href="{href}"{current}>{label}</a></li>')
    return "\n".join(items)


def build_head(title, description, path, extra_jsonld=""):
    canonical = BASE_URL + path
    return f"""  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="{SITE_NAME} — Portfolio" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{canonical}" />
  <meta name="twitter:card" content="summary" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="css/style.css" />
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
{extra_jsonld}"""


HEADER = """  <!-- Skip link must be the first focusable element on the page -->
  <a class="skip-link" href="#main-content">Skip to main content</a>

  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="index.html">
        Pooja N <span class="brand-mark" aria-hidden="true">ISE</span>
      </a>

      <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="primary-navigation">
        Menu
      </button>

      <!-- Native <nav> landmark; no extra ARIA role needed -->
      <nav class="site-nav" id="primary-navigation" aria-label="Primary">
        <ul class="nav-list">
{nav_items}
        </ul>
      </nav>
    </div>
  </header>
"""

FOOTER = f"""  <footer class="site-footer">
    <div class="wrap footer-inner">
      <p class="footer-note">&copy; <span id="year">2026</span> Pooja N. Built with semantic HTML5 and CSS.</p>
      <nav aria-label="Footer">
        <ul class="footer-links">
          <li><a href="{GITHUB}">GitHub</a></li>
          <li><a href="{LINKEDIN}">LinkedIn</a></li>
          <li><a href="mailto:{EMAIL}">Email</a></li>
        </ul>
      </nav>
    </div>
  </footer>
"""

SCRIPT_TAG = '  <script src="js/main.js" defer></script>\n'


def page_shell(file_name, title_tag, description, path, main_html, extra_jsonld=""):
    nav_items = build_nav(file_name)
    header_html = HEADER.format(nav_items=nav_items)
    head_html = build_head(title_tag, description, path, extra_jsonld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head_html}
</head>
<body>
{header_html}
  <main id="main-content">
{main_html}
  </main>
{FOOTER}{SCRIPT_TAG}</body>
</html>
"""


def write(file_name, content):
    with open(os.path.join(os.path.dirname(__file__), file_name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", file_name)
