# Systeme – Anschlussregeln (verbindlich)

Vor jedem Schema: System bestimmen (§ 0), alle Regeln des Systems lesen, Grenzwerte gegen die Anfrage
prüfen. Verstößt die Anfrage gegen eine Regel, **nicht „passend zeichnen“**, sondern dem Nutzer die
korrekte Lösung vorschlagen (z. B. „mehr als 4 Innenstationen → Set 8 Anschlüsse statt VT4“).
Widersprechen sich Quellen, gilt § 9. Jede Regel trägt ihre Quelle (Kürzel + Seite). Seitenzahlen sind
die gedruckten Seiten, nur bei VS, AS und V1 die PDF-Seiten (VS: gedruckt = PDF − 7).

| Kürzel | Dokument (Shop-Download, Stand 09/2026) |
|---|---|
| XI | Systemanleitung XDM10 Innenstation (`Systemanleitung_XDM10_M_IS_EK.pdf`) |
| XT | Systemanleitung XDM10 MAXIOR Türstation (`Systemanleitung_XDM10_M_TS_EK.pdf`) |
| XQ / XM / XD | QSG XDM10 MAXIOR · Montageanleitung XDM10 · Datenblatt XDM10-MAXIOR |
| VS | Systemanleitung VDM10 2.0 (`Systemanleitung_VDM10.pdf`, Stand 12/2025) |
| V2 / V1 | Anleitung VDM10 2.0 · Anleitung VDM10 Altgeneration (11/2022) |
| VQ / AV / CL | QSG VDM10 · Anschlussvorgaben 2-Draht IP + LAN/PoE · Checkliste Sprechanlagen VDM10/ADM10 |
| AS / AD | Systemanleitung ADM10 3.0 · Datenblatt ADM10 |
| SD / SQ / SP | Systemanleitung SDM10 · QSG SDM10 · Leitungswahl Stromversorgung SDM10 |
| HB / S250 | Anleitung SDM10H-Beleuchtung · Montageanleitung Stele S250 (SDM10S) |
| SM | Anleitung Sicherheitsmodul VDM10 |
| HW | Hinweise zur Komponentenauswahl und Installation |
| NEO / KAI / RGB | Klingeltastenzuweisung VDM10-Neo · ADM10-NT (Kai) · Drucktaster D19-TF-RGB |
| Shop | Produkt- und Konfiguratorseiten edelstahl-tuerklingel.de |

Links und Fundstellen aller PDFs: `quellen.md`.

## 0 · Welches System?

| System | Produkte | Verkabelung | Zentrale |
|---|---|---|---|
| **XDM10 · 2-Draht-BUS** | MAXIOR 1–3 Taster, Paketbox Zivo 2 · 2-Draht-BUS | 1 Aderpaar, auch Bestandsleitung, Daisy-Chain | XDM10-VT4 + PSU36 (48 V 36 W) oder XDM10-VT8 + 48 V 150 W |
| **VDM10 2.0 · 2-Draht IP** | Colson, Kian, Niko, Neo, Horizon, Briefkasten BK212/Siebert, Paketbox 37175 (Variante 2-Draht) | Stern, 1 Aderpaar je Gerät | VDM10-VT6-2.0 + VDM10-TRAFO 24 V 36 W |
| **VDM10 2.0 · LAN/PoE** | dieselben (Variante LAN/PoE), Zivo 2 · LAN/PoE, Bispo 2 | Netzwerkkabel je Gerät | PoE-Switch 802.3af |
| **ADM10 · Audio** | Dominik, Kai 1–6 | wie VDM10 (LAN/PoE oder 2-Draht IP, Mischbetrieb) | wie VDM10 |
| **SDM10** | SDM10X, SDM10H, SDM10S | LAN – **kein PoE an der Türstation** | 12-V-Netzteil + PoE-Switch für die Innenstationen |

- XDM10 ist ein geschlossenes System: **nicht mit VDM10 2-Draht mischbar** (XI S. 3–4).
  Es gibt keine interne Anwahl zwischen Innenstationen (XT S. 9).
- VDM10 1.0 und 2.0 (2-Draht) sind **nicht kompatibel**, ebenso VDM10 1.0 und ADM10 2.0 (VS S. 23, AS S. 21).
  Altgeräte heißen ohne „-2.0“, z. B. VDM10-VM-2-Draht (V1 S. 9–10).
