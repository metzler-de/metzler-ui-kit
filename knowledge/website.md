# edelstahl-tuerklingel.de — Shop reference for designers

**Stand: 01.10.2026** · verified live (curl of public pages + browser pane, read-only) · Shop: https://edelstahl-tuerklingel.de (JTL-Shop, template "Snackys"/ETK2022, Metzler GmbH, Reutlingen)

Read this before designing any page for the shop. Quotes in „…“ are the exact live German copy. Everything here was seen on the live site on the date above; things that could not be verified are marked **(nicht geprüft)**. Product data (prices, Art.-Nr., colours) lives in `knowledge/products.json` / `products.md`, not here.

---

## 0 · Rules for new designs (derived from the live shop)

| # | Rule |
|---|---|
| R1 | Address the customer with **„Sie“**, always. Never „du“. |
| R2 | Prices are **gross**, German format, `€` after the number with a space: „899,00 €“, „1.490,00 €“. From-prices use lowercase „ab“: „ab 699,00 €“. Always two decimals. |
| R3 | On product/price blocks use the shop's tax/shipping line: PDP „inkl. 19% USt., zzgl. Versand“ (live renders „inkl. 19% USt. , zzgl. Versand“ with a stray space — don't copy the space); footer/asterisk „inkl. gesetzliche MwSt., zzgl. Versand“. Never show a price on PDP/cart without one of these; „Versand“ links to `/zahlung-und-versand`. |
| R4 | Surcharges are shown as „+ 29,01 €“ / „+4,95 €“ next to the option; base price stays „ab …“ until configured, then „Preis wie konfiguriert“. |
| R5 | Product names follow `Metzler <Produkttyp> \| <Merkmal> \| <Merkmal> \| <Modellname>`; colour variants insert the colour before the model: „… \| RAL 7016 Anthrazitgrau \| Colson“. On listing cards the brand is a separate small line („Metzler“) and the name starts with the product type. |
| R6 | Colours are named by RAL/DB code + German name: „RAL 7016 Anthrazitgrau“, „RAL 9016 Verkehrsweiß“, „RAL 9007 Graualuminium“, „DB 703 Eisenglimmer“, „RAL 9005 Tiefschwarz“, „RAL 7012 Basaltgrau“, „Edelstahl Gebürstet“, „Wunschfarbe nach RAL“. Facets use the short family name („Anthrazit“, „Eisenglimmer“, „Wunschfarbe“). |
| R7 | Dimensions always **B × H × T in cm** with comma decimals: „37,00 × 37,00 × 10,50 cm“ (label „Breite × Höhe × Tiefe“). |
| R8 | Trust claims may only be the ones in §3 with the exact wording/numbers; the review numbers change — re-read the footer slider before publishing. |
| R9 | The warranty is „10 Jahre Metzler Garantie“ **against Durchrostung only**, DE + AT, consumers only. Don't write „10 Jahre Garantie auf alles“. Keep it visually separate from „Gesetzliche Gewährleistung“. |
| R10 | Engraving: „Lasergravur“ / „Individuelle Lasergravur“, plates in „V4A-Edelstahl“ (Briefkasten). Promise only what the configurator really offers (font/alignment counts differ per product — see §5). |
| R11 | Do **not** copy the shop's defects into new designs: give users a visible sort + price filter, readable font names, hyphenation instead of `break-all`, one unit („Modelle“ *or* „Artikel“), facet counts that match results, correct microdata. |
| R12 | Brand teal is the top-bar/FAQ colour `#015253` / `#005253` — but take all colours/tokens from `metzler-tokens.css`, not from this file. |
| R13 | Section copy patterns: short benefit headline + one-line explanation („Großzügige Einwurfklappe“ / „Ermöglicht den Einwurf von DIN-A4-Umschlägen …“). CTAs are imperative: „Jetzt konfigurieren“, „Jetzt anpassen“, „In den Warenkorb“, „Mehr erfahren“, „Zu den Angeboten“. |

---

## 1 · Navigation

### 1.1 Header (desktop, 1440 px)

1. **Trust bar** (`.topbar-neu`, bg `#015253`, 12 px, white 85 %), left → right:
   „Original Metzler Qualität seit 2013“ · „über 2 Mio. zufriedene Kunden“ · „10 Jahre Metzler Garantie“ (link → `/metzler-garantieerklaerung`) · „Trusted Shops Käuferschutz“ · „Kauf auf Rechnung“
   Right side links: „Kontaktiere uns“ → `/Kontakt` · „Zahlung & Versand“ → `/Zahlung-und-Versand`.
   Responsive: 1024–1199 px hides claims 4–5; ≤ 1023 px shows only claims 1–2; ≤ 767 px shows claims 2–3 („über 2 Mio. zufriedene Kunden“, „10 Jahre Metzler Garantie“), links hidden.
2. **Main bar**: logo „METZLER“ (→ home) · search field, placeholder „Suchen — Türklingel, Briefkasten, Sprechanlage…“ · account („Anmelden“ dropdown: E-Mail-Adresse, Passwort, „Passwort vergessen?“, „Neu hier? Jetzt registrieren!“) · cart icon with count (side basket: „Bestellübersicht“, „Es befinden sich keine Artikel im Warenkorb.“, „Zur Kasse“, „Zum Warenkorb“).
3. **Category nav** (9 main categories, in this order): Briefkästen · Paketboxen · Mülltonnenboxen · Sprechanlagen · Sicherheitstechnik · Türklingeln · Hausnummern · Außenleuchten · Garten. Narrow viewports get an „Alle“ (hamburger) button; when scrolled the sticky header collapses to a „Kategorien“ button + search.
4. **Sprechanlagen pages only** (category + intercom PDPs) get a second teal service bar: „Sprechanlagen-Hotline 07121 / 317 7333“ · „Termin vereinbaren“ · „Fachhandelspartner“ · button „Metzler FAQ“.

### 1.2 Mega menu

Two `#cat-ul` lists exist in the DOM:
- **Desktop mega menu** `#cat-w #cat-ul > li.mgm-fw` (link class `mm-mainlink`): each main category opens a panel of **level‑2 image tiles** (category photo + name). Three panels carry a promo poster (`aside.mega-poster`, eyebrow / title / features / button „Jetzt konfigurieren“):
  - Briefkästen: „Einfamilien Briefkasten“ / „Metzler Briefkasten aus hochwertigem Stahl“ / „Farbe · Gravur · Befestigung“ → `/metzler-briefkasten-aus-hochwertigem-stahl-siebert`
  - Paketboxen: „Paketbox mit Briefkasten“ / „Metzler Paketbox XL mit Briefkasten“ / „Farbe · Gravur · Befestigung“ → `/metzler-paketbox-xl-mit-briefkasten-paketkasten-rostfrei-personalisiert-mit-gravur-bispo-max-2`
  - Sprechanlagen: „Video-Türsprechanlage“ / „Metzler XDM10 mit austauschbarem Namensschild“ / „Farbe · Klingeltaster“ → `/metzler-xdm10-video-tuersprechanlage-mit-austauschbarem-namensschild-2-draht-bus-1-klingeltaster-maxior`
  - Desktop-only extra tiles: Briefkästen panel also shows **„Paketboxen“** (`/paketboxen`); Sprechanlagen panel also shows **„Briefkastenanlagen Konfigurator“** (`/briefkastenanlage`).
- **Recursive tree** (`header #cat-ul`, `li.categories-recursive-mobile-f`): same level 2 plus **level 3** (with „Zurück“ back links) — used for the off-canvas/mobile menu.

