# Spec: Clone the wellbeing-support page

Goal: produce a fully working, self-contained static clone of ONLY
https://www.licensedtradecharity.org.uk/wellbeing-support/ in a new folder
`wellbeing-support-clone/` at the repo root. The site owner has authorized
this clone of their own website. Follow the same approach already used for
`homepage-clone/` (see SPEC_clone_homepage.md and SPEC_serve_homepage.md in
this repo for reference on structure/conventions).

## Requirements

1. Fetch the live page HTML (`https://www.licensedtradecharity.org.uk/wellbeing-support/`).
2. Identify every asset referenced by the page: CSS, JS, web fonts, images
   (including responsive `srcset`/`data-src` variants), and any
   videos/embeds on the page.
3. Download all of those assets into `wellbeing-support-clone/assets/`
   organized by type (`assets/css`, `assets/js`, `assets/img`,
   `assets/fonts`, `assets/video`). Reuse identical shared assets already
   present in `homepage-clone/assets/` by copying them over rather than
   re-downloading, where the filenames match; download anything new.
4. Rewrite `wellbeing-support-clone/index.html` so every asset reference
   points to the downloaded local copy (relative paths) instead of the live
   URL. Leave third-party resources remote (Google Fonts CDN, analytics,
   Instagram embeds, cookie consent banner) exactly as was done for
   homepage-clone.
5. Preserve the page's structure, copy/content, layout, styling, and any
   CSS/JS-driven animations or interactions exactly as they appear live.
6. Strip anything that only works on the live WordPress backend and would
   visibly break locally (admin bar, nonce-based AJAX), same as before.
7. Add `wellbeing-support-clone/README.md` with a one-line local-view
   instruction, and add an `npm run start:wellbeing` script to the root
   `package.json` that runs `serve -l 4174 wellbeing-support-clone`
   (homepage-clone stays on its existing `start` script/port 4173 — don't
   touch that).

## Out of scope

- Do not touch homepage-clone/ or any other page/route of the site.
- Do not modify anything outside `wellbeing-support-clone/` other than the
  `package.json` script addition described above.
- Do not create git commits.
