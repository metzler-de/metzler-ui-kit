# Best practice: Homepage

**Stand: 01.10.2026.**

- Sources were opened on that date, and numbers are quoted as stated.
- Metzler's current state comes from a live check of https://edelstahl-tuerklingel.de/ on 01.10.2026.
- A rebuilt homepage template exists in `Main page/startseite-template/`.

**Current homepage, briefly**

- **Title:** "METZLER Briefkästen, Sprechanlagen & Türklingeln".
- **Green USP strip (site-wide):**
  - "Original Metzler Qualität seit 2013"
  - "über 2 Mio. zufriedene Kunden"
  - "10 Jahre Metzler Garantie"
  - "Trusted Shops Käuferschutz"
  - "Kauf auf Rechnung"
- **Promos:**
  - "Aktion – 15 % auf Sicherheitstechnik" (01.–31.10.2026)
  - "Brand Weeks … –10 % auf STEINEL"
- **Hero / category grid:**
  - Sprechanlagen tile with an autoplay XDM10 video and a "reddot winner 2026" label.
  - Briefkästen tile labelled "Vergleichssieger".
  - Tiles for Paketboxen, Mülltonnenboxen, Hochbeete, Außenleuchten, Funkklingeln, Briefkastenschilder, Hausnummern, Schriftzüge, Türklingeln.
- **Content blocks:**
  - Intercom block "POWERED BY Hikvision / DESIGNED IN GERMANY".
  - ntv H1 "Deutschlands beliebtester Anbieter für Briefkästen – bereits das vierte Jahr in Folge".
  - About block ("Familienunternehmen seit 2013 … 165 Mitarbeitende").
  - "Haus-Gemälde".
  - Customer photo gallery.
- **Footer:** review slider (4,71 / 36.785) and TopShop badges.
- **No newsletter form.**
- **A French-shop popup** ("Visitez notre boutique française") is in the HTML of every page.

---

### 1. Value proposition in the hero: what you sell and why buy here
- **Why:**
  - The homepage must communicate the "unique value proposition clearly … through a descriptive tagline". https://www.nngroup.com/articles/homepage-design-principles/
  - 42 % of mobile sites don't let users infer what kind of site they are on. https://baymard.com/blog/mobile-ecommerce-search-and-navigation
- **Example:** https://www.thomann.de/de/index.html opens with a value strip (Money-Back, Garantie, "Kostenloser Versand ab 29 €").
- **Metzler, now:** the hero is a grid of category tiles. The value proposition is split between the green strip and an ntv H1 further down.
- **Metzler, recommended:** add a one-line hero claim above the grid, e.g. "Briefkästen, Klingeln & Sprechanlagen vom Hersteller – mit Ihrer Gravur, live in 3D gestaltet".

### 2. Show the breadth of the range: link 40–50 % of product types
- **Why:**
  - 22 % of sites show too narrow a range. Baymard recommends 40–50 % of product types. https://baymard.com/blog/inferring-product-catalog-from-homepage
  - 70 % of test subjects scrolled the entire homepage on arrival. https://baymard.com/blog/mobile-ecommerce-search-and-navigation
- **Example:** Thomann's "Unsere Kategorien" grid.
- **Metzler, now:** 11 category tiles. Good breadth.
- **Metzler, recommended:**
  - Keep the tiles.
  - Order them by revenue and intent (Briefkästen, Sprechanlagen, Türklingeln, Paketboxen first).
  - Put a "N Modelle" count on each tile, as /briefkasten already does.

### 3. No auto-rotating carousels. If you use one: 5 frames or fewer, manual control, first slide broadly relevant
- **Why:**
  - NN/g: "Include 5 or fewer frames"; "Do not auto-forward on mobile". https://www.nngroup.com/articles/designing-effective-carousels/
  - Baymard: 46 % of homepage carousels have UX problems. https://baymard.com/blog/homepage-carousel
  - A deal on a 5-second rotation was visible only 20 % of the time. https://www.nngroup.com/articles/auto-forwarding/
- **Metzler, now:** the hero is a static grid; one tile carries an autoplay video. Fine.
- **Metzler, recommended:**
  - Don't introduce a hero slider for the Aktionen.
  - Give each campaign its own static band.
  - Make the video muted, with a poster frame, and pausable (BFSG; see `landing-page-campaign.md`).

### 4. Promos: specific products or categories; no load-time overlays
- **Why:**
  - 40 % of sites flash an overlay on homepage or category load. https://baymard.com/blog/avoid-these-ecommerce-graphics
  - 55 % use overly aggressive homepage ads. https://baymard.com/blog/ecommerce-navigation-best-practice
- **Metzler, now:**
  - The two promo bands link to real categories. Good.
  - The French-shop popup and the cookie layer stack on first load.
- **Metzler, recommended:**
  - Show the French-shop hint only to visitors whose browser language is French or whose geolocation is France, and as a slim bar, not a modal.
  - Keep no more than 2 promos at once.

### 5. Make tiles obvious and link every product in inspiration images
- **Why:**
  - 51 % of sites don't make hit areas clear.
  - **70 % don't link the products shown in inspirational imagery.**
  - Source: https://baymard.com/blog/ecommerce-navigation-best-practice