### 1.3 Full category tree (main → sub → sub-sub), URLs relative to https://edelstahl-tuerklingel.de

Listing count = „N Artikel“ on the main category page (parents only).

**Briefkästen** `/briefkasten` (80 Artikel)
- Einfamilien Briefkasten `/exklusiv-briefkasten` · Briefkasten ohne Gravur `/briefkasten-ohne-gravur` · Standbriefkästen `/standbriefkasten-sets` · Briefkasten mit Klingel & Sprechanlage `/briefkasten-funkklingel-sprechanlage` · Mehrfamilien Briefkästen `/briefkasten-zweifamilienhaus` · Unterputz Briefkästen `/unterputz-briefkaesten` · *(desktop only: Paketboxen `/paketboxen`)* · Briefkastenanlagen Konfigurator `/briefkastenanlage` · Briefkastenschilder `/briefkastenschilder` · Briefkastenständer `/briefkastenstaender`
- Ersatzteile & Zubehör `/briefkasten-zubehoer` → Ersatz Gravurleisten & Namensschilder `/briefkasten-ersatz-gravurblenden`

**Paketboxen** `/paketboxen` (72 Artikel)
- Paketboxen mit Gravur `/paketboxen-mit-gravur` · Paketboxen beleuchtet `/paketboxen-beleuchtet` · Paketboxen mit Klingel & Sprechanlage `/paketboxen-mit-klingel-sprechanlage` · Paketboxen ohne Gravur `/paketboxen-ohne-gravur` · Ersatzteile & Zubehör `/ersatzteile-zubehoer`

**Mülltonnenboxen** `/muelltonnenbox` (72 Artikel)
- Mülltonnenbox für 1 Tonne `/muelltonnenbox-fuer-1-tonne` · … für 2 Tonnen `/muelltonnenbox-fuer-2-tonnen` · … für 3 Tonnen `/muelltonnenbox-fuer-3-tonnen` · … für 4 Tonnen `/muelltonnenbox-fuer-4-tonnen` · … für 5 Tonnen `/muelltonnenbox-fuer-5-tonnen` · Ersatzteile & Zubehör `/ersatzteile-zubehoer_1`

**Sprechanlagen** `/tuersprechanlagen` (41 Artikel; H1 „Türsprechanlagen“)
- Video Sprechanlagen `/video-tuersprechanlagen` → Video Sprechanlagen IP-Serie `/video-sprechanlagen-ip-serie` · Video Sprechanlagen 2-Draht-BUS-Serie `/video-sprechanlagen-2-draht-bus-serie`
- Sprechanlagen Sets `/sprechanlagen-sets` → Sprechanlagen Sets IP-Serie `/sprechanlagen-sets-ip-serie` · Sprechanlagen Sets 2-Draht-Bus-Serie `/sprechanlagen-sets-2-draht-bus-serie`
- Audio Sprechanlagen `/audio-tuersprechanlagen` · Video Sprechanlagen mit Briefkasten/Paketbox `/sprechanlage-briefkasten` · *(desktop only: Briefkastenanlagen Konfigurator `/briefkastenanlage`)* · Innenstationen `/innenstationen` · Ersatz Namensschilder `/ersatz-namensschilder`
- Erweiterungen & Zubehör `/vdm10-zubehoer` → … für IP-Serie `/erweiterungen-zubehoer-fuer-ip-serie` · … für 2-Draht-BUS-Serie `/erweiterungen-zubehoer-fuer-2-draht-bus-serie`

**Sicherheitstechnik** `/sicherheitstechnik` (23 Artikel; title „Sicherheitstechnik von HiLook by HIKVISION“)
- Alarmanlagen `/alarmanlagen` · IP Kamera Sets `/ip-kamera-sets` · IP Kameras `/ip-kameras` · EasyLink WLAN Sets `/easylink` · WLAN Kameras `/wlan-kameras` · 4G Kameras `/4g-kameras` · Dual-Objektiv Kameras `/dual-objektiv-kameras` · Videorekorder `/videorekorder` · Anschlussdosen & Zubehör `/anschlussdosen-zubehoer`

**Türklingeln** `/tuerklingel` (87 Artikel)
- Funkklingeln `/funkklingeln` → Edelstahl Funkklingeln `/edelstahl-funkklingeln` · Funkklingel Briefkasten `/briefkasten-funkklingel` · Türklingel Erweiterung `/tuerklingel-weiterleitung-erweiterung` · Funk-Empfänger - Funkgongs `/funkklingel-empfaenger` · Funksender `/tuerklingel-funksender` · Standard Funkklingeln `/standard-funkklingeln` · Heidemann HX Serie `/heidemann-hx-serie`
- Aufputz Türklingeln `/aufputz-tuerklingel` → Aufputz Klingeln kabelgebunden `/aufputz-klingeln-kabelgebunden` · Aufputz Funkklingeln `/aufputz-funk-klingeln`
- Unterputz Türklingeln `/unterputz-tuerklingeln` · Mehrfamilien Klingel `/mehrfamilien-klingel`
- Türgongs `/gong` → Elektronische Gongs `/elektronische-gongs` · Elektromechanische Gongs `/elektromechanische-gongs` · Funk Gongs `/funk-gongs` · Unterputz Gongs `/unterputz-gongs`
- Türklingel Weiterleitung `/tuerklingel-weiterleitung`
- Ersatzteile & Zubehör `/tuerklingel-zubehoer` → Ersatz Namensschilder `/tuerklingel-ersatz-namensschilder` · Klingeltaster & Lichtschalter `/tuerklingel-drucktaster` · Klingeltrafos `/klingel-transformator` · Anschluss & Montage `/tuerklingel-ersatz-montagematerial`

**Hausnummern** `/hausnummern-schilder-schriftzuege` (111 Artikel)
- Einzelne Ziffern & Buchstaben `/hausnummern-einzelne-ziffern` · Beleuchtete Hausnummern `/beleuchtete-hausnummern` → Solar Hausnummern `/solar-hausnummern` · Hausnummernschilder `/hausnummernschilder` · Schriftzüge `/schriftzuege` · Namens- & Hinweisschilder `/namensschilder` · Ersatzteile & Zubehör `/hausnummer-zubehoer`

**Außenleuchten** `/beleuchtung` (357 Artikel; many third-party brands)
- Wand- & Deckenleuchten `/wand-deckenleuchten` → Deckenleuchten `/deckenleuchten` · Wandleuchten `/wandleuchten`
- Hausnummernleuchten `/hausnummernleuchten`
- Strahler/Spots & Wegeleuchten `/strahler-spots-wegeleuchten` → Bodeneinbauleuchten `/bodeneinbauleuchten` · Strahler & Spots `/strahler-spots` · Wegeleuchten `/wegeleuchten`
- Akku-, Solar- und Kameraleuchten `/akku-solar-und-kameraleuchten` → Akkuleuchten `/akkuleuchten` · Solarleuchten `/solarleuchten` · Kameraleuchten `/kameraleuchten`
- Plug & Shine Gartenbeleuchtung `/plug-shine-gartenbeleuchtung` → 1. Leuchten wählen `/plug-shine-gartenbeleuchtungssystem/leuchten` · 2. Kabel wählen `…/kabel` · 3. Trafo wählen `…/trafo` · 4. Steuerung wählen `…/steuerung`
- 24V Garten-Lichtsystem `/metzler-24v-garten-lichtsystem-steinel` → 1. Leuchten wählen `/1-leuchten-waehlen` · 2. Kabel wählen `/2-kabel-waehlen` · 3. Verbinder wählen `/3-verbinder-waehlen` · 4. Netzteil wählen `/4-netzteil-waehlen`
- Sensoren & Zubehör `/sensoren-zubehoer` → Sensoren `/bewegungsmelder-daemmerungsschalter` · Zubehör `/zubehoer`

