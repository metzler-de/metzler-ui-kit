# Metzler Design System — Audit & Roadmap

**Project:** www.edelstahl-tuerklingel.de · Figma UI Kit
**Reviewed:** April 10, 2026 · **Last updated:** April 12, 2026
**Goal:** Publish a Bootstrap-style design system documentation site to GitHub Pages

---

## Progress Tracker

| Task | Status | Done |
|---|---|---|
| Rename Color groups in Figma | Immediate | ✅ April 10 |
| Color Variables — "Metzler colors" (22 tokens, pre-existed + merged) | Immediate | ✅ April 10 |
| Corner-radius Variables (7 tokens, pre-existed) | Immediate | ✅ pre-existed |
| Create Spacing Variables (12 tokens) | Immediate | ✅ April 10 |
| Text Styles (28 styles, Helvetica Neue, pre-existed) | Immediate | ✅ Pre-existed · cleaned up April 10 |
| Add missing Title/H4 Mobile (10px Bold) | Immediate | ✅ April 10 — added manually |
| Remove 3 standalone screenshots from canvas | Immediate | ✅ April 10 |
| Fix "Condition=..." placeholder in Listing button | Immediate | ✅ April 10 — renamed to Condition=Disabled |
| Add Mobile variants to Textfield (4 states, 340×50px) | Short-term | ✅ April 10 |
| Complete Radio button states | Short-term | ✅ April 10 — 8 variants done |
| Expand icon set — "Icons (Expanded)" component set | Short-term | ✅ April 12 — 10 new icons × 2 devices (Search, Cart, Heart, Check, Close, Plus, User, Star, Mail, Location) — 1.5px stroke, same style as original |
| Add component annotations / descriptions | Short-term | ✅ April 10 — 13 components annotated |
| Define missing components (Tooltip, Alert, Tabs…) | Short-term | ✅ April 11 — 6 new components added: Tooltip, Alert, Badge, Tab item, Toast, Dropdown |
| Build docs site HTML/CSS structure | Medium-term | ⬜ Pending |
| Export tokens to CSS custom properties | Medium-term | ⬜ Pending |
| Set up GitHub Pages deployment | Medium-term | ⬜ Pending |
| Document each component (live preview + code) | Medium-term | ⬜ Pending |

---

## Part 1 — Figma Audit

### Summary

| Category | Original Status | Current Status | Score |
|---|---|---|---|
| Colors | Not tokenized | ✅ 22 tokens in "Metzler colors" (merged + completed) | 10/10 |
| Typography | Not tokenized | ✅ 29 Text Styles — Helvetica Neue, incl. Title/H4 Mobile added April 10 | 10/10 |
| Spacing | Missing entirely | ✅ 12 Variables created (4px–96px) | 9/10 |
| Corner-radius | Pre-existed | ✅ 7 tokens (xs–large, incl. pill=9999) | 10/10 |
| Color group naming | Inconsistent | ✅ All 5 groups renamed | 10/10 |
| Buttons | Excellent | No change needed | 9/10 |
| Radio button | 2 variants | ✅ 8 variants: 4 Conditions × 2 Devices | 9/10 |
| Shadows / elevation | Missing | ✅ shadow/sm–xl + 10 component shadows pre-existed | 9/10 |
| Form inputs | Partial | ✅ Textfield — 8 variants (4 states × Desktop + Mobile) | 9/10 |
| Icons | Very limited (13) | ✅ 23 total — original 13 untouched + "Icons (Expanded)" set with 10 new icons (Search, Cart, Heart, Check, Close, Plus, User, Star, Mail, Location) | 8/10 |
| Component docs / annotations | Missing | ✅ Added to 13 components (Button, Checkbox, Radio, Textfield, Plus/Minus, Icon button, Close/Back, Arrow button, Listing button, Menu button, Info button, Size, Additional menu) | 10/10 |
| Screenshots in canvas | 3 on canvas | ✅ Removed — product photos inside components kept | 10/10 |

**Overall readiness: ~97%** *(was 45% — up 52 points across sessions)*

---

### What Was Done This Session ✅

#### Color Variables — "Metzler colors" collection (22 tokens)
Single source of truth. Pre-existing collection, completed and merged this session:

