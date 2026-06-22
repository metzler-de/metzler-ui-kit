# Build the Metzler Design System in Claude — Master Instruction

> **How to use this:** Paste this entire file into Claude, together with the repository link:
> **https://github.com/metzler-de/metzler-ui-kit**
> Then tell Claude which page or component you want. Claude must read the repo first, follow every rule below exactly, and never invent values.

---

## 0 · Your mission

Recreate / extend the **Metzler Design System** — a German-language (DE) UI kit for outdoor hardware (intercoms, mailboxes, doorbells, house numbers). You are not designing from scratch: a complete, authoritative system already exists in the repo. Your job is to reproduce it **1:1** and build new pages/components on top of it with zero drift.

Default deliverable: **one self-contained HTML file** (inline `<style>`, inline `<svg>` icons, vanilla JS for interactions) that renders without a build step. No external CSS frameworks, no icon libraries, no web-font imports.

---

## 1 · Read the repo first — and obey this precedence

Before writing any code, read these files. When two sources disagree, the one **higher in this list wins**:

| Priority | File | Authority |
|---|---|---|
| 1 | **`metzler-tokens.css`** | Canonical token **names + values** (colors, radius, shadow, spacing, typography). Always the truth for variables. |
| 2 | **`index.html`** | The live React design system. Canonical for **component markup, class names, states, and interactions**. Contains a hidden `#for-claude` block auto-generated from live tokens. |
| 3 | **`FOR-CLAUDE.md`** | Prose rules + copy-paste CSS. Use for rules and layout, but if a component's class names differ from `index.html`, **`index.html` wins**. |
| 4 | **`metzler-design-system.md`** | Human reference (color/type tables, usage notes). |

If a value you need is missing, **stop and ask** — never guess a hex, size, or class name.

---

## 2 · Non-negotiable rules

1. **Tokens, never raw values.** Reference every color, radius, shadow, and font size as a CSS variable from `metzler-tokens.css`.
2. **Token scheme is `--color-*`.** Use `var(--color-teal)`, `var(--color-graphite-800)`, `var(--color-digital-black)`, `var(--color-metzler-rot)`, etc. **Never** emit the short scheme `--teal`, `--g-800`, `--black`, `--rot` — those names do not exist in the stylesheet and will render as `undefined`.
3. **rem only, never px.** Base `16px = 1rem`. Convert every pixel value (`16px → 1rem`, `2px → 0.125rem`, `8px → 0.5rem`). Do not output px in the final code.
4. **Font is the system stack.** `font-family: var(--font-family)` = `"Helvetica Neue", Helvetica, Arial, sans-serif`. Never import or set a custom font.
5. **Language is German (DE)** for all copy, labels, placeholders, and CTAs.
6. **Icons are inline `<svg>`** with `stroke="currentColor"`, `stroke-width: 1.8–2`, `stroke-linecap/linejoin: round`, `fill: none`. No external icon libraries.
7. **Container is exactly `100rem` (1600px)** — see §5.
8. **Every page uses the design-system header and footer** — never custom ones (see §7, §8).

---

## 3 · Foundation — link the tokens, then build