**Garten** `/garten` (36 Artikel)
- Hochbeete `/hochbeet` · Aufbewahrungen `/aufbewahrungen` · Mährobotergaragen `/maehrobotergaragen` · Steckdosensäulen `/steckdosensaeulen`

Other entry points: Briefkastenanlagen 3D-Konfigurator `/konfigurator` (started from `/briefkastenanlage`), Haus-Gemälde `/haus-gemaelde` („Ihr Zuhause als Kunstwerk.“), Geschenkgutschein `/metzler-geschenkgutschein`. Sitemap: `/export/sitemap_index.xml` → one file `/export/sitemap_0.xml.gz` (4.207 URLs incl. colour-variant pages).

### 1.4 Footer (desktop)

- **Brand block**: „Edelstahl-Tuerklingel.de ist ein Unternehmen der Metzler Gruppe“ · „Der Anbieter für Briefkästen, Sprechanlagen, Türklingeln und Hausnummern.“ · „Mehr erfahren“
- **Contact**: „Allgemeine Hotline: +49 (0) 7121 / 317 7310 (Mo-Fr: 09:00-16:00 Uhr)“ · „Sprechanlagen Hotline: +49 (0) 7121 / 317 7333 (Mo-Fr: 09:00-16:00 Uhr)“ · „E-Mail Support:“ (Cloudflare-obfuscated address) · „Kontaktformular: Zum Kontaktformular“ → `/Kontakt`
- **Informationen**: Auszeichnungen `/auszeichnungen` · Geschenkgutschein `/metzler-geschenkgutschein` · Kundenbilder `/tuerklingel-galerie` · Stellenangebote `https://www.metzlergmbh.de/jobs/` · Wir über uns `/ueber-uns` · News `/News` · Zahlung und Versand `/zahlung-und-versand`
- **Service**: Begriffserklärung `/begriffserklaerung` · FAQ `/faq` · Geschäftskunden `/b2b` · Newsletter `/newsletter` · VDM10 FAQ `/faq/sprechanlagen`
- **Follow us**: Pinterest, Facebook, Instagram, YouTube, X / Twitter (icons)
- **Qualität**: badges „TopShop 2023“, „TopShop 2024“, „TopShop 2025“, „TopShop“ → `/topshop`
- **Mid row**: „Unsere Versandpartner:“ DPD · DHL · Hasenauer & Koch — „Einfach bezahlen:“ SEPA Lastschrift · American Express · Visa · Amazon Pay · Klarna · PayPal · Mastercard · Apple Pay · Google Pay · Vorkasse — review slider (see §3.6) + „Geprüfte Kundenbewertungen“
- **Legal row**: Metzler Garantieerklärung · Datenschutz · AGB · Sitemap · Zahlung und Versand · Impressum · Gesetzliche Gewährleistung · Barrierefreiheit · **„Vertrag widerrufen“** (rendered as a teal button, → `/online-widerrufsformular`) · Batterieentsorgungsgesetz · Widerrufsrecht · Hinweise zur Elektroaltgeräteentsorgung · Cookie-Einstellungen
- „* inkl. gesetzliche MwSt., zzgl. Versand“ · „© 2013 - 2026 | Metzler GmbH“

Global overlays: cookie banner „Wie wir Cookies & Co nutzen“ (buttons „Alle akzeptieren“ / „Ablehnen“ / „Konfigurieren“), French-shop modal „Visitez notre boutique française“ (→ metzler.fr), geo modal, Trusted Shops trustbadge bottom-right (shows ★ 4,7).

---

## 2 · Page types

### 2.1 Home `/`

Title „METZLER Briefkästen, Sprechanlagen & Türklingeln“. Sections in order (server HTML, 01.10.2026):
1. **Promo band** (`.mtz-promo`, seasonal): „Aktion · 15 % auf Sicherheitstechnik“ — „Kameras und Alarmanlagen für mehr Schutz rund ums Haus.“ — two tiles („–15 % Überwachungskameras · Kamera-Sets, WLAN-Kameras & Rekorder“, „–15 % Alarmanlagen · Funk-Alarm für Haus & Wohnung“) — CTA „Zur Sicherheitstechnik“ — „Gültig vom 01.10. bis 31.10.2026“.
2. **Category video grid** (looping videos with labels): Sprechanlagen, Briefkästen, Mülltonnenboxen, Hochbeete, Paketboxen, Außenleuchten, Funkklingeln, Briefkastenschilder, Hausnummern, Schriftzüge, Türklingeln — with an embedded promo tile „Brand Weeks · 01.10.2026 – 15.10.2026 · –10 % auf STEINEL · Zu den Angeboten“.
3. **XDM10/VDM10 banner**: „Die passende Video-Türsprechanlage – egal ob Neubau oder Altbau“ · „POWERED BY“ / „DESIGNED IN GERMANY“ · body (see §4) · „Mehr erfahren“ · Red-Dot image (alt „reddot winner 2026“).
4. **Hero / award** (only H1 on the page): „Deutschlands beliebtester Anbieter für Briefkästen - bereits das vierte Jahr in Folge“ + ntv/DISQ text + „Über 2 Millionen zufriedene Kunden vertrauen bereits auf Metzler – überzeugen auch Sie sich von unserer Qualität!“
5. **Über Metzler**: „Mehr als ein Shop – ein Familienunternehmen seit 2013“ (165 Mitarbeitende, Denis Metzler) · „Metzler kennenlernen“ · „Mehr über unsere Technik“.
6. **Haus-Gemälde**: „Ihr Zuhause als Kunstwerk.“ · „Jetzt gestalten“ → `/haus-gemaelde`.
7. Customer-pictures slider, then footer.
No product carousels on the home page today.

### 2.2 Category / listing page (e.g. `/tuersprechanlagen`, `/briefkasten`)

Layout top → bottom:
1. Breadcrumb „Home › …“
2. H1 + **sub-category slider**: image tile + name + count („Video Sprechanlagen · 38 Modelle“); configurator tile shows „Jetzt konfigurieren“ instead of a count.
3. Count „41 Artikel“ (top right of grid).
4. *(Sprechanlagen only)* **Kaufberater** bar (§2.5).
5. **Left sidebar facets** (desktop) / „Filter“ button with count (mobile, opens off-canvas). Colour facet shows swatch + count. Sidebar ends with a „Kategorien“ tree and an award box „Beliebtester Anbieter Deutschlands 2026 … 1. Platz“.
6. **Product grid**, 24 cards per page, 4 per row desktop / 2 per row mobile; pagination „1 2 … Gehe zu Seite“, URLs `/<kategorie>_s2`.
7. Editorial promo tiles can be interleaved in the grid (Sprechanlagen: the XDM10 „Neubau oder Altbau“ banner appears twice among the first cards).
8. Long SEO text with H2s + FAQ, truncated with „Mehr lesen“ / „Weniger anzeigen“.

**Product card content** (`.p-c`): overlay label top-left („Top bewertet“, or promo „Gültig bis: 31.10.2026 - 15%“, „Sale %“) · image with hover second image · feature pills (Sprechanlagen only: „IP-System“, „BUS-System“, „RFID“, „PIN-Code“, „QR-Code“, „Gesichtserkennung“, „Fingerprint“) · brand line „Metzler“ + stars + count „(64)“ (links to `#tab-votes`) · name (bold link) · price „ab 699,00 €“ (struck-through old price if on sale) · colour dots (3 visible) + „+5 weitere“. No „inkl. MwSt.“ line on cards; no add-to-cart on cards.

