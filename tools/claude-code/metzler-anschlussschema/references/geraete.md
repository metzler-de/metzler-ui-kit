# Geräte-Katalog

Alle Geräte stehen als Zeichenfunktion in `scripts/devices.py` (1 Einheit = 1 mm, nach den Produktfotos
des Shops gezeichnet, Stand 09/2026). **Nie ein Gerät frei zeichnen** – fehlt eines, nach derselben Methode
ergänzen (siehe unten) und in diese Tabelle eintragen.

Aufruf im Schema: `p = S.place(funktion(D, …), x, y, maßstab)`; Anschlusspunkte: `p.a('NAME')`,
beliebiger Punkt: `p.pt(fx, fy)` (Anteil von Breite/Höhe), Kanten: `p.x p.y p.right p.bottom p.cx`.

## Türstationen

| Funktion | Produkt (Shop-Art.) | System | Maße B × H (mm) | Optik |
|---|---|---|---|---|
| `xdm10_maxior(D, names)` | XDM10 MAXIOR 1/2/3 Klingeltaster (45248, 45256, 45263) | XDM10 2-Draht-BUS | 135 × 293 (T 44) | schwarze Glasfront mit Statussymbolen, kleiner Kamera, Lautsprecherschlitz; Edelstahlleiste; anthrazites Unterteil mit 1–3 silbernen Namensschildern |
| `vdm10_colson(D, name, buttons=None)` | VDM10 2.0 Colson 1–7 Taster (31101, 31122, 31135, 38941, 38947, 38953, 38959) | VDM10 2.0 · LAN/PoE oder 2-Draht IP | 135 × 267 | Edelstahlleisten oben/unten, schwarzes Kameraband mit Punkt-Ring-Kamera, gravierter Name, Leuchttaster; `buttons=[…]` = Mehrfamilien-Variante mit runden Tastern + Namensfeld |
| `vdm10_kian(D, name)` | VDM10 2.0 Kian 1 Taster (31086; 2/3 Taster: 31315, 31321) | VDM10 2.0 | 135 × 271 | runde Kamera, 2 × 5 Lautsprecherschlitze, erhabenes Namensschild, Leuchttaster |
| `vdm10_niko(D, name)` | VDM10 2.0 Niko mit Fingerprint 1–3 (40484, 40492, 40501) | VDM10 2.0 | 135 × 288 | wie Colson + schwarzes Band mit Fingerabdruck-Leser |
| `vdm10_neo(D, names)` | VDM10 2.0 Neo 1–6 (40373, 40380, 40387, 40394, 40411, 40418) | VDM10 2.0 | 135 × 280 | Kameraband, austauschbare Namensschilder mit Glocken-Symbol (1–6 Zeilen) |
| `vdm10_horizon(D, lines)` | VDM10 2.0 Horizon modular (36478) | VDM10 2.0 | 135 × 247 | runde Kamera, Kreuz-Lautsprechergitter, Touch-Display-Modul (VDM10-TDM) mit Glocke + Name |
| `adm10_dominik(D, name)` | ADM10 Dominik (41096) | ADM10 Audio | 133 × 245 (T 43) | abgerundet, **keine Kamera**, schwarzes Namensband, Leuchtring-Taster |
| `adm10_kai(D, names, number, street)` | ADM10 Kai 1–6 (42899, 42911, 42918, 42891, 42892, 42893) | ADM10 Audio | 135 × 280 | große Hausnummer + Straße, Lautsprecher, Namensschilder mit Glocke |
| `sdm10x(D)` | SDM10X (40132) | SDM10 · LAN + 12 V | 194 × 330 (T 31) | großes Touch-Display hochkant (08:35, Rezeption · Büros · PIN-Code) |
| `sdm10h(D, number)` | SDM10H Hausnummer beleuchtet (42955) | SDM10 | 180 × 445 (T 30) | beleuchtete Hausnummer (blauer Schein) + Display |
| `sdm10s(D, number, street)` | SDM10S Stele (44643) | SDM10 | 200 × 1600 (T 68) | Säule: Display oben, Nummer, Straßenname senkrecht |
| `paketbox_saeule(D, name, number, street)` | Paketbox Zivo 2 · 2-Draht-BUS (45564) = **XDM10**; Zivo 2 · LAN/PoE (45337), Bispo 2 · LAN/PoE (45465) = **VDM10 LAN/PoE** | s. links | 503 × 1603 (T 373) | Säule, schwarzes Sprechanlagen-Band oben, Namens- und Nummernschild |
| `paketbox_videomodul(D, name, street, number)` | Video-Türsprechanlage mit Paketbox (37175, VM300/VM400) | VDM10 2.0 · LAN/PoE oder 2-Draht IP | 440 × 955 (T 220) | Glasband mit Klingel + Kamera, Brieffach, Nummernleiste, Paketfach |
| `briefkasten_vdm10(D, name)` | Briefkasten mit VDM10 2.0 (39718, BK212) | VDM10 2.0 | 392 × 604 (T 119) | Videomodul-Band mit Ring-Klingel + Kamera, „Zeitungen“ |

