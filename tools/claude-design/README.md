# Claude Design sync

Rebuilds the **Metzler Design System** in Claude Design (https://claude.ai/artifact/GmM9m9zSAbikHUorc4dJ3H) from this kit.

- `build.py` — reads `metzler-tokens.css`, `FOR-CLAUDE.md`, `SECTIONS.md`, `COMPONENTS.md`, `ICONS.md`, `BRANDBOOK.md`, `CHANGELOG.md`, `header/` and writes `out/project/…` (tokens.json, README, component previews + READMEs, bundle.css, guidelines, cover, index).
- `staged.json` — every uploaded asset (kit path → Claude Design blob id). New images must be uploaded first and added here.

To sync: ask Claude "sync the Claude Design system". Claude runs `build.py`, uploads new assets, and republishes only the changed files, with the index last.
