# -*- coding: utf-8 -*-
"""
Die 5 Referenzschemata (Stand 09/2026). Jede Funktion gibt den SVG-Text zurück.
Neue Schemata: neues_schema.py kopieren – nicht diese Datei aufblähen.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scheme import *  # noqa: E402,F401,F403


# =================================================================================
# 1 · XDM10 · Einfamilienhaus mit Türöffner
# =================================================================================
def scheme_xdm10_efh():
    S = Scene('x1', 1280, 1084)
    D = S.D
    S.header('Anschlussschema · XDM10 Einfamilienhaus',
             '2-Draht-BUS über vorhandene Klingelleitung · 2 Innenstationen in Reihe · Türöffner über Sicherheitsmodul',
             tags=('XDM10', '2-Draht-BUS · 48 V'),
             link=('Zum Produkt ↗', SHOP + 'metzler-xdm10-video-tuersprechanlage-mit-austauschbarem-namensschild-2-draht-bus-1-klingeltaster-maxior'))

    S.zone(32, 104, 268, 656, 'Außen · Hauseingang')
    S.zone(316, 104, 932, 262, 'Wohnbereich')
    S.zone(316, 382, 932, 378, 'Technikraum · Medienverteiler', fill='#EEF0F4', stroke='#E1E4EA')

    # ---- Außen
    strike = S.place(tueroeffner(D), 60, 300, 0.95)
    S.caption(strike.cx, 262, 'Türöffner', ('12 V DC',))
    door = S.place(xdm10_maxior(D, ('Vossmann',)), 156, 206, 0.86)
    S.caption(door.cx, 160, 'XDM10 MAXIOR', ('Türstation · 1 Klingeltaster',))

    # ---- Wohnbereich
    is1 = S.place(xdm10_monitor(D, 'white', room='3'), 600, 172, 1.0)
    is2 = S.place(xdm10_monitor(D, 'white', room='3'), 862, 172, 1.0)
    S.caption(is1.cx, 138, 'XDM10 Innenstation 7″', ('Haupt-Innenstation · Zimmer 03',))
    S.caption(is2.cx, 138, 'XDM10 Innenstation 7″', ('Innenerweiterung 1 · Zimmer 03',))
    rt = S.place(router(D), 1110, 250, 0.95)
    S.caption(rt.cx, 312, 'Router', ('optional · WLAN für App',))
    S.wlan((is2.right + 6, is2.y + 64), (rt.x - 6, rt.y + 12))

    # ---- Technikraum (DIN-Schiene), Maßstab s
    s = 1.3
    ytop = 544
    S.din_rail(342, 944, ytop + 45 * s)
    psu_sm = S.place(meanwell_hdr30(D, '12', '2', '24', model='12 V DC 24 W'), 352, ytop, s)
    sm = S.place(sicherheitsmodul(D), 420, ytop + (90 - 76) / 2 * s, s)
    psu_to = S.place(meanwell_hdr30(D, '12', '2', '24', model='12 V DC 24 W'), 590, ytop, s)
    vt4 = S.place(dist_xdm10_vt4(D), 680, ytop, s)
    psu36 = S.place(meanwell_hdr30(D, '48', '0.75', '36', model='HDR-30-48'), 884, ytop, s)

    cy = 718
    S.caption(psu_sm.cx, cy, 'Netzteil', ('12 V DC', 'Modul'))
    S.caption(sm.cx, cy, 'Sicherheitsmodul', ('Klemmen 1–4 · 19–20', 'DIP 1 = ON (Relais 1)'))
    S.caption(psu_to.cx, cy, 'Netzteil', ('12 V DC', 'Türöffner'))
    S.caption(vt4.cx, cy, 'XDM10-VT4', ('Verteiler · 4 Kanäle', 'max. 30 W'))
    S.caption(psu36.cx + 8, cy, 'XDM10-PSU36', ('48 V DC · 36 W',))

    # ---- Leitungen
    halo_z = '#EEF0F4'
    rs_x = door.x + 0.36 * door.w
    bus_x = door.x + 0.64 * door.w
    ch1, ch2 = vt4.a('CH1'), vt4.a('CH2')
    y_bus, y_door, y_rs = 474, 484, 496
    # (2) 2-Draht Türstation -> VT4 CH1
    S.pair([(bus_x, door.bottom - 4), (bus_x, y_bus), (ch1[0], y_bus), ch1], ('red', 'yellow'))
    S.pill(712, y_bus, '2-Draht')
    S.step(760, y_bus, 2)
    # (3) 2-Draht VT4 CH2 -> Innenstation (IN), Reihe -> Innenerweiterung (OUT -> IN)
    in1 = (is1.x + 87, is1.bottom - 4)
    out1 = (is1.x + 103, is1.bottom - 4)
    in2 = (is2.x + 87, is2.bottom - 4)
    S.pair([ch2, (ch2[0], 424), (in1[0], 424), in1], ('red', 'yellow'))
    S.pill(748, 424, '2-Draht')
    S.step(834, 424, 3)
    S.pair([out1, (out1[0], 336), (in2[0], 336), in2], ('red', 'yellow'))
    S.pill(826, 336, 'in Reihe (Daisy-Chain)')
    S.tlabel(in1[0] - 6, 352, 'IN', anchor='end')
    S.tlabel(out1[0] + 6, 352, 'OUT')
    S.tlabel(in2[0] + 7, 326, 'IN')
    S.tlabel(ch1[0] - 5, 536, 'CH1', anchor='end')
    S.tlabel(ch2[0] + 6, 536, 'CH2')
    # (4) RS-485 Türstation -> Sicherheitsmodul 3 (RS-485+) / 4 (RS-485−)
    t3, t4 = sm.a('T3'), sm.a('T4')
    S.pair([(rs_x, door.bottom - 4), (rs_x, y_rs), (t4[0] + 6, y_rs)], ('green', 'white'), ends=[t3, t4])
    S.pill(356, y_rs, 'RS-485')
    S.step(398, y_rs, 4)
    # Türöffner-Leitung: rot -> 20 DOOR_NO, schwarz -> Netzteil −V ; Brücke +V -> 19 DOOR_COM
    t19, t20 = sm.a('T19'), sm.a('T20')
    vneg, vpos = psu_to.a('V-'), psu_to.a('V+')
    S.pair([(strike.cx, strike.bottom - 4), (strike.cx, y_door), (vneg[0] + 6, y_door)], ('red', 'black'),
           ends=[t20, vneg])
    S.pill(520, y_door, 'Türöffner · 2-adrig')
    S.wire([vpos, (vpos[0], 530), (t19[0], 530), t19], 'red', halo=halo_z)
    # Modul-Versorgung 12 V -> 1 (+12 V) / 2 (GND)
    t1, t2 = sm.a('T1'), sm.a('T2')
    mneg, mpos = psu_sm.a('V-'), psu_sm.a('V+')
    S.wire([mneg, (mneg[0], 522), (t2[0], 522), t2], 'black', halo=halo_z)
    S.wire([mpos, (mpos[0], 530), (t1[0], 530), t1], 'red', halo=halo_z)
    # (1) 48 V DC PSU36 -> VT4 (+ −)
    pneg, ppos = psu36.a('V-'), psu36.a('V+')
    pw = vt4.a('PWR')
    plus, minus = (pw[0] - 2.2 * s, vt4.bottom - 2), (pw[0] + 2.2 * s, vt4.bottom - 2)
    gx = vt4.right + 8
    S.wire([ppos, (ppos[0], 522), (gx + 4, 522), (gx + 4, 676), (plus[0], 676), plus], 'red', halo=halo_z)
    S.wire([pneg, (pneg[0], 530), (gx, 530), (gx, 670), (minus[0], 670), minus], 'black', halo=halo_z)
    S.pill(958, 506, '48 V DC')
    S.step(1000, 506, 1)
    # 230 V AC
    for p in (psu_sm, psu_to, psu36):
        n, l = p.a('N'), p.a('L')
        S.wire([n, (n[0], 692)], 'blue', halo=halo_z)
        S.wire([l, (l[0], 692)], 'brown', halo=halo_z)
        S.pill(p.cx, 692, '230 V AC')

    # ---- Adressierung (Drehschalter)
    ax, ay, aw = 1026, 420, 204
    rows = [('Türstation', 'Gebäude 01 · Tür 00'),
            ('Innenstation', 'Gebäude 01 · Zimmer 03', 'Erweiterung 0'),
            ('Innenerweiterung', 'Gebäude 01 · Zimmer 03', 'Erweiterung 1')]
    yy = ay + 56
    body = []
    for r in rows:
        body.append(text(ax + 16, yy, r[0], size=12, weight=700, fill=INK))
        for k, v in enumerate(r[1:]):
            body.append(text(ax + 16, yy + 16 + k * 15, v, size=12, fill=TXT2))
        yy += 16 + 15 * (len(r) - 1) + 14
    body.append(text(ax + 16, yy + 4, '1 Klingeltaster → Zimmer 03', size=12, weight=700, fill=TEAL))
    ah = yy + 20 - ay
    S.add('labels', rect(ax, ay, aw, ah, rx=10, fill=WHITE, stroke='#E1E4EA', stroke_width=1))
    S.add('labels', text(ax + 16, ay + 29, 'Drehschalter', size=14, weight=700, fill=INK))
    S.add('labels', ''.join(body))
    S.add('labels', circle(ax + aw - 22, ay + 24, 11, fill=TEAL) +
          text(ax + aw - 22, ay + 28.4, '5', size=12, weight=700, fill='#FFFFFF', anchor='middle'))

    # ---- Tipp (Außenbereich unten)
    tx, ty, tw = 48, 612, 236
    tl = wrap('Vor der Montage im Tischaufbau testen: Türstation, Verteiler, Netzteil und eine Innenstation '
              'anschließen und die Signalqualität prüfen.', 12, tw - 28)
    S.add('labels', rect(tx, ty, tw, 30 + 15 * len(tl), rx=10, fill=TEAL50, stroke='#D5E3E3', stroke_width=1))
    S.add('labels', text(tx + 14, ty + 22, 'Tipp', size=12, weight=700, fill=TEAL))
    for k, ln in enumerate(tl):
        S.add('labels', text(tx + 14, ty + 40 + k * 15, ln, size=12, fill=INK))

    # ---- Info-Band
    S.info_band(780, steps=[
        'Netzteil XDM10-PSU36 an 230 V anschließen und mit „+ −  48 VDC“ am Verteiler verbinden.',
        'Türstation mit einem freien Kanal CH1–CH4 verbinden (eigenes Aderpaar).',
        'Haupt-Innenstation an CH2 (Klemme 2-Draht-IN), Innenerweiterung von OUT → IN in Reihe.',
        'Sicherheitsmodul: RS-485 an Klemme 3/4, eigenes 12-V-Netzteil an 1/2, Türöffner an 19/20.',
        'Drehschalter einstellen (Gebäude-Nr., Zimmer-Nr.), Kopplung starten – fertig.',
    ], notes=[
        'Pro Gerät nur ein Aderpaar nutzen, keine Netzwerkkabel (Impedanz über 42 Ω / 100 m).',
        'Leitungslängen: Verteiler → Türstation ≤ 60 m; Verteiler → Innenstation ≤ 60 m (Twisted Pair ≤ 40 m); Innenstation → Innenstation ≤ 100 m (Twisted Pair ≤ 80 m).',
        'Ein PSU36 versorgt 1 Türstation und bis zu 4 Innenstationen; max. 4 Innenstationen in Reihe.',
        '230-V-Leitungen ≥ 0,5 m entfernt verlegen. XDM10 ist nicht mit VDM10 2-Draht mischbar.',
        'Zuerst das Sicherheitsmodul, dann die Sprechanlage einschalten. Nur Türöffner mit 12 V DC.',
    ], legend=[
        ('pair', ('red', 'yellow'), '2-Draht-BUS – 1 Aderpaar, z. B. J-Y(St)Y 2×2×0,8'),
        ('pair', ('green', 'white'), 'RS-485 Türstation → Sicherheitsmodul'),
        ('pair', ('red', 'black'), '12 / 48 V DC · rot = +, schwarz = −'),
        ('pair', ('brown', 'blue'), '230 V AC · L braun, N blau (Elektrofachkraft)'),
        ('wlan', None, 'WLAN (optional) für die Hik-Connect App'),
    ],
    )
    S.footer(FOOT)
    return S.svg('Anschlussschema XDM10 Einfamilienhaus',
                 'XDM10 2-Draht-BUS: MAXIOR-Türstation und zwei Innenstationen in Reihe am Verteiler XDM10-VT4 mit '
                 '48-V-Netzteil; Türöffner über das Metzler Sicherheitsmodul mit eigenen 12-V-Netzteilen.')


# =================================================================================
# 2 · XDM10 · Mehrfamilienhaus mit Stockwerksverteiler  (Set „8 Anschlüsse“)
# =================================================================================
def scheme_xdm10_mfh():
    S = Scene('x2', 1280, 1100)
    D = S.D
    S.header('Anschlussschema · XDM10 Mehrfamilienhaus',
             '2-Draht-BUS mit Stockwerksverteiler · 3 Wohnungen · mehr als 4 Innenstationen möglich (Set „8 Anschlüsse“)',
             tags=('XDM10', '2-Draht-BUS · 48 V'),
             link=('Zum Produkt ↗', SHOP + 'metzler-xdm10-video-tuersprechanlage-mit-austauschbarem-namensschild-2-draht-bus-3-klingeltaster-maxior'))

    S.zone(32, 104, 268, 672, 'Außen · Hauseingang')
    S.zone(316, 104, 932, 398, 'Etage · Wohnungen')
    S.zone(316, 518, 932, 258, 'Technikraum · Medienverteiler', fill='#EEF0F4', stroke='#E1E4EA')

    # ---- Türstation mit 3 Klingeltastern (Zimmer-Nr. 02 / 04 / 06 laut Zimmernummer-Zuweisung)
    names = ('Steinbach-Kehl', 'Vossmann', 'Zimmermann')
    door = S.place(xdm10_maxior(D, names), 100, 206, 0.86)
    S.caption(door.cx, 160, 'XDM10 MAXIOR', ('Türstation · 3 Klingeltaster',))
    for ty, room in zip((196.0, 225.5, 255.0), ('02', '04', '06')):
        yy = door.y + ty * door.s
        S.add('labels', line(door.right + 4, yy - 4, door.right + 14, yy - 4, stroke=TEAL, stroke_width=1.5))
        S.add('labels', text(door.right + 18, yy, 'Zi. %s' % room, size=12, weight=700, fill=TEAL))
    S.step(door.x - 18, door.y + 225.5 * door.s - 4, 5)

    # ---- Wohnungen
    ms = 0.9
    xs = (344, 572, 800, 1028)
    rooms = ('2', '4', '6', '6')
    heads = (('Steinbach-Kehl', 'Innenstation · Zimmer 02'), ('Vossmann', 'Innenstation · Zimmer 04'),
             ('Zimmermann', 'Innenstation · Zimmer 06'), ('Zimmermann', 'Innenerweiterung 1 · Zimmer 06'))
    mons = []
    for x, r, (t, l) in zip(xs, rooms, heads):
        m = S.place(xdm10_monitor(D, 'white', room=r), x, 192, ms)
        S.caption(m.cx, 160, t, (l,))
        mons.append(m)

    vts = S.place(stockwerksverteiler(D, flipped=True), 716, 376, 1.7)
    S.caption(vts.right + 22, 414, 'Stockwerksverteiler', ('4 Kanäle · max. 20 W je Kanal', 'Versorgung über den BUS'),
              anchor='start')

    # ---- Technikraum
    s = 1.3
    ytop = 590
    S.din_rail(640, 1060, ytop + 46 * s)
    dist = S.place(dist_xdm10_6ch(D), 650.8, ytop, s)
    psu = S.place(meanwell_hdr150_48(D), 900, ytop + 1.3, s)
    S.caption(dist.x - 22, 636, 'XDM10-VT8', ('Verteiler · IN · OUT · CH1–CH6', 'Set „8 Anschlüsse“'), anchor='end')
    S.caption(psu.right + 16, 636, 'Transformator', ('48 V DC · 150 W', 'MEAN WELL HDR-150-48'), anchor='start')

    # ---- Leitungen
    halo_z = '#EEF0F4'
    ch1, ch2 = dist.a('CH1'), dist.a('CH2')
    # (2) Türstation -> CH1
    S.pair([(door.cx, door.bottom - 4), (door.cx, 562), (ch1[0], 562), ch1], ('red', 'yellow'))
    S.pill(440, 562, '2-Draht')
    S.step(490, 562, 2)
    S.tlabel(ch1[0] - 6, 584, 'CH1', anchor='end')
    # (3) CH2 -> Stockwerksverteiler IN
    vin, vout = vts.a('IN'), vts.a('OUT')
    S.pair([ch2, (ch2[0], (ch2[1] + vin[1]) / 2 + 20), (vin[0], (ch2[1] + vin[1]) / 2 + 20), (vin[0], vin[1] - 2)],
           ('red', 'yellow'))
    S.tlabel(ch2[0] + 6, 584, 'CH2')
    S.tlabel(vin[0] - 6, 496, 'IN', anchor='end')
    S.step(ch2[0] + 24, 540, 3)
    # Kaskade: OUT -> nächster Stockwerksverteiler
    yo = 490
    S.pair([(vout[0], vout[1] - 2), (vout[0], yo), (vts.right + 70, yo)], ('red', 'yellow'))
    ex = vts.right + 70
    S.add('cables', line(ex + 4, yo, ex + 120, yo, stroke='#9AA0A7', stroke_width=2, stroke_dasharray='5 5'))
    S.add('cables', poly([(ex + 128, yo), (ex + 118, yo - 5.5), (ex + 118, yo + 5.5)], fill='#9AA0A7'))
    S.tlabel(vts.right + 10, yo + 18, 'OUT')
    S.add('labels', text(ex + 136, yo - 4, 'weitere Etage: OUT → IN', size=12, weight=700, fill=TXT2))
    S.add('labels', text(ex + 136, yo + 12, 'bis zu 16 Stockwerksverteiler', size=12, fill=TXT2))
    # (4) Stockwerksverteiler CH1–CH4 -> je 1 Innenstation (eigenes Aderpaar)
    hs = (358, 346, 346, 358)
    for i, (m, h) in enumerate(zip(mons, hs)):
        c = vts.a('CH%d' % (i + 1))
        tgt = (m.x + (95 - 8) * ms, m.bottom - 4)
        S.pair([c, (c[0], h), (tgt[0], h), tgt], ('red', 'yellow'))
    S.pill(536, 358, '2-Draht')
    S.pill(1000, 358, '2-Draht')
    S.step(596, 358, 4)
    for m in mons:
        S.tlabel(m.x + (95 - 8) * ms - 6, m.bottom + 20, 'IN', anchor='end')
    # (1) 48 V DC -> Verteiler (+ −)
    vneg, vpos = psu.a('V-i'), psu.a('V+i')
    pw = dist.a('PWR')
    plus, minus = (pw[0] - 2.2 * s, dist.bottom - 2), (pw[0] + 2.2 * s, dist.bottom - 2)
    gx = dist.right + 12
    S.wire([vpos, (vpos[0], 576), (gx + 4, 576), (gx + 4, 732), (plus[0], 732), plus], 'red', halo=halo_z)
    S.wire([vneg, (vneg[0], 584), (gx, 584), (gx, 726), (minus[0], 726), minus], 'black', halo=halo_z)
    S.pill(1000, 570, '48 V DC')
    S.step(1044, 570, 1)
    n, l = psu.a('N'), psu.a('L')
    S.wire([n, (n[0], 752)], 'blue', halo=halo_z)
    S.wire([l, (l[0], 752)], 'brown', halo=halo_z)
    S.pill((n[0] + l[0]) / 2, 752, '230 V AC')

    # ---- Drehschalter-Karte (Außenbereich unten)
    ax, ay, aw = 48, 596, 236
    lines = [('Türstation', 'Gebäude 01 · Tür 00'), ('Steinbach-Kehl', 'Zimmer 02'), ('Vossmann', 'Zimmer 04'),
             ('Zimmermann', 'Zimmer 06'), ('Innenerweiterung', 'Zi. 06 · Erw. 1')]
    S.add('labels', rect(ax, ay, aw, 164, rx=10, fill=WHITE, stroke='#E1E4EA', stroke_width=1))
    S.add('labels', text(ax + 16, ay + 28, 'Drehschalter', size=14, weight=700, fill=INK))
    for k, (a_, b_) in enumerate(lines):
        yy = ay + 52 + k * 17
        S.add('labels', text(ax + 16, yy, a_, size=12, weight=700, fill=INK))
        S.add('labels', text(ax + aw - 16, yy, b_, size=12, fill=TXT2, anchor='end'))
    S.add('labels', text(ax + 16, ay + 148, 'Alle Geräte: Gebäude-Nr. 01', size=12, weight=700, fill=TEAL))

    # ---- Info-Band
    S.info_band(796, steps=[
        'Transformator 48 V DC an 230 V anschließen und mit „+ −  48 VDC“ am Verteiler verbinden.',
        'Türstation an einen Kanal des Verteilers anschließen (hier CH1).',
        'Stockwerksverteiler: Eingang IN an einen weiteren Kanal (hier CH2) – ohne eigenes Netzteil.',
        'Jede Innenstation mit eigenem Aderpaar an CH1–CH4 des Stockwerksverteilers.',
        'Zimmer-Nr. je Klingeltaster einstellen: 3 Taster = Zimmer 02 / 04 / 06, Erweiterung auf 1.',
    ], notes=[
        'Set „8 Anschlüsse“ (Verteiler + 48-V-Transformator 150 W) für Anlagen mit mehr als 4 Innenstationen.',
        'Bis zu 16 Stockwerksverteiler pro Gebäude kaskadierbar (OUT → IN).',
        'Pro Gerät ein eigenes Aderpaar, keine Netzwerkkabel verwenden.',
        'Leitungslängen: Verteiler → Türstation ≤ 60 m; Verteiler → Innenstation ≤ 60 m (Twisted Pair ≤ 40 m).',
        '230-V-Leitungen ≥ 0,5 m entfernt verlegen. Verteiler im Medienverteiler montieren.',
    ], legend=[
        ('pair', ('red', 'yellow'), '2-Draht-BUS – 1 Aderpaar je Gerät, z. B. J-Y(St)Y 2×2×0,8'),
        ('pair', ('red', 'black'), '48 V DC · rot = +, schwarz = −'),
        ('pair', ('brown', 'blue'), '230 V AC · L braun, N blau (Elektrofachkraft)'),
    ],
        extra=[('Klingeltaster → Zimmer-Nr. (XDM10)', True), ('1 Taster: 03', False),
               ('2 Taster: 02 · 04', False), ('3 Taster: 02 · 04 · 06', False)],
    )
    S.footer(FOOT)
    return S.svg('Anschlussschema XDM10 Mehrfamilienhaus',
                 'XDM10 2-Draht-BUS mit 6-Kanal-Verteiler und 48-V-Transformator 150 W: MAXIOR-Türstation mit '
                 '3 Klingeltastern, Stockwerksverteiler mit 4 Innenstationen (3 Wohnungen und eine Innenerweiterung).')



# =================================================================================
# 3 · VDM10 2.0 · 2-Draht IP (Sternverkabelung)
# =================================================================================
def scheme_vdm10_2draht():
    S = Scene('v3', 1280, 1100)
    D = S.D
    S.header('Anschlussschema · VDM10 2-Draht IP',
             'Sternverkabelung am Video-/Audioverteiler VT6 · Türstation an CH6 · 3 Innenstationen · optional Router für die App',
             tags=('VDM10 2.0 · ADM10', '2-Draht IP · 24 V'),
             link=('Zum Produkt ↗', SHOP + 'metzler-vdm10-20-video-tuersprechanlage-1-klingeltaster-colson'))

    S.zone(32, 104, 928, 308, 'Wohnbereich')
    S.zone(976, 104, 272, 672, 'Außen · Hauseingang')
    S.zone(32, 428, 928, 348, 'Technikraum · Medienverteiler', fill='#EEF0F4', stroke='#E1E4EA')

    # ---- Innenstationen (Stern)
    ms = 0.86
    specs = ((96, 'white', 'Haupt-Innenstation · weiß'), (356, 'black', 'Neben-Innenstation · schwarz'),
             (616, 'white', 'Neben-Innenstation · weiß'))
    mons = []
    for x, col, sub in specs:
        m = S.place(vdm10_home(D, col, room='1'), x, 190, ms)
        S.caption(m.cx, 156, 'Innenstation Home 7″ · 2-Draht', (sub,))
        mons.append(m)
    hx, hy, hw = 822, 150, 124
    hl = wrap('Mischbetrieb möglich: Über einen PoE-Switch am LAN-Port lassen sich auch Innenstationen mit LAN/PoE einbinden.', 12, hw - 26)
    S.add('labels', rect(hx, hy, hw, 34 + 15 * len(hl), rx=10, fill=TEAL50, stroke='#D5E3E3', stroke_width=1))
    S.add('labels', text(hx + 13, hy + 22, 'Tipp', size=12, weight=700, fill=TEAL))
    for k, ln in enumerate(hl):
        S.add('labels', text(hx + 13, hy + 40 + k * 15, ln, size=12, fill=INK))

    # ---- Türstation (rechts)
    door = S.place(vdm10_colson(D, 'VOSSBERG'), 1054, 206, 0.86)
    S.caption(door.cx, 160, 'VDM10 2.0 · Colson', ('Türstation 2-Draht (VM-2W-2.0)',))
    S.add('labels', text(door.cx, 572, 'Anschluss immer an CH6', size=12, weight=700, fill=TEAL,
                         anchor='middle'))
    S.add('labels', text(door.cx, 588, '16 W für Türstation + Module', size=12, fill=TXT2,
                         anchor='middle'))

    # ---- Technikraum
    s = 1.35
    ytop = 560
    S.din_rail(452, 752, ytop + 45 * s)
    vt6 = S.place(dist_vdm10_vt6(D), 470, ytop, s)
    trafo = S.place(meanwell_hdr30(D, '24', '1.5', '36', model='VDM10-TRAFO'), 690, ytop, s)
    S.caption(vt6.x + 34, 724, 'VDM10-VT6-2.0', ('Video-/Audioverteiler', 'CH1–CH5 je 6 W · CH6 16 W'), anchor='start')
    S.caption(trafo.right + 18, 600, 'VDM10-TRAFO', ('24 V DC · 36 W', 'Hutschienen-Netzteil'), anchor='start')
    rt = S.place(router(D), 150, 690, 0.95)
    S.caption(rt.cx, 744, 'Router', ('optional · App & Einrichtung',))
    ph = S.place(smartphone(D), 56, 612, 0.9)
    S.add('labels', text(ph.cx, ph.y - 10, 'App', size=12, weight=700, fill=INK, anchor='middle'))

    halo_z = '#EEF0F4'
    # (3) Innenstationen: CH1 -> M1, CH2 -> M2, CH3 -> M3 (je eigenes Kabel)
    hs = (506, 490, 490)
    for i, (m, h) in enumerate(zip(mons, hs)):
        c = vt6.a('CH%d' % (i + 1))
        tgt = (m.cx, m.bottom - 4)
        S.pair([c, (c[0], h), (tgt[0], h), tgt], ('red', 'yellow'))
    S.pill(300, 506, '2-Draht')
    S.step(246, 506, 3)
    S.add('labels', text(248, 474, 'sternförmig: je Innenstation', size=12, weight=700, fill=TEAL))
    S.add('labels', text(248, 490, 'ein eigenes Kabel', size=12, weight=700, fill=TEAL))
    for i in range(3):
        c = vt6.a('CH%d' % (i + 1))
    S.tlabel(vt6.a('CH1')[0] - 5, 552, 'CH1', anchor='end')
    S.tlabel(vt6.a('CH3')[0] + 6, 552, 'CH2–3')
    # (2) Türstation -> CH6
    ch6 = vt6.a('CH6')
    S.pair([(door.cx, door.bottom - 4), (door.cx, 520), (ch6[0], 520), ch6], ('red', 'yellow'))
    S.pill(880, 520, '2-Draht')
    S.step(930, 520, 2)
    S.tlabel(ch6[0] + 6, 546, 'CH6')
    # (1) 24 V DC TRAFO -> VT6 (+ −)
    vneg, vpos = trafo.a('V-'), trafo.a('V+')
    pw = vt6.a('PWR')
    plus, minus = (pw[0] - 2.2 * s, vt6.bottom - 2), (pw[0] + 2.2 * s, vt6.bottom - 2)
    gx = vt6.right + 8
    S.wire([vpos, (vpos[0], 540), (gx + 4, 540), (gx + 4, 702), (plus[0], 702), plus], 'red', halo=halo_z)
    S.wire([vneg, (vneg[0], 548), (gx, 548), (gx, 696), (minus[0], 696), minus], 'black', halo=halo_z)
    S.pill(790, 540, '24 V DC')
    S.step(834, 540, 1)
    n, l = trafo.a('N'), trafo.a('L')
    S.wire([n, (n[0], 748)], 'blue', halo=halo_z)
    S.wire([l, (l[0], 748)], 'brown', halo=halo_z)
    S.pill(trafo.cx, 748, '230 V AC')
    # (4) LAN -> Router
    lan = vt6.a('LAN')
    S.lan([(lan[0], lan[1] - 3), (lan[0], 706), (rt.right + 14, 706)], halo=halo_z)
    S.pill(360, 706, 'LAN · Cat 7', fill=LAN_C[1])
    S.step(420, 706, 4)
    S.tlabel(lan[0] + 6, 698, 'LAN')
    # Kaskade: OUT -> weiterer Verteiler
    out = vt6.a('OUT')
    yc = 534
    S.pair([out, (out[0], yc), (430, yc)], ('red', 'yellow'))
    S.add('cables', line(426, yc, 330, yc, stroke='#9AA0A7', stroke_width=2, stroke_dasharray='5 5'))
    S.add('cables', poly([(322, yc), (332, yc - 5.5), (332, yc + 5.5)], fill='#9AA0A7'))
    S.add('labels', text(314, yc - 4, 'weiterer Verteiler: OUT → IN', size=12, weight=700, fill=TXT2, anchor='end'))
    S.add('labels', text(314, yc + 12, 'bis zu 15 kaskadierbar', size=12, fill=TXT2, anchor='end'))
    S.tlabel(out[0] - 6, 552, 'OUT', anchor='end')
    # WLAN/Internet zur App (schematisch)
    S.wlan((ph.right + 4, ph.y + 30), (rt.x + 8, rt.y + 6))
    S.step(mons[0].x - 26, mons[0].y + 58, 5)

    # ---- Info-Band
    S.info_band(796, steps=[
        'VDM10-TRAFO an 230 V anschließen und mit „+ −  24 VDC“ am Verteiler VT6 verbinden.',
        'Türstation immer an CH6 – dort stehen 16 W für Türstation und Module bereit.',
        'Jede Innenstation mit eigenem Kabel an CH1–CH5 (sternförmig, je 6 W).',
        'Optional: LAN-Port mit dem Router verbinden (App, PC-Software iVMS-4200).',
        'Innenstation einrichten: Sprache, Passwort, Netzwerk, Haupt-Türstation koppeln.',
    ], notes=[
        'Nur sternförmig anschließen – für jedes Gerät ein eigenes Kabel, kein Durchschleifen.',
        'Keine Netzwerkkabel für die 2-Draht-Strecken; geschirmte Leitung empfohlen.',
        'Twisted Pair 0,5 mm²: Türstation ≤ 60 m, Innenstation ≤ 100 m · 0,2 mm²: je ≤ 35 m.',
        'Verteiler nicht im Schaltschrank montieren, 230-V-Leitungen ≥ 0,5 m entfernt.',
        'Bis zu 15 Verteiler kaskadierbar, max. 500 Geräte. Gilt auch für ADM10 (Audio).',
    ], legend=[
        ('pair', ('red', 'yellow'), '2-Draht – 1 Aderpaar je Gerät (verdrillt, geschirmt empfohlen)'),
        ('lan', None, 'Netzwerkkabel Cat 5e–7 mit RJ45'),
        ('pair', ('red', 'black'), '24 V DC · rot = +, schwarz = −'),
        ('pair', ('brown', 'blue'), '230 V AC · L braun, N blau (Elektrofachkraft)'),
        ('wlan', None, 'Internet / WLAN zur Hik-Connect App'),
    ],
    )
    S.footer(FOOT)
    return S.svg('Anschlussschema VDM10 2-Draht IP',
                 'VDM10 2.0 im 2-Draht-IP-System: Türstation an CH6 und drei Innenstationen sternförmig an CH1–CH3 '
                 'des Verteilers VDM10-VT6-2.0 mit 24-V-Transformator; optional Router am LAN-Port.')



# =================================================================================
# 4 · VDM10 2.0 · LAN/PoE
# =================================================================================
def scheme_vdm10_poe():
    S = Scene('v4', 1280, 1100)
    D = S.D
    S.header('Anschlussschema · VDM10 LAN/PoE',
             'Netzwerk-Variante: Türstation und Innenstationen per Netzwerkkabel am PoE-Switch · Router für die App · Türöffner mit eigenem Netzteil',
             tags=('VDM10 2.0 · ADM10', 'LAN / PoE'),
             link=('Zum Produkt ↗', SHOP + 'metzler-vdm10-20-video-tuersprechanlage-1-klingeltaster-colson'))

    S.zone(32, 104, 928, 316, 'Wohnbereich')
    S.zone(976, 104, 272, 672, 'Außen · Hauseingang')
    S.zone(32, 436, 928, 340, 'Technikraum', fill='#EEF0F4', stroke='#E1E4EA')

    # ---- Innenstationen (Home 7'', Pro 7'', Ultra 10'')
    ms = 0.8
    home = S.place(vdm10_home(D, 'white', room='1'), 100, 218, ms)
    pro = S.place(vdm10_pro(D, room='1'), 330, 218, ms)
    ultra = S.place(vdm10_ultra(D, room='1'), 570, 330 - 166 * ms, ms)
    S.caption(home.cx, 176, 'Innenstation Home 7″ · LAN', ('Haupt-Innenstation · weiß',))
    S.caption(pro.cx, 176, 'Innenstation Pro 7″ · LAN', ('Neben-Innenstation',))
    S.caption(ultra.cx, ultra.y - 42, 'Innenstation Ultra 10,1″ · LAN', ('Neben-Innenstation',))

    # ---- Außen: Türstation + Türöffner
    door = S.place(vdm10_colson(D, 'VOSSBERG'), 1000, 206, 0.86)
    S.caption(door.cx, 160, 'VDM10 2.0 · Colson', ('Türstation LAN/PoE (VM-POE-2.0)',))
    strike = S.place(tueroeffner(D), 1172, 300, 0.95)
    S.caption(strike.cx + 6, 262, 'Türöffner', ('z. B. 12 V DC',))

    # ---- Technikraum
    sw = S.place(poe_switch(D, 4), 330, 560, 2.0)
    S.caption(sw.x, 644, 'PoE-Switch 4 × PoE', ('802.3af/at · 60 W',), anchor='start')
    sock = S.place(wall_socket(D), 170, 506, 0.8)
    ad = S.place(plug_adapter(D, '48 V DC'), 186, 548, 1.1)
    S.caption(ad.cx - 4, 648, 'Steckernetzteil', ('48 V DC für den Switch',))
    rt = S.place(router(D), 596, 690, 0.95)
    S.caption(rt.cx, 668, 'Router', ('Internet · optional',))
    ph = S.place(smartphone(D), 760, 640, 0.9)
    S.add('labels', text(ph.cx, ph.y - 10, 'App', size=12, weight=700, fill=INK, anchor='middle'))
    s = 1.3
    psu = S.place(meanwell_hdr30(D, '12', '2', '24', model='12 V DC'), 836, 560, s)
    S.caption(psu.cx, 724, 'Netzteil', ('Türöffner',))

    halo_z = '#EEF0F4'
    ports = [sw.a('P%d' % i) for i in range(1, 5)]
    top = lambda p: (p[0], sw.y + 2)
    # (3) Innenstationen: P1 -> Home, P2 -> Pro, P3 -> Ultra
    for (px, py), m, h, mx in ((ports[0], home, 500, home.x + home.w * 0.9), (ports[1], pro, 474, pro.cx),
                               (ports[2], ultra, 488, ultra.cx)):
        S.lan([top((px, py)), (px, h), (mx, h), (mx, m.bottom - 6)], halo='#FFFFFF', plug_end=False,
              plug_start=True)
    S.pill(318, 500, 'LAN · Cat 7', fill=LAN_C[1])
    S.step(364, 500, 3)
    # (2) Türstation -> P4
    p4 = top(ports[3])
    S.lan([(door.x + 30, door.bottom - 6), (door.x + 30, 520), (p4[0], 520), p4], plug_end=True, plug_start=False)
    S.pill(560, 520, 'LAN · Cat 7', fill=LAN_C[1])
    S.step(614, 520, 2)
    # (4) Uplink -> Router
    up = sw.a('UP')
    S.lan([(up[0], up[1] - 2), (up[0], 706), (rt.x - 2, 706)], halo=halo_z, plug_end=False, plug_start=True)
    S.step(up[0] + 30, 706, 4)
    S.wlan((rt.right + 4, rt.y + 4), (ph.x - 4, ph.y + 36))
    S.tlabel(ports[0][0] - 14, 552, 'PoE 1–3', anchor='end')
    S.tlabel(ports[3][0] + 8, 552, 'PoE 4')
    S.tlabel(up[0] + 8, 636, 'Uplink')
    # (1) Stromversorgung Switch: Steckdose -> Steckernetzteil -> DC-Eingang
    dc_in = (sw.x + 2, sw.y + sw.h * 0.5)
    S.wire([(ad.cx, ad.bottom - 2), (ad.cx, 628), (300, 628), (300, dc_in[1]), dc_in], 'black', halo=halo_z)
    S.step(ad.x - 20, ad.y + 26, 1)
    # (5) Türöffner: COM -> Netzteil +, NO1 -> Türöffner, Türöffner -> Netzteil −
    vneg, vpos = psu.a('V-'), psu.a('V+')
    com_x, no_x = door.x + 60, door.x + 90
    s_red, s_blk = strike.x + 6, strike.x + 19
    S.wire([(no_x, door.bottom - 6), (no_x, 470), (s_red, 470), (s_red, strike.bottom - 3)], 'red')
    S.wire([(com_x, door.bottom - 6), (com_x, 546), (vpos[0], 546), vpos], 'red', halo='#FFFFFF')
    S.wire([(s_blk, strike.bottom - 3), (s_blk, 554), (vneg[0], 554), vneg], 'black', halo='#FFFFFF')
    S.tlabel(com_x - 6, 492, 'COM', anchor='end')
    S.tlabel(no_x + 6, 462, 'NO1')
    S.pill(930, 546, '12 V DC')
    S.step(930, 574, 5)
    n, l = psu.a('N'), psu.a('L')
    S.wire([n, (n[0], 700)], 'blue', halo=halo_z)
    S.wire([l, (l[0], 700)], 'brown', halo=halo_z)
    S.pill(psu.cx, 700, '230 V AC')
    S.add('labels', text(1112, 600, 'Empfehlung:', size=12, weight=700, fill=TEAL, anchor='middle'))
    S.add('labels', text(1112, 616, 'Türöffner über das', size=12, fill=TXT2, anchor='middle'))
    S.add('labels', text(1112, 632, 'Sicherheitsmodul', size=12, fill=TXT2, anchor='middle'))
    S.add('labels', text(1112, 648, 'anschließen', size=12, fill=TXT2, anchor='middle'))

    # ---- Info-Band
    S.info_band(796, steps=[
        'PoE-Switch über das Steckernetzteil (48 V DC) mit Strom versorgen.',
        'Türstation (LAN/PoE) mit Netzwerkkabel an einen PoE-Port anschließen.',
        'Jede Innenstation mit eigenem Netzwerkkabel an einen PoE-Port (IEEE 802.3af).',
        'Uplink-Port mit dem Router verbinden – für App und Einrichtung per PC.',
        'Türöffner: COM → Netzteil (+), NO1 → Türöffner, Türöffner → Netzteil (−).',
    ], notes=[
        'Netzwerkkabel CAT5e bis 60 m, ab CAT6 bis 100 m; an jedem Anschluss 1,5–2 m Reserve lassen und beschriften.',
        'Türöffner mit separater Leitung und eigenem Netzteil (Relais max. 30 V / 1 A).',
        'Innenstation nicht gleichzeitig per LAN und WLAN mit demselben Router verbinden.',
        'Ohne PoE: Home/Ultra über Netzteil 12 V (3 m Kabel) versorgen – nicht für Pro.',
        '230-V-Leitungen ≥ 0,5 m entfernt verlegen. Gilt auch für ADM10 (Audio).',
    ], legend=[
        ('lan', None, 'Netzwerkkabel Cat 5e–7 mit RJ45 (Daten + PoE)'),
        ('pair', ('red', 'black'), '12 / 48 V DC · rot = +, schwarz = −'),
        ('pair', ('brown', 'blue'), '230 V AC · L braun, N blau (Elektrofachkraft)'),
        ('wlan', None, 'Internet / WLAN zur Hik-Connect App'),
    ],
    )
    S.footer(FOOT)
    return S.svg('Anschlussschema VDM10 LAN/PoE',
                 'VDM10 2.0 in der LAN/PoE-Variante: Türstation und drei Innenstationen (Home, Pro, Ultra) am '
                 'PoE-Switch 4 × PoE, Uplink zum Router; Türöffner direkt an der Türstation mit eigenem 12-V-Netzteil.')



# =================================================================================
# 5 · SDM10 · LAN mit Sicherheitsmodul und Türöffner
# =================================================================================
def scheme_sdm10():
    S = Scene('s5', 1280, 1140)
    D = S.D
    S.header('Anschlussschema · SDM10 mit Türöffner',
             'Türstation mit Gesichtserkennung per LAN · eigenes 12-V-Netzteil · Innenstationen per PoE · Türöffner über Sicherheitsmodul',
             tags=('SDM10X · SDM10H · SDM10S', 'LAN · 12 V DC'),
             link=('Zum Produkt ↗', SHOP + 'metzler-tuersprechanlage-mit-kamera-gesichtserkennung-touch-display-live-hd-video-ein-und-mehrfamilien-sdm10x'))

    S.zone(32, 104, 928, 296, 'Wohnbereich')
    S.zone(976, 104, 272, 712, 'Außen · Hauseingang')
    S.zone(32, 416, 928, 400, 'Technikraum', fill='#EEF0F4', stroke='#E1E4EA')

    # ---- Innenstationen
    ms = 0.8
    home = S.place(vdm10_home(D, 'white', room='1'), 80, 216, ms)
    ultra = S.place(vdm10_ultra(D, room='1'), 330, 328 - 166 * ms, ms)
    S.caption(home.cx, 176, 'Innenstation Home 7″ · LAN', ('Haupt-Innenstation',))
    S.caption(ultra.cx, ultra.y - 42, 'Innenstation Ultra 10,1″ · LAN', ('Neben-Innenstation',))
    hx, hy, hw = 620, 150, 320
    hl = wrap('Die SDM10-Türstation unterstützt kein PoE: Sie braucht ein eigenes 12-V-Netzteil (2 A) und ein '
              'Netzwerkkabel. Die Innenstationen werden über den PoE-Switch versorgt.', 12, hw - 28)
    S.add('labels', rect(hx, hy, hw, 34 + 15 * len(hl), rx=10, fill=TEAL50, stroke='#D5E3E3', stroke_width=1))
    S.add('labels', text(hx + 14, hy + 22, 'Wichtig', size=12, weight=700, fill=TEAL))
    for k, ln in enumerate(hl):
        S.add('labels', text(hx + 14, hy + 40 + k * 15, ln, size=12, fill=INK))

    # ---- Außen
    door = S.place(sdm10x(D), 1008, 222, 0.62)
    S.caption(door.cx, 146, 'SDM10X', ('Türstation mit Gesichtserkennung', 'LAN · 12 V DC / 2 A',
                                       'Abgänge: LAN · A1/A2 · C3/C4'))
    strike = S.place(tueroeffner(D), 1178, 300, 0.95)
    S.caption(strike.cx + 2, 262, 'Türöffner', ('12 V DC',))
    # Tabelle Leitungsquerschnitt 12 V
    tx, ty, tw = 992, 560, 240
    S.add('labels', rect(tx, ty, tw, 226, rx=10, fill=WHITE, stroke='#E1E4EA', stroke_width=1))
    S.add('labels', text(tx + 16, ty + 28, '12-V-Zuleitung Türstation', size=14, weight=700, fill=INK))
    S.add('labels', text(tx + 16, ty + 46, 'max. Länge bei 2 A (≤ 3 % Abfall)', size=12, fill=TXT2))
    rows = (('0,28 mm² (J-Y(St)Y 0,6)', 'ca. 1 m'), ('0,5 mm²', '≤ 3 m'), ('1,0 mm²', '≤ 6 m'),
            ('1,5 mm²', '≤ 7 m'))
    for k, (a_, b_) in enumerate(rows):
        yy = ty + 74 + k * 24
        S.add('labels', line(tx + 16, yy + 8, tx + tw - 16, yy + 8, stroke=HAIR, stroke_width=1))
        S.add('labels', text(tx + 16, yy, a_, size=12, fill=INK))
        S.add('labels', text(tx + tw - 16, yy, b_, size=12, weight=700, fill=INK, anchor='end'))
    S.add('labels', text(tx + 16, ty + 186, 'Netzteil nah an der Türstation', size=12, weight=700, fill=TEAL))
    S.add('labels', text(tx + 16, ty + 202, 'montieren (geschützter Innenbereich).', size=12, fill=TEAL))

    # ---- Technikraum: Switch, Router, DIN-Schiene
    sw = S.place(poe_switch(D, 8), 170, 540, 1.4)
    S.caption(sw.x, 614, 'Gigabit-PoE-Switch 8 × PoE', ('802.3af/at · 110 W',), anchor='start')
    sock = S.place(wall_socket(D), 60, 470, 0.8)
    ad = S.place(plug_adapter(D, '48 V DC'), 70, 512, 1.1)
    rt = S.place(router(D), 380, 720, 0.95)
    S.caption(rt.cx, 700, 'Router', ('Internet · optional',))
    ph = S.place(smartphone(D), 508, 670, 0.9)
    S.add('labels', text(ph.cx, ph.y - 10, 'App', size=12, weight=700, fill=INK, anchor='middle'))

    s = 1.2
    ytop = 590
    S.din_rail(566, 912, ytop + 45 * s)
    trafo = S.place(meanwell_hdr30(D, '12', '2', '24', model='SDM10-TRAFO'), 580, ytop, s)
    psu_sm = S.place(meanwell_hdr30(D, '12', '2', '24', model='12 V DC'), 640, ytop, s)
    sm = S.place(sicherheitsmodul(D), 700, ytop + (90 - 76) / 2 * s, s)
    psu_to = S.place(meanwell_hdr30(D, '12', '2', '24', model='12 V DC'), 858, ytop, s)
    cy = 756
    S.caption(trafo.cx, cy, 'SDM10-TRAFO', ('12 V · 24 W',))
    S.caption(psu_sm.cx + 4, cy + 36, 'Netzteil Modul', ())
    S.caption(sm.cx + 8, cy, 'Sicherheitsmodul', ('DIP 1 = ON',))
    S.caption(psu_to.cx, cy + 36, 'Netzteil Türöffner', ())

    halo_z = '#EEF0F4'
    top = lambda p: (p[0], sw.y + 2)
    p1, p2, p8, up = sw.a('P1'), sw.a('P2'), sw.a('P8'), sw.a('UP')
    # (3) Innenstationen an PoE-Ports, Uplink -> Router
    S.lan([top(p1), (p1[0], 470), (home.cx, 470), (home.cx, home.bottom - 6)], plug_end=False, plug_start=True)
    S.lan([top(p2), (p2[0], 450), (ultra.cx, 450), (ultra.cx, ultra.bottom - 6)], plug_end=False, plug_start=True)
    S.pill(home.cx, 372, 'LAN · Cat 7', fill=LAN_C[1])
    S.step(home.cx + 56, 372, 3)
    S.lan([(up[0], up[1] - 2), (up[0], 736), (rt.x - 2, 736)], halo=halo_z, plug_end=False, plug_start=True)
    S.wlan((rt.right - 18, rt.y - 4), (ph.x - 4, ph.y + 12))
    # Switch-Stromversorgung
    dc_in = (sw.x + 2, sw.y + sw.h * 0.5)
    S.wire([(ad.cx, ad.bottom - 2), (ad.cx, 596), (150, 596), (150, dc_in[1]), dc_in], 'black', halo=halo_z)
    S.caption(ad.cx, 630, 'Steckernetzteil', ('48 V DC',))

    # Türstation-Abgänge (von links nach rechts): LAN, 12 V, RS-485 ; Türöffner rechts daneben
    lan_x, v12_x, rs_x = door.x + 24, door.x + 58, door.x + 92
    y_lan, y_12, y_rs, y_to = 470 + 22, 506, 522, 538
    # (2) LAN Türstation -> P8
    p8t = top(p8)
    S.lan([(lan_x, door.bottom - 6), (lan_x, y_lan), (p8t[0], y_lan), p8t])
    S.pill(760, y_lan, 'LAN · Cat 6/7', fill=LAN_C[1])
    S.step(816, y_lan, 2)
    # (1) 12 V DC SDM10-TRAFO -> A1 (+12 V, rot) / A2 (GND, schwarz)
    tneg, tpos = trafo.a('V-'), trafo.a('V+')
    S.pair([(v12_x, door.bottom - 6), (v12_x, y_12), (tpos[0] + 6, y_12)], ('red', 'black'), ends=[tpos, tneg])
    S.pill(900, y_12, '12 V DC')
    S.step(944, y_12, 1)
    # (4) RS-485 C3 (grün, +) / C4 (weiß, −) -> Sicherheitsmodul 3 / 4
    t3, t4 = sm.a('T3'), sm.a('T4')
    S.pair([(rs_x, door.bottom - 6), (rs_x, y_rs), (t4[0] + 6, y_rs)], ('green', 'white'), ends=[t3, t4])
    S.pill(820, y_rs + 1, 'RS-485')
    S.step(866, y_rs + 1, 4)
    # Türöffner: rot -> 20 DOOR_NO, schwarz -> Netzteil Türöffner −V ; Brücke +V -> 19 DOOR_COM
    t19, t20 = sm.a('T19'), sm.a('T20')
    vneg, vpos = psu_to.a('V-'), psu_to.a('V+')
    S.pair([(strike.cx, strike.bottom - 4), (strike.cx, y_to), (vneg[0] + 6, y_to)], ('red', 'black'),
           ends=[t20, vneg])
    S.step(1110, y_to, 5)
    S.wire([vpos, (vpos[0], 578), (t19[0], 578), t19], 'red', halo=halo_z)
    # Modul-Versorgung 12 V -> 1 / 2
    t1, t2 = sm.a('T1'), sm.a('T2')
    mneg, mpos = psu_sm.a('V-'), psu_sm.a('V+')
    S.wire([mneg, (mneg[0], 570), (t2[0], 570), t2], 'black', halo=halo_z)
    S.wire([mpos, (mpos[0], 578), (t1[0], 578), t1], 'red', halo=halo_z)
    # 230 V AC
    for p in (trafo, psu_sm, psu_to):
        n, l = p.a('N'), p.a('L')
        S.wire([n, (n[0], 726)], 'blue', halo=halo_z)
        S.wire([l, (l[0], 726)], 'brown', halo=halo_z)
    S.pill((trafo.cx + psu_sm.cx) / 2, 726, '230 V AC')
    S.pill(psu_to.cx, 726, '230 V AC')

    # ---- Info-Band
    S.info_band(836, steps=[
        'SDM10-TRAFO an 230 V und an A1 (+12 V, rot) / A2 (GND, schwarz) der Türstation.',
        'Türstation per Netzwerkkabel (Cat 6/7) mit dem Switch verbinden.',
        'Innenstationen per Netzwerkkabel an PoE-Ports, Uplink zum Router.',
        'RS-485: C3 (grün, +) / C4 (weiß, −) an Klemme 3 / 4, Modul-Netzteil an 1 / 2.',
        'Türöffner an 20 DOOR_NO, +12 V an 19 DOOR_COM. Zuerst Modul, dann Anlage einschalten.',
    ], notes=[
        'Die Türstation braucht 12 V DC / 2 A – Zuleitung kurz halten (Tabelle rechts).',
        'Netzwerkkabel CAT5e bis 60 m, ab CAT6 bis 100 m; PoE nach IEEE 802.3af.',
        'Sicherheitsmodul im geschützten Innenbereich, als letztes Gerät am RS-485-Bus.',
        'Nur Türöffner mit 12 V DC am Sicherheitsmodul; eigenes Netzteil empfohlen.',
        'Nur eine 2-Draht-Leitung vorhanden? 2-Draht-LAN/PoE-Konverter nutzen (immer paarweise).',
    ], legend=[
        ('lan', None, 'Netzwerkkabel Cat 6/7 mit RJ45'),
        ('pair', ('red', 'black'), '12 / 48 V DC · rot = +, schwarz = −'),
        ('pair', ('green', 'white'), 'RS-485 · C3 grün (+), C4 weiß (−)'),
        ('pair', ('brown', 'blue'), '230 V AC · L braun, N blau (Elektrofachkraft)'),
        ('wlan', None, 'Internet / WLAN zur Hik-Connect App'),
    ],
    )
    S.footer(FOOT)
    return S.svg('Anschlussschema SDM10 mit Türöffner',
                 'SDM10-Türstation mit Gesichtserkennung: 12 V DC über den SDM10-TRAFO, LAN zum Gigabit-PoE-Switch, '
                 'Innenstationen per PoE, Türöffner über das Metzler Sicherheitsmodul (RS-485) mit eigenen 12-V-Netzteilen.')


# id, Dateiname, Funktion
SCHEMES = [
    ('xdm10-einfamilienhaus', 'xdm10-einfamilienhaus-tueroeffner', scheme_xdm10_efh),
    ('xdm10-mehrfamilienhaus', 'xdm10-mehrfamilienhaus-stockwerksverteiler', scheme_xdm10_mfh),
    ('vdm10-2-draht-ip', 'vdm10-2-draht-ip-stern', scheme_vdm10_2draht),
    ('vdm10-lan-poe', 'vdm10-lan-poe', scheme_vdm10_poe),
    ('sdm10-sicherheitsmodul', 'sdm10-lan-sicherheitsmodul', scheme_sdm10),
]
