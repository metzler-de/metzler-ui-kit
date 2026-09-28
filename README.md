# Metzler Design System (UI Kit)

**The only design system for Metzler web work** — styles, tokens, header, footer, components, sections, icons and brand rules.
Current version: **v1.9 · 2026-09-28** (history in [`CHANGELOG.md`](CHANGELOG.md)).

- Live kit: https://metzler-de.github.io/metzler-ui-kit/
- Repo: https://github.com/metzler-de/metzler-ui-kit
- Local: `~/Documents/Claude/Projects/Metzler UI Kit`

## What's in here

| File / folder | What it is |
|---|---|
| `index.html` | **Source of truth.** The rendered kit: tokens, components, sections, header, footer, icons |
| `metzler-tokens.css` | All CSS custom properties. Link it, never copy it |
| `brandbook.html` | Logo, colour, type, imagery rules (Do / Don't) |
| `header/` | Canonical header, mega menu, sticky + mobile variants (`header/preview.html`) |
| `footer/` | Footer logos, badges, payment and social icons |
| `media/`, `img/`, `Pictures/`, `subcategory_photos/` | Images the kit and header use |
| `FOR-CLAUDE.md` | Page brief: tokens, typography, layout, header, **footer (§14, full HTML/CSS)**, rules |
| `SECTIONS.md` | Ready-made page sections + page blueprints + maintenance protocol |
| `COMPONENTS.md` | Full component catalog |
| `ICONS.md` | All icons as SVG |
| `BRANDBOOK.md` | Text version of the brandbook, for compliance checks |
| `CLAUDE.md` | Rules Claude follows when working in this folder |

## Use it on a page

```html
<link rel="stylesheet" href="https://metzler-de.github.io/metzler-ui-kit/metzler-tokens.css">
```
Header: copy `header/preview.html`. Footer: copy `FOR-CLAUDE.md` §14 (assets load from `…/metzler-ui-kit/footer/`).

## Change it

1. Change `index.html` first (the rendered kit wins over every `.md` file).
2. Bump `CHANGELOG.version` / `date` in `index.html` and add a section to `CHANGELOG.md`.
3. Sync the affected `.md` exports (see "Maintenance" at the end of `SECTIONS.md`).
4. Commit and push → GitHub Pages updates the live kit in 1–2 minutes.

Do **not** use the old "Metzler Design System" MCP connector — its content is an outdated July 2026 snapshot.
