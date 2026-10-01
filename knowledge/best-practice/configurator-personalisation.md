# Best practice: Configurator & personalisation (Gravur, 3D live configurator)

**Stand: 01.10.2026.**

- Sources were opened on that date, and numbers are quoted as stated.
- NN/g's customisation studies are old (2000/2009) but remain their current published guidance.
- This is not legal advice. Have the Widerruf wording checked by counsel or the legal-text provider.

**Metzler current state (live, 01.10.2026; 3D coverage from a 400-product sample, Sept 2026)**

- **3D coverage:** 3D live configurator with engraving preview on **~15 % of products**:
  - Paketboxen 32 %
  - Briefkästen 31 %
  - Sprechanlagen 27 %
  - **Türklingeln 2 %**
  - Hausnummern 0 %
  - The 3D marker `mpc3d_cunique_ek_` sits on **colour-variant pages** (e.g. Siebert `/?a=29323`), not the parent.
- **Siebert configurator steps:** "Jetzt anpassen" leads through:
  1. Gravurdaten
  2. Smart-Briefkastenschloss (+49,99)
  3. Funk-Briefkastensensor (+59,99)
  4. Befestigung
  5. Erweiterungen & Zubehör
  6. Dekorieren & Verzieren
- **Engraving fields:**
  - Text fields: "Namensschild", "Straße", "Hausnummer".
  - "Kommentar zur Gravur (Ausrichtung, Sonderwunsch, etc)".
  - A font dropdown with **"Schriftart 0, 1, 2, 4, 7, 8, 9, 15, 16, 17, 77, 99"** (12 options), each labelled "Schrift wie Produktbild".
  - The description promises "zwanzig auserwählten Schriftarten".
  - "Gravurgröße bearbeiten".
  - "Entwurf vor Fertigung +4,95 €": a designer proof by e-mail within 3–4 working days, with up to 2 corrections. It is the route for things the configurator can't do.
- **Sticky bar:** fixed bottom CTA bar with "Preis wie konfiguriert" and an "Ihre Konfiguration" drawer.
- **Competitor benchmarks** (see `../competitors.md`):
  - Frabox: 2D live overlay, real font names.
  - gravuru: free canvas with motifs and curved text.
  - DoorBird: 3D + AR, live price + delivery time, save with technical drawing.
  - Siedle IQ planner: per-flat names, "Projektübersicht teilen".
  - Ritto: auto-adds the Netzteil.

---

### 1. Live preview of the engraving on the product, as the user types, on every engravable product
- **Why:** product-customisation sites averaged **66 % task completion**, against 83 % for interface-customisation sites. Users felt less in control (60 % vs 66 %). https://www.nngroup.com/articles/customization-of-uis-and-products/
- **Examples:**
  - https://www.apple.com/de/shop/buy-airpods/airpods-pro-3: "Gravur hinzufügen" renders the text onto the case image immediately.
  - Frabox (2D): https://www.frabox.de/fb94-11170/frabox-quadratische-klingelplatte-stoke-led-fuer-unterputzmontage?number=FB94-11170.1
- **Metzler, now:** 3D preview on ~15 %. Elsewhere there are text fields with no preview, including 98 % of Türklingeln, the most price-competitive category.
- **Metzler, recommended:**
  - Roll out a **2D live overlay** (text rendered on the hero photo in the chosen font and position) to every engravable product as the baseline.
  - Keep 3D as the premium layer.
  - The Stella doorbell already proves the 3D template works on doorbells.

### 2. Validate fit inline and show limits up front
- **Why:** Apple shows an inline error ("passt nicht in den verfügbaren Platz") and disables saving, instead of a hidden hard cut-off. Example: the Apple page above.
- **Metzler, now:** no visible character or line limit was observed. "Gravurgröße bearbeiten" exists.
- **Metzler, recommended:**
  - Show "Zeile 1: 12 / max. 20 Zeichen" live.
  - Warn when text would drop below the minimum letter height.
  - Offer "Entwurf vor Fertigung" right at that warning.

### 3. Use human labels: font names with a sample, letter height in mm
- **Why:** NN/g describes users failing with font sizes in units "that made no sense to the average person". https://www.nngroup.com/articles/customization-of-uis-and-products/
- **Example:** Frabox lists Eurostile, Avantgarde Md BT, Arial, Monotype Corsiva.
- **Metzler, now:**
  - The font labels are machine IDs ("Schriftart 0…99"), each with the same label "Schrift wie Produktbild".
  - The PDP copy promises 20 fonts; Alan's copy promises "20 Schriftarten und 5 Ausrichtungen" while the configurator offers 10 fonts and one alignment.
