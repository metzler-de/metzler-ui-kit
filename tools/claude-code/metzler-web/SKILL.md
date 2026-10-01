---
name: metzler-web
description: Build or change any Metzler web UI — pages, sections, components, landing pages, product/category pages, configurators, cart, emails or prototypes for edelstahl-tuerklingel.de, metzlergmbh.de or Metzler devices — exactly on the Metzler UI Kit, with real shop data and a research-first brief. Also use when syncing the kit into Claude Design or refreshing shop knowledge.
---

# Metzler web work

Everything lives in one folder: **`~/Documents/Claude/Projects/Metzler UI Kit`** (below: `KIT`). Read files there directly; never ask the user to paste the design system, and never use the old "Metzler Design System" MCP connector or `~/Documents/Claude3 Code Metzler UI Kit`.

| Need | Read |
|---|---|
| Rules, file map | `KIT/CLAUDE.md`, `KIT/README.md` |
| Tokens | `KIT/metzler-tokens.css` (link it; never paste a copy) |
| Page brief, typography, layout, header + footer code | `KIT/FOR-CLAUDE.md` (footer = §14, copy 1:1) |
| Ready-made sections + page blueprints | `KIT/SECTIONS.md` |
| Components (HTML + CSS) | `KIT/COMPONENTS.md`; rendered truth: `KIT/index.html` |
| Icons (inline SVG) | `KIT/ICONS.md` |
| Brand rules (logo, Do/Don't) | `KIT/BRANDBOOK.md` |
| Header (canonical, matches live shop) | `KIT/header/preview.html` (+ `preview-sticky.html`, `preview-mobile-sticky.html`, `preview-megamenu.html`) |
| Products, prices, specs, colours | `KIT/knowledge/products.md` → `KIT/knowledge/products/<category>.md`; exact data: `KIT/knowledge/products.json` |
| Shop structure, services, tone of voice | `KIT/knowledge/website.md` |
| Competitors | `KIT/knowledge/competitors.md` |
| Best practice per page type | `KIT/knowledge/best-practice/<page-type>.md` |

## 1 · Research and brief first (new pages and new sections)
1. Read `knowledge/website.md`, the matching `knowledge/best-practice/<page-type>.md`, `knowledge/competitors.md` and the product data for the products involved.
2. If the brief needs it, look at 2–3 current best-in-class examples on the web.
3. Write a one-screen brief before building: goal, sections (from `SECTIONS.md` blueprints first), kit components used, real products/prices used, 2–3 references and why, and a **"done when…"** list (3–6 checkable points). Ask the user to confirm it (AskUserQuestion) unless they said to just build.

## 2 · Build on the kit only
- `<link>` `KIT/metzler-tokens.css` (relative path or copy step at build time; GitHub Pages is off, the repo is private). Only kit tokens, rem only, `var(--font-family)`.
- Header: copy `KIT/header/preview.html` 1:1 (logo = `header/logo.svg` as `<img>`, icons as in the file). Footer: copy `FOR-CLAUDE.md` §14 1:1 with `KIT/footer/` assets. Never re-implement them.
- Sections from `SECTIONS.md`, components from `COMPONENTS.md`. Reuse the closest existing piece; if something truly doesn't exist, ask instead of inventing a value.
- German copy in the shop's voice (Sie, „ab 899,00 €“, „inkl. MwSt., zzgl. Versand“). Prices, Art.-Nr., dimensions (B × H × T cm), colours and surcharges only from `knowledge/products.json` or the live product page.
- No hover lift / translate on hover. Cards `radius-lg`, buttons `radius`.
- If `knowledge/products.json` is older than 14 days or misses a product, refresh it (`KIT/tools/shop-data/README.md`) or read the live product page with curl.

## 3 · Check before saying done
- Screenshot desktop 1440 px and mobile 390 px; compare with the user's reference and the "done when…" list; fix, then report.
- Checklist: kit header/footer unchanged · tokens only · rem only · container/inset as in the kit · German copy · real data · no hover lift · images real Metzler photos.
- Always end with the local path and a preview link.

## 4 · When the kit itself changes
1. Change `KIT/index.html` (and the affected `header/`, `footer/`, `.md` exports) — the rendered kit wins.
2. Bump `CHANGELOG.version` in `index.html` and add the entry to `CHANGELOG.md`.
3. Re-sync Claude Design: `cd KIT/tools/claude-design && python3 build.py`, upload new images first (record them in `staged.json`), then publish only changed `out/project/` files to https://claude.ai/artifact/GmM9m9zSAbikHUorc4dJ3H (index `project/design-system.json` last, only if an asset record changed; read it right before).
4. Commit and push the kit — only your own paths; other sessions may have uncommitted work there.
