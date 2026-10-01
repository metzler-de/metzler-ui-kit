# Best practice: Cart & checkout

**Stand: 01.10.2026.**

- Sources were opened on that date, and numbers are quoted as stated.
- Baymard's abandonment survey covers US shoppers.
- EHI figures cover the German market.
- This is not legal advice.
- **Limits of what was checked:**
  - No cart or checkout was used, so the Metzler checkout itself (guest option, steps, fields, order button) was **not verified**.
  - The current state below comes from public pages: https://edelstahl-tuerklingel.de/zahlung-und-versand and the footer.

**Metzler public facts (01.10.2026)**

- **Shipping:**
  - DE/AT: free from 99,00 €, otherwise 4,95 €.
  - EU: 9,90 €.
  - GB: 19,90 €.
  - DPD Sperrgut (bulky goods): 29 € (up to 30 kg) to 174 €.
- **Delivery time:** 1–3 working days in DE.
- **Payment methods:**
  - Vorkasse, Kreditkarte.
  - Klarna: Sofort / Rechnung / Ratenkauf / Lastschrift / Kreditkarte.
  - Amazon Pay.
  - PayPal: Express, Später bezahlen, Apple Pay, Google Pay, SEPA.
  - Mollie Klarna Rechnung.
  - **Direct "Rechnung" is only for Behörden und öffentliche Institutionen.** The top-bar USP "Kauf auf Rechnung" therefore depends on Klarna.
- **Withdrawal button:** the footer has a "Vertrag widerrufen" button, linking to /online-widerrufsformular.
- **Login flyout:** shows only "Neu hier? Jetzt registrieren!".

---

### 1. All costs visible before checkout: shipping on the PDP and in the cart
- **Why:**
  - Baymard abandonment reasons, with "just browsing" excluded:
    - "Extra costs too high" **40 %**
    - Couldn't see the total up front **12 %**
  - Average documented abandonment is **70,22 %**.
  - Source: https://baymard.com/lists/cart-abandonment-rate
  - Law: § 6 PAngV (VAT and shipping costs). https://www.gesetze-im-internet.de/pangv_2022/__6.html
- **Example:** https://www.hornbach.de/projekte/. The footer reads "Alle Preise inkl. MwSt. und ggf. zzgl. Versandkosten".
- **Metzler, now:** the PDP shows "zzgl. Versand" and "Gratis Versand · ab 99 €". The DPD Sperrgut surcharge (29–174 €) appears only on the shipping page.
- **Metzler, recommended:**
  - In the cart, show a shipping line with the exact amount.
  - Show a Sperrgut note on affected PDPs, such as Standbriefkästen, Paketboxen and Mülltonnenboxen.
  - Never show the Sperrgut surcharge for the first time at payment.

### 2. Guest checkout as the most prominent option
- **Why:**
  - **18 %** abandoned because they had to create an account (1.026 US adults).
  - **62 %** of sites fail to make guest checkout the most prominent option.
  - Source: https://baymard.com/research-articles/current-state-of-checkout-ux
  - Earlier survey: **24 %** abandoned due to forced account creation. https://baymard.com/blog/make-guest-checkout-prominent
- **Example:** Siedle's label service offers "Als Gast fortfahren". https://iq.siedle.com/de/labelling-service/start
- **Metzler, now:** not verified. The login flyout pushes "Jetzt registrieren!". /kundenbewertungen says only buyers with an account can review, which suggests that an account is pushed.
- **Metzler, recommended:**
  - Put "Als Gast bestellen" first, as a primary button.
  - Offer the account afterwards (rule 3).
  - Collect reviews by e-mail link after delivery, independent of any account.

### 3. Offer account creation on the confirmation page
- **Why:**
  - **42 %** of sites interrupt users before or during checkout to suggest an account. https://baymard.com/blog/delayed-account-creation
  - **84 %** fail to offer delayed account creation. https://baymard.com/research-articles/checkout-flow-average-form-fields
- **Metzler, recommended:** on the "Danke" page, offer "Passwort festlegen – Bestellung verfolgen, Gravur-Entwurf freigeben". The second item is a real benefit for engraved orders.

### 4. Minimal form: 7–8 fields is achievable
- **Why:**
  - An ideal checkout can have 12–14 form elements (7–8 fields). The US average is 23,48 elements. https://baymard.com/lists/cart-abandonment-rate
  - The 2024 average is 5,1 steps and 11,3 fields; field count matters more than step count. https://baymard.com/research-articles/checkout-flow-average-form-fields
