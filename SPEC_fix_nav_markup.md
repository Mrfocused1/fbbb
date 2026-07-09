# Spec: Fix broken/orphaned nav markup in homepage-clone/index.html

## Bug

A previous edit truncated the header `<nav class="header-menu"><ul id="menu-header-menu">...</ul></nav>`
(and its mobile duplicate `<ul id="menu-header-menu-1">`) after the
"Contact" item, but left the remainder of the original menu's `<li>`
elements (which included a submenu under an "About Us" item, plus several
other page links) sitting AFTER the closing `</ul></nav>` tag, outside any
list/nav wrapper. These orphaned `<li>` elements — with link text such as
"About Us", "The LTC FAQ", "Our Schools", "History", "News", "Podcasts",
and similar — render as an unstyled flat list dumped directly into the
page body below the header, breaking the page layout (visible in a
screenshot: an ugly unstyled vertical link list appears right under the
header, pushing the hero content down).

There are two occurrences of this same corruption pattern in
`homepage-clone/index.html`: one following `id="menu-header-menu"`
(desktop nav) and one following `id="menu-header-menu-1"` (mobile
duplicate nav in `.header__mobile__bottom`).

## Fix

1. In both places, find the closing `</ul></nav>` that follows the
   "Contact" menu item, and locate the orphaned `<li>...</li>` elements
   that follow it (outside the closed tags) before the next legitimate
   sibling element/section begins.
2. Delete those orphaned `<li>` elements entirely (including any nested
   `<div class='sub-menu-wrapper'>...</div>` inside them) — the nav should
   contain ONLY: Home, About, Courses, CPD, One-to-One Training, Open
   Days, Gallery, FAQs, Contact, per the site's rebranded nav spec. Do not
   re-add or rename any of the orphaned items — just remove them cleanly
   so the HTML is well-formed (every `<li>` stays inside its `<ul>`).
3. Also fix a malformed attribute on the site logo link near
   `class="custom-logo-link"`: it currently reads
   `href=""https://www.fbbstrainingacademy.com/"` (an extra stray `"`
   right after `href=`). Fix it to `href="https://www.fbbstrainingacademy.com/"`.
4. After editing, verify the file has no orphaned `<li>` elements outside
   a `<ul>`, and that both `<ul id="menu-header-menu">` and
   `<ul id="menu-header-menu-1">` contain exactly the 9 nav items listed
   above and nothing else. Also grep for any other leftover old-brand page
   slugs (`/faq/`, `/our-courses/`, `/news/`, `/about-us/` when not
   pointing at a real new page) elsewhere in the file and remove similar
   orphaned fragments if the same corruption pattern repeats anywhere
   else in the document (e.g. re-check the whole file for `<li>` elements
   that are not descendants of any `<ul>`).
5. Do not touch `wellbeing-support-clone/` or `contact-clone/`.
6. Do not create git commits.
