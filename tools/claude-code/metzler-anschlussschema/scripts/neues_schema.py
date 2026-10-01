# -*- coding: utf-8 -*-
"""
VORLAGE für ein neues Anschlussschema.

So benutzen:
  1. Diese Datei in den Arbeitsordner kopieren (NICHT im Design-System ändern), z. B. mein_schema.py.
  2. Funktion umbenennen, Geräte/Leitungen/Texte anpassen (Regeln: references/systeme.md, Stil: references/stil.md).
  3. Bauen und prüfen:
       python3 <skill>/scripts/build.py --module mein_schema.py --out . --png
     → Warnungen lesen, PNG ansehen (Ausschnitte zoomen), korrigieren, wiederholen.

Das Beispiel unten ist vollständig lauffähig: VDM10 2.0 · 2-Draht IP · Kian + 1 Innenstation.
Koordinaten: Zeichenfläche 1280 px breit, y nach unten. Geräte in mm gezeichnet, platziert mit Maßstab s.
"""
import os
import sys

# Pfad zu den Skill-Skripten: dieser Ordner, sonst der installierte Skill (~/.claude/skills/…)
SKILL_SCRIPTS = os.environ.get('METZLER_SCHEMA_SCRIPTS') or os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(os.path.join(SKILL_SCRIPTS, 'scheme.py')):
    SKILL_SCRIPTS = os.path.expanduser('~/.claude/skills/metzler-anschlussschema/scripts')
sys.path.insert(0, SKILL_SCRIPTS)
from scheme import *  # noqa: E402,F401,F403  (Scene, Leitungsfarben, Texthelfer, Geräte)