- **Metzler, now:** the customer photo gallery and award-gala photos are not shoppable.
- **Metzler, recommended:**
  - Add a "Fassaden-Look" section: a facade photo with hotspots for Briefkasten, Klingel, Hausnummer and Leuchte.
  - Set this up as a "Komplett-Look" with "alles in einer Farbe" (RAL 7016). Cross-category matching is Metzler's unique range advantage.

### 6. Search prominent on the homepage
- **Why:**
  - On homepages, search should be a type-in field, not a link. https://www.nngroup.com/articles/search-visible-and-simple/
  - 22 % of sites don't show it prominently. https://baymard.com/learn/ux-statistics
- **Metzler, now:** an open header field ("Suchen — Türklingel, Briefkasten, Sprechanlage…") with an instant dropdown. Good. See `search-navigation.md` for its quality issues.

### 7. Trust above the fold, consistent and sourced
- **Why:** NN/g's credibility factors include up-front disclosure and "comprehensive, current" content. https://www.nngroup.com/articles/trustworthy-design/
- **Metzler, now:**
  - Strong assets: 36.785 reviews, ntv four years, TopShop, Red Dot.
  - The review score sits only in the footer slider.
  - Customer counts conflict across pages: 2 Mio. here, 1.800.000 on /ueber-uns, 1.000.000 in the category SEO text.
  - "Trusted Shops Käuferschutz" is a text claim. No trustbadge script was found.
  - "Kauf auf Rechnung" depends on Klarna; direct invoice is for Behörden only.
- **Metzler, recommended:**
  - Add a compact rating element in the first screen ("4,7 ★ · 36.785 Bewertungen", linked).
  - Unify the customer count everywhere.
  - Link each claim to its proof (Trusted Shops profile, ntv result, Red Dot page).
  - Word the USPs accurately, e.g. "Rechnung & Ratenkauf mit Klarna".

### 8. Red Dot 2026 deserves a dedicated, linked moment
- **Why:** this is competitive context, not a benchmark. No D2C rival has a comparable design award on an intercom (see `../competitors.md`).
- **Metzler, now:**
  - The award is only an image label on the Sprechanlagen tile.
  - /reddot and /xdm10 return 404.
  - A news article exists: https://edelstahl-tuerklingel.de/news-metzler-xdm10-red-dot-award-auszeichnung
  - /auszeichnungen is stale (ntv "3 Jahre … 2025", no Red Dot).
- **Metzler, recommended:**
  - Add a homepage band "Ausgezeichnet: XDM10 – Red Dot Award 2026", linking to an XDM10 landing page (see `landing-page-campaign.md`).
  - Update /auszeichnungen.

### 9. Explain "Hersteller" and the Hikvision relationship carefully
- **Why:** this follows from NN/g's credibility factor of up-front disclosure. https://www.nngroup.com/articles/trustworthy-design/
- **Metzler, now:**
  - The intercom block says "POWERED BY Hikvision", next to the meta description "Hersteller Direktverkauf".
  - Hikvision kits sell from 285 € at retailers, e.g. https://geizhals.de/hikvision-ip-video-intercom-kit-ds-kis604-s-a2499060.html
- **Metzler, recommended:** if the logo stays, add what Metzler adds: design (Red Dot), engraved nameplate, German support hotline, 2-Draht retrofit, Kaufberater.

### 10. Cut filler; every block needs a job
- **Why:** NN/g found 52 % of homepage space wasted on filler (2013 data, directional only). https://www.nngroup.com/articles/homepage-real-estate-allocation/
- **Metzler, now:**
  - The homepage HTML is 1,35 MB uncompressed, including about 413 KB of inline CSS.
  - It loads 71 scripts.
  - Throttled mobile LCP was 5,2 s in the Sept 2026 audit.
- **Metzler, recommended:**
  - Use this order: hero claim → categories → configurator teaser ("Live in 3D gestalten") → Fassaden-Look → Kaufberater teaser → proof (reviews/awards) → about.
  - Drop or move the gala photos.

### 11. Prioritise PDP speed, but fix the homepage LCP too
- **Why:**
  - In retail, PDP load time is often more important than the homepage. https://www.thinkwithgoogle.com/_qs/documents/9757/Milliseconds_Make_Millions_report_hQYAbZJ.pdf
  - The "good" LCP threshold is 2,5 s. https://web.dev/articles/vitals
- **Metzler, now:** Cloudflare caches nothing (`cache-control: no-store`, `cf-cache-status: DYNAMIC`; Sept 2026 audit).
- **Metzler, recommended:**
  - Cache anonymous HTML at the edge.
  - Move the inline CSS to cacheable files.
  - Make the hero image or video poster the LCP element, with `fetchpriority="high"`.

### 12. Newsletter: earn it, then ask
- **Why:** sites must meet basic trust needs before asking for information (NN/g trust pyramid). https://www.nngroup.com/articles/commitment-levels/
- **Metzler, now:** there is no homepage signup, only a footer link to /newsletter with no incentive text.
- **Metzler, recommended:**
  - Use an inline footer band with a concrete benefit, e.g. "Pflege-Tipps & Aktionen, ca. 1× im Monat".
  - Use double opt-in.
  - No popup.
