# Best practice: Product page (PDP)

**Stand: 01.10.2026.**

- I opened every source on that date. Numbers are quoted as the source states them.
- Baymard figures come from US/EU benchmark testing.
- The Metzler current state comes from a live read-only check of edelstahl-tuerklingel.de on 01.10.2026, using three PDPs:
  - Stella doorbell: https://edelstahl-tuerklingel.de/metzler-tuerklingel-mit-gravur-led-taster-optional-stella
  - Siebert Briefkasten: https://edelstahl-tuerklingel.de/metzler-briefkasten-aus-hochwertigem-stahl-siebert (variant `/?a=29323`)
  - XDM10 Maxior: https://edelstahl-tuerklingel.de/metzler-xdm10-video-tuersprechanlage-mit-austauschbarem-namensschild-2-draht-bus-1-klingeltaster-maxior
- Configurator-specific rules live in `configurator-personalisation.md`. Review rules live in `trust-reviews.md`.

---

### 1. Gallery first: high resolution, zoom, many angles, video
- **Why:** "56% of users' first actions" on a PDP is exploring the images. 25% of sites lack enough resolution or zoom. https://baymard.com/blog/ensure-sufficient-image-resolution-and-zoom
- **Example:** https://www.thomann.de/de/harley_benton_hbd120bk_westerngitarre.htm. On mobile it has a thumbnail strip with video and audio tiles and a "+10" tile.
- **Metzler, now:**
  - Siebert has 35 images and a YouTube video.
  - Stella has 12 images and no video.
  - XDM10 has 7 images and an MP4.
  - Shop images are web-optimised; the largest variant is about 27 KB.
- **Metzler, recommended:**
  - Serve at least 1600 px zoomable images.
  - Give every PDP at least 1 video (installation or engraving close-up).
  - On mobile, show a thumbnail strip, not dots.

### 2. At least one in-scale / in-context image
- **Why:**
  - "42% of users will attempt to gauge the overall scale and size of a product from its product images." https://baymard.com/blog/in-scale-product-images
  - 37% of sites don't provide one (2026 benchmark). https://baymard.com/blog/current-state-ecommerce-product-page-ux
- **Example:** https://www.ikea.com/de/de/p/billy-buecherregal-weiss-90401932/. The dimensions are in the product name, and the page has a dedicated "Maße" section.
- **Metzler, now:** customer photo galleries exist (/tuerklingel-galerie, homepage gallery). Whether every PDP has a scale shot was not checked systematically.
- **Metzler, recommended:**
  - Image 2 or 3 of every product: mounted on a facade or gate, with a hand or door frame for scale.
  - Mailboxes: an A4/C4 letter going in.
  - Doorbells: shown beside a standard light switch.

### 3. Callouts on images for invisible qualities
- **Why:** "52% of sites don't use descriptive text or graphics for their top-selling products." https://baymard.com/blog/product-images-descriptive-text
- **Metzler, now:** some images have German marketing text and award badges burnt in. That is unstructured and can't be translated or reused.
- **Metzler, recommended:**
  - Add 1–2 info-graphic images per product, built from the kit, not burnt into photos.
  - Content: "V2A Edelstahl 1.4301", plate thickness, engraving depth, IP rating, "wetterfest".

### 4. One-column spec table, grouped, with a key-spec summary next to the buy box
- **Why:** "50% of e-commerce sites have spec sheet designs that are difficult for users to scan". "Only 3% of sites use a summary to highlight the most critical product specs." https://baymard.com/blog/spec-sheet-scannability
- **Example:** the Thomann PDP above. It has key bullets near the price and a full attribute table below.
- **Metzler, now:**
  - XDM10 has a "Technische Details" tab.
  - Siebert's specs contradict each other: the header and table give 10,5 cm depth, but the description says "370 x 370 x 85 mm".
- **Metzler, recommended:**
  - Put 4–6 key specs under the price: B × H × T, Material, Montageart, Einwurf (C4?), Taster count or System.
  - Group the full table under headings (Maße / Material / Elektrik / Lieferumfang).
  - Generate the specs from one data source so the description cannot contradict them.