- VDM10 (ab FW V2.2.3, Protokoll 2.0), ADM10 und SDM10 laufen im Verbund. Jede kann Haupttürstation sein
  (VS S. 16, 59; AS S. 15; SD S. 9).

## 1 · XDM10 · 2-Draht-BUS

**Komponenten und Netzteil**
- Alle Geräte erhalten Daten **und** Versorgung über 1 Aderpaar. Das Kabel nie unterbrechen (XI S. 3).
  Die Polung an den 2-Wire-Klemmen ist beliebig (XQ S. 2).
- **Set „4 Anschlüsse“** (44301) besteht aus XDM10-VT4 (CH1–CH4, kein IN/OUT) und **XDM10-PSU36**
  (48 V 0,75 A 36 W, MEAN WELL HDR-30-48).
  - Türstation an CH1–CH4, Innenstationen an CH1–CH4.
  - Je Kanal 2 Türstationen bzw. bis 4 Innenstationen; an CH1–CH4 zusammen max. **30 W** (XI S. 3–4).
- Ein Netzteil versorgt 1 Türstation + bis 4 Innenstationen. Es gilt 1 Verteiler je Netzteil.
  Das Netzteil muss Metzler-zertifiziert sein (XI S. 2–3).
- **Set „8 Anschlüsse“** (44768) = **XDM10-VT8** (IN, OUT, CH1–CH6) + Transformator 48 V 150 W
  (MEAN WELL HDR-150-48), für mehr als 4 Innenstationen (Shop, XD).
- **Stockwerksverteiler XDM10-VTS** (44779): IN/OUT + 4 Kanäle für Innenstationen (Aufdruck „MAX 20W“).
  Er hat kein eigenes Netzteil und wird kaskadiert (OUT → IN), **bis 16 je Gebäude** (XI S. 3, Shop).

**Verkabelung**
- **Daisy-Chain:** 2-Draht-IN (Klemmen 5/6, 48 VDC 0,4 A) → OUT (3/4, 48 VDC 0,3 A) → nächste IN.
  Max. **4 Innenstationen** hintereinander; mindestens eine hängt direkt am Verteiler
  (XI S. 3 und S. 11, XQ S. 2). Klemme 1 = GND, 2 = Etagenruf (Taster an GND + Call Floor).
- Leitungen (XI S. 3) – nur **1 Aderpaar** je Kabel, Schirm empfohlen, **keine Netzwerkkabel**
  (> 42 Ω/100 m), 230-V-Leitungen ≥ 0,5 m entfernt, Verteiler in Medienverteiler.

  | Strecke | parallel 0,5–1,5 mm² | TP 0,28 mm² / 1 mm² |
  |---|---|---|
  | VT4 → Innenstation | ≤ 60 m | ≤ 40 m |
  | Innenstation → Innenstation | ≤ 100 m | ≤ 80 m |
  | VT4 → Türstation | ≤ 60 m | ≤ 60 m |

- Vor dem Einbau Signalqualität im „fliegenden Aufbau“ messen (XI S. 2).

**MAXIOR-Klemmen** (XT S. 15)

| Klemme | Belegung |
|---|---|
| A1–A4 | 485− / 485+ / 12 V OUT / GND – Ausgang Module |
| B1 / B2 / B3 | NC / NO / COM – Türöffner 2, ab Werk inaktiv, erst freischalten |
| B4 | LOCK1 – Türöffner 1, spannungsgeführt 20 V 4 A Impuls, 300 mA Haltestrom, max. 30 Ω (XD) |
| B5 / B6 | 485 reserviert |
| B7 / B8 | 12 V DC IN (Stabilisierung bei langen/alten Leitungen) / GND |
| B9 / B10 | AIN1 / AIN2 – Alarm oder Exit-Taster |
| C | 2-Wire |

- Relaisausgang max. 30 V DC / 1 A. Versorgung 48 V über VT4/VT8 oder 12 V DC, ≤ 6 W (XD).
- Module über RS-485 in Reihe: Ausgang → Eingang des Namensschild-Moduls NEO-K12 (A1 RS-485−, A2 +,
  A3 12 V IN, A4 GND; B1–B4 = Ausgang).
- Modul-DIP: 1–4 = Adresse 1–8 (jede nur einmal), 5–7 reserviert, 8 = 120 Ω für Leitungen > 30 m (XT S. 15–17).
- Türöffner: am sichersten über das Sicherheitsmodul (§ 6). LOCK1 ist ab Werk aktiv und direkt nutzbar,
  wenn der Öffner passt (XT S. 16). Metzler-Beispiel EFH: 2 Türen, 2 × Sicherheitsmodul,
  4 × 12 V DC 24 W (XT S. 10).