**Facets per main category** (labels exactly as live, desktop-visible ones; counts as of 01.10.2026):

| Category | Facets (in order) |
|---|---|
| Briefkästen | Anzahl der Briefkastenfächer (1, 2) · Material (Acrylglas, Edelstahl, Galvanisierter Stahl, Lärchenholz, Metall, V2A Edelstahl (1.4301), V4A Edelstahl) · Farbe (Anthrazit, Braun, Edelstahl, Eisenglimmer, Grau, Schwarz, Weiß, Wunschfarbe) · Montageart (Aufputz, Unterputz) · Zeitungsfach (Integriert, Ohne, Optional) · Marke (Metzler) |
| Paketboxen | Anzahl der Briefkastenfächer (1–5) · Anzahl der Klingeltaster (1–3 Taster) · Farbe · Material (Galvanisierter Stahl) · Namensschild (Lasergraviert) · Marke · Paketbox (Integriert) · System (IP-System / BUS-System, with help text) · Briefkastentyp (Standbriefkasten) |
| Mülltonnenboxen | Anzahl der Mülltonnen (1 Mülltonne … 5 Mülltonnen) · Fassungsvermögen Mülltonne (240 Liter) · Farbe (incl. Beige) |
| Sprechanlagen | Anzahl der Klingeltaster (1–7 Taster, „Flexibel von 1-500“) · Farbe · Türöffner Bedienung (Fingerprint, Gesichtserkennung, PIN-Code, QR-Code, RFID) · Namensschild (Lasergraviert, mit Papiereinleger, Digital) · System. *(Briefkastenfächer, Montageart, Material, Zeitungsfach, Paketbox, Briefkastentyp exist in HTML but are hidden on this page.)* |
| Sicherheitstechnik | Auflösung (2 MP … „8 MP [4K]“) · Speicherart (Cloud, Intern) · Nachtsicht (Farbe) · Marke (Hilook) · PTZ-Funktion (Ja/Nein) · POE (Ja) |
| Türklingeln | Anzahl der Klingeltaster (1–7) · Spannung · Einbaudurchmesser · LED-Spannung · Material · Farbe · Montageart · Stromversorgung · LED-Farbe (Blau, Gelb, Grün, Ohne LED, Pink, Rot, Weiß) · Kopfform · Marke · Beleuchtung (Ringbeleuchtung, Symbol) |
| Hausnummern | LED-Spannung · Material · Farbe · Hausnummernbeleuchtung (Beleuchtete / Solar / Unbeleuchtete Hausnummer) · Marke · Beleuchtung (Ohne) · LED-Farbe (Weiß) |
| Außenleuchten | Hersteller (Metzler & EGLO, Metzler & Steinel, Metzler, Calex, Konstsmide, EGLO Leuchten, Paulmann, Theben AG, Nordlux, Steinel, Star Trading) · Länge in mm · Garantie (15 Jahre, 5 Jahre) · Spannung · LED-Spannung · Material · Farbe (incl. Gold, Silber) · Hausnummernbeleuchtung · Schutzklasse (IP44, IP65) |
| Garten | Farbe · Material (Galvanisierter Stahl) · Marke (Metzler) |

System help texts (Sprechanlagen/Paketboxen): IP-System „Ideal für Neubauten. Nutzt LAN- oder 2-Draht-Sternverkabelung für maximale Flexibilität.“ · BUS-System „Perfekt zum Modernisieren. Nutzt vorhandene 2-Draht-Leitung — kein Neuverlegen nötig.“
Filter URLs compose as `/<kategorie>__<wert>` (e.g. `/tuersprechanlagen__anthrazit`, `/tuersprechanlagen__2-taster`). Many facets have a single value (e.g. „Marke: Metzler“, „Fassungsvermögen: 240 Liter“) — avoid single-value facets in new designs.

**Sort**: a „Sortierung“ dropdown („Standard“ `?Sortierung=100`, „Bestseller“ `?Sortierung=11`) exists in the HTML of every listing and the URL parameter works, but the control is `display:none` at all widths → users cannot sort. **No price filter anywhere.**

### 2.3 Product page (PDP)

Parent pages (e.g. `/metzler-briefkasten-aus-hochwertigem-stahl-siebert`) show „ab“ prices and the hint „Dieser Artikel hat Variationen. Wählen Sie bitte die gewünschte Farbe aus.“ — the **configurator only appears after a colour is chosen** (colour-variant page, e.g. `/?a=29323`). Order of blocks (Siebert, Anthrazit variant):

1. Breadcrumb · gallery („1 / 36“, „Alle 36 Bilder ansehen“, thumbnails; **„3D“ tab** where available, with „Vorschau verlassen“ and „Gravurgröße bearbeiten“)
2. Title (H1) · stars „5,0 (739)“ · „Produkt teilen“ (Link kopieren / E-Mail / WhatsApp)
3. Spec trio: „Hersteller Metzler“ · „Breite × Höhe × Tiefe 37,00 × 37,00 × 10,50 cm“ · „Artikelnummer 29323“
4. Price „89,99 €“ (parent: „ab 89,99 €“) · „inkl. 19% USt. , zzgl. Versand“ · availability „Sofort verfügbar“
5. „Farbe:“ swatches (surcharge tags „+ 29,01 €“, „Wunschfarbe nach RAL + 49,01 €“)
6. Button **„Jetzt anpassen“** → horizontal step bar + accordion steps (see table)
7. „Ihre Konfiguration“ / „Preis wie konfiguriert“ / „In den Warenkorb“ (also as sticky bottom bar with „Details“)
8. „Versanddatum 05.10.2026 - 07.10.2026“ · „Lieferung Gratis Versand · ab 99 €“ · „Details“
9. 5 USP rows with icon + headline + sentence, „10 Jahre Metzler Garantie“ badge, product video
10. Review summary (distribution 5→1 Sterne, photo reviews „Weitere Bewertungen mit Foto“)
11. Tabs: „Beschreibung“ · „Bewertungen (739)“ · „Befestigung“ (Wandmontage / Standbriefkasten – Bodenverankerung / Zaunmontage instructions) · „Downloads (1)“ („Anleitungen & Dokumente … als PDF“) · „Frage zum Artikel“ (form). Intercoms add „Technische Details“ and an „Abmessungen / Größe · Anschluss 2-Draht · IP · Datenblatt“ panel.
12. Merkmale list, „Abmessungen“, weights, „Herstellerinformationen: Metzler GmbH, Täleswiesenstr. 9, 72770 Reutlingen, Germany“, „Warn- und Sicherheitshinweise“
13. „Kundenstimmen“ / „Das schätzen Kunden am meisten“ · „Häufige Fragen zum Produkt:“ (or „Häufige Fragen (FAQ)“) · „Frage stellen“
14. Cross-selling rows (category-dependent): „Passende Klingeln & Sprechanlagen“, „Passende Briefkästen“, „Passende Hausnummern & -schilder“, „Passende Paket- & Mülltonnenboxen“, „Ähnliche Artikel“.

**Configurator steps (verified examples — capability varies per product, never generalise):**

