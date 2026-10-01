# Stil – Bildsprache der Metzler-Anschlussschemata

Gilt für jedes neue Schema. Die 5 Referenzschemata in `beispiele/` zeigen den Stil fertig angewendet –
vor einem neuen Schema das ähnlichste öffnen und als Vorbild nehmen.

## 1 · Grundlage: Metzler UI Kit

Farben nur aus `metzler-tokens.css` (im SVG als Hex, weil die Datei eigenständig sein muss):

| Rolle | Token | Hex |
|---|---|---|
| Hintergrund Fläche | `--color-paper` | `#F5F6FA` |
| Überschriften, Gerätetitel | `--color-digital-black` | `#1A171B` |
| Zweitzeilen, Hinweise | `--color-graphite-700` | `#54545C` |
| Zonen-Label, Fußzeile | `--color-graphite-600` | `#6A6A6A` |
| Akzent: Schritt-Badges, Links, Tipps | `--color-teal` | `#015253` |
| Tipp-Kästen | `--color-teal-50` | `#F2F6F6` |
| Haarlinien / Rahmen | `--color-graphite-200` / `-300` | `#E6E6E8` / `#DADADA` |
| Karten | `--color-white` | `#FFFFFF` |

`--color-metzler-rot` nur im Logo (die Geräte bringen ihr Logo selbst mit).
Schrift: `"Helvetica Neue", Helvetica, Arial, sans-serif` (Konstante `FONT`). Für Beschriftungen nur
die Kit-Größen **30 · 24 · 20 · 18 · 16 · 14 · 12 px**: Titel 24 fett, Untertitel 14, Kartentitel 16 fett,
Kartentext 14, Gerätetitel 14 fett, Zweitzeilen/Klemmen/Pills 12. Aufdrucke *auf* Geräten dürfen kleiner
sein – sie bilden den echten Aufdruck nach. Alle Texte auf Deutsch.

## 2 · Fläche und Raster

- Breite **1280 px**, Höhe ergibt sich aus dem Info-Band (≈ 1100–1200). Hintergrund `paper`, Radius 18.
- Kopf: Titel `Anschlussschema · <System> <Situation>` (x 40, y 52), Untertitel (y 76), rechts System-Tags
  (weiße Pills mit Rahmen) und Link „Zum Produkt ↗“ (teal, unterstrichen) auf die Shop-Seite.
- **Zonen** (Radius 12) zeigen, wo montiert wird: „Außen · Hauseingang“, „Wohnbereich“ bzw.
  „Etage · Wohnungen“, „Technikraum · Medienverteiler“ (Fläche `#EEF0F4`). Zonen-Label 12 px fett,
  Versalien, Laufweite 1,2, mit Halo in Zonenfarbe (liegt über Leitungen).
- Zwei erprobte Raster:
  - **A – Tür links** (XDM10-Schemata): Außen x 32 / B 268 · Wohnbereich x 316 / B 932 oben ·
    Technikraum x 316 / B 932 darunter.
  - **B – Tür rechts** (VDM10/SDM10): Wohnbereich x 32 / B 928 oben · Außen x 976 / B 272 ·
    Technikraum x 32 / B 928 darunter.
  - Wahl nach Klemmenlage: Die Türstation kommt auf die Seite, auf der ihr Klemmenplatz liegt (VT6: CH6
    ganz rechts → Tür rechts), damit ihr Kabel keine anderen kreuzt.
- **Info-Band** unten (`S.info_band(...)`): drei weiße Karten gleicher Höhe – „So wird angeschlossen“
  (nummerierte Schritte, gleiche Nummern wie die Badges im Bild), „Wichtig“ (Regeln aus den
  Anleitungen), „Leitungen“ (Legende, optional Zusatzzeilen). Höhe passt sich automatisch an.
- Fußzeile (12 px): Quelle + Stand + „Arbeiten an 230 V nur durch eine Elektrofachkraft.“ (`FOOT`).
- Freie Flächen nutzen für **Tipp-Kästen** (teal-50) oder Tabellen (Drehschalter, Leitungsquerschnitt).

## 3 · Geräte

- Immer aus `scripts/devices.py`, in echten Proportionen (siehe `geraete.md`). Hutschienen-Geräte
  stehen auf einer Hutschiene (`S.din_rail`), Reihenfolge nach Leitungsführung (siehe 5).
