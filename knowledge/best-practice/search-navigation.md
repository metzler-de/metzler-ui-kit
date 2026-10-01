# Best practice: Search & navigation

**Stand: 01.10.2026.**

- All sources were opened on that date. Numbers are quoted exactly as the source states them.
- The Metzler current state comes from a live check of the header search and /search on 01.10.2026.

**Metzler search today**

- **Header instant search (`metzler_search` plugin v3.3.8):**
  - Endpoint: `/metzler-search-api`. Returns up to 14 hits.
  - Has sorting (Relevanz, Preis auf- und absteigend, Neueste, Beliebtheit).
  - Shows "Letzte Suchen" and hand-picked "Unsere Empfehlungen".
  - Input has `minlength="4"`.
  - **Typos:**
    - Fuzzy matching on typos returns hits with poor relevance: "klingle" gives 21 hits, the first a Klingeltrafo; "briefkastn" gives 25 hits, all Briefkastenanlagen.
    - `/metzler-suggest-api` returns category chips only, and nothing (`[]`) for typos.
- **Full results page (`/search/?qs=`):**
  - "briefkasten" returns 298 articles, but the first hits are BK212 modules and configurator parts (999,00 € and 474,81 €). Siebert is not first.
  - "hausnummer" returns 234 articles, with relevant hits.
  - "klingle" and "briefkastn" return "Leider wurde zu Ihrem Suchbegriff nichts gefunden." with **no suggestions**.
  - Sort options: Standard / Bestseller only.
  - So the header search and the results page disagree.

---

### 1. Always-open search field on desktop, wide enough
- **Why:**
  - On homepages, search should be a type-in field, not a link. https://www.nngroup.com/articles/search-visible-and-simple/
  - 22 % of sites don't show it prominently. https://baymard.com/learn/ux-statistics
- **Example:** https://www.otto.de/ has an open "Wonach suchst du?" field.
- **Metzler, now:** open field with the placeholder "Suchen — Türklingel, Briefkasten, Sprechanlage…". Good.
- **Metzler, recommended:**
  - Keep it.
  - Lower `minlength` to 2–3. "XDM", "SK2" and "LED" are real queries, and a 4-character minimum blocks "Box".

### 2. Autocomplete with query suggestions, at most 10 on desktop and 4–8 on mobile
- **Why:** autocomplete is on 80 % of sites, but "only 19%" get all the implementation details right. https://baymard.com/blog/autocomplete-design
- **Example:** on otto.de, "briefkas" suggests "briefkasten mit zeitungsfach / mit paketfach / mit namensschild / personalisiert …", with the predicted part in bold.
- **Metzler, now:** the dropdown shows products and category chips. It has no query completions, such as "briefkasten mit zeitungsfach".
- **Metzler, recommended:**
  - Add 4–6 query suggestions built from Merkmale: "Briefkasten mit Zeitungsfach", "… anthrazit", "… Standbriefkasten", "… mit Klingel".
  - Show them above the product hits.
  - Highlight the predicted part, not the typed part.

### 3. Typo tolerance, consistent everywhere
- **Why:** "69% of sites don't support autocomplete spelling suggestions for slightly misspelled queries." Some users then abandon the site. https://baymard.com/blog/offer-autocomplete-suggestions-for-misspellings
- **Examples:**
  - On otto.de, "brifkasten" still suggests "briefkasten …".
  - https://www.otto.de/suche/briefkastn/ returns wall mailboxes.
- **Metzler, now:**
  - The instant search is fuzzy but ranks badly.
  - The results page has zero tolerance.
  - The suggest endpoint gives nothing on typos.
- **Metzler, recommended:**
  - Route the results page through the same engine as the instant search.
  - Add "Meinten Sie: briefkasten?" with an automatic correction when there are no exact hits.
  - Rank category-name matches first.

### 4. Synonyms and German domain vocabulary
- **Why:** abbreviation and symbol searches cause problems on "54% of Sites". https://baymard.com/blog/ecommerce-search-query-types
- **Metzler, recommended:** maintain a synonym list. Map at least:
  - Postkasten / Briefkasten
  - Klingelplatte / Klingelschild / Türklingel
  - Gegensprechanlage / Türsprechanlage / Sprechanlage / Video-Klingel
  - Paketkasten / Paketbox / Paketbriefkasten
  - Mülltonnenbox / Mülltonnenverkleidung
  - V2A = 1.4301, V4A = 1.4404
  - Anthrazit = RAL 7016
  - Unterputz = UP, Aufputz = AP
  - 2-Draht = Zweidraht = BUS
  - "mm" / "cm"

### 5. Feature, use-case and compatibility queries
- **Why:**
  - These query types fail on many sites: "Feature" 39 %, "Use Case" 43 %, "Compatibility" 44 %.
  - Overall, "56% of sites fail to adequately support users' search needs."
  - Source: https://baymard.com/blog/ecommerce-search-query-types
