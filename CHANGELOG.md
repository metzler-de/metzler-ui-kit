# Metzler Design System · Changelog

The kit (`index.html`) is the source of truth. Bump `CHANGELOG.version` in `index.html` and add a section here on every change.

## v1.13 · 2026-10-01
- **Header mega menu synced 1:1 with edelstahl-tuerklingel.de** (`header/preview.html`): all 9 menus with the shop's tiles and links (Briefkästen 11 · Paketboxen 5 · Mülltonnenboxen 6 · Sprechanlagen 8 · Sicherheitstechnik 9 · Türklingeln 7 · Hausnummern 6 · Außenleuchten 7 · Garten 4). Square image box with graphite-100 border, 2-line label, hover = teal border tint + soft shadow (no lift, the old image lift is gone), promo posters for Briefkästen, Paketboxen and Sprechanlagen. Mülltonnenboxen menu was missing and is added. Panel heights match the shop exactly. `header/preview-megamenu.html` regenerated with the same design.
- **Header inset as on the shop:** rows max 1600px, 100px side inset, 50px up to 1400px (was 40px up to 1199px); menu underline without scale animation.
- **Footer rebuilt 1:1 from the live shop** (desktop + mobile, every box within 1px at 1440px and 375px): new font sizes, greys and spacing, shipping/payment tiles 52×33 with the shop's logo files, TopShop badges, rating pill rotating every 5 s through Alle / Trusted Shops / Google / Trustpilot, „Vertrag widerrufen“ on its own last row, mobile layout below 62rem (992px). One file, `footer/preview.html`, shown in the kit and exported in FOR-CLAUDE.md §14; the React footer in `index.html` is gone.
- **New tokens:** `--color-footer-muted` #99A9AA and `--color-footer-line` #1A3E3F (Colors → Footer).
- **Images:** 85 files copied from the shop: `header/megamenu/tiles/` (63), `header/megamenu/posters/` (3), `footer/payment/` (13), `footer/topshop/` (4), `footer/reviews/` (3).
- Version v1.13 everywhere.

## v1.12 · 2026-09-29
- **Fix — Section 01 Support & Kontakt:** the primary card showed a phone number that is not Metzler's and could belong to a stranger. It now shows the Sprechanlagen-Hotline +49 (0) 7121 / 317 7333 (kit preview, code sample, SECTIONS.md). The same number was removed from the "wrong" footer example in FOR-CLAUDE.md.
- Version v1.12 everywhere.

## v1.11 · 2026-09-29
- **New: Section 04c · FAQ · Split („Frage zum Artikel")** from the PDP prototype (Version B, `#sx-frage`): sticky Beratung card („Zum Kundensupport" + Sprechanlagen-Hotline +49 (0) 7121 / 317 7333, Mo–Fr 09:00–16:00 Uhr) next to a flat FAQ list on Paper; FAQ first below 56.25rem. Built from existing tokens only (title H1, card title + number H2, open row Teal 50, 0.25rem accent bar, answer line-height 1.7); chevron = Icons page `chevron-right` rotated, link arrow = `arrow-right`. Exported to SECTIONS.md; PDP blueprint notes 04c as the alternative to 01 + 04.
- Version v1.11 everywhere (kit, tokens, .md exports).

