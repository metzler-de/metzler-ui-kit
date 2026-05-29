# Metzler Design System — Claude Briefing

Share this file with Claude when asking it to build pages, components, or UI for Metzler.
It contains exact tokens, component patterns, and layout rules so Claude produces output
that matches the real design system — not a guess.

---

## Brand

- **Company:** Metzler GmbH — sells outdoor hardware (mailboxes, doorbells, intercoms, house numbers, garden)
- **Font rule — same weights, sizes, and line-heights on all systems:**
  - macOS / Ubuntu → `"Helvetica Neue", Helvetica, Arial, sans-serif` (Helvetica Neue first)
  - Windows → `Arial, "Helvetica Neue", Helvetica, sans-serif` (Arial first = default)
  - No import needed — both are system fonts.
- **Language:** German (DE) by default
- **Logo:** Red M-square (`#D42924`) on left, "METZLER" wordmark in `#1A171B` on right
- **Base:** 16px = 1rem. All measurements in rem.

---

## Design Tokens (CSS)

Paste this `<link>` in any HTML page, or copy the variables directly into a `<style>` block:

```css
:root {
  /* FONT */
  --font: "Helvetica Neue", Helvetica, Arial, sans-serif;

  /* TEAL — brand primary */
  --teal-50:   #F2F6F6;
  --teal-75:   #E3F2F0;
  --teal-100:  #E6EEEE;
  --teal:      #015253;   /* DEFAULT — CTAs, links, focus rings */
  --teal-600:  #014A4B;   /* hover / pressed */
  --teal-700:  #013E3E;   /* high-contrast text */
  --teal-900:  #001D1D;   /* footer background */

  /* BRAND */
  --rot:    #D42924;   /* Metzler Rot — logo M-square, sale badges ONLY */
  --black:  #1A171B;   /* Digital Schwarz — headlines, wordmark */

  /* GREEN — success / availability */
  --green:  #009951;

  /* RED — error / signal (anchored to Metzler Rot) */
  --red-50:   #FFF0EF;   /* error background fills */
  --red:      #D42924;   /* DEFAULT error color */
  --red-600:  #B52320;   /* hover */
  --red-900:  #4D0E0D;   /* text on red surfaces */

  /* ACCENT */
  --mint:   #5CDBD3;   /* links on dark/teal backgrounds */
  --star:   #FFC041;   /* review stars */

  /* SURFACES */
  --paper:     #F5F6FA;   /* page background */
  --g-100:     #F0F0F0;   /* row dividers, skeleton */
  --g-200:     #E6E6E8;   /* hairline separators */
  --g-300:     #DADADA;   /* default borders */
  --g-400:     #BFBFC2;   /* focused borders */
  --g-450:     #CCCCCC;   /* soft borders, dividers, skeleton */

  /* TEXT */
  --g-500:     #A1A1A1;   /* placeholder, disabled */
  --g-600:     #7A7A82;   /* metadata, captions */
  --g-700:     #54545C;   /* secondary text */
  --g-800:     #2E2E36;   /* body text */
  --g-850:     #333333;   /* icon fills, dark UI labels */
  --g-900:     #1A1A1F;   /* headings */

  /* BASE */
  --white: #FFFFFF;

  /* GRADIENTS */
  --gradient-brand:  linear-gradient(90deg, #01292A 0%, #011D1E 50%, #000000 100%);
  --gradient-accent: linear-gradient(135deg, #5CDBD3, #015253);

  /* RADIUS */
  --radius-sm:   0.125rem;   /* 2px  — badges */
  --radius:      0.25rem;    /* 4px  — DEFAULT: buttons, inputs */
  --radius-lg:   0.5rem;     /* 8px  — cards, modals */
  --radius-xl:   0.75rem;    /* 12px — large modals */
  --radius-pill: 624.94rem;  /* fully rounded */

  /* SHADOWS */
  --shadow-card:  0 0.125rem 0.5rem rgba(0,0,0,0.08);
  --shadow-modal: 0 1.25rem 3.75rem rgba(0,0,0,0.2), 0 0.25rem 1rem rgba(0,0,0,0.1);
}
```

---

## Typography Scale

