# Metzler Design System

The official design system documentation for [edelstahl-tuerklingel.de](https://www.edelstahl-tuerklingel.de) — built like Bootstrap docs, hosted on GitHub Pages.

**Live site:** https://metzlerruban.github.io/metzler-design-system/

---

## What's inside

| Section | Contents |
|---|---|
| **Colors** | 22 brand tokens — click any swatch to copy hex |
| **Typography** | Helvetica Neue scale — desktop + mobile |
| **Spacing** | 12 spacing tokens (4px–96px) |
| **Shadows** | 4 elevation levels |
| **Icons** | System icon set with SVG code |
| **Buttons** | 4 variants × 3 sizes × Desktop/Mobile |
| **Form Elements** | Textfield (4 states), Checkbox, Radio |
| **Dropdown** | Select input (Default, Active, Error) |
| **Tooltip** | Dark + Light, Top + Bottom |
| **Alert** | Info, Success, Warning, Error |
| **Badge** | Status + Product badges |
| **Toast** | Auto-dismiss notifications |
| **Tabs** | Tab bar with Active/Disabled states |
| **Notifications** | Inline feedback messages |
| **Product Cards** | Desktop, Tablet, Mobile |
| **Header** | Full site header preview |
| **Footer** | Full site footer preview |

---

## Deployment

This is a **single static HTML file** — no build step needed.

### How to deploy to GitHub Pages

1. Push this repo to `https://github.com/metzlerruban/metzler-design-system`
2. Go to **Settings → Pages**
3. Set **Source** to `GitHub Actions`
4. Push to `main` — the GitHub Action will deploy automatically
5. Your site will be live at `https://metzlerruban.github.io/metzler-design-system/`

### Running locally

Just open `index.html` in Chrome — no server needed.

---

## Figma source

**File:** [www.edelstahl-tuerklingel.de](https://www.figma.com/design/OOPAbqeLgcHSPsmAEh3j1J/)  
**Components page:** node `6041:121800`  
**Design tokens:** Figma Variables → "Metzler colors" (22 tokens), "Spacing Tokens" (12 tokens), "Corner-radius" (7 tokens)  
**Text styles:** 29 styles — Helvetica Neue

---

## Tech stack

- React 18 (CDN)
- Babel Standalone (CDN, for JSX in browser)
- Pure inline styles (no CSS framework)
- Zero build dependencies
