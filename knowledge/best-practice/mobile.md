# Best practice: Mobile

**Stand: 01.10.2026.** Sources were opened on that date, and numbers are quoted as stated.

**Metzler mobile today**

These come from a live HTML check on 01.10.2026, plus the September 2026 audit for the LCP figures.

- **Viewport:** `width=device-width, initial-scale=1.0, user-scalable=no, … viewport-fit=cover`. Zoom is disabled.
- **Sticky elements:**
  - header
  - PDP tab bar
  - configurator bottom CTA bar (`.fixed-cta-wrapper`)
  - floating filter button (`.filter-top-fixed`)
  - Google rating badge, fixed bottom-right on the PDP
  - Botpress webchat, loaded site-wide
- **Page weight:**
  - Homepage HTML: 1,35 MB uncompressed, 151 KB compressed.
  - PDP HTML: about 2,0 MB.
  - Homepage loads 71 scripts.
- **TTFB:** home 0,34 s, category 0,47 s, PDP 0,68 s.
- **Throttled-mobile LCP (Sept 2026):** home 5,2 s, product 2,8 s. gravuru measured 1,7 s.
- **Images:** srcset and lazyload are used well (266 of 267 images lazy).
- **Layout bug:** `word-break: break-all` on product names breaks German words mid-word.

---

### 1. Hit the Core Web Vitals at the 75th percentile: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1
- **Why:** these are the "good" thresholds, measured at "the 75th percentile of page loads, segmented across mobile and desktop". https://web.dev/articles/vitals
- **Metzler, now:**
  - Lab LCP is 5,2 s on home and 2,8 s on the PDP (throttled).
  - Cloudflare caches nothing (`no-store`, `DYNAMIC`).
- **Metzler, recommended:**
  - Edge-cache anonymous HTML.
  - Move the roughly 413 KB of inline CSS into cacheable files.
  - Defer third-party scripts: chat, Google badge, PayPal messaging.
  - Track CrUX field data per template.

### 2. Treat speed as revenue
- **Why:**
  - Vodafone: a 31 % LCP improvement brought +8 % total sales in an A/B test. https://web.dev/case-studies/vodafone
  - Rakuten 24: +33,13 % conversion rate and +53,37 % revenue per visitor. https://web.dev/case-studies/rakuten
  - redBus (INP work): +7 % sales. https://web.dev/case-studies/redbus-inp
  - Think with Google (37 brands): a 0,1 s gain gave +8,4 % retail conversions. https://www.thinkwithgoogle.com/_qs/documents/9757/Milliseconds_Make_Millions_report_hQYAbZJ.pdf
- **Metzler, recommended:** set a performance budget per kit page: JS ≤ 300 KB compressed, LCP image ≤ 150 KB. Check every new page against it before handoff.

### 3. Allow zoom
- **Why:** zoom is a WCAG 2.1 AA requirement (Resize Text), and the BFSG applies to shops. https://www.ihk.de/freiburg/unternehmen-beraten/recht-steuern/weitere-themen/barrierefreie-webseiten-und-onlineshops-6797892
- **Metzler, now:** `user-scalable=no`.
- **Metzler, recommended:**
  - Remove `user-scalable=no` and any `maximum-scale`.
  - Users need to zoom on engraving previews and spec tables in particular.

### 4. Tap targets at least 7 × 7 mm, ideally about 1 × 1 cm, with spacing
- **Why:**
  - Baymard: a 7 mm × 7 mm minimum. https://baymard.com/blog/button-design
  - NN/g: about 1 cm × 1 cm. https://www.nngroup.com/articles/touch-target-size/
  - 66 % of mobile sites place tappable elements too close together. https://baymard.com/learn/ux-statistics
- **Metzler, recommended:**
  - Make swatches, filter checkboxes, font tiles and configurator toggles at least 44 × 44 CSS px (2,75 rem).
  - Use kit spacing tokens between swatches.

### 5. Sticky purchase bar with breathing room, and no clutter around it
- **Why:**
  - Don't make a sticky add-to-cart full-width. Surround it with white space. https://baymard.com/blog/ecommerce-ux-best-practices
  - A sticky summary keeps "Buy" within reach. https://baymard.com/blog/responsive-upscaling
- **Example:** the Thomann mobile PDP shows a fixed bar with quantity and "IN DEN WARENKORB" after scrolling. https://www.thomann.de/de/harley_benton_hbd120bk_westerngitarre.htm
- **Metzler, now:**
  - The configurator CTA bar is good: thumbnail, "Preis wie konfiguriert", cart button.
  - It competes with the Google badge, the chat bubble, the filter button and the sticky tab bar.
