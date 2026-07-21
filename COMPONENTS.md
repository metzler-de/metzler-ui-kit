# Metzler Design System — Component Catalog (COMPONENTS.md)

> **Maschinell generierter Export** aus dem gerenderten UI Kit (https://metzler-de.github.io/metzler-ui-kit/), Stand 2026-07-21, Kit-Version v1.8.
> Vollständige Komponenten-Doku der ComponentsPage: alle 31 Kapitel mit Regeln, HTML-Beispielen und CSS-Definitionen.
> **Source of truth** ist das gerenderte Kit; bei Abweichungen gewinnt das Kit, dann diesen Export neu generieren.

---
## Introduction

### One source of truth for all Metzler digital products
A complete library of design tokens, reusable components, and interaction patterns that keep every Metzler product consistent, accessible, and fast to build.

`Copy` `#015253` - metzler-design-system.md — add it if Claude needs more detail on a specific component's exact states/variants than FOR-CLAUDE.md's condensed version gives.
- metzler-tokens.css — not for reading, for shipping: give it to Claude when you want the finished page to <link> the real stylesheet instead of an inlined token block.

## Favicon

```html
<!-- Pflicht im <head> jeder Metzler-Seite (Datei-Variante) -->
<link rel="icon" type="image/svg+xml" href="favicon.svg">
```
Self-contained Variante — inline Data-URI, kein externes Asset nötig (empfohlen für Einzeldatei-Seiten):

```html
<link rel="icon" type="image/svg+xml"
  href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 184.3 184.3'%3E%3Crect width='184.3' height='184.3' rx='5.75' fill='%23cc322b'/%3E%3Cpath fill='%23fff' d='M70.19,34.81l19.04,32.98-9.58,16.57-28.59-49.55h19.13ZM70.28,108.58h0l-23.45-40.64v85.89h-16.57V34.81h16.57l33.02,57.21L123.92,15.65h19.13l-63.22,109.52-9.58-16.57.02-.02ZM153.14,153.83h-16.57v-85.87l-33,57.14h-19.13l52.11-90.28h16.57v119.02l.02-.02Z'/%3E%3C/svg%3E">
```

## Colors
`T.red` `--color-metzler-rot` `T.dBlack` `--color-digital-black` `T.teal50` `--color-teal-50` `T.teal75` `--color-teal-75` `T.teal100` `--color-teal-100` `T.teal` `--color-teal` `T.teal600` `--color-teal-600` `T.teal700` `--color-teal-700` `T.teal900` `--color-teal-900` `T.green` `--color-green` `T.green` `--color-green` `T.red50` `--color-red-50` `T.red` `--color-metzler-rot` `T.red600` `--color-red-600` `T.red900` `--color-red-900` `T.paper` `--color-paper` `T.g100` `--color-graphite-100` `T.g200` `--color-graphite-200` `T.g300` `--color-graphite-300` `T.g400` `--color-graphite-400` `T.g450` `--color-graphite-450` `T.g500` `--color-graphite-500` `T.g600` `--color-graphite-600` `T.g700` `--color-graphite-700` `T.g800` `--color-graphite-800` `T.g850` `--color-graphite-850` `T.g900` `--color-graphite-900` `T.black` `--color-black` `T.white` `--color-white` `T.white` `--color-white` `T.mint` `--color-mint` 
## Typography
`Arial, "Helvetica Neue", Helvetica, sans-serif` `rem` `"Helvetica Neue", Helvetica, Arial, sans-serif` `--display-1` `T.fD1` `--display-2` `T.fD2` `--display-3` `T.fD3` `--display-4` `T.fD4` 
```html
Desktop 1.875rem · 30px
Tablet 1.625rem · 26px
Mobile 1.5rem · 24px
weight 700 / lh 1.25
```
`.h1` `T.fH1` 
```html
Desktop 1.5rem · 24px
Tablet 1.375rem · 22px
Mobile 1.25rem · 20px
weight 700 / lh 1.3
```
`.h2` `T.fH2` 
```html
Desktop 1.25rem · 20px
Tablet 1.1875rem · 19px
Mobile 1.125rem · 18px
weight 700 / lh 1.35
```
`.h3` `T.fH3` 
```html
Desktop 1.125rem · 18px
Tablet 1.0625rem · 17px
Mobile 1rem · 16px
weight 700 / lh 1.375
```
`.h4` `T.fH4` `--font-regular` `T.fXl` `--font-bold` `T.fXl` `--font-strong` `T.fXl` `--font-regular` `T.fLg` `--font-bold` `T.fLg` `--font-strong` `T.fLg` `--font-regular` `T.fBody` `--font-bold` `T.fBody` `--font-strong` `T.fBody` `--font-regular` `T.fSm` `--font-bold` `T.fSm` `--font-strong` `T.fSm` `--font-regular` `T.fXs` `--font-bold` `T.fXs` `--font-strong` `T.fXs` `--color-graphite-600` 
```html
CSS VARIABLES
/* Typography tokens — paste in :root { } */
/* Base: 1rem = 16px (browser default) */
/* ── Font weights ── */
--font-regular
:
400
;
/* body copy · weight 400 */
--font-bold
:
600
;
/* emphasis · weight 600 */
--font-strong
:
800
;
/* strong emphasis · weight 800 */
/* ── Fluid / Responsive ── */
--display-1
:
5rem
;
/* 80px · lh 0.85 · ls -0.04em · weight 700 */
--display-2
:
3.5rem
;
/* 56px · lh 0.92 · ls -0.04em · weight 700 */
--display-3
:
3rem
;
/* 48px · lh 1.0 · ls -0.03em · weight 700 */
--display-4
:
2.875rem
;
/* 46px · lh 1.15 · weight 700 */
/* ── Headings — .h1–.h4 · 3 sizes: Desktop / Tablet ≤991 / Mobile ≤767 ── */
--text-h1
:
1.875rem
;
/* 30px → 26px → 24px · weight 700 */
--text-h2
:
1.5rem
;
/* 24px → 22px → 20px · weight 700 */
--text-h3
:
1.25rem
;
/* 20px → 19px → 18px · weight 700 */
--text-h4
:
1.125rem
;
/* 18px → 17px → 16px · weight 700 */
/* ── Body 16px ── */
--text-body-xl
:
1.25rem
;
/* 20px · weight 400 */
--text-body-xl-medium
:
1.25rem
;
/* 20px · weight 500 */
--text-body-xl-bold
:
1.25rem
;
/* 20px · weight 700 */
--text-body-lg
:
1.125rem
;
/* 18px · weight 400 */
--text-body-lg-medium
:
1.125rem
;
/* 18px · weight 500 */
--text-body-lg-bold
:
1.125rem
;
/* 18px · weight 700 */
--text-body
:
1rem
;
/* 16px · weight 400 */
--text-body-medium
:
1rem
;
/* 16px · weight 500 */
--text-body-bold
:
1rem
;
/* 16px · weight 700 */
/* ── Body SM 14px ── */
--text-body-sm
:
0.875rem
;
/* 14px · weight 400 */
--text-body-sm-medium
:
0.875rem
;
/* 14px · weight 500 */
--text-body-sm-bold
:
0.875rem
;
/* 14px · weight 700 */
/* ── Caption 12px ── */
--text-caption
:
0.75rem
;
/* 12px · weight 400 */
--text-caption-medium
:
0.75rem
;
/* 12px · weight 500 */
--text-caption-bold
:
0.75rem
;
/* 12px · weight 700 */
```

## Border Radius
`border-radius` `--radius-sm` `T.rSm` `--radius` `T.r` `--radius-lg` `T.rLg` `--radius-pill` `T.rPill` 
## Spacers & Dividers
`S` `M` `L` 
```html
<!-- HTML — add a named class to any block element -->
<div class="spacer-s"></div>   <!-- 24px -->
<div class="spacer-m"></div>   <!-- 48px -->
<div class="spacer-l"></div>   <!-- 96px -->
```

```html
.spacer-s { display: block; height: 1.5rem; }
.spacer-m { display: block; height: 3rem; }
.spacer-l { display: block; height: 6rem; }
```
`S` `M` `L` 
```html
<!-- HTML — use <hr> with a divider class -->
<hr class="divider-s">   <!-- 1rem top & bottom margin -->
<hr class="divider-m">   <!-- 2rem top & bottom margin -->
<hr class="divider-l">   <!-- 4rem top & bottom margin -->
```

```html
.divider-s { border: none; border-top: 0.0625rem solid var(--color-graphite-200, #E6E6E8); margin: 1rem 0; }
.divider-m { border: none; border-top: 0.0625rem solid var(--color-graphite-200, #E6E6E8); margin: 2rem 0; }
.divider-l { border: none; border-top: 0.0625rem solid var(--color-graphite-200, #E6E6E8); margin: 4rem 0; }
```

## Breakpoints
`768px` `xs` `—` `sm` `sm` `md` `md` `lg` `lg` `xl` `xl` `xxl` `xxl` `@media (max-width: 767.98px)` 
```html
/* Metzler breakpoints — mobile-first (min-width) */
/* xs — no query needed; this is the mobile default */
/* sm — landscape phones and up */
@media (min-width: 576px)  { ... }
/* md — tablets and up  ← Mobile UI ends here */
@media (min-width: 768px)  { ... }
/* lg — desktop and up  ← Desktop UI starts here */
@media (min-width: 992px)  { ... }
/* xl — large desktops */
@media (min-width: 1200px) { ... }
/* xxl — wide canvas · Metzler design width */
@media (min-width: 1440px) { ... }
/* Max-width helpers (target mobile only) */
@media (max-width: 767.98px)  { /* xs + sm — mobile styles */ }
@media (max-width: 991.98px)  { /* xs–md — tablet and below */ }
/* Practical example — hide desktop nav on mobile */
.desktop-nav { display: flex; }
.mobile-nav { display: none; }
@media (max-width: 767.98px) {
  .desktop-nav { display: none; }
  .mobile-nav { display: flex; }
}
```

## Buttons
`.btn` 
### Variants
.btn-primary — filled teal, main CTA. .btn-secondary — ghost outline with subtle teal hover tint. .btn-proceed — filled teal with directional arrow. .btn-white — white outline, same proportions as secondary, for dark/colored section backgrounds.

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-proceed">
  Weiter
  <svg width="12" height="10" viewBox="0 0 14 12" fill="none">
    <path d="M1 6h12M7 1l6 5-6 5" stroke="currentColor"
      stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</button>
```

### Disabled state
Add the disabled boolean attribute to any variant. Primary and Proceed get a gray fill; Secondary gets a gray border and text.

```html
<button class="btn btn-primary" disabled>Primary</button>
<button class="btn btn-secondary" disabled>Secondary</button>
<button class="btn btn-proceed" disabled>
  Weiter
  <svg width="12" height="10" viewBox="0 0 14 12" fill="none">
    <path d="M1 6h12M7 1l6 5-6 5" stroke="currentColor"
      stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</button>
```

### Sizes
Add .btn-lg or .btn-sm for size variants. Default (no modifier) is medium. All sizes support every variant with and without the arrow icon — the icon scales proportionally.

LARGE · .BTN-LG · HEIGHT 50PX · 1.1REM / 600

```html
<button class="btn btn-primary btn-lg">Primary</button>
<button class="btn btn-secondary btn-lg">Secondary</button>
<button class="btn btn-proceed btn-lg">Weiter<svg …/></button>
```
MEDIUM · DEFAULT · HEIGHT 42PX · 1REM / 500

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-proceed">Weiter<svg …/></button>
```
SMALL · .BTN-SM · HEIGHT 35PX · 0.9REM / 400

```html
<button class="btn btn-primary btn-sm">Primary</button>
<button class="btn btn-secondary btn-sm">Secondary</button>
<button class="btn btn-proceed btn-sm">Weiter<svg …/></button>
```

### Full-width · .btn-block
Add .btn-block to make a button fill the entire width of its container. Works with all variants and sizes.

```html
<div style="width: 100%">
  <button class="btn btn-primary btn-block">Primary</button>
  <button class="btn btn-secondary btn-block" style="margin-top: 10px">Secondary</button>
  <button class="btn btn-proceed btn-block" style="margin-top: 10px">
    Weiter <svg …/>
  </button>
</div>
```

### White variant · .btn-white

### CSS definitions

```html
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  height: 2.625rem;
  padding: .7rem 1.2rem;
  border-radius: var(--radius);
  font-family: var(--font-family);
  font-size: 1rem;
  font-weight: 500;
  white-space: nowrap;
  line-height: 1.2;
  cursor: pointer;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
}
.btn-lg { font-size: 1.1rem; font-weight: 600; }
.btn-sm { font-size: 0.9rem; font-weight: 400; }
.btn-block {
  display: flex;
  text-align: center;
  width: 100%;
}
.btn-primary,
.btn-proceed { background: var(--color-teal); color: var(--color-white); border: none; }
.btn-primary:hover,  .btn-proceed:hover { background: var(--color-teal-600); }
.btn-primary:active, .btn-proceed:active { background: var(--color-teal-700); }
.btn-primary:disabled, .btn-proceed:disabled { background: var(--color-graphite-500); cursor: default; }
.btn-secondary { background: transparent; color: var(--color-teal); border: 0.125rem solid var(--color-teal); }
.btn-secondary:hover { background: var(--color-teal-100); }
.btn-secondary:active { background: var(--color-teal); color: var(--color-white); }
.btn-secondary:disabled { color: var(--color-graphite-500); border-color: var(--color-graphite-500); cursor: default; }
.btn-white { background: transparent; color: var(--color-white); border: 0.125rem solid var(--color-white); }
.btn-white:hover { background: rgba(255,255,255,0.1); }
.btn-white:active { background: var(--color-white); color: var(--color-teal); border-color: var(--color-white); }
.btn-white:disabled { color: rgba(255,255,255,0.35); border-color: rgba(255,255,255,0.25); cursor: default; }
/* Dark / Hero variants — use on dark or image backgrounds */
.btn-dark,
.btn-dark-outline {
  padding: 0.875rem 1.75rem;
  border-radius: var(--radius);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  text-align: center;
  transition: opacity 0.2s, border-color 0.3s, background 0.3s;
}
.btn-dark { background: var(--color-teal); color: var(--color-white); border: none; }
.btn-dark:hover { opacity: 0.85; }
.btn-dark:disabled { background: rgba(1,82,83,0.4); color: rgba(255,255,255,0.5); cursor: default; }
.btn-dark-outline { background: transparent; color: var(--color-white); border: 0.0625rem solid var(--color-white); }
.btn-dark-outline:hover { border-color: var(--color-teal); background: rgba(255,255,255,0.05); }
.btn-dark-outline:disabled { color: rgba(255,255,255,0.35); border-color: rgba(255,255,255,0.25); cursor: default; }
```

## Navigation Arrows
Square icon-only buttons for carousel and step navigation. Secondary style — teal border, teal icon, tinted hover. Icon: chevron (‹›). Always used as a pair.

LARGE — 50×50PX

```html
<button class="btn-nav btn-nav-lg">
  <svg viewBox="0 0 9 16" fill="none">
    <polyline points="8,1.5 1.5,8 8,14.5"
      stroke="currentColor" stroke-width="2.2"
      stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</button>
<button class="btn-nav btn-nav-lg">
  <svg viewBox="0 0 9 16" fill="none">
    <polyline points="1,1.5 7.5,8 1,14.5"
      stroke="currentColor" stroke-width="2.2"
      stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</button>
```
MEDIUM — 42×42PX

```html
<button class="btn-nav">...</button>
<button class="btn-nav">...</button>
```
SMALL — 35×35PX

```html
<button class="btn-nav btn-nav-sm">...</button>
<button class="btn-nav btn-nav-sm">...</button>
```

### Disabled state

```html
<!-- All disabled -->
<button class="btn-nav" disabled>...</button>
<button class="btn-nav" disabled>...</button>
<!-- First page (left disabled) -->
<button class="btn-nav" disabled>...</button>
<button class="btn-nav">...</button>
<!-- Last page (right disabled) -->
<button class="btn-nav">...</button>
<button class="btn-nav" disabled>...</button>
```

### CSS definitions

```html
.btn-nav {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.625rem;
  height: 2.625rem;
  border-radius: var(--radius);
  background: var(--color-white);
  color: var(--color-teal);
  border: 0.0625rem solid var(--color-teal);
  cursor: pointer;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
}
.btn-nav-lg { width: 3.125rem; height: 3.125rem; }
.btn-nav-sm { width: 2.1875rem; height: 2.1875rem; }
.btn-nav:hover { background: var(--color-teal-100); }
.btn-nav:active { background: var(--color-teal); color: var(--color-white); }
.btn-nav:disabled { color: var(--color-graphite-500); border-color: var(--color-graphite-500); cursor: default; }
/* Dark / inverted variant — use on teal or dark section backgrounds */
.btn-nav-inverted {
  background: transparent;
  color: var(--color-white);
  border: 0.0625rem solid rgba(255, 255, 255, 0.55);
}
.btn-nav-inverted:hover { background: rgba(255, 255, 255, 0.12); }
.btn-nav-inverted:active { background: var(--color-white); color: var(--color-teal); }
.btn-nav-inverted:disabled {
  color: rgba(255, 255, 255, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
  cursor: default;
}
```

### Dark / inverted variant
On teal, dark-teal, or any dark section background use .btn-nav-inverted. The border and icon switch to white; pressing fills the button white with a teal icon — the exact inverse of the default light-surface state.

```html
<button class="btn-nav btn-nav-inverted">‹</button>
<button class="btn-nav btn-nav-inverted">›</button>
<!-- Disabled on dark -->
<button class="btn-nav btn-nav-inverted" disabled>‹</button>
```

## Pagination
Selectable button for pagination and filter lists. Same three sizes as Navigation Arrows. Default: white + 1px solid #015253 border · Hover: teal tint + teal text · Active: #005253 fill + white text · More: no border, shows ….

LARGE — 50×50PX

```html
<button class="listing-btn listing-btn--lg">1</button>
<button class="listing-btn listing-btn--lg">2</button>
<button class="listing-btn listing-btn--lg active">3</button>
<button class="listing-btn listing-btn--lg more">…</button>
```
MEDIUM — 42×42PX

```html
<button class="listing-btn">1</button>
<button class="listing-btn">2</button>
<button class="listing-btn active">3</button>
<button class="listing-btn more">…</button>
```
SMALL — 35×35PX

```html
<button class="listing-btn listing-btn--sm">1</button>
<button class="listing-btn listing-btn--sm">2</button>
<button class="listing-btn listing-btn--sm active">3</button>
<button class="listing-btn listing-btn--sm more">…</button>
```

### Live example

```html
<nav class="pagination">
  <button class="btn-nav" disabled>‹</button>
  <button class="listing-btn">1</button>
  <button class="listing-btn active">2</button>
  <button class="listing-btn">3</button>
  <button class="listing-btn more">…</button>
  <button class="listing-btn">8</button>
  <button class="btn-nav">›</button>
</nav>
```

### CSS definitions

```html
.listing-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.625rem;
  height: 2.625rem;
  border-radius: var(--radius);
  background: var(--color-white);
  border: 0.0625rem solid var(--color-teal);
  font-family: var(--font-family);
  font-size: 1rem;
  font-weight: 500;
  color: var(--color-black);
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease;
}
.listing-btn--lg { width: 3.125rem; height: 3.125rem; font-size: 1.1rem; }
.listing-btn--sm { width: 2.1875rem; height: 2.1875rem; font-size: 0.9rem; }
.listing-btn:hover { background: rgba(1, 82, 83, 0.05); color: var(--color-teal); }
.listing-btn.active { background: var(--color-teal); border-color: var(--color-teal); color: var(--color-white); cursor: default; }
.listing-btn.more { border: none; cursor: default; }
/* Dark / inverted — teal or dark section backgrounds */
.listing-btn-inverted {
  background: transparent;
  border: 0.0625rem solid rgba(255, 255, 255, 0.5);
  color: var(--color-white);
}
.listing-btn-inverted:hover { background: rgba(255, 255, 255, 0.12); }
.listing-btn-inverted.active { background: var(--color-white); color: var(--color-teal); border-color: var(--color-white); cursor: default; }
.listing-btn-inverted.more { border: none; }
```

### Dark / inverted variant
On teal or dark section backgrounds add .listing-btn-inverted alongside .btn-nav-inverted. Active page fills solid white with teal text — inverse of the light-surface state. Fully interactive below.

```html
<nav class="pagination">
  <button class="btn-nav btn-nav-inverted" disabled>‹</button>
  <button class="listing-btn listing-btn-inverted">1</button>
  <button class="listing-btn listing-btn-inverted active">2</button>
  <button class="listing-btn listing-btn-inverted">3</button>
  <button class="listing-btn listing-btn-inverted more">…</button>
  <button class="listing-btn listing-btn-inverted">8</button>
  <button class="btn-nav btn-nav-inverted">›</button>
</nav>
```

## Filter Chips

```html
<div class="filter-chip">
  <span><b>Farbe:</b> Anthrazit</span>
  <button class="filter-chip__remove" aria-label="Filter entfernen">×</button>
</div>
```

```html
.filter-chip {
  display: inline-flex; align-items: center; gap: 0.3125rem;
  height: 2.125rem; padding: 0 0.625rem;
  border: 0.0625rem solid var(--color-teal-100);
  border-radius: var(--radius); font-size: 0.875rem;
}
.filter-chip b { color: var(--color-teal); font-weight: 700; }
.filter-chip__remove {
  width: 1rem; height: 1rem;
  background: var(--color-teal); color: var(--color-white);
  border: none; border-radius: var(--radius-sm);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.875rem; cursor: pointer; line-height: 1;
}
```

## Form Elements

### Textfield
Single-line text input for forms — names, emails, addresses. Comes in four states: Default (empty, waiting), Active (focused, cursor visible), Done (value entered), Error (validation failed). The label floats above the field on focus or when a value is present.

ALL STATES · PADDING 0.7REM 0.9375REM · BORDER-RADIUS 0.25REM

```html
<!-- Default -->
<div class="field-wrapper">
  <input type="text" id="name" placeholder=" "/>
  <label for="name">Name</label>
</div>
<!-- Active (focused) -->
<div class="field-wrapper field--active">
  <input type="text" id="name" placeholder=" "/>
  <label for="name">Name</label>
</div>
<!-- Done (has value) -->
<div class="field-wrapper field--done">
  <input type="text" id="name" value="Vossberg" placeholder=" "/>
  <label for="name">Name</label>
</div>
<!-- Error -->
<div class="field-wrapper field--error">
  <input type="text" id="name" placeholder=" "/>
  <label for="name">Name</label>
  <span class="field__error">Dieses Feld ausfüllen</span>
</div>
```
WITH REQUIREMENT HINT

```html
<div class="field-wrapper">
  <input type="password" id="password" placeholder=" "/>
  <label for="password">Passwort</label>
  <span class="field__hint">Passwort muss aus mindestens 8 Zeichen bestehen.</span>
</div>
```
TRY IT

### Sizing

```html
<input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" aria-label=".form-control-lg example">
<input class="form-control" type="text" placeholder="Default input" aria-label="default input example">
<input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" aria-label=".form-control-sm example">
```

### CSS definitions

```html
/* Base input — padding-based sizing, no fixed height */
.form-control {
  display: block;
  width: 100%;
  padding: 0.7rem 0.9375rem;
  font-family: var(--font-family);
  font-size: 1rem;
  color: var(--color-black);
  background: var(--color-white);
  border: 0.0625rem solid var(--color-graphite-300);
  border-radius: var(--radius);
  box-sizing: border-box;
  outline: none;
  transition: border-color 0.15s;
}
.form-control:focus { border-color: var(--color-teal); }
.form-control.error { border-color: #C90000; }
.form-control-lg { padding: 0.8rem 1rem; font-size: 1.125rem; }
.form-control-sm { padding: 0.35rem 0.75rem; font-size: 0.875rem; }
/* Floating label wrapper */
.field-wrapper { position: relative; }
.field-wrapper label {
  position: absolute;
  left: 0.9375rem;
  top: 50%;
  transform: translateY(-50%);
  font-family: var(--font-family);
  font-size: 1rem;
  color: var(--color-graphite-500);
  pointer-events: none;
  transition: all 0.15s ease;
  background: transparent;
  padding: 0;
  line-height: 1.4;
  white-space: nowrap;
  z-index: 1;
}
/* Float label above the input border on focus or when value is present */
.field-wrapper .form-control:focus + label,
.field-wrapper .form-control:not(:placeholder-shown) + label {
  top: -0.5625rem;
  left: 0.6875rem;
  transform: none;
  font-size: 0.75rem;
  color: var(--color-black);
  background: var(--color-white);
  padding: 0 0.3125rem;
}
/* Error & hint text */
.field__error {
  position: absolute;
  bottom: -0.4375rem;
  right: 0.6875rem;
  background: var(--color-white);
  padding: 0 0.3125rem;
  font-family: var(--font-family);
  font-size: 0.75rem;
  color: #C90000;
  white-space: nowrap;
  line-height: 0.875rem;
}
.field__hint {
  display: block;
  margin-top: 0.3125rem;
  font-family: var(--font-family);
  font-size: 0.8125rem;
  color: #6A6A6A;
  line-height: 1.45;
}
```

### Checkbox
Two checked variants: Filter (teal #015253) for filter panels and navigation, and Configurator (green #009951) for product configurators and selection lists. Unchecked state is always white with a #DADADA border. Click any checkbox to toggle it.

DEFAULT · 25×25PX · BORDER-RADIUS 4PX

```html
<!-- Unchecked -->
<label class="checkbox-wrapper">
  <span class="checkbox"></span>
  Label
</label>
<!-- Checked – Filter (Teal) -->
<label class="checkbox-wrapper">
  <span class="checkbox checked-filter">
    <svg width="13" height="13" viewBox="0 0 14 14" fill="none">
      <path d="M2 7l3.5 3.5L12 3" stroke={T.white} stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
  Filter option
</label>
<!-- Checked – Configurator (Green) -->
<label class="checkbox-wrapper">
  <span class="checkbox checked-config">
    <svg width="13" height="13" viewBox="0 0 14 14" fill="none">
      <path d="M2 7l3.5 3.5L12 3" stroke={T.white} stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
  Configurator option
</label>
```
SMALL · 18×18PX · BORDER-RADIUS 3PX · ADD .CHECKBOX-SM

```html
<!-- Small — add class .checkbox-sm to wrapper -->
<label class="checkbox-wrapper checkbox-sm">
  <span class="checkbox"></span>
  Label
</label>
<label class="checkbox-wrapper checkbox-sm">
  <span class="checkbox checked-filter">
    <svg width="9" height="9" viewBox="0 0 14 14" fill="none">
      <path d="M2 7l3.5 3.5L12 3" stroke={T.white} stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
  Filter option
</label>
<label class="checkbox-wrapper checkbox-sm">
  <span class="checkbox checked-config">
    <svg width="9" height="9" viewBox="0 0 14 14" fill="none">
      <path d="M2 7l3.5 3.5L12 3" stroke={T.white} stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
  Configurator option
</label>
```
DARK BACKGROUND — INVERTED

```html
<!-- On dark/teal backgrounds the unchecked box uses a white border.
     Checked variants (teal fill, green fill) work unchanged. -->
<!-- Unchecked on dark -->
<label class="checkbox-wrapper checkbox-dark">
  <span class="checkbox"></span>
  Unchecked
</label>
<!-- Checked – Filter (Teal fill — same as light) -->
<label class="checkbox-wrapper checkbox-dark">
  <span class="checkbox checked-filter">...</span>
  Filter option
</label>
/* CSS */
.checkbox-dark { color: var(--color-white); }
.checkbox-dark .checkbox {
  border-color: rgba(255, 255, 255, 0.55);
  background: transparent;
}
```

### CSS definitions

```html
.checkbox-wrapper {
  display: inline-flex;
  align-items: center;
  gap: 0.5625rem;
  cursor: pointer;
  font-family: var(--font-family);
  font-size: 1rem;
  color: var(--color-black);
  user-select: none;
}
.checkbox-wrapper.checkbox-sm { font-size: 0.875rem; }
.checkbox {
  width: 1.5625rem;
  height: 1.5625rem;
  border-radius: var(--radius);
  border: 0.0625rem solid var(--color-graphite-300);
  background: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-sizing: border-box;
  transition: background 0.12s;
}
.checkbox-sm .checkbox { width: 1.125rem; height: 1.125rem; border-radius: 0.1875rem; }
.checkbox.checked-filter { background: var(--color-teal); border-color: var(--color-teal); }
.checkbox.checked-config { background: var(--color-green); border-color: var(--color-green); }
```

### Radio Button
Circular single-select control. Active state shows a Metzler teal #015253 dot. Error state uses a red #C90000 border. Disabled reduces opacity and blocks interaction. Click any unselected radio to activate it.

DEFAULT · 20×20PX

```html
<!-- Default (Unselected) -->
<label class="radio-wrapper">
  <span class="radio"></span>
  Unselected
</label>
<!-- Active (Selected) -->
<label class="radio-wrapper">
  <span class="radio active"></span>
  Selected
</label>
<!-- Disabled -->
<label class="radio-wrapper disabled">
  <span class="radio"></span>
  Disabled
</label>
<!-- Error -->
<label class="radio-wrapper">
  <span class="radio error"></span>
  Error state
</label>
```
SMALL · 16×16PX · ADD .RADIO-SM

```html
<!-- Small — add class .radio-sm to wrapper -->
<label class="radio-wrapper radio-sm">
  <span class="radio"></span>
  Unselected
</label>
<label class="radio-wrapper radio-sm">
  <span class="radio active"></span>
  Selected
</label>
<label class="radio-wrapper radio-sm disabled">
  <span class="radio"></span>
  Disabled
</label>
<label class="radio-wrapper radio-sm">
  <span class="radio error"></span>
  Error state
</label>
```

### CSS definitions

```html
.radio-wrapper {
  display: inline-flex;
  align-items: center;
  gap: 0.5625rem;
  cursor: pointer;
  font-family: var(--font-family);
  font-size: 1rem;
  color: var(--color-black);
  user-select: none;
}
.radio-wrapper.radio-sm { font-size: 0.875rem; }
.radio-wrapper.disabled { opacity: 0.45; cursor: not-allowed; }
.radio {
  width: 1.25rem;
  height: 1.25rem;
  border-radius: 50%;
  border: 0.0625rem solid var(--color-graphite-300);
  background: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-sizing: border-box;
  transition: border-color 0.12s;
}
.radio-sm .radio { width: 1rem; height: 1rem; }
.radio.active::after {
  content: '';
  width: 0.8125rem;
  height: 0.8125rem;
  border-radius: 50%;
  background: var(--color-teal);
}
.radio-sm .radio.active::after { width: 0.625rem; height: 0.625rem; }
.radio.active { border-color: var(--color-teal); }
.radio.error { border-color: #C90000; }
```

### Switch
Toggle switch — styled checkbox rendered as a pill track with a sliding knob. Off: #DADADA track. On: #015253 teal track. Knob uses a spring transition. Disabled reduces opacity and blocks interaction.

STATES · CLICK TO TOGGLE

```html
<div class="form-switch">
<input class="form-switch-input" type="checkbox" role="switch" id="sw1">
<label class="form-switch-label" for="sw1">Default switch</label>
</div>
<div class="form-switch">
<input class="form-switch-input" type="checkbox" role="switch" id="sw2" checked>
<label class="form-switch-label" for="sw2">Checked switch</label>
</div>
<div class="form-switch">
<input class="form-switch-input" type="checkbox" role="switch" id="sw3" disabled>
<label class="form-switch-label" for="sw3">Disabled switch</label>
</div>
<div class="form-switch">
<input class="form-switch-input" type="checkbox" role="switch" id="sw4" checked disabled>
<label class="form-switch-label" for="sw4">Disabled checked</label>
</div>
```

```html
.form-switch {
display: inline-flex;
align-items: center;
gap: 0.625rem;
cursor: pointer;
user-select: none;
}
.form-switch-input {
appearance: none;
-webkit-appearance: none;
position: relative;
width: 2.75rem;  /* 44px */
height: 1.5rem;  /* 24px */
border-radius: var(--radius-pill);  /* always fully rounded */
background: var(--color-graphite-300);
cursor: pointer;
flex-shrink: 0;
outline: none;
margin: 0;
transition: background 0.2s;
}
.form-switch-input::after {
content: '';
position: absolute;
top: 0.1875rem;  /* 3px */
left: 0.1875rem;
width: 1.125rem;  /* 18px */
height: 1.125rem;
border-radius: 50%;
background: var(--color-white);
box-shadow: 0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.15);
transition: left 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.form-switch-input:checked {
background: var(--color-teal);
}
.form-switch-input:checked::after {
left: calc(100% - 1.3125rem);  /* 21px from right */
}
.form-switch-input:disabled {
opacity: 0.5;
cursor: not-allowed;
}
.form-switch-input:focus-visible {
box-shadow: 0 0 0 0.1875rem rgba(1, 82, 83, 0.25);
}
.form-switch-label {
font-family: var(--font-family);
font-size: 1rem;
color: var(--color-black);
cursor: pointer;
}
```

## Quantity Counter

```html
<!-- Default (md) -->
<div class="qty-counter">
  <button class="qty-btn" aria-label="Decrease">−</button>
  <span class="qty-value">1</span>
  <button class="qty-btn" aria-label="Increase">+</button>
</div>
<!-- Large -->
<div class="qty-counter qty-counter-lg">...</div>
<!-- Small -->
<div class="qty-counter qty-counter-sm">...</div>
<!-- Disabled -->
<div class="qty-counter" aria-disabled="true">...</div>
```

```html
.qty-counter {
  display: inline-flex;
  align-items: center;
  border: 0.0625rem solid var(--color-graphite-300);
  border-radius: var(--radius);  /* 4px — all sizes */
  height: 2.5rem;  /* 40px */
  min-width: 8.25rem;
  background: var(--color-white);
  user-select: none;
  overflow: hidden;
}
.qty-counter-lg { height: 3rem; min-width: 10rem; }
.qty-counter-sm { height: 2rem; min-width: 6.75rem; }
.qty-btn {
  width: 2.5rem;
  height: 100%;
  border: none;
  background: var(--color-paper);  /* always filled — not just on hover */
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: background 0.1s, color 0.1s;
}
.qty-counter-lg .qty-btn { width: 3rem; }
.qty-counter-sm .qty-btn { width: 2rem; }
/* − button */
.qty-btn:first-child { border-radius: var(--radius) 0 0 var(--radius); color: var(--color-graphite-900); }
/* + button */
.qty-btn:last-child { border-radius: 0 var(--radius) var(--radius) 0; color: var(--color-teal); }
/* Click / active — primary teal flash */
.qty-btn:active {
  background: var(--color-teal);
  color: var(--color-white);
}
.qty-btn:disabled { color: #BFBFC2; cursor: default; }
.qty-btn:disabled:active { background: var(--color-paper); color: #BFBFC2; }
.qty-value {
  flex: 1;
  text-align: center;
  font-family: var(--font-family);
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-graphite-900);
  /* no border — dividers removed */
}
.qty-counter-lg .qty-value { font-size: 1.125rem; }
.qty-counter-sm .qty-value { font-size: 0.875rem; }
/* Disabled whole counter */
.qty-counter[aria-disabled="true"] {
  opacity: 0.45;
  pointer-events: none;
}
```

## Alerts

### Variants
Four semantic variants using Metzler tokens. Each has a contextual icon and matching text color. Use role="alert" for accessibility.

```html
<div class="alert alert-success" role="alert">
  <!-- success icon -->
  Your changes have been saved successfully.
</div>
<div class="alert alert-danger" role="alert">
  <!-- danger icon -->
  Something went wrong. Please review the errors below and try again.
</div>
<div class="alert alert-warning" role="alert">
  <!-- warning icon -->
  Your session will expire in 5 minutes. Save your work to avoid losing changes.
</div>
<div class="alert alert-info" role="alert">
  <!-- info icon -->
  A new version of the product catalog is available. Prices have been updated.
</div>
```

### Without icon
The same four semantic variants, text-only — no contextual icon. Use when space is tight or the colour and copy already carry the meaning. Add .alert-no-icon to drop the icon.

```html
<div class="alert alert-success alert-no-icon" role="alert">
  Your changes have been saved successfully.
</div>
<div class="alert alert-danger alert-no-icon" role="alert">
  Something went wrong. Please review the errors below and try again.
</div>
<div class="alert alert-warning alert-no-icon" role="alert">
  Your session will expire in 5 minutes. Save your work to avoid losing changes.
</div>
<div class="alert alert-info alert-no-icon" role="alert">
  A new version of the product catalog is available. Prices have been updated.
</div>
```

### With link
Use .alert-link on any <a> inside an alert to get a matching underlined link color.

```html
<div class="alert alert-success" role="alert">
  File uploaded. <a href="#" class="alert-link">View in your documents</a>.
</div>
<div class="alert alert-danger" role="alert">
  Payment failed. <a href="#" class="alert-link">Update your billing details</a>.
</div>
<div class="alert alert-info" role="alert">
  New prices apply from 01.06.2026. <a href="#" class="alert-link">See what changed</a>.
</div>
```

### With heading
Add .alert-heading for a bold title inside the alert, and a <hr> divider for additional body text.

Your order #MZ-2026-4812 has been placed and will be shipped within 2 business days.

You will receive a confirmation email at the address on file.

```html
<div class="alert alert-success" role="alert">
  <h4 class="alert-heading">Order confirmed!</h4>
  <p>Your order #MZ-2026-4812 has been placed and will be shipped within 2 business days.</p>
  <hr class="alert-divider">
  <p>You will receive a confirmation email at the address on file.</p>
</div>
```

### Dismissible
Add .alert-dismissible and an × close button. Clicking removes the alert from the DOM.

```html
<div class="alert alert-success alert-dismissible" role="alert">
  <!-- icon --> Your changes have been saved successfully.
  <button class="alert-close" aria-label="Close">×</button>
</div>
```

### CSS definitions

```html
.alert {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  border-radius: var(--radius);
  border: 0.0625rem solid transparent;
  border-left-width: 0.25rem;
  padding: 0.875rem 1rem;
  font-family: var(--font-family);
  font-size: 0.9375rem;
  line-height: 1.6;
  position: relative;
}
/* Variants */
.alert-success {
  background: #F0FDF4;
  border-color: var(--color-green);
  color: #14532D;
}
.alert-danger {
  background: #FFF1F1;
  border-color: #C90000;
  color: #4A0000;
}
.alert-warning {
  background: #FFFBEB;
  border-color: #F59E0B;
  color: #78350F;
}
.alert-info {
  background: var(--color-teal-100);
  border-color: var(--color-teal);
  color: #012F30;
}
/* Heading inside alert */
.alert-heading {
  font-size: 1rem;
  font-weight: 700;
  margin: 0 0 0.5rem;
}
/* Link inside alert */
.alert-link {
  font-weight: 600;
  text-decoration: underline;
}
.alert-success .alert-link { color: #15803D; }
.alert-danger  .alert-link { color: #B52320; }
.alert-warning .alert-link { color: #D97706; }
.alert-info    .alert-link { color: var(--color-teal-600); }
/* Divider inside alert */
.alert-divider {
  border: none;
  border-top: 0.0625rem solid currentColor;
  opacity: 0.25;
  margin: 0.625rem 0;
}
/* Dismissible */
.alert-dismissible { padding-right: 2.5rem; }
.alert-close {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  background: none;
  border: none;
  cursor: pointer;
  opacity: 0.6;
  font-size: 1.125rem;
  line-height: 1;
  color: inherit;
}
.alert-close:hover { opacity: 1; }
```

## Tooltip

```html
/* Wrapper — must be position:relative */
.tooltip-wrapper { position: relative; display: inline-flex; }
/* Bubble */
.tooltip {
  position: absolute; z-index: 100;
  padding: 0.4rem 0.75rem;
  background: var(--color-teal); color: var(--color-white);
  border-radius: 0.375rem;
  font-size: 0.8125rem; line-height: 1.45; white-space: nowrap;
  box-shadow: 0 0.25rem 1rem rgba(0,0,0,0.15);
  pointer-events: none;
  opacity: 0; transition: opacity 0.15s, transform 0.15s;
}
.tooltip-wrapper:hover .tooltip { opacity: 1; transform: translate(-50%, 0); }
/* Position variants */
.tooltip-top { bottom: calc(100% + 0.5rem); left: 50%; transform: translateX(-50%) translateY(4px); }
.tooltip-bottom { top: calc(100% + 0.5rem); left: 50%; transform: translateX(-50%) translateY(-4px); }
.tooltip-left { right: calc(100% + 0.5rem); top: 50%; transform: translateY(-50%) translateX(4px); }
.tooltip-right { left: calc(100% + 0.5rem); top: 50%; transform: translateY(-50%) translateX(-4px); }
/* Light variant */
.tooltip-light {
  background: var(--color-white); color: var(--color-black);
  border: 0.0625rem solid var(--color-graphite-300);
}
/* Multiline — allow text to wrap */
.tooltip-multiline {
  white-space: normal;
  max-width: 14rem;  /* ~224px — adjust as needed */
  width: max-content;
  padding: 0.5rem 0.875rem;
  line-height: 1.5;
}
```

## Badge

```html
<!-- Product Type Badge -->
<span class="badge badge--primary">Primary</span>
<span class="badge badge--success">Success</span>
<span class="badge badge--warning">Warning</span>
<span class="badge badge--danger">-15%</span>
<span class="badge badge--neutral">Neutral</span>
<span class="badge badge--outlined">Outlined</span>
<!-- Discount Label -->
<div class="discount-label">
  <div class="discount-label__value">10 %</div>
  <div class="discount-label__tag">Rabatt</div>
</div>
```

```html
.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.3125rem 0.75rem;  /* 5px 12px */
  border-radius: 0.125rem;  /* --radius-sm */
  font-size: 0.75rem;
  font-weight: 500;
  line-height: 1;
}
.badge--primary { background: var(--color-teal); color: var(--color-white); }
.badge--success { background: var(--color-green); color: var(--color-white); }
.badge--warning { background: #E67E00; color: var(--color-white); }
.badge--danger { background: var(--color-metzler-rot); color: var(--color-white); }
.badge--neutral { background: var(--color-graphite-100); color: var(--color-graphite-700); }
.badge--outlined { background: var(--color-white); color: var(--color-teal);
                   border: 0.0625rem solid var(--color-teal); }
/* Discount Label */
.discount-label {
  width: 4.125rem;  /* 66px */
  border: 0.125rem solid var(--color-metzler-rot);
  border-radius: 0.375rem;
  background: var(--color-white);
  overflow: hidden;
}
.discount-label__value {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.375rem 0.375rem 0.25rem;
  font-size: 1.625rem;  /* 26px */
  font-weight: 700;
  color: var(--color-black);
  line-height: 1;
  letter-spacing: -0.125rem;
}
.discount-label__tag {
  background: var(--color-metzler-rot);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.3125rem 0.375rem 0.375rem;
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--color-white);
  line-height: 1;
}
```

## Tabs

```html
<div class="tabs">
  <div class="tabs__bar">
    <button class="tabs__tab tabs__tab--active">Overview</button>
    <button class="tabs__tab">Specifications</button>
    <button class="tabs__tab">Reviews</button>
    <button class="tabs__tab tabs__tab--disabled" disabled>Installation</button>
  </div>
  <div class="tabs__panel">
    <!-- active tab content goes here -->
  </div>
</div>
```

```html
.tabs__bar {
  display: flex;
  border-bottom: 0.125rem solid var(--color-graphite-200);
}
.tabs__tab {
  padding: 0.625rem 1.5rem;
  background: none;
  border: none;
  border-bottom: 0.1875rem solid transparent;
  margin-bottom: -0.125rem;
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-graphite-600);
  cursor: pointer;
  transition: color 0.15s, border-color 0.15s;
}
.tabs__tab:hover {
  color: var(--color-teal);
  border-bottom-color: rgba(1, 82, 83, 0.25);
}
.tabs__tab--active {
  color: var(--color-teal);
  border-bottom-color: var(--color-teal);
}
.tabs__tab--disabled {
  color: var(--color-graphite-450);
  cursor: not-allowed;
}
.tabs__panel {
  padding: 1.25rem 0;
  font-size: 1rem;
  color: var(--color-graphite-700);
  line-height: 1.7;
}
```

## Stepper

```html
<nav class="pdp-stepper" aria-label="Konfigurationsschritte">
  <div class="pdp-stepper-inner">
    <button class="pdp-stepper-step completed" data-step="1">
      <span class="pdp-stepper-num">1.</span>
      <span class="pdp-stepper-label">Anschluss</span>
    </button>
    <span class="pdp-stepper-sep" aria-hidden="true">
      <svg viewBox="0 0 8 16" fill="none" stroke="currentColor"
           stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="1 1 7 8 1 15"/>
      </svg>
    </span>
    <button class="pdp-stepper-step active" data-step="2" aria-current="step">
      <span class="pdp-stepper-num">2.</span>
      <span class="pdp-stepper-label">Modul</span>
    </button>
    <!-- repeat <span.pdp-stepper-sep> + <button.pdp-stepper-step> for each additional step -->
  </div>
</nav>
```

```html
.pdp-stepper {
  width: 100%;
}
.pdp-stepper-inner {
  display: flex;
  align-items: stretch;
  background: var(--color-teal);  /* Teal 500 — #015253 */
  border-radius: 0.5rem;
  overflow: hidden;
  height: 3.5rem;
}
.pdp-stepper-step {
  flex: 1 1 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.375rem;
  padding: 0 1.25rem;
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.55);
  font-size: 1rem;
  cursor: pointer;
  transition: color 0.15s, background 0.2s;
  z-index: 1;
}
.pdp-stepper-step.active {
  background: var(--color-teal-dark);  /* Teal 700 — #01292A */
  color: #fff;
  clip-path: polygon(
    0 0,
    calc(100% - 0.75rem) 0,
    100% 50%,
    calc(100% - 0.75rem) 100%,
    0 100%
  );
  padding-right: calc(1.25rem + 0.75rem);
  z-index: 2;
}
.pdp-stepper-step.completed {
  color: rgba(255, 255, 255, 0.85);
}
.pdp-stepper-num { font-weight: 700; }
.pdp-stepper-label { font-weight: 400; }
/* Hide label on inactive steps — show only the number */
.pdp-stepper-step:not(.active) .pdp-stepper-label {
  display: none;
}
.pdp-stepper-sep {
  display: flex;
  align-items: center;
  flex-shrink: 0;
  color: rgba(255, 255, 255, 0.3);
}
.pdp-stepper-sep svg {
  width: 0.5rem;
  height: 1rem;
}
```

## Lists

#### Unordered
Teal dash marker. Nested lists use a smaller teal circle.

- Lorem ipsum dolor sit amet
- Consectetur adipiscing elit
- Integer molestie lorem at massa
- Facilisis in pretium nisl aliquet
- Nulla volutpat aliquam velit
- Phasellus iaculis neque Purus sodales ultricies Vestibulum laoreet porttitor sem
- Faucibus porta lacus fringilla vel
- Eget porttitor lorem

```html
<ul class="list-metzler">
  <li>Lorem ipsum dolor sit amet</li>
  <li>Nulla volutpat aliquam velit
    <ul>
      <li>Phasellus iaculis neque</li>
      <li>Purus sodales ultricies</li>
    </ul>
  </li>
  <li>Eget porttitor lorem</li>
</ul>
```

#### Ordered
Two-digit teal counter. Clear hierarchy for step-by-step content.

- 01 Lorem ipsum dolor sit amet
- 02 Consectetur adipiscing elit
- 03 Integer molestie lorem at massa
- 04 Facilisis in pretium nisl aliquet
- 05 Nulla volutpat aliquam velit

```html
<ol class="list-metzler-ordered">
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
  <li>Integer molestie lorem at massa</li>
</ol>
```

#### Checklist
Use for feature lists, benefit summaries, and comparison tables.

- Lorem ipsum dolor sit amet
- Consectetur adipiscing elit
- Integer molestie lorem at massa
- Facilisis in pretium nisl aliquet
- Nulla volutpat aliquam velit

```html
<ul class="list-metzler-check">
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
</ul>
```

#### Unstyled · .list-unstyled
Removes all markers and left padding. Add the class to nested lists too.

- Lorem ipsum dolor sit amet
- Consectetur adipiscing elit
- Integer molestie lorem at massa
- Facilisis in pretium nisl aliquet
- Nulla volutpat aliquam velit

```html
<ul class="list-unstyled">
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
</ul>
```

#### CSS definitions

```html
/* Unordered — teal dash */
.list-metzler { list-style: none; padding: 0; margin: 0; }
.list-metzler > li {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.3rem 0; font-size: 1rem; line-height: 1.5;
}
.list-metzler > li::before {
  content: ''; flex-shrink: 0;
  width: 0.375rem; height: 0.125rem;
  background: var(--color-teal); border-radius: var(--radius-sm); margin-top: 0.6rem;
}
/* Nested */
.list-metzler ul { list-style: none; padding: 0 0 0 1.25rem; margin: 0.25rem 0; }
.list-metzler ul li { display: flex; align-items: center; gap: 0.75rem; padding: 0.25rem 0; font-size: 0.9375rem; color: #54545C; }
.list-metzler ul li::before {
  content: ''; flex-shrink: 0;
  width: 0.25rem; height: 0.25rem; border-radius: 50%;
  border: 0.09375rem solid var(--color-teal); margin-top: 0.45rem;
}
/* Ordered — two-digit teal counter */
.list-metzler-ordered { list-style: none; padding: 0; margin: 0; counter-reset: metz; }
.list-metzler-ordered > li {
  display: flex; align-items: center; gap: 0.875rem;
  padding: 0.3rem 0; font-size: 1rem; line-height: 1.5;
  counter-increment: metz;
}
.list-metzler-ordered > li::before {
  content: counter(metz, decimal-leading-zero);
  flex-shrink: 0; min-width: 1.5rem;
  font-family: monospace; font-size: 0.8125rem; font-weight: 700; color: var(--color-teal);
}
/* Checklist — teal circle tick */
.list-metzler-check { list-style: none; padding: 0; margin: 0; }
.list-metzler-check > li {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.35rem 0; font-size: 1rem; line-height: 1.5;
}
.list-metzler-check > li::before {
  content: '';  flex-shrink: 0;
  width: 1.125rem; height: 1.125rem; border-radius: 50%;
  background: rgba(1,82,83,0.1);
  /* Use an SVG tick via mask-image in real implementation */
}
/* Unstyled */
.list-unstyled { list-style: none; padding: 0; margin: 0; }
.list-unstyled > li { padding: 0.3rem 0; }
```

## Table

#### Default
Outer border, column dividers, hairline row dividers. Header uses the same text style as body, bold weight.

| Merkmal | Modell A | Modell B | Modell C |
| --- | --- | --- | --- |
| Bildschirm | 17,78 cm | 17,78 cm | 25,70 cm |
| Abmessung | 200 × 140 × 25,1 mm | 180 × 140 × 22,4 mm | 254 × 166 × 24,7 mm |
| Display | LCD Touchscreen | IPS LED Touchscreen | LCD Touchscreen |
| Auflösung | 1024 × 600 PX | 1024 × 600 PX | 1024 × 600 PX |
| Highlights | Günstiger Preis, Vollwertiges Endgerät | Aluminium in Luft- und Raumfahrtqualität, Sensortaste für Türöffnung, IPS LED Display | Sehr großes 10,1 Zoll LCD Display, extrem flache Bauart |

```html
<table class="table">
  <thead>
    <tr>
      <th>Merkmal</th>
      <th>Modell A</th>
      <th>Modell B</th>
      <th>Modell C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bildschirm</td>
      <td>17,78 cm</td>
      <td>17,78 cm</td>
      <td>25,70 cm</td>
    </tr>
    <!-- … -->
  </tbody>
</table>
```

#### Striped · .table-striped
Every other row gets a subtle #F5F6FA fill. Good for wide tables with many columns.

| Bildschirm | 17,78 cm | 17,78 cm | 25,70 cm |
| --- | --- | --- | --- |
| Abmessung | 200 × 140 × 25,1 mm | 180 × 140 × 22,4 mm | 254 × 166 × 24,7 mm |
| Display | LCD Touchscreen | IPS LED Touchscreen | LCD Touchscreen |
| Auflösung | 1024 × 600 PX | 1024 × 600 PX | 1024 × 600 PX |
| Highlights | Günstiger Preis, Vollwertiges Endgerät | Aluminium in Luft- und Raumfahrtqualität, Sensortaste für Türöffnung, IPS LED Display | Sehr großes 10,1 Zoll LCD Display, extrem flache Bauart |

#### CSS definitions

```html
.table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-family);
  font-size: 0.9375rem;
}
/* Header */
.table thead tr { border-bottom: 0.0625rem solid var(--color-graphite-200); }
.table th {
  padding: 0.75rem 1rem;
  height: 3rem;
  box-sizing: border-box;
  text-align: left;
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--color-black);
  white-space: nowrap;
  background: var(--color-graphite-100);
  border-right: 0.0625rem solid var(--color-graphite-200);
}
.table th:last-child { border-right: none; }
/* Rows */
.table td {
  padding: 0.75rem 1rem;
  height: 3rem;
  box-sizing: border-box;
  color: #54545C;
  font-weight: 400;
  line-height: 1.45;
  border-bottom: 0.0625rem solid var(--color-graphite-100);
  border-right: 0.0625rem solid var(--color-graphite-100);
}
.table td:last-child { border-right: none; }
.table tbody tr { transition: background 0.1s; }
.table tbody tr:hover { background: var(--color-paper); }
.table tbody tr:last-child td { border-bottom: none; }
/* Bordered wrapper (default variant) */
.table-bordered { border: 0.0625rem solid var(--color-graphite-200); border-radius: 0.5rem; overflow: hidden; }
/* Striped variant */
.table-striped tbody tr:nth-child(even) { background: var(--color-paper); }
.table-striped tbody tr:nth-child(even):hover { background: var(--color-teal-100); }
/* Sortable columns */
.table th[data-sortable] { cursor: pointer; user-select: none; }
.table th[data-sortable]:hover { color: var(--color-teal-600); }
/* Status badges inside cells */
.table-badge {
  display: inline-block;
  padding: 0.1875rem 0.625rem;
  border-radius: 1.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}
.table-badge--green { color: var(--color-green); background: rgba(0,153,81,0.08); }
.table-badge--amber { color: #B06000; background: rgba(176,96,0,0.08); }
.table-badge--red { color: #C90000; background: rgba(201,0,0,0.08); }
```

## Links
`.link-primary` `.link-muted` `.link-danger` `.link-dark` `.link-mint` `.link-white` 
```html
<a class="link-arrow" href="#">
  Mehr erfahren
  <svg width="14" height="12" viewBox="0 0 14 12" fill="none">
    <path d="M1 6h12M7 1l6 5-6 5" stroke="currentColor"
      stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</a>
```

```html
/* All link variants share the same base reset */
a {
  text-underline-offset: 0.2em;
  transition: color 0.15s, text-decoration-color 0.15s;
}
.link-primary { color: var(--color-teal); text-decoration: none; }
.link-primary:hover { color: var(--color-teal-600); text-decoration: underline; }
.link-primary:visited { color: var(--color-teal-700); }
.link-muted { color: #54545C; text-decoration: none; }
.link-muted:hover { color: var(--color-graphite-900); text-decoration: underline; }
.link-danger { color: #C90000; text-decoration: none; }
.link-danger:hover { color: #B52320; text-decoration: underline; }
.link-dark { color: var(--color-graphite-900); text-decoration: none; }
.link-dark:hover { color: var(--color-teal); text-decoration: underline; }
/* Use on dark / teal backgrounds only */
.link-mint { color: var(--color-mint); text-decoration: none; }
.link-mint:hover { color: var(--color-mint); text-decoration: underline; }
.link-white { color: #DADADA; text-decoration: none; }
.link-white:hover { color: #ffffff; text-decoration: underline; }
/* Arrow link — arrow slides right on hover */
.link-arrow {
  display: inline-flex; align-items: center; gap: 0.375rem;
  color: var(--color-teal); text-decoration: none;
}
.link-arrow:hover { text-decoration: underline; }
.link-arrow svg {
  flex-shrink: 0;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.link-arrow:hover svg { transform: translateX(4px); }
/* Underline CTA — bold text link with a persistent underline, fades on hover.
   Used for inline "… entdecken" calls-to-action (Story / craft sections). */
.link-underline {
  display: inline-block;
  font-size: 0.875rem; font-weight: 700;
  color: var(--color-teal); text-decoration: none;
  border-bottom: 1px solid currentColor; padding-bottom: 2px;
  transition: opacity 0.22s ease;
}
.link-underline:hover { opacity: 0.75; }
/* On dark / teal backgrounds */
.link-underline--mint { color: var(--color-mint); }
```

## File Download

```html
<div class="file-download">
  <!-- Teal icon block -->
  <div class="file-download__icon">
    <svg width="26" height="32" viewBox="0 0 26 32" fill="none">...</svg>
    <span>PDF</span>
  </div>
  <!-- Title + meta -->
  <div class="file-download__info">
    <div class="file-download__title">Schnellstartanleitung</div>
    <div class="file-download__meta">PDF · 1,2 MB · 03/2026</div>
  </div>
  <!-- Download button -->
  <div class="file-download__btn">
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
      <path d="M7 1v8M3.5 6.5L7 10l3.5-3.5"
        stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <line x1="2" y1="13" x2="12" y2="13"
        stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    </svg>
  </div>
</div>
```

```html
.file-download {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: var(--color-white);
  border: 0.0625rem solid var(--color-graphite-300);
  border-radius: 0.5rem;  /* --radius-lg */
  padding: 0.875rem 1rem;
  width: 26.25rem;
  cursor: pointer;
  transition: border-color 0.15s, box-shadow 0.15s;
}
.file-download:hover {
  border-color: var(--color-teal);
  box-shadow: 0 0.25rem 1rem rgba(1, 82, 83, 0.12);
}
.file-download__icon {
  flex-shrink: 0;
  width: 2.75rem;
  height: 3.25rem;
  border-radius: 0.375rem;
  background: var(--color-teal);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.125rem;
}
.file-download__icon span {
  font-size: 0.5rem;
  font-weight: 800;
  color: var(--color-white);
  line-height: 1;
}
.file-download__info { flex: 1; min-width: 0; }
.file-download__title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-black);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.file-download__meta {
  font-size: 0.8125rem;
  color: var(--color-graphite-500);
  margin-top: 0.1875rem;
}
.file-download__btn {
  flex-shrink: 0;
  width: 2.125rem;
  height: 2.125rem;
  border-radius: 50%;
  background: var(--color-paper);
  color: var(--color-teal);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, color 0.15s;
}
.file-download:hover .file-download__btn {
  background: var(--color-teal);
  color: var(--color-white);
}
```

## Modal

#### 4 Modal Sizes
Verwende immer die dem Inhalt entsprechende Größe. Kein Footerbereich mit Aktionsbuttons — Buttons gehören in den Body.

| Klasse | Breite | Verwendungszweck |
| --- | --- | --- |
| .modal-xl | 1100px | Produktdetail — 2-spaltig, Bild links, Info rechts |
| .modal-lg | 960px | Lieferinfo / Bewertung (Foto) / Kontakt (Split-Panel) |
| .modal-md | 600px | Cookie-Banner, Bestätigungen — Buttons im Body |
| .modal-sm | 400px | Login, kleine Formulare — CTA-Button im Body |

#### XL · 1100px — Produktdetail
Zweispaltig: Bildbereich links (~45%), Produktinfo rechts (~55%). Header mit Titel und X. Kein Footer.

##### Metzler Intercom Innenstation Ultra, 10 Zoll Touchscreen, LAN PoE, schwarz

| Hersteller: Metzler | Breite × Höhe × Tiefe: 25,40 × 16,60 × 2,47 cm | Artikelnummer: 29407 |
| --- | --- | --- |
Metzler Innenstation für Intercom mit Touchscreen Display und Standard POE-Netzwerkanschluss. Ideal für die Integration in moderne Smart-Home-Systeme.

```html
<div class="modal-overlay" role="dialog" aria-modal="true">
  <div class="modal-dialog modal-xl">
    <div class="modal-header">
      <span class="modal-title">Produktdetails</span>
      <button class="modal-close" aria-label="Schließen">✕</button>
    </div>
    <div class="modal-body modal-body--product">
      <div class="modal-media">
        <!-- Produktbild / Karussell -->
      </div>
      <div class="modal-info">
        <h4 class="product-title">Metzler Intercom Innenstation Home …</h4>
        <div class="product-rating">★★★★★ 5,0 (32)</div>
        <div class="product-meta">Hersteller: Metzler · Artikelnummer: 29384</div>
        <div class="product-price">199,00 €</div>
        <p>Kurzbeschreibung …</p>
      </div>
    </div>
  </div>
</div>
```

#### LG · 960px — 3 Varianten
Großer Inhalt, Bewertungsfotos und Kontakt-Split-Panel nutzen alle dieselbe Breite. Header oder Overlay-X je nach Variante.

A — Kundenfoto & Bewertung (Split-Panel, Bildergalerie)

##### Schicke Video-Türsprechanlage
Philip W. | 2026-04-05

Wir sind insgesamt sehr zufrieden mit dieser schicken und zuverlässigen Video-Türsprechanlage. Diese fügt sich optisch gut ins Gesamtbild und die Bedienung ist sehr einfach.

```html
<div class="modal-overlay">
  <div class="modal-dialog modal-lg modal-split">
    <div class="modal-gallery">
      <img class="modal-photo" src="…" alt="Kundenfoto"/>
      <button class="nav-arr nav-prev" aria-label="Zurück">‹</button>
      <button class="nav-arr nav-next" aria-label="Weiter">›</button>
      <div class="modal-thumbs"> … </div>
    </div>
    <div class="modal-review">
      <button class="modal-close" aria-label="Schließen">✕</button>
      <h4>Schicke Video-Türsprechanlage <span class="stars">★★★★★</span></h4>
      <p class="review-meta">Philip W. | 2026-04-05</p>
      <p>Wir sind insgesamt sehr zufrieden …</p>
    </div>
  </div>
</div>
```
D — Experten-Kontakt & Service (Split-Panel, product page)

#### Sprechen Sie mit einem Experten.
Persönliche Beratung, technischer Support und geprüfte Partnerbetriebe — alles an einem Ort.

#### Wie können wir Ihnen helfen?
Wählen Sie Ihr Anliegen — wir helfen Ihnen gerne weiter.

```html
<div class="modal-overlay">
  <div class="modal-dialog modal-lg" style="display:flex;flex-direction:row;">
    <!-- Left hero panel -->
    <div class="modal-panel-hero">
      <h3>Sprechen Sie mit einem <em>Experten.</em></h3>
      <p>Persönliche Beratung, technischer Support …</p>
      <hr class="panel-rule" />
      <div class="panel-contact">
        <span class="label">Hotline</span>
        <a href="tel:+4971213177333">+49 (0) 7121 · 317 7333</a>
        <span>Mo–Fr · 09:00–16:00 Uhr</span>
        <a href="mailto:service@metzlergmbh.de">service@metzlergmbh.de</a>
      </div>
    </div>
    <!-- Right action panel — X button overlaid -->
    <div class="modal-panel-action">
      <button class="modal-close modal-close--overlay" aria-label="Schließen">✕</button>
      <div class="eyebrow">Kontakt &amp; Service</div>
      <h4>Wie können wir Ihnen helfen?</h4>
      <p>Wählen Sie Ihr Anliegen — wir helfen Ihnen gerne weiter.</p>
      <div class="service-cards">
        <a class="service-card service-card--active" href="#">
          <span class="service-card__ico"><!-- chat SVG --></span>
          <div><strong>Produktberatung &amp; Bestellung</strong><p>Beratung vor dem Kauf · Antwort meist in 5 Min.</p></div>
          <svg class="chevron">…</svg>
        </a>
        <!-- repeat for Technischer Support, Partnerbetrieb, Dokumentation -->
      </div>
    </div>
  </div>
</div>
```
E — Zahlung & Versand (Standard Header, scrollbarer Body)

Zahlung per Rechnung ist ausschließlich für Behörden und öffentliche Institutionen möglich. Der Rechnungsbetrag ist innerhalb von 14 Tagen auszugleichen.

| Versandland | Versandart | Preis |
| --- | --- | --- |
| Deutschland + Österreich | DHL / DPD | Gratis ab 99,00 €, sonst 4,95 € |
| Europa | DHL / DPD | 9,90 € |
| Schweiz + Großbritannien | DHL / DPD | 19,90 € |

| Deutschland | 1–3 Werktage |
| --- | --- |
| Österreich | 2–4 Werktage |
| Europa / Schweiz / Großbritannien | 3–5 Werktage |
Soweit im Angebot keine andere Frist angegeben ist, erfolgt die Lieferung innerhalb Deutschlands in 1–3 Werktagen nach Vertragsschluss. An Sonn- und Feiertagen erfolgt keine Zustellung. Bei Bestellungen mit unterschiedlichen Lieferzeiten gilt die längste Lieferzeit.

Die Lieferung erfolgt im Inland (Deutschland) und in folgende Länder: Belgien, Bulgarien, Dänemark, Estland, Finnland, Frankreich, Griechenland, Großbritannien, Irland, Italien, Kroatien, Lettland, Litauen, Luxemburg, Malta, Niederlande, Österreich, Polen, Portugal, Rumänien, Schweden, Schweiz, Slowakei, Slowenien, Spanien, Tschechien, Ungarn, Zypern.

```html
<div class="modal-overlay">
  <div class="modal-dialog modal-lg">
    <div class="modal-header">
      <span class="modal-title">Zahlung und Versand</span>
      <button class="modal-close" aria-label="Schließen">✕</button>
    </div>
    <div class="modal-body">
      <h5>Akzeptierte Zahlungsmöglichkeiten</h5>
      <div class="payment-badges"><!-- PayPal, Amazon Pay, Klarna … --></div>
      <h5>Versandkosten</h5>
      <table class="modal-specs-table">…</table>
      <h5>Lieferfristen</h5>
      <table class="modal-specs-table">…</table>
    </div>
  </div>
</div>
```

#### MD · 600px — Cookie-Banner / Bestätigung
Standard Header-Balken — Titel links, X rechts, Trennlinie darunter. Aktionsbuttons gestapelt innerhalb des Body.

Durch Klicken auf „Alle akzeptieren" gestatten Sie den Einsatz folgender Dienste auf unserer Website: YouTube, Vimeo, ReCaptcha, Hotjar Tracking, AWIN, Pinterest, PayPal Express Checkout und Ratenzahlung, Analytics via Google Tag Manager, Microsoft Bing Ads, Google Ads. Unsere Partner erheben Daten und verwenden Cookies, um personalisierte Werbung bereitzustellen und zu Analysezwecken. Sie können die Einstellung jederzeit über den Link Cookie-Einstellungen im Footer ändern. Weitere Details finden Sie unter Konfigurieren und in unserer Datenschutzerklärung | Impressum.

```html
<div class="modal-overlay">
  <div class="modal-dialog modal-md">
    <!-- Standard header — same as all modals -->
    <div class="modal-header">
      <span class="modal-title">Wie wir Cookies &amp; Co nutzen</span>
      <button class="modal-close" aria-label="Schließen">✕</button>
    </div>
    <div class="modal-body">
      <p>Durch Klicken auf „Alle akzeptieren" …</p>
      <!-- Buttons are INSIDE the body — not a footer zone -->
      <button class="btn btn-primary btn-block">Alle akzeptieren</button>
      <div class="modal-btn-row">
        <button class="btn btn-ghost">Ablehnen</button>
        <button class="btn btn-ghost">Konfigurieren</button>
      </div>
    </div>
  </div>
</div>
```

#### SM · 400px — Login / kleine Formulare
Schmalster Dialog — Standard Header-Balken, Titel links, X rechts, Trennlinie darunter. Kompaktes Formular mit vollbreitem CTA-Button im Body, kein Footer.

Melden Sie sich an, um Ihre Bestellungen und Ihren Account zu verwalten.

Neu hier? Jetzt registrieren!

```html
<div class="modal-overlay">
  <div class="modal-dialog modal-sm">
    <div class="modal-header">
      <span class="modal-title">Anmelden</span>
      <button class="modal-close" aria-label="Schließen">✕</button>
    </div>
    <div class="modal-body">
      <p>Melden Sie sich an, um Ihre Bestellungen …</p>
      <div class="field-wrapper"><input type="email" placeholder=" "/><label>E-Mail</label></div>
      <div class="field-wrapper"><input type="password" placeholder=" "/><label>Passwort</label></div>
      <a class="link-right" href="#">Passwort vergessen?</a>
      <button class="btn btn-primary btn-block">Anmelden</button>
      <p>Neu hier? <a href="#">Jetzt registrieren!</a></p>
    </div>
  </div>
</div>
```

#### CSS-Definitionen

```html
/* Overlay */
.modal-overlay {
  position: fixed; inset: 0; z-index: 9999;
  background: rgba(0, 0, 0, 0.45);
  display: flex; align-items: center; justify-content: center;
  padding: 1rem;
}
/* Dialog base */
.modal-dialog {
  width: 100%; max-width: 37.5rem;  /* 600px — MD default */
  background: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: 0 1.25rem 3.75rem rgba(0,0,0,0.2), 0 0.25rem 1rem rgba(0,0,0,0.1);
  display: flex; flex-direction: column;
  max-height: 90vh; overflow: hidden;
  position: relative;
}
/* Size modifiers */
.modal-dialog.modal-xl { max-width: 68.75rem; } /* 1100px — Product detail */
.modal-dialog.modal-lg { max-width: 60rem;    } /* 960px  — Rich content, split, review */
.modal-dialog.modal-sm { max-width: 25rem;    } /* 400px  — Login, small forms */
/* Header — always title left, X right */
.modal-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 1.25rem 1.5rem;
  border-bottom: 0.0625rem solid var(--color-graphite-200);
  flex-shrink: 0;
}
.modal-title {
  font-family: var(--font-family);
  font-size: 1.5rem; font-weight: 700; line-height: 1.3; letter-spacing: -0.015em; color: var(--color-digital-black);
}
/* Close button — same style in all modals */
.modal-close {
  display: flex; align-items: center; justify-content: center;
  width: 2rem; height: 2rem;
  border: none; border-radius: var(--radius);
  background: transparent; cursor: pointer; color: var(--color-graphite-700);
  transition: background 0.15s; flex-shrink: 0;
}
.modal-close:hover { background: var(--color-graphite-100); }
/* Overlay close (no-header variants: photo/review) */
.modal-close--overlay {
  position: absolute; top: 1rem; right: 1rem; z-index: 2;
  background: var(--color-white);
  box-shadow: 0 0.125rem 0.5rem rgba(0,0,0,0.15);
  border-radius: 50%;
}
.modal-close--overlay:hover { background: var(--color-graphite-100); }
/* Body */
.modal-body {
  padding: 1.5rem; overflow-y: auto; flex-grow: 1;
  font-family: var(--font-family);
  font-size: 1rem; color: var(--color-graphite-700); line-height: 1.6;
}
/* XL: 2-column product layout */
.modal-xl .modal-body--product {
  display: flex; padding: 0; overflow: hidden;
}
.modal-xl .modal-body--product .modal-media {
  flex: 0 0 45%; background: var(--color-graphite-100);
}
.modal-xl .modal-body--product .modal-info {
  flex: 1; padding: 2rem; overflow-y: auto;
}
/* LG photo/review: no-header, full-height left image */
.modal-lg .modal-body--review {
  display: flex; padding: 0; overflow: hidden; flex-grow: 1;
}
.modal-lg .modal-body--review .modal-photo {
  flex: 0 0 50%; object-fit: cover;
}
.modal-lg .modal-body--review .modal-review-content {
  flex: 1; padding: 2rem; overflow-y: auto;
}
/* LG split panel */
.modal-lg .modal-body--split {
  display: flex; padding: 0; flex-grow: 1;
}
.modal-body--split .modal-panel-left {
  flex: 0 0 40%; background: var(--color-teal);
  padding: 2rem; display: flex; flex-direction: column; gap: 1.5rem;
}
.modal-body--split .modal-panel-right {
  flex: 1; padding: 1.5rem; overflow-y: auto;
}
```

#### Live-Demos
Öffne einen echten Modal in jeder Größe direkt im Browser.

#### Mobile Popups
Alle Popups in ihrer mobilen Darstellung. Die Live-Popups reagieren automatisch auf die tatsächliche Viewport-Breite — bei Desktop-Ansicht entspricht die mobile Darstellung dem zentrsierten Stil.

Durch Klicken auf „Alle akzeptieren" gestatten Sie den Einsatz folgender Dienste auf unserer Website: YouTube, Vimeo, ReCaptcha, Hotjar Tracking, AWIN, Pinterest, PayPal Express Checkout und Ratenzahlung, Analytics via Google Tag Manager, Microsoft Bing Ads, Google Ads. Unsere Partner erheben Daten und verwenden Cookies, um personalisierte Werbung bereitzustellen und zu Analysezwecken. Sie können die Einstellung jederzeit über den Link Cookie-Einstellungen im Footer ändern. Weitere Details finden Sie unter Konfigurieren und in unserer Datenschutzerklärung | Impressum.

Einstellungen, die Sie hier vornehmen, werden auf Ihrem Endgerät im „Local Storage" gespeichert und sind beim nächsten Besuch unseres Onlineshops wieder aktiv. Sie können diese Einstellungen jederzeit ändern (Fingerabdruck-Icon links unten).

Informationen zur Cookie-Funktionsdauer sowie Details zu technisch notwendigen Cookies erhalten Sie in unserer Datenschutzerklärung.

Melden Sie sich an, um Ihre Bestellungen und Ihren Account zu verwalten.

Neu hier? Jetzt registrieren!

Zahlung per Rechnung ist ausschließlich für Behörden und öffentliche Institutionen möglich. Der Rechnungsbetrag ist innerhalb von 14 Tagen auszugleichen.

| Versandland | Versandart | Preis |
| --- | --- | --- |
| Deutschland + Österreich | DHL / DPD | Gratis ab 99,00 €, sonst 4,95 € |
| Europa | DHL / DPD | 9,90 € |
| Schweiz + Großbritannien | DHL / DPD | 19,90 € |

| Deutschland | 1–3 Werktage |
| --- | --- |
| Österreich | 2–4 Werktage |
| Europa / Schweiz / Großbritannien | 3–5 Werktage |
Soweit im Angebot keine andere Frist angegeben ist, erfolgt die Lieferung innerhalb Deutschlands in 1–3 Werktagen nach Vertragsschluss. An Sonn- und Feiertagen erfolgt keine Zustellung. Bei Bestellungen mit unterschiedlichen Lieferzeiten gilt die längste Lieferzeit.

Die Lieferung erfolgt im Inland (Deutschland) und in folgende Länder: Belgien, Bulgarien, Dänemark, Estland, Finnland, Frankreich, Griechenland, Großbritannien, Irland, Italien, Kroatien, Lettland, Litauen, Luxemburg, Malta, Niederlande, Österreich, Polen, Portugal, Rumänien, Schweden, Schweiz, Slowakei, Slowenien, Spanien, Tschechien, Ungarn, Zypern.

##### Schicke Video-Türsprechanlage
Philip W. | 2026-04-05

Wir sind insgesamt sehr zufrieden mit dieser schicken und zuverlässigen Video-Türsprechanlage. Diese fügt sich optisch gut ins Gesamtbild und die Bedienung ist sehr einfach.

##### Wie können wir Ihnen helfen?
Wählen Sie Ihr Anliegen — wir helfen Ihnen gerne weiter.

## Breadcrumbs
Hierarchical navigation trail. Active (current) page in black, parent links in gray #6A6A6A — green #015253 with underline on hover. Separator is a #A1A1A1 chevron. Two sizes: sm (12px · used on mobile), md (14px · default).

SIZE · SM — 12PX (MOBILE)

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb breadcrumb-sm">
    <li class="breadcrumb-item active" aria-current="page">Home</li>
  </ol>
</nav>
<nav aria-label="breadcrumb">
  <ol class="breadcrumb breadcrumb-sm">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Briefkästen</li>
  </ol>
</nav>
<nav aria-label="breadcrumb">
  <ol class="breadcrumb breadcrumb-sm">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item"><a href="#">Briefkästen</a></li>
    <li class="breadcrumb-item"><a href="#">Edelstahl Briefkästen</a></li>
    <li class="breadcrumb-item active" aria-current="page">Metzler Briefkasten Typ 200</li>
  </ol>
</nav>
```
SIZE · MD — 14PX (DEFAULT)

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item active" aria-current="page">Home</li>
  </ol>
</nav>
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Briefkästen</li>
  </ol>
</nav>
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item"><a href="#">Briefkästen</a></li>
    <li class="breadcrumb-item"><a href="#">Edelstahl Briefkästen</a></li>
    <li class="breadcrumb-item active" aria-current="page">Metzler Briefkasten Typ 200</li>
  </ol>
</nav>
```

### CSS definitions

```html
.breadcrumb {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.625rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.breadcrumb-item a {
  font-family: var(--font-family);
  font-size: 0.875rem;
  color: var(--color-graphite-600);
  text-decoration: none;
  cursor: pointer;
  transition: color 0.15s;
}
.breadcrumb-item a:hover {
  color: var(--color-teal);
  text-decoration: underline;
}
.breadcrumb-item.active {
  font-family: var(--font-family);
  font-size: 0.875rem;
  color: var(--color-black);
  text-decoration: none;
}
/* Size variants */
.breadcrumb-sm .breadcrumb-item a,
.breadcrumb-sm .breadcrumb-item.active { font-size: 0.75rem; }
/* Chevron separator between items */
.breadcrumb-item + .breadcrumb-item {
  display: flex;
  align-items: center;
  gap: 0.625rem;
}
.breadcrumb-item + .breadcrumb-item::before {
  content: '';
  display: inline-block;
  width: 0.375rem;
  height: 0.625rem;
  background: url("data:image/svg+xml,%3Csvg width='6' height='10' viewBox='0 0 6 10' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1l4 4-4 4' stroke='%23A1A1A1' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") no-repeat center;
}
```

## Product Cards

### Product Card
Catalog page card. Contains: product image with badge overlay, brand + star rating, title (clamped), price with sale tag, and color swatches.

DESKTOP — 340PX · HOVER SHADOW + IMAGE SWAP · FEATURE-PILLS

Width 340px, border-radius 8px (token l), padding 20px, border 1px solid #DADADA. Title underlines and image swaps on hover; box-shadow elevates to 0 4px 20px rgba(0,0,0,0.12). Feature-Pills (.pcard__sys / .pcard__feat): Graphite-100-Fill, Inset-Hairline, Pill-Radius, 12px / 500 — einzeilig scrollend mit Rand-Fade.

```html
.pcard__tags {
  display: flex; align-items: center; flex-wrap: nowrap;
  gap: 0.5rem; overflow-x: auto; scrollbar-width: none;
}
.pcard__tags::-webkit-scrollbar { display: none; }
/* Rand-Fade: genau EINE Seite gleichzeitig */
.pcard__tags.is-scroll {          /* mehr Pills rechts → rechts faden */
  mask-image: linear-gradient(90deg, #000 0, #000 calc(100% - 26px), transparent 100%);
}
.pcard__tags.is-scroll.at-end {   /* am Ende → links faden */
  mask-image: linear-gradient(90deg, transparent 0, #000 26px, #000 100%);
}
/* System-/Feature-Pill — Text-only */
.pcard__sys, .pcard__feat {
  flex: 0 0 auto; align-self: center;
  padding: 0.3rem 0.8rem;
  border-radius: 999px;
  background: var(--color-graphite-100);
  box-shadow: inset 0 0 0 1px rgba(0,0,0,0.08);
  color: var(--color-digital-black);
  font-size: 0.75rem;  /* 12px */
  font-weight: 500;
  letter-spacing: 0.02em;
  white-space: nowrap;
}
```

```html
<div class="product-card">
  <div class="product-card__image">
    <img src="product.jpg" alt="Product name" />
    <span class="product-card__badge">IP-System</span>
    <span class="product-card__discount-badge">-15%</span>
  </div>
  <div style="display:flex; align-items:center; justify-content:space-between;">
    <span class="product-card__brand">Metzler</span>
    <div class="product-card__stars"><!-- star icons --></div>
    <span class="product-card__review-count">(300)</span>
  </div>
  <div class="product-card__title">
    Video-Türsprechanlage mit Paketbox | Anthrazit RAL 7016 …
  </div>
  <div style="display:flex; align-items:center; gap:0.25rem;">
    <span class="product-card__price-from">ab</span>
    <span class="product-card__price">49,99 €</span>
    <span class="product-card__original-price">1.289,99 €</span>
  </div>
  <div style="display:flex; align-items:center; gap:0.625rem;">
    <div class="product-card__swatch" style="background:#505f70;"></div>
    <div class="product-card__swatch" style="background:rgba(0,0,0,0.75);"></div>
    <div class="product-card__swatch" style="background:#b02828;"></div>
    <a class="product-card__more-colors">+ 5 weitere</a>
  </div>
</div>
```

```html
.product-card {
  width: 21.25rem;
  border-radius: var(--radius-lg);
  border: 0.0625rem solid var(--color-graphite-300);
  background: var(--color-white);
  padding: 1.25rem;
  display: flex; flex-direction: column; gap: 0.9375rem;
  box-sizing: border-box; position: relative;
  transition: box-shadow 0.2s ease;
}
.product-card:hover { box-shadow: 0 0.25rem 1.25rem rgba(0,0,0,0.12); }
.product-card__image {
  width: 100%; aspect-ratio: 1/1;
  background: var(--color-paper); border-radius: var(--radius);
  overflow: hidden; position: relative;
}
.product-card__badge {
  position: absolute; top: 0.3125rem; left: 0.3125rem;
  background: var(--color-teal); border-radius: var(--radius-sm);
  padding: 0.1875rem 0.375rem; font-size: 0.875rem; font-weight: 500;
  color: var(--color-white); line-height: 1rem; white-space: nowrap;
}
.product-card__brand { font-size: 0.875rem; font-weight: 500; color: var(--color-teal); }
.product-card__review-count { font-size: 0.6875rem; font-weight: 500; color: var(--color-black); }
.product-card__title {
  font-size: 1rem; font-weight: 500; color: var(--color-black);
  line-height: 1.375rem; display: -webkit-box;
  -webkit-line-clamp: 3; -webkit-box-orient: vertical;
  overflow: hidden; height: 4.125rem;
}
.product-card__price-from { font-size: 1rem; color: var(--color-black); }
.product-card__price { font-size: 1.25rem; font-weight: 700; color: #C90000; }
.product-card__original-price {
  font-size: 0.875rem; color: var(--color-black); text-decoration: line-through;
}
.product-card__discount {
  background: #C90000; border-radius: var(--radius);
  padding: 0.125rem 0.375rem; font-size: 0.75rem; font-weight: 800;
  color: var(--color-white);
}
.product-card__swatch {
  width: 1.75rem; height: 1.75rem; border-radius: var(--radius);
  border: 0.0625rem solid var(--color-graphite-300); cursor: pointer;
}
.product-card__more-colors {
  font-size: 1rem; color: var(--color-black);
  text-decoration: underline; cursor: pointer;
}
```
MOBILE — 2-COLUMN GRID · SAME DESIGN AS DESKTOP · SMALLER PADDINGS

Width 50% per card (2-column grid). Same design as the desktop card — border (1px graphite-200), --radius-lg corners and the feature-pill row — just tighter: 12px card padding and smaller type/swatches. Static image (no hover swap). Title clamped to 2 lines. Container has 15px padding and15px gap between cards.

```html
/* ── Product Card · Mobile ── ──────────────────────── */
/* 2-column grid · ≤767px · flush · no border · no padding */
.product-card--mobile {
  width: 100%;
  border-radius: 0;
  border: none;
  background: var(--color-white);
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  box-sizing: border-box;
  position: relative;
  /* No hover shadow — touch devices */
}
/* Image */
.product-card--mobile .product-card__image {
  width: 100%;
  aspect-ratio: 1 / 1;
  border-radius: var(--radius);
  overflow: hidden;
}
/* Badges */
.product-card--mobile .product-card__badge {
  font-size: 0.625rem;
  padding: 0.125rem 0.3125rem;
  line-height: 0.875rem;
}
/* Brand */
.product-card--mobile .product-card__brand {
  font-size: 0.6875rem;
  line-height: 0.875rem;
}
/* Title — 2-line clamp */
.product-card--mobile .product-card__title {
  font-size: 0.75rem;
  line-height: 1.0625rem;
  -webkit-line-clamp: 2;
  height: 2.125rem;
}
/* Price */
.product-card--mobile .product-card__price {
  font-size: 0.875rem;
}
.product-card--mobile .product-card__price-from,
.product-card--mobile .product-card__original-price {
  font-size: 0.6875rem;
}
/* Swatches */
.product-card--mobile .product-card__swatch {
  width: 1.125rem;
  height: 1.125rem;
  border-radius: 0.1875rem;
}
/* 2-column layout (mobile grid) */
@media (max-width: 767px) {
  .product-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    padding: 0 1rem;
  }
}
```

## Configurator

```html
<!-- Aktiv: grüne Checkbox + grüner Rahmen + Mengenzähler -->
<div class="config-card config-card--active">
  <span class="checkbox checkbox--configurator checkbox--checked"></span>
  <img src="innenstation.webp" alt="…">
  <div class="config-card__title">Metzler Innenstation mit 7″ Touchdisplay | Weiß</div>
  <div class="config-card__price">+279,00 €</div>
  <div class="qty-counter">…</div>
</div>
<!-- Default: leere Checkbox + grauer Rahmen · KEIN Mengenzähler (erscheint erst nach Auswahl) -->
<div class="config-card">
  <span class="checkbox checkbox--configurator"></span>
  <img src="innenstation.webp" alt="…">
  <div class="config-card__title">Metzler Innenstation mit 7″ Touchdisplay | Schwarz</div>
  <div class="config-card__price">+279,00 €</div>
</div>
```

## Header

```html
<!-- Desktop Info Bar — height 48px, background var(--color-teal, #015253) -->
<div class="info-bar">
  <div class="container">
    <div class="info-bar__links">
      <span class="info-bar__label">Fragen? Hotline:</span>
      <a class="info-bar__item info-bar__item--primary" href="tel:+4971213177333">
        <!-- phone icon --> 07121-3177333
      </a>
      <span class="info-bar__sep"></span>
      <a class="info-bar__btn" href="#">
        <!-- calendar icon --> Termin vereinbaren
      </a>
      <a class="info-bar__btn" href="#">
        <!-- map-pin icon --> Fachhandelspartner
      </a>
    </div>
    <a class="info-bar__cta" href="#">
      <!-- info icon --> Info- &amp; Hilfecenter
    </a>
  </div>
</div>
<!-- Mobile Info Bar — accordion (add class .is-open to toggle) -->
<div class="info-bar info-bar--mobile">
  <button class="info-bar__accordion" aria-expanded="false">
    Info- &amp; Hilfecenter
    <svg class="info-bar__chevron" width="16" height="16" viewBox="0 0 24 24"
      fill="none" stroke="currentColor" stroke-width="2.5"
      stroke-linecap="round" stroke-linejoin="round">
      <polyline points="6 9 12 15 18 9"/>
    </svg>
  </button>
  <div class="info-bar__dropdown">
    <a class="info-bar__dropdown-item" href="#">Metzler FAQ</a>
    <a class="info-bar__dropdown-item" href="#">Termin vereinbaren</a>
    <a class="info-bar__dropdown-item" href="#">Fachhandelspartner</a>
  </div>
</div>
```

```html
/* ── Desktop ── */
.info-bar {
  background: var(--color-teal, #015253);
  height: 3rem;  /* 48px */
}
.info-bar .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.info-bar__links {
  display: flex; align-items: center; gap: 0.875rem;
}
.info-bar__label {
  color: rgba(255,255,255,0.72);
  font-size: 0.8125rem;
  white-space: nowrap;
}
.info-bar__item {
  display: flex; align-items: center; gap: 0.375rem;
  color: var(--color-white);
  font-size: 0.8125rem;
  font-weight: 700;
  text-decoration: none;
}
.info-bar__sep {
  width: 0.0625rem; height: 0.875rem;
  background: rgba(255,255,255,0.25); flex-shrink: 0;
}
.info-bar__btn {
  display: flex; align-items: center; gap: 0.375rem;
  padding: 0.25rem 0.625rem;
  border-radius: 0.25rem;
  border: 0.0625rem solid rgba(255,255,255,0.4);
  color: var(--color-white);
  font-size: 0.8125rem; font-weight: 500;
  text-decoration: none;
  transition: background 0.15s; white-space: nowrap;
}
.info-bar__btn:hover { background: rgba(255,255,255,0.12); }
.info-bar__cta {
  display: flex; align-items: center; gap: 0.375rem;
  padding: 0.3125rem 0.875rem;
  border-radius: 0.25rem;
  background: rgba(255,255,255,0.8);
  color: var(--color-teal);
  font-size: 0.8125rem; font-weight: 600;
  text-decoration: none; transition: background 0.15s;
}
.info-bar__cta:hover { background: rgba(255,255,255,0.95); }
/* ── Mobile — accordion ── */
@media (max-width: 48rem) {
  .info-bar--mobile { height: auto; position: relative; }
  .info-bar__accordion {
    width: 100%;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 1rem; height: 2.75rem;
    background: none; border: none; outline: none;
    color: var(--color-white);
    font-size: 0.875rem; font-weight: 700;
    cursor: pointer;
  }
  .info-bar__chevron {
    transition: transform 0.2s;
  }
  .info-bar__accordion[aria-expanded="true"] .info-bar__chevron {
    transform: rotate(180deg);
  }
  .info-bar__dropdown {
    display: none;
    background: var(--color-white);
  }
  .info-bar__accordion[aria-expanded="true"] + .info-bar__dropdown {
    display: block;
  }
  .info-bar__dropdown-item {
    display: block;
    padding: 0.875rem 1rem;
    font-size: 0.875rem; font-weight: 700;
    color: var(--color-teal);
    text-decoration: none;
    border-bottom: 0.0625rem solid var(--color-graphite-200);
  }
  .info-bar__dropdown-item:last-child { border-bottom: none; }
  .info-bar__dropdown-item:hover { background: var(--color-teal-50); }
}
```

```html
<!-- Header Desktop — 3 rows: info bar · logo+search+icons · category nav -->
<!-- Row 1: Info bar (see Info Bar component) -->
<div class="info-bar">
  <div class="container"><!-- phone · ghost buttons · CTA --></div>
</div>
<!-- Row 2: Logo + Search + Icons -->
<header class="site-header">
  <div class="container site-header__inner">
    <a href="/" class="site-header__logo">
      <img src="header/logo.svg" alt="Metzler" />
    </a>
    <div class="site-header__search">
      <span>Produkte suchen</span>
      <!-- search icon -->
    </div>
    <div class="site-header__actions">
      <!-- user icon · cart icon with badge -->
    </div>
  </div>
</header>
<!-- Row 3: Category nav -->
<nav class="category-nav">
  <div class="container">
    <a class="category-nav__item" href="#">Briefkastenanlagen</a>
    <a class="category-nav__item" href="#">Türsprechanlagen</a>
    <!-- … more items -->
  </div>
</nav>
```

```html
.site-header { background: var(--color-white); }
.site-header__inner {
  display: flex; align-items: center; gap: 3.125rem;
  height: 4.375rem;
}
.site-header__logo img { height: 2.125rem; }
.site-header__search {
  flex: 1; background: var(--color-paper); border-radius: var(--radius);
  height: 2.5rem; display: flex; align-items: center;
  justify-content: space-between; padding: 0 0.9375rem;
  font-size: 1rem; color: var(--color-graphite-500);
}
.site-header__actions { display: flex; align-items: center; gap: 1.25rem; }
.category-nav {
  background: var(--color-white);
  border-top: 0.0625rem solid var(--color-graphite-300);
  height: 2.5rem;
}
.category-nav .container { display: flex; align-items: stretch; }
.category-nav__item {
  height: 2.5rem; display: flex; align-items: center;
  padding: 0 0.5rem; font-size: 1rem; font-weight: 500;
  color: var(--color-black); text-decoration: none;
}
.category-nav__item:hover { color: var(--color-teal); }
```

## Header · Mobile

```html
<!-- Mobile Header — 360px · Top bar: teal 23px · Logo bar: white 45px -->
<!-- Top trust bar -->
<div class="mobile-header__top">
  <span><b>1.5 Mio.</b> Kunden</span>
  <span><b>10 Jahre</b> Metzler Garantie</span>
</div>
<!-- Logo bar: hamburger + search | logo | user + cart -->
<div class="mobile-header__bar">
  <div class="mobile-header__left">
    <button class="mobile-header__icon-btn" aria-label="Menü"><!-- hamburger --></button>
    <button class="mobile-header__icon-btn" aria-label="Suche"><!-- search --></button>
  </div>
  <a href="/" class="mobile-header__logo">
    <img src="header/logo.svg" alt="Metzler" />
  </a>
  <div class="mobile-header__right">
    <button class="mobile-header__icon-btn" aria-label="Konto"><!-- user --></button>
    <button class="mobile-header__icon-btn" aria-label="Warenkorb"><!-- cart --></button>
  </div>
</div>
```

```html
.mobile-header__top {
  background: var(--color-teal); height: 1.4375rem;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 0.8125rem;
  font-size: 0.75rem; color: var(--color-white);
}
.mobile-header__bar {
  height: 2.8125rem; background: var(--color-white);
  border-bottom: 0.03125rem solid var(--color-graphite-300);
  display: flex; align-items: center;
  justify-content: space-between; padding: 0 0.9375rem;
}
.mobile-header__logo img { width: 6.875rem; height: 1.1875rem; object-fit: contain; }
.mobile-header__left,
.mobile-header__right { display: flex; gap: 0.625rem; align-items: center; }
.mobile-header__icon-btn {
  background: none; border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
}
```

## Header · Sticky

```html
<!-- Sticky Mobile Header — logo bar only, fixed to top on scroll -->
<!-- Same markup as .mobile-header__bar — add .is-sticky via JS on scroll -->
<div class="mobile-header__bar sticky-header">
  <div class="mobile-header__left">
    <button class="mobile-header__icon-btn" aria-label="Menü"><!-- hamburger --></button>
    <button class="mobile-header__icon-btn" aria-label="Suche"><!-- search --></button>
  </div>
  <a href="/" class="mobile-header__logo">
    <img src="header/logo.svg" alt="Metzler" />
  </a>
  <div class="mobile-header__right">
    <button class="mobile-header__icon-btn" aria-label="Konto"><!-- user --></button>
    <button class="mobile-header__icon-btn" aria-label="Warenkorb"><!-- cart --></button>
  </div>
</div>
```

```html
/* Sticky state — add .sticky-header via JS when scrollY > 0 */
.sticky-header {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  box-shadow: 0 0.125rem 0.5rem rgba(0,0,0,0.10);
}
/* JS — toggle class on scroll */
/* window.addEventListener('scroll', () => {
  document.querySelector('.mobile-header__bar')
    .classList.toggle('sticky-header', window.scrollY > 0);
}); */
```

## Footer
Edelstahl-Tuerklingel.de ist ein Unternehmen der Metzler Gruppe

Der Anbieter für Briefkästen, Sprechanlagen, Türklingeln und Hausnummern.

Follow us

Qualität

Allgemeine Hotline:

Sprechanlagen Hotline:

E-Mail Support:

Kontaktformular:

Informationen

Service

## Footer · Mobile
Der Anbieter für Briefkästen, Sprechanlagen, Türklingeln und Hausnummern.

Edelstahl-Tuerklingel.de ist ein Unternehmen der Metzler Gruppe

Alle Preise inkl. gesetzliche MwSt., zzgl. Versand

© 2013 - 2024 | Metzler GmbH
