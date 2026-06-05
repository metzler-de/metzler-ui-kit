Read the file index.html in this folder. It is a complete Metzler UI Kit 
built in React. Extract everything and generate a file called 
`metzler-design-system.md` with the following sections:

1. **Overview** — what this design system is, who it's for, stack used

2. **Color Tokens** — every color with: token name, hex value, RGB, 
   exact usage rule. Group by: Teal Tones, Red Tones, Brand, Green, 
   Yellow, Graphite Surfaces, Graphite Text, Graphite Overlays, Accent.

3. **Border Radius Tokens** — all 5 tokens with name, rem value, 
   which components use them

4. **Typography** — font family, all font sizes used in components, 
   weights and where they apply

5. **Spacing & Sizing** — rem scale reference, button heights 
   (lg/md/sm), padding values

6. **Components** — for each component include:
   - Class names and all variants
   - All states (default, hover, active, disabled)
   - Exact CSS (copy-paste ready)
   - When to use / when NOT to use
   
   Components to cover: Buttons (primary, secondary, proceed, 
   dark, dark-outline, block), Navigation Arrows (btn-nav), 
   Pagination (listing-btn), Breadcrumbs, Textfield, Checkbox, 
   Radio Button

7. **Rules** — non-negotiable design rules:
   - Always rem, never px
   - Never hardcode hex — use token names
   - Red never on CTA buttons
   - Dark buttons only on dark/hero backgrounds
   - Icon source (always from Icons page, never custom SVG)
   - Border widths per component type

8. **Usage for Claude AI** — a short paragraph explaining how a 
   developer should use this file as Claude context

Keep it dense and precise. Developers will paste this into Claude AI 
as project context — every rule must be unambiguous. No filler text.
Save the file to the same folder as index.html.