- **Metzler, recommended:**
  - Keep at most one sticky element at the bottom (the CTA bar) and one at the top (a compact header).
  - Hide the Google badge and chat bubble on PDPs while the CTA bar is visible. Open chat from inside the bar or the header instead.

### 6. First screen of the PDP: image, title, rating, price incl. MwSt., availability, CTA
- **Why:** NN/g lists these as PDP must-haves, including "Price, including any additional product-specific charges". https://www.nngroup.com/articles/ecommerce-product-pages/
- **Example:** at 375 × 812, the Thomann PDP shows all of these above the fold, including "Alle Preise inkl. MwSt." and "Sofort lieferbar".
- **Metzler, now:** not measured at 375 px. The parent-page CTA reads "Bitte Farbe wählen", so no direct buy action is possible.
- **Metzler, recommended:**
  - Preselect a colour so the first screen ends in a real CTA ("Gravur gestalten" or "In den Warenkorb").
  - Show the delivery date line in the first screen.

### 7. Image thumbnails, not just dots
- **Why:** "Always Use Thumbnails to Represent Additional Product Images (76% of Mobile Sites Don't)". https://baymard.com/blog/collections/product-page
- **Metzler, now:** the gallery shows "1 / 35" with an "Alle 35 Bilder ansehen" link.
- **Metzler, recommended:**
  - Add a horizontal thumbnail strip under the main image, with a video tile and a "3D" tile.
  - The 3D tile matters: it is the cheapest way to show that 3D exists on mobile.

### 8. Filter tray: labelled "Filter", slides over the results, live "X Ergebnisse anzeigen"
- **Why:**
  - Use a prominent "Show X Results" button and a deliberate apply action on mobile. https://baymard.com/blog/ecommerce-filter-ui
  - Words like "Filter" are understood much better than icons. https://www.nngroup.com/articles/mobile-faceted-search/
- **Example:** on Hornbach mobile, "ALLE FILTER" opens a tray and the button goes from "350 Ergebnisse anzeigen" to "30 Ergebnisse anzeigen". https://www.hornbach.de/c/eisenwaren/briefkaesten/S23225/
- **Metzler, now:** there is a floating filter button. The tray's apply behaviour was not verified.
- **Metzler, recommended:**
  - Make the button "Filter & Sortierung (2)".
  - Use a tray with a live result count on the apply button.
  - Put sort at the top of the tray.

### 9. Applied filters as a horizontal chip row with a truncation cue
- **Why:** this is the Baymard pattern for applied filters on mobile. https://baymard.com/blog/how-to-design-applied-filters
- **Metzler, recommended:**
  - Show the chip row directly under the category title, with a fade edge.
  - Make the last chip "Alle löschen".

### 10. The right keyboard for every field
- **Why:**
  - 54 % of mobile sites fail to invoke optimised keyboards. The numeric keypad's keys are "521% larger". https://baymard.com/blog/mobile-touch-keyboards
- **Metzler, recommended:**
  - PLZ: `inputmode="numeric"`. Hausnummer stays a text field, because of values like "12a" and "3–5".
  - Phone: `type="tel"`.
  - E-mail: `type="email"`.
  - Engraving text: `autocorrect="off" autocapitalize="off" spellcheck="false"`, so autocorrect doesn't "fix" family names. This last point is an inference, not a source finding.

### 11. Collapse sections instead of tabs or sub-pages
- **Why:** https://baymard.com/blog/avoid-horizontal-tabs
- **Metzler, now:** a horizontal tab bar on the PDP, sticky.
- **Metzler, recommended:**
  - Use accordions: Beschreibung, Technische Daten, Montage & Downloads, Bewertungen, Fragen.
  - Keep Bewertungen open by default.

### 12. Avoid sticky chat bubbles and load overlays on mobile
- **Why:**
  - Be cautious with sticky chat elements on mobile. https://baymard.com/blog/ecommerce-ux-best-practices
  - 95 % of mobile sites place distracting ads in primary homepage areas. https://baymard.com/learn/ux-statistics
- **Metzler, now:**
  - Botpress chat is loaded site-wide.
  - The French-shop popup is in the HTML.
  - The cookie banner shows.
- **Metzler, recommended:**
  - Show only one first-visit layer: the consent banner.
  - Never show the French hint to German-language visitors.

### 13. Product names hyphenate; never break mid-word
- **Why:** Metzler-specific bug (audit, Sept 2026). There is no external source.
- **Metzler, now:** `word-break: break-all` on `a.etk-pl-name`.
- **Metzler, recommended:** use `hyphens: auto; overflow-wrap: break-word;` with `lang="de"` on the root.