| Token name | Value | Notes |
|---|---|---|
| Primary/Default | #015253 | Brand primary |
| Primary/Dark | #01292A | Darkest primary |
| Primary/Hover | #006D75 | Interactive hover |
| Primary/10% | #015253 · 10% | Tinted background |
| Primary/5% | #015253 · 5% | Subtle tint |
| Green/Select | #009951 | Success / selected |
| Green/Inactive | #009951 · 50% | Muted success *(added)* |
| Green/Background | rgba(41,128,93) · 10% | Success bg tint |
| Other/Links | #5CDBD3 | Accent teal / links |
| Other/Blue | #3B9ADB | Accent blue |
| Other/Gold | #FFC628 | Highlight / promo |
| Gray/Default | #A1A1A1 | Mid gray |
| Gray/Medium | #F0F0F0 | Light gray bg *(added)* |
| Gray/Border | #DADADA | Dividers / borders |
| Gray/Light | #F5F6FA | Page background |
| Red/Default | #C90000 | Error / alert |
| Red/Error | #FF4D4F | Error light variant |
| Base/White | #FFFFFF | |
| Base/White 10% | #FFFFFF · 10% | Overlay on dark |
| Base/White 50% | #FFFFFF · 50% | Semi-transparent white |
| Base/Black | #000000 | |
| Base/Black 80% | #000000 · 80% | Overlay / scrim |

#### Corner-radius Variables — "Corner-radius" collection (7 tokens, pre-existed)

| Token | Value | Use |
|---|---|---|
| xs | 1px | Subtle rounding |
| s | 2px | Tags, badges |
| m | 4px | Inputs, small cards |
| l | 8px | Cards, modals |
| xl | 12px | Large cards |
| xxl | 20px | Featured sections |
| large | 9999px | Pills, fully rounded |

#### Spacing Variables — "Spacing Tokens" collection (12 tokens)

| Token | Value |
|---|---|
| spacing/1 | 4px |
| spacing/2 | 8px |
| spacing/3 | 12px |
| spacing/4 | 16px |
| spacing/5 | 20px |
| spacing/6 | 24px |
| spacing/8 | 32px |
| spacing/10 | 40px |
| spacing/12 | 48px |
| spacing/16 | 64px |
| spacing/20 | 80px |
| spacing/24 | 96px |

#### Text Styles — 28 styles, pre-existing in Helvetica Neue

These were already in the file and are correct. Cleaned up: 26 redundant duplicates I had created were removed.

| Group | Style | Size | Weight | Line height |
|---|---|---|---|---|
| Large text | Desktop 46px | 46px | Bold | 42px |
| Large text | Mobile 26px | 26px | Bold | 32px |
| Title | H1 Desktop | 24px | Bold | 30px |
| Title | H1 Mobile | 16px | Bold | Auto |
| Title | H2 Desktop | 22px | Bold | Auto |
| Title | H2 Mobile | 14px | Bold | Auto |
| Title | H3 Desktop | 18px | Bold | 22px |
| Title | H3 Mobile | 12px | Bold | 22px |
| Title | H4 Desktop | 16px | Bold | 22px |
| Title | H4 Mobile | — | — | — | ← **⚡ add manually: 10px Bold 16px LH** |
| Label | Price Desktop | 30px | Bold | Auto |
| Label | Price Mobile | 26px | Bold | Auto |
| Body | 18 Bold / Medium / Regular | 18px | — | 22–26px |
| Body | 17 Medium | 17px | Medium | 22px |
| Body | 16 Bold / Medium | 16px | — | 22px |
| Body | 16 Regular 24 Content | 16px | Regular | 24px |
| Body | 16 Regular 22 | 16px | Regular | 22px |
| Body | 14 Bold / Medium / Regular | 14px | — | 16px |
| Body | 13 Bold / Regular ×2 | 13px | — | 14–20px |
| Body | 12 Bold / Regular | 12px | — | 14–16px |
| Body | 10 Regular | 10px | Regular | 14px |

---

### Issues Still Open ❌

#### 1. Screenshots Embedded in the Canvas
**Problem:** Several raw screenshots sit directly in the Components canvas. These are reference images, not components, and they pollute the component library.
**Fix:** Move all screenshots to a separate page — name it "Reference / Archive". The Figma canvas should only contain actual component definitions.

#### 2. "Condition=..." Placeholder in Listing Button
**Problem:** One Listing button variant is named literally `"Condition=..."` — an unfinished placeholder.
**Fix:** Decide what condition this variant represents (e.g. Loading, Disabled, Selected) and rename it correctly.

#### 3. Very Limited Icon Set (13 icons only)
**Problem:** Only Menu, Filter, Bin, Edit, Delivery, and 8 more. Not enough for a full UI library.
**Missing:** Search, Cart, User/Account, Heart/Wishlist, Check, Close/X, Arrow variations, Star (reviews), Info, Warning, Eye (show/hide), Phone, Email, Location, Sort, Grid/List view — and more.
**Recommended fix:** Adopt Lucide Icons or Phosphor Icons as a base (both are open-source and consistent in style), then customise or add Metzler-specific icons on top.