- **Metzler, recommended:**
  - Show a font picker as visual tiles, each rendering the customer's own name in that font, with a readable name ("Klassisch Serif", "Modern Grotesk", "Schreibschrift").
  - Make the copy match the real count.

### 4. Start from a good default and a few templates, not a blank form
- **Why:**
  - NN/g: "Edit; Don't Design". Offer a small number of pre-designed templates; put the most common changes first and move expert options aside. https://www.nngroup.com/articles/customers-as-designers/
  - Many users never customise, so defaults matter. https://www.nngroup.com/articles/customization-of-uis-and-products/
- **Example:** https://www.mymuesli.com/pages/mixer shows ready-made mixes beside build-your-own.
- **Metzler, now:** empty fields with placeholders.
- **Metzler, recommended:**
  - Prefill an example ("Familie Muster" / "12") rendered in the preview, plus 3–4 layout templates (Name only / Name + Hausnummer / Zwei Familien / Straße + Nr.).
  - Keep "Kommentar", emoji and free layout under "Sonderwunsch → Entwurf vor Fertigung".

### 5. Make the personalisation entry findable in the buy box
- **Why:** on customisation sites, poor findability caused **45 %** of task failures. https://www.nngroup.com/articles/customization-of-uis-and-products/
- **Example:** Apple's AirTag buy box: "Personalisiere dein AirTag mit einer kostenlosen Gravur". https://www.apple.com/de/shop/buy-airtag/airtag
- **Metzler, now:**
  - On parent pages the CTA is "Bitte Farbe wählen".
  - The 3D tab appears only after picking a colour variant.
- **Metzler, recommended:**
  - Preselect the bestseller colour.
  - Show "Gravur gestalten – Vorschau live" as the primary block in the buy box.
  - Put a "3D" badge on the hero image.

### 6. Show options as visible choices, not long dropdown chains
- **Why:** NN/g criticises configurators built as long lists of dropdowns: they hide alternatives and make comparison hard. https://www.nngroup.com/articles/customers-as-designers/
- **Example:** https://www.nike.com/de/nike-by-you, a curated set of colours and materials in 3D.
- **Metzler, now:**
  - Six steps, mostly dropdowns and add-on lists.
  - Colour is a swatch sidebar.
  - The swatch images are whole-product photos, unreadable at 56 px.
- **Metzler, recommended:**
  - Use cropped material swatches.
  - Make Befestigung visual tiles (Wand / Pfosten / Zaun / Standfuß) with an image and price.
  - Make add-ons cards with a toggle.

### 7. Let users go back and change any step without losing the rest
- **Why:** "Allow users to change previous selections" is NN/g tip 7. https://www.nngroup.com/articles/customization/
- **Metzler, now:** the Kaufberater has "Quiz neu starten". Earlier issues: the step total jumps ("Schritt 1 von 7" → "Schritt 2 von 2").
- **Metzler, recommended:**
  - Use a step list where every step stays clickable.
  - Show the summary ("Ihre Konfiguration") with "ändern" links.
  - Don't show a fixed step total when steps branch.

### 8. Update the price live and highlight the total
- **Why:**
  - Law: § 3 Abs. 3 PAngV says the total must be highlighted when a price is broken down. https://www.gesetze-im-internet.de/pangv_2022/__3.html
  - UX: 67 % of sites show no total estimate near the buy section. https://baymard.com/blog/current-state-ecommerce-product-page-ux
- **Metzler, now:** "Preis wie konfiguriert" sits in the sticky bar. Surcharges sit next to options (+49,99 etc.). Good.
- **Metzler, recommended:**
  - Keep it, with a line-item breakdown in the drawer: Grundpreis, Farbe, Gravur, Zubehör.
  - Show the total in a bold, larger font.
  - Avoid odd cents like "+29,01 €"; they read as a bug.

### 9. Save, reopen and share a configuration without an account
- **Why:** 89 % of sites don't make "Save" easy; 21 % of 1.193 respondents rely on it; a participant gave up because saving required sign-up. https://baymard.com/blog/current-state-ecommerce-product-page-ux
- **Examples:**
  - IKEA planners save with a "Planungscode": https://www.ikea.com/de/de/planners/
  - Porsche offers "Gespeicherte Konfiguration laden": https://www.porsche.com/germany/models/
  - The Siedle IQ planner has "Projektübersicht teilen".
- **Metzler, now:** no save or share found.
- **Metzler, recommended:**
  - Encode the configuration in a URL and add a "Link kopieren / per E-Mail senden" button.
  - Important for couples deciding together, and for installers.

