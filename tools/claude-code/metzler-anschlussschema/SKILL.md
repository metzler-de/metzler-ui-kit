---
name: metzler-anschlussschema
description: Erstellt technisch korrekte Metzler-Anschlussschemata als PDF (plus SVG) im Stil des Metzler UI Kit – Türstationen, Innenstationen, Verteiler, Netzteile, PoE-Switches, Sicherheitsmodul, Türöffner, Exit-Taster mit farbcodierten Leitungen, Klemmenbeschriftung und Info-Band. Für XDM10 2-Draht-BUS, VDM10 2.0 (2-Draht IP und LAN/PoE), ADM10 und SDM10, auch Paketbox und Briefkasten mit Sprechanlage. Verwenden bei Anschlussschema, Anschlussplan, Verdrahtungsplan, Schaltplan, Installationsschema, Topologie, Verkabelung, wiring diagram, connection scheme oder „wie wird … angeschlossen“ für Metzler-Sprechanlagen.
---

# Metzler-Anschlussschema

Dieser Skill erzeugt ein Anschlussschema wie die 5 Referenzen in `beispiele/`. Er bündelt drei Dinge:

- die Bildsprache des Metzler UI Kit,
- die Anschlussregeln aus allen Metzler-Anleitungen (Shop-PDFs, Stand 09/2026),
- eine Python-Bibliothek, die Geräte maßstäblich zeichnet und das Ergebnis als Vektor-PDF ausgibt.

Pfade in diesem Dokument sind relativ zum Ordner dieser Datei (`<skill>`).

| Datei | Inhalt |
|---|---|
| `references/systeme.md` | **Anschlussregeln je System** mit Quellen, Grenzwerten, Klemmen, Widersprüchen, Prüfliste |
| `references/stil.md` | Bildsprache: Kit-Tokens, Schriftgrößen, Raster, Zonen, **Leitungsfarben**, Leitungsführung |
| `references/geraete.md` | Gerätekatalog: Funktion in `devices.py` ↔ Produkt/Artikel, Maße, Anker |
| `references/quellen.md` | Produkte, Konfigurator-Optionen, alle 57 PDFs mit Links, Recherche-Methode |
| `scripts/scheme.py` | `Scene`: Zonen, Geräte, Leitungen, Pills, Schritte, Info-Band, Layout-Prüfung, PDF-Export |
| `scripts/devices.py` | alle Geräte als SVG in Millimetern (nach Shop-Fotos) |
| `scripts/referenz.py` | Code der 5 Referenzschemata – beste Vorlage für ähnliche Fälle |
| `scripts/neues_schema.py` | kommentierte, lauffähige Minimal-Vorlage |
| `scripts/build.py` | baut SVG + PDF (+ PNG) und meldet Layout-Fehler |
| `beispiele/` | die 5 Referenzen als SVG, PDF und PNG |

Die Referenzschemata:

| id | Situation |
|---|---|
| `xdm10-einfamilienhaus` | XDM10 MAXIOR · VT4 + PSU36 · 2 Innenstationen in Reihe · Sicherheitsmodul + Türöffner mit eigenen 12-V-Netzteilen |
| `xdm10-mehrfamilienhaus` | XDM10 MAXIOR 3 Taster · XDM10-VT8 + 48 V 150 W · Stockwerksverteiler mit 4 Innenstationen (3 Wohnungen + Innenerweiterung) |
| `vdm10-2-draht-ip` | VDM10 2.0 2-Draht IP · Türstation an CH6 · 3 Innenstationen sternförmig an CH1–CH3 · 24-V-Trafo · Router am LAN-Port |
| `vdm10-lan-poe` | VDM10 2.0 LAN/PoE · Türstation + Home/Pro/Ultra am PoE-Switch · Uplink Router · Türöffner mit eigenem 12-V-Netzteil |
| `sdm10-sicherheitsmodul` | SDM10X · SDM10-TRAFO 12 V · LAN zum Gigabit-PoE-Switch · Sicherheitsmodul (RS-485) + Türöffner mit eigenen 12-V-Netzteilen |

## Ablauf

1. **Anfrage verstehen.** Benötigt werden:
   - Produkt/System (Name oder Shop-Link) und Variante (2-Draht IP oder LAN/PoE).
   - Zahl der Taster bzw. Wohnungen.
   - Innenstationen: Modell, Anzahl, Haupt oder Erweiterung.
   - Türöffner: Wege und Spannung.
   - Extras: Sicherheitsmodul, Exit-Taster, Türkontakt, Etagenruf, Router/App, Kaskade, Paketbox.

   Nur nachfragen, was sich weder aus der Anfrage noch aus der Produktseite ergibt. Sonst sinnvolle
   Standards wählen und im Info-Band nennen. Standards:
   - Türöffner über das Sicherheitsmodul.
   - Je Tür 12-V-Netzteile für Modul und Öffner.
   - Innenstation Home 7″ weiß.
2. **Regeln laden.** Aus `references/systeme.md` lesen:
   - § 0 und den Abschnitt des Systems,
   - § 6 bei Türöffnern,
   - § 9 (Widersprüche).

   Grenzwerte prüfen: Kanäle, Watt, Daisy-Chain, Kaskade, Leitungslängen, Modulanzahl. Ist die Anfrage
   so nicht zulässig, dem Nutzer die korrekte Lösung vorschlagen, statt sie falsch zu zeichnen.
   Fehlt ein Fakt, im passenden PDF nachlesen (Links in `quellen.md`) und mit Quelle in `systeme.md`
   ergänzen. Nie raten.
