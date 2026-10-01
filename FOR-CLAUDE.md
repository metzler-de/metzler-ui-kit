# Metzler Design System — Claude Page Brief

> Kit-Version **v1.14** · 2026-10-01 · source of truth: `index.html` in this folder (history: `CHANGELOG.md`).

Claude reads this file directly from the kit folder (`~/Documents/Claude/Projects/Metzler UI Kit`) before building any Metzler page, section or component. No pasting needed.
Follow every rule here exactly. Do not invent values, do not skip sections, do not use custom fonts or external libraries.

> **Companion file:** ready-made page sections (heroes, feature grids, sliders, FAQ, spec layouts …) live in **`SECTIONS.md`** — always check there first before designing a new section from scratch. This file covers tokens, primitives (buttons, forms, cards), header/footer, and page scaffolding.

---

## 1 · Brand & Language

- **Company:** Metzler GmbH — outdoor hardware (intercoms, mailboxes, doorbells, house numbers)
- **Language:** German (DE) everywhere — all copy, labels, placeholders, CTAs
- **Font:** system stack, no import needed — picked per OS automatically, same scale everywhere
  - macOS / iOS / Linux → **Helvetica Neue**: `"Helvetica Neue", Helvetica, Arial, sans-serif` (`--font-family`)
  - Windows → **Arial**: `Arial, "Helvetica Neue", Helvetica, sans-serif` (`--font-family-windows`)
  - Always write `font-family: var(--font-family);` and add this one line in `<head>` so Windows switches to Arial:
    `<script>if (/Windows|Win32|Win64/.test(navigator.userAgent)) document.documentElement.classList.add('os-windows');</script>`
    (`metzler-tokens.css` then sets `html.os-windows { --font-family: var(--font-family-windows); }`)
- **Base:** 16px = 1rem — all measurements in rem, never px

---

## 2 · Design Tokens

**Preferred:** link the canonical stylesheet — `<link rel="stylesheet" href="metzler-tokens.css">` — then use `var(--color-teal)` etc. The block below is an inline fallback with the **same names and values** as that file; never define competing short names like `--teal` or `--g-800`.

```css
:root {
  --font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;           /* macOS / iOS / Linux */
  --font-family-windows: Arial, "Helvetica Neue", Helvetica, sans-serif;   /* Windows (html.os-windows) */

  /* ── TEAL — primary brand ── */
  --color-teal-50:    #F2F6F6;   /* icon badge backgrounds */
  --color-teal-75:    #E3F2F0;   /* light tint hover fills */
  --color-teal-100:   #E6EEEE;   /* selected backgrounds */
  --color-teal:       #015253;   /* CTAs, links, active borders, focus rings */
  --color-teal-600:   #014A4B;   /* hover state */
  --color-teal-700:   #01292A;   /* footer background, pressed/active states, dark gradient stops */
  --color-teal-900:   #001D1D;   /* darkest sections, CTA bands (.section--dark) */

  /* ── BRAND ── */
  --color-metzler-rot:        #D42924;   /* Metzler Rot — logo M-square, sale badges ONLY */
  --color-digital-black:      #1A171B;   /* Digital Schwarz — headlines, wordmark */

  /* ── STATUS ── */
  --color-green:      #009951;   /* success, availability dot */
  --color-red-50:     #FFF0EF;   /* error background */
  --color-red:        #D42924;   /* error borders, text */
  --color-red-600:    #B52320;   /* error hover */
  --color-red-900:    #4D0E0D;   /* readable text on red-50 surfaces */

  /* ── ACCENT ── */
  --color-mint:       #5CDBD3;   /* links / icons on dark/teal backgrounds */
  --color-star:       #FFC041;   /* rating stars only */

  /* ── SURFACES ── */
  --color-white:      #FFFFFF;   /* card backgrounds, input backgrounds */
  --color-black:      #000000;   /* reserved — never for text or section backgrounds */
  --color-footer-muted: #99A9AA; /* footer secondary text + links (white 60 % on teal-700) */
  --color-footer-line:  #1A3E3F; /* footer divider lines (white 10 % on teal-700) */
  --color-paper:      #F5F6FA;   /* page background, secondary surfaces */
  --color-graphite-100:      #F0F0F0;   /* row separators, skeleton fills */
  --color-graphite-200:      #E6E6E8;   /* hairline dividers (1px lines) */
  --color-graphite-300:      #DADADA;   /* default borders on inputs, cards */
  --color-graphite-400:      #BFBFC2;   /* focused borders, ghost-button hover border */
  --color-graphite-450:      #CCCCCC;   /* soft borders, dividers, skeleton lines */

  /* ── TEXT ── */
  --color-graphite-500:      #A1A1A1;   /* placeholder, disabled, metadata */
  --color-graphite-600:      #6A6A6A;   /* captions, secondary labels */
  --color-graphite-700:      #54545C;   /* secondary body text */
  --color-graphite-800:      #2E2E36;   /* primary body text */
  --color-graphite-850:      #333333;   /* icon fills, dark UI labels, editorial answer text */
  --color-graphite-900:      #1A1A1F;   /* heading text (alternative to --color-digital-black) */

  /* ── BORDER RADIUS ── */
  --radius-sm:   0.125rem;   /*  2px — tags, micro badges */
  --radius:      0.25rem;    /*  4px — buttons, inputs, chips */
  --radius-lg:   0.5rem;     /*  8px — cards, dropdowns, modals */
  --radius-xl:   0.75rem;    /* 12px — large panels */
  --radius-pill: 624.94rem;  /* fully rounded — pill badges */

  /* ── SHADOWS ── */
  --shadow-card:  0 0.125rem 0.5rem rgba(0,0,0,0.08);
  --shadow-hover: 0 0.25rem 1.25rem rgba(0,0,0,0.10);
  --shadow-modal: 0 1.25rem 3.75rem rgba(0,0,0,0.2), 0 0.25rem 1rem rgba(0,0,0,0.1);

  /* ── GRADIENTS ── */
  --gradient-brand:  linear-gradient(90deg, #01292A 0%, #011D1E 50%, #000000 100%);
  --gradient-accent: linear-gradient(135deg, #5CDBD3 0%, #015253 100%);
}
```

---

## 3 · Typography — Rules and CSS

**Font weight vocabulary:** 400 = regular, 500 = medium, 700 = bold, 800 = extrabold

All text uses `font-family: var(--font-family)` — never set a custom font-family.
Letter-spacing is negative on large headings, zero on body.

**Forbidden font sizes** — never use these: `10px, 15px, 17px, 19px, 22px, 28px, 32px, 36px` or any px value not matching an exact class below. Use only the defined scale.

```css
/* ── HEADINGS ── */
h1, .h1 {
  font-size: 1.875rem;        /* 30px */
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: -0.02em;
  color: var(--color-digital-black);
  font-family: var(--font-family);
  margin: 0 0 1rem;
}
h2, .h2 {
  font-size: 1.5rem;          /* 24px */
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -0.015em;
  color: var(--color-digital-black);
  font-family: var(--font-family);
  margin: 0 0 0.875rem;
}
h3, .h3 {
  font-size: 1.25rem;         /* 20px */
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -0.01em;
  color: var(--color-digital-black);
  font-family: var(--font-family);
  margin: 0 0 0.75rem;
}
h4, .h4 {
  font-size: 1.125rem;        /* 18px */
  font-weight: 700;
  line-height: 1.375;
  letter-spacing: -0.005em;
  color: var(--color-digital-black);
  font-family: var(--font-family);
  margin: 0 0 0.625rem;
}

/* ── BODY ── */
p, .body {
  font-size: 1rem;            /* 16px — ALWAYS 1rem, never 17px or 15px */
  font-weight: 400;
  line-height: 1.55;
  color: var(--color-graphite-800);        /* ALWAYS --color-graphite-800 for body; --color-graphite-700 is secondary only */
  font-family: var(--font-family);
  margin: 0 0 1rem;
}
.body-lg {
  font-size: 1.125rem;        /* 18px — lead paragraphs, intros */
  font-weight: 400;
  line-height: 1.5;
  color: var(--color-graphite-800);
  font-family: var(--font-family);
}
.body-lg--medium { font-weight: 500; }
.body-lg--bold   { font-weight: 700; line-height: 1.375; }
.body-sm {
  font-size: 0.875rem;        /* 14px */
  line-height: 1.5;
  color: var(--color-graphite-700);        /* secondary / supporting text */
  font-family: var(--font-family);
}
.caption {
  font-size: 0.75rem;         /* 12px */
  line-height: 1.4;
  color: var(--color-graphite-600);        /* captions, metadata, timestamps */
  font-family: var(--font-family);
}

/* ── LABELS / OVERLINES ── */
.overline {
  font-size: 0.75rem;         /* 12px */
  font-weight: 700;
  line-height: 1.4;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--color-graphite-600);        /* ALWAYS --color-graphite-600 on white/paper; ALWAYS --color-mint on dark/teal-900 */
  font-family: var(--font-family);
}
/* On dark sections only: */
.section--dark .overline { color: var(--color-mint); }
.label {
  font-size: 0.8125rem;       /* 13px */
  font-weight: 600;
  color: var(--color-graphite-800);
  font-family: var(--font-family);
}

/* ── DISPLAY (hero headlines only) ── */
.display-1 { font-size: clamp(3rem, 9vw, 5rem);   font-weight: 700; line-height: 0.85; letter-spacing: -0.04em; } /* max 80px / min 48px */
.display-2 { font-size: clamp(3rem, 7vw, 3.5rem); font-weight: 700; line-height: 0.92; letter-spacing: -0.04em; } /* max 56px / min 48px */
.display-3 { font-size: 3rem;                      font-weight: 700; line-height: 1.0;  letter-spacing: -0.03em; } /* 48px */
.display-4 { font-size: 2.875rem;                  font-weight: 700; line-height: 1.1;  letter-spacing: -0.02em; } /* 46px */
```

---

## 4 · Container & Layout

**Every page must use one and only one container definition:**

```css
.container {
  max-width: 100rem;      /* 1600px — never use any other value */
  margin: 0 auto;
  padding: 0 4rem;        /* 64px sides on desktop */
}
@media (max-width: 48rem) {           /* 768px */
  .container { padding: 0 1.5rem; }  /* 24px sides on mobile */
}
```

**Rules:**
- Every section (header, hero, content, footer) gets a `<div class="container">` inside it
- This applies to EVERY band without exception: header rows, breadcrumbs, tab bars / section menus (e.g. Beschreibung · Bewertungen · Downloads · Technische Details), detail sections, and the footer — same `.container`, same width, always
- Outer `<section>` / `<header>` / `<footer>` / `<nav>` elements have NO horizontal padding of their own
- Full-width backgrounds (and full-width border-bottoms on tab bars) are on the outer element; text content is always inside `.container`
- All content left-edges align with the logo left-edge — achieved automatically by `.container`
- Self-check before delivering a page: the logo, breadcrumb, first heading, tab labels, section content, and footer logo must all start on the SAME vertical line

---

## 5 · Breakpoints

| Name | Value | Purpose |
|------|-------|---------|
| sm   | 30rem (480px)   | small phones |
| md   | 48rem (768px)   | **main switch** — header, footer, layout all change here |
| lg   | 64rem (1024px)  | tablet landscape |
| xl   | 80rem (1280px)  | desktop |
| 2xl  | 90rem (1440px)  | wide desktop |
| max  | 100rem (1600px) | max container width |

**Mobile-first always:** write base styles for mobile, override for desktop with `@media (min-width: 48rem)`.

---

## 6 · Page Structure — HTML Template

Every page must follow this exact structure:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Seitentitel — Metzler</title>
  <!-- PFLICHT: Metzler-Favicon auf JEDER Seite (rotes M-Quadrat) -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <style>
    /* paste design tokens here */
    /* paste component CSS here */
  </style>
</head>
<body>

  <!-- HEADER — full width, no padding, sticky on scroll -->
  <header class="site-header" id="site-header">
    <div class="header-inner container">
      <!-- logo + nav + search -->
    </div>
  </header>

  <main>

    <!-- BREADCRUMBS — left-aligned, below header -->
    <section class="breadcrumb-bar">
      <div class="container">
        <nav class="breadcrumb"><!-- breadcrumb items --></nav>
      </div>
    </section>

    <!-- HERO / PAGE INTRO -->
    <section class="hero-section">
      <div class="container">
        <!-- heading, sub, CTA -->
      </div>
    </section>

    <!-- CONTENT SECTIONS — repeat as needed -->
    <section class="content-section">
      <div class="container">
        <!-- section content -->
      </div>
    </section>

  </main>

  <!-- FOOTER — full width, no padding -->
  <footer class="site-footer">
    <div class="container">
      <!-- footer columns, legal row -->
    </div>
  </footer>

