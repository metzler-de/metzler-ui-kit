# Best practice: Category / product listing page (PLP)

**Stand: 01.10.2026.**

- Sources were opened on that date, and numbers are quoted as the source states them.
- The Metzler current state comes from a live check of these pages:
  - https://edelstahl-tuerklingel.de/briefkasten (80 articles)
  - /tuerklingel (87)
  - /paketboxen (72)
  - /tuersprechanlagen (41)
- All four list 24 products per page.
- A redesign of /tuersprechanlagen already exists locally in `~/Documents/Claude/Projects/Category page/`. It adds a sort control, a price filter, facet counts and a 3D badge.

---

### 1. Filter shared attributes; don't split them into sub-categories
- **Why:** "75% of our benchmark sites fail to get this right." Filters solve it "for most users". https://baymard.com/blog/ecommerce-over-categorization
- **Example:** https://www.hornbach.de/c/eisenwaren/briefkaesten/S23225/ has only 3 sub-categories. Colour, dimensions and Ausführung are filters.
- **Metzler, now:** /briefkasten starts with sub-category tiles ("Einfamilien Briefkasten 77", "Standbriefkästen 56", "Paketboxen 72"). They overlap heavily: 77 of 80 are "Einfamilien".
- **Metzler, recommended:**
  - Keep only real product types as tiles (Wandbriefkasten, Standbriefkasten, Briefkastenanlage, Paketbox).
  - Make Montageart, Fächer and Zeitungsfach filters.

### 2. Small catalogue → no intermediate category pages
- **Why:** "31% of participants on test sites with intermediary category pages struggled to reach the product list." https://baymard.com/research-articles/dtc-avoid-intermediary-category-pages
- **Metzler, now:** product cards follow the tiles on the same page. OK.
- **Metzler, recommended:** never build a tiles-only page for 40–90 products.

### 3. Offer the essential filter types, including price
- **Why:** "only 43% of our benchmark sites offer all of the key filter types". 12% have no price filter, and 53% have no rating filter. https://baymard.com/blog/5-essential-filters
- **Example:** the Hornbach Briefkästen page filters by Preis, Marke, Grundfarbe, Breite, Höhe, Tiefe and Ausführung.
- **Metzler, now:**
  - **No price filter** on any category.
  - No rating filter.
  - No dimension filters on Briefkasten, though dimensions matter for C4 letters and pillar mounting.
- **Metzler, recommended:**
  - Add a price slider with buckets.
  - Add "4 Sterne & mehr".
  - Add Breite/Höhe/Tiefe ranges.
  - Use "Serie" (XDM10/VDM10/SDM10) instead of "Marke" where the brand is always Metzler.

### 4. Promote the top 4–6 filters as a visible bar
- **Why:** "61% of sites don't promote filters in the product list". Promoted filters should also stay in the full list. https://baymard.com/blog/promoting-product-filters
- **Example:** Hornbach desktop shows a bar (Verfügbarkeit, Preis, Marke …) plus "Alle Filter".
- **Metzler, now:** every filter, and even the sort, sits inside a **collapsed "Filter" panel**.
- **Metzler, recommended:** keep the panel always visible on desktop, or promote a bar. Examples:
  - Briefkasten: Farbe, Montageart, Fächer, Preis.
  - Türklingel: Klingeltaster, Farbe, Beleuchtung, Montageart.
  - Sprechanlagen: System (2-Draht/IP), Taster, Türöffner.

### 5. Show the result count per filter value, and make it correct
- **Why:** counts like "Blue (34)" give users confidence before clicking. https://baymard.com/blog/ecommerce-filter-ui
- **Example:** Hornbach shows "Edelstahl (30)", "Anthrazit (17)".
- **Metzler, now:**
  - Counts are shown, but they are **wrong**: Anthrazit "(40)" gives 53 articles, Schwarz "(31)" gives 34. The cause is colour-variant articles (checked Sept 2026).
  - Single-value facets and duplicate values ("Edelstahl" / "V2A Edelstahl (1.4301)") persist.
- **Metzler, recommended:**
  - Count parents, not variants.
  - Merge duplicate material values.
  - Hide facets that have only one value.

### 6. Multi-select with checkboxes; help text where the term is technical
- **Why:** 14% of sites don't allow multiple selections. https://baymard.com/blog/ecommerce-filter-ui
- **Metzler, now:**
  - The Sprechanlagen "System" filter already explains its options ("IP-System … Ideal für Neubauten" / "BUS-System … Perfekt zum Modernisieren"). Good.
  - No such help text on Türklingel "Spannung", "LED-Spannung" or "Kopfform".
- **Metzler, recommended:** add an info icon with a kit tooltip to every technical facet.

### 7. Applied-filter chips above the results; filter state in the URL
- **Why:** "28% of sites … don't display an overview at all" (20% in the 2025 benchmark). https://baymard.com/blog/how-to-design-applied-filters
- **Example:** Hornbach shows an "Edelstahl" chip and the URL `?f.fixgrundfarbe000=Edelstahl`.
- **Metzler, now:** filter URLs compose as paths (`/tuersprechanlagen__2-taster__anthrazit`). Whether chips are shown was not verified on every category.
- **Metzler, recommended:** add removable chips plus "Alle zurücksetzen", and keep the SEO-friendly path URLs.