## v1.10 · 2026-09-29
- **Typography — font per OS:** Helvetica Neue on macOS, iOS and Linux (`"Helvetica Neue", Helvetica, Arial, sans-serif`), Arial on Windows (`Arial, "Helvetica Neue", Helvetica, sans-serif`). Replaces the wrong "Arial on all platforms" note. The kit detects the OS (now incl. iOS) and shows the active typeface in the OS banner, the typeface showcase and the Display previews. `metzler-tokens.css`: `html.os-windows { --font-family: var(--font-family-windows); }` plus a one-line detection script; FOR-CLAUDE.md §1/§2 and COMPONENTS.md updated.
- **Colors:** group „GRAPHITE · OVERLAYS" renamed to „BASE · BLACK & WHITE" (True Black, Pure White, White 50 % are not graphite tones; matches „COLORS — BASE" in `metzler-tokens.css`).
- Version v1.10 everywhere (kit, tokens, .md exports).

## v1.9 · 2026-09-28
- **Header icons**: account and cart icons replaced with the live shop's filled icons (person 20.42×21.67, shopping bag 20.37×21.58, 25px, #1A171B, teal on hover) in all header files; standalone copies `header/icon-account.svg`, `header/icon-basket.svg`.
- **Logo** `header/logo.svg` replaced with the live shop file (Metzler_Logo-rot-schwarz.svg): red M-square #d32b25 with white M, wordmark #1b181c. Colors are now fill attributes instead of `.cls-*` classes, so an inlined copy can no longer be recolored by other SVGs on the page.
- **Header synced with the live shop** (`header/preview.html`): trust bar 36px / 12px / 85 % white with „über 2 Mio. zufriedene Kunden“, „Trusted Shops Käuferschutz“, „Kontaktiere uns“, „Zahlung & Versand“ (real links); logo row 70px with no divider, 224px logo box, 791px search field (#DADADA border, 0.2rem radius, 16px text), 25px icons 20px apart; menu 45px, 16px/600, flush to the 100px inset, one #E9E9E9 line; content inset 100px from 1200px width; body offset 151px. Mega-menu thumbnails added in `header/pictures/nav/`.
- **Footer synced with the live shop** (desktop + mobile): Informationen now Auszeichnungen · Geschenkgutschein · Kundenbilder · Stellenangebote · Wir über uns · News · Zahlung und Versand; „Mehr erfahren“ link; shipping partner Hasenauer & Koch (`footer/Choice=hasenauer-koch.svg`) replaces GoGreen; 13 legal links (added Zahlung und Versand, Gesetzliche Gewährleistung, Barrierefreiheit) plus the „Vertrag widerrufen“ button; real hrefs on every link and social icon; copyright „© 2013 - <current year>“; rating values of 28 Sep 2026.
- **FOR-CLAUDE.md §14** replaced: full 5-column static footer export (HTML + CSS, tokens and rem only, assets linked from GitHub Pages). COMPONENTS.md footer chapter updated.
- **Cleanup:** removed everything that is not the design system: pages (2draht-bus/ → own repo `metzler-de/2draht-bus`, konfigurator.html + Images/ + logo.png, product-page, tuersprechanlagen, warenkorb-leer, sprechanlagen-info, sprechanlagen-merkmale, sprechanlagen-images/), superseded docs (BUILD-IN-CLAUDE.md, metzler-design-system.md, generate-design-system-md.md, Design-System-Audit-and-Roadmap.md, Metzler-UI-Kit-Prompt.docx), duplicate Logo.svg, unused Babel package files. All still in git history.
- `xdm10-hero.webp` / `xdm10-detail.webp` moved to `media/`.
- One version everywhere (kit, tokens, all .md exports): v1.9.

## v1.8 · 2026-07-02
- *new:* SECTIONS.md — static HTML/CSS catalog of all 14 sections + page blueprints + maintenance protocol, synced with the SectionsPage
- *improved:* XDM10 Hero breadcrumb now uses the design-system chevron separator (white-opacity dark variant, same spec as About Hero) instead of text "/"
- *improved:* Consistency pass: --color-teal-700 canonicalized to #01292A everywhere (tokens.css, FOR-CLAUDE.md, cssVarMap); all code samples use canonical var(--color-*) names; drifted section samples (Support, Neue Features nfs-*, Slider, FAQ, Product Hero, Feature Detail/Duo) resynced with the rendered components
- *new:* CSS code examples tokenized — all CodeBlock sections now use var(--color-teal), var(--radius), var(--font-family) etc. instead of hardcoded hex/rem values
- *new:* Token documentation — Colors show T.xxx chip + --css-var chip per swatch; Typography shows T.fBody / T.fSm etc.; Border Radius shows T.r / T.rLg etc.
- *new:* JS design tokens object T — central single-source-of-truth for all 37 color, radius, and font-size values; 880+ references across all components
- *new:* metzler-tokens.css — standalone CSS custom properties file for use in any project
- *new:* FOR-CLAUDE.md — design system briefing file for Claude chat, includes all tokens, patterns and rules
- *new:* Cookie consent modal — Metzler-styled dialog with "Alle akzeptieren", "Ablehnen", "Konfigurieren" buttons; interactive with choice feedback
- *new:* Typography OS detection banner — auto-detects macOS/Ubuntu (Helvetica Neue) vs Windows (Arial); shows active font stack
- *improved:* Red Tones — anchored to Metzler Rot (#D42924) as default; Red 50 / 600 / 900 derived from it
- *improved:* Typography: Windows uses Arial, "Helvetica Neue", Helvetica, sans-serif (Arial first by default) — same scale as macOS
- *improved:* Display typography — letter-spacing (-0.04em) removed from Display 1, 2 and 3
- *improved:* Alert variants — left-accent border removed; border removed entirely; background fill only
- *improved:* Modal static preview replaced with cookie consent dialog (centered title, no close button, stacked footer)
- *improved:* Graphite scale — two new tokens added: Graphite 450 (#CCCCCC) and Graphite 850 (#333333)
- *removed:* Color Utilities section removed (text-* / bg-* utility classes)
- *removed:* Product Status Badges section removed
- *removed:* Status column removed from data tables
- *removed:* Review · Photo + Text modal removed
- *fix:* Radio button selected dot — centered with absolute positioning (top/left 50% + translate)