</body>
</html>
```

---

## 7 · Header

> ⚠️ **The block below is a SIMPLIFIED single-row header.** The canonical production header is the full multi-row component in **`header/preview.html`**: green trust-bar (`.hdr-row1`) + logo/search/icons (`.hdr-row2`) + category nav (`.nav` with `.nav-cat`) + sticky compact bar (`.hdr-compact`) + mobile bar (`.hdr-mobile`) + side drawer (`.side-menu`), `position: fixed` with `body { padding-top: 151px }` (36 trust bar + 70 logo row + 45 menu, as on the live shop) (78px mobile). **For real pages, copy `header/preview.html` verbatim** — use the simplified template below only for a quick mockup.

### Desktop (≥ 768px) — 4rem (64px) tall

```html
<header class="site-header" id="site-header">
  <div class="container" style="height:4rem; display:flex; align-items:center; gap:1.25rem;">

    <!-- Logo -->
    <a href="/" style="display:flex; align-items:center; gap:0.625rem; text-decoration:none; flex-shrink:0;">
      <svg width="32" height="32" viewBox="0 0 184.3 184.3">
        <rect width="184.3" height="184.3" rx="5.75" fill="#D42924"/>
        <path fill="#fff" d="M70.19,34.81l19.04,32.98-9.58,16.57-28.59-49.55h19.13ZM70.28,108.58h0l-23.45-40.64v85.89h-16.57V34.81h16.57l33.02,57.21L123.92,15.65h19.13l-63.22,109.52-9.58-16.57.02-.02ZM153.14,153.83h-16.57v-85.87l-33,57.14h-19.13l52.11-90.28h16.57v119.02l.02-.02Z"/>
      </svg>
      <span style="font-size:1.0625rem; font-weight:800; letter-spacing:0.14em; color:#1A171B; font-family:var(--font-family);">METZLER</span>
    </a>

    <!-- Alle Kategorien button -->
    <button style="background:var(--color-teal); color:#fff; border:none; border-radius:var(--radius);
                   height:2.5rem; padding:0 1.125rem; font-size:1rem; font-weight:500;
                   font-family:var(--font-family); cursor:pointer; display:flex; align-items:center; gap:0.5rem; flex-shrink:0;">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>
      </svg>
      Alle Kategorien
    </button>

    <!-- Search bar -->
    <div style="flex:1; height:2.5rem; background:var(--color-paper); border:0.0625rem solid var(--color-graphite-300);
                border-radius:var(--radius); display:flex; align-items:center; padding:0 0.875rem; gap:0.625rem;">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#A1A1A1" stroke-width="2">
        <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
      </svg>
      <input type="search" placeholder="Suchen — Türklingel, Briefkasten, Hausnummer …"
             style="flex:1; border:none; background:none; font-size:0.9375rem; font-family:var(--font-family);
                    color:var(--color-digital-black); outline:none;"/>
    </div>

    <!-- Account + Cart -->
    <div style="display:flex; gap:0.375rem; margin-left:auto; flex-shrink:0;">
      <a href="#" class="header-icon-btn"><!-- user icon --></a>
      <a href="#" class="header-icon-btn" style="position:relative;"><!-- cart icon + badge --></a>
    </div>
  </div>
</header>
```

```css
.site-header {
  background: var(--color-white);
  border-bottom: 0.0625rem solid var(--color-graphite-200);
  position: relative;
  z-index: 100;
}
/* Sticky activates on scroll — add .is-sticky via JS */
.site-header.is-sticky {
  position: sticky;
  top: 0;
  box-shadow: 0 0.125rem 0.5rem rgba(0,0,0,0.08);
}
.header-icon-btn {
  width: 2.5rem; height: 2.5rem;
  display: flex; align-items: center; justify-content: center;
  border-radius: 50%; color: var(--color-digital-black); text-decoration: none;
  transition: background 0.14s;
}
.header-icon-btn:hover { background: var(--color-paper); }
```

```js
// Sticky header — CRITICAL: compact must be hidden at page load
// Only call this ONCE — never set is-sticky / hdr-compact--visible in CSS by default
const siteHeader = document.getElementById('site-header');
const compactHeader = document.getElementById('hdr-compact');  // if two-row design

function onScroll() {
  const scrolled = window.scrollY > 0;
  siteHeader.classList.toggle('is-sticky', scrolled);
  if (compactHeader) compactHeader.classList.toggle('visible', scrolled);
}
window.addEventListener('scroll', onScroll, { passive: true });
// Run once on load to ensure correct initial state (NOT sticky):
onScroll();
```

**IMPORTANT:** The compact/sticky header row must NEVER have `visible`, `active`, or `show` class on page load. It starts hidden. The scroll listener adds visibility. Never use `position: fixed` on the compact header row at load time — it must enter the DOM as `display: none` or `opacity: 0; pointer-events: none`.


### Mobile (< 768px) — 3.125rem (50px) tall

```html
<header class="site-header site-header--mobile">
  <div style="max-width:100%; padding:0 1rem; height:3.125rem;
              display:flex; align-items:center; justify-content:space-between;">
    <div style="display:flex; gap:0.875rem; align-items:center;">
      <button class="mobile-icon-btn" aria-label="Menü"><!-- hamburger icon --></button>
      <button class="mobile-icon-btn" aria-label="Suche"><!-- search icon --></button>
    </div>
    <a href="/" style="position:absolute; left:50%; transform:translateX(-50%);">
      <!-- logo centered -->
    </a>
    <div style="display:flex; gap:0.875rem; align-items:center;">
      <button class="mobile-icon-btn" aria-label="Konto"><!-- user icon --></button>
      <button class="mobile-icon-btn" aria-label="Warenkorb"><!-- cart icon --></button>
    </div>
  </div>
</header>
```

```css
.site-header--mobile { border-bottom: 0.0625rem solid var(--color-graphite-300); }
.mobile-icon-btn {
  width: 2rem; height: 2rem;
  background: none; border: none; cursor: pointer; padding: 0;
  display: flex; align-items: center; justify-content: center;
  color: var(--color-digital-black);
}
```

---

## 8 · Breadcrumbs

Always left-aligned, always below the header, always in the same `.container`. The separator is a **chevron SVG** (not `/` text). Links are `var(--color-teal)` with underline, active/current item is `var(--color-digital-black)`.

```html
<section class="breadcrumb-bar">
  <div class="container">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="/">Home</a></li>
        <li class="breadcrumb-item"><a href="/paketboxen">Paketboxen</a></li>
        <li class="breadcrumb-item active" aria-current="page">Bispo Max 2</li>
      </ol>
    </nav>
  </div>
</section>
```

```css
.breadcrumb-bar {
  background: var(--color-white);
  border-bottom: 0.0625rem solid var(--color-graphite-200);
  padding: 0.625rem 0;
}
.breadcrumb {
  list-style: none; margin: 0; padding: 0;
  display: flex; align-items: center; flex-wrap: wrap; gap: 0.625rem;
}
.breadcrumb-item a {
  font-size: 0.875rem; font-family: var(--font-family);
  color: var(--color-graphite-600); text-decoration: none; cursor: pointer; transition: color 0.15s;
}
.breadcrumb-item a:hover { color: var(--color-teal); text-decoration: underline; }
.breadcrumb-item.active {
  font-size: 0.875rem; font-family: var(--font-family);
  color: var(--color-digital-black); font-weight: 500;
}
/* Chevron separator — SVG data URI, NOT "/" text */
.breadcrumb-item + .breadcrumb-item {
  display: flex; align-items: center; gap: 0.625rem;
}
.breadcrumb-item + .breadcrumb-item::before {
  content: '';
  display: inline-block;
  width: 0.375rem; height: 0.625rem;
  background: url("data:image/svg+xml,%3Csvg width='6' height='10' viewBox='0 0 6 10' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1l4 4-4 4' stroke='%23A1A1A1' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") no-repeat center;
}
```

**Never use `content: "/"` as the separator** — always use the chevron data URI above.

---

## 9 · Section Patterns

### Section spacing (apply to every `<section>`)

```css
/* Standard content section */
.section { padding: 4rem 0; }

/* Compact section */
.section--sm { padding: 2.5rem 0; }

/* Large hero-style section */
.section--lg { padding: 6rem 0; }

/* Dark background section */
.section--dark {
  background: var(--color-teal-900);
  color: var(--color-white);
}
/* Tinted background section */
.section--tinted { background: var(--color-paper); }

/* White background section */
.section--color-white { background: var(--color-white); }

@media (max-width: 48rem) {
  .section     { padding: 2.5rem 0; }
  .section--sm { padding: 1.75rem 0; }
  .section--lg { padding: 3.5rem 0; }
}
```

### Section header pattern (intro text for each section)

```html
<div class="section-intro">
  <p class="overline">Abschnitt-Label</p>
  <h2>Abschnittsüberschrift</h2>
  <p class="section-intro__lead">Kurze Beschreibung des Inhalts — maximal zwei Sätze.</p>
</div>
```

```css
.section-intro { margin-bottom: 2.5rem; }
.section-intro .overline { margin-bottom: 0.5rem; }
.section-intro h2 { margin-bottom: 0.625rem; }
.section-intro__lead {
  font-size: 1rem; color: var(--color-graphite-700); max-width: 60ch; line-height: 1.6;
}
/* Centered variant */
.section-intro--center { text-align: center; }
.section-intro--center .section-intro__lead { margin-left: auto; margin-right: auto; }
```

### Dividers / horizontal rules

```css
/* Standard hairline — between sections or inside cards */
.divider {
  width: 100%; height: 0;
  border: none; border-top: 0.0625rem solid var(--color-graphite-200);
  margin: 2rem 0;
}
/* On dark backgrounds */
.divider--dark { border-top-color: rgba(255,255,255,0.12); }
```

---

## 10 · Cards

```css
/* Base card */
.card {
  background: var(--color-white);
  border: 0.0625rem solid var(--color-graphite-200);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: box-shadow 0.18s, border-color 0.18s;
}
.card:hover {
  box-shadow: var(--shadow-hover);
  border-color: var(--color-graphite-300);
}

/* Card padding variants */
.card__body          { padding: 1.5rem; }
.card__body--compact { padding: 1rem 1.25rem; }
.card__body--loose   { padding: 2rem 2.5rem; }

/* Icon badge inside card (for feature cards) */
.card-icon {
  width: 2.5rem; height: 2.5rem;
  border-radius: var(--radius-lg);   /* 0.5rem = 8px for the generic .card-icon (the feature-grid .nfs-card-icon uses 0.625rem — see Section 19) */
  background: rgba(1,82,83,0.08);    /* teal at 8% opacity — always this value */
  color: var(--color-teal);
  display: inline-flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.card-icon svg { width: 1.375rem; height: 1.375rem; }
```

---

## 11 · Buttons

```css
/* ── BASE — all buttons share this ── */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  height: 2.75rem; padding: 0 1.375rem;
  font-size: 1rem; font-weight: 500; font-family: var(--font-family);
  border: none; border-radius: var(--radius);
  cursor: pointer; text-decoration: none; white-space: nowrap;
  transition: background 0.14s, color 0.14s, border-color 0.14s;
}
.btn--sm { height: 2.25rem; padding: 0 1rem; font-size: 0.875rem; }
.btn--lg { height: 3.25rem; padding: 0 2rem; font-size: 1.0625rem; }

