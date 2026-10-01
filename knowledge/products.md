# Metzler Shop — Produktwissen (edelstahl-tuerklingel.de)

Stand: 2026-10-01T09:42:25+02:00 · Quelle: https://edelstahl-tuerklingel.de · 1312 Elternartikel · 2143 Kindartikel (Farb- und andere Varianten).

**So benutzen:** Für exakte Werte (Name, Art.-Nr., Preis, Maße, Merkmale, Farben, Bilder) immer `knowledge/products.json` lesen (ein Eintrag je Elternartikel, Varianten unter `variants`). Die Kategorie-Dateien unten sind kompakte Tabellen zum Überblick. Nichts ist geschätzt: fehlt ein Wert im Shop, ist das Feld leer/`null`. Neu erzeugen: `tools/shop-data/README.md`.

**Hinweise:** Art.-Nr. = Hersteller-Artikelnummer (JSON-LD `mpn`, z. B. „smAP_11080“). Die Zeile „Artikelnummer“ auf der Artikelseite zeigt dagegen die interne ID `kArtikel` (Feld `artnr_display`). „ab“-Preise: `price_from` (günstigster Kindartikel) verwenden, nicht `price` der Elternseite. XDM10 PRO wird mit UVP „verbindliches Angebot über Ihren Fachpartner“ gezeigt. Jeder Artikel steht in genau einer Hauptkategorie (Breadcrumb), auch wenn der Shop ihn zusätzlich anderswo listet.

## Kategorien

| Hauptkategorie | Artikel | Kindartikel | Preis von – bis | Median | mit 3D | Entwurf vor Fertigung | Datei |
|---|---|---|---|---|---|---|---|
| Außenleuchten | 349 | 426 | 0,39 € – 257,40 € | 54,99 € | 0 (0 %) | 0 | [aussenleuchten.md](products/aussenleuchten.md) |
| Türklingeln | 295 | 306 | 1,99 € – 199,00 € | 24,95 € | 3 (1 %) | 101 | [tuerklingeln.md](products/tuerklingeln.md) |
| Briefkästen | 196 | 392 | 5,99 € – 2.390,00 € | 109,00 € | 42 (21 %) | 105 | [briefkaesten.md](products/briefkaesten.md) |
| Hausnummern | 134 | 393 | 2,99 € – 299,00 € | 59,99 € | 1 (1 %) | 92 | [hausnummern.md](products/hausnummern.md) |
| Paketboxen | 98 | 212 | 12,99 € – 759,00 € | 319,00 € | 35 (36 %) | 56 | [paketboxen.md](products/paketboxen.md) |
| Sprechanlagen | 88 | 322 | 3,99 € – 2.599,00 € | 699,00 € | 16 (18 %) | 33 | [sprechanlagen.md](products/sprechanlagen.md) |
| Mülltonnenboxen | 81 | 64 | 6,99 € – 2.799,00 € | 799,00 € | 0 (0 %) | 0 | [muelltonnenboxen.md](products/muelltonnenboxen.md) |
| Sicherheitstechnik | 37 | 0 | 9,34 € – 739,50 € | 113,90 € | 0 (0 %) | 0 | [sicherheitstechnik.md](products/sicherheitstechnik.md) |
| Garten | 34 | 28 | 16,99 € – 1.499,00 € | 149,00 € | 0 (0 %) | 0 | [garten.md](products/garten.md) |
| **Gesamt** | **1312** | **2143** | | | **97 (7 %)** | **387** | |

Preise = günstigster Preis je Elternartikel (Elternseite oder Kindartikel), brutto inkl. 19 % MwSt., ohne Konfigurator-Optionen. 3D = Live-3D-Konfigurator auf der Artikelseite.

## Marken (JSON-LD brand)