3. **Geräte wählen** aus `references/geraete.md`. Fehlt ein Gerät, nach der Methode dort ergänzen
   (Shop-Foto, Maße, Vergleichsrender). Nie frei skizzieren.
4. **Layout planen** nach `references/stil.md`:
   - Raster A (Tür links) oder B (Tür rechts), je nach Klemmenlage.
   - Zonen: Außen, Wohnbereich, Technikraum.
   - Hutschienen-Reihenfolge kreuzungsfrei.

   Die ähnlichste Referenz als PNG ansehen und ihren Code in `scripts/referenz.py` lesen.
5. **Schema schreiben.** `scripts/neues_schema.py` oder die passende Referenzfunktion als neue Datei in
   den Arbeitsordner kopieren, nie im Skill-Ordner ändern. Dann anpassen:
   - Funktionsname, Szenen-Präfix, `SCHEMES`-Eintrag.
   - Geräte, Leitungen, Pills, Schritt-Badges.
   - Info-Band: Schritte, Hinweise aus `systeme.md`, Legende.
6. **Bauen und prüfen**, bis nichts mehr zu korrigieren ist:
   ```bash
   python3 <skill>/scripts/build.py --module mein_schema.py --out <zielordner> --png
   ```
   - Jede `⚠`-Warnung beheben: Text-Überlappung, Text auf einem Gerät, Text außerhalb.
   - Das PNG ansehen, Ausschnitte vergrößern (Klemmen, Pills, Kreuzungen, Info-Band).
   - Die Prüfliste `systeme.md` § 10 abhaken.
7. **Abgeben.**
   - Das **PDF** (Vektor, Schriften eingebettet, Produktlink klickbar) und das SVG liegen im Zielordner.
     Ohne Ordnerangabe in den aktuellen Arbeitsordner, Dateiname `<system>-<situation>.pdf`.
   - Dazu eine kurze Antwort in der Sprache des Nutzers: was gezeigt wird, getroffene Annahmen,
     wichtige Grenzwerte.
   - PNG nur zur eigenen Kontrolle, nicht als Ergebnis.

## Regeln, die nie gebrochen werden

- **Technik nur aus `systeme.md`.** XDM10 und VDM10 nie mischen.
  - VDM10 2-Draht: Türstation an **CH6**, sternförmig, Trafo **24 V DC 36 W**.
  - XDM10: max. 4 Innenstationen je PSU36, Daisy-Chain ≤ 4.
  - SDM10: **kein PoE** an der Türstation.
  - Sicherheitsmodul: nur 12-V-DC-Öffner und das letzte Gerät am RS-485-Bus.
- **Geräte nur aus `devices.py`**, in echten Proportionen und mit der Shop-Optik.
- **Leitungsfarben:**

  | Leitung | Darstellung |
  |---|---|
  | 2-Draht | Paar rot + gelb |
  | RS-485 | Paar grün + weiß |
  | LAN | blau mit RJ45 |
  | DC | rot + / schwarz − |
  | 230 V | braun L / blau N |
  | WLAN | teal gestrichelt |

  Jede Leitung endet auf ihrer Klemme und ist beschriftet. Die Legende erklärt jede verwendete Art.
- **Nur Metzler-UI-Kit-Tokens** (`stil.md` § 1). Schriftgrößen nur 30 · 24 · 20 · 18 · 16 · 14 · 12 px.
  `--color-metzler-rot` nur im Logo. Das Metzler UI Kit ist die einzige Design-Quelle; den
  MCP-Connector „Metzler Design System“ nicht verwenden.
- **Alle Texte im Schema auf Deutsch.** Fußzeile mit Quelle, Stand und dem Hinweis „Arbeiten an 230 V
  nur durch eine Elektrofachkraft.“ (`FOOT`).
- Kein Schema ohne Bau-Lauf ohne Warnungen und ohne Sichtprüfung des PNG.

## Werkzeuge

- Python ≥ 3.9 (nur Standardbibliothek).
- `rsvg-convert` (librsvg) für PDF/PNG – macOS: `brew install librsvg`. Fehlt es, erzeugt `scheme.py`
  PDF und PNG über Google Chrome headless.
- Schrift Helvetica Neue (macOS). Andere Systeme fallen auf Arial zurück; die Textbreiten in `text_w`
  sind auf Helvetica abgestimmt, daher das PNG genau prüfen.
- Referenzen neu bauen: `python3 <skill>/scripts/build.py --out <skill>/beispiele --png`.

## Pflege

- Neue Erkenntnisse (Regel, Gerät, Widerspruch) immer in `systeme.md`, `geraete.md` oder `quellen.md`
  nachtragen, mit Quelle.
- Ein neues Referenzschema als Funktion in `referenz.py` ergänzen, mit Eintrag in `SCHEMES`. Dann
  `beispiele/` neu bauen.
- Die Kit-Seite zeigt den Skill im Abschnitt „Anschlussschemata“ (`#anschlussschemata`). Ändert sich
  etwas, das dort steht (Systeme, Beispiele), gilt das Änderungsprotokoll des Kits: `index.html`,
  CHANGELOG, `.md`-Exporte.