**Drehschalter**
- **Türstation** (XT S. 11–12, XI S. 7, XQ S. 1–2):
  - Gebäude-Nr. 01 bei Einzelgebäude.
  - Türstation-Nr.: 0 = Haupt, 1–16 = Neben, 90–99 = äußere Türstation.
  - Türöffnungszeit (für beide Relais): 0 = 2 s, 1 = 1 s, 2 = 3 s, 3 = 4 s, 4 = 5 s, 5 = 8 s, 6 = 10 s,
    7–9 reserviert.
  - Werkseinstellung: Gebäude 1, Öffner 3 s.
- **Innenstation** (XQ S. 1–2):
  - Innenerweiterung: 0 = Haupt, 1–3 = Erweiterung.
  - Gebäude-Nr. 1–99; alle Geräte haben dieselbe Gebäude-Nr.
  - Zimmer-Nr. ab Werk 03.
  - Eine Erweiterung bekommt **dieselbe** Gebäude- und Zimmer-Nr. wie die Innenstation, mit der sie klingelt.
  - Bis 3 Erweiterungen je Innenstation (XI S. 2).
  - Danach koppeln: beliebige Klingeltaste ca. 10 s halten (XQ S. 2).
- **Zimmer-Nr. je Klingeltaster** (XM S. 2, von oben):

  | Taster | Zimmer-Nr. |
  |---|---|
  | 1 | 03 |
  | 2 | 02, 04 |
  | 3 | 02, 04, 06 |
  | 4 | 03–06 |
  | 5 | 02–06 |
  | 6 | 01–06 |

- **Eco-Modus** (DIP-1 = 0, Werk): Es ist nur ein Display gleichzeitig aktiv. Erweiterungen klingeln,
  das Bild kommt erst bei Annahme.
- **Komfort-Modus** (DIP-1 = 1): nur mit externem 12 V DC 1 A an „Ex. Power“.
- DIP-2 = 1: automatische Türöffnung (XI S. 2, S. 9).

## 2 · VDM10 2.0 · 2-Draht IP

- **Nur sternförmig:** Jedes Gerät hat ein eigenes Kabel. Durchschleifen über weitere Adern desselben
  Kabels führt zu Abbrüchen (VS S. 12, AV S. 1).
- Komponenten (VS S. 12):
  - Türstation VDM10-VM-2W-2.0.
  - Innenstation **nur Home** VDM10-IS-W/-SC-2W-2.0; Pro und Ultra gibt es nur mit LAN.
  - Verteiler **VDM10-VT6-2.0** + **VDM10-TRAFO 24 V DC 36 W** (Hutschiene).
  - Nur ein Metzler-zertifiziertes Netzteil (VS S. 13).
- **Türstation an CH6 (16 W)**, Innenstationen an CH1–CH5 (je 6 W) (VS S. 13, S. 18; V1 S. 15).
  Türstation inkl. Module < 12 W (VM 4 W, Touch-Display 4 W, FP-RFID 4 W, Namensschild 2 W);
  VM + Touch-Display nur an CH6 (VS S. 13, S. 18).
- Verteiler-Klemmen (Aufdruck): IN/OUT oben, LAN unten links, „+ − 24 VDC“ unten rechts.
  Polung beachten, nie 230 V anschließen (V1 S. 15).
- **Kaskade:**
  - Bis 15 Verteiler über IN/OUT in Reihe.
  - Darüber hinaus Gbit-Switches an den LAN-Ports der Verteiler; System bis 500 Geräte (VS S. 12–13).
- **LAN-Port** des Verteilers: Router (App, iVMS-4200) oder PoE-Switch.
  - So ist **Mischbetrieb** mit LAN/PoE-Geräten möglich; dann beide Zentralen einplanen (VS S. 11).
  - Metzler-Beispiel EFH: VM + Home 2-Draht am VT6, VT6-LAN → Switch, Ultra PoE am Switch,
    Sicherheitsmodul an Tür 1 (VS S. 23).
- Leitungen (VS S. 13):

  | Strecke | TP 0,2 mm² | TP 0,5 mm² | Telefonleitung parallel |
  |---|---|---|---|
  | VT6 → Türstation | ≤ 35 m | ≤ 60 m | ≤ 35 m |
  | VT6 → Innenstation | ≤ 35 m | ≤ 100 m | ≤ 50 m |
  | VT6 → VT6 | ≤ 60 m | ≤ 60 m | ≤ 35 m |