def scheme_beispiel():
    # 1) Fläche + Kopfzeile (Titel 24 px, Untertitel 14 px, System-Tags, Produkt-Link)
    S = Scene('bsp', 1280, 1100)                     # Präfix muss je Schema eindeutig sein (Gradient-IDs)
    D = S.D
    S.header('Anschlussschema · VDM10 2-Draht IP (Beispiel)',
             'Vorlage: Türstation an CH6 · 1 Innenstation an CH1 · Verteiler VT6 mit 24-V-Transformator',
             tags=('VDM10 2.0', '2-Draht IP · 24 V'),
             link=('Zum Produkt ↗', SHOP + 'metzler-vdm10-20-video-tuersprechanlage-1-klingeltaster-kian'))

    # 2) Zonen: wo wird montiert? (Wohnbereich · Außen · Technikraum)
    S.zone(32, 104, 928, 308, 'Wohnbereich')
    S.zone(976, 104, 272, 672, 'Außen · Hauseingang')
    S.zone(32, 428, 928, 348, 'Technikraum · Medienverteiler', fill='#EEF0F4', stroke='#E1E4EA')

    # 3) Geräte platzieren – immer aus devices.py, nie frei zeichnen
    mon = S.place(vdm10_home(D, 'white', room='1'), 300, 190, 0.86)
    S.caption(mon.cx, 156, 'Innenstation Home 7″ · 2-Draht', ('Haupt-Innenstation · weiß',))
    door = S.place(vdm10_kian(D, 'Steinbach'), 1054, 206, 0.86)
    S.caption(door.cx, 160, 'VDM10 2.0 · Kian', ('Türstation 2-Draht (VM-2W-2.0)',))

    s = 1.35                                           # Hutschienen-Maßstab
    ytop = 560
    S.din_rail(452, 752, ytop + 45 * s)
    vt6 = S.place(dist_vdm10_vt6(D), 470, ytop, s)
    trafo = S.place(meanwell_hdr30(D, '24', '1.5', '36', model='VDM10-TRAFO'), 690, ytop, s)
    S.caption(vt6.x + 34, 724, 'VDM10-VT6-2.0', ('Video-/Audioverteiler',), anchor='start')
    S.caption(trafo.right + 18, 600, 'VDM10-TRAFO', ('24 V DC · 36 W',), anchor='start')

    # 4) Leitungen – orthogonale Punktlisten; Anschlusspunkte über p.a('NAME')
    halo_z = '#EEF0F4'                                 # Halo = Hintergrundfarbe der Zone
    ch1, ch6 = vt6.a('CH1'), vt6.a('CH6')
    S.pair([ch1, (ch1[0], 480), (mon.cx, 480), (mon.cx, mon.bottom - 4)], ('red', 'yellow'))      # 2-Draht
    S.pill(420, 480, '2-Draht')
    S.step(370, 480, 3)
    S.pair([(door.cx, door.bottom - 4), (door.cx, 520), (ch6[0], 520), ch6], ('red', 'yellow'))
    S.pill(880, 520, '2-Draht')
    S.step(930, 520, 2)
    S.tlabel(ch1[0] - 5, 552, 'CH1', anchor='end')
    S.tlabel(ch6[0] + 6, 546, 'CH6')
    # 24 V DC: rot = +, schwarz = − ; jede Ader einzeln auf ihre Klemme
    vneg, vpos = trafo.a('V-'), trafo.a('V+')
    pw = vt6.a('PWR')
    plus, minus = (pw[0] - 2.2 * s, vt6.bottom - 2), (pw[0] + 2.2 * s, vt6.bottom - 2)
    gx = vt6.right + 8
    S.wire([vpos, (vpos[0], 540), (gx + 4, 540), (gx + 4, 702), (plus[0], 702), plus], 'red', halo=halo_z)
    S.wire([vneg, (vneg[0], 548), (gx, 548), (gx, 696), (minus[0], 696), minus], 'black', halo=halo_z)
    S.pill(790, 540, '24 V DC')
    S.step(834, 540, 1)
    n, l = trafo.a('N'), trafo.a('L')                 # 230 V: N blau, L braun
    S.wire([n, (n[0], 748)], 'blue', halo=halo_z)
    S.wire([l, (l[0], 748)], 'brown', halo=halo_z)
    S.pill(trafo.cx, 748, '230 V AC')

    # 5) Info-Band: Schritte (gleiche Nummern wie die Badges), Hinweise, Legende – Höhe passt sich an
    S.info_band(796, steps=[
        'VDM10-TRAFO an 230 V anschließen und mit „+ −  24 VDC“ am Verteiler VT6 verbinden.',
        'Türstation immer an CH6 – dort stehen 16 W zur Verfügung.',
        'Innenstation mit eigenem Kabel an CH1–CH5 (sternförmig).',
    ], notes=[
        'Nur sternförmig anschließen – für jedes Gerät ein eigenes Kabel.',
        'Keine Netzwerkkabel für 2-Draht; Twisted Pair 0,5 mm²: Türstation ≤ 60 m, Innenstation ≤ 100 m.',
        'Verteiler nicht im Schaltschrank montieren, 230-V-Leitungen ≥ 0,5 m entfernt.',
    ], legend=[
        ('pair', ('red', 'yellow'), '2-Draht – 1 Aderpaar je Gerät'),
        ('pair', ('red', 'black'), '24 V DC · rot = +, schwarz = −'),
        ('pair', ('brown', 'blue'), '230 V AC · L braun, N blau (Elektrofachkraft)'),
    ])
    S.footer(FOOT)
    return S.svg('Anschlussschema VDM10 2-Draht IP (Beispiel)',
                 'Vorlage: VDM10 2.0 Kian an CH6, eine Innenstation an CH1 des Verteilers VT6 mit 24-V-Transformator.')


# id, Dateiname ohne Endung, Funktion – build.py baut alle Einträge
SCHEMES = [
    ('beispiel', 'anschlussschema-beispiel', scheme_beispiel),
]

if __name__ == '__main__':
    out = os.getcwd()
    for _id, base, fn in SCHEMES:
        for p in write(fn(), out, base, pdf=True, png=True):
            print('geschrieben:', p)
        for w in last_scene().check():
            print('  ⚠', w)
