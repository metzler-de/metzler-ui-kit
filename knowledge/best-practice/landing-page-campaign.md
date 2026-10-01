# Best practice: Landing pages & campaigns

**Stand: 01.10.2026.**

- All sources were opened on that date. Numbers are quoted exactly as the sources state them.
- This is not legal advice.

**Metzler campaign and landing pages that exist today (live, 01.10.2026)**

- **Live:**
  - /sprechanlagen-info
  - /topshop
  - /auszeichnungen (stale: no Red Dot, ntv only up to 2025)
  - /metzler-geschenkgutschein (25–200 €)
  - /b2b
  - /partnerbetriebe
  - /haus-gemaelde
  - /produktionsprozess
  - /tuerklingel-galerie
  - /Sale (130 Artikel)
  - /sicherheitstechnik (Aktion 15 %, 01.–31.10.2026)
  - /metzler-24v-garten-lichtsystem-steinel
  - /news (including the Red Dot article https://edelstahl-tuerklingel.de/news-metzler-xdm10-red-dot-award-auszeichnung)
- **Return 404:** /reddot, /red-dot, /xdm10, /black-friday, /architekten, /fachhandel, /angebote.
- **Gaps:** there is no product-launch page for XDM10, no seasonal or gift landing page beyond the voucher, and no page for architects or planners.

---

### 1. First screen: value proposition, hero product, primary CTA
- **Why:** users spent about **57 %** of their viewing time above the fold and **74 %** in the first two screens. https://www.nngroup.com/articles/scrolling-and-attention/
- **Example:** https://www.apple.com/de/airpods-pro/ — a launch page with its own sticky sub-nav and a "Kaufen" link.
- **Metzler, recommended:**
  - Use a fixed hero template: product on a façade, a one-line claim, proof (award or rating), and the CTA "Jetzt konfigurieren".
  - Add a sticky sub-nav with Überblick / Technik / Varianten / Kaufen.

### 2. Build an XDM10 Red Dot product page (currently missing)
- **Why:** the award is an independent proof point; D2C shoppers look for third-party evidence (62 %, see `trust-reviews.md`). Rules for using the label:
  - The Basic licence covers the website, social media and PR.
  - Packaging, sales and promotional materials need the **Advanced** licence.
  - The mark must be at least **10 mm** in diameter.
  - Source: https://www.red-dot.org/pd/red-dot-label
- **Metzler, now:**
  - The award appears only as an image label on a homepage tile and in a news post.
  - The XDM10 product page does not mention it.
- **Metzler, recommended:**
  - Create /xdm10. Sections:
    1. Hero
    2. Why it won (the jury criteria text, quoted at most briefly)
    3. Retrofit on 2-Draht ("Nachrüsten ohne neue Kabel")
    4. Variants and prices (XDM10 from 899 €, Pro from 1.299 €)
    5. Kaufberater entry
    6. Downloads
    7. FAQ
  - **Check the licence tier with Red Dot before using the label on campaign or ad pages.**

### 3. Make the page fast: campaign pages are image-heavy
- **Why:** in a Google-published study of 37 brands, a 0,1 s mobile speed gain went with **8,4 %** more retail conversions and **9,2 %** higher order value. https://www.thinkwithgoogle.com/_qs/documents/9757/Milliseconds_Make_Millions_report_hQYAbZJ.pdf
- **Metzler, now:** throttled-mobile LCP was 5,2 s on the homepage (Sept 2026 audit); Cloudflare caches nothing.
- **Metzler, recommended:**
  - Build campaign pages as static, cacheable kit pages.
  - Use WebP/AVIF images.
  - Give video a poster frame and no autoplay on mobile data.

### 4. No auto-rotating sliders for offers
- **Why:** NN/g saw a user fail to find a deal set in 98-point type because the panel kept rotating. https://www.nngroup.com/articles/auto-forwarding/
- **Metzler, recommended:** put one offer per band. If a page has more than 3 offers, it is a category page, not a landing page.

### 5. Disclose terms up front: price incl. MwSt., shipping, delivery time, validity
- **Why:**
  - NN/g recommends up-front disclosure. https://www.nngroup.com/articles/trustworthy-design/
  - § 6 PAngV. https://www.gesetze-im-internet.de/pangv_2022/__6.html
- **Metzler, now:** promo bands state validity ("Gültig vom 01.10. bis 31.10.2026"). Good.
- **Metzler, recommended:** every campaign hero carries, in small text, the validity dates, "inkl. MwSt., zzgl. Versand / versandkostenfrei ab 99 €", and any exclusions (e.g. gravierte Sonderanfertigungen).

### 6. Discounts: refer to the 30-day lowest price
- **Why:**
  - § 11 PAngV. https://www.gesetze-im-internet.de/pangv_2022/__11.html
  - EuGH C-330/23 (26.09.2024): percentage discounts must be calculated from the lowest price of the previous 30 days. https://curia.europa.eu/site/upload/docs/application/pdf/2024-09/cp240152de.pdf
- **Metzler, now:** the Steinel Brand Weeks (–10 %) and Sicherheitstechnik (–15 %) promotions are running.
- **Metzler, recommended:** compute "-X %" from the 30-day low, and never from the UVP, unless the page is clearly labelled as a UVP comparison.

### 7. Show the product at real scale and in context
- **Why:** 42 % of users judge size from images. https://baymard.com/blog/current-state-ecommerce-product-page-ux
- **Metzler, recommended:**
  - Use façade, gate and garden shots in the brand's photo style.
  - Mailbox imagery follows the standing image rules: always the Siebert, white nitrile gloves.
  - Add one shoppable "Komplett-Look" (hotspots) per campaign.

### 8. Repeat proof: rating, review count, verified badge, real customer photos
- **Why:** see `trust-reviews.md` (Spiegel: five reviews raise purchase likelihood by 270 %; verified badge +15 %). https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/
- **Metzler, recommended:**
  - Reuse the product's own reviews, e.g. Siebert 5,0 / 739, with customer photos.
  - If a product has none (XDM10), show the shop rating, labelled as a shop rating.

### 9. Lead into the configurator with a preset, not an empty form
- **Why:** NN/g's "Edit; Don't Design". https://www.nngroup.com/articles/customers-as-designers/
- **Example:** https://www.mymuesli.com/pages/mixer — preset mixes next to "build your own".
- **Metzler, recommended:**
  - Campaign CTAs open the configurator with a preset: colour, a template layout and sample text.
  - Use deep links such as `?farbe=7016&layout=name-nr`.
  - This depends on the save/share URL state described in `configurator-personalisation.md`, rule 9.

### 10. Gift and seasonal pages must respect engraving lead time
- **Why:** 78 % of sites don't show gifting options on the product page. https://baymard.com/blog/current-state-ecommerce-product-page-ux
- **Example:** https://www.manufactum.de/geschenke-c199132/ — a dedicated gift landing page.
- **Metzler, now:** only the voucher page exists (25–200 €).
- **Metzler, recommended:**
  - Build a "Geschenkideen fürs neue Zuhause" page: Einzug, Hausbau, Richtfest.
  - Group products by budget: bis 50 €, bis 150 €, Premium.
  - Show a deadline line: "Für Lieferung bis 24.12. graviert bestellen bis …".
  - Offer the voucher as the fallback.

### 11. B2B and planner page (currently missing)
- **Why:** this is competitor practice (see `../competitors.md`):
  - DoorBird shows net prices and a partner portal.
  - Knobloch accepts Billie invoices.
  - 2N has a "Wie kaufen" page.
  - Siedle offers "Preisbeispiele" PDFs.
- **Metzler, now:**
  - /b2b is a reseller registration that requires a Gewerbenachweis.
  - /partnerbetriebe is a partner search.
  - /architekten and /fachhandel return 404.
- **Metzler, recommended:**
  - Build a "Für Profis" landing page: Installateure, Architekten, Hausverwaltungen, Bauträger.
  - Content: Planungsunterlagen and CAD/Datenblätter, Preisbeispiele for 1–4-Familienhaus, Briefkastenanlagen configurator with quote, Netto-Preise after login, project hotline.

### 12. Accessibility (BFSG) from the start
- **Why:** the BFSG applies to consumer e-commerce services provided after 28.06.2025. The practical standard is EN 301 549 / WCAG 2.1 AA, plus an accessibility statement. Sources:
  - https://www.gesetze-im-internet.de/bfsg/__1.html
  - https://www.ihk.de/freiburg/unternehmen-beraten/recht-steuern/weitere-themen/barrierefreie-webseiten-und-onlineshops-6797892
- **Metzler, now:**
  - The footer has a Barrierefreiheit link.
  - The viewport sets `user-scalable=no`, which blocks zoom and is an accessibility issue.
  - Autoplay video on the homepage.
- **Metzler, recommended:**
  - Allow pinch-zoom.
  - Give every video a pause control and captions or a text alternative.
  - Write alt text for every hero.
  - Keep text contrast at least 4.5:1, using kit tokens.

### 13. Structured data and a clean campaign URL
- **Why:** merchant listings can show price, availability, shipping and returns. https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- **Metzler, recommended:**
  - Use short, permanent URLs (/xdm10, /geschenkideen, /fuer-profis).
  - After a seasonal campaign ends, keep the URL and update the content rather than letting it 404.
  - Add Product markup for featured products.
