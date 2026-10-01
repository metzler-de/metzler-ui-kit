#!/usr/bin/env python3
"""Step 3: knowledge/products.json -> knowledge/products.md + knowledge/products/<slug>.md

    python3 render.py
"""
import json, os, re, statistics, unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
KN = os.path.normpath(os.path.join(HERE, '..', '..', 'knowledge'))
MAX_BYTES = 150 * 1024


def slug(s):
    s = s.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('Ä', 'Ae').replace('Ö', 'Oe') \
         .replace('Ü', 'Ue').replace('ß', 'ss').replace('&', 'und')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def eur(x):
    if x is None:
        return ''
    s = '{:,.2f}'.format(x).replace(',', 'X').replace('.', ',').replace('X', '.')
    return s + ' €'


def num(x):
    if x is None:
        return '?'
    return ('%g' % x).replace('.', ',')


def cell(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ')


def dims(p):
    d = p.get('dimensions')
    if not d:
        return ''
    if d.get('b') is not None and d.get('h') is not None and d.get('t') is not None:
        return '%s × %s × %s %s' % (num(d['b']), num(d['h']), num(d['t']), d['unit'])
    return '%s: %s' % (d.get('label') or '', d.get('text') or '')


def min_price(p):
    """Lowest unit price a customer can buy at (cheapest child article, else the parent), JSON-LD based."""
    return p.get('price_from') if p.get('price_from') is not None else p['price']


def de_num(s):
    m = re.search(r'\d[\d.]*(?:,\d+)?', s or '')
    return float(m.group(0).replace('.', '').replace(',', '.')) if m else None


def preis_ab(p):
    """Price as the shop's buy box shows it, with notes where JSON-LD unit prices tell more."""
    pt = p['price_text'] or eur(p['price'])
    lab = p.get('price_label') or ''
    if lab.startswith('Unverbindliche'):
        return 'UVP %s (Fachpartner)' % pt
    if p.get('bulk_prices') and lab == 'ab' and de_num(pt) == min(b['price'] for b in p['bulk_prices']):
        return '%s (Staffelpreis ab %s)' % (eur(min_price(p)), pt[3:].strip())
    pf = p.get('price_from')
    if p['variants'] and pf is not None and de_num(pt) != pf:
        pt += ' (Varianten ab %s)' % eur(pf)
    if p.get('price_old_text'):
        pt += ' statt %s' % p['price_old_text']
    return pt


def farben(p):
    g = next((g for g in p.get('variation_groups', []) if g['group'] == 'Farbe'), None)
    if not g:
        return '–'
    parts = []
    for v in g['values']:
        s = v['name'] or '?'
        if v.get('surcharge_text'):
            s += ' (%s)' % v['surcharge_text']
        parts.append(s)
    return '%d: %s' % (len(parts), ', '.join(parts))


def other_vars(p):
    """Non-colour child variation groups, e.g. 'Anzahl der Klingeltaster: 1 Fach–5 Fach (5)'."""
    out = []
    for g in p.get('variation_groups', []):
        if g['group'] == 'Farbe':
            continue
        vals = [v['name'] for v in g['values']]
        out.append('%s: %s' % (g['group'], ', '.join(vals) if len(vals) <= 6 else '%s … %s (%d)' % (vals[0], vals[-1], len(vals))))
    return '; '.join(out)


def main():
    data = json.load(open(os.path.join(KN, 'products.json'), encoding='utf-8'))
    prods = data['products']
    by_cat = defaultdict(list)
    for p in prods:
        by_cat[p['main_category'] or 'Ohne Kategorie'].append(p)
    order = sorted(by_cat, key=lambda c: (-len(by_cat[c]), c))
    os.makedirs(os.path.join(KN, 'products'), exist_ok=True)
    date = data['generated'][:10]

    # ---------- per-category files ----------
    files = {}
    for cat in order:
        ps = by_cat[cat]
        fn = slug(cat) + '.md'
        files[cat] = fn
        L = []
        L.append('# %s — Produktübersicht' % cat)
        L.append('')
        L.append('Quelle: %s · Stand %s · %d Elternartikel, %d Kindartikel (Varianten) · generiert von `tools/shop-data/` '
                 '(Details je Artikel in `knowledge/products.json`, Schlüssel `kArtikel`).'
                 % (data['source'], date, len(ps), sum(len(p['variants']) for p in ps)))
        L.append('')
        L.append('Preise brutto inkl. 19 % MwSt. „Preis ab“ = Preisanzeige der Elternseite wie im Shop; Zusätze: '
                 '„Varianten ab“ = günstigster Kindartikel, falls abweichend; „Staffelpreis ab“ = Mengenrabatt; '
                 '„statt“ = durchgestrichener Preis; „UVP (Fachpartner)“ = nur über Fachpartner. Maße B × H × T laut Artikelseite. '
                 'Farben = Farbvarianten (Kindartikel) mit Aufpreis, falls der Shop einen zeigt. 3D = Live-3D-Konfigurator. '
                 'Leere Zelle = Wert steht nicht im Shop.')
        L.append('')
        sub = defaultdict(list)
        for p in ps:
            sub[' › '.join(p['category_path'][1:]) or '(direkt in %s)' % cat].append(p)
        L.append('| Unterkategorie | Artikel |')
        L.append('|---|---|')
        for s in sorted(sub, key=lambda s: (s.startswith('('), s)):
            L.append('| %s | %d |' % (cell(s), len(sub[s])))
        L.append('')
        for s in sorted(sub, key=lambda s: (s.startswith('('), s)):
            L.append('## %s' % s)
            L.append('')
            L.append('| Name | Art.-Nr. | Preis ab | Maße B×H×T | Farben | weitere Varianten | 3D | Link |')
            L.append('|---|---|---|---|---|---|---|---|')
            for p in sorted(sub[s], key=lambda p: (min_price(p) is None, min_price(p) or 0, p['name'])):
                L.append('| %s | %s | %s | %s | %s | %s | %s | [Shop](%s) |' % (
                    cell(p['name']), cell(p['artikelnummer']), cell(preis_ab(p)), dims(p), cell(farben(p)),
                    cell(other_vars(p)), 'ja' if p['has_3d'] else '', p['url']))
            L.append('')
        txt = '\n'.join(L)
        size = len(txt.encode('utf-8'))
        if size > MAX_BYTES:
            print('WARNING %s is %d bytes (> 150 KB)' % (fn, size))
        open(os.path.join(KN, 'products', fn), 'w', encoding='utf-8').write(txt)
        print('%-40s %4d rows %7d bytes' % (fn, len(ps), size))

    # ---------- articles without category (configurator building blocks) ----------
    unc = data.get('uncategorized') or []
    if unc:
        L = ['# Artikel ohne Shop-Kategorie (Konfigurator-Bausteine)', '',
             'Quelle: %s · Stand %s · %d Artikel. Diese Artikel haben eine eigene Seite, hängen aber in keiner '
             'Kategorie (Breadcrumb nur „Startseite“). Fast alle sind Optionen im Produkt-Konfigurator '
             '(Schriftart, Ausrichtung, Taster, Dübel, Größen …). Nicht in den Kategorie-Zählungen enthalten.'
             % (data['source'], date, len(unc)), '',
             '| Name | Art.-Nr. | Preis | kArtikel | Link |', '|---|---|---|---|---|']
        for p in sorted(unc, key=lambda p: p['name'] or ''):
            L.append('| %s | %s | %s | %s | [Shop](%s) |' % (cell(p['name']), cell(p['artikelnummer']),
                                                           cell(p['price_text'] or eur(p['price'])), p['kArtikel'], p['url']))
        open(os.path.join(KN, 'products', 'konfigurator-bausteine.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

    # ---------- index ----------
    L = []
    L.append('# Metzler Shop — Produktwissen (edelstahl-tuerklingel.de)')
    L.append('')
    L.append('Stand: %s · Quelle: %s · %d Elternartikel · %d Kindartikel (Farb- und andere Varianten).'
             % (data['generated'], data['source'], len(prods), sum(len(p['variants']) for p in prods)))
    L.append('')
    L.append('**So benutzen:** Für exakte Werte (Name, Art.-Nr., Preis, Maße, Merkmale, Farben, Bilder) immer '
             '`knowledge/products.json` lesen (ein Eintrag je Elternartikel, Varianten unter `variants`). '
             'Die Kategorie-Dateien unten sind kompakte Tabellen zum Überblick. Nichts ist geschätzt: '
             'fehlt ein Wert im Shop, ist das Feld leer/`null`. Neu erzeugen: `tools/shop-data/README.md`.')
    L.append('')
    L.append('**Hinweise:** Art.-Nr. = Hersteller-Artikelnummer (JSON-LD `mpn`, z. B. „smAP_11080“). Die Zeile '
             '„Artikelnummer“ auf der Artikelseite zeigt dagegen die interne ID `kArtikel` (Feld `artnr_display`). '
             '„ab“-Preise: `price_from` (günstigster Kindartikel) verwenden, nicht `price` der Elternseite. '
             'XDM10 PRO wird mit UVP „verbindliches Angebot über Ihren Fachpartner“ gezeigt. '
             'Jeder Artikel steht in genau einer Hauptkategorie (Breadcrumb), auch wenn der Shop ihn zusätzlich anderswo listet.')
    L.append('')
    L.append('## Kategorien')
    L.append('')
    L.append('| Hauptkategorie | Artikel | Kindartikel | Preis von – bis | Median | mit 3D | Entwurf vor Fertigung | Datei |')
    L.append('|---|---|---|---|---|---|---|---|')
    for cat in order:
        ps = by_cat[cat]
        pr = [min_price(p) for p in ps if min_price(p) is not None]
        n3 = sum(p['has_3d'] for p in ps)
        ne = sum(p['entwurf_vor_fertigung']['offered'] for p in ps)
        L.append('| %s | %d | %d | %s – %s | %s | %d (%d %%) | %d | [%s](products/%s) |' % (
            cell(cat), len(ps), sum(len(p['variants']) for p in ps),
            eur(min(pr)) if pr else '', eur(max(pr)) if pr else '', eur(statistics.median(pr)) if pr else '',
            n3, round(100 * n3 / len(ps)), ne, files[cat], files[cat]))
    n3 = sum(p['has_3d'] for p in prods)
    L.append('| **Gesamt** | **%d** | **%d** | | | **%d (%d %%)** | **%d** | |' % (
        len(prods), sum(len(p['variants']) for p in prods), n3, round(100 * n3 / len(prods)),
        sum(p['entwurf_vor_fertigung']['offered'] for p in prods)))
    L.append('')
    L.append('Preise = günstigster Preis je Elternartikel (Elternseite oder Kindartikel), brutto inkl. 19 % MwSt., '
             'ohne Konfigurator-Optionen. 3D = Live-3D-Konfigurator auf der Artikelseite.')
    L.append('')

    # brands
    L.append('## Marken (JSON-LD brand)')
    L.append('')
    L.append('| Marke | Artikel | Hauptkategorien |')
    L.append('|---|---|---|')
    br = defaultdict(list)
    for p in prods:
        br[p.get('brand') or '(keine Angabe)'].append(p)
    for b in sorted(br, key=lambda b: -len(br[b])):
        cats = Counter(p['main_category'] for p in br[b])
        L.append('| %s | %d | %s |' % (cell(b), len(br[b]), ', '.join('%s (%d)' % kv for kv in cats.most_common())))
    L.append('')

    # series
    L.append('## Serien / Modellfamilien')
    L.append('')
    L.append('Erkannt am Produktnamen (Liste in `parse.py`, `SERIES`). Briefkasten- und Klingel-Modelle tragen '
             'meist einen Vornamen nach dem „|“ (z. B. „| Siebert“, „| Sena“) — siehe Spalte „Modellnamen“.')
    L.append('')
    L.append('| Serie | Artikel | Hauptkategorien | Preis von – bis |')
    L.append('|---|---|---|---|')
    ser = defaultdict(list)
    for p in prods:
        for s in p['series_all']:
            ser[s].append(p)
    for s in sorted(ser, key=lambda s: -len(ser[s])):
        ps = ser[s]
        pr = [min_price(p) for p in ps if min_price(p) is not None]
        cats = Counter(p['main_category'] for p in ps)
        L.append('| %s | %d | %s | %s – %s |' % (s, len(ps), ', '.join('%s (%d)' % kv for kv in cats.most_common()),
                                                 eur(min(pr)) if pr else '', eur(max(pr)) if pr else ''))
    L.append('')
    # model first names after "|"
    mn = defaultdict(list)
    for p in prods:
        if p['name'] and '|' in p['name'] and (p.get('brand') or '').startswith('Metzler'):
            m = p['name'].rsplit('|', 1)[1].strip()
            w = m.split()
            if 1 <= len(w) <= 3 and w[0][:1].isupper() and not re.search(r'\d|&|RAL|LED|Schwarz|Weiß|Weiss|Anthrazit|Edelstahl|Sensor|Türgriff|Zubehör|Solar|Bewegungsmelder|Smartphone|Dämmerung|App\b', m):
                mn[m].append(p)
    common = sorted(mn, key=lambda m: (-len(mn[m]), m))[:60]
    L.append('**Häufigste Metzler-Modellnamen (Text nach dem letzten „|“, ohne Farb-/Ausstattungszusätze; Anzahl Elternartikel):** ' +
             ', '.join('%s (%d)' % (m, len(mn[m])) for m in common))
    L.append('')

    # top rated
    L.append('## Bestbewertete Artikel')
    L.append('')
    L.append('Sortiert nach Anzahl Bewertungen, nur Durchschnitt ≥ 4,5 (Shop-Bewertungen aus JSON-LD `aggregateRating`).')
    L.append('')
    L.append('| Name | Kategorie | Bewertung | Anzahl | Preis ab |')
    L.append('|---|---|---|---|---|')
    rated = [p for p in prods if p['rating'] and p['rating']['value'] >= 4.5]
    for p in sorted(rated, key=lambda p: (-p['rating']['count'], -p['rating']['value']))[:20]:
        L.append('| [%s](%s) | %s | %s | %d | %s |' % (cell(p['name']), p['url'], cell(p['main_category']),
                                                   num(p['rating']['value']), p['rating']['count'], cell(preis_ab(p))))
    nr = sum(1 for p in prods if p['rating'])
    L.append('')
    L.append('%d von %d Elternartikeln haben Bewertungen.' % (nr, len(prods)))
    L.append('')

    # colours
    L.append('## Farben (Werte der Variationsgruppe „Farbe“, Anzahl Elternartikel)')
    L.append('')
    cc = Counter(c for p in prods for c in p['colours'])
    L.append(', '.join('%s (%d)' % kv for kv in cc.most_common()))
    L.append('')

    # data completeness
    L.append('## Datenlage')
    L.append('')
    def cnt(f):
        return sum(1 for p in prods if f(p))
    L.append('| Feld | vorhanden bei |')
    L.append('|---|---|')
    for lab, f in [('Preis', lambda p: p['price'] is not None), ('Art.-Nr. (mpn)', lambda p: p['artikelnummer']),
                   ('Maße B×H×T', lambda p: p['dimensions'] and p['dimensions']['b'] is not None),
                   ('Gewicht', lambda p: p['weight_text']), ('Kurzbeschreibung', lambda p: p['short_description']),
                   ('Merkmale', lambda p: p['merkmale']), ('Bilder', lambda p: p['images']),
                   ('Bewertung', lambda p: p['rating']), ('Farbauswahl (Gruppe „Farbe“)', lambda p: p['colours']), ('Kindartikel / Varianten', lambda p: p['variants'])]:
        L.append('| %s | %d / %d |' % (lab, cnt(f), len(prods)))
    L.append('')
    L.append('## Kategorie-Dateien')
    L.append('')
    for cat in order:
        L.append('- [%s](products/%s) — %d Artikel' % (cat, files[cat], len(by_cat[cat])))
    L.append('')
    if unc:
        L.append('- [Artikel ohne Kategorie / Konfigurator-Bausteine](products/konfigurator-bausteine.md) — %d Artikel '
                 '(nicht in den Zählungen oben)' % len(unc))
        L.append('')
    open(os.path.join(KN, 'products.md'), 'w', encoding='utf-8').write('\n'.join(L))
    print('products.md written')


if __name__ == '__main__':
    main()