| Marke | Artikel | Hauptkategorien |
|---|---|---|
| Metzler | 879 | Türklingeln (260), Briefkästen (193), Hausnummern (112), Paketboxen (98), Sprechanlagen (83), Mülltonnenboxen (81), Garten (34), Außenleuchten (18) |
| Paulmann | 84 | Außenleuchten (80), Hausnummern (4) |
| Steinel | 80 | Außenleuchten (77), Hausnummern (3) |
| Nordlux | 68 | Außenleuchten (68) |
| HiLook by HIKVISION | 36 | Sicherheitstechnik (36) |
| Grothe | 30 | Türklingeln (30) |
| EGLO Leuchten | 27 | Außenleuchten (27) |
| Konstsmide | 24 | Außenleuchten (24) |
| Calex | 23 | Außenleuchten (23) |
| Theben AG | 20 | Außenleuchten (20) |
| Metzler & Steinel | 13 | Hausnummern (13) |
| Star Trading | 9 | Außenleuchten (9) |
| Hikvision | 4 | Sprechanlagen (3), Sicherheitstechnik (1) |
| Heidemann | 4 | Türklingeln (4) |
| Wago | 3 | Außenleuchten (3) |
| (keine Angabe) | 2 | Briefkästen (1), Türklingeln (1) |
| Caramba | 2 | Briefkästen (2) |
| Metzler & EGLO | 2 | Hausnummern (2) |
| Mean Well | 2 | Sprechanlagen (2) |

## Serien / Modellfamilien

Erkannt am Produktnamen (Liste in `parse.py`, `SERIES`). Briefkasten- und Klingel-Modelle tragen meist einen Vornamen nach dem „|“ (z. B. „| Siebert“, „| Sena“) — siehe Spalte „Modellnamen“.

| Serie | Artikel | Hauptkategorien | Preis von – bis |
|---|---|---|---|
| VDM10 | 39 | Sprechanlagen (37), Briefkästen (2) | 19,99 € – 1.590,00 € |
| Siebert | 13 | Briefkästen (8), Sprechanlagen (5) | 15,99 € – 1.059,00 € |
| XDM10 | 11 | Sprechanlagen (11) | 19,99 € – 1.999,00 € |
| BK212 | 10 | Briefkästen (10) | 12,99 € – 269,00 € |
| ADM10 | 8 | Sprechanlagen (8) | 149,00 € – 749,00 € |
| XDM10 Pro | 6 | Sprechanlagen (6) | 1.299,00 € – 1.649,00 € |
| SDM10 | 3 | Briefkästen (2), Sprechanlagen (1) | 19,99 € – 2.390,00 € |

**Häufigste Metzler-Modellnamen (Text nach dem letzten „|“, ohne Farb-/Ausstattungszusätze; Anzahl Elternartikel):** Erpo (12), Maxior (12), Neo (9), Bispo (7), Colson (7), Hoffmann (6), Kai (6), Masiva (6), Cube (5), Hermann (5), Siebert (5), Stencil (5), Bispo Max (4), Geo (4), Nexus (4), Prisma (4), Witterungsbeständig (4), Anton (3), Bispo Funk (3), Bispo RE (3), Heidi (3), Kian (3), Lumic (3), Neumann (3), Niko (3), Oltmann (3), Alan (2), Alan Slim (2), Ares Bell (2), Ava Slim (2), Boris (2), Ebenhard (2), Enno (2), Farbwechsel (2), Friesen (2), G (2), Gustav (2), Kasa (2), Magneto (2), Modell-G (2), Paloma (2), Parisa (2), Selma (2), Sena (2), Serie Otis (2), Steinbach (2), Svena (2), Thobe (2), Vera (2), Vitus (2), Wester (2), Z (2), Abakos (1), Adam (1), Albrecht (1), Alma (1), Alves (1), Alvin (1), Ares (1), Ari (1)

## Bestbewertete Artikel

Sortiert nach Anzahl Bewertungen, nur Durchschnitt ≥ 4,5 (Shop-Bewertungen aus JSON-LD `aggregateRating`).