- **Metzler, recommended:**
  - Put address autocomplete on the street field.
  - Make the phone number optional, with a reason ("nur für Rückfragen des Paketdienstes").
  - Hide "Firma" behind "Ich bestelle als Firma". When it is ticked, show the USt-IdNr. field.

### 5. Collapse rare fields; billing address defaults to delivery address
- **Why:**
  - **30 %** of participants stopped at "Address Line 2".
  - Coupon fields send users off to search for codes.
  - 24 % of sites assume different billing and shipping addresses by default.
  - Source: https://baymard.com/research-articles/checkout-flow-average-form-fields
- **German caveat:** Baymard recommends a single name field. German checkouts usually split Vorname/Nachname. A/B test it; don't copy blindly.
- **Metzler, recommended:**
  - Put "Adresszusatz hinzufügen" behind a link.
  - Put "Gutschein einlösen" behind a link.
  - Check "Rechnungsadresse = Lieferadresse" by default.

### 6. Mark required and optional fields; write specific error messages
- **Why:**
  - **32 %** missed a required field when only optional fields were marked.
  - **61 %** of sites don't mark both.
  - **94 %** of sites don't use adaptive error messages.
  - Source: https://baymard.com/research-articles/current-state-of-checkout-ux
- **Metzler, recommended:**
  - Mark fields "Pflichtfeld" / "optional".
  - Write errors that name the problem and the fix, e.g. "Bitte Hausnummer ergänzen (z. B. 12a)".

### 7. Delivery as a date, including engraving production time
- **Why:**
  - **48 %** of sites show a speed, not a date.
  - **83 %** don't show the order cut-off as a countdown.
  - **20 %** of shoppers abandon because delivery is too slow.
  - Sources: https://baymard.com/research-articles/current-state-of-checkout-ux and https://baymard.com/lists/cart-abandonment-rate
- **Example:** OBI shows "Bestelle bis 13:00 Uhr" with a countdown. https://www.obi.de/p/8390452/burg-waechter-briefkasten-modena-3857-edelstahl
- **Metzler, now:** variant PDPs show "Versanddatum 05.10.–07.10.2026". The shipping page says "1-3 Werktage".
- **Metzler, recommended:**
  - Cart and checkout show "Lieferung voraussichtlich Do., 9.10. – Mo., 13.10. (inkl. Gravur-Fertigung)".
  - If the cart mixes products with different lead times, show a date per item or split shipments.

### 8. Payment mix: Rechnung and PayPal prominently at the top
- **Why:**
  - EHI 2026 (2025 data, 172 retailers), share of German online revenue:
    - PayPal **28,7 %**
    - Rechnung **26,1 %**
    - Lastschrift 14,4 %
    - Karten 13,7 %
    - Ratenkauf 4,7 %
    - Vorkasse 3,5 %
    - Apple Pay 1,3 %
    - Source (trade-press report): https://www.it-finanzmagazin.de/online-payment-rechnungskauf-und-paypal-weiter-dominierend-laut-ehi-studie-online-payment-2026-244098/
    - EHI 2025 press release: https://www.ehi.org/presse/paypal-festigt-spitzenposition/
  - Bitkom (2022): 32 % prefer invoice, and **48 % of over-65s** do. That age group matters for doorbells and mailboxes. https://www.bitkom.org/Presse/Presseinformation/So-bezahlen-Online-Shopper-am-liebsten
- **Example:** https://www.otto.de/bezahlung/ explains Rechnung (with a credit check) with 30 days to pay.
- **Metzler, now:** Rechnung exists via Klarna, Mollie-Klarna and PayPal "Später bezahlen". Direct Rechnung is for Behörden only.
- **Metzler, recommended:**
  - Order the methods: PayPal → Rechnung (Klarna) → Lastschrift → Karte → Apple/Google Pay → Ratenkauf → Vorkasse.
  - Label the provider honestly: "Rechnung (über Klarna)".
  - Show "Rechnung für Behörden & öffentliche Auftraggeber" as a separate B2B method.
  - Consider a B2B invoice provider. Knobloch uses Billie (see `../competitors.md`).