- Beschriftung (`S.caption`): Titel 14 fett + Zeilen 12; über Monitoren/Türstationen, unter oder neben
  Hutschienen-Geräten. Inhalte: Produktname, Rolle (Haupt-/Neben-Innenstation, Innenerweiterung,
  Zimmer-Nr.), Kenndaten (24 V DC · 36 W, 4 Kanäle …).
- Zimmernummern auch im Monitor-Display zeigen (`room=`) und an Mehrfach-Tastern als „Zi. 02“.

## 4 · Leitungen (Farbcode – verbindlich)

| Leitung | Darstellung | Pill |
|---|---|---|
| 2-Draht (XDM10-BUS, VDM10/ADM10 2-Draht IP) | Aderpaar **rot + gelb** (`S.pair(..., ('red','yellow'))`) | schwarz „2-Draht“ |
| RS-485 Türstation → Sicherheitsmodul | Aderpaar **grün + weiß** (SDM10-Kabelbaum: C3 grün +, C4 weiß −) | schwarz „RS-485“ |
| Netzwerk Cat 5e–7 | **blaues** Kabel mit RJ45-Stecker (`S.lan`) | blau „LAN · Cat 7“ |
| Kleinspannung DC 12/24/48 V, Türöffner-Kreis | **rot = +, schwarz = −**, Einzeladern genau auf die Klemmen (`S.wire`) | schwarz „24 V DC“ … |
| 230 V AC | **braun = L, blau = N**, Einzeladern auf N/L | schwarz „230 V AC“ |
| WLAN / Internet | teal gestrichelt + WLAN-Symbol (`S.wlan`) | – |

Herkunft: Metzler-Schnellstartanleitungen (Haus-Grafiken: 2-Draht rot/gelb, Cat 7 blau, DC rot/schwarz),
Sicherheitsmodul-Anleitung („N meist blaue Ader, L meist braunes Kabel“). Die XDM10-Topologie-Grafik
zeichnet den Bus rot/schwarz – bewusst nicht übernommen, damit 2-Draht nicht wie DC aussieht.
Bei neuen Leitungsarten eine neue, eindeutige Farbe wählen und in der Legende erklären.

## 5 · Leitungsführung

- Nur waagrecht/senkrecht, Läufe auf eigenen y-Höhen, Pills auf geraden Stücken (nie auf Kreuzungen),
  Schritt-Badge direkt neben der Pill.
- **Kreuzungsfrei ordnen:** Laufen mehrere Kabel von einer Seite herunter, dann waagrecht und wieder
  herunter auf Klemmen, müssen Quellen und Ziele dieselbe Reihenfolge haben (linkeste Quelle → linkestes
  Ziel); bei Lauf nach rechts liegt das Kabel mit der weiter rechts liegenden Quelle höher, bei Lauf
  nach links das mit der weiter links liegenden Quelle. Danach Hutschienen-Reihenfolge wählen (z. B.
  XDM10: Netzteil Modul · Sicherheitsmodul · Netzteil Türöffner · Verteiler · PSU).
- Unvermeidbare Kreuzungen (z. B. MEAN WELL „−V +V“ ↔ Verteiler „+ −“, Brücke +V → DOOR_COM) sind ok:
  `S.wire` zeichnet einen Halo, die Kreuzung wirkt als Brücke. Halo = Zonenfarbe (`halo_z`).
- Aderpaare landen exakt: `S.pair(mittellinie, farben, ends=[ziel_für_farbe1, ziel_für_farbe2])`.
- Kabel zu Monitoren und Türstationen enden an der Unterkante des Geräts (laufen dahinter).
- Klemmen-Beschriftung (`S.tlabel`, 12 fett, Halo): CH1, CH6, IN, OUT, LAN, PoE 1–3, Uplink, COM, NO1 …
- Kaskaden/Erweiterungen als kurzes Kabel + graue Strichellinie mit Pfeil + Text („weitere Etage: OUT → IN“).

## 6 · Ausgabe

- SVG (eigenständig, Fonts per Systemschrift) + **PDF** (Vektor, Schriften eingebettet, Link klickbar;
  Seitengröße = Schema, ≈ 339 × 300 mm, druckt auf A3) + PNG nur zur Kontrolle.
- Dateiname: `<system>-<situation>.svg/pdf`, z. B. `vdm10-mehrfamilienhaus-neo.pdf`.