### 8. Sort by price, rating, bestseller and newest
- **Why:** "64% of desktop sites don't offer all four of these sort types." https://baymard.com/blog/essential-sort-types
- **Example:** https://www.otto.de/suche/briefkasten/ offers "Topseller, Niedrigster Preis, Höchster Preis, … Neuheiten, Bewertungen".
- **Metzler, now:** "Sortierung" offers only "Standard" and "Bestseller", hidden in the filter panel.
- **Metzler, recommended:**
  - Put a visible sort dropdown on the results line.
  - Options: Beliebtheit, Preis aufsteigend, Preis absteigend, Beste Bewertung, Neuheiten.
  - The header search API already supports price sorting, so the logic exists.

### 9. Consistent product cards: rating with count, key attribute, delivery
- **Why:**
  - "64% of sites fail to adequately present information in product listings." https://baymard.com/blog/list-item-design-ecommerce
  - Users prefer 4.5★ from 57 ratings over 5★ from 4. https://baymard.com/blog/user-perception-of-product-ratings
- **Examples:**
  - Hornbach cards show "HxBxT 362/322/100 mm" and a rating count.
  - Otto cards show "bis Di., 6. Okt. bei dir".
  - Frabox cards show "nur 2 - 3 Werktage" (see `../competitors.md`).
- **Metzler, now:**
  - Cards show stars with count (e.g. Siebert (739)), "ab" price, swatches "+5 weitere" and a "Top bewertet" badge. Good.
  - **No delivery info** on cards.
  - **No key dimension** on cards.
- **Metzler, recommended:**
  - Add one line "Lieferung ca. 2–4 Werktage" (or the earliest date).
  - Add one key attribute per category: B×H×T for Briefkasten, System for Sprechanlage.
  - Add a "3D-Vorschau" or "Gravur inklusive" badge where true.

### 10. Several thumbnails per card (hover or swipe)
- **Why:** "Always Provide 3 or More Product Thumbnails in Product Lists … (80% Don't)". https://baymard.com/blog/current-state-product-list-and-filtering
- **Metzler, now:** a second image on hover only.
- **Metzler, recommended:**
  - Use image 1 for the product, image 2 for the mounted/context shot, image 3 for an engraving close-up.
  - On mobile, make them swipeable.

### 11. "Mehr laden" instead of pagination
- **Why:** "Load More" generally performs best. Load "50–100 products at once for spec-driven sites" on desktop, and 15–30 on mobile. https://baymard.com/blog/number-of-items-loaded-by-default
- **Metzler, now:** 24 per page, numbered pages (`_s2`) with "Gehe zu Seite".
- **Metzler, recommended:** load 48 or more on desktop, then a "Weitere Produkte laden" button. Keep `_s2` URLs for crawling.

### 12. Return to the same scroll position after viewing a PDP
- **Why:** on 13% of sites users are returned to the top of the list. Use `history.pushState()`. https://baymard.com/blog/return-same-place
- **Metzler, now:** not verified.
- **Metzler, recommended:** test this with AJAX pagination and filters active.

### 13. Keep promo banners out of the grid
- **Why:** an ad inside a list makes users "interpret it as the end of the list". https://baymard.com/blog/avoid-these-ecommerce-graphics
- **Metzler, now:** inline USP banners appear inside the grid ("Original Metzler Briefkästen – Langlebig & wetterfest").
- **Metzler, recommended:** if a banner stays, make it card-shaped and clearly a promo. Better: put USPs in a slim strip above the grid.

### 14. Guided selling where choice is technical
- **Why:** this is competitive evidence, not a benchmark. Siedle, DoorBird, Nuki, Ring and ZaWo-Tec all put a finder before the product list. See `../competitors.md` §1.7–1.14.
- **Metzler, now:**
  - The Kaufberater ("Finden statt Suchen") exists only on /tuersprechanlagen.
  - Known issues: the step count jumps and the model counts are inconsistent.
- **Metzler, recommended:**
  - Add short finders (3–4 questions) for Briefkasten (Montageart, Fächer/Parteien, Zeitungsfach, Paketfach?) and Türklingel (Parteien, Unterputz/Aufputz, Beleuchtung).
  - Show a live "Aktuell passen X Modelle" count.

### 15. Category copy: current, consistent, short above the grid
- **Why:** there is no verified benchmark for intro text. The rule follows from NN/g's credibility factor "comprehensive, current" content. https://www.nngroup.com/articles/trustworthy-design/
- **Metzler, now:**
  - The SEO text below the grid is outdated ("über 1.000.000 Kunden", "2023 + 2024 von ntv"), while the homepage says 2 Mio. and four years.
  - The left column on /tuerklingel shows an ntv box "für Briefkästen".
- **Metzler, recommended:**
  - Use one source of truth for claims.
  - Keep the intro to 1–2 sentences above the grid.
  - Put the long FAQ below the grid.
  - Show only awards that match the category.