| Product (variant page) | Steps |
|---|---|
| Briefkasten Siebert (29323) | 1 Gravurdaten · 2 Smart-Briefkastenschloss · 3 Funk-Briefkastensensor · 4 Befestigung („Bitte wählen Sie maximal 1.“) · 5 Erweiterungen & Zubehör · 6 Dekorieren & Verzieren · 7 Entwurf zur Freigabe |
| Türklingel Stella (5189) | 1 Größe · 2 Gravurdaten · 3 Klingeltaster · 4 Montageart · 5 Befestigung · 6 Entwurf zur Freigabe |
| Funkklingel Alan (6677) | 1 Gravurdaten · 2 Anschlussart der Klingel · 3 Funk Empfänger (Gongs) · 4 Klingeltaster · 5 Signalverstärker · 6 Entwurf zur Freigabe |
| VDM10 2.0 Colson (36845) | 1 Anschluss (LAN / PoE, 2-Draht IP, with „Anschlussvorgaben“ modal) · 2 Gravurdaten · 3 Innenstationen · 4 Stromversorgung · 5 Erweiterungen & Zubehör · 6 Entwurf zur Freigabe |
| XDM10 Maxior (44297) | 1 Montageart · 2 Stromversorgung · 3 Innenstationen · 4 Erweiterungen & Zubehör (no engraving step) |

Optional add-ons are listed as cards with price „+49,99 €“, often preceded by a benefit list (e.g. Smart-Briefkastenschloss: „Flexible Öffnung – Entriegelung per Fingerabdruck, RFID oder App“; „Schlüssellose Nutzung“; „Einfache Einrichtung“; „Lange Batterielaufzeit“).

**Engraving / Namensschild inputs** (placeholders): Siebert „Namensschild“, „Straße“, „Hausnummer“; Stella/Alan „Gravur Zeile 1“, „Gravur Zeile 2“ (+ Alan „Hausnummer“); VDM10 „Gravurtext“. Comment field „Kommentar zur Gravur (Ausrichtung, Sonderwunsch, etc)“ / „Gravur Kommentar (Ausrichtung, Sonderwunsch, etc)“. Font picker „Schriftart · Bitte wählen“ with options labelled „Schriftart 0, 1, 2, 4, 7, 8, 9, 15, 16, 17, 99, 77“ (12 on Siebert/Stella, 10 on Alan, fewer on VDM10); the font used in the product photo is tagged „Schrift wie Produktbild“. Alignment picker „Gravur Ausrichtung“ (Stella only „Ausrichtung F“, Alan only „Ausrichtung A“). Inputs render in the chosen font.

**„Entwurf vor Fertigung“ (+4,95 €)**, step „Entwurf zur Freigabe“: „Wir senden Ihnen vor der Anfertigung einen Entwurf per E-Mail zu. Sie bestätigen die Anfertigung oder teilen unserer Grafikabteilung Ihre Änderungswünsche mit. Es sind bis zu 2 Korrekturen enthalten. Die angegebene Lieferzeit bezieht sich auf die Anfertigung nach Ihrer Freigabe.“ + „Aktuelle Anfertigungszeit des Entwurfs: 3 Werktage“ (a second variant says 4 Werktage). It is the route for anything the configurator can't do (larger/smaller text, special layouts) — present it as a service, not a fee for a preview. Seen on 32 of 120 random sitemap URLs today.

**3D live preview**: on variant pages that carry the marker `mpc3d_cunique_ek_` a „3D“ tab opens a WebGL canvas (600×600); typed engraving text renders live on the model (verified today on Siebert Anthrazit: text typed into „Straße“ appeared on the plate; default demo name „Hoffmann“). Present on Siebert, Stella, VDM10 Colson; not on Alan, XDM10 Maxior. Coverage is low: 7 of 120 random sitemap URLs today (Sept 2026 audit: 59/399 ≈ 15 %, Türklingeln 2 %). Design rule: show a 3D badge only where the marker exists.

**Briefkastenanlagen** `/briefkastenanlage` → „3D-Live-Konfigurator“: „Dank der Live-Vorschau wählen Sie Funktionen, Design, Montageart und Klingelanlage in Echtzeit … Zudem erhalten Sie sofort einen verbindlichen Preis für Ihre Konfiguration.“ · „Jetzt Konfigurator starten“ → `/konfigurator` · „✓ Kostenlos & unverbindlich · Sofortiger Festpreis · In nur 3 Minuten fertig“.

### 2.4 Cart `/Warenkorb`

Only the **empty cart** was checked (no add-to-cart allowed): H „Warenkorb (0 Artikel)“ · „Ihr Warenkorb ist derzeit leer.“ · „Stöbern Sie in unseren Kategorien und finden Sie das perfekte Produkt für Ihr Zuhause.“ · „Weiter einkaufen“ · help box „Können wir Ihnen helfen? Unser Kundenservice steht Ihnen gerne zur Verfügung. Kontakt aufnehmen“ · category links (Briefkästen, Sprechanlagen, Mülltonnenboxen, Paketboxen, Türklingeln, Hausnummern & Schriftzüge, Außenleuchten, Garten & Aufbewahrung, Zubehör) · „Weitere Metzler Produkte für Sie“ (cards incl. base price „4,00 € pro 100 ml“). Filled cart and checkout (`/Bestellvorgang`) **(nicht geprüft)**.

### 2.5 Kaufberater (only on `/tuersprechanlagen`)

Native plugin `metzler_advisor` (`section.mtz-advisor`, data via `GET /metzler-advisor-api?flow=sprechanlagen`, 57 products, max. 3 results). Closed bar: „Finden statt Suchen“ / „Beantworten Sie ein paar kurze Fragen – der Berater empfiehlt Ihnen die passende Türsprechanlage.“ / button „Kaufberater“. Open: „SCHRITT 1 VON 7“, per-option model counts, „Weiter“ / „Überspringen“ / „Zurück“, „Aktuell passen 57 von 57 Modellen zu Ihrer Auswahl.“, last button „Empfehlung anzeigen“.

| Step | Question | Options (label — description) | Shown when |
|---|---|---|---|
| System | „Wie sieht die Verkabelung bei Ihnen aus?“ (help „Die Verkabelung entscheidet, welche Serie passt.“) | „Modernisierung und bestehende Verkabelung“ — „Nachrüstung ohne neue Kabel · 2-Draht-BUS“ (13 Modelle) · „Neubau oder Neuverkabelung“ — „moderne Funktionen (App, Video, Gesicht) · IP-System“ (44 Modelle) | always |
| Parteien | „Für wie viele Wohneinheiten / Klingeltaster?“ | 1 Partei — Einfamilienhaus · 2 Parteien — Zweifamilienhaus · 3 Parteien — Dreifamilienhaus · 4 und mehr Parteien — Mehrfamilienhaus · Flexibel — „Großobjekt · modular für 1–500 Parteien“ | always |
| Kombination | „Nur Sprechanlage – oder als Kombination?“ | Nur Sprechanlage · Mit Briefkasten · Mit Paketbox | IP only |
| Medium | „Möchten Sie sehen, wer klingelt?“ | Video-Sprechanlage — „Mit Kamera – Besucher sehen“ · Audio genügt — „Nur Sprechen & Hören“ | IP only |
| Bauform | „Wie soll montiert werden?“ | Aufputz · Standmontage | Briefkasten + 1–2 Parteien |
| Türstation | „Welche Türstation soll integriert sein?“ | Standard-Video (VDM10) — „Kamera, App, FRITZ!Box“ · Touch-Display & Gesichtserkennung (SDM10) | Briefkasten + 1–2 Parteien |
| Zutritt (multi) | „Wie möchten Sie schlüssellos öffnen?“ („Mehrfachauswahl möglich. Die App-Öffnung ist immer dabei.“) | RFID-Karte / -Chip · PIN-Code · Fingerabdruck · Gesichtserkennung | IP, no Briefkasten |
| Namensschild | „Wie soll der Name angezeigt werden?“ | Lasergraviertes Namensschild · Namensschild mit Papiereinleger · Digitales Namensschild | IP, Sprechanlage only |
| Farbe | „Welche Farbe oder Oberfläche?“ | Anthrazit (RAL 7016) · Edelstahl · Schwarz (RAL 9005) · Weiß (RAL 9016) · Grau (RAL 9007) · Weitere Farben → Braun / Eisenglimmer / Wunschfarbe | IP, Sprechanlage only |

