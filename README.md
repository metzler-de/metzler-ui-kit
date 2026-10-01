# Metzler Design System (UI Kit)

**The only design system for Metzler web work** — styles, tokens, header, footer, components, sections, icons and brand rules.
Current version: **v1.14 · 2026-10-01** (history in [`CHANGELOG.md`](CHANGELOG.md)).

- Claude Design: https://claude.ai/artifact/GmM9m9zSAbikHUorc4dJ3H
- Repo: https://github.com/metzler-de/metzler-ui-kit
- Local: `~/Documents/Claude/Projects/Metzler UI Kit`

## What's in here

| File / folder | What it is |
|---|---|
| `index.html` | **Source of truth.** The rendered kit: tokens, components, sections, header, footer, icons |
| `metzler-tokens.css` | All CSS custom properties. Link it, never copy it |
| `brandbook.html` | Logo, colour, type, imagery rules (Do / Don't) |
| `header/` | Canonical header with the live shop's mega menu (`header/preview.html`, tiles in `header/megamenu/`), sticky + mobile variants |
| `footer/` | Canonical footer (`footer/preview.html`, 1:1 with the live shop) + its payment, TopShop and review images |
| `media/`, `img/`, `Pictures/`, `subcategory_photos/` | Images the kit and header use |
| `FOR-CLAUDE.md` | Page brief: tokens, typography, layout, header, **footer (§14, full HTML/CSS)**, rules |
| `SECTIONS.md` | Ready-made page sections + page blueprints + maintenance protocol |
| `COMPONENTS.md` | Full component catalog |
| `ICONS.md` | All icons as SVG |
| `BRANDBOOK.md` | Text version of the brandbook, for compliance checks |
| `CLAUDE.md` | Rules Claude follows when working in this folder |
| `tools/claude-code/metzler-anschlussschema/` | Claude skill: correct wiring diagrams (Anschlussschemata) as PDF in the kit style; kit section `#anschlussschemata` |

## Use it on a page

Link `metzler-tokens.css` from this kit (the repo is public; live at https://metzler-de.github.io/metzler-ui-kit/). Header: copy `header/preview.html` (thumbnails in `header/pictures/nav/`). Footer: copy `FOR-CLAUDE.md` §14 with the `footer/` assets.

## Claude Design

This kit is mirrored as the **Metzler Design System** in Claude Design: https://claude.ai/artifact/GmM9m9zSAbikHUorc4dJ3H — tokens, brand book, 40 components and sections, header, footer and 193 assets. After changing the kit, re-sync it: ask Claude to "sync the Claude Design system" (`tools/claude-design/build.py` rebuilds the files; `staged.json` holds the uploaded asset ids).

## Change it

1. Change `index.html` first (the rendered kit wins over every `.md` file).
2. Bump `CHANGELOG.version` / `date` in `index.html` and add a section to `CHANGELOG.md`.
3. Sync the affected `.md` exports (see "Maintenance" at the end of `SECTIONS.md`).
4. Commit and push → GitHub Pages updates the live kit in 1–2 minutes.

Do **not** use the old "Metzler Design System" MCP connector — its content is an outdated July 2026 snapshot.
