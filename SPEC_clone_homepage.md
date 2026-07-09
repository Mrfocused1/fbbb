# Spec: Clone homepage of licensedtradecharity.org.uk

Goal: produce a fully working, self-contained static clone of ONLY the
homepage of https://www.licensedtradecharity.org.uk/ in a new folder
`homepage-clone/` at the repo root. The site owner has authorized this
clone of their own website.

## Requirements

1. Fetch the live homepage HTML (`https://www.licensedtradecharity.org.uk/`).
2. Identify every asset referenced by the homepage: CSS files, JS files,
   web fonts, images (including responsive `srcset`/`data-src` variants),
   and any videos/embeds used in the hero/banner or elsewhere on the page.
3. Download all of those assets into `homepage-clone/assets/` organized by
   type (e.g. `assets/css`, `assets/js`, `assets/img`, `assets/fonts`,
   `assets/video`). Use `curl` or `wget` with a normal browser User-Agent.
4. Rewrite `homepage-clone/index.html` so every asset reference points to
   the downloaded local copy (relative paths) instead of the live URL —
   the page must render correctly when opened locally / served via a
   simple static file server, with no dependency on the live site except
   for things that must stay remote (e.g. Google Fonts CDN, analytics
   scripts, embedded third-party widgets like a cookie consent banner —
   those may be left pointing at their original URLs).
5. Preserve the page's structure, copy/content, layout, styling, and any
   CSS/JS-driven animations or interactions (e.g. scroll effects, sliders,
   accordions, nav menu behavior) exactly as they appear on the live site.
6. Strip anything that only makes sense on the live WordPress backend and
   would break locally (e.g. admin bar, nonce-based AJAX calls that require
   a live PHP backend) — but only if it would visibly break the page;
   otherwise leave functionality intact.
7. Add a minimal `homepage-clone/README.md` with one line on how to view it
   locally (e.g. `npx serve homepage-clone`).

## Out of scope

- Do not touch any other page/route of the site — homepage only.
- Do not modify anything outside `homepage-clone/` other than adding the
  README inside it.
- Do not create git commits.
