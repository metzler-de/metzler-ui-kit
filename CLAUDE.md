Claude Design System Instructions
Unit Conversion: Always Use REM
All measurements must be expressed in rem units, never pixels. Use a base of 16px = 1rem for conversions.
Apply this rule to:

Font sizes
Line heights (when using fixed values)
Borders and border widths
Border radiuses
Padding and margins
Width and height
Gaps and spacing
Any other size-related property

Conversion reference:

1px = 0.0625rem
2px = 0.125rem
4px = 0.25rem
8px = 0.5rem
12px = 0.75rem
14px = 0.875rem
16px = 1rem
20px = 1.25rem
24px = 1.5rem
32px = 2rem

Important: Even when the user provides values in pixels (e.g., "use 16px font size", "2px border", "8px border-radius"), automatically convert and apply them in rem. Do not output pixel values in the final code.
Example:

User says: "font-size 16px, padding 12px, border 1px, border-radius 8px"
You output: font-size: 1rem; padding: 0.75rem; border: 0.0625rem; border-radius: 0.5rem;

Icons

Always pull icons from the Icons page in the design system, never create custom inline SVGs or use external icon libraries.
This applies to all component icons, including (but not limited to) arrows in buttons, status indicators, navigation icons, and decorative elements.
Reference icons by their exact name as defined on the Icons page.

Design Tokens — Always Use System Values
Never hardcode values. Always reference tokens from the design system for:

Colors — use only colors from the defined color palette (no hex codes, RGB values, or arbitrary colors)
Typography — use only the predefined font styles (no custom font-family, font-weight, or font-size combinations outside the system)
Border radiuses — use only the predefined radius tokens
Borders — use only the predefined border tokens
Spacing — use only the predefined spacing scale where applicable
Shadows — use only the predefined shadow tokens

Workflow

When a component is requested, first identify which design tokens apply.
Convert any pixel values mentioned to rem before writing code.
Reference icons from the Icons page rather than inlining them.
If a requested value doesn't exist in the system, flag it and ask whether to add a new token or use the closest existing one — do not invent values silently.

---

Page Layout Rules — Required on Every Page

Every page built with the Metzler design system must follow these rules. They are not optional and apply regardless of page type (landing, category, product, etc.).

Header — Two-State Sticky Behaviour
Always use the design system header component. The header has two states:
1. Default (top of page): full header visible — logo, full navigation menu ("Alle Kategorien" button), search bar.
2. Sticky (on scroll): compact version sticks to the top of the viewport as the user scrolls down. It must NOT be sticky at page load — only activate sticky behaviour after the user begins scrolling.
Never make the header sticky from the start. Never create a custom header — always use the one from the design system.

Breadcrumbs — Always Left-Aligned
Breadcrumbs must be left-aligned and follow the same horizontal container as the page content. Never centre breadcrumbs. They sit directly below the header and align flush with the left edge of the content container.

Arrows and Carousels — No Step Numbers Above Arrows
Navigation arrows (e.g. carousel prev/next controls) must never show step numbers or slide index counters above or beside them. Arrows are controls only — no numeric labels.

Footer — Always Use Design System Footer
Every page must use the Metzler design system footer component. Never create a custom footer or link to an external one. If the page layout does not yet include a footer, add it.

Content Alignment — One Container, All Elements
All page content (hero sections, text, product grids, banners, etc.) must be constrained to the same horizontal container as the header and footer. This means:
- The container max-width is exactly 100rem (1600px). Use this value for every page without exception — do not use 90rem, 1440px, or any other width.
- Apply consistent horizontal padding inside the container: 1.5rem on mobile, 4rem on desktop. The container itself is centred with margin: 0 auto.
- Every section on the page — header, breadcrumbs, hero text, product grids, banners, footer — uses this same 100rem container. Nothing may be wider or narrower.
- The left edge of body text and section content must align with the left edge of the logo in the header. No section may push content further left or right than the header's content area.
- Hero/banner backgrounds may be full-width (width: 100%), but the text and CTA inside them must still be wrapped in the 100rem container.

Header and Footer — No Direct Padding
The header and footer outer elements must have NO horizontal padding of their own. Each row inside the header and the footer's content area must use an inner .container div that provides the 100rem max-width and responsive padding. This is the only way all content stays aligned across sections.

Never do this:
<header style="padding: 0 30px;">...</header>

Always do this:
<header>
  <div class="container">...</div>
</header>

<footer>
  <div class="container">...</div>
</footer>

Standard container CSS (use exactly this pattern on every page):
.container {
  max-width: 100rem;
  margin: 0 auto;
  padding: 0 4rem;
}
@media (max-width: 48rem) {
  .container { padding: 0 1.5rem; }
}

Page Layout HTML Template
Every page must follow this exact structure. Do not deviate:
<body>
  <header>                          <!-- full width, no padding -->
    <div class="container">         <!-- 100rem max-width, 4rem padding -->
      <!-- logo, nav, search -->
    </div>
  </header>

  <main>
    <section>                       <!-- full width, no padding -->
      <div class="container">
        <!-- breadcrumbs, hero text, content -->
      </div>
    </section>
    <!-- repeat for each section -->
  </main>

  <footer>                          <!-- full width, no padding -->
    <div class="container">
      <!-- footer columns, legal links -->
    </div>
  </footer>
</body>