Start every artifact by linking (or, if linking isn't possible in the target environment, pasting verbatim) the canonical stylesheet:

```html
<link rel="stylesheet" href="metzler-tokens.css">
```

Then use the variables. Key tokens (full list in the file):

```
Brand / interactive   var(--color-teal)        #015253   CTAs, links, active, focus rings
CTA hover             var(--color-teal-600)    #014A4B
Footer / dark bg      var(--color-teal-900)    #001D1D
Brand red (logo only) var(--color-metzler-rot) #D42924   logo M-square + sale badges ONLY
Error                 var(--color-red)         #D42924   (red-50 #FFF0EF, red-600 #B52320)
Success               var(--color-green)       #009951
Accent on dark        var(--color-mint)        #5CDBD3
Stars                 var(--color-star)        #FFC041
Page bg               var(--color-paper)       #F5F6FA
Card / input bg       var(--color-white)       #FFFFFF
Hairline dividers     var(--color-graphite-200)
Default borders       var(--color-graphite-300)
Headings              var(--color-digital-black) #1A171B  (or --color-graphite-900)
Body text             var(--color-graphite-800)
Secondary text        var(--color-graphite-700)
Captions / overlines  var(--color-graphite-600)
Placeholder/disabled  var(--color-graphite-500)
Radius                var(--radius) 0.25rem · --radius-lg 0.5rem · --radius-xl 0.75rem · --radius-pill
Shadows               var(--shadow-card) · --shadow-hover · --shadow-modal
```

---

## 4 · Typography scale (exact — do not invent sizes)

All text uses `font-family: var(--font-family)`. Negative letter-spacing on large headings, zero on body.

| Class / element | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `.display-1` | `clamp(3rem, 9vw, 5rem)` (max 80px) | 700 | 0.85 | landing hero |
| `.display-2` | `clamp(3rem, 7vw, 3.5rem)` (max 56px) | 700 | 0.92 | large hero |
| `.display-3` | `3rem` (48px) | 700 | 1.0 | landing intro |
| `.display-4` | `2.875rem` (46px) | 700 | 1.1 | hero heading |
| `h1` | `1.875rem` (30px) | 700 | 1.25 | page title |
| `h2` | `1.5rem` (24px) | 700 | 1.3 | section heading |
| `h3` | `1.25rem` (20px) | 700 | 1.35 | sub-heading |
| `h4` | `1.125rem` (18px) | 700 | 1.375 | small heading |
| `.body-lg` | `1.125rem` (18px) | 400 / 500 / 700 | 1.5 (bold 1.375) | lead paragraphs, intros |
| `p` / `.body` | `1rem` (16px) | 400 | 1.55 | body — **always `--color-graphite-800`** |
| `.body-sm` | `0.875rem` (14px) | 400/500/700 | 1.5 | secondary, sidebars |
| `.label` | `0.8125rem` (13px) | 600 | — | form labels |
| `.caption` | `0.75rem` (12px) | 400 | 1.4 | metadata |
| `.overline` | `0.6875rem` (11px) | 700 | — | section kickers — `--color-graphite-600` on light, `--color-mint` on dark |

**Forbidden sizes — never use:** `10px, 15px, 17px, 19px, 22px, 28px, 32px, 36px, 72px`, or any value not in the table above.

---

## 5 · Layout

```css
.container { max-width: 100rem; margin: 0 auto; padding: 0 4rem; }
@media (max-width: 48rem) { .container { padding: 0 1.5rem; } }
```

- Every section (header, hero, content, footer) wraps its content in a `<div class="container">`.
- Outer `<header>` / `<section>` / `<footer>` have **no horizontal padding** of their own — full-width backgrounds on the outer element, content always inside `.container`.
- All content left-edges align with the logo (automatic via `.container`).

**Breakpoints (mobile-first):** sm 30rem · **md 48rem (main switch)** · lg 64rem · xl 80rem · 2xl 90rem · max 100rem. Write base styles for mobile, override with `@media (min-width: 48rem)`.

**Section spacing:** `.section { padding: 4rem 0 }` · `.section--sm { 2.5rem }` · `.section--lg { 6rem }` (mobile: 2.5rem / 1.75rem / 3.5rem). Dark section: `background: var(--color-teal-900); color: var(--color-white)`.

---

## 6 · Components — reproduce exactly from `index.html`

For each component, copy the class names, states, and CSS from the live system. Key specifics:

**Buttons** — base `.btn` + one variant. Use the **real class names** (single dash) from `index.html`:
`.btn-primary` (filled teal, main CTA) · `.btn-secondary` (outline, teal hover tint) · `.btn-proceed` (filled teal + directional arrow) · `.btn-white` (white outline, for dark backgrounds) · `.btn-dark` · `.btn-nav` (carousel arrows). Sizes: `.btn-lg`, `.btn-sm`. Full width: `.btn-block`.
🚫 Do **not** use `.btn--primary`, `.btn--ghost`, or `.btn--danger` — those do not exist in the system.
**Red is never used on any button.** CTAs are teal.

**Cards** — `.card` (white bg, `--color-graphite-200` border, `var(--radius-lg)`, hover → `--shadow-hover`). Generic icon badge `.card-icon` = 2.5rem × 2.5rem, `border-radius: var(--radius-lg)` (0.5rem), `background: rgba(1,82,83,0.08)`, `color: var(--color-teal)`. **Exception:** the feature-grid `.nfs-card-icon` uses `border-radius: 0.625rem` — that is correct only for that component.

**Form inputs** — **floating-label pattern only.** `<div class="field-wrapper"><input … placeholder=" "/><label>…</label></div>`. The `placeholder=" "` (single space) is required (CSS uses `:not(:placeholder-shown)`). Never use stacked label-above-input.

**Breadcrumbs** — left-aligned, in `.container`, below header. Links `var(--color-teal)` underlined; current item `var(--color-digital-black)`. Separator is a **chevron SVG** via `::before`, never a `/` text character.

**FAQ accordion** — copy the design-system component: `.faq-stage / .faq-list / .faq-item / .faq-btn / .faq-q / .faq-icon / .faq-body / .faq-answer`. Question `1.125rem / weight 700`. Answer `1rem / var(--color-graphite-700)`. Icon is a **chevron that rotates 180°** (not `+`/`×`); open item gets a teal left-accent bar and teal border.

**Carousel / nav arrows** — controls only; **never show step numbers or slide counters** beside them.

---

## 7 · Header — two-state, sticky on scroll

Use the design-system header. Desktop 4rem tall (logo + "Alle Kategorien" button + search bar + account/cart). Mobile 3.125rem ([hamburger, search] · centered logo · [account, cart]).

**Critical:** the header is **NOT sticky at page load.** A scroll listener adds `.is-sticky` only when `window.scrollY > 0`; any compact row starts hidden and must never carry a `visible`/`active`/`show` class in the initial HTML. Run the handler once on load to set the correct (non-sticky) state.

---

## 8 · Footer — copy verbatim, never invent

Use the exact design-system footer (`background: var(--color-teal-900)`). 4 columns on desktop → 1 on mobile. Do not invent columns, headings, or links:
- **Col 1:** logo + tagline ("Edelstahl-Tuerklingel.de ist ein Unternehmen der Metzler Gruppe" / "Der Anbieter für Briefkästen, Sprechanlagen, Türklingeln und Hausnummern.")
- **Col 2 · Kontakt** (exact): Allgemeine Hotline `+49 (0) 7121 / 317 7310`, Sprechanlagen Hotline `+49 (0) 7121 / 317 7333` (Mo–Fr 09:00–16:00), `service@metzlergmbh.de`, Kontaktformular.
- **Col 3 · Informationen:** Auszeichnungen · Fotowettbewerb · Kundenbilder · Stellenangebote · News · Zahlung und Versand
- **Col 4 · Service:** Begriffserklärung · FAQ · Geschäftskunden · Newsletter · VDM10 FAQ
- **Legal row:** © 2026 Metzler GmbH · Datenschutz · AGB · Impressum · Widerrufsrecht · Sitemap · Cookie-Einstellungen

---

## 9 · Quality bar — self-check before returning code

Reject your own output if any of these fail:
- [ ] Every color/size/radius/shadow is a `var(--color-*)` / token — zero raw hex, zero px.
- [ ] No short token names (`--teal`, `--g-800`, `--black`) anywhere.
- [ ] Container is `100rem`; header/footer outer tags have no padding.
- [ ] Header is not sticky on load; becomes sticky via JS on scroll.
- [ ] Buttons use real `.btn-*` classes; no red on any CTA.
- [ ] Breadcrumbs left-aligned with chevron-SVG separator.
- [ ] Footer matches §8 exactly (phones, links, columns).
- [ ] All copy is German.
- [ ] Font sizes are only from the §4 scale.
- [ ] Page renders standalone (no external CSS/JS/font/icon dependencies).

---

## 10 · Common drift traps (do not repeat)

- ❌ Short token names / linking the stylesheet but using `--teal`. ✅ `--color-*` only.
- ❌ Body text at `17px`/`15px` or in `--color-graphite-700`. ✅ `1rem` in `--color-graphite-800`.
- ❌ Overline kicker in teal. ✅ `--color-graphite-600` (light) / `--color-mint` (dark).
- ❌ Dark CTA/banner in `#000`/`#111`. ✅ `var(--color-teal-900)` or `var(--gradient-brand)`.
- ❌ `.btn--primary` / `--ghost` / `--danger`. ✅ `.btn-primary` / `.btn-secondary` / `.btn-proceed` / `.btn-white`.
- ❌ FAQ question at `1rem`/600. ✅ `1.125rem`/700.
- ❌ Generic icon badge at `0.625rem`. ✅ `var(--radius-lg)` (0.625rem only for `.nfs-card-icon`).
- ❌ Inventing footer columns or phone numbers. ✅ Copy §8 verbatim.