Siebert-Briefkasten mit VDM10 (36045, 36050, 36299) ist **noch nicht gezeichnet** (gleiche Technik wie
VDM10 2.0, 24-V-Trafo 36 W) – bei Bedarf nach dem Foto ergänzen.

Anschlusspunkte Türstationen: `bottom`, `top`, `left`, `right`, `bus` (Mitte −14 mm), `rs485` (+14 mm),
`pwr` (+28 mm, SDM10: `pwr` links, `lan` Mitte, `rs485` rechts). Kabel enden an der Unterkante
(sie verschwinden hinter dem Gerät) – Klemmennamen werden als Beschriftung angegeben.

## Innenstationen

| Funktion | Produkt | System | Maße | Optik |
|---|---|---|---|---|
| `xdm10_monitor(D, color, room)` | XDM10 Innenstation 7″ Weiß (44303) / Schwarz (44302), WLAN 2,4 GHz | XDM10 | 190 × 138 (T 20) | „METZLER“ oben, grüne Oberfläche 12:36, 3 Hardware-Tasten unten; Anker `b_in` / `b_out` (2-Draht IN/OUT) |
| `vdm10_home(D, color, room)` | Innenstation Home 7″ LAN weiß (29384) / schwarz (30646) · 2-Draht weiß (37817) / schwarz (37820) | VDM10 2.0 | 200 × 140 (T 25) | rote Oberfläche 12:00, „METZLER“ unten – LAN und 2-Draht sehen gleich aus |
| `vdm10_pro(D, room)` | Innenstation Pro 7″ IPS LAN (31197) | VDM10 2.0 · nur LAN | 180 × 140 | Glas schwarz + graues Aluband mit Schlüssel-Sensortaste |
| `vdm10_ultra(D, room)` | Innenstation Ultra 10,1″ LAN (29407) | VDM10 2.0 · nur LAN | 254 × 166 | schwarz, großes Display |
| `adm10_monitor(D, color)` | ADM10 Innenstation Home 7″ LAN+PoE (41158) / 2-Draht (41157) | ADM10 | 200 × 140 | weiß, dunkle 4-Kachel-Oberfläche (Anrufen, Tür öffnen, Stumm, Einstellungen) |

Anker: `bottom`, `top`, `left`, `right`. Maßstab 0,8–1,0.

## Verteiler, Netzteile, Netzwerk

