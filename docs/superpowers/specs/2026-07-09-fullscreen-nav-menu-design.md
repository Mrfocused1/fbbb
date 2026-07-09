# Full-screen nav menu

## Problem

The header's 16-item horizontal nav list overflows/crowds the header on desktop and doesn't work at all as a flat list on mobile.

## Design

**Header (all pages, mobile + desktop):** remove the horizontal `<ul>` nav list. Replace with a single hamburger icon button (pill background, brand gold/dark accent) placed next to the existing gold "Book Online" button, which is unchanged and stays always visible outside the menu.

**Menu overlay:** clicking the hamburger opens a full-screen fixed panel (fade/slide transition) covering the viewport:
- Logo top-left, close (✕) button top-right in the hamburger's former position
- Body scroll locks while open
- Escape key or a click on the overlay backdrop (outside the link list) closes it

**Link list:** the 16 sitemap pages (Home, About, Hair Academy, Beauty Academy, Wellness Academy, Professional Development, Business & Enterprise, AI for Beauty Professionals, CPD Masterclasses, One-to-One Training, Open Days, Student Support, Partners, Gallery, News & Insights, Contact) render as a single-column, large display-type numbered list (`01 Home`, `02 About`, ...).

- **Staggered entrance:** each link fades/slides in slightly after the previous one when the overlay opens, via CSS `transition-delay` per item (no JS animation library).
- **Desktop hover imagery:** hovering a link crossfades a background photo behind the list, for a curated subset of items that have a relevant existing downloaded asset (Home, Hair Academy, Beauty Academy, Wellness Academy, One-to-One Training, Gallery). Items without a mapped photo fall back to a subtle brand-color gradient background. No hover behavior on touch/mobile — same list, no imagery.

**Scope:** applies identically to `homepage-clone/`, `about-clone/`, and `contact-clone/` since they share the same header markup. Plain HTML/CSS/vanilla JS only, reusing existing site fonts/colors/assets — no new dependencies.

**Out of scope:** the mobile off-canvas panel implementation (`.header__mobile__bottom`) is being replaced by this same full-screen overlay, so both hamburgers (desktop nav + mobile duplicate) converge on one shared overlay markup/behavior instead of two separate nav instances.