| Style | Size | Weight | Line-height |
|---|---|---|---|
| Display 1 | clamp(3rem, 9vw, 8rem) | 700 | 0.85 |
| Display 2 | clamp(3rem, 7vw, 6rem) | 700 | 0.95 |
| H1 | 1.875rem | 700 | 1.25 |
| H2 | 1.5rem | 700 | 1.3 |
| H3 | 1.25rem | 700 | 1.35 |
| H4 | 1.125rem | 700 | 1.375 |
| Body | 1rem | 400/500/700 | 1.5 |
| Body SM | 0.875rem | 400/500/700 | 1.5 |
| Caption | 0.75rem | 400/500/700 | 1.4 |

---

## Breakpoints

| Name | px | Role |
|---|---|---|
| sm | 480px | small mobile |
| md | 768px | **critical** — mobile ↔ desktop switch |
| lg | 1024px | tablet landscape |
| xl | 1280px | desktop |
| 2xl | 1440px | wide desktop |
| 3xl | 1600px | max content width |

Below 768px: hamburger header, stacked footer, single-column layout, block buttons.

---

## Header — Desktop (sticky, 64px)

```html
<header style="background:#fff; border-bottom:1px solid #E6E6E8; height:4rem;">
  <div style="max-width:100rem; margin:0 auto; padding:0 2.5rem;
              height:100%; display:flex; align-items:center; gap:1.25rem;">

    <!-- Logo -->
    <a href="/">
      <!-- Red M-square SVG + METZLER wordmark -->
    </a>

    <!-- "Alle Kategorien" button -->
    <button style="background:#015253; color:#fff; border:none;
                   border-radius:0.25rem; height:2.5rem; padding:0 1.2rem;
                   font-size:1rem; font-weight:500; cursor:pointer;">
      ☰ Alle Kategorien
    </button>

    <!-- Search bar -->
    <div style="flex:1; max-width:calc(100% - 30rem); height:2.5rem;
                background:#F5F6FA; border:1px solid #E6E6E8;
                border-radius:0.25rem; display:flex; align-items:center;
                padding:0 1rem; gap:0.75rem;">
      <input placeholder="Suchen — Türklingel, Briefkasten..."
             style="flex:1; border:none; background:none; font-size:0.9375rem;" />
    </div>

    <!-- Icons: account + cart -->
    <div style="display:flex; gap:0.5rem; margin-left:auto;">
      <a href="#" style="width:2.5rem; height:2.5rem; display:flex;
                         align-items:center; justify-content:center;
                         border-radius:50%; color:#333;"><!-- user icon --></a>
      <a href="#" style="width:2.5rem; height:2.5rem; display:flex;
                         align-items:center; justify-content:center;
                         border-radius:50%; color:#333;"><!-- cart icon --></a>
    </div>
  </div>
</header>
```

---

## Header — Mobile (50px)

```html
<header style="height:3.125rem; background:#fff; border-bottom:1px solid #DADADA;
               display:flex; align-items:center; justify-content:space-between;
               padding:0 0.9375rem;">
  <div style="display:flex; gap:1rem;">
    <!-- Hamburger + Search icon -->
  </div>
  <!-- Centered logo -->
  <a href="/"><img src="logo.svg" style="height:1.375rem;" /></a>
  <div style="display:flex; gap:1rem;">
    <!-- User + Cart icons -->
  </div>
</header>
```

---

## Footer — Desktop

```html
<footer style="background:#001D1D; color:#fff; padding:3rem 2.5rem 1.5rem;">
  <div style="max-width:100rem; margin:0 auto;">
    <!-- 4-column grid: logo+desc | links | links | contact -->
    <!-- Link hover color: #5CDBD3 (mint) -->
    <!-- Divider line: rgba(255,255,255,0.1) -->
  </div>
</footer>
```

---

## Buttons