/* Primary */
.btn--primary { background: var(--color-teal); color: #fff; }
.btn--primary:hover  { background: var(--color-teal-600); }
.btn--primary:active { background: var(--color-teal-700); }

/* Secondary (outline) */
.btn--secondary {
  background: transparent; color: var(--color-teal);
  border: 0.125rem solid var(--color-teal);
}
.btn--secondary:hover { background: var(--color-teal-50); }

/* Ghost */
.btn--ghost {
  background: transparent; color: var(--color-graphite-700);
  border: 0.0625rem solid var(--color-graphite-300);
}
.btn--ghost:hover { background: var(--color-paper); border-color: var(--color-graphite-400); }

/* Danger */
.btn--danger { background: var(--color-red); color: #fff; }
.btn--danger:hover { background: var(--color-red-600); }

/* Block button — full width on mobile */
@media (max-width: 48rem) {
  .btn--block-mobile { width: 100%; }
}
```

---

## 12 · Form Inputs — Floating Label Pattern

The Metzler design system uses a **floating label** — the `<label>` sits inside the input and floats above the border on focus or when a value is present. Never use a simple stacked label-above-input pattern.

**HTML structure — copy exactly:**

```html
<!-- Default state -->
<div class="field-wrapper">
  <input type="text" id="name" placeholder=" "/>
  <label for="name">Name</label>
</div>

<!-- With hint text -->
<div class="field-wrapper">
  <input type="password" id="password" placeholder=" "/>
  <label for="password">Passwort</label>
  <span class="field__hint">Passwort muss aus mindestens 8 Zeichen bestehen.</span>
</div>

<!-- Error state -->
<div class="field-wrapper field--error">
  <input type="text" id="name" placeholder=" "/>
  <label for="name">Name</label>
  <span class="field__error">Dieses Feld ausfüllen</span>
</div>
```

Critical: `placeholder=" "` (single space) is **required** — the CSS uses `:not(:placeholder-shown)` to detect when a value is present and float the label.

**CSS — copy exactly:**

```css
/* Base input */
.form-control {
  display: block; width: 100%;
  padding: 0.7rem 0.9375rem;
  font-family: var(--font-family); font-size: 1rem;
  color: var(--color-digital-black); background: var(--color-white);
  border: 0.0625rem solid var(--color-graphite-300);
  border-radius: var(--radius);
  box-sizing: border-box; outline: none;
  transition: border-color 0.15s;
}
.form-control:focus   { border-color: var(--color-teal); }
.form-control.error   { border-color: var(--color-red); }

/* Floating label wrapper */
.field-wrapper { position: relative; }

.field-wrapper label {
  position: absolute; left: 0.9375rem; top: 50%;
  transform: translateY(-50%);
  font-family: var(--font-family); font-size: 1rem;
  color: var(--color-graphite-500);
  pointer-events: none; transition: all 0.15s ease;
  background: transparent; padding: 0;
  line-height: 1.4; white-space: nowrap; z-index: 1;
}

/* Float label on focus or when value is present */
.field-wrapper .form-control:focus + label,
.field-wrapper .form-control:not(:placeholder-shown) + label {
  top: -0.5625rem; left: 0.6875rem;
  transform: none; font-size: 0.75rem;
  color: var(--color-digital-black);
  background: var(--color-white); padding: 0 0.3125rem;
}

/* Error & hint text */
.field__error {
  position: absolute; bottom: -0.4375rem; right: 0.6875rem;
  background: var(--color-white); padding: 0 0.3125rem;
  font-family: var(--font-family); font-size: 0.75rem;
  color: var(--color-red); white-space: nowrap;
}
.field__hint {
  display: block; margin-top: 0.3125rem;
  font-family: var(--font-family); font-size: 0.8125rem;
  color: var(--color-graphite-600); line-height: 1.45;
}
```

**Never use** `<label class="input-label">` stacked above an `<input class="input">` — that is not the Metzler design system pattern.

---

## 13 · Colors — When to Use What

| Context | Token |
|---------|-------|
| Page background | `--color-paper` |
| Card / panel background | `--color-white` |
| Primary CTA, links, active state | `--color-teal` |
| CTA hover | `--color-teal-600` |
| Hairline dividers between sections | `--color-graphite-200` |
| Default card / input borders | `--color-graphite-300` |
| Main headline text | `--color-digital-black` |
| Body text | `--color-graphite-800` |
| Secondary / supporting text | `--color-graphite-700` |
| Captions, metadata | `--color-graphite-600` |
| Placeholder, disabled | `--color-graphite-500` |
| Footer background | `--color-teal-700` |
| Dark CTA band / `.section--dark` | `--color-teal-900` |
| Links / icons on footer / dark bg | `--color-mint` |
| Error state | `--color-red` |
| Success / availability | `--color-green` |
| Metzler logo M-square + sale badge | `--color-metzler-rot` |
| Rating stars only | `--color-star` |

**Icon badge tint** (feature cards, support cards): `background: rgba(1,82,83,0.08)` — do not use `--color-teal-50` for this.

---

## 14 · Footer

> **Canonical source:** `footer/preview.html` (rendered in the kit under Footer and Footer · Mobile). The block below is its **1:1 static export**: use it for every real page. It matches the live shop **edelstahl-tuerklingel.de as of 1 Oct 2026** (checked element by element at 1440 px and 375 px).
>
> **Assets:** every logo and badge comes from the kit's `footer/` folder (paths below are relative to the kit root): `footer/payment/` (shipping + payment tiles), `footer/topshop/` (TopShop badges), `footer/reviews/` (Trusted Shops, Google, Trustpilot). The Metzler logo, social icons, stars and the combined-rating badge are inline SVG, exactly as on the shop.

**Fixed content. Do not invent, rename, reorder or drop anything:**
- **Desktop (≥ 62rem / 992 px), 5 columns:** Logo + „Edelstahl-Tuerklingel.de ist ein Unternehmen der Metzler Gruppe“ + tagline + „Mehr erfahren“ | Kontakt (Allgemeine Hotline +49 (0) 7121 / 317 7310, Sprechanlagen Hotline +49 (0) 7121 / 317 7333, both Mo-Fr 09:00-16:00 Uhr; service@metzlergmbh.de; Zum Kontaktformular) | Informationen (7 links) | Service (5 links) | Follow us (5 social icons) + Qualität (4 TopShop badges)
- **Row 2 (stacked; side by side from 93.75rem / 1500 px):** „Unsere Versandpartner:“ DPD · DHL · Hasenauer & Koch; „Einfach bezahlen:“ SEPA · Amex · Visa · Amazon Pay · Klarna · PayPal · Mastercard · Apple Pay · Google Pay · Vorkasse; the **rating pill** rotating every 5 s through Alle Bewertungen 4,71 (36.785) · Trusted Shops 4,73 (32.461) · Google 4,63 (3.190) · Trustpilot 4,42 (1.134) — values of 1 Oct 2026, the shop loads them live
- **Row 3:** 13 legal links + Cookie-Einstellungen; the **„Vertrag widerrufen“ button** (legally required Widerrufsbutton) always sits alone on the last row, centred
- **Row 4:** „inkl. gesetzliche MwSt., zzgl. Versand © 2013 - <current year> | Metzler GmbH“
- **Mobile (< 62rem):** logo block → contact → Informationen / Service accordions → shipping → payment → rating pill → social icons → legal links + button → „* inkl. gesetzliche MwSt., zzgl. Versand / © 2013 - <year> | Metzler GmbH“
- Colors: background `var(--color-teal-700)`, secondary text and links `var(--color-footer-muted)`, divider lines `var(--color-footer-line)`, phone/e-mail/„Metzler Gruppe“ `var(--color-mint)`. The only literal colors are the payment brands (DHL, Amex, Klarna), the logo tile outline and the rating widget's arrows.

```html
<!-- needs metzler-tokens.css -->
<footer class="ft" role="contentinfo">
  <div class="ft-desktop">
    <div class="ft-top">
      <div class="ft-col ft-col--brand">
        <a class="ft-logo" href="https://edelstahl-tuerklingel.de/" aria-label="Metzler – zur Startseite"><svg aria-hidden="true" viewBox="0 0 230 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M34.5177 1.80762H2.82788V36.5249H34.5177V1.80762Z" fill="white"></path><path d="M37.4156 0H1.20394C0.541308 0 0 0.560657 0 1.24698V38.753C0 39.4393 0.541308 40 1.20394 40H37.4156C38.0782 40 38.6195 39.4393 38.6195 38.753V1.24698C38.6195 0.560657 38.0782 0 37.4156 0ZM14.7087 7.55437L18.6985 14.7124L16.6919 18.3084L10.7002 7.55437H14.7087ZM14.7273 23.5669L9.81354 14.7463V33.3881H6.34171V7.55437H9.81354L16.7339 19.971L25.9688 3.39778H29.9773L16.7292 27.1677L14.7226 23.5718L14.7273 23.5669ZM32.0912 33.3881H28.6193V14.7511L21.7037 27.1532H17.6952L28.6147 7.55921H32.0865V33.3929L32.0912 33.3881Z" fill="#D32B25"></path><path d="M70.9394 33.3881L70.8694 19.6955L64.4577 30.8409H61.3218L54.9428 20.0628V33.3881H48.4238V7.55432H54.2335L62.9971 22.4649L71.5507 7.55432H77.3604L77.4304 33.3881H70.9441H70.9394Z" fill="white"></path><path d="M104.006 27.7428V33.3881H83.9821V7.55432H103.544V13.1996H90.9678V17.5543H102.051V23.0159H90.9678V27.738H104.011L104.006 27.7428Z" fill="white"></path><path d="M115.159 13.3494H107.496V7.55432H129.839V13.3494H122.214V33.3881H115.159V13.3494Z" fill="white"></path><path d="M154.963 27.5978V33.3929H132.621V28.8158L145.197 13.3542H132.938V7.55432H154.422V12.1314L141.846 27.593H154.959L154.963 27.5978Z" fill="white"></path><path d="M160.339 7.55432H167.395V27.5978H179.294V33.3929H160.339V7.55432Z" fill="white"></path><path d="M202.244 27.7428V33.3881H182.22V7.55432H201.782V13.1996H189.206V17.5543H200.289V23.0159H189.206V27.738H202.249L202.244 27.7428Z" fill="white"></path><path d="M217.923 26.5248H214.073V33.3881H207.018V7.55432H218.418C220.676 7.55432 222.636 7.94098 224.298 8.7143C225.959 9.48762 227.242 10.5944 228.147 12.0347C229.048 13.4751 229.501 15.1667 229.501 17.1097C229.501 19.0526 229.081 20.6089 228.236 22.0009C227.391 23.3929 226.188 24.4804 224.62 25.2682L230 33.3881H222.445L217.919 26.5248H217.923ZM221.274 14.3112C220.536 13.6491 219.445 13.3156 217.993 13.3156H214.073V20.8796H217.993C219.44 20.8796 220.536 20.5558 221.274 19.9033C222.011 19.2508 222.38 18.3228 222.38 17.1193C222.38 15.9158 222.011 14.9782 221.274 14.316V14.3112Z" fill="white"></path></svg></a>
        <p class="ft-subtitle">Edelstahl-Tuerklingel.de ist ein Unternehmen der <a class="ft-special" href="https://metzlergmbh.de">Metzler Gruppe</a></p>
        <p class="ft-tagline"><strong>Der Anbieter für Briefkästen, Sprechanlagen, Türklingeln und Hausnummern.</strong></p>
        <p class="ft-tagline ft-tagline--cta"><strong><a href="https://edelstahl-tuerklingel.de/ueber-uns">Mehr erfahren</a></strong></p>
      </div>
      <div class="ft-col ft-col--contact">
<div class="ft-contact"><strong>Allgemeine Hotline:</strong><a href="tel:+4971213177310">+49 (0) 7121 / 317 7310</a><small>(Mo-Fr: 09:00-16:00 Uhr)</small></div>
<div class="ft-contact"><strong>Sprechanlagen Hotline:</strong><a href="tel:+4971213177333">+49 (0) 7121 / 317 7333</a><small>(Mo-Fr: 09:00-16:00 Uhr)</small></div>
<div class="ft-contact"><strong>E-Mail Support:</strong><a href="mailto:service@metzlergmbh.de">service@metzlergmbh.de</a></div>
<div class="ft-contact"><strong>Kontaktformular:</strong><a href="https://edelstahl-tuerklingel.de/Kontakt">Zum Kontaktformular</a></div></div>
      <div class="ft-col ft-col--links"><strong>Informationen</strong><ul><li><a href="https://edelstahl-tuerklingel.de/auszeichnungen">Auszeichnungen</a></li><li><a href="https://edelstahl-tuerklingel.de/metzler-geschenkgutschein">Geschenkgutschein</a></li><li><a href="https://edelstahl-tuerklingel.de/tuerklingel-galerie">Kundenbilder</a></li><li><a href="https://www.metzlergmbh.de/jobs/" target="_blank" rel="noopener">Stellenangebote</a></li><li><a href="https://edelstahl-tuerklingel.de/ueber-uns">Wir über uns</a></li><li><a href="https://edelstahl-tuerklingel.de/News">News</a></li><li><a href="https://edelstahl-tuerklingel.de/zahlung-und-versand">Zahlung und Versand</a></li></ul></div>
      <div class="ft-col ft-col--links"><strong>Service</strong><ul><li><a href="https://edelstahl-tuerklingel.de/begriffserklaerung">Begriffserklärung</a></li><li><a href="https://edelstahl-tuerklingel.de/faq">FAQ</a></li><li><a href="https://edelstahl-tuerklingel.de/b2b">Geschäftskunden</a></li><li><a href="https://edelstahl-tuerklingel.de/newsletter">Newsletter</a></li><li><a href="https://edelstahl-tuerklingel.de/faq/sprechanlagen">VDM10 FAQ</a></li></ul></div>
      <div class="ft-col ft-col--social">
        <strong>Follow us</strong>
<div class="ft-social"><a href="https://www.pinterest.de/METZLERGmBH/" title="Pinterest" aria-label="Pinterest" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.9888 20.5499C15.4141 23.5792 14.7137 26.4831 12.6366 28C11.9963 23.4219 13.5773 19.9845 14.3127 16.3348C13.0594 14.2118 14.4635 9.94169 17.1044 10.9944C20.355 12.2879 14.2897 18.8834 18.3609 19.7084C22.6124 20.5675 24.3475 12.2835 21.711 9.58969C17.9031 5.69798 10.625 9.4984 11.521 15.0698C11.7384 16.4315 13.1359 16.844 12.0793 18.7239C9.64163 18.1805 8.91393 16.2446 9.0079 13.664C9.15869 9.4401 12.7764 6.48446 16.4062 6.07417C20.9964 5.55608 25.3047 7.77143 25.9002 12.1174C26.5699 17.0244 23.8285 22.3395 18.9193 21.9567C17.5884 21.8522 17.0312 21.1878 15.9888 20.5499Z" fill="white"></path></svg></a><a href="https://www.facebook.com/MetzlerGmbHDE" title="Facebook" aria-label="Facebook" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M23 6.83573L19.944 6.83203C16.9805 6.83203 15.0661 8.79539 15.0661 11.8375V14.1438H12V18.3173H15.0661L15.0624 27.1682H19.3524L19.3561 18.3173H22.8743L22.8715 14.1447H19.3561V12.1878C19.3561 11.2468 19.5789 10.7708 20.8037 10.7708L22.9908 10.7698L23 6.83573Z" fill="white"></path></svg></a><a href="https://www.instagram.com/metzlergmbh/?hl=de" title="Instagram" aria-label="Instagram" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21.9457 6.26147H13.0543C11.3164 6.26277 9.65005 6.93728 8.42117 8.1369C7.19229 9.33653 6.50132 10.9632 6.5 12.6597V21.3394C6.50106 23.0361 7.19191 24.663 8.42082 25.8629C9.64973 27.0627 11.3162 27.7373 13.0543 27.7386H21.9457C23.6837 27.7371 25.35 27.0624 26.5789 25.8626C27.8077 24.6628 28.4987 23.036 28.5 21.3394V12.6597C28.4992 10.963 27.8084 9.33607 26.5794 8.13633C25.3504 6.9366 23.6838 6.26225 21.9457 6.26147ZM26.2879 21.3394C26.2876 22.4635 25.8301 23.5415 25.0158 24.3364C24.2015 25.1313 23.0972 25.578 21.9457 25.5782H13.0543C12.4841 25.5782 11.9195 25.4686 11.3928 25.2556C10.866 25.0425 10.3874 24.7303 9.98425 24.3367C9.58112 23.943 9.26137 23.4757 9.04327 22.9615C8.82516 22.4472 8.71297 21.896 8.7131 21.3394V12.6597C8.71297 12.1032 8.82517 11.552 9.04329 11.0378C9.26141 10.5236 9.58117 10.0564 9.98431 9.66283C10.3875 9.26928 10.8661 8.95713 11.3928 8.74421C11.9196 8.53128 12.4842 8.42175 13.0543 8.42188H21.9457C23.097 8.42214 24.201 8.86871 25.0151 9.6634C25.8292 10.4581 26.2866 11.5359 26.2869 12.6597L26.2879 21.3394Z" fill="white"></path><path d="M17.5005 11.4458C14.3624 11.4458 11.8122 13.9362 11.8122 16.9986C11.8122 20.0611 14.3634 22.5515 17.5005 22.5515C20.6376 22.5515 23.1888 20.0611 23.1888 16.9986C23.1888 13.9362 20.6386 11.4458 17.5005 11.4458ZM17.5005 20.3911C16.5788 20.3912 15.6949 20.0339 15.043 19.3978C14.3912 18.7617 14.025 17.8989 14.0248 16.9991C14.0247 16.0994 14.3907 15.2365 15.0423 14.6002C15.694 13.9639 16.5778 13.6064 17.4995 13.6062C18.4212 13.6061 19.3051 13.9634 19.957 14.5995C20.6088 15.2356 20.975 16.0984 20.9752 16.9982C20.9753 17.8979 20.6093 18.7608 19.9577 19.3971C19.306 20.0334 18.4222 20.3909 17.5005 20.3911ZM23.2008 10.1562C23.4703 10.1564 23.7337 10.2346 23.9577 10.3809C24.1817 10.5272 24.3562 10.735 24.4593 10.9781C24.5623 11.2212 24.5892 11.4886 24.5366 11.7467C24.484 12.0047 24.3542 12.2417 24.1636 12.4277C23.973 12.6137 23.7302 12.7404 23.4659 12.7918C23.2016 12.8432 22.9276 12.8169 22.6786 12.7163C22.4296 12.6157 22.2167 12.4453 22.0668 12.2267C21.917 12.008 21.8369 11.7509 21.8367 11.4878C21.8367 10.7537 22.3467 10.1562 23.2008 10.1562Z" fill="white"></path></svg></a><a href="https://www.youtube.com/channel/UC8irktjZBDQh2l0Vl8kURqg/videos" title="YouTube" aria-label="YouTube" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M26.9602 8.25967C26.9602 8.25967 23.9432 7.88013 17.4636 7.88013C11.1943 7.88013 8.03864 8.25967 8.03864 8.25967C7.23264 8.25997 6.45975 8.58037 5.88993 9.1504C5.32011 9.72044 5 10.4934 5 11.2994V22.7017C4.99985 23.1009 5.07833 23.4962 5.23095 23.8651C5.38358 24.2339 5.60736 24.5691 5.88953 24.8515C6.17169 25.1339 6.50671 25.3579 6.87545 25.5108C7.2442 25.6637 7.63945 25.7425 8.03864 25.7426C8.03864 25.7426 10.9727 26.1199 17.4636 26.1199C23.9511 26.1199 26.9602 25.7426 26.9602 25.7426C27.3596 25.7429 27.7551 25.6645 28.1241 25.5117C28.4931 25.359 28.8284 25.135 29.1107 24.8526C29.3931 24.5701 29.617 24.2348 29.7695 23.8657C29.9221 23.4966 30.0004 23.1011 30 22.7017V11.2972C30 10.8981 29.9214 10.5029 29.7686 10.1342C29.6158 9.76557 29.3918 9.43062 29.1095 9.14853C28.8272 8.86644 28.4921 8.64275 28.1233 8.49024C27.7545 8.33772 27.3593 8.25937 26.9602 8.25967ZM14.1602 21.5165V12.4881L22.267 16.9994L14.1602 21.5165Z" fill="white"></path></svg></a><a href="https://twitter.com/metzlerklingeln?lang=de" title="X / Twitter" aria-label="X / Twitter" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M19.3094 15.5461L26.3838 7.5H24.708L18.5627 14.4849L13.6582 7.5H8L15.4182 18.0634L8 26.5H9.6758L16.1611 19.1221L21.3418 26.5H27M10.2806 8.7365H12.8551L24.7067 25.3242H22.1316" fill="white"></path></svg></a></div>
        <strong>Qualität</strong>
<div class="ft-badges"><a href="https://edelstahl-tuerklingel.de/topshop"><img src="footer/topshop/top-shop-2023.svg" alt="TopShop 2023"></a><a href="https://edelstahl-tuerklingel.de/topshop"><img src="footer/topshop/top-shop-2024.svg" alt="TopShop 2024"></a><a href="https://edelstahl-tuerklingel.de/topshop"><img src="footer/topshop/top-shop-2025.svg" alt="TopShop 2025"></a><a href="https://edelstahl-tuerklingel.de/topshop"><img src="footer/topshop/top-shop.svg" alt="TopShop"></a></div>
      </div>
    </div>
    <hr class="ft-hr">
    <div class="ft-mid">
      <div class="ft-mid__shipping"><span class="ft-label">Unsere Versandpartner:</span><ul class="ft-pay"><li class="ship-dpd" role="img" aria-label="DPD"></li><li class="ship-dhl" role="img" aria-label="DHL"></li><li class="ship-hk" role="img" aria-label="Hasenauer &amp; Koch"></li></ul></div>
      <div class="ft-mid__payment"><span class="ft-label">Einfach bezahlen:</span><ul class="ft-pay"><li class="pay-sepa" role="img" aria-label="SEPA Lastschrift"></li><li class="pay-ae" role="img" aria-label="American Express"></li><li class="pay-visa" role="img" aria-label="Visa"></li><li class="pay-amazon" role="img" aria-label="Amazon Pay"></li><li class="pay-klarna" role="img" aria-label="Klarna"></li><li class="pay-paypal" role="img" aria-label="PayPal"></li><li class="pay-mastercard" role="img" aria-label="Mastercard"></li><li class="pay-apple" role="img" aria-label="Apple Pay"></li><li class="pay-google" role="img" aria-label="Google Pay"></li><li class="pay-vorkasse" role="img" aria-label="Vorkasse"></li></ul></div>
      <div class="ft-mid__rating">
<div class="ft-rating" data-ft-rating aria-roledescription="Karussell" aria-label="Kundenbewertungen">
<div class="ft-rating__viewport" aria-live="polite">
<div class="ft-rating__slide is-active" data-source="overall" title="Alle Bewertungen">
<div class="ft-rating__badge" aria-hidden="true"><svg aria-hidden="true" viewBox="0 0 30 30" xmlns="http://www.w3.org/2000/svg"><circle cx="15" cy="15" r="15" fill="#009951"></circle><path d="M9 15 l4 4 8-8" stroke="#FFFFFF" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,71 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24"><defs><linearGradient id="ft-half-d-overall"><stop offset="50%" stop-color="#F9DA53"></stop><stop offset="50%" stop-color="rgba(255,255,255,0.18)"></stop></linearGradient></defs><path fill="url(#ft-half-d-overall)" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,71 Sehr gut</span><span class="ft-rating__count ft-rating__count--plain">36.785 Bewertungen</span></div></div></div>
<div class="ft-rating__slide" data-source="TrustedShops" title="Trusted Shops">
<div class="ft-rating__badge" aria-hidden="true"><img src="footer/reviews/ts-logo.png" alt="" loading="lazy"></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,73 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24"><defs><linearGradient id="ft-half-d-TrustedShops"><stop offset="50%" stop-color="#F9DA53"></stop><stop offset="50%" stop-color="rgba(255,255,255,0.18)"></stop></linearGradient></defs><path fill="url(#ft-half-d-TrustedShops)" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,73 Sehr gut</span><a class="ft-rating__count" href="https://www.trustedshops.de/bewertung/info_XAC423DA09B591A4D639343B80266EF70.html" target="_blank" rel="noopener nofollow">32.461 Bewertungen</a></div></div></div>
<div class="ft-rating__slide" data-source="Google" title="Google">
<div class="ft-rating__badge" aria-hidden="true"><img src="footer/reviews/google.svg" alt="" loading="lazy"></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,63 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24"><defs><linearGradient id="ft-half-d-Google"><stop offset="50%" stop-color="#F9DA53"></stop><stop offset="50%" stop-color="rgba(255,255,255,0.18)"></stop></linearGradient></defs><path fill="url(#ft-half-d-Google)" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,63 Sehr gut</span><a class="ft-rating__count" href="https://www.google.com/search?hl=de-DE&amp;gl=de&amp;q=Metzler+GmbH,+T%C3%A4leswiesenstra%C3%9Fe+9,+72770+Reutlingen" target="_blank" rel="noopener nofollow">3.190 Bewertungen</a></div></div></div>
<div class="ft-rating__slide" data-source="Trustpilot" title="Trustpilot">
<div class="ft-rating__badge" aria-hidden="true"><img src="footer/reviews/trustpilot.svg" alt="" loading="lazy"></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,42 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="rgba(255,255,255,0.18)"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,42 Gut</span><a class="ft-rating__count" href="https://de.trustpilot.com/review/metzlergmbh.de" target="_blank" rel="noopener nofollow">1.134 Bewertungen</a></div></div></div></div>
<div class="ft-rating__nav"><button type="button" class="ft-rating__arrow" data-dir="prev" aria-label="Vorherige Quelle"><svg viewBox="0 0 11 18" fill="none" aria-hidden="true"><path d="M9.5 17L1.5 9L9.5 1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><button type="button" class="ft-rating__arrow ft-rating__arrow--next" data-dir="next" aria-label="Nächste Quelle"><svg viewBox="0 0 11 18" fill="none" aria-hidden="true"><path d="M9.5 17L1.5 9L9.5 1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button></div></div></div>
    </div>
    <hr class="ft-hr">
    <div class="ft-legal"><ul><li><a href="https://edelstahl-tuerklingel.de/kundenbewertungen">Geprüfte Kundenbewertungen</a></li><li><a href="https://edelstahl-tuerklingel.de/metzler-garantieerklaerung">Metzler Garantieerklärung</a></li><li><a href="https://edelstahl-tuerklingel.de/datenschutz">Datenschutz</a></li><li><a href="https://edelstahl-tuerklingel.de/AGB">AGB</a></li><li><a href="https://edelstahl-tuerklingel.de/Sitemap">Sitemap</a></li><li><a href="https://edelstahl-tuerklingel.de/zahlung-und-versand">Zahlung und Versand</a></li><li><a href="https://edelstahl-tuerklingel.de/impressum">Impressum</a></li><li><a href="https://edelstahl-tuerklingel.de/gesetzliche-gewaehrleistung">Gesetzliche Gewährleistung</a></li><li><a href="https://edelstahl-tuerklingel.de/barrierefreiheit">Barrierefreiheit</a></li><li class="ft-withdraw"><a href="https://edelstahl-tuerklingel.de/online-widerrufsformular">Vertrag widerrufen</a></li><li><a href="https://edelstahl-tuerklingel.de/Batterieentsorgungsgesetz">Batterieentsorgungsgesetz</a></li><li><a href="https://edelstahl-tuerklingel.de/Widerrufsrecht">Widerrufsrecht</a></li><li><a href="https://edelstahl-tuerklingel.de/elektroaltgeraeteentsorgung">Hinweise zur Elektroaltgeräteentsorgung</a></li><li><a href="#" role="button">Cookie-Einstellungen</a></li></ul></div>
    <div class="ft-copy">inkl. gesetzliche MwSt., zzgl. <a href="https://edelstahl-tuerklingel.de/zahlung-und-versand">Versand</a> © 2013 - <span data-ft-year>2026</span> | Metzler GmbH</div>
  </div>
  <div class="ft-mobile">
    <div class="ft-m-logo">
      <a class="ft-logo" href="https://edelstahl-tuerklingel.de/" aria-label="Metzler – zur Startseite"><svg aria-hidden="true" viewBox="0 0 230 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M34.5177 1.80762H2.82788V36.5249H34.5177V1.80762Z" fill="white"></path><path d="M37.4156 0H1.20394C0.541308 0 0 0.560657 0 1.24698V38.753C0 39.4393 0.541308 40 1.20394 40H37.4156C38.0782 40 38.6195 39.4393 38.6195 38.753V1.24698C38.6195 0.560657 38.0782 0 37.4156 0ZM14.7087 7.55437L18.6985 14.7124L16.6919 18.3084L10.7002 7.55437H14.7087ZM14.7273 23.5669L9.81354 14.7463V33.3881H6.34171V7.55437H9.81354L16.7339 19.971L25.9688 3.39778H29.9773L16.7292 27.1677L14.7226 23.5718L14.7273 23.5669ZM32.0912 33.3881H28.6193V14.7511L21.7037 27.1532H17.6952L28.6147 7.55921H32.0865V33.3929L32.0912 33.3881Z" fill="#D32B25"></path><path d="M70.9394 33.3881L70.8694 19.6955L64.4577 30.8409H61.3218L54.9428 20.0628V33.3881H48.4238V7.55432H54.2335L62.9971 22.4649L71.5507 7.55432H77.3604L77.4304 33.3881H70.9441H70.9394Z" fill="white"></path><path d="M104.006 27.7428V33.3881H83.9821V7.55432H103.544V13.1996H90.9678V17.5543H102.051V23.0159H90.9678V27.738H104.011L104.006 27.7428Z" fill="white"></path><path d="M115.159 13.3494H107.496V7.55432H129.839V13.3494H122.214V33.3881H115.159V13.3494Z" fill="white"></path><path d="M154.963 27.5978V33.3929H132.621V28.8158L145.197 13.3542H132.938V7.55432H154.422V12.1314L141.846 27.593H154.959L154.963 27.5978Z" fill="white"></path><path d="M160.339 7.55432H167.395V27.5978H179.294V33.3929H160.339V7.55432Z" fill="white"></path><path d="M202.244 27.7428V33.3881H182.22V7.55432H201.782V13.1996H189.206V17.5543H200.289V23.0159H189.206V27.738H202.249L202.244 27.7428Z" fill="white"></path><path d="M217.923 26.5248H214.073V33.3881H207.018V7.55432H218.418C220.676 7.55432 222.636 7.94098 224.298 8.7143C225.959 9.48762 227.242 10.5944 228.147 12.0347C229.048 13.4751 229.501 15.1667 229.501 17.1097C229.501 19.0526 229.081 20.6089 228.236 22.0009C227.391 23.3929 226.188 24.4804 224.62 25.2682L230 33.3881H222.445L217.919 26.5248H217.923ZM221.274 14.3112C220.536 13.6491 219.445 13.3156 217.993 13.3156H214.073V20.8796H217.993C219.44 20.8796 220.536 20.5558 221.274 19.9033C222.011 19.2508 222.38 18.3228 222.38 17.1193C222.38 15.9158 222.011 14.9782 221.274 14.316V14.3112Z" fill="white"></path></svg></a>
      <div class="ft-m-logo__text">
        <span class="ft-m-logo__sub">Edelstahl-Tuerklingel.de ist ein Unternehmen der <a class="ft-special" href="https://metzlergmbh.de">Metzler Gruppe</a></span>
        <strong>Der Anbieter für Briefkästen,<br>Sprechanlagen, Türklingeln und Hausnummern.</strong>
        <p class="ft-m-logo__cta"><strong><a href="https://edelstahl-tuerklingel.de/ueber-uns">Mehr erfahren</a></strong></p>
      </div>
    </div>
    <div class="ft-m-contact">
<div class="ft-contact"><strong>Allgemeine Hotline:</strong><a href="tel:+4971213177310">+49 (0) 7121 / 317 7310</a><small>(Mo-Fr: 09:00-16:00 Uhr)</small></div>
<div class="ft-contact"><strong>Sprechanlagen Hotline:</strong><a href="tel:+4971213177333">+49 (0) 7121 / 317 7333</a><small>(Mo-Fr: 09:00-16:00 Uhr)</small></div>
<div class="ft-contact"><strong>E-Mail Support:</strong><a href="mailto:service@metzlergmbh.de">service@metzlergmbh.de</a></div>
<div class="ft-contact"><strong>Kontaktformular:</strong><a href="https://edelstahl-tuerklingel.de/Kontakt">Zum Kontaktformular</a></div></div>
    <div class="ft-acc">
<div class="ft-acc__item"><button class="ft-acc__toggle" type="button" aria-expanded="false">Informationen<svg aria-hidden="true" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 6L8 11L13 6" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button>
<div class="ft-acc__body"><ul><li><a href="https://edelstahl-tuerklingel.de/auszeichnungen">Auszeichnungen</a></li><li><a href="https://edelstahl-tuerklingel.de/metzler-geschenkgutschein">Geschenkgutschein</a></li><li><a href="https://edelstahl-tuerklingel.de/tuerklingel-galerie">Kundenbilder</a></li><li><a href="https://www.metzlergmbh.de/jobs/" target="_blank" rel="noopener">Stellenangebote</a></li><li><a href="https://edelstahl-tuerklingel.de/ueber-uns">Wir über uns</a></li><li><a href="https://edelstahl-tuerklingel.de/News">News</a></li><li><a href="https://edelstahl-tuerklingel.de/zahlung-und-versand">Zahlung und Versand</a></li></ul></div></div>
<div class="ft-acc__item"><button class="ft-acc__toggle" type="button" aria-expanded="false">Service<svg aria-hidden="true" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 6L8 11L13 6" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button>
<div class="ft-acc__body"><ul><li><a href="https://edelstahl-tuerklingel.de/begriffserklaerung">Begriffserklärung</a></li><li><a href="https://edelstahl-tuerklingel.de/faq">FAQ</a></li><li><a href="https://edelstahl-tuerklingel.de/b2b">Geschäftskunden</a></li><li><a href="https://edelstahl-tuerklingel.de/newsletter">Newsletter</a></li><li><a href="https://edelstahl-tuerklingel.de/faq/sprechanlagen">VDM10 FAQ</a></li></ul></div></div></div>
    <div class="ft-m-pay"><span class="ft-label">Unsere Versandpartner:</span><ul class="ft-pay ft-pay--m"><li class="ship-dpd" role="img" aria-label="DPD"></li><li class="ship-dhl" role="img" aria-label="DHL"></li><li class="ship-hk" role="img" aria-label="Hasenauer &amp; Koch"></li></ul></div>
    <div class="ft-m-pay"><span class="ft-label">Einfach bezahlen:</span><ul class="ft-pay ft-pay--m"><li class="pay-sepa" role="img" aria-label="SEPA Lastschrift"></li><li class="pay-ae" role="img" aria-label="American Express"></li><li class="pay-visa" role="img" aria-label="Visa"></li><li class="pay-amazon" role="img" aria-label="Amazon Pay"></li><li class="pay-klarna" role="img" aria-label="Klarna"></li><li class="pay-paypal" role="img" aria-label="PayPal"></li><li class="pay-mastercard" role="img" aria-label="Mastercard"></li><li class="pay-apple" role="img" aria-label="Apple Pay"></li><li class="pay-google" role="img" aria-label="Google Pay"></li><li class="pay-vorkasse" role="img" aria-label="Vorkasse"></li></ul></div>
    <div class="ft-m-rating">
<div class="ft-rating" data-ft-rating aria-roledescription="Karussell" aria-label="Kundenbewertungen">
<div class="ft-rating__viewport" aria-live="polite">
<div class="ft-rating__slide is-active" data-source="overall" title="Alle Bewertungen">
<div class="ft-rating__badge" aria-hidden="true"><svg aria-hidden="true" viewBox="0 0 30 30" xmlns="http://www.w3.org/2000/svg"><circle cx="15" cy="15" r="15" fill="#009951"></circle><path d="M9 15 l4 4 8-8" stroke="#FFFFFF" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,71 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24"><defs><linearGradient id="ft-half-m-overall"><stop offset="50%" stop-color="#F9DA53"></stop><stop offset="50%" stop-color="rgba(255,255,255,0.18)"></stop></linearGradient></defs><path fill="url(#ft-half-m-overall)" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,71 Sehr gut</span><span class="ft-rating__count ft-rating__count--plain">36.785 Bewertungen</span></div></div></div>
<div class="ft-rating__slide" data-source="TrustedShops" title="Trusted Shops">
<div class="ft-rating__badge" aria-hidden="true"><img src="footer/reviews/ts-logo.png" alt="" loading="lazy"></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,73 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24"><defs><linearGradient id="ft-half-m-TrustedShops"><stop offset="50%" stop-color="#F9DA53"></stop><stop offset="50%" stop-color="rgba(255,255,255,0.18)"></stop></linearGradient></defs><path fill="url(#ft-half-m-TrustedShops)" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,73 Sehr gut</span><a class="ft-rating__count" href="https://www.trustedshops.de/bewertung/info_XAC423DA09B591A4D639343B80266EF70.html" target="_blank" rel="noopener nofollow">32.461 Bewertungen</a></div></div></div>
<div class="ft-rating__slide" data-source="Google" title="Google">
<div class="ft-rating__badge" aria-hidden="true"><img src="footer/reviews/google.svg" alt="" loading="lazy"></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,63 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24"><defs><linearGradient id="ft-half-m-Google"><stop offset="50%" stop-color="#F9DA53"></stop><stop offset="50%" stop-color="rgba(255,255,255,0.18)"></stop></linearGradient></defs><path fill="url(#ft-half-m-Google)" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,63 Sehr gut</span><a class="ft-rating__count" href="https://www.google.com/search?hl=de-DE&amp;gl=de&amp;q=Metzler+GmbH,+T%C3%A4leswiesenstra%C3%9Fe+9,+72770+Reutlingen" target="_blank" rel="noopener nofollow">3.190 Bewertungen</a></div></div></div>
<div class="ft-rating__slide" data-source="Trustpilot" title="Trustpilot">
<div class="ft-rating__badge" aria-hidden="true"><img src="footer/reviews/trustpilot.svg" alt="" loading="lazy"></div>
<div class="ft-rating__body">
<div class="ft-rating__stars" aria-label="4,42 von 5 Sternen"><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="#F9DA53"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg><svg aria-hidden="true" class="ft-rating__star" viewBox="0 0 24 24" fill="rgba(255,255,255,0.18)"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
<div class="ft-rating__meta"><span class="ft-rating__text">4,42 Gut</span><a class="ft-rating__count" href="https://de.trustpilot.com/review/metzlergmbh.de" target="_blank" rel="noopener nofollow">1.134 Bewertungen</a></div></div></div></div>
<div class="ft-rating__nav"><button type="button" class="ft-rating__arrow" data-dir="prev" aria-label="Vorherige Quelle"><svg viewBox="0 0 11 18" fill="none" aria-hidden="true"><path d="M9.5 17L1.5 9L9.5 1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><button type="button" class="ft-rating__arrow ft-rating__arrow--next" data-dir="next" aria-label="Nächste Quelle"><svg viewBox="0 0 11 18" fill="none" aria-hidden="true"><path d="M9.5 17L1.5 9L9.5 1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button></div></div></div>
    <div class="ft-m-social"><a href="https://www.pinterest.de/METZLERGmBH/" title="Pinterest" aria-label="Pinterest" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.9888 20.5499C15.4141 23.5792 14.7137 26.4831 12.6366 28C11.9963 23.4219 13.5773 19.9845 14.3127 16.3348C13.0594 14.2118 14.4635 9.94169 17.1044 10.9944C20.355 12.2879 14.2897 18.8834 18.3609 19.7084C22.6124 20.5675 24.3475 12.2835 21.711 9.58969C17.9031 5.69798 10.625 9.4984 11.521 15.0698C11.7384 16.4315 13.1359 16.844 12.0793 18.7239C9.64163 18.1805 8.91393 16.2446 9.0079 13.664C9.15869 9.4401 12.7764 6.48446 16.4062 6.07417C20.9964 5.55608 25.3047 7.77143 25.9002 12.1174C26.5699 17.0244 23.8285 22.3395 18.9193 21.9567C17.5884 21.8522 17.0312 21.1878 15.9888 20.5499Z" fill="white"></path></svg></a><a href="https://www.facebook.com/MetzlerGmbHDE" title="Facebook" aria-label="Facebook" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M23 6.83573L19.944 6.83203C16.9805 6.83203 15.0661 8.79539 15.0661 11.8375V14.1438H12V18.3173H15.0661L15.0624 27.1682H19.3524L19.3561 18.3173H22.8743L22.8715 14.1447H19.3561V12.1878C19.3561 11.2468 19.5789 10.7708 20.8037 10.7708L22.9908 10.7698L23 6.83573Z" fill="white"></path></svg></a><a href="https://www.instagram.com/metzlergmbh/?hl=de" title="Instagram" aria-label="Instagram" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21.9457 6.26147H13.0543C11.3164 6.26277 9.65005 6.93728 8.42117 8.1369C7.19229 9.33653 6.50132 10.9632 6.5 12.6597V21.3394C6.50106 23.0361 7.19191 24.663 8.42082 25.8629C9.64973 27.0627 11.3162 27.7373 13.0543 27.7386H21.9457C23.6837 27.7371 25.35 27.0624 26.5789 25.8626C27.8077 24.6628 28.4987 23.036 28.5 21.3394V12.6597C28.4992 10.963 27.8084 9.33607 26.5794 8.13633C25.3504 6.9366 23.6838 6.26225 21.9457 6.26147ZM26.2879 21.3394C26.2876 22.4635 25.8301 23.5415 25.0158 24.3364C24.2015 25.1313 23.0972 25.578 21.9457 25.5782H13.0543C12.4841 25.5782 11.9195 25.4686 11.3928 25.2556C10.866 25.0425 10.3874 24.7303 9.98425 24.3367C9.58112 23.943 9.26137 23.4757 9.04327 22.9615C8.82516 22.4472 8.71297 21.896 8.7131 21.3394V12.6597C8.71297 12.1032 8.82517 11.552 9.04329 11.0378C9.26141 10.5236 9.58117 10.0564 9.98431 9.66283C10.3875 9.26928 10.8661 8.95713 11.3928 8.74421C11.9196 8.53128 12.4842 8.42175 13.0543 8.42188H21.9457C23.097 8.42214 24.201 8.86871 25.0151 9.6634C25.8292 10.4581 26.2866 11.5359 26.2869 12.6597L26.2879 21.3394Z" fill="white"></path><path d="M17.5005 11.4458C14.3624 11.4458 11.8122 13.9362 11.8122 16.9986C11.8122 20.0611 14.3634 22.5515 17.5005 22.5515C20.6376 22.5515 23.1888 20.0611 23.1888 16.9986C23.1888 13.9362 20.6386 11.4458 17.5005 11.4458ZM17.5005 20.3911C16.5788 20.3912 15.6949 20.0339 15.043 19.3978C14.3912 18.7617 14.025 17.8989 14.0248 16.9991C14.0247 16.0994 14.3907 15.2365 15.0423 14.6002C15.694 13.9639 16.5778 13.6064 17.4995 13.6062C18.4212 13.6061 19.3051 13.9634 19.957 14.5995C20.6088 15.2356 20.975 16.0984 20.9752 16.9982C20.9753 17.8979 20.6093 18.7608 19.9577 19.3971C19.306 20.0334 18.4222 20.3909 17.5005 20.3911ZM23.2008 10.1562C23.4703 10.1564 23.7337 10.2346 23.9577 10.3809C24.1817 10.5272 24.3562 10.735 24.4593 10.9781C24.5623 11.2212 24.5892 11.4886 24.5366 11.7467C24.484 12.0047 24.3542 12.2417 24.1636 12.4277C23.973 12.6137 23.7302 12.7404 23.4659 12.7918C23.2016 12.8432 22.9276 12.8169 22.6786 12.7163C22.4296 12.6157 22.2167 12.4453 22.0668 12.2267C21.917 12.008 21.8369 11.7509 21.8367 11.4878C21.8367 10.7537 22.3467 10.1562 23.2008 10.1562Z" fill="white"></path></svg></a><a href="https://www.youtube.com/channel/UC8irktjZBDQh2l0Vl8kURqg/videos" title="YouTube" aria-label="YouTube" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M26.9602 8.25967C26.9602 8.25967 23.9432 7.88013 17.4636 7.88013C11.1943 7.88013 8.03864 8.25967 8.03864 8.25967C7.23264 8.25997 6.45975 8.58037 5.88993 9.1504C5.32011 9.72044 5 10.4934 5 11.2994V22.7017C4.99985 23.1009 5.07833 23.4962 5.23095 23.8651C5.38358 24.2339 5.60736 24.5691 5.88953 24.8515C6.17169 25.1339 6.50671 25.3579 6.87545 25.5108C7.2442 25.6637 7.63945 25.7425 8.03864 25.7426C8.03864 25.7426 10.9727 26.1199 17.4636 26.1199C23.9511 26.1199 26.9602 25.7426 26.9602 25.7426C27.3596 25.7429 27.7551 25.6645 28.1241 25.5117C28.4931 25.359 28.8284 25.135 29.1107 24.8526C29.3931 24.5701 29.617 24.2348 29.7695 23.8657C29.9221 23.4966 30.0004 23.1011 30 22.7017V11.2972C30 10.8981 29.9214 10.5029 29.7686 10.1342C29.6158 9.76557 29.3918 9.43062 29.1095 9.14853C28.8272 8.86644 28.4921 8.64275 28.1233 8.49024C27.7545 8.33772 27.3593 8.25937 26.9602 8.25967ZM14.1602 21.5165V12.4881L22.267 16.9994L14.1602 21.5165Z" fill="white"></path></svg></a><a href="https://twitter.com/metzlerklingeln?lang=de" title="X / Twitter" aria-label="X / Twitter" target="_blank" rel="noopener"><svg aria-hidden="true" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M19.3094 15.5461L26.3838 7.5H24.708L18.5627 14.4849L13.6582 7.5H8L15.4182 18.0634L8 26.5H9.6758L16.1611 19.1221L21.3418 26.5H27M10.2806 8.7365H12.8551L24.7067 25.3242H22.1316" fill="white"></path></svg></a></div>
    <div class="ft-m-legal"><ul><li><a href="https://edelstahl-tuerklingel.de/kundenbewertungen">Geprüfte Kundenbewertungen</a></li><li><a href="https://edelstahl-tuerklingel.de/metzler-garantieerklaerung">Metzler Garantieerklärung</a></li><li><a href="https://edelstahl-tuerklingel.de/datenschutz">Datenschutz</a></li><li><a href="https://edelstahl-tuerklingel.de/AGB">AGB</a></li><li><a href="https://edelstahl-tuerklingel.de/Sitemap">Sitemap</a></li><li><a href="https://edelstahl-tuerklingel.de/zahlung-und-versand">Zahlung und Versand</a></li><li><a href="https://edelstahl-tuerklingel.de/impressum">Impressum</a></li><li><a href="https://edelstahl-tuerklingel.de/gesetzliche-gewaehrleistung">Gesetzliche Gewährleistung</a></li><li><a href="https://edelstahl-tuerklingel.de/barrierefreiheit">Barrierefreiheit</a></li><li class="ft-withdraw"><a href="https://edelstahl-tuerklingel.de/online-widerrufsformular">Vertrag widerrufen</a></li><li><a href="https://edelstahl-tuerklingel.de/Batterieentsorgungsgesetz">Batterieentsorgungsgesetz</a></li><li><a href="https://edelstahl-tuerklingel.de/Widerrufsrecht">Widerrufsrecht</a></li><li><a href="https://edelstahl-tuerklingel.de/elektroaltgeraeteentsorgung">Hinweise zur Elektroaltgeräteentsorgung</a></li><li><a href="#" role="button">Cookie-Einstellungen</a></li></ul>
      <span class="ft-m-copy">* inkl. gesetzliche MwSt., zzgl. <a href="https://edelstahl-tuerklingel.de/zahlung-und-versand">Versand</a><br> © 2013 - <span data-ft-year>2026</span> | Metzler GmbH</span>
    </div>
  </div>
</footer>
```

```css
/* ── FOOTER — 1:1 with edelstahl-tuerklingel.de (1 Oct 2026). rem + tokens; the only literal colors
      are the payment brands (DHL, Amex, Klarna), the logo tile outline and the rating widget's star/arrow colors. ── */
.ft { background: var(--color-teal-700); color: var(--color-white); font-family: var(--font-family);
  font-size: 1rem; line-height: 1.4; padding-top: 2rem; overflow-x: hidden; }
.ft a { color: var(--color-white); text-decoration: none; }
.ft ul { list-style: none; margin: 0; padding: 0; }
.ft p { margin: 0; }
.ft strong { font-weight: 600; }
.ft-logo { display: inline-block; line-height: 0; }
.ft-logo svg { width: 11.875rem; height: 2.0625rem; }
.ft-special { color: var(--color-mint) !important; font-weight: 800; }
.ft-label { display: block; margin-bottom: 0.5rem; font-size: 0.75rem; font-weight: 700; line-height: 1.4; color: var(--color-footer-muted); }
.ft-hr { height: 0; margin: 0.9375rem 0; border: 0; border-top: 0.0625rem solid var(--color-footer-line); }

/* Logo tiles (shipping + payment): 52×33 desktop, 44×28 mobile */
.ft-pay { display: flex; flex-wrap: wrap; }
.ft-pay li { width: 3.25rem; height: 2.0625rem; margin: 0 0.55rem 0.5rem 0; border-radius: 0.3125rem; outline: 0.0625rem solid #006D75; }
.ft-pay .ship-dpd { background: url("footer/payment/ship-dpd.svg") center center / 70% auto no-repeat, var(--color-white); }
.ft-pay .ship-dhl { background: url("footer/payment/ship-dhl.svg") center center / cover no-repeat, #FFCB00; }
.ft-pay .ship-hk { background: url("footer/payment/ship-hasenauer-koch.svg") center center / 88% auto no-repeat, var(--color-white); }
.ft-pay .pay-sepa { background: url("footer/payment/pay-sepa.svg") center center / 70% auto no-repeat, var(--color-white); }
.ft-pay .pay-ae { background: url("footer/payment/pay-amex.svg") right center / 75% auto no-repeat, #006FCF; }
.ft-pay .pay-visa { background: url("footer/payment/pay-visa.svg") center center / 70% auto no-repeat, var(--color-white); }
.ft-pay .pay-amazon { background: url("footer/payment/pay-amazon.svg") center center / 45% auto no-repeat, var(--color-white); }
.ft-pay .pay-klarna { background: url("footer/payment/pay-klarna.svg") center center / 80% auto no-repeat, #FFB4C7; }
.ft-pay .pay-paypal { background: url("footer/payment/pay-paypal.svg") center center / 85% auto no-repeat, var(--color-white); }
.ft-pay .pay-mastercard { background: url("footer/payment/pay-mastercard.svg") center center / 60% auto no-repeat, var(--color-white); }
.ft-pay .pay-apple { background: url("footer/payment/pay-apple.svg") center center / 70% auto no-repeat, var(--color-white); }
.ft-pay .pay-google { background: url("footer/payment/pay-google.svg") center center / 80% auto no-repeat, var(--color-white); }
.ft-pay .pay-vorkasse { background: url("footer/payment/pay-vorkasse.svg") center center / 90% auto no-repeat, var(--color-white); }

/* Rating pill (auto-rotates every 5 s, pauses on hover) */
.ft-rating { box-sizing: border-box; display: inline-flex; align-items: center; justify-content: space-between; gap: 0.625rem;
  width: 100%; min-width: 25rem; height: 3.25rem; padding: 0.625rem 0.9375rem; border-radius: 3.75rem;
  background: rgba(255,255,255,0.08); color: var(--color-white); line-height: 1.1; }
.ft-rating__viewport { position: relative; flex: 1 1 auto; height: 2rem; min-width: 0; }
.ft-rating__slide { position: absolute; inset: 0; display: flex; align-items: center; gap: 0.625rem; opacity: 0; visibility: hidden;
  pointer-events: none; transition: opacity 0.3s cubic-bezier(0.4,0,0.2,1), visibility 0.3s cubic-bezier(0.4,0,0.2,1); }
.ft-rating__slide.is-active { opacity: 1; visibility: visible; pointer-events: auto; }
.ft-rating__badge { flex-shrink: 0; width: 1.875rem; height: 1.875rem; display: inline-flex; align-items: center; justify-content: center; }
.ft-rating__badge img, .ft-rating__badge svg { width: 100%; height: 100%; object-fit: contain; display: block; }
.ft-rating__body { display: flex; flex-direction: column; align-items: flex-start; gap: 0.1875rem; min-width: 0; }
.ft-rating__stars { display: inline-flex; align-items: center; gap: 0.1875rem; height: 1rem; }
.ft-rating__star { width: 0.85rem; height: 0.85rem; flex: 0 0 auto; display: inline-block; }
.ft-rating__meta { display: inline-flex; align-items: center; gap: 0.3125rem; height: 0.875rem; font-size: 0.8125rem; line-height: 0.875rem; white-space: nowrap; }
.ft-rating__count { color: var(--color-mint) !important; }
a.ft-rating__count:hover { text-decoration: underline; }
.ft-rating__count--plain { color: rgba(255,255,255,0.65) !important; }
.ft-rating__nav { flex-shrink: 0; display: inline-flex; align-items: center; gap: 0.375rem; }
.ft-rating__arrow { width: 1.375rem; height: 1.375rem; padding: 0; border: 0.0625rem solid #DDDDDD; border-radius: 0.4rem;
  background: var(--color-white); color: var(--color-black); display: inline-flex; align-items: center; justify-content: center;
  cursor: pointer; transition: background-color 0.15s; }
.ft-rating__arrow:hover { background: #F6F6F6; }
.ft-rating__arrow svg { width: 0.29rem; height: 0.47rem; }
.ft-rating__arrow--next svg { transform: rotate(180deg); }

/* Legal links + Widerrufsbutton (always last, own row) */
.ft-legal, .ft-m-legal { text-align: center; }
.ft-legal ul, .ft-m-legal ul { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.3rem 0.8rem; }
.ft-legal a, .ft-m-legal a { font-size: 0.75rem; line-height: 1.4; color: var(--color-footer-muted); }
.ft-legal a:hover, .ft-m-legal a:hover { color: var(--color-white); }
.ft-withdraw { order: 99; flex-basis: 100%; margin-top: 0.5rem; }
.ft .ft-withdraw a { display: inline-block; padding: 0.35rem 0.8rem; border-radius: var(--radius); background: var(--color-teal);
  font-size: 0.75rem; font-weight: 600; line-height: 1.4; color: var(--color-white); }
.ft .ft-withdraw a:hover { background: #00373A; color: var(--color-white); }

/* ── Desktop (≥ 62rem) ── */
.ft-desktop { display: none; max-width: 100rem; margin: 0 auto; padding: 0 6.25rem; }
@media (max-width: 87.5rem) { .ft-desktop { padding: 0 3.125rem; } }
.ft-top { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 2.5rem; margin: 0 -0.9375rem; padding: 2.5rem 0 2rem; line-height: 1.5; }
.ft-col { min-width: 0; padding: 0 0.9375rem; }
.ft-col--brand, .ft-col--social { flex: 0 0 18%; }
.ft-col--contact { flex: 0 0 20%; }
.ft-col--links { flex: 0 0 14%; }
.ft-subtitle { font-size: 0.85rem; line-height: 1.6; color: var(--color-footer-muted); }
.ft-tagline { margin: 0.75rem 0 0.5rem !important; font-size: 0.9rem; font-weight: 700; line-height: 1.6; }
.ft-tagline--cta { margin-top: 1.25rem !important; }
.ft-contact { margin-bottom: 0.85rem; }
.ft-contact strong, .ft-col--links strong, .ft-col--social strong { display: block; font-size: 1rem; font-weight: 700; }
.ft-contact strong { margin-bottom: 0.15rem; }
.ft-contact a { display: block; font-size: 0.9rem; font-weight: 700; color: var(--color-mint); }
.ft-contact small { font-size: 0.8rem; line-height: 1.3; color: var(--color-footer-muted); }
.ft-col--links strong { margin-bottom: 0.6rem; }
.ft-col--links li { margin-bottom: 0.4rem; }
.ft-col--links a { font-size: 0.9rem; color: var(--color-footer-muted); }
.ft-col--links a:hover { color: var(--color-white); }
.ft-col--social strong { margin-bottom: 0.5rem; }
.ft-social { display: flex; gap: 0.6rem; margin-bottom: 2.25rem; }
.ft-social a { display: flex; align-items: center; justify-content: center; padding: 0.25rem; border-radius: 50%; background: rgba(255,255,255,0.1); }
.ft-social svg { width: 1.75rem; height: 1.75rem; fill: var(--color-white); }
.ft-badges { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.ft-badges img { display: block; width: auto; height: 4.6875rem; }
.ft-mid { display: flex; flex-direction: column; align-items: flex-start; gap: 2rem; }
@media (min-width: 93.75rem) { .ft-mid { flex-direction: row; align-items: center; } }
.ft-mid__shipping, .ft-mid__rating { flex: 0 0 auto; }
.ft-mid__payment { flex: 1 1 0%; }
.ft-legal { padding: 0.75rem 0; }
.ft-copy { padding: 0.5rem 0 1rem; text-align: center; font-size: 0.75rem; line-height: 1.4; color: var(--color-footer-muted); }

/* ── Mobile (< 62rem) ── */
.ft-mobile { padding: 0 1.25rem 2rem; font-size: 0.9rem; }
.ft-m-logo { padding: 1.25rem 0 1rem; }
.ft-m-logo a { display: inline-block; margin-bottom: 0.75rem; }
.ft-m-logo .ft-logo { line-height: 1.4; }
.ft-m-logo__text { font-size: 0.85rem; line-height: 1.5; color: var(--color-footer-muted); }
.ft-m-logo__sub { display: block; margin-bottom: 1rem; }
.ft-m-logo__text > strong { display: block; margin-bottom: 0.35rem; font-size: 0.9rem; font-weight: 700; color: var(--color-white); }
.ft-m-logo__cta { margin: 1rem 0 1.75rem !important; font-size: 0.95rem; line-height: 1.5; }
.ft-m-logo__cta strong { font-size: 0.9rem; font-weight: 700; }
.ft-m-contact { padding-bottom: 1rem; border-bottom: 0.0625rem solid var(--color-footer-line); }
.ft-m-contact .ft-contact { margin: 0.85rem 0 0; }
.ft-m-contact strong { display: block; margin-bottom: 0.15rem; font-size: 0.85rem; font-weight: 700; }
.ft-m-contact a { display: block; font-size: 0.9rem; font-weight: 700; color: var(--color-mint); }
.ft-m-contact small { display: block; font-size: 0.78rem; line-height: 1.3; color: var(--color-footer-muted); }
.ft-acc { border-top: 0.0625rem solid var(--color-footer-line); }
.ft-acc__item { border-bottom: 0.0625rem solid var(--color-footer-line); }
.ft-acc__toggle { width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 0.9rem 0;
  border: 0; background: none; color: var(--color-white); font: inherit; font-size: 1rem; font-weight: 600; line-height: 1; letter-spacing: 0.01em; cursor: pointer; }
.ft-acc__toggle svg { width: 1rem; height: 1rem; flex-shrink: 0; transition: transform 0.25s; }
.ft-acc__toggle[aria-expanded="true"] svg { transform: rotate(180deg); }
.ft-acc__body { display: none; padding-bottom: 0.75rem; }
.ft-acc__body.is-open { display: block; }
.ft-acc__body li { padding: 0.35rem 0; }
.ft-acc__body a { font-size: 0.9rem; }
.ft-m-pay { padding: 0.85rem 0; border-bottom: 0.0625rem solid var(--color-footer-line); }
.ft-m-pay .ft-label { line-height: 1.5; letter-spacing: 0.04em; }
.ft-pay--m { gap: 0.5rem; }
.ft-pay--m li { width: 2.75rem; height: 1.75rem; margin: 0; border-radius: var(--radius); outline: 0; flex-shrink: 0; }
.ft-m-rating { padding: 1.25rem 0; border-bottom: 0.0625rem solid var(--color-footer-line); }
@media (max-width: 30rem) { .ft-rating { min-width: 0; } .ft-rating__meta { font-size: 0.75rem; } }
.ft-m-social { display: flex; align-items: center; justify-content: center; gap: 0.6rem; padding: 1.35rem 0; border-bottom: 0.0625rem solid var(--color-footer-line); }
.ft-m-social a { display: flex; align-items: center; justify-content: center; width: 2.375rem; height: 2.375rem; border: 0.0625rem solid rgba(255,255,255,0.4); border-radius: 50%; }
.ft-m-social svg { width: 1.25rem; height: 1.25rem; fill: var(--color-white); }
.ft-m-legal { padding-top: 1.25rem; }
.ft-m-legal li { font-size: 0.9rem; }
.ft-m-copy { display: block; padding-top: 1.25rem; text-align: center; font-size: 0.75rem; line-height: 1.6; color: var(--color-footer-muted); }

@media (min-width: 62rem) { .ft-desktop { display: block; } .ft-mobile { display: none; } }
@media (prefers-reduced-motion: reduce) { .ft-rating__slide, .ft-acc__toggle svg { transition: none; } }
```

```html
<script>
(function () {
  document.querySelectorAll('[data-ft-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  /* Mobile accordions: Informationen / Service */
  document.querySelectorAll('.ft-acc__toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', open);
      btn.nextElementSibling.classList.toggle('is-open', open);
    });
  });
  /* Rating pill: 4 sources, 5 s autoplay, pause on hover */
  document.querySelectorAll('[data-ft-rating]').forEach(function (root) {
    var slides = root.querySelectorAll('.ft-rating__slide'), i = 0, timer = null;
    function show(n) { slides[i].classList.remove('is-active'); i = (n + slides.length) % slides.length; slides[i].classList.add('is-active'); }
    function play() { stop(); timer = setInterval(function () { show(i + 1); }, 5000); }
    function stop() { if (timer) clearInterval(timer); timer = null; }
    root.querySelector('[data-dir="prev"]').addEventListener('click', function () { show(i - 1); play(); });
    root.querySelector('[data-dir="next"]').addEventListener('click', function () { show(i + 1); play(); });
    root.addEventListener('mouseenter', stop); root.addEventListener('mouseleave', play);
    play();
  });
})();
</script>
```

## 15 · Mobile Rules

Apply these on every page for the `< 768px` breakpoint:

```css
@media (max-width: 48rem) {

  /* Typography — scale down */
  h1, .h1 { font-size: 1.5rem; }
  h2, .h2 { font-size: 1.25rem; }
  h3, .h3 { font-size: 1.125rem; }
  .display-4 { font-size: 2rem; }

  /* Layout — single column */
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  .grid-2--md { grid-template-columns: 1fr 1fr; }  /* 2-col still ok at md */

  /* Sections */
  .section     { padding: 2.5rem 0; }
  .section--lg { padding: 3.5rem 0; }

  /* Cards — full width, no horizontal gap */
  .card-grid  { gap: 0.75rem; }

  /* Buttons — full width in mobile CTAs */
  .btn--block-mobile { width: 100%; }

  /* Hide desktop-only elements */
  .hide-mobile { display: none !important; }
}
@media (min-width: 48rem) {
  .hide-desktop { display: none !important; }
}
```

---

## 16 · Grids

```css
/* 2-column content grid */
.grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }

/* 3-column feature grid */
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }

/* 4-column product grid */
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; }

/* Auto-responsive grid (min 16rem per column) */
.grid-auto { display: grid; grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr)); gap: 1.25rem; }

@media (max-width: 64rem) {
  .grid-4 { grid-template-columns: repeat(3, 1fr); }
}
@media (max-width: 48rem) {
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  .grid-4 { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 30rem) {
  .grid-4 { grid-template-columns: 1fr; }
}
```

---

## 17 · Rules Claude Must Always Follow

1. **All values in rem** — never use px in CSS output (1px = 0.0625rem)
2. **All colors from tokens** — never use bare hex codes; reference `var(--color-teal)`, `var(--color-graphite-200)` etc.
3. **Font always `var(--font-family)`** — never set a custom font-family
4. **Container max-width exactly 100rem** — never 90rem, 1440px, or anything else
5. **No padding on `<header>` / `<footer>` outer tags** — padding lives inside `.container` only
6. **Header two-state:** not sticky at page load; `.is-sticky` class added via JS on first scroll
7. **Breadcrumbs always left-aligned** — never centered
8. **Footer always `var(--color-teal-700)` (#01292A) background** — never a custom dark color. Always copy the exact footer from Section 14 — never invent columns, headings, or links. The footer has 5 columns: logo+tagline | Kontakt (exact phone numbers) | Informationen | Service | Follow us + Qualität, then the shipping/payment/rating row, 13 legal links, the „Vertrag widerrufen“ button and the copyright line. Headings, link texts and order are fixed — do not change them.
9. **Cards always `var(--radius-lg)` (0.5rem) radius** — never sharp corners, never pill-radius
10. **Arrows / carousel controls never show step numbers** — navigation arrows are controls only
11. **No external icon libraries** — use inline `<svg>` with `stroke="currentColor"`, `stroke-width: 1.8–2`, `stroke-linecap: round`, `stroke-linejoin: round`, `fill: none`; icon container is 2.5rem × 2.5rem with `border-radius: var(--radius-lg)` (0.5rem = 8px) for the generic `.card-icon`; the feature-grid `.nfs-card-icon` is the one exception at 0.625rem (10px)
12. **Mobile-first** — base styles for mobile, overrides inside `@media (min-width: 48rem)`

---

## 18 · Complete Minimal Page Example

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neue Seite — Metzler</title>
  <!-- PFLICHT: Metzler-Favicon auf JEDER Seite (rotes M-Quadrat) -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; background: #F5F6FA; }

    :root {
      --font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      --color-teal: #015253; --color-teal-600: #014A4B; --color-teal-900: #001D1D;
      --color-teal-50: #F2F6F6; --color-mint: #5CDBD3;
      --color-digital-black: #1A171B; --color-metzler-rot: #D42924;
      --color-white: #FFFFFF; --color-paper: #F5F6FA;
      --color-graphite-200: #E6E6E8; --color-graphite-300: #DADADA;
      --color-graphite-600: #6A6A6A; --color-graphite-700: #54545C; --color-graphite-800: #2E2E36;
      --radius: 0.25rem; --radius-lg: 0.5rem;
    }

    .container { max-width: 100rem; margin: 0 auto; padding: 0 4rem; }
    @media (max-width: 48rem) { .container { padding: 0 1.5rem; } }

    /* header, breadcrumbs, footer, etc. using rules above */
  </style>
</head>
<body>

  <header class="site-header" id="site-header">
    <div class="container" style="height:4rem; display:flex; align-items:center; gap:1.25rem;">
      <!-- logo, nav, search -->
    </div>
  </header>

  <section class="breadcrumb-bar">
    <div class="container">
      <nav><ol class="breadcrumb">
        <li><a href="/">Home</a></li>
        <li aria-current="page">Aktuelle Seite</li>
      </ol></nav>
    </div>
  </section>

  <section class="section section--color-white">
    <div class="container">
      <h1>Seitenüberschrift</h1>
      <p>Beschreibung der Seite.</p>
    </div>
  </section>

  <footer class="site-footer">
    <div class="container">
      <!-- footer content -->
    </div>
  </footer>

  <script>
    const siteHeader = document.getElementById('site-header');
    const compactHeader = document.getElementById('hdr-compact');
    function onScroll() {
      const scrolled = window.scrollY > 0;
      siteHeader.classList.toggle('is-sticky', scrolled);
      if (compactHeader) compactHeader.classList.toggle('visible', scrolled);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // ensure correct state at load — NOT sticky
  </script>
</body>
</html>
```

---

## 19 · Common Mistakes — What Claude Gets Wrong

Read this section carefully. These are real errors observed in generated pages.

### ❌ Body text wrong font-size or color

```css
/* WRONG — never do this */
p { font-size: 17px; }         /* invented value */
p { font-size: 15px; }         /* invented value */
p { color: var(--color-graphite-700); }     /* g-700 is secondary text, not body */

/* CORRECT */
p { font-size: 1rem; }         /* always 16px = 1rem */
p { color: var(--color-graphite-800); }     /* primary body text */
.body-sm { color: var(--color-graphite-700); }  /* secondary/supporting text only */
```

### ❌ Inventing font sizes outside the type scale

**Permitted font sizes only:**

| Class | Size | Use |
|-------|------|-----|
| `.caption` | 0.75rem (12px) | metadata, timestamps |
| `.overline` | 0.75rem (12px) · ls 0.15em | section kickers |
| `.label` / `.body-sm` | 0.8125–0.875rem (13–14px) | labels, captions |
| `p` / `.body` | 1rem (16px) | body text |
| `h4` | 1.125rem (18px) | small headings |
| `h3` | 1.25rem (20px) | sub-headings |
| `h2` | 1.5rem (24px) | section headings |
| `h1` | 1.875rem (30px) | page title |
| `.display-4` | 2.875rem (46px) | hero headings |
| `.display-3` | 3rem (48px) | landing intro |
| `.display-2` | clamp → max 3.5rem (56px) | large hero |
| `.display-1` | clamp → max 5rem (80px) | landing hero |

**NEVER use:** 10px, 15px, 17px, 19px, 22px, 28px, 32px, 36px, 72px — or any px value not listed above.

### ❌ Sticky compact header visible at page load

```css
/* WRONG — never apply a visible/active/show class by default */
.hdr-compact { display: block; opacity: 1; }
.hdr-compact.visible { ... }   /* OK as a rule, but 'visible' must NOT be in HTML on load */

/* CORRECT starting state in HTML */
<div id="hdr-compact" class="hdr-compact">   <!-- no 'visible' class -->

/* JS adds it only on scroll */
function onScroll() {
  document.getElementById('hdr-compact')
    .classList.toggle('visible', window.scrollY > 0);
}
window.addEventListener('scroll', onScroll, { passive: true });
onScroll(); // ← call immediately to set correct initial state
```

### ❌ Overline/section-kicker wrong color

```css
/* WRONG */
.overline { color: var(--color-teal); }   /* teal is for CTAs, not kicker labels */

/* CORRECT — always gray on light backgrounds */
.overline { color: var(--color-graphite-600); }

/* CORRECT — only on dark (teal-900) backgrounds */
.section--dark .overline { color: var(--color-mint); }
```

### ❌ Icon badge border-radius not using token

```css
/* WRONG — generic card icon must use the token, not a raw value */
.card-icon { border-radius: 0.625rem; }

/* CORRECT — generic icon badge */
.card-icon { border-radius: var(--radius-lg); }  /* 0.5rem = 8px */

/* EXCEPTION — the feature-grid icon is intentionally 0.625rem (10px). This is the
   one place 0.625rem is correct; it matches the rendered .nfs-card-icon component. */
.nfs-card-icon { border-radius: 0.625rem; background: rgba(1,82,83,0.08); color: var(--color-teal); }
```

### ❌ Dark CTA/banner using pure black instead of brand dark

```css
/* WRONG */
.cta-section { background: #000; }
.cta-section { background: #111; }

/* CORRECT — always use the brand dark token */
.cta-section { background: var(--color-teal-900); }   /* #001D1D */
/* OR the brand gradient */
.cta-section { background: var(--gradient-brand); }
```

### ❌ Section padding not using defined classes

```css
/* WRONG — arbitrary one-off values */
section { padding: 32px 0 48px; }
section { padding: 10px 0; }

/* CORRECT — always one of these three */
.section     { padding: 4rem 0; }   /* standard — use for most sections */
.section--sm { padding: 2.5rem 0; } /* compact — for tight rows */
.section--lg { padding: 6rem 0; }   /* spacious — hero sections */

@media (max-width: 48rem) {
  .section     { padding: 2.5rem 0; }
  .section--sm { padding: 1.75rem 0; }
  .section--lg { padding: 3.5rem 0; }
}
```

### ❌ Custom footer with wrong columns or invented links

```html
<!-- WRONG — Claude invented "Paketboxen", "Briefkästen", "Sprechanlagen" as columns -->
<footer>
  <div>
    <h3>Produkte</h3>
    <ul><li>Paketboxen</li><li>Briefkästen</li></ul>
  </div>
  <div>
    <h3>Kontakt</h3>
    <p>Mo – Fr · 08:00 – 17:00 Uhr</p>
    <p>+49 (0) XXXX / XXX XXX</p>  <!-- WRONG: invented phone number -->
  </div>
</footer>

<!-- CORRECT — copy Section 14 verbatim (5 columns, exact content):
     Col 1: logo + tagline + „Mehr erfahren“
     Col 2: Kontakt — +49 (0) 7121 / 317 7310, +49 (0) 7121 / 317 7333, service@metzlergmbh.de, Kontaktformular
     Col 3: Informationen — Auszeichnungen, Geschenkgutschein, Kundenbilder, Stellenangebote, Wir über uns, News, Zahlung und Versand
     Col 4: Service — Begriffserklärung, FAQ, Geschäftskunden, Newsletter, VDM10 FAQ
     Col 5: Follow us (5 icons) + Qualität (4 TopShop badges)
     Then: Versandpartner + Bezahlen + rating, 13 legal links, „Vertrag widerrufen“ button, copyright
-->
```

### ❌ Section with padding but no container inside

```html
<!-- WRONG — section has its own padding, content bleeds edge to edge -->
<section style="padding: 64px 30px;">
  <h2>Heading</h2>
</section>

<!-- CORRECT — section has no padding; container provides alignment -->
<section class="section section--tinted">
  <div class="container">
    <h2>Heading</h2>
  </div>
</section>
```

### ❌ Mixing text color tokens incorrectly

| Token | Correct use |
|-------|------------|
| `--color-digital-black` / `--color-graphite-900` | H1, H2, H3, H4 headings |
| `--color-graphite-800` | Primary body paragraphs |
| `--color-graphite-700` | Secondary body, section intro lead text |
| `--color-graphite-600` | Captions, breadcrumb links, overlines, metadata |
| `--color-graphite-500` | Placeholders, disabled text |
| `--color-teal` | Links, icon colors, interactive elements |
| `--color-white` | Text on dark/teal backgrounds |
| `--color-mint` | Links and icons on dark/teal-900 backgrounds |

**Never use `--color-graphite-700` for primary body paragraphs. Never use `--color-graphite-600` for body text.**

### ❌ Breadcrumb with "/" text separator and wrong link color

```css
/* WRONG */
.breadcrumb li:not(:last-child)::after { content: "/"; }  /* ❌ text separator */
.breadcrumb a { color: var(--color-graphite-600); }                    /* ❌ wrong color */

/* CORRECT */
/* Separator is a chevron SVG via ::before on li + li (see Section 8) */
.breadcrumb-item a { color: var(--color-graphite-600); text-decoration: none; }
.breadcrumb-item a:hover { color: var(--color-teal); text-decoration: underline; }
.breadcrumb-item.active { color: var(--color-digital-black); font-weight: 500; }
```

### ❌ Section overline/heading without section-intro wrapper (bad spacing)

```html
<!-- WRONG — overline and heading floated directly in section, no spacing control -->
<section>
  <div class="container">
    <span class="overline">AUSGEZEICHNETE QUALITÄT</span>
    <h2>Geprüft, empfohlen & tausendfach bewährt</h2>
  </div>
</section>

<!-- CORRECT — always wrap in .section-intro for consistent spacing -->
<section class="section section--color-white">
  <div class="container">
    <div class="section-intro section-intro--center">
      <p class="overline">Ausgezeichnete Qualität</p>
      <h2>Geprüft, empfohlen &amp; tausendfach bewährt</h2>
      <p class="section-intro__lead">Supporting lead text here.</p>
    </div>
    <!-- section content below -->
  </div>
</section>
```
`.section-intro .overline` has `margin-bottom: 0.5rem` and `.section-intro h2` has `margin-bottom: 0.625rem` — these spacings only work inside `.section-intro`.

### ❌ Stacked label+input instead of floating label pattern

```html
<!-- WRONG — stacked label above input, wrong classes -->
<label class="input-label">Name</label>
<input class="input" type="text" placeholder="z. B. Familie Breitenbach"/>

<!-- CORRECT — floating label inside field-wrapper, placeholder must be a single space -->
<div class="field-wrapper">
  <input type="text" id="name" placeholder=" "/>
  <label for="name">Name</label>
</div>
```

### ❌ FAQ built from scratch instead of using the design system component

```html
<!-- WRONG — invented classes, wrong icon, wrong sizes -->
<div class="faq">
  <div class="faq-item">
    <div class="faq-q">Frage?</div>
    <div class="faq-a-inner" style="font-size:0.9375rem; color:var(--color-graphite-700);">...</div>
    <!-- ❌ uses + icon, wrong classes, no hover/open states, no left accent bar -->
  </div>
</div>

<!-- CORRECT — copy the verbatim template from Section 20 -->
<!-- Key class names: faq-stage, faq-list (ul), faq-item (li), faq-btn, faq-q, faq-icon, faq-body, faq-answer -->
<!-- Question: font-size: 1.125rem; font-weight: 700 -->
<!-- Answer: font-size: 1rem; color: var(--color-graphite-700) — g-700 IS CORRECT for faq-answer -->
<!-- Icon: chevron SVG that rotates 180deg (not + / ×) -->
<!-- Open state: teal border + left accent bar (.faq-item.is-open::before) -->
```

---

## 20 · Product Page (PDP) — Specific Rules

For product detail pages, follow this structure in addition to all general rules:

```
Trust bar (dark, full-width)
Header (two-state)
Breadcrumbs (left-aligned)
Product hero (image gallery left, info panel right — 55% / 45% split)
Feature bar (4 icons in a row, white bg)
Why-this-product section (section-intro centered + 3-col feature cards)
Split sections (alternating image left/right with text)
Personalization / configurator section (--color-paper bg)
Gallery / lifestyle images
Specs / dimensions table
Awards / trust section
FAQ accordion
CTA bar (--color-teal-900 bg, price + button)
Footer
```

**Product hero panel rules:**
- Price: `font-size: 2rem; font-weight: 700; color: var(--color-digital-black);`
- Original price (strikethrough): `font-size: 1.25rem; color: var(--color-graphite-500); text-decoration: line-through;`
- Availability badge: green dot + `color: var(--color-green); font-size: 0.875rem;`
- Add-to-cart button: `.btn.btn--primary.btn--lg` — always full width in the panel
- Star rating color: `color: var(--color-star);` (#FFC041)

**Feature bar (4 icons below hero):**
- Each icon: `.card-icon` (2.5rem × 2.5rem, `var(--radius-lg)`, teal 8% bg)
- Label below icon: `font-size: 0.8125rem; font-weight: 600; color: var(--color-digital-black);`
- Sub-label: `font-size: 0.75rem; color: var(--color-graphite-600);`
- Layout: 4-col on desktop, 2-col on mobile (never 1-col)

**Specs / dimensions table — use this exact structure:**

```html
<div class="specs-table-wrapper">
  <table class="specs-table">
    <tbody>
      <tr>
        <td class="specs-label">Breite</td>
        <td class="specs-value">72 cm</td>
      </tr>
      <tr>
        <td class="specs-label">Höhe</td>
        <td class="specs-value">145 cm</td>
      </tr>
      <!-- repeat for each spec row -->
    </tbody>
  </table>
</div>
```

```css
.specs-table-wrapper {
  border: 0.0625rem solid var(--color-graphite-200);
  border-radius: var(--radius-lg);
  overflow: hidden;
}
.specs-table {
  width: 100%; border-collapse: collapse; font-family: var(--font-family);
}
.specs-table tr { border-bottom: 0.0625rem solid var(--color-graphite-100); }
.specs-table tr:last-child { border-bottom: none; }
.specs-table tr:hover { background: var(--color-paper); }
.specs-label {
  padding: 0.75rem 1rem; width: 40%;
  font-size: 0.875rem; color: var(--color-graphite-600); font-weight: 400;
}
.specs-value {
  padding: 0.75rem 1rem;
  font-size: 0.9375rem; color: var(--color-digital-black); font-weight: 600;
}
```

**FAQ accordion — ALWAYS use the exact design system component. Copy this HTML and CSS verbatim:**

```html
<div class="faq-stage">
  <div class="faq-header">
    <p class="faq-label">HÄUFIGE FRAGEN</p>
    <h2 class="faq-heading">Gut zu wissen</h2>
  </div>
  <ul class="faq-list">
    <li class="faq-item">
      <button class="faq-btn" aria-expanded="false" onclick="toggleFaq(this)">
        <span class="faq-left">
          <span class="faq-q">Question text here?</span>
        </span>
        <span class="faq-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
        </span>
      </button>
      <div class="faq-body">
        <div class="faq-body-inner">
          <p class="faq-answer">Answer text here.</p>
        </div>
      </div>
    </li>
    <!-- repeat <li class="faq-item"> for each question -->
  </ul>
</div>

<script>
function toggleFaq(btn) {
  const item = btn.closest('.faq-item');
  const body = item.querySelector('.faq-body');
  const isOpen = item.classList.contains('is-open');
  document.querySelectorAll('.faq-item.is-open').forEach(el => {
    el.classList.remove('is-open');
    el.querySelector('.faq-body').classList.remove('is-open');
    el.querySelector('.faq-btn').setAttribute('aria-expanded','false');
  });
  if (!isOpen) {
    item.classList.add('is-open');
    body.classList.add('is-open');
    btn.setAttribute('aria-expanded','true');
  }
}
</script>
```

```css
.faq-stage { border-top: 0.0625rem solid var(--color-graphite-200); padding: 2.5rem 0 3rem; display: flex; flex-direction: column; align-items: center; }
.faq-header { text-align: center; margin-bottom: 2.5rem; }
.faq-label { font-size: 0.75rem; font-weight: 700; line-height: 1.4; letter-spacing: 0.15em; text-transform: uppercase; color: var(--color-teal); margin: 0 0 1.25rem; }
.faq-heading { font-size: 2.875rem; font-weight: 700; line-height: 1.15; letter-spacing: -0.02em; color: var(--color-digital-black); margin: 0; }
.faq-list { list-style: none; margin: 0; padding: 0; width: 100%; max-width: 54rem; display: flex; flex-direction: column; gap: 0.75rem; }
.faq-item { position: relative; background: var(--color-white); border: 0.0625rem solid var(--color-graphite-200); border-radius: 0.5rem; overflow: hidden; transition: border-color 0.2s ease, box-shadow 0.2s ease; }
.faq-item:hover { border-color: var(--color-teal); }
.faq-item.is-open { border-color: var(--color-teal); background: linear-gradient(180deg, var(--color-white) 0%, var(--color-paper) 100%); }
.faq-item.is-open::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 0.25rem; background: var(--color-teal); }
.faq-btn { width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 1.5rem; background: none; border: none; cursor: pointer; text-align: left; }
.faq-left { display: flex; align-items: center; gap: 1.25rem; min-width: 0; }
.faq-q { font-size: 1.125rem; font-weight: 700; color: var(--color-digital-black); line-height: 1.3; letter-spacing: -0.01em; margin: 0; }
.faq-btn:hover .faq-q { color: var(--color-teal); }
.faq-icon { width: 2rem; height: 2rem; display: inline-flex; align-items: center; justify-content: center; color: var(--color-teal); transition: transform 0.35s cubic-bezier(.22,1,.36,1); flex-shrink: 0; }
.faq-item.is-open .faq-icon { transform: rotate(180deg); }
.faq-body { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 400ms cubic-bezier(.22,1,.36,1); }
.faq-body.is-open { grid-template-rows: 1fr; }
.faq-body-inner { overflow: hidden; min-height: 0; }
.faq-answer { font-size: 1rem; line-height: 1.7; color: var(--color-graphite-700); padding: 0 1.5rem 1.75rem; margin: 0; max-width: 42rem; }
@media (max-width: 62.5rem) { .faq-heading { font-size: 1.875rem; } }
@media (max-width: 35rem) {
  .faq-heading { font-size: 1.5rem; }
  .faq-btn { padding: 1.25rem 1.125rem; }
  .faq-left { gap: 0.875rem; }
  .faq-answer { padding: 0 1.125rem 1.5rem; }
}
```

Key rules:
- Icon is a **chevron** (not `+`/`×`) that **rotates 180deg** when open
- Open item gets a **left accent bar** via `::before` (0.25rem teal) and **teal border**
- `max-width: 54rem` on `.faq-list` is correct per design system — do not change it
- Question: `font-size: 1.125rem; font-weight: 700` — NEVER 1rem/600
- Answer: `font-size: 1rem; color: var(--color-graphite-700)` — 1rem is correct, g-700 is correct here

---

## 21 · Anschlussschemata — Claude skill `metzler-anschlussschema`

Wiring diagrams (Anschlussschemata, Anschlusspläne, Verdrahtungspläne) for Metzler intercoms are **never drawn freehand**. Use the skill in `tools/claude-code/metzler-anschlussschema/`. It is installed like `metzler-web`: symlink it into `~/.claude/skills/`. Kit page: section `#anschlussschemata`.

- **Systems:** XDM10 2-Draht-BUS, VDM10 2.0 (2-Draht IP and LAN/PoE), ADM10, SDM10 – also Paketbox and Briefkasten with intercom.
- **Output:**
  - Vector PDF + SVG, 1280 px canvas.
  - Kit tokens only, type scale 30 · 24 · 20 · 18 · 16 · 14 · 12 px.
  - German copy.
  - Footer with source and „Arbeiten an 230 V nur durch eine Elektrofachkraft.“
- **Cable colours:**

  | Line | Drawn as |
  |---|---|
  | 2-Draht | red + yellow pair |
  | RS-485 | green + white pair |
  | LAN | blue cable with RJ45 plug |
  | DC | red + / black − |
  | 230 V | brown L / blue N |
  | WLAN | teal dashed |

- **Rules with sources:** `references/systeme.md`. Examples:
  - VDM10 2-Draht: the door station always goes on CH6.
  - XDM10: max. 4 indoor stations per PSU36.
  - SDM10: never PoE at the door station.
  - Sicherheitsmodul: 12 V DC door openers only, and it is the last device on the RS-485 bus.
- **Devices:** only from `scripts/devices.py` (real proportions, shop look); catalogue in `references/geraete.md`.
- **Examples:** `beispiele/` holds 5 reference schemes as PDF, SVG and PNG.