- **Keine Netzwerkkabel**, Schirm empfohlen, 230 V ≥ 0,5 m entfernt.
  Verteiler in den Medienverteiler, **nicht in den Schaltschrank** (VS S. 12, AV S. 1).
- Innenstations-Firmware nach 10/2019 (VS S. 13).

## 3 · VDM10 2.0 · LAN/PoE

- Jedes Gerät per Netzwerkkabel am **PoE-Switch (IEEE 802.3af)**. Switches per Gbit-Uplink koppeln,
  Uplink → Router (VS S. 11, S. 13).
- Kabel (AV S. 3–4):
  - CAT5e ≤ 60 m, ab CAT6 ≤ 100 m, RJ45 T568A/B.
  - An jedem Anschlusspunkt 1,5–2 m Reserve lassen, Kabel beschriften.
  - Für Innenstationen flexible Kabel verwenden.
- PoE-Budget: 802.3af ≈ 10,8 W nach Kabelverlust; mit 12-V-Netzteil 16 W für Module (VS S. 18).
- Ohne PoE:
  - Türstation 12 V DC 1 A (VS S. 14). An A7 nur beim PoE-Modell, wenn kein PoE anliegt.
  - Home/Ultra über VDM10-IS-NETZTEIL (12 V, 3 m Kabel), nicht Pro (VS S. 11, Shop 35864).
- Innenstation nicht gleichzeitig per LAN **und** WLAN mit demselben Router verbinden (VS S. 39, VQ).
  Bei WLAN bleibt die Türstation verkabelt, alle Geräte sind im selben Netz (VS S. 41).
- **Verwaltungsnetz und WLAN-Netz müssen unterschiedliche Netzwerke sein** (CL S. 1–2).
- PoE-Switches im Sortiment:
  - 4 × PoE (30659): 10/100, 802.3af/at, 60 W, VIP-Ports 1–2, Netzteil 48 V 1,35 A.
  - 8 × Gigabit-PoE (31594): + SFP, 110 W, 48 V 2,5 A (Shop).
- Vor der Montage den Tischaufbau testen. Die Parameter bleiben nach dem Abbau gespeichert (CL S. 1–2).

## 4 · VDM10-/ADM10-Türstation – Klemmen und Türöffner (VM-2W/POE-2.0 = ADM10-AM)

| Klemme | Belegung (VS S. 25, AS S. 23) |
|---|---|
| A1 / A2 / A3 | NC1 / NO1 / COM (gemeinsam) |
| A4 / A5 | NC2 / NO2 |
| A6 | GND |
| A7 | 12 V DC IN (nur PoE-Modell ohne PoE; bei 2W ungenutzt) bzw. **OUT1 12 V / 500 mA** (nur VM-POE-2.0) |
| A8 | GND für AIN1–4 |
| B1 / B2 | AIN2 (Taster 2 / Türkontakt 2) · AIN1 (Taster 1 / Türkontakt 1) |
| B3 / B4 | AIN3 (Taster 3 / Exit 1) · AIN4 (Taster 4 / Exit 2) |
| B5 / B6 / B7 / B8 | RS-485− / RS-485+ / 12 V OUT2 / GND |

- RS-485-Ausgang = 4-poliger Stecker 485− / 485+ / 12 V OUT / GND; Buskabel liegen bei (VS S. 34).
- **Erweiterungsmodule** in Reihe (VS S. 31):
  - Eingang A1 RS-485−, A2 +, A3 12 V IN, A4 GND; Ausgang B1–B4.
  - **Bis 8 Module**, DIP 1–4 = Adresse 1–8, DIP 8 = 120 Ω bei > 30 m. Das Hauptmodul braucht keine
    Adresse (VS S. 17, S. 35).
  - Taster-Modul: bis 5 Taster per JST-Stecker (VS S. 28).
- **Relais** max. 30 V AC/DC, 1 A (VS S. 25, AS S. 23).
  - Werk: NC1/COM für Magnetschlösser, NO1/COM für Türöffner (VS S. 26).
  - Ausgang 2 ist ab Werk aus. Einschalten unter E/A-Einstellungen → Ausgang 2 → „Elektrisches Schloss“.
  - Öffnungsdauer 0,1–600 s (VS S. 94).