### 9. Legal sequence of the order process (§ 312j BGB)
- **What the law requires:**
  - Abs. 1: show payment methods and any delivery restrictions at the latest when ordering begins.
  - Abs. 2: show a summary (essential features, total price, shipping, term) **immediately above** the button.
  - Abs. 3: the button must read "zahlungspflichtig bestellen" or something equally unambiguous.
  - Abs. 4: otherwise no contract is formed.
  - Source: https://www.gesetze-im-internet.de/bgb/__312j.html
- **Metzler, now:** not verified (no checkout was used).
- **Metzler, recommended:**
  - Final step order: summary with engraving thumbnail and text → total → "Jetzt zahlungspflichtig bestellen".
  - Nothing between the summary and the button except the checkboxes that are legally needed.

### 10. Widerrufsbutton (§ 356a BGB, mandatory since 19.06.2026)
- **What the law requires:**
  - A "Vertrag widerrufen" button, available throughout the withdrawal period, prominent and easy to reach.
  - It asks only for name, contract identification and where to send the receipt.
  - A second button, "Widerruf bestätigen".
  - A receipt sent on a durable medium.
  - It must not sit behind a login if ordering didn't require one.
  - If the Widerrufsbelehrung doesn't mention the function, the withdrawal period can extend to 12 months and 14 days.
  - Sources:
    - https://www.gesetze-im-internet.de/bgb/__356a.html
    - https://shopbetreiber-blog.de/ab-19.6.2026-der-widerrufsbutton-kommt
    - https://www.verbraucherzentrale.de/wissen/vertraege-reklamation/kundenrechte/widerrufsbutton-ab-juni-2026-onlinevertraege-einfacher-widerrufen-118449
    - https://itmr-legal.de/blog/widerrufsbutton-356a-bgb
- **Example:** otto.de, thomann.de, manufactum.de and hornbach.de all show "Vertrag widerrufen" in the footer.
- **Metzler, now:** the footer button exists (teal) and leads to /online-widerrufsformular.
- **Metzler, recommended:**
  - Keep the footer button in every new page footer. It is canonical in the kit footer.
  - Check the form against the 3-data-item rule and the two-step confirmation.
  - Check that old § references in the AGB and Widerrufsbelehrung were updated after the renumbering.

### 11. Trust at the payment step
- **Why:**
  - **19 %** didn't trust the site with card details; 13 % abandoned over the returns policy. https://baymard.com/lists/cart-abandonment-rate
  - NN/g "upfront disclosure" covers contact details, fees, returns and guarantee links. https://www.nngroup.com/articles/trustworthy-design/
- **Metzler, recommended:** in the checkout sidebar, show:
  - "4,7 ★ aus 36.785 Bewertungen" (link to Trusted Shops)
  - Hotline +49 7121 317 7310 (Mo–Fr)
  - Payment logos
  - "Rückgabe: 14 Tage, gravierte Artikel ausgenommen"
  - Keep the checkout header minimal, with no mega menu.

### 12. Progress towards free shipping in the cart
- **Why:** this is an example only; no verified effect size was found. mymuesli's cart shows "Noch 59 € für GRATIS Versandkosten". https://www.mymuesli.com/pages/mixer
- **Metzler, now:** the threshold is 99 € (DE/AT).
- **Metzler, recommended:**
  - Show a progress bar: "Noch 14,01 € bis zum Gratis-Versand".
  - Suggest add-ons that make sense: Hausnummer, Montageset, Edelstahl-Pflegeset.
  - Don't suggest unrelated sale items.

### 13. Quantity steppers in the cart
- **Why:** **97 %** of sites don't use +/- buttons with an editable field. https://baymard.com/research-articles/current-state-of-checkout-ux
- **Metzler, recommended:** use a kit stepper. For engraved items, a quantity above 1 should ask "gleiche Gravur?"

### 14. Price reductions: base the strike price on the 30-day lowest price
- **Law:**
  - § 11 PAngV. https://www.gesetze-im-internet.de/pangv_2022/__11.html
  - EuGH C-330/23 (Aldi Süd, 26.09.2024): percentage discounts must be based on that lowest price. https://curia.europa.eu/site/upload/docs/application/pdf/2024-09/cp240152de.pdf
- **Metzler, now:**
  - Promo cards show "Gültig bis: 15.10.2026 – 10%" with strike prices.
  - Running promos: Steinel Brand Weeks; 15 % on Sicherheitstechnik until 31.10.2026.
- **Metzler, recommended:**
  - Every strike price in cart and checkout must equal the 30-day low.
  - Label it "Niedrigster Preis der letzten 30 Tage: …" where it differs from the UVP.