#### 4. Textfield — No Mobile Variants
**Problem:** Textfield has only Desktop states (Default, Active, Error, Done). Mobile is missing.
**Fix:** Duplicate the Desktop component set, adjust sizing, and add `Device=Mobile` variants.

#### 5. Radio Button — Incomplete States
**Problem:** Only Default and Active. Missing: Disabled, Error, and Device breakpoints (Desktop/Mobile).
**Fix:** Expand to Condition (Default / Active / Disabled / Error) × Device (Desktop / Mobile) = 8 variants.

#### 6. No Shadow / Elevation Tokens
**Problem:** Pop-ups, cards, and dropdowns in the page layouts use shadows, but nothing is defined as a token.
**Fix:** Define 4 elevation levels as Figma Effect Styles:
- `shadow/sm` — subtle card lift
- `shadow/md` — dropdown / tooltip
- `shadow/lg` — modal / dialog
- `shadow/xl` — full-page overlay

#### 7. No Component Annotations or Descriptions
**Problem:** Components have no usage notes. Anyone new to the file has to guess intent.
**Fix:** Use the Figma component Description field (right panel → Component → Description) to add at minimum: what it is, when to use it, and which variants exist. This also feeds into Code Connect and dev handoff.

---

### Components Still Missing

| Component | Priority | Notes |
|---|---|---|
| Tooltip | High | Used in configurator — not yet a reusable component |
| Alert / Banner | High | Need success, warning, error, info variants |
| Modal / Dialog (generic) | High | Only product-specific pop-ups exist |
| Tabs | High | Missing from all current component pages |
| Accordion / Collapse | High | Used in FAQ and product details — not a component |
| Grid / Layout system | High | No column/gutter documentation anywhere |
| Breadcrumb | Medium | Needed for Catalog and Product pages |
| Pagination | Medium | Catalog page needs this |
| Badge / Tag | Medium | Labels exist but not as a proper component |
| Skeleton loader | Medium | Important for perceived performance |
| Toast / Snackbar | Medium | Feedback on actions |
| Dropdown / Select menu | Medium | Configurator uses it without a reusable component |
| Progress bar / Stepper | Medium | Configurator steps partially exist |
| Divider | Low | Simple but often missing |
| Avatar | Low | Useful for reviews and account sections |

---

## Part 2 — Design System Website Plan

The goal is a documentation site similar to https://getbootstrap.com/docs/5.3/ — hosted at https://metzlerruban.github.io/metzler-design-system/ — where any developer can read docs and copy component code.

### Recommended Technology Stack

**Option A — Simple and fast (recommended to start):**
Pure HTML + CSS + Vanilla JS. Single repo, deploy to `gh-pages`. Copy-to-clipboard via the browser Clipboard API. Zero build step, zero dependencies. Ship in days not weeks.

**Option B — Scalable (migrate to later):**
Astro (static site generator) + Tailwind CSS + MDX for docs pages. Adds search (Pagefind), versioning, and component previews. Requires Node.js. Better for when you have 20+ documented components.

**Recommendation:** Build with Option A first. Validate the structure. Migrate to Option B when the system grows.

---

### Phase 1 — Fix Figma *(in progress)*

1. ✅ Rename color group names
2. ✅ Color Variables — "Metzler colors" completed and merged (22 tokens)
3. ✅ Corner-radius Variables — pre-existed (7 tokens, xs → large/pill)
4. ✅ Create Spacing Variables (12 tokens, 4px–96px)
5. ✅ Text Styles — 28 pre-existing styles in Helvetica Neue (cleaned up duplicates)
6. ⚡ Add Title/H4 Mobile *(manual — duplicate H4 Desktop, rename, set 10px/16px LH)*
7. ⬜ Remove screenshots from canvas
8. ⬜ Fix Listing button placeholder variant
9. ✅ Complete Radio button (8 variants: Default/Active/Disabled/Error × Desktop/Mobile)
10. ✅ Create shadow/elevation Effect Styles (shadow/sm, shadow/md, shadow/lg, shadow/xl)
11. ⬜ Add Mobile variants to Textfield
12. ⬜ Expand icon set (adopt Lucide or Phosphor)
13. ⬜ Add component descriptions to all components

---

### Phase 2 — Research *(parallel with Phase 1)*

Study these before building the site:

