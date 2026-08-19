# Pooja N — Portfolio

A 5-page static portfolio built with semantic HTML5, hand-written CSS (no
framework), and a small amount of vanilla JavaScript for the mobile nav
toggle and contact-form validation.

## Project structure

```
portfolio/
├── index.html        Home
├── about.html         About (education, certifications, activities)
├── skills.html        Skills
├── projects.html       Projects
├── contact.html        Contact (with accessible form)
├── robots.txt
├── sitemap.xml
├── css/
│   └── style.css      All styling — design tokens, layout, components
├── js/
│   └── main.js         Mobile nav toggle + contact form validation
├── assets/
│   └── favicon.svg     Monogram favicon (no personal photo was supplied)
├── build.py             Generator: shared header/footer/meta components
├── pages.py              Generator: per-page content, writes the .html files
└── README.md
```

`build.py` and `pages.py` are the source of truth — they generate the five
HTML files so the header, footer, and metadata pattern stay identical across
pages. If you want to edit copy, it's easiest to edit `pages.py` and rerun
`python3 pages.py`, but you can also edit the generated `.html` files
directly; nothing else depends on the generator at runtime.

## Before you deploy

- `build.py` uses `https://example.com` as a **placeholder** base URL for
  canonical links, Open Graph tags, JSON-LD, `robots.txt`, and
  `sitemap.xml`. Replace it with your real domain once you know it (search
  for `example.com` across the project), then rerun `python3 pages.py`.
- The Experience & Activities section on the About page uses clearly marked
  placeholder text, since no specific hackathons/internships/events were
  provided. Replace those `<p class="placeholder-note">` entries with real
  details when you have them.
- No headshot photo was supplied, so the hero uses a decorative SVG graphic
  instead of a fabricated photo. Swap in a real photo (with meaningful alt
  text) if you'd like one.

## Running it locally

No build step or server-side code is required — it's static HTML/CSS/JS.

**Option A — just open it:**
Double-click `index.html`, or open it from your browser's File menu.
(The contact form's `mailto:` fallback and internal links work fine this
way. Some browsers restrict `fetch`-based features under `file://`, but this
site doesn't use any.)

**Option B — serve it locally (recommended for accurate Lighthouse results):**

```bash
cd portfolio
python3 -m http.server 8000
```

Then visit `http://localhost:8000` in your browser.

If you have Node.js installed, `npx serve .` from the `portfolio` folder
works the same way.

## Testing with Chrome Lighthouse

1. Serve the site locally (Option B above) — Lighthouse results on `file://`
   URLs can be less reliable than on `http://`.
2. Open `http://localhost:8000` in Google Chrome.
3. Open DevTools (`F12` or `Ctrl+Shift+I` / `Cmd+Option+I`).
4. Go to the **Lighthouse** tab.
5. Select the **Accessibility** and **SEO** categories (and Performance/Best
   Practices if you'd like), choose **Desktop** or **Mobile**, then click
   **Analyze page load**.
6. Repeat for each of the five pages — scores are calculated per page, not
   per site.
7. For a keyboard/screen-reader pass alongside Lighthouse: tab through each
   page to confirm the skip link, nav, and form all work without a mouse,
   and check the "Accessibility" panel in DevTools or a screen reader (VoiceOver,
   NVDA, or ChromeVox) for anything Lighthouse's automated checks can't catch
   (Lighthouse audits are a strong baseline but do not replace manual
   testing).

This build has **not** been run through Lighthouse yet — the structural,
semantic, and contrast choices above are designed to score well, but you
should run the audit yourself before citing a specific score.
