# Metzler Design System — Claude Page Brief

Paste this file into Claude when asking it to build any Metzler page, section, or component.
Follow every rule here exactly. Do not invent values, do not skip sections, do not use custom fonts or external libraries.

---

## 1 · Brand & Language

- **Company:** Metzler GmbH — outdoor hardware (intercoms, mailboxes, doorbells, house numbers)
- **Language:** German (DE) everywhere — all copy, labels, placeholders, CTAs
- **Font:** system stack, no import needed
  - macOS / Linux → `"Helvetica Neue", Helvetica, Arial, sans-serif`
  - Windows → `Arial, "Helvetica Neue", Helvetica, sans-serif`
  - Use one declaration: `font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;`
- **Base:** 16px = 1rem — all measurements in rem, never px

---

## 2 · Design Tokens

Copy this block into every page `<style>` (or link `metzler-tokens.css`):

```css
:root {
  --font: "Helvetica Neue", Helvetica, Arial, sans-serif;

  /* ── TEAL — primary brand ── */
  --teal-50:    #F2F6F6;   /* icon badge backgrounds */
  --teal-75:    #E3F2F0;   /* light tint hover fills */
  --teal-100:   #E6EEEE;   /* selected backgrounds */
  --teal:       #015253;   /* CTAs, links, active borders, focus rings */
  --teal-600:   #014A4B;   /* hover / pressed state */
  --teal-700:   #01292A;   /* high-contrast text on light */
  --teal-900:   #001D1D;   /* footer background */

  /* ── BRAND ── */
  --rot:        #D42924;   /* Metzler Rot — logo M-square, sale badges ONLY */
  --black:      #1A171B;   /* Digital Schwarz — headlines, wordmark */

  /* ── STATUS ── */
  --green:      #009951;   /* success, availability dot */
  --red-50:     #FFF0EF;   /* error background */
  --red:        #D42924;   /* error borders, text */
  --red-600:    #B52320;   /* error hover */

  /* ── ACCENT ── */
  --mint:       #5CDBD3;   /* links / icons on dark/teal backgrounds */
  --star:       #FFC041;   /* rating stars only */

  /* ── SURFACES ── */
  --white:      #FFFFFF;   /* card backgrounds, input backgrounds */
  --paper:      #F5F6FA;   /* page background, secondary surfaces */
  --g-100:      #F0F0F0;   /* row separators, skeleton fills */
  --g-200:      #E6E6E8;   /* hairline dividers (1px lines) */
  --g-300:      #DADADA;   /* default borders on inputs, cards */

  /* ── TEXT ── */
  --g-500:      #A1A1A1;   /* placeholder, disabled, metadata */
  --g-600:      #7A7A82;   /* captions, secondary labels */
  --g-700:      #54545C;   /* secondary body text */
  --g-800:      #2E2E36;   /* primary body text */
  --g-900:      #1A1A1F;   /* heading text (alternative to --black) */

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
  --gradient-brand:  linear-gradient(90deg, #01292A 0%, #011a1b 35%, #050505 70%, #000 100%);
  --gradient-accent: linear-gradient(135deg, #5CDBD3 0%, #015253 100%);
}
```

---

## 3 · Typography — Rules and CSS

**Font weight vocabulary:** 400 = regular, 500 = medium, 700 = bold, 800 = extrabold

All text uses `font-family: var(--font)` — never set a custom font-family.
Letter-spacing is negative on large headings, zero on body.