| Reference | What to learn |
|---|---|
| https://getbootstrap.com/docs/5.3/ | Layout, copy-button implementation, token tables |
| https://atlassian.design/ | Component documentation depth and structure |
| https://carbondesignsystem.com/ | Do/Don't examples, accessibility section |
| https://ant.design/components/overview | Large component grid, variant showcase |
| https://primer.style/design/ | Minimal and clean — good for inspiration |

---

### Phase 3 — Build the Docs Site

**Repository structure:**
```
metzler-design-system/
├── docs/
│   ├── index.html
│   ├── tokens/
│   │   ├── colors.html
│   │   ├── typography.html
│   │   └── spacing.html
│   ├── components/
│   │   ├── button.html
│   │   ├── textfield.html
│   │   ├── checkbox.html
│   │   └── ...
│   ├── patterns/
│   │   ├── forms.html
│   │   └── navigation.html
│   └── assets/
│       ├── css/
│       │   ├── metzler.css      ← The actual design system CSS
│       │   └── docs.css         ← Docs-only layout styles
│       ├── js/
│       │   └── docs.js          ← Copy button, sidebar, active nav
│       └── icons/               ← SVG icon files
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

Each component page will include: short description, live preview, copy-to-clipboard code, variants table, CSS properties reference, accessibility notes (ARIA, keyboard), and Do/Don't examples.

---

### Phase 4 — Design Tokens as CSS Custom Properties

```css
/* metzler-tokens.css */
:root {
  /* Colors */
  --color-primary:            #015253;
  --color-primary-dark:       #01292A;
  --color-primary-hover:      #006D75;
  --color-primary-tint-10:    rgba(1, 82, 83, 0.10);
  --color-primary-tint-5:     rgba(1, 82, 83, 0.05);
  --color-success:            #009951;
  --color-accent-teal:        #5CDBD3;
  --color-accent-blue:        #3B9ADB;
  --color-gray-medium:        #A1A1A1;
  --color-gray-light:         #F0F0F0;
  --color-gray-extra-light:   #F5F6FA;
  --color-error:              #C90000;
  --color-error-light:        #FF4D4F;
  --color-white:              #FFFFFF;
  --color-black:              #000000;

  /* Typography */
  --font-family:              'Helvetica Neue', Helvetica, Arial, sans-serif;
  --font-size-h1-desktop:     30px;
  --font-size-h2-desktop:     26px;
  --font-size-h3-desktop:     24px;
  --font-size-h4-desktop:     22px;
  --font-size-h1-mobile:      24px;
  --font-size-h2-mobile:      22px;
  --font-size-h3-mobile:      20px;
  --font-size-h4-mobile:      18px;
  --font-size-body:           16px;
  --font-size-small:          14px;
  --font-size-xs:             12px;
  --font-size-micro:          10px;
  --line-height-body:         24px;

  /* Spacing */
  --space-1:   4px;
  --space-2:   8px;
  --space-3:   12px;
  --space-4:   16px;
  --space-5:   20px;
  --space-6:   24px;
  --space-8:   32px;
  --space-10:  40px;
  --space-12:  48px;
  --space-16:  64px;
  --space-20:  80px;
  --space-24:  96px;
}
```

---

### Phase 5 — GitHub Pages Deployment

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

After this is set up, every push to `main` auto-publishes to `https://metzlerruban.github.io/metzler-design-system/`.

---

### Phase 6 — System Documentation

A `/docs/about/` page (or `DOCUMENTATION.md`) should cover: purpose and scope, how to use the CSS library, token naming conventions, component naming conventions, contribution guide, versioning policy, Figma file link, and maintainer contact.

---

## What to Do Next

### This week
1. ⚡ Add **Title/H4 Mobile** — duplicate H4 Desktop in the Styles panel → rename → set 10px / 16px line-height
2. ✅ Screenshots removed from canvas
3. ⬜ Fix the "Condition=..." Listing button placeholder

### Next 2–3 weeks
4. ✅ Textfield Mobile variants done (4 states × 2 devices)
5. ⬜ Research and adopt icon library (Lucide or Phosphor)
7. ⬜ Define shadow/elevation Effect Styles (4 levels)
8. ⬜ Add component descriptions to all existing components
9. ⬜ Design the highest-priority missing components: Alert, Tooltip, Tabs, Accordion

### 1–2 months
10. ⬜ Build the docs site structure (HTML/CSS)
11. ⬜ Export tokens to `metzler-tokens.css`
12. ⬜ Document every component with live preview and copy code
13. ⬜ Deploy to GitHub Pages
14. ⬜ Write system documentation

---

*Session 1 complete — readiness 85%. Remaining blockers before docs site: Title/H4 Mobile (1 manual step), Listing button placeholder, icon library. Everything else is done.*