### 10. Show the result at real scale and in context, incl. AR for large items
- **Why:** 42 % of users try to judge size from images; 37 % of sites have no in-scale image. https://baymard.com/blog/current-state-ecommerce-product-page-ux
- **Examples:**
  - DoorBird configurator with AR on a facade photo or the camera (per DoorBird): https://www.doorbird.com/de/configurator
  - 2N AppeAR "Virtuelle Installation": https://www.2n.com/de-DE/online-tools/2n-appear/
- **Metzler, now:** 3D product only, with no environment, no scale reference and no AR.
- **Metzler, recommended:**
  - Phase 1: add a "Maßstab" toggle in 3D (silhouette of a door or an A4 sheet).
  - Phase 2: WebAR (model-viewer, USDZ/GLB) for Briefkasten, Paketbox and Sprechanlage.

### 11. Intercoms: generate a complete, correct system
- **Why:** this is competitor practice.
  - Ritto auto-adds "TwinBus Netzgerät" and "Video-Netzgerät" (https://konfigurator.ritto.de/).
  - Siedle IQ collects resident names per flat (https://iq.siedle.com/de/configurator/quick-selection).
  - Nuki and Ring run a compatibility check first (https://nuki.io/de-de/find-your-solution, https://ring.com/intercom-compatibility-checker).
- **Metzler, now:**
  - The XDM10 variant configurator steps are Montageart → Stromversorgung (+162/+368) → Innenstationen (+279) → Zubehör.
  - The Kaufberater is separate from it.
- **Metzler, recommended:**
  - Start with "Nachrüsten auf vorhandener 2-Draht-Leitung oder Neubau mit LAN?".
  - Then ask for the Wohnungen count. Names per Wohnung feed the engraved Namensschild.
  - Then auto-add the required Netzteil and Innenstationen.
  - Hand off to the phone by QR so the check can be done at the door.

### 12. Disclose the Widerruf exclusion for personalised goods, correctly scoped, before ordering
- **Why (law):**
  - § 312g Abs. 2 Nr. 1 BGB excludes withdrawal for goods made to the consumer's individual choice. https://www.gesetze-im-internet.de/bgb/__312g.html
  - The duty to inform is in Art. 246a § 1 Abs. 3 EGBGB. https://www.gesetze-im-internet.de/bgbeg/art_246a__1.html
  - Name engraving counts, even before production starts (EuGH C-529/19). https://www.it-recht-kanzlei.de/Ausschluss-des-Verbraucher-Widerrufsrechts-Verbraucher-Bestimmung-Personalisierung.html
  - Choosing from options the seller predefines is **not** personalisation (OLG Brandenburg). https://shopbetreiber-blog.de/olg-brandenburg-kein-ausschluss-des-widerrufsrecht-wegen-personalisierung-bei-vorgegebenen-auswahlmoeglichkeiten
- **Metzler, now:** where and how the exclusion appears in the configurator and checkout was not verified.
- **Metzler, recommended:**
  - Next to the engraving input: "Individuell graviert – vom Widerruf ausgeschlossen (§ 312g BGB)".
  - Never apply it to colour or option-only configurations.
  - Repeat it in the checkout summary.

### 13. Offer a proof (Entwurf) and a correction window, framed as a service
- **Why:** Apple's DE shopping help offers self-service "Ändere die Personalisierung". https://www.apple.com/de/shop/help. No published conversion figure was found for proofs.
- **Metzler, now:** "Entwurf vor Fertigung +4,95 €" (3–4 working days, 2 corrections). It is correct and useful, but it reads like a fee for reassurance.
- **Metzler, recommended:**
  - Name it "Persönlicher Gestaltungsservice" and explain when it is needed: small text, logos, emoji, special layouts.
  - Show it at the fit warning (rule 2).
  - Consider making it free above a certain cart value. That is a business decision.

### 14. Carry the personalisation into the cart, summary and confirmation e-mail
- **Why:** § 312j Abs. 2 BGB requires the essential product features immediately before ordering. https://www.gesetze-im-internet.de/bgb/__312j.html. Showing the engraving there is an inference, not a statement in the source.
- **Metzler, now:** not verified (no cart was used).
- **Metzler, recommended:**
  - Show a cart line with the preview thumbnail of the engraving, the text, the font name and an "ändern" link back into the configurator with its state intact.

### 15. Use personalisation as the headline benefit
- **Why:** competitor evidence. Letterman headlines "GRATIS Gravur"; Apple says "kostenlose Gravur". https://www.letterman.de/products/briefkasten-letterman-6-inkl-gravur-led-licht
- **Metzler, now:** whether engraving is included in the "ab" price is not stated prominently on cards.
- **Metzler, recommended:**
  - If included, state it everywhere: "inkl. Lasergravur" badge on cards and in the buy box.
  - If it costs extra, show "Gravur + X €" up front.