```css
/* ── HEADINGS ── */
h1, .h1 {
  font-size: 1.875rem;        /* 30px */
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: -0.02em;
  color: var(--black);
  font-family: var(--font);
  margin: 0 0 1rem;
}
h2, .h2 {
  font-size: 1.5rem;          /* 24px */
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -0.015em;
  color: var(--black);
  font-family: var(--font);
  margin: 0 0 0.875rem;
}
h3, .h3 {
  font-size: 1.25rem;         /* 20px */
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -0.01em;
  color: var(--black);
  font-family: var(--font);
  margin: 0 0 0.75rem;
}
h4, .h4 {
  font-size: 1.125rem;        /* 18px */
  font-weight: 700;
  line-height: 1.375;
  letter-spacing: -0.005em;
  color: var(--black);
  font-family: var(--font);
  margin: 0 0 0.625rem;
}

/* ── BODY ── */
p, .body {
  font-size: 1rem;            /* 16px */
  font-weight: 400;
  line-height: 1.55;
  color: var(--g-800);
  font-family: var(--font);
  margin: 0 0 1rem;
}
.body-sm {
  font-size: 0.875rem;        /* 14px */
  line-height: 1.5;
  color: var(--g-700);
  font-family: var(--font);
}
.caption {
  font-size: 0.75rem;         /* 12px */
  line-height: 1.4;
  color: var(--g-600);
  font-family: var(--font);
}

/* ── LABELS / OVERLINES ── */
.overline {
  font-size: 0.6875rem;       /* 11px */
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--g-600);
  font-family: var(--font);
}
.label {
  font-size: 0.8125rem;       /* 13px */
  font-weight: 600;
  color: var(--g-800);
  font-family: var(--font);
}

/* ── DISPLAY (hero headlines only) ── */
.display-1 { font-size: clamp(3rem, 9vw, 8rem);   font-weight: 700; line-height: 0.85; letter-spacing: -0.04em; }
.display-2 { font-size: clamp(3rem, 7vw, 6rem);   font-weight: 700; line-height: 0.92; letter-spacing: -0.04em; }
.display-3 { font-size: clamp(2rem, 5vw, 4.5rem); font-weight: 700; line-height: 1.0;  letter-spacing: -0.03em; }
.display-4 { font-size: 2.875rem;                  font-weight: 700; line-height: 1.1;  letter-spacing: -0.02em; }
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
- Outer `<section>` / `<header>` / `<footer>` elements have NO horizontal padding of their own
- Full-width backgrounds are on the outer element; text content is always inside `.container`
- All content left-edges align with the logo left-edge — achieved automatically by `.container`

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
      <span style="font-size:1.0625rem; font-weight:800; letter-spacing:0.14em; color:#1A171B; font-family:var(--font);">METZLER</span>
    </a>

    <!-- Alle Kategorien button -->
    <button style="background:var(--teal); color:#fff; border:none; border-radius:var(--radius);
                   height:2.5rem; padding:0 1.125rem; font-size:1rem; font-weight:500;
                   font-family:var(--font); cursor:pointer; display:flex; align-items:center; gap:0.5rem; flex-shrink:0;">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>
      </svg>
      Alle Kategorien
    </button>

    <!-- Search bar -->
    <div style="flex:1; height:2.5rem; background:var(--paper); border:0.0625rem solid var(--g-300);
                border-radius:var(--radius); display:flex; align-items:center; padding:0 0.875rem; gap:0.625rem;">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#A1A1A1" stroke-width="2">
        <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
      </svg>
      <input type="search" placeholder="Suchen — Türklingel, Briefkasten, Hausnummer …"
             style="flex:1; border:none; background:none; font-size:0.9375rem; font-family:var(--font);
                    color:var(--black); outline:none;"/>
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
  background: var(--white);
  border-bottom: 0.0625rem solid var(--g-200);
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
  border-radius: 50%; color: var(--black); text-decoration: none;
  transition: background 0.14s;
}
.header-icon-btn:hover { background: var(--paper); }
```

```js
// Sticky header — activate only after first scroll
window.addEventListener('scroll', () => {
  document.getElementById('site-header')
    .classList.toggle('is-sticky', window.scrollY > 0);
}, { passive: true });
```

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
.site-header--mobile { border-bottom: 0.0625rem solid var(--g-300); }
.mobile-icon-btn {
  width: 2rem; height: 2rem;
  background: none; border: none; cursor: pointer; padding: 0;
  display: flex; align-items: center; justify-content: center;
  color: var(--black);
}
```

---

## 8 · Breadcrumbs

Always left-aligned, always below the header, always in the same container.

```html
<section class="breadcrumb-bar">
  <div class="container">
    <nav aria-label="Breadcrumb">
      <ol class="breadcrumb">
        <li><a href="/">Home</a></li>
        <li><a href="/kategorie">Türsprechanlagen</a></li>
        <li aria-current="page">XDM10</li>
      </ol>
    </nav>
  </div>