Results: „Unsere Top-Empfehlung“ / „%s passende Türsprechanlagen“, „Alle passenden Modelle ansehen“, „Quiz neu starten“; empty: „Keine exakte Übereinstimmung“ + „Passen Sie einzelne Angaben an – oder lassen Sie sich persönlich beraten.“; support box „Unsicher bei der Auswahl?“ / „Unsere Experten beraten Sie kostenlos – auch zur Verkabelung vor Ort.“ („Produktberatung“, „Installationspartner“); lead capture „Empfehlung per E-Mail & Beratung“ (E-Mail + reCAPTCHA); with Briefkasten a teaser „Briefkastenanlage nach Maß“ → `/briefkastenanlage`. Dead options show „nur IP-Serie · wechseln?“. Quirk: header says „von 7“ although branches are shorter.

### 2.6 Search `/search/?qs=…`

Header form `GET /search/`, field `qs`, `minlength="4"` (3-letter queries like „Box“ cannot be submitted). Results page = listing template: H1 „Suche nach: Klingel“, „242 Artikel“, facets mixed from all categories (e.g. Mülltonnen facets on a „Klingel“ search), hidden sort. Correct spellings work (Klingel 242, Briefkasten 298, Sprechanlage 83, Hausnummer 234, Paketbox 122, VDM10 66, Siebert 18). **Any typo returns zero**: klingle, briefkastn, sprechanlge, siebrt, hausnumer, paketbx → „Leider wurde zu Ihrem Suchbegriff nichts gefunden. Bitte geben Sie einen anderen Suchbegriff ein.“ — no suggestions, no categories, no contact hint. (`/search?search=` does not work; use `qs`.)

### 2.7 Service pages

- `/faq` = separate React app „Metzler Support“ (theme `#015253`), `/faq/sprechanlagen` = VDM10 FAQ.
- `/Kontakt`: „Kennen Sie schon unseren FAQ Bereich?“ teaser, two entry cards „Allgemeiner Kontakt“ / „Technischer Support (Sprechanlagen)“, form (Vorname, Nachname, Firma, E-Mail, Telefon, Betreff: Barrierefreiheit · Allgemeine Anfrage · Liefertermin · Technischer Support · Stornieren · Reklamation · Widerruf · Änderungsanfrage · „Kaufberatung: Intercom VDM10/SDM10/ADM10“ · Rücksendung; Nachricht), reCAPTCHA.
- Sprechanlagen „Kontakt & Service“ modal (`#vdm10-contact-popup`, opened by „Termin vereinbaren“): „Sprechen Sie mit einem Experten“ · „Persönliche Beratung, technischer Support und Metzler Partnerbetriebe – wir sind für Sie da.“ · Hotline „+49 (0) 7121 / 317 7333 · Mo–Fr · 09:00–16:00 Uhr“ · „Wie können wir Ihnen helfen?“ → „Produktberatung & Bestellung“ (→ `https://calendly.com/kaufberatung`), „Metzler Partnerbetriebe“ (→ `/partnerbetriebe`), „Häufige Fragen (FAQ)“ (→ `/faq/`), „Technischer Support · Techniker Termin zur Einrichtung.“ (→ `/sprechanlagen-online-support-termin`).

---

## 3 · Services & promises (only what the site states)

### 3.1 Shipping (`/zahlung-und-versand`)
| Ziel | Versand | Preis | Lieferzeit |
|---|---|---|---|
| Deutschland, Österreich | DHL/DPD | „Gratis ab 99,00 €, sonst 4,95 €“ | DE „1-3 Werktage“, AT „2-4 Werktage“ |
| EU | DHL/DPD | 9,90 € | „3-5 Werktage“ |
| Großbritannien | DHL/DPD | 19,90 € | „3-5 Werktage“ |
- Delivery countries: DE + BE, BG, DK, EE, FI, FR, GR, GB, IE, IT, HR, LV, LT, LU, MT, NL, AT, PL, PT, RO, SE, SK, SI, ES, CZ, HU, CY.
- „Versandkosten Sperrgut“ (DPD Sperrgut): bis 30 kg 29 € · 60 kg 58 € · 90 kg 87 € · 120 kg 116 € · 150 kg 145 € · bis 1000 kg 174 €.
- Footer partners: DPD, DHL, Hasenauer & Koch. PDP shows a concrete „Versanddatum“ range and „Lieferung Gratis Versand · ab 99 €“. Services (e.g. Support-Termin) say „Versandkostenfreie Lieferung“.
- Short form for designs: „Versandkostenfrei ab 99 €“ (Über-uns uses „VERSANDKOSTENFREI AB 99 €“).

### 3.2 Payment
Accepted (page list): Vorkasse per Überweisung · Kreditkarte · Rechnung · via Klarna: Sofortüberweisung, Rechnung, Ratenkauf, Lastschrift, Kreditkarte · Amazon Pay · via PayPal Checkout: PayPal, PayPal Express, Kreditkarte, SEPA-Lastschrift, „Später bezahlen“ · Apple Pay · Google Pay · via Mollie: Rechnung (über Klarna). Note: „Die Zahlung per Rechnung ist nur für Behörden und öffentliche Institutionen möglich.“ (direct invoice) — consumers' „Kauf auf Rechnung“ (top bar) runs via Klarna/PayPal. „Der Rechnungsbetrag ist bei Zahlung auf Rechnung innerhalb von 14 Tagen auszugleichen.“ Footer logos: SEPA Lastschrift, American Express, Visa, Amazon Pay, Klarna, PayPal, Mastercard, Apple Pay, Google Pay, Vorkasse.

### 3.3 Metzler Garantie vs. gesetzliche Gewährleistung
- **Metzler Garantie** (`/metzler-garantieerklaerung`): Garantiegeber Metzler GmbH, Täleswiesenstraße 9, 72770 Reutlingen; „Räumlicher Geltungsbereich: Deutschland und Österreich“; only Metzler-brand products bought in this shop by end consumers („Gewerbekunden sind von der zusätzlichen Garantie ausgeschlossen“; orders from 01.09.2022). Content: „eine Garantie gegen Durchrostung des Produkts für die Dauer von zehn Jahren ab Übergabe“; remedy repair or new/refurbished parts. Excluded: Flugrost, mechanical damage („insbesondere Vandalismus“), ignored care instructions / faulty installation. Claim by e-mail/post with order number + photo; return label / freight pickup at Metzler's cost. „Durch diese Garantie werden diese Rechte nicht eingeschränkt.“
- Marketing wording: „10 Jahre Metzler Garantie“ (top bar, PDP badge); Über uns says „Metzler Garantie · Bis zu 10 Jahre · Schutz vor Durchrostung · Reparatur oder Ersatzteile“.
- **Gesetzliche Gewährleistung** (`/gesetzliche-gewaehrleistung`): the page currently shows only its heading (no body text). Lighting facet „Garantie: 15 Jahre / 5 Jahre“ refers to third-party manufacturer warranties.

