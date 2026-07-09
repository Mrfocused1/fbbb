# Full-Screen Nav Menu Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the crowded 16-item horizontal header nav with a single hamburger button that opens a full-screen, staggered-animation link overlay, on all three pages.

**Architecture:** One shared markup/CSS/JS fragment is authored once against `homepage-clone/index.html`, verified by rendering in a local static server, then the same fragment is applied to `about-clone/index.html` and `contact-clone/index.html`. No test framework exists in this static-HTML project — "tests" here mean curl/grep structural checks plus an actual rendered-page check (per project convention: UI changes must be visually verified before being called done, not just diffed).

**Tech Stack:** Plain HTML, CSS (added to the existing inline `<style id="wpr-usedcss">` block for homepage-clone/about-clone, and `contact.css` for contact-clone), vanilla JS (no new dependencies).

---

### Task 1: Build and verify the overlay on homepage-clone

**Files:**
- Modify: `homepage-clone/index.html` (header markup, inline CSS block, add a `<script>` block before `</body>`)

- [ ] **Step 1: Remove the old flat nav `<ul>` and mobile duplicate, add the hamburger trigger**

In `homepage-clone/index.html`, replace the `<div class="header__nav">...</div>` block (containing `<ul id="menu-header-menu">`) with just a single trigger button:

```html
<button type="button" id="nav-menu-trigger" class="nav-menu-trigger" aria-label="Open menu" aria-expanded="false" aria-controls="nav-menu-overlay">
    <span></span><span></span><span></span>
</button>
```

Remove the entire `<div class="header__mobile__bottom">...</div>` block (the old mobile duplicate nav/CTA/social panel) — the overlay built in Step 2 replaces it for both mobile and desktop. Remove the now-orphaned `.header__mobile__hamburger` markup (the old two-image hamburger icon) since `#nav-menu-trigger` replaces it.