### 5. Price block: "inkl. MwSt." plus shipping info, legally and visibly
- **Why (law):** § 6 PAngV. https://www.gesetze-im-internet.de/pangv_2022/__6.html
- **Why (UX):** "64% of users looked for shipping costs on the product page." 43% of sites show none. https://baymard.com/blog/show-shipping-costs-on-product-pages
- **Example:** https://www.obi.de/p/8390452/burg-waechter-briefkasten-modena-3857-edelstahl shows "inkl. 19 % MwSt. … Versandkostenfrei" right under the price.
- **Metzler, now:**
  - Parent pages show "inkl. 19% USt., zzgl. Versand" plus "Lieferung: Gratis Versand · ab 99 €". Good.
  - XDM10 says "Versandkostenfreie Lieferung".
- **Metzler, recommended:**
  - Keep it.
  - Use one wording for all products: "inkl. 19 % MwSt. · versandkostenfrei ab 99 € (DE/AT), sonst 4,95 €".
  - Show bulky-goods surcharges (DPD Sperrgut from 29 €) on the PDP before the cart.
  - Grundpreis (§ 4 PAngV) applies only to goods sold by weight, volume, length or area. It is not needed for piece goods like doorbells, but check any goods sold by the metre.

### 6. Delivery as a date, with production time for engraved goods
- **Why:** "41% of sites in our benchmark didn't provide the delivery date". Users stall when given only a shipping speed. https://baymard.com/blog/shipping-speed-vs-delivery-date. That finding comes from checkout testing; applying it to the PDP is an inference.
- **Examples:**
  - OBI PDP above: "ca. 3 Tage Lieferzeit · Bestelle bis 13:00 Uhr" with a countdown.
  - Letterman: "bis 12 Uhr … taggleicher Versand". https://www.letterman.de/products/briefkasten-letterman-6-inkl-gravur-led-licht
- **Metzler, now:**
  - Parent pages: "Sofort verfügbar".
  - Variant pages: "Versanddatum 05.10.2026 - 07.10.2026". That is a ship date, labelled as such, with a DE-only popover.
- **Metzler, recommended:**
  - Show the estimated **delivery** date already on the parent page, e.g. "Lieferung voraussichtlich Mi., 8.10. – Fr., 10.10." (ship date + carrier days).
  - For engraved items, add "inkl. Gravur-Fertigung".
  - Show a cut-off time if production allows it.

### 7. Rating and count directly under the title, linked to a distribution
- **Why:**
  - "53% of users during testing actively sought out the negative reviews".
  - 43% of top sites have no ratings-distribution UI.
  - Source: https://baymard.com/blog/user-ratings-distribution-summary
- **Example:** https://www.ikea.com/de/de/p/billy-buecherregal-weiss-90401932/. It shows "4.6 von 5 … Alle Bewertungen: 2911" beside the title.
- **Metzler, now:**
  - Stella shows 5,0 (147) with a distribution.
  - Siebert shows 5,0 (739) with a distribution, star filters (`?btgsterne=`) and customer photos. Very good.
  - **XDM10 shows no reviews at all.**
- **Metzler, recommended:**
  - Keep the pattern.
  - For products with no reviews, show the shop rating ("4,7 ★ aus 36.785 Shop-Bewertungen") clearly labelled as shop reviews, never as product reviews.
  - Start review collection for XDM10.

### 8. D2C: link to independent proof
- **Why:** "62% of DTC users" said they would look for third-party reviews; 29% actually left the test site to find them. https://baymard.com/blog/user-reviews-dtc
- **Metzler, now:**
  - The Siebert hero carries a vergleich.org seal.
  - **The XDM10 PDP does not mention Red Dot 2026.** A `.reddot-col` CSS rule exists but nothing uses it.
- **Metzler, recommended:**
  - Put award badges in the buy box: Red Dot on XDM10, ntv on mailboxes.
  - Link each badge to its source: red-dot.org, the ntv/DISQ result page, the Trusted Shops profile.

### 9. FAQ written by the shop plus community Q&A
- **Why:** "70% of sites don't have the ideal combination of both site-authored FAQs and community-driven Q&As". When a Q&A was available, 40% of test subjects used it. https://baymard.com/blog/product-page-faq-and-qa
- **Metzler, now:**
  - "Häufige Fragen zum Produkt" exists.
  - "Frage zum Artikel" is a private contact form, so answers are never published.
- **Metzler, recommended:**
  - Publish answered questions (with consent) as a Q&A list.
  - Seed it with the top support topics: Verkabelung, Bohrschablone, Gravur-Schriften, Pflege Edelstahl, 2-Draht vs IP.