### 3.4 Widerruf / returns (`/widerrufsrecht`, form `/online-widerrufsformular`)
„Sie haben das Recht, binnen eines Monats ohne Angabe von Gründen diesen Vertrag zu widerrufen.“ (1 month, longer than the legal 14 days). Refund within 14 days incl. standard delivery costs; goods back within 14 days; customer bears direct return costs (non-parcel goods „auf höchstens etwa 75 EUR geschätzt“). **No right of withdrawal for personalised goods** („Waren, die nicht vorgefertigt sind und für deren Herstellung eine individuelle Auswahl oder Bestimmung durch den Verbraucher maßgeblich ist …“) — i.e. engraved items. Widerruf contact phone „+49 (0) 7121 / 3179114“. Footer button „Vertrag widerrufen“.

### 3.5 Other services
- **Geschenkgutschein** `/metzler-geschenkgutschein` (Art. 12582): Werte 25 / 50 / 75 / 100 / 125 / 150 / 175 / 200 € („ab 25,00 €“); „Der Gutschein gilt für alle Artikel aus unserem Onlineshop.“ „Der Gutschein wird Ihnen per Post in einem hochwertigen Geschenkumschlag zugestellt und ist ab Ausstellungsdatum 3 Jahre lang gültig.“
- **Geschäftskunden/B2B** `/b2b`: „Willkommen auf dem b2b Marktplatz von Metzler für Elektrofachhändler und Wiederverkäufer“; 3 steps: im Webshop registrieren → Gewerbenachweis per E-Mail senden → Prüfung und Aktivierung des „B2B-Wiederverkäufer Account“; promise „verbesserten Einkaufskonditionen“.
- **Fachhandelspartner** `/partnerbetriebe` („Partnersuche“): PLZ/Stadt search, „Umkreis: 50 km“, types „Premiumpartner“ / „Montagepartner“; „Alle Partner sind von Metzler geschult und zertifiziert.“ Montagepartner = installation offer; Premiumpartner = VDM10 demo unit in store + full advice, sale, installation.
- **Termin vereinbaren**: Sprechanlagen modal → Calendly „kaufberatung“ (free advice). Paid **„Sprechanlagen Online Support Termin“** `/sprechanlagen-online-support-termin` (Art. 38275): „ab 59,00 €“, 30 or 60 Minuten, remote via TeamViewer, only for orders from edelstahl-tuerklingel.de.
- **Hotlines**: Allgemeine Hotline +49 (0) 7121 / 317 7310 · Sprechanlagen Hotline +49 (0) 7121 / 317 7333 — both „Mo-Fr: 09:00-16:00 Uhr“. Address Metzler GmbH, Täleswiesenstr. 9, 72770 Reutlingen.
- **Newsletter** `/newsletter`: „Newsletter abonnieren (Abmeldung jederzeit möglich)“, E-Mail* + Vorname/Nachname, Mailchimp, button „Abonnieren“; Über uns promises „neue Produkte, exklusive Angebote und Einblicke aus unserer Manufaktur – einmal im Monat.“ No discount incentive stated.
- **Kundenbilder** `/tuerklingel-galerie`, **News** `/News`, **Begriffserklärung** `/begriffserklaerung`, French shop metzler.fr.

### 3.6 Awards, reviews, claims
| Claim | Exact wording / source |
|---|---|
| Kunden | „über 2 Mio. zufriedene Kunden“ (top bar) · „Über 2 Millionen zufriedene Kunden“ (home) · Über uns: „2 Mio. Kunden“ |
| Since | „Original Metzler Qualität seit 2013“ · „ein Familienunternehmen seit 2013“ · „Manufaktur seit 2013 · Reutlingen“ |
| Company facts (Über uns) | 165 Mitarbeitende · 2.500 Produkte · 500 Designs („Über 500 eingetragene Designs entstammen unserer Konstruktionsabteilung in Reutlingen.“) · founder Denis Metzler |
| ntv | „Deutschlands beliebtester Anbieter für Briefkästen - bereits das vierte Jahr in Folge“ (ntv / Deutsches Institut für Servicequalität, „rund 50.000 Befragten“); listing box „Beliebtester Anbieter Deutschlands 2026 … 1. Platz“ |
| TopShop | COMPUTER BILD & Statista „Top Shop“ 2023, 2024, 2025 („bereits zum dritten Jahr in Folge“), `/topshop` |
| Red Dot | „Red Dot Winner 2026“ — Kategorie Product Design, for the **XDM10** („Die XDM10 wurde mit dem Red Dot Award ausgezeichnet.“) — on Über uns + home banner image; not yet on `/auszeichnungen` |
| Others (`/auszeichnungen`) | „3 Jahre Statista Trend-Shop Aufsteiger des Jahres“ · „Metzler Briefkasten als Vergleichssieger bei vergleich.org“ (2024) |
| Reviews (footer slider, 01.10.2026) | Alle Bewertungen **4,71 „Sehr gut“ · 36.785** · Trusted Shops **4,73 „Sehr gut“ · 32.461** · Google **4,63 „Sehr gut“ · 3.190** · Trustpilot **4,42 „Gut“ · 1.134**; PDP reviews own system („Geprüfte Kundenbewertungen“, e.g. Siebert 5,0 / 739) |
| Made in Germany | Home/intercom banner „DESIGNED IN GERMANY“ (XDM10). Türklingeln: „Wir als deutscher Hersteller von handgefertigten Türklingeln & Klingelplatten …“, „Viele unserer Türklingeln werden in Deutschland hergestellt.“; Stella bullet „Metzler Qualitätsprodukt – Made in Germany“. Use „Made in Germany“ only where the product page says it. |
| Engraving | „Individuelle Lasergravur“, „Auch nach Jahren ist ein Verblassen oder Verwischen der Schrift ausgeschlossen.“, „UV- und witterungsbeständig“, „Gravurplatte: rostfreier Edelstahl V4A“ (Briefkasten); Türklingeln: „3D Lasergravur oder 3D Glas Gravur“ |
| Standard | Briefkasten „gemäß DIN/EN 13724“ (Siebert) |

---

## 4 · Voice & tone

- **Sie-form**, warm-sachlich, benefit first, then proof. Short noun-phrase headlines („Verdecktes Schloss“, „Integriertes Zeitungsfach“) + one explanatory sentence. Section headlines often use a dash or colon construction („Mehr als ein Shop – ein Familienunternehmen seit 2013“).
- Lists of benefits with en dash: „Flexible Öffnung – Entriegelung per Fingerabdruck, RFID oder App“.
- Typical words: hochwertig, massiv, witterungsbeständig, personalisiert, individuell, Unikat, Blickfang, Eingangsbereich, Zuhause, rostfrei, pulverbeschichtet.
- Numbers: German formatting (1.490,00 €, 36.785, 4,73); units with space („37 × 37 × 10,5 cm“, „240l“ in names, „150m Reichweite“ in names — names are inconsistent, prefer spaced units in new copy).
- Model names are given names (Siebert, Colson, Kian, Maxior, Stella, Alan, Bispo, Zivo…) and always come last in the product name.
- Category SEO texts are long and generic; PDP copy is concrete. Write like the PDPs.