- **Türöffner mit externem Netzteil (Standard):** Netzteil + → COM, NO1 → Türöffner, Türöffner →
  Netzteil −; bis 30 V / 1 A (VS S. 26, V2 S. 17, V1 S. 8). Separate Leitung und separate Versorgung
  für den Öffner (HW, V1 S. 10).
- **Türöffner aus der Türstation (nur LAN/PoE):** Brücke 12 V OUT1 → COM, NO1 → Öffner +, Öffner − →
  GND. OUT1 ist bei PoE automatisch aktiv, max. 500 mA (VS S. 26).
- **Türkontakt** AIN1 + GND (zu NC1/NO1), AIN2 zu Ausgang 2 → Eingang auf „Türstatus“ stellen.
- **Exit-Taster** AIN3 + GND (Exit 1), AIN4 (Exit 2) → „Exit-Taste“.
- Ab Werk sind AIN1–4 Klingeltaster (VS S. 25–26, S. 76).
- **Empfohlen:** Sicherheitsmodul im Innenbereich, statt den Öffner direkt an der Türstation
  anzuschließen (VS S. 32, V2 S. 21; § 6).
- **Grenzen** (VS S. 16–20):
  - 1 Haupttürstation, bis 16 Neben-Türstationen, bis 500 Innenstationen.
  - Bis 10 Innenerweiterungen je Haupt-Innenstation.
  - 16 IP-Kameras je Haupt-Innenstation; 2 Sicherheitsmodule je Kameramodul.
- **Adressierung** (VS S. 21–22, 37–40, 58–59, 90–91):
  - **Zimmer-Nr. = Klingeltaster** (Zimmer 1 = Taster 1); je Taster genau eine Haupt-Innenstation.
  - Innenerweiterungen haben die Nebenstellen-Nr. 1–10 und klingeln parallel.
  - Türstation-Nr. 0 = Haupt, 1–16 = Neben.
  - Community/Building/Unit überall gleich (1-1-1), ebenso das Registrierungspasswort.
  - Einrichtung im Assistenten der ersten Innenstation (Zimmer 1):
    1. Netzwerk.
    2. Zimmer-Nr.
    3. WLAN (optional).
    4. Türstation als „Haupt“ wählen.
    5. Erweiterungen per Seriennummer.
    6. Hik-Connect.
  - Zurücksetzen: erst die Türstation, dann die Innenstation (VS S. 65).
- **Innenstation – Alarm-Terminal** (2 × 10 Pins, Stecker liegt bei) (VS S. 52, 69):
  - Etagenruf-Taster an AIN1 + GND, Polung egal (VS S. 52).
  - Gong: Trafo + → COM1, NO1 → Gong +, Gong − → Trafo −; zweiter Gong an COM2/NO2 (VS S. 69).
  - Ausgänge max. 30 V DC / 300 mA. Die Pro hat Transistorausgänge → Koppelrelais (VS S. 57, 68).

## 5 · SDM10 (X · H · S)

- **Kein PoE an der Türstation.**
  - Eigenes **12 V DC / 2 A** (SDM10-TRAFO, Hutschiene, liegt bei).
  - Dazu LAN (CAT6/7) zum PoE-Switch, an dem die Innenstationen hängen; optional Router (SD S. 16, SQ).
- Kabelbaum (SD S. 16):

  | Gruppe | Belegung (Aderfarbe · Signal · Funktion) |
  |---|---|
  | A | A1 rot +12 V DC · A2 schwarz GND |
  | B | B1 gelb/rot AIN1 Türkontakt · B3 gelb/blau AIN3 Ausgangstaste · B4 gelb/grün AIN4 Feueralarm · B5 blau/schwarz GND |
  | C | **C3 grün RS-485B+ · C4 weiß RS-485B−** (Sicherheitsmodul) · C5 gelb/schwarz GND |
  | E | E1 weiß/blau NC1 · E2 weiß/grün COM1 · E3 weiß/rot NO1 (Türöffner 1) |

  B2, C1/C2, D1–D4 und F1–F3 sind reserviert.
- 12-V-Zuleitung bei 2 A (SP, ΔU 3 %):
  - 0,28 mm² ca. 1 m, 0,5 mm² ≤ 3 m, 1 mm² ≤ 6 m, 1,5 mm² ≤ 7 m.
  - 0,2 mm² nie verwenden.
  - Das Netzteil also nahe an die Türstation (Hutschiene in der Nähe/UV) – im Schema angeben.