</section>
```

```css
.breadcrumb-bar {
  background: var(--white);
  border-bottom: 0.0625rem solid var(--g-200);
  padding: 0.625rem 0;
}
.breadcrumb {
  list-style: none; margin: 0; padding: 0;
  display: flex; align-items: center; gap: 0.375rem; flex-wrap: wrap;
  font-size: 0.8125rem; font-family: var(--font);
}
.breadcrumb li { display: flex; align-items: center; gap: 0.375rem; }
.breadcrumb li:not(:last-child)::after {
  content: "/"; color: var(--g-500); font-size: 0.75rem;
}
.breadcrumb a { color: var(--g-600); text-decoration: none; }
.breadcrumb a:hover { color: var(--teal); }
.breadcrumb li:last-child { color: var(--black); font-weight: 500; }
```

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
  background: var(--teal-900);
  color: var(--white);
}
/* Tinted background section */
.section--tinted { background: var(--paper); }

/* White background section */
.section--white { background: var(--white); }

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
  font-size: 1rem; color: var(--g-700); max-width: 60ch; line-height: 1.6;
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
  border: none; border-top: 0.0625rem solid var(--g-200);
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
  background: var(--white);
  border: 0.0625rem solid var(--g-200);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: box-shadow 0.18s, border-color 0.18s;
}
.card:hover {
  box-shadow: var(--shadow-hover);
  border-color: var(--g-300);
}

/* Card padding variants */
.card__body          { padding: 1.5rem; }
.card__body--compact { padding: 1rem 1.25rem; }
.card__body--loose   { padding: 2rem 2.5rem; }

/* Icon badge inside card (for feature cards) */
.card-icon {
  width: 2.5rem; height: 2.5rem;
  border-radius: 0.625rem;
  background: rgba(1,82,83,0.08);
  color: var(--teal);
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
  font-size: 1rem; font-weight: 500; font-family: var(--font);
  border: none; border-radius: var(--radius);
  cursor: pointer; text-decoration: none; white-space: nowrap;
  transition: background 0.14s, color 0.14s, border-color 0.14s;
}
.btn--sm { height: 2.25rem; padding: 0 1rem; font-size: 0.875rem; }
.btn--lg { height: 3.25rem; padding: 0 2rem; font-size: 1.0625rem; }

/* Primary */
.btn--primary { background: var(--teal); color: #fff; }
.btn--primary:hover  { background: var(--teal-600); }
.btn--primary:active { background: var(--teal-700); }

/* Secondary (outline) */
.btn--secondary {
  background: transparent; color: var(--teal);
  border: 0.125rem solid var(--teal);
}
.btn--secondary:hover { background: var(--teal-50); }

/* Ghost */
.btn--ghost {
  background: transparent; color: var(--g-700);
  border: 0.0625rem solid var(--g-300);
}
.btn--ghost:hover { background: var(--paper); border-color: var(--g-400); }

/* Danger */
.btn--danger { background: var(--red); color: #fff; }
.btn--danger:hover { background: var(--red-600); }

/* Block button — full width on mobile */
@media (max-width: 48rem) {
  .btn--block-mobile { width: 100%; }
}
```

---

## 12 · Form Inputs

```css
.input {
  width: 100%; height: 3rem;
  border: 0.0625rem solid var(--g-300);
  border-radius: var(--radius);
  padding: 0 1rem; font-size: 1rem; font-family: var(--font);
  color: var(--g-800); background: var(--white); outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.input:focus {
  border-color: var(--teal);
  box-shadow: 0 0 0 0.1875rem rgba(1,82,83,0.15);
}
.input::placeholder { color: var(--g-500); }
.input.is-error     { border-color: var(--red); }
.input:disabled     { background: var(--paper); color: var(--g-500); cursor: not-allowed; }

/* Label above input */
.input-label {
  display: block; margin-bottom: 0.375rem;
  font-size: 0.875rem; font-weight: 600;
  color: var(--g-800); font-family: var(--font);
}
/* Error message below input */
.input-error {
  margin-top: 0.25rem; font-size: 0.8125rem;
  color: var(--red); font-family: var(--font);
}
```

---

## 13 · Colors — When to Use What

| Context | Token |
|---------|-------|
| Page background | `--paper` |
| Card / panel background | `--white` |
| Primary CTA, links, active state | `--teal` |
| CTA hover | `--teal-600` |
| Hairline dividers between sections | `--g-200` |
| Default card / input borders | `--g-300` |
| Main headline text | `--black` |
| Body text | `--g-800` |
| Secondary / supporting text | `--g-700` |
| Captions, metadata | `--g-600` |
| Placeholder, disabled | `--g-500` |
| Footer background | `--teal-900` |
| Links / icons on footer / dark bg | `--mint` |
| Error state | `--red` |
| Success / availability | `--green` |
| Metzler logo M-square + sale badge | `--rot` |
| Rating stars only | `--star` |

**Icon badge tint** (feature cards, support cards): `background: rgba(1,82,83,0.08)` — do not use `--teal-50` for this.

---

## 14 · Footer