| Funktion | Produkt | Anker | Hinweise |
|---|---|---|---|
| `dist_xdm10_vt4(D)` | XDM10-VT4, Set „4 Anschlüsse“ (44301) | `CH1`–`CH4` (oben), `PWR` (unten rechts) | 144 × 90; zwei Blindklemmen ohne Funktion (kein IN/OUT) |
| `meanwell_hdr30(D,'48','0.75','36','HDR-30-48')` | XDM10-PSU36, 48 V 36 W (im Set 44301) | `V-` `V+` (oben), `N` `L` (unten) | 35 × 90 |
| `dist_xdm10_6ch(D)` | **XDM10-VT8** – Verteiler IN/OUT + CH1–CH6, Set „8 Anschlüsse“ (44768) | `IN` `OUT` `CH1`–`CH6`, `PWR` | 144 × 92 |
| `meanwell_hdr150_48(D)` | Transformator 48 V 150 W, MEAN WELL HDR-150-48 (Set 44768) | `V-` `V+` außen, `V-i` `V+i` innen, `N` `L` | 105 × 90 |
| `stockwerksverteiler(D, flipped)` | Stockwerksverteiler 2-Draht = XDM10-VTS (44779) | `IN` `OUT`, `CH1`–`CH4` | 70,6 × 60 + Laschen; `flipped=True`: Kanäle oben, IN/OUT unten |
| `dist_vdm10_vt6(D)` | VDM10-VT6-2.0, Set „6 Anschlüsse“ (36028) | `IN` `OUT` `CH1`–`CH6` (oben), `PWR` (unten rechts), `LAN` (unten links) | 144 × 90; Aufdruck CH1–5 „MAX 6W“, CH6 „MAX 16W“ |
| `meanwell_hdr30(D,'24','1.5','36','VDM10-TRAFO')` | VDM10-TRAFO 24 V DC 36 W | wie oben | Shop-Foto des Sets zeigt fälschlich 48 V |
| `meanwell_hdr30(D,'12','2','24', model=…)` | Hutschienen-Netzteil 12 V DC 24 W (SDM10-TRAFO, Sicherheitsmodul, Türöffner) | wie oben | |
| `sicherheitsmodul(D)` | Metzler Sicherheitsmodul mit Hutschienenhalter (44914) | `T1`–`T20` (oben) | 1 +12 V · 2 GND · 3 RS-485+ · 4 RS-485− · 14 DOOR_SENSOR · 15 GND · 16 DOOR_BUTTON · 17 GND · 18 DOOR_NC · 19 DOOR_COM · 20 DOOR_NO |
| `poe_switch(D, 4)` | PoE-Switch 4 × PoE (30659): 4 × 10/100 PoE + Uplink, 802.3af/at, 60 W, Port 1–2 VIP | `P1`–`P4`, `UP` (unten) | Netzteil 48 V DC 1,35 A (`plug_adapter`) |
| `poe_switch(D, 8)` | Gigabit-PoE-Switch 8 × PoE (31594): 8 × PoE + Uplink + SFP, 110 W | `P1`–`P8`, `UP` | 48 V DC 2,5 A |
| `tueroeffner(D)` | elektrischer Türöffner (Schließblech) | `bottom` | generisch |
| `exit_button(D)` | Ausgangstaster (Exit) | `bottom` | generisch |
| `router(D)`, `smartphone(D)`, `plug_adapter(D, label)`, `wall_socket(D)` | Umfeld | | keine Metzler-Produkte |

Noch nicht gezeichnet (bei Bedarf ergänzen): Netzteil mit 3 m Kabel für Innenstationen (35864 VDM10
Home/Ultra, 44282 XDM10 – 12 V 1 A Stecker), 2-Draht-LAN/PoE-Konverter (42509, Paar Master/Slave) mit
Netzteil 52 V 1 A (42668), VDM10-RFID-READER, RFID-Karte/Schlüsselanhänger, Montagewinkel.

## Typische Maßstäbe im Schema (1280 px Fläche)

Türstationen 0,62–0,9 · Monitore 0,8–1,0 · Hutschiene 1,2–1,35 · Stockwerksverteiler 1,7 ·
PoE-Switch 1,4 (8×) / 2,0 (4×) · Router 0,95 · Paketbox 0,28–0,42 · Stele 0,25.

## Fehlendes Gerät ergänzen (Methode)

1. Produktseite per `curl -sL -A "Mozilla/5.0" <url>` laden, Galerie-Bilder
   `media/image/product/<id>/lg/…jpg` (1200 × 1200) herunterladen, weißen Rand wegschneiden.
2. Maße aus der Produktseite („Breite × Höhe × Tiefe“, cm) – sonst Seitenverhältnis aus dem Foto.
3. Neue Funktion in `devices.py`: alles in mm, Farben wie die verwandten Geräte (`_plate`, `steel`,
   `_dot_camera`, `_round_camera`, `_ring_button`, `_name_rows`, `_sdm_display`), Anker definieren.
4. Galerie rendern (`rsvg-convert`) und neben das Foto legen: Proportionen, Positionen der Elemente,
   Beschriftungen prüfen. Erst dann im Schema verwenden und diese Tabelle ergänzen.