```css
/* Primary */
.btn-primary {
  background: #015253; color: #fff; border: none;
  border-radius: 0.25rem; padding: 0.6rem 1.25rem;
  font-size: 1rem; font-weight: 500; cursor: pointer;
}
.btn-primary:hover  { background: #014A4B; }
.btn-primary:active { background: #013E3E; }

/* Secondary (outline) */
.btn-secondary {
  background: transparent; color: #015253;
  border: 2px solid #015253; border-radius: 0.25rem;
  padding: 0.6rem 1.25rem; font-size: 1rem; font-weight: 500;
}
.btn-secondary:hover { background: #E6EEEE; }

/* Ghost */
.btn-ghost {
  background: transparent; color: #54545C;
  border: 1px solid #DADADA; border-radius: 0.25rem;
  padding: 0.6rem 1.25rem;
}
.btn-ghost:hover { background: #F5F6FA; }

/* Danger */
.btn-danger {
  background: #D42924; color: #fff; border: none;
  border-radius: 0.25rem; padding: 0.6rem 1.25rem;
}
.btn-danger:hover { background: #B52320; }
```

---

## Form Inputs

```css
.input {
  width: 100%; height: 3rem; /* 48px */
  border: 1px solid #DADADA; border-radius: 0.25rem;
  padding: 0 1rem; font-size: 1rem; font-family: var(--font);
  color: #2E2E36; background: #fff; outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.input:focus {
  border-color: #015253;
  box-shadow: 0 0 0 3px rgba(1,82,83,0.15);
}
.input::placeholder { color: #A1A1A1; }
.input.error        { border-color: #D42924; }
```

---

## Cards

```css
.card {
  background: #fff;
  border: 1px solid #E6E6E8;
  border-radius: 0.5rem;  /* 8px — cards always use radius-lg */
  overflow: hidden;
}
.card:hover {
  box-shadow: 0 0.25rem 1.25rem rgba(0,0,0,0.1);
}
```

---

## Alerts / Notifications

No border — background fill only. No left-accent border.

```html
<!-- Success -->
<div style="background:#E3F2F0; border-radius:0.25rem; padding:0.875rem 1rem;
            display:flex; gap:0.75rem; color:#013E3E;">
  ✓  Your changes have been saved successfully.
</div>

<!-- Error -->
<div style="background:#FFF0EF; border-radius:0.25rem; padding:0.875rem 1rem;
            display:flex; gap:0.75rem; color:#4D0E0D;">
  ⚠  Something went wrong.
</div>

<!-- Warning: background #FFF3E0, color #7A3800 -->
<!-- Info:    background #E6EEEE, color #013E3E -->
```

---

## Modal

```html
<!-- Overlay -->
<div style="position:fixed; inset:0; background:rgba(0,0,0,0.45);
            display:flex; align-items:center; justify-content:center; padding:1rem; z-index:9999;">

  <!-- Dialog — default 520px, sm 400px, lg 800px -->
  <div style="width:100%; max-width:32.5rem; background:#fff;
              border-radius:0.5rem;
              box-shadow:0 1.25rem 3.75rem rgba(0,0,0,0.2), 0 0.25rem 1rem rgba(0,0,0,0.1);
              display:flex; flex-direction:column; max-height:90vh; overflow:hidden;">

    <!-- Header -->
    <div style="display:flex; align-items:center; justify-content:space-between;
                padding:1.25rem 1.5rem; border-bottom:1px solid #E6E6E8;">
      <span style="font-size:1.125rem; font-weight:700;">Titel</span>
      <!-- Close button: 2rem × 2rem, border-radius 0.25rem, color #555 -->
    </div>

    <!-- Body -->
    <div style="padding:1.5rem; overflow-y:auto; flex:1;">
      Content
    </div>

    <!-- Footer -->
    <div style="display:flex; justify-content:flex-end; gap:0.75rem;
                padding:1rem 1.5rem; border-top:1px solid #E6E6E8;">
      <!-- Buttons -->
    </div>
  </div>
</div>
```

---

## Rules Claude must follow

1. **All measurements in rem** — never px. Base: 16px = 1rem.
2. **Never hardcode hex values** — use the token values from the table above.
3. **Primary CTA = `#015253` (teal)** — never use red for buttons.
4. **Red (`#D42924`)** is for error states, sale badges, and the logo M-square only.
5. **Cards use `border-radius: 0.5rem`** (8px), controls use `0.25rem` (4px).
6. **Font is always** `"Helvetica Neue", Helvetica, Arial, sans-serif`.
7. **Page background** is `#F5F6FA` (Paper White), not pure white.
8. **Body text** is `#2E2E36` (Graphite 800), not black.
9. **Alerts have no left-accent border** — background fill only.
10. **Links on dark/teal backgrounds** use mint `#5CDBD3`.