```html
<footer class="site-footer">
  <div class="container">

    <!-- Top row: 4 columns -->
    <div class="footer-grid">

      <!-- Col 1: logo + description -->
      <div class="footer-col footer-col--brand">
        <!-- logo -->
        <p style="font-size:0.875rem; color:rgba(255,255,255,0.65); line-height:1.6; margin:1rem 0 0;">
          Metzler GmbH — Ihre Experten für Türsprechanlagen, Briefkästen und Hausnummern.
        </p>
      </div>

      <!-- Col 2–3: link lists -->
      <div class="footer-col">
        <p class="footer-col-heading">Produkte</p>
        <ul class="footer-links">
          <li><a href="#">Türsprechanlagen</a></li>
          <li><a href="#">Briefkästen</a></li>
          <li><a href="#">Hausnummern</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <p class="footer-col-heading">Service</p>
        <ul class="footer-links">
          <li><a href="#">Support</a></li>
          <li><a href="#">Installation</a></li>
          <li><a href="#">FAQ</a></li>
        </ul>
      </div>

      <!-- Col 4: contact -->
      <div class="footer-col">
        <p class="footer-col-heading">Kontakt</p>
        <p style="font-size:0.875rem; color:rgba(255,255,255,0.65);">
          Mo – Fr · 08:00 – 17:00 Uhr<br>
          +49 (0) 7181 / 4999 110
        </p>
      </div>
    </div>

    <!-- Divider -->
    <div class="divider divider--dark"></div>

    <!-- Legal row -->
    <div class="footer-legal">
      <span>© 2026 Metzler GmbH</span>
      <div style="display:flex; gap:1.5rem; flex-wrap:wrap;">
        <a href="#">Impressum</a>
        <a href="#">Datenschutz</a>
        <a href="#">AGB</a>
        <a href="#">Widerrufsrecht</a>
      </div>
    </div>

  </div>
</footer>
```

```css
.site-footer {
  background: var(--teal-900);
  color: var(--white);
  padding: 3.5rem 0 1.5rem;
  margin-top: 5rem;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.6fr 1fr 1fr 1fr;
  gap: 3rem;
  margin-bottom: 2.5rem;
}
.footer-col-heading {
  font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--mint);
  margin: 0 0 1rem; font-family: var(--font);
}
.footer-links { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.625rem; }
.footer-links a {
  font-size: 0.9375rem; color: rgba(255,255,255,0.72);
  text-decoration: none; font-family: var(--font);
  transition: color 0.14s;
}
.footer-links a:hover { color: var(--mint); }
.footer-legal {
  display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;
  font-size: 0.8125rem; color: rgba(255,255,255,0.45); font-family: var(--font);
}
.footer-legal a { color: rgba(255,255,255,0.45); text-decoration: none; }
.footer-legal a:hover { color: var(--white); }

/* Mobile footer */
@media (max-width: 48rem) {
  .site-footer { padding: 2.5rem 0 1.5rem; }
  .footer-grid { grid-template-columns: 1fr; gap: 2rem; }
  .footer-legal { flex-direction: column; align-items: flex-start; }
}
```

---

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
2. **All colors from tokens** — never use bare hex codes; reference `var(--teal)`, `var(--g-200)` etc.
3. **Font always `var(--font)`** — never set a custom font-family
4. **Container max-width exactly 100rem** — never 90rem, 1440px, or anything else
5. **No padding on `<header>` / `<footer>` outer tags** — padding lives inside `.container` only
6. **Header two-state:** not sticky at page load; `.is-sticky` class added via JS on first scroll
7. **Breadcrumbs always left-aligned** — never centered
8. **Footer always `var(--teal-900)` background** — never a custom dark color
9. **Cards always `var(--radius-lg)` (0.5rem) radius** — never sharp corners, never pill-radius
10. **Arrows / carousel controls never show step numbers** — navigation arrows are controls only
11. **No external icon libraries** — use inline `<svg>` with `stroke="currentColor"`, `stroke-width: 1.8–2`, `stroke-linecap: round`, `stroke-linejoin: round`, `fill: none`; icon container is 2.5rem × 2.5rem with `border-radius: 0.625rem`
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
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; background: #F5F6FA; }

    :root {
      --font: "Helvetica Neue", Helvetica, Arial, sans-serif;
      --teal: #015253; --teal-600: #014A4B; --teal-900: #001D1D;
      --teal-50: #F2F6F6; --mint: #5CDBD3;
      --black: #1A171B; --rot: #D42924;
      --white: #FFFFFF; --paper: #F5F6FA;
      --g-200: #E6E6E8; --g-300: #DADADA;
      --g-600: #7A7A82; --g-700: #54545C; --g-800: #2E2E36;
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

  <section class="section section--white">
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
    window.addEventListener('scroll', () => {
      document.getElementById('site-header')
        .classList.toggle('is-sticky', window.scrollY > 0);
    }, { passive: true });
  </script>
</body>
</html>
```