- Türöffner ohne Modul (SD S. 18): eigenes Netzteil, Netzteil + → COM1, NO1 → Öffner → Netzteil −.
  Exit-Taster an AIN3 + GND, Türkontakt an AIN1 + GND.
- Die Gesichtserkennung öffnet immer Türöffner 1; Tür 2 nur über ein Sicherheitsmodul mit ID 2 (SD S. 25, 93).
- Grenzen (SD S. 9–12):
  - 1 Haupttürstation, bis 16 Neben-Türstationen, bis 500 Innenstationen.
  - Bis 10 Innenerweiterungen je Haupt-Innenstation.
- Zimmer-Nr. 1 = Klingeltaster 1 (SD S. 31, 51). Display-Layouts: 5 + 1, 6, 7 + 1 (PIN-Taste),
  8 Tasten oder Kontaktliste (SD S. 74).
- **2-Draht-LAN/PoE-Konverter** (GVS, 42509, nur paarweise) (SD S. 19–22):
  - Kette: SDM10 –CAT7– Slave –2-Draht– Master –CAT7– PoE-Switch.
  - Master am Switch („PD“), Slave am Gerät („PSE“). DIP M/S vor dem Einschalten setzen.
  - Den Master versorgt der PoE-Switch, sonst 52 V DC (42668). Der Slave wird vom Master versorgt –
    nie beide speisen.
  - TP-Klemme links +, rechts −. RVV 2 × 0,75 mm² bis 500 m.
  - Die SDM10 behält ihr 12-V-Netzteil.
- **SDM10H** – Hausnummer-Licht (HB):
  - 12 V DC ±5 %, ≤ 2,2 W; rot/markiert = +12 V, schwarz = GND.
  - Eigenes Netzteil (SELV, ≥ 0,5 A / 6 W), nicht im Lieferumfang; nie 230 V.
- **SDM10S** – Stele S250 (S250):
  - Ab Werk verkabelt, 7 gekennzeichnete Adern unten; SDM10-TRAFO liegt bei.
  - Die Beleuchtung braucht zusätzlich **24 V DC stabilisiert ≥ 40 W** (bis 35 W), rot +, schwarz −.

## 6 · Sicherheitsmodul (Metzler-SM 44914) und Türöffner

- Im **geschützten Innenbereich** montieren. Der Öffner hängt am Modul statt an der Türstation, der
  Befehl kommt über RS-485 (VS S. 32, SD S. 23).
- Klemmen (Hutschienen-Version, Aufdruck):

  | Klemme | Belegung |
  |---|---|
  | 1 / 2 | +12 V DC / GND |
  | 3 / 4 | RS-485+ / RS-485− |
  | 14 / 15 | DOOR_SENSOR / GND |
  | 16 / 17 | DOOR_BUTTON (Exit) / GND |
  | 18 / 19 / 20 | DOOR_NC / DOOR_COM / DOOR_NO |

- Kabel-Version (VS S. 32):

  | Ader | Farbe | Funktion |
  |---|---|---|
  | A1 / A2 | rot / schwarz | +12 V / GND |
  | B1 / B2 | gelb / blau | RS-485+ / RS-485− |
  | D8 / D9 | gelb/grün / schwarz | DOOR_SENSOR / GND |
  | D10 / D11 | gelb/grau / schwarz | DOOR_BUTTON / GND |
  | D12 / D13 / D14 | weiß/lila / weiß/gelb / weiß/rot | NC / COM / NO |

- **Öffner** (SM, VS S. 33):
  - Verdrahtung: **+12 V → DOOR_COM, DOOR_NO → Türöffner, Türöffner → −12 V**.
  - Nur Türöffner mit **12 V DC**. Relais potentialfrei max. **12 V DC / 1 A**; darüber (z. B. 24 V AC)
    ein Koppelrelais.
- **Versorgung:**
  - Modul 12 V DC / 0,5 A (6 W), eigene Quelle empfohlen.
  - Metzler-Schaltbild: Modul und Öffner haben je ein eigenes 12-V-Netzteil (VS S. 34).
  - **Gleichzeitig mit oder vor** der Türstation einschalten. Das Modul bindet sich an deren
    Seriennummer (VS S. 33, HW).