- [ ] **Step 2: Add the overlay markup right after `<header ...>` opens (as the first child, so it's not nested inside `.header_content`)**

```html
<div id="nav-menu-overlay" class="nav-menu-overlay" aria-hidden="true">
    <div class="nav-menu-overlay__backdrop" data-nav-close></div>
    <div class="nav-menu-overlay__panel">
        <div class="nav-menu-overlay__top">
            <a href="/" class="nav-menu-overlay__logo">
                <img src="assets/img/Layer_1-1.svg" alt="FBBS Training Academy">
            </a>
            <button type="button" class="nav-menu-overlay__close" data-nav-close aria-label="Close menu">&#10005;</button>
        </div>
        <nav class="nav-menu-overlay__list" aria-label="Site">
            <a href="/" class="nav-menu-overlay__link" data-bg="assets/img/Licenced-Trade-Charity-serving-drinks-people-since-1793-medium.jpg" style="transition-delay:0.03s"><span class="nav-menu-overlay__num">01</span><span>Home</span></a>
            <a href="/about/" class="nav-menu-overlay__link" style="transition-delay:0.06s"><span class="nav-menu-overlay__num">02</span><span>About</span></a>
            <a href="/hair-academy/" class="nav-menu-overlay__link" data-bg="assets/img/Fleet-Street-Comms_LTC-Campaign__Group_04-1.jpg" style="transition-delay:0.09s"><span class="nav-menu-overlay__num">03</span><span>Hair Academy</span></a>
            <a href="/beauty-academy/" class="nav-menu-overlay__link" data-bg="assets/img/DSC00481.webp" style="transition-delay:0.12s"><span class="nav-menu-overlay__num">04</span><span>Beauty Academy</span></a>
            <a href="/wellness-academy/" class="nav-menu-overlay__link" data-bg="assets/img/CC-Juniors-Grounds-2-1-768x513.jpg" style="transition-delay:0.15s"><span class="nav-menu-overlay__num">05</span><span>Wellness Academy</span></a>
            <a href="/professional-development/" class="nav-menu-overlay__link" style="transition-delay:0.18s"><span class="nav-menu-overlay__num">06</span><span>Professional Development</span></a>
            <a href="/business-enterprise/" class="nav-menu-overlay__link" style="transition-delay:0.21s"><span class="nav-menu-overlay__num">07</span><span>Business &amp; Enterprise</span></a>
            <a href="/ai-for-beauty-professionals/" class="nav-menu-overlay__link" style="transition-delay:0.24s"><span class="nav-menu-overlay__num">08</span><span>AI for Beauty Professionals</span></a>
            <a href="/cpd-masterclasses/" class="nav-menu-overlay__link" style="transition-delay:0.27s"><span class="nav-menu-overlay__num">09</span><span>CPD Masterclasses</span></a>
            <a href="/one-to-one-training/" class="nav-menu-overlay__link" data-bg="assets/img/Screenshot-2026-01-19-160820-1.png" style="transition-delay:0.30s"><span class="nav-menu-overlay__num">10</span><span>One-to-One Training</span></a>
            <a href="/open-days/" class="nav-menu-overlay__link" style="transition-delay:0.33s"><span class="nav-menu-overlay__num">11</span><span>Open Days</span></a>
            <a href="/student-support/" class="nav-menu-overlay__link" style="transition-delay:0.36s"><span class="nav-menu-overlay__num">12</span><span>Student Support</span></a>
            <a href="/partners/" class="nav-menu-overlay__link" style="transition-delay:0.39s"><span class="nav-menu-overlay__num">13</span><span>Partners</span></a>
            <a href="/gallery/" class="nav-menu-overlay__link" data-bg="assets/img/Rectangle-5.png" style="transition-delay:0.42s"><span class="nav-menu-overlay__num">14</span><span>Gallery</span></a>
            <a href="/news-insights/" class="nav-menu-overlay__link" style="transition-delay:0.45s"><span class="nav-menu-overlay__num">15</span><span>News &amp; Insights</span></a>
            <a href="/contact/" class="nav-menu-overlay__link" style="transition-delay:0.48s"><span class="nav-menu-overlay__num">16</span><span>Contact</span></a>
        </nav>
    </div>
</div>
```

- [ ] **Step 3: Add CSS.** Insert immediately before the closing `</style>` of `<style id="wpr-usedcss">`:

```css
.nav-menu-trigger{width:44px;height:44px;border-radius:50%;background:var(--main-color);border:none;cursor:pointer;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;flex-shrink:0}
.nav-menu-trigger span{display:block;width:20px;height:2px;background:var(--tertiary-bg)}
.nav-menu-overlay{position:fixed;inset:0;z-index:10000;visibility:hidden;opacity:0;transition:opacity .35s ease,visibility 0s linear .35s}
.nav-menu-overlay.is-open{visibility:visible;opacity:1;transition:opacity .35s ease}
.nav-menu-overlay__backdrop{position:absolute;inset:0;background:var(--tertiary-bg,#1a2e29)}
.nav-menu-overlay__panel{position:relative;height:100%;width:100%;overflow-y:auto;display:flex;flex-direction:column;padding:24px}
.nav-menu-overlay__top{display:flex;align-items:center;justify-content:space-between}
.nav-menu-overlay__logo img{height:40px;width:auto}
.nav-menu-overlay__close{width:44px;height:44px;border-radius:50%;background:transparent;border:1px solid var(--main-color);color:var(--main-color);font-size:18px;cursor:pointer}
.nav-menu-overlay__list{margin:auto;display:flex;flex-direction:column;gap:4px;width:100%;max-width:900px}
.nav-menu-overlay__link{display:flex;align-items:baseline;gap:20px;font-family:'FSAlbert Bold',sans-serif;font-size:clamp(28px,6vw,64px);color:var(--main-color);text-decoration:none;padding:10px 20px;border-radius:12px;opacity:0;transform:translateY(16px);transition:opacity .4s ease,transform .4s ease,background-color .25s ease}
.nav-menu-overlay.is-open .nav-menu-overlay__link{opacity:1;transform:translateY(0)}
.nav-menu-overlay__num{font-size:16px;font-family:'FSAlbert Regular',sans-serif;opacity:.6;width:28px}
@media(hover:hover){.nav-menu-overlay__link:hover{background-color:rgba(253,141,28,.12)}}
.nav-menu-overlay__panel.has-bg:before{content:"";position:absolute;inset:0;background-size:cover;background-position:center;opacity:0;transition:opacity .3s ease;z-index:-1}
body.nav-open{overflow:hidden}
@media(max-width:600px){.nav-menu-overlay__link{font-size:28px;gap:12px}}
```

- [ ] **Step 4: Add JS.** Insert a new `<script>` block right before `</body>`:

```html
<script>
(function(){
    var trigger = document.getElementById('nav-menu-trigger');
    var overlay = document.getElementById('nav-menu-overlay');
    if(!trigger || !overlay) return;
    var panel = overlay.querySelector('.nav-menu-overlay__panel');
    var links = overlay.querySelectorAll('.nav-menu-overlay__link');

    function openMenu(){
        overlay.classList.add('is-open');
        overlay.setAttribute('aria-hidden','false');
        trigger.setAttribute('aria-expanded','true');
        document.body.classList.add('nav-open');
    }
    function closeMenu(){
        overlay.classList.remove('is-open');
        overlay.setAttribute('aria-hidden','true');
        trigger.setAttribute('aria-expanded','false');
        document.body.classList.remove('nav-open');
    }
    trigger.addEventListener('click', openMenu);
    overlay.querySelectorAll('[data-nav-close]').forEach(function(el){
        el.addEventListener('click', closeMenu);
    });
    document.addEventListener('keydown', function(e){
        if(e.key === 'Escape' && overlay.classList.contains('is-open')) closeMenu();
    });
    links.forEach(function(link){
        var bg = link.getAttribute('data-bg');
        if(!bg) return;
        link.addEventListener('mouseenter', function(){
            panel.style.backgroundImage = 'url(' + bg + ')';
            panel.classList.add('has-bg');
        });
        link.addEventListener('mouseleave', function(){
            panel.classList.remove('has-bg');
        });
    });
})();
</script>
```

- [ ] **Step 5: Verify structurally**

Run:
```bash
python3 -c "
html = open('homepage-clone/index.html', encoding='utf-8').read()
assert html.count(chr(34)) % 2 == 0, 'quote parity broken'
assert 'nav-menu-trigger' in html
assert html.count('nav-menu-overlay__link') == 16
print('OK')
"
```
Expected: `OK`

- [ ] **Step 6: Verify by rendering**

Start (or reuse) the local server for this page (`npx serve -l 4173 homepage-clone`), then in a headless/real browser: load `http://localhost:4173/`, confirm the hamburger button renders, click it, confirm the overlay opens with the 16 staggered links, hover a mapped link (e.g. "Hair Academy") and confirm the background photo crossfades in, press Escape and confirm it closes. This is a hard requirement per project convention — do not mark this task done from code inspection alone.

- [ ] **Step 7: Commit**

```bash
git add homepage-clone/index.html
git commit -m "replace crowded header nav with single-button full-screen menu overlay"
```

---

### Task 2: Apply the same overlay to about-clone

**Files:**
- Modify: `about-clone/index.html`

- [ ] **Step 1:** Repeat Task 1 Steps 1–4 verbatim against `about-clone/index.html` (same markup/CSS/JS — about-clone shares the identical header/CSS-block structure as homepage-clone since it was cloned from the same theme).
- [ ] **Step 2:** Run the same Step 5 structural check, substituting the file path.
- [ ] **Step 3:** Render-check per Task 1 Step 6 against `http://localhost:4174/` (about-clone's dev server).
- [ ] **Step 4: Commit**

```bash
git add about-clone/index.html
git commit -m "apply full-screen nav menu overlay to about-clone"
```

---

### Task 3: Apply the same overlay to contact-clone

**Files:**
- Modify: `contact-clone/index.html`

contact-clone is a hand-authored simpler page (its own `<style>`/no huge inline critical-CSS block) — the nav `<ul>` there is a plain flat list, not the WordPress-generated markup from Task 1.

- [ ] **Step 1:** Replace contact-clone's `<div class="header__nav">...</div>` block (containing `<ul id="menu-header-menu">`) with the same `#nav-menu-trigger` button markup from Task 1 Step 1.
- [ ] **Step 2:** Insert the same overlay markup from Task 1 Step 2 as the first child inside `<header class="header">`, adjusting `data-bg` image paths to `/assets/img/...` (contact-clone already references shared images at root-absolute `/assets/...` per its existing asset-path convention — see `contact-clone/index.html`'s existing `src="/assets/img/Layer_1-1.svg"`).
- [ ] **Step 3:** Append the CSS block from Task 1 Step 3 to `contact-clone/contact.css` (not an inline `<style>` block, since contact-clone uses an external stylesheet).
- [ ] **Step 4:** Add the JS block from Task 1 Step 4 before `</body>` in `contact-clone/index.html`.
- [ ] **Step 5:** Run the same structural check from Task 1 Step 5 against `contact-clone/index.html`.
- [ ] **Step 6:** Render-check per Task 1 Step 6 against `http://localhost:4175/`.
- [ ] **Step 7: Commit**

```bash
git add contact-clone/index.html contact-clone/contact.css
git commit -m "apply full-screen nav menu overlay to contact-clone"
```

---

### Task 4: Redeploy

**Files:**
- Modify: `deploy/` (rebuilt from the three source folders, not hand-edited)

- [ ] **Step 1:** Rebuild the deploy bundle:

```bash
cd /Users/paulbridges/Desktop/fbbb
rm -rf deploy
mkdir -p deploy
cp -R homepage-clone/. deploy/
mkdir -p deploy/about && cp -R about-clone/. deploy/about/
mkdir -p deploy/contact && cp -R contact-clone/. deploy/contact/
find deploy -name "clone_assets.py" -delete
find deploy -name "README.md" -delete
```

- [ ] **Step 2:** Deploy to production:

```bash
cd deploy && vercel --prod --yes
```

- [ ] **Step 3:** Verify live

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://www.m365.sbs/
curl -s -o /dev/null -w "%{http_code}\n" https://www.m365.sbs/about/
curl -s -o /dev/null -w "%{http_code}\n" https://www.m365.sbs/contact/
```
Expected: `200` for each. Then load `https://www.m365.sbs/` in a real/headless browser and click the hamburger to confirm the overlay works on the live domain (per project convention, UI changes are verified by rendering, not just HTTP status).