### 10. Stacked collapsible sections instead of horizontal tabs
- **Why:** horizontal tabs "performed poorly over many years of large-scale testing" yet are still used by 29% of sites. https://baymard.com/blog/avoid-horizontal-tabs
- **Metzler, now:** horizontal tabs on all three PDPs (Beschreibung / Bewertungen / Befestigung / Downloads / Frage zum Artikel), with a sticky tab bar.
- **Metzler, recommended:**
  - Desktop: stacked, expanded sections with a sticky anchor nav.
  - Mobile: accordions.
  - Content in tabs is skipped.

### 11. Separate "Alternativen" and "Passendes Zubehör" modules
- **Why:** only 42% of sites offer both kinds. 58% offer one, or mix both in the same element. https://baymard.com/blog/product-page-suggestions
- **Metzler, now:**
  - Stella and Siebert have "Passende Briefkästen / Hausnummern … / Ähnliche Artikel". Good.
  - XDM10 has only "Ähnliche Artikel". It has no accessories module (Innenstation, Netzteil, Türöffner).
- **Metzler, recommended:**
  - Every PDP gets an "Passend dazu" module (required or compatible parts) and a "Ähnliche Modelle" module.
  - Intercoms: show "Für den Betrieb benötigt" separately from optional items.

### 12. Returns and warranty linked on the PDP, stated precisely
- **Why:** "42% of sites don't display or link to return information on the product page" (44% in the 2026 benchmark). https://baymard.com/learn/ux-statistics
- **Example:** https://www.thomann.de/de/harley_benton_hbd120bk_westerngitarre.htm shows "30 Tage Money-Back-Garantie · 3 Jahre Thomann Garantie" in the buy box.
- **Metzler, now:**
  - "10 Jahre Metzler Garantie" sits in the USP list on every PDP, including XDM10.
  - But the Garantieerklärung covers only "Durchrostung" on Metzler-brand products for DE/AT consumers. https://edelstahl-tuerklingel.de/metzler-garantieerklaerung
- **Metzler, recommended:**
  - Make the label say what it covers, e.g. "10 Jahre Garantie gegen Durchrostung".
  - On electronics, show the actual warranty or Gewährleistung terms.
  - Link the Widerrufsrecht summary, and mark personalised items as excluded (see `cart-checkout.md`).

### 13. Downloads as a visible block, not hidden in a tab
- **Why:** this is a competitive norm rather than a benchmark number.
  - Frabox PDPs have Bohrschablone, Anschlussanleitung and Montageanleitung.
  - Knobloch has a "Montagehilfen" tab.
  - Burg-Wächter has an "Anleitungen / Videos" tab.
  - See `../competitors.md`.
- **Metzler, now:** XDM10 has a Downloads (8) tab; Siebert has Downloads (1) plus a GPSR PDF.
- **Metzler, recommended:**
  - Add a "Montage & Downloads" section: file type and size (the shop already shows "Deutsch · 172 KB"), Bohrschablone, wiring diagram (see `connection_schemes`) and installation video.
  - Link it from the buy box ("Montageanleitung ansehen").

### 14. Merchant-listing structured data that is correct
- **Why:** Product/Offer markup makes pages eligible for merchant-listing experiences. Google recommends adding shipping and returns data. https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- **Metzler, now:** JSON-LD carries gross prices. **But listing microdata has ×1000 `itemprop="price"` bugs**, for example `content="89989.00"` for 89,99 €.
- **Metzler, recommended:**
  - Fix the microdata.
  - Add `shippingDetails` and `hasMerchantReturnPolicy`.
  - Mark up only reviews that are visible on the page.

### 15. Personalisation entry visible next to the price, not below the fold
- **Why:** customisation links should be "positioned near the content they relate to" and "well-named". https://www.nngroup.com/articles/customization/
- **Example:** https://www.apple.com/de/shop/buy-airtag/airtag. "Personalisiere dein AirTag mit einer kostenlosen Gravur" sits in the buy box.
- **Metzler, now:**
  - On the parent page the cart button reads "Bitte Farbe wählen" and opens a colour sidebar.
  - 3D appears only after choosing a colour variant.
  - "Jetzt anpassen" exists.
- **Metzler, recommended:**
  - Show the engraving input and its live preview on the parent PDP, with a default colour preselected.
  - Never make the main CTA a "please choose" instruction.