- **RS-485** (VS S. 33, SM S. 3, S. 8):
  - Das Modul ist **das letzte Gerät** am Bus, max. 50 m. Es zählt nicht zu den 8 Modulen.
  - VDM10: RS-485+ rot / − schwarz des Türstations-Steckers → gelb / blau am Modulkabel.
  - Mit RFID-Reader in dessen „RS485 OUT“.
  - SDM10: C3 grün / C4 weiß. XDM10: RS-485-Ausgang des letzten Moduls.
- **DIP:** ON-OFF-OFF-OFF = ID 1 → Tür 1; OFF-ON-OFF-OFF = ID 2 → Tür 2. Zwei Module mit RS-485
  parallel (VS S. 33–34, SD S. 25).
- Gepufferte Versorgung (USV für PoE-Switch und 12-V-Netzteile) empfohlen (V2 S. 22).

## 7 · ADM10 (Audio, ohne Kamera)

- Infrastruktur wie VDM10: LAN/PoE oder 2-Draht IP, Mischbetrieb möglich (AS S. 10–12, S. 22).
  - Klemmen, Relais, OUT1, AIN, Sicherheitsmodul, Leitungslängen und Kanalregeln wie § 2–4
    (AS S. 12, 23–29).
  - Versorgung: 12 V DC / PoE 802.3af / 24 V über VT6, < 16 W; Audiomodul 4 W, Namensschild-Modul
    VDM10-NT 2 W (AD, AS S. 13, 17).
  - Innenstation nur **ADM10 Home 7″** (LAN oder 2-Draht). Das VDM10-IS-NETZTEIL passt auch (AS S. 18, 22).
  - Ausgang 2: nur „Deaktivieren“, „Elektrisches Schloss“ oder „Türklingel“ (AS S. 69).
- Die Türstation kommt in der Regel vormontiert und fertig adressiert (AS S. 16, 30).
  - Grenzen: 500 Innenstationen, 16 Neben-Türstationen (AD).
- Kai-Klingeltaster (ADM10-AM-20, FW V3.7.1, von oben gezählt; KAI S. 2):

  | Taster | Zimmer-Nr. |
  |---|---|
  | 1 | 6 |
  | 2 | 5–6 |
  | 3 | 4–6 |
  | 4 | 3–6 |
  | 5 | 2–6 |
  | 6 | 1–6 |

  Dominik (1 Taster) ruft Zimmer 1 (AS S. 80).

## 8 · Klingeltaster, Zubehör, Montage

- **VDM10-Neo** (NEO; von oben, werkseitig gerufene Zimmer-Nr.; nach der Ersteinrichtung frei zuweisbar):

  | FW-Build | 1 T | 2 T | 3 T | 4 T | 5 T | 6 T |
  |---|---|---|---|---|---|---|
  | V2.2.63_build240527 | 4 | 3, 5 | 2, 4, 6 | 2–5 | 1–5 | 1–6 |
  | V2.2.63_build231213 | 5 | 4, 6 | 3, 5, 7 | 3–6 | 2–6 | 2–7 |

  Neuere Firmware: erste Taste = Zimmer 1 (VS S. 64, 91). → Im Schema immer „Zuweisung nach
  Einrichtung“ schreiben oder die FW nennen.
- **RGB-Drucktaster D19-TF-RGB** (RGB):
  - Adern: rot = LED +, schwarz = LED −, weiß + gelb = Schließer (NO).
  - LED 6–24 V DC, Kontakt 1 A.
  - DIP 1 blau, 2 grün, 3 rot (Kombinationen = Mischfarben). Nie 230 V.
- **Paketbox-Videomodul VM300/VM400:** für XDM10-VM oder VDM10-VM.
  - Die Leitung kommt unter der Box aus dem Boden und läuft innen hinten rechts hoch.
  - Durch die Kabeltülle zur Modul-Rückseite.
- **Montagehöhen:**
  - Innenstation 1,4–1,6 m (XI S. 11).
  - Kameralinse der Türstation 1,4–1,6 m (XT S. 19).

## 9 · Widersprüche in den Quellen – so wird gezeichnet