| Name | Kategorie | Bewertung | Anzahl | Preis ab |
|---|---|---|---|---|
| [Metzler Briefkasten aus hochwertigem Stahl \| Siebert](https://edelstahl-tuerklingel.de/metzler-briefkasten-aus-hochwertigem-stahl-siebert) | Briefkästen | 5 | 739 | ab 89,99 € |
| [Metzler Briefkasten austauschbares Namensschild \| Ebenhard](https://edelstahl-tuerklingel.de/metzler-briefkasten-austauschbares-namensschild-ebenhard) | Briefkästen | 5 | 246 | ab 89,99 € |
| [Metzler Paketbox mit Briefkasten \| personalisiert mit Gravur \| Edelstahl-Namensschild \| mit Briefeinwurf \| Bispo 2](https://edelstahl-tuerklingel.de/metzler-paketbox-mit-briefkasten-personalisiert-mit-gravur-edelstahl-namensschild-mit-briefeinwurf-bispo-2) | Paketboxen | 5 | 195 | 329,00 € |
| [Metzler Batterie Empfänger 25 Melodien Funk-Gong](https://edelstahl-tuerklingel.de/metzler-batterie-empfaenger-25-melodien-funk-gong) | Türklingeln | 4,5 | 161 | 29,99 € |
| [Metzler Briefkasten mit Lasergravur \| Hermann](https://edelstahl-tuerklingel.de/metzler-briefkasten-mit-lasergravur-hermann) | Briefkästen | 5 | 158 | 99,99 € |
| [Metzler Namensschild Briefkastenschild aus Edelstahl \| 8,5 x 3 cm](https://edelstahl-tuerklingel.de/metzler-namensschild-briefkastenschild-aus-edelstahl-85-x-3-cm) | Hausnummern | 5 | 147 | 9,99 € |
| [Metzler Türklingel mit Gravur + LED-Taster optional \| Stella](https://edelstahl-tuerklingel.de/metzler-tuerklingel-mit-gravur-led-taster-optional-stella) | Türklingeln | 5 | 147 | ab 24,99 € |
| [Metzler Briefkasten mit zwei Edelstahl-Namensschildern \| personalisiert mit Gravur \| Albrecht](https://edelstahl-tuerklingel.de/metzler-briefkasten-mit-zwei-edelstahl-namensschildern-personalisiert-mit-gravur-albrecht) | Briefkästen | 5 | 125 | ab 99,99 € |
| [Metzler Briefkasten mit Lasergravur \| Stencil](https://edelstahl-tuerklingel.de/metzler-briefkasten-mit-lasergravur-stencil) | Briefkästen | 5 | 100 | 99,99 € |
| [Metzler Standbriefkasten aus hochwertigem Stahl \| Siebert](https://edelstahl-tuerklingel.de/metzler-standbriefkasten-aus-hochwertigem-stahl-siebert) | Briefkästen | 5 | 96 | ab 159,00 € |
| [Metzler Funkklingel kabellos Edelstahl V2A \| Aufputz Türklingel IP67 \| 150m Reichweite \| Vitus](https://edelstahl-tuerklingel.de/metzler-funkklingel-kabellos-edelstahl-v2a-aufputz-tuerklingel-ip67-150m-reichweite-vitus) | Türklingeln | 5 | 93 | ab 79,99 € |
| [Metzler Mülltonnenbox \| 3er \| 240l \| aus Stahl \| rostfrei & massiv \| Türgriff mit Schloss](https://edelstahl-tuerklingel.de/metzler-muelltonnenbox-3er-240l-aus-stahl-rostfrei-massiv-tuergriff-mit-schloss) | Mülltonnenboxen | 5 | 91 | 799,00 € |
| [Metzler Mülltonnenbox \| 4er \| 240l \| aus Stahl \| rostfrei & massiv \| Türgriff mit Schloss](https://edelstahl-tuerklingel.de/metzler-muelltonnenbox-4er-240l-aus-stahl-rostfrei-massiv-tuergriff-mit-schloss) | Mülltonnenboxen | 5 | 81 | 1.039,00 € |
| [Metzler Mülltonnenbox \| 4er \| 240l \| in Holzoptik \| Anthrazit RAL 7016 \| aus Stahl \| rostfrei & massiv \| Türgriff mit Schloss](https://edelstahl-tuerklingel.de/metzler-muelltonnenbox-4er-240l-in-holzoptik-anthrazit-ral-7016-aus-stahl-rostfrei-massiv-tuergriff-mit-schloss) | Mülltonnenboxen | 5 | 72 | ab 1.119,00 € |
| [Metzler Türklingel Weiß austauschbares Namensschild Gravur \| Otto Slim](https://edelstahl-tuerklingel.de/metzler-tuerklingel-weiss-austauschbares-namensschild-gravur-otto-slim) | Türklingeln | 5 | 65 | ab 39,99 € |
| [Metzler VDM10 2.0 Video-Türsprechanlage \| 1 Klingeltaster \| Colson](https://edelstahl-tuerklingel.de/metzler-vdm10-20-video-tuersprechanlage-1-klingeltaster-colson) | Sprechanlagen | 4,5 | 64 | ab 699,00 € |
| [Solar-Hausnummer von Steinel \| Edelstahl \| Dämmerungssensor](https://edelstahl-tuerklingel.de/solar-hausnummer-von-steinel-edelstahl-daemmerungssensor) | Hausnummern | 5 | 60 | ab 107,10 € statt 119,00 € |
| [Namensschild groß 100 x 40 mm \| aus Edelstahl mit Lasergravur](https://edelstahl-tuerklingel.de/namensschild-gross-100-x-40-mm-aus-edelstahl-mit-lasergravur) | Hausnummern | 5 | 58 | ab 14,99 € |
| [Metzer-Namensschild mit Lasergravur aus rostfreiem Edelstahl](https://edelstahl-tuerklingel.de/metzer-namensschild-mit-lasergravur-aus-rostfreiem-edelstahl) | Hausnummern | 5 | 54 | ab 9,99 € |
| [Metzler Funkklingel für Einfamilienhaus \| personalisiert mit Gravur \| Alan](https://edelstahl-tuerklingel.de/metzler-funkklingel-fuer-einfamilienhaus-personalisiert-mit-gravur-alan) | Türklingeln | 5 | 51 | ab 89,99 € |

1096 von 1312 Elternartikeln haben Bewertungen.

## Farben (Werte der Variationsgruppe „Farbe“, Anzahl Elternartikel)

RAL 7016 Anthrazitgrau (271), RAL 9007 Graualuminium (223), DB 703 Eisenglimmer (223), RAL 9005 Tiefschwarz (182), RAL 9016 Verkehrsweiß (172), Edelstahl Gebürstet (87), Schwarz (58), Weiß (52), Wunschfarbe nach RAL (47), Anthrazit (40), Edelstahl gebürstet (37), Silber (15), Grau (10), Grün (7), Rost (7), Sandfarbig (6), Weiss (6), Beige (5), Metallisch Braun (5), Edelstahl (5), Verzinkt (5), Holzoptik (5), Bronze (4), Linen Tex Black (4), Black Satin (3), Braun (2), Blau (2), RAL 7039 Quarzgrau (2), Kupfer (2), Seaside Schwarz (2), Orange (1), Rostoptik (1), Gebürstet Nickel (1), Messing (1), RAL 7012 Basaltgrau (1)

## Datenlage

| Feld | vorhanden bei |
|---|---|
| Preis | 1312 / 1312 |
| Art.-Nr. (mpn) | 1312 / 1312 |
| Maße B×H×T | 979 / 1312 |
| Gewicht | 1176 / 1312 |
| Kurzbeschreibung | 1142 / 1312 |
| Merkmale | 1203 / 1312 |
| Bilder | 1312 / 1312 |
| Bewertung | 1096 / 1312 |
| Farbauswahl (Gruppe „Farbe“) | 373 / 1312 |
| Kindartikel / Varianten | 473 / 1312 |

## Kategorie-Dateien

- [Außenleuchten](products/aussenleuchten.md) — 349 Artikel
- [Türklingeln](products/tuerklingeln.md) — 295 Artikel
- [Briefkästen](products/briefkaesten.md) — 196 Artikel
- [Hausnummern](products/hausnummern.md) — 134 Artikel
- [Paketboxen](products/paketboxen.md) — 98 Artikel
- [Sprechanlagen](products/sprechanlagen.md) — 88 Artikel
- [Mülltonnenboxen](products/muelltonnenboxen.md) — 81 Artikel
- [Sicherheitstechnik](products/sicherheitstechnik.md) — 37 Artikel
- [Garten](products/garten.md) — 34 Artikel

- [Artikel ohne Kategorie / Konfigurator-Bausteine](products/konfigurator-bausteine.md) — 313 Artikel (nicht in den Zählungen oben)