**Real example sentences (verbatim):**
1. „Beantworten Sie ein paar kurze Fragen – der Berater empfiehlt Ihnen die passende Türsprechanlage.“ (Kaufberater)
2. „Ob Neubau mit Netzwerkkabel oder Renovierung im Bestand: Metzler hat das passende System.“ (home / Sprechanlagen)
3. „Ihre vorhandene 2-Draht-Klingelleitung nutzen Sie einfach weiter – ohne neue Kabel, ohne aufgestemmte Wände.“
4. „Und per App sehen Sie jederzeit, wer vor der Tür steht.“
5. „Der Briefkasten besticht durch die professionelle Lasergravur und wird so zum Unikat.“ (Siebert)
6. „Ermöglicht den Einwurf von DIN-A4-Umschlägen und C4-Großbriefen, ohne diese zu knicken.“ (Siebert USP)
7. „Das Schloss ist durch die Einwurfklappe geschützt, um es vor Witterungseinflüssen zu bewahren.“
8. „Keine Lust auf unerwünschte Werbung? Kein Thema mehr mit unseren praktischen Briefkastenschildern.“
9. „Die Dekorationselemente lassen sich schnell und ohne Bohren montieren und werten Ihren Briefkasten auf.“ (configurator step 6)
10. „Wir senden Ihnen vor der Anfertigung einen Entwurf per E-Mail zu.“ (Entwurf vor Fertigung)
11. „Unsere Klingeln ermöglichen es Ihnen, Ihren Eingang zu einem wahren Blickfang zu gestalten.“ (/tuerklingel)
12. „Mit einer Türsprechanlage können Sie über die Innenstation jederzeit sehen oder hören, wer vor Ihrer Tür steht, ohne diese öffnen zu müssen.“ (/tuersprechanlagen)
13. „Persönliche Beratung, technischer Support und Metzler Partnerbetriebe – wir sind für Sie da.“ (Kontakt & Service modal)
14. „Unsere Experten beraten Sie kostenlos – auch zur Verkabelung vor Ort.“ (Kaufberater)
15. „Sie gestalten Ihr Produkt nach Ihren Wünschen – Farbe, Gravur und Zubehör wählen Sie selbst.“ (Über uns)

Microcopy to reuse: „Jetzt konfigurieren“, „Jetzt anpassen“, „Preis wie konfiguriert“, „In den Warenkorb“, „Sofort verfügbar“, „Versanddatum“, „Bitte Farbe wählen“, „Bitte wählen“, „Weiter“, „Mehr lesen“, „Alle … Bewertungen ansehen“, „Frage zum Artikel“, „Zum Kontaktformular“, „Weiter einkaufen“.

---

## 5 · Known issues (verified 01.10.2026) — avoid in new designs

| # | Issue | Status today | Evidence |
|---|---|---|---|
| 1 | Search has no typo tolerance | **still present** | klingle / briefkastn / sprechanlge / siebrt / hausnumer / paketbx → 0 results, no suggestions; plus `minlength="4"` blocks short queries |
| 2 | Machine font names „Schriftart 0…99“ | **still present** | Siebert/Stella: Schriftart 0, 1, 2, 4, 7, 8, 9, 15, 16, 17, 99, 77; Alan: 10 of them. Copy also over-promises: Alan „20 verschiedene Schriftarten sowie 5 unterschiedliche Ausrichtungen“ vs 10 fonts + only „Ausrichtung A“; Stella „20 ausgesuchte Schriften sowie 3 unterschiedliche Ausrichtungen“ vs 12 fonts + only „Ausrichtung F“; Siebert text „zwanzig auserwählten Schriftarten“ vs 12 |
| 3 | `word-break: break-all` on product names on mobile | **still present** | inline CSS `@media(max-width:400px){a.title.block.h4.m0.etk-pl-name{word-break:break-all}}`; computed `break-all` at 375/390 px (cards 168 px wide, 2 per row), `normal` at 768 px; `hyphens: manual` |
| 4 | No sort / no price filter | **still present** (partly built) | Price filter: none on any category or search. Sort: „Sortierung · Standard / Bestseller“ is in the HTML and `?Sortierung=11` reorders, but the control is `display:none` at 1440/768/390/375 px |
| 5 | Facet counts disagree with results | **still present** | Sprechanlagen „Anthrazit (40)“ → 53 Artikel, „Schwarz (31)“ → 34; Briefkästen „Anthrazit (70)“ → 71. Units also disagree: „41 Artikel“ vs tile „Video Sprechanlagen · 38 Modelle“ vs Kaufberater „57 Modelle“; Briefkästen „80 Artikel“ vs tile „Einfamilien Briefkasten · 77 Modelle“ |
| 6 | Wrong `itemprop="price"` microdata on listing cards | **still present, broader than ×1000** | Affects „ab“-priced cards. Page 1 counts: Türklingeln 21/24, Briefkästen 9/24, Sprechanlagen 4/24, also Hausnummern, Außenleuchten, Garten, Sicherheitstechnik; Paketboxen/Mülltonnenboxen 0. Two patterns: inflated (31101 „699000.00“ for 699,00 €; 42955 „1590000.00“; 35857 „39989.00“ for 39,99 €; 36621 „89989.00“) and truncated cents (35875 „24.00“ for 24,99 €). Visible `.price` text is correct — never read prices from that meta |
| 7 | Generic VDM10 block inside long descriptions | **not found / fixed** | 0 of 30 random non-intercom PDP descriptions + Siebert, Stella, Alan contain VDM10 text; VDM10 only appears in cross-sell rows. The XDM10 „Neubau oder Altbau“ banner lives only on home and in the /tuersprechanlagen grid |

**Further issues found today**
- `/gesetzliche-gewaehrleistung` has no body text (heading only, also in the rendered page).
- Warranty wording conflict: Über uns „Metzler Garantie · Bis zu 10 Jahre … Privat & Gewerbe“ vs Garantieerklärung „Gewerbekunden sind von der zusätzlichen Garantie ausgeschlossen“.
- „Kauf auf Rechnung“ (top bar) vs payment page „Die Zahlung per Rechnung ist nur für Behörden und öffentliche Institutionen möglich.“ (consumers pay later via Klarna/PayPal) — word invoice claims carefully.
- `/auszeichnungen` is behind: still „3 Jahre n-tv … 2025“ and no Red Dot 2026, while home says „vierte Jahr in Folge“.
- PDP tax line renders with a stray space: „inkl. 19% USt. , zzgl. Versand“ — write „inkl. 19% USt., zzgl. Versand“ (no space before the comma) in new designs.
- Configurator hidden behind colour choice on parent pages; 3D only on a minority of variant pages (7/120 sampled).
- Facets differ in structure per category (single-value facets like „Marke: Metzler“, „Material: Galvanisierter Stahl (45)“ on Paketboxen; duplicate materials „Edelstahl“ vs „V2A Edelstahl (1.4301)“).
- Kaufberater shows „SCHRITT 1 VON 7“ though most paths are shorter.
- Search results mix facets of unrelated categories.

---

## 6 · How this was checked (to refresh)

- `curl -A "Mozilla/5.0"` works for all public pages (WebFetch only sees the nav). Collapse whitespace before parsing (newlines inside tags).
- Menu: `#cat-w #cat-ul > li.mgm-fw` (desktop tiles + `aside.mega-poster`), `header #cat-ul` (3-level tree).
- Facets: `aside#sp-l section.box-filter-*` (heading `.panel-heading`, options `a.filter-item`, count `.ctr`); visibility needs a rendered page.
- Cards: `id="result-wrapper_buy_form_<kArtikel>"`; visible price `strong.price`; overlay `.ov-t`; pills `.pcard__pill`.
- Variant page: `/?a=<kArtikel>` (swatch `label.variation[data-ref]`); configurator steps `.step-label`, fonts `.schriftart-numbers .txt`, 3D marker `mpc3d_cunique_ek_`.
- Kaufberater data: `GET /metzler-advisor-api?flow=sprechanlagen` (JSON: steps, strings, products).
- Review numbers: footer `.maio-slider__slide[data-source]`.
- Not verified today: filled cart, checkout, login/account, mobile header details beyond the trust bar, chat bubble seen on /tuersprechanlagen.