| # | Widerspruch | Entscheidung |
|---|---|---|
| 1 | XDM10: „bis zu 4 Innenstationen pro Gebäude“ (XI S. 2) vs. Set 8 Anschlüsse / 16 VTS | ≤ 4 Innenstationen: VT4 + PSU36. Mehr: XDM10-VT8 + 150 W bzw. VTS. Set im Schema nennen. |
| 2 | XDM10-Kabeltabelle führt UTP Kat.5 ≤ 60 m, Text verbietet Netzwerkkabel (XI S. 3) | Text gilt: kein Netzwerkkabel für 2-Draht. |
| 3 | XDM10-Topologiegrafik: Bus rot/schwarz, Text: VT4, Grafik: VT8 | Bus rot/gelb (stil.md). Verteiler passend zur Geräteanzahl. |
| 4 | VT6-Set-Foto zeigt 48 V | VDM10-TRAFO = **24 V DC 36 W**. |
| 5 | V2 S. 17 „integriertes Netzteil“: Öffner zwischen NC1 und 12 V OUT1 | Nicht übernehmen. Variante aus VS S. 26 (Brücke OUT1 → COM, NO1 → Öffner) und nur bei PoE. |
| 6 | Innenerweiterungen: Bilder „1…5“, Text „bis zu 10“ (VS S. 11–20) | Text: bis 10. In Beispielen ≤ 5 zeichnen. |
| 7 | CH1–5 „bis 3 Untermodule“ vs. 6-W-Budget; „< 12 W“ vs. CH6 16 W | Türstation immer an CH6, Summe ≤ 12 W. |
| 8 | Stückliste EFH nennt „VM-POE-2.0 … 2-Draht“ (VS S. 23) | 2-Draht-Türstation = **VDM10-VM-2W-2.0**. |
| 9 | SM-Kabel: rot = +12 V, gelb = RS-485+; aufgetrenntes Buskabel: rot = RS-485+, gelb = 12 V (VS S. 32–33) | Immer **nach Beschriftung**, nie nach Farbe anschließen. Im Schema RS-485 grün/weiß + Klemmentext. |
| 10 | DIP „5–8 reserviert“ und zugleich 8 = 120 Ω | DIP 8 = 120 Ω bei > 30 m (XT S. 17). |
| 11 | Kaskadenkoppler „VDM10-VT6-2.0“ vs. Bild „DS-KD706-S“ | VDM10-VT6-2.0 schreiben. |
| 12 | ADM10 Relais „36 V“ (AD) vs. 30 V / 1 A (AS); Versorgung „12 V 5 A“ (AS S. 13) | 30 V / 1 A. 12 V DC ohne Stromangabe. |
| 13 | Namensschild-Modul „VDM10-NT“ vs. „DS-KD-KK“ | „Namensschild-Modul (VDM10-NT)“. |
| 14 | VS S. 24: PoE-Türstation → SM als „2-Draht“ beschriftet | Ist RS-485 – so beschriften. |
| 15 | SP: Tabelle zeigt 0,28 mm² bis 2 m, Text „ca. 1 m“ | Text: ca. 1 m. |
| 16 | NEO-Zuordnung je Firmware verschieden | „Zuweisung nach Einrichtung“, ggf. FW nennen. |
| 17 | Shop-Produktseite „VT1“, Datenblatt VT4/VT8 · SM-Aufdruck „FIR-“, „ALM_IN_I4“ | Tippfehler – VT4/VT8. Aufdruck nicht übernehmen. |
| 18 | Zutrittsgruppen iVMS: nur Relais 1 vs. „2 ansteuerbare Türöffner“ | Beide Öffner sind möglich; Zutrittsgruppen nur Relais 1 (Hinweis). |

## 10 · Prüfliste vor Abgabe eines Schemas

1. System und Varianten stimmen mit dem Produkt überein (§ 0); keine Mischung XDM10 ↔ VDM10.
2. Jede Leitung hat die richtige Art und Farbe (stil.md § 4), landet auf der richtigen Klemme und ist
   beschriftet (CH6, IN/OUT, PoE-Port, COM/NO …).
3. Grenzwerte eingehalten: Kanäle, Watt, Daisy-Chain ≤ 4, Kaskaden, Leitungslängen, Modulanzahl.
4. Türöffner-Kreis vollständig: Netzteil + → COM → NO → Öffner → Netzteil −; Spannung passend
   (SM: 12 V DC; Türstation: ≤ 30 V / 1 A).
5. 230 V nur an Netzteilen, mit Hinweis „Elektrofachkraft“.
6. Adressierung angegeben: Gebäude-/Zimmer-Nr., Haupt/Neben, DIP-IDs.
7. Info-Band: Schritte = Badges im Bild, Hinweise mit den Regeln aus diesem Dokument, Legende vollständig.
8. `build.py` ohne Warnungen, PNG angesehen (Texte, Kreuzungen, Pills nicht auf Kreuzungen).
