# Licensed Trade Charity Homepage Clone

Static clone of https://www.licensedtradecharity.org.uk/ homepage.

## How to view locally

```bash
npx serve homepage-clone
```

Or use any static file server:

```bash
python3 -m http.server 8000 --directory homepage-clone
```

Then open http://localhost:8000 in your browser.

## What's included

- Homepage HTML with all internal assets downloaded locally
- CSS/JS files from the original site
- Images, SVGs, and other media assets
- Third-party resources (Instagram feeds, Google Fonts, analytics) remain remote

## Notes

- Navigation links point to the live site
- Instagram feed images are loaded from Instagram's CDN
- Cookie consent and analytics scripts remain connected to original services
- WordPress admin functionality has been removed