- **Metzler, recommended:**
  - Map queries to filtered category URLs, e.g. "klingel 3 parteien" → `/tuerklingel__3-taster`, "briefkasten für C4", "zubehör XDM10".
  - The filter-path URLs already exist (`/tuersprechanlagen__2-taster__anthrazit`).

### 6. Send exact category queries straight to the category
- **Why:**
  - 46 % of sites don't auto-direct exact category queries. https://baymard.com/blog/autodirect-searches-matching-category-scopes
  - On mobile, 72 % don't suggest relevant categories. https://baymard.com/blog/mobile-ecommerce-search-and-navigation
- **Metzler, now:** "briefkasten" lands on a results page of 298 items led by BK212 parts, not on the curated /briefkasten category with Siebert first.
- **Metzler, recommended:** redirect exact category names (Briefkasten, Türklingel, Paketbox, Sprechanlage, Hausnummer, Mülltonnenbox) to their category page, keeping the query visible.

### 7. Keep the query in the field after search
- **Why:** search terms are cleared on 33 % of desktop and 42 % of mobile sites. https://baymard.com/blog/persist-search-queries
- **Metzler, now:** not verified.
- **Metzler, recommended:** keep the query in the field on the results page.

### 8. The no-results page is never a dead end
- **Why:**
  - "nearly 50% of sites fail to provide users with effective ways to recover". https://baymard.com/blog/no-results-page
  - 88 % of mobile sites give no intelligent help. https://baymard.com/blog/mobile-ecommerce-search-and-navigation
- **Example:** a nonsense query on Otto (https://www.otto.de/suche/xqzvwplk%20briefkastenx/) still returns mailbox results.
- **Metzler, now:** "Leider wurde zu Ihrem Suchbegriff nichts gefunden." and nothing else.
- **Metzler, recommended:** show, in this order:
  1. A spelling correction
  2. Category tiles
  3. Bestsellers
  4. "Kaufberater starten"
  5. The hotline and chat ("Wir helfen persönlich: 07121 317 7310")

### 9. Search ranks main products above parts
- **Why:** this follows from the relevance findings above (rules 3 and 5).
- **Metzler, now:** BK212 modules and configurator parts, priced 474,81 € and 999,00 €, outrank the bestselling Siebert (739 reviews).
- **Metzler, recommended:**
  - Boost by sales and reviews.
  - Down-rank items flagged as Ersatzteil, Modul or Zubehör unless the query contains "Ersatz", "Zubehör" or a part number.
  - Hide configurator-only parts from search.

### 10. Navigation visible on desktop; product categories as the top level on mobile
- **Why:**
  - Hiding the main navigation cuts discoverability "almost in half". https://www.nngroup.com/articles/hamburger-menus/
  - 33 % of mobile sites don't make product categories the top-level menu items. https://baymard.com/blog/main-navigation-product-categories
- **Metzler, now:** desktop has a mega menu with poster cards ("Jetzt konfigurieren": Siebert, Bispo Max 2, XDM10).
- **Metzler, recommended:** on mobile, show the product categories as the first menu level, and put service links (Kontakt, FAQ, B2B) below them.

### 11. Mega menu: grouped, hover delay, current scope highlighted
- **Why:**
  - NN/g: the cursor should rest about 0,5 s before the menu opens, and the menu should then appear within 0,1 s. https://www.nngroup.com/articles/mega-menus-work-well/
  - 61 % of sites have no hover delay, and 95 % don't highlight the current scope. https://baymard.com/blog/ecommerce-navigation-best-practice
- **Metzler, recommended:**
  - Group the menu by product type and by need ("Nach Montageart", "Nach Farbe", "Mit Gravur", "Mit 3D-Vorschau").
  - Highlight the active section.
  - Add a 300–500 ms hover intent.

### 12. Breadcrumbs that show the hierarchy, with BreadcrumbList markup
- **Why:**
  - Breadcrumbs show the hierarchy, and the last crumb is not a link. https://www.nngroup.com/articles/breadcrumbs/
  - 65 % of mobile sites have no breadcrumbs on product pages. https://baymard.com/blog/implementing-mobile-hierarchy-breadcrumbs
  - Markup guidance: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- **Examples:** Hornbach mobile shows "Eisenwaren > Briefkästen"; Thomann mobile shows "← Dreadnought Gitarren".
- **Metzler, now:** not systematically verified.
- **Metzler, recommended:**
  - Use the pattern Home › Briefkästen › Wandbriefkästen › Siebert.
  - On mobile, show at least a "← Wandbriefkästen" back-crumb.

### 13. Results-page sort and filters match the category pages
- **Why:** sort-type coverage, from `category-page.md` rule 8. https://baymard.com/blog/essential-sort-types
- **Metzler, now:** the results page sorts by Standard / Bestseller only. The instant search API already supports sorting by price.
- **Metzler, recommended:** give the search results page the same sort and filter set as the category pages, including price.
