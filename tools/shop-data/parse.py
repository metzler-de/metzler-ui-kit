#!/usr/bin/env python3
"""Step 2: parse cached pages -> knowledge/products.json (one entry per PARENT product).

    python3 parse.py

Reads only the cache written by crawl.py (no network). Never invents values:
anything not found on the page stays null / empty.
"""
import datetime, html, json, os, re, sys
from shoplib import BASE, CACHE, fetch, is_cached

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', '..', 'knowledge', 'products.json'))

# Series / model families, matched against the product name (word boundary, case-insensitive).
# Ordered: first match wins for "series"; all matches go to "series_all".
SERIES = ['XDM10 Pro', 'XDM10', 'VDM10', 'SDM10', 'ADM10', 'TDM10', 'BK212', 'SK212', 'Siebert']


def txt(s):
    s = re.sub(r'<br\s*/?>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def de_num(s):
    """'1.299,00' -> 1299.0 ; returns None if not a number."""
    s = (s or '').strip().replace(' ', ' ')
    m = re.search(r'-?\d[\d.]*(?:,\d+)?', s)
    if not m:
        return None
    return float(m.group(0).replace('.', '').replace(',', '.'))


def json_ld_blocks(t):
    out = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', t, flags=re.S):
        raw = m.group(1)
        try:
            out.append(json.loads(raw))
        except Exception:
            try:  # tolerate raw control chars inside strings
                out.append(json.loads(re.sub(r'[\x00-\x1f]', ' ', raw)))
            except Exception:
                pass
    return out


def parse_page(t):
    """Extract everything we need from one product page. Returns None for non-product pages."""
    t = re.sub(r'\s+', ' ', t)
    lds = json_ld_blocks(t)
    prod = next((b for b in lds if isinstance(b, dict) and b.get('@type') == 'Product'), None)
    if not prod:
        return None
    crumbs = next((b for b in lds if isinstance(b, dict) and b.get('@type') == 'BreadcrumbList'), None)
    d = {}
    g = lambda pat, grp=1: (lambda m: m.group(grp) if m else None)(re.search(pat, t))
    d['item_id'] = g(r"'item_id':\s*'(\d+)'")
    d['current'] = g(r'id="AktuellerkArtikel"[^>]*value="(\d+)"')
    d['canonical'] = g(r'<link rel="canonical" href="([^"]+)"')
    h1 = g(r'<h1[^>]*>(.*?)</h1>')
    d['h1'] = txt(h1) if h1 else None
    d['ld_name'] = html.unescape(prod.get('name') or '') or None
    d['sku'] = prod.get('sku')
    d['mpn'] = prod.get('mpn')
    d['gtin13'] = prod.get('gtin13')
    br = prod.get('brand')
    d['brand'] = (br.get('name') if isinstance(br, dict) else br) or None
    off = prod.get('offers') or {}
    if isinstance(off, list):
        off = off[0] if off else {}
    d['price'] = float(off['price']) if off.get('price') not in (None, '') else None
    d['availability'] = (off.get('availability') or '').rsplit('/', 1)[-1] or None
    imgs = prod.get('image') or []
    d['images'] = [imgs] if isinstance(imgs, str) else list(imgs)
    ar = prod.get('aggregateRating')
    d['rating'] = ({'value': float(ar['ratingValue']), 'count': int(ar.get('reviewCount') or ar.get('ratingCount') or 0)}
                   if ar and ar.get('ratingValue') else None)
    # visible price block (first price_wrapper on the page = main buy box; later ones are cross-sells)
    d['price_text'] = d['price_old_text'] = d['price_label'] = d['price_note'] = None
    pw = re.search(r'<div class="price_wrapper[^"]*">(.*?)<div class="delivery-status', t)
    if pw:
        blk = pw.group(1)
        mpo = re.search(r'<span class="mpo-price__label">(.*?)</span>\s*<strong class="mpo-price__value[^"]*">(.*?)</strong>\s*(?:<span class="mpo-price__note">(.*?)</span>\s*</div>)?', blk)
        if mpo:  # UVP display (sold via Fachpartner), e.g. XDM10 Pro
            d['price_label'] = txt(mpo.group(1))
            d['price_text'] = txt(mpo.group(2))
            d['price_note'] = txt(mpo.group(3)) if mpo.group(3) else None
        else:
            lab = re.search(r'<span class="price_label[^"]*">(.*?)</span>', blk)
            pr = re.search(r'<strong class="price[^"]*">(.*?)(?:<small class="s-del">|</strong>)', blk)
            old = re.search(r'<del class="value">(.*?)</del>', blk)
            d['price_label'] = txt(lab.group(1)) if lab else None
            d['price_text'] = ' '.join(x for x in [d['price_label'] or '', txt(pr.group(1)) if pr else ''] if x) or None
            d['price_old_text'] = txt(old.group(1)) if old and txt(old.group(1)) else None
    # graduated prices (Staffelpreise)
    d['bulk_prices'] = []
    bp = re.search(r'<div class="bulk-price">(.*?)</table>', t)
    if bp:
        for q, pt in re.findall(r'<tr class="bulk-price-\d+"><td[^>]*>(.*?)</td><td[^>]*>(.*?)</td>', bp.group(1)):
            d['bulk_prices'].append({'min_qty': int(de_num(txt(q))), 'price_text': txt(pt), 'price': de_num(txt(pt))})
    # spec block (dt/dd): "Artikelnummer" as printed, dimensions with their axis label
    specs = {txt(a): txt(b) for a, b in re.findall(
        r'<dt class="pdp-specs__label">(.*?)</dt>\s*<dd class="pdp-specs__value">(.*?)</dd>', t)}
    d['artnr_display'] = specs.get('Artikelnummer') or None
    d['dimensions'] = None
    for lab, val in specs.items():
        axes = [a.strip() for a in lab.split('×')]
        if not axes or not set(axes) <= {'Breite', 'Höhe', 'Tiefe'}:
            continue
        val = val.strip()
        if not val or val in ('—', '-'):
            continue
        m = re.match(r'^([\d.,]+(?: × [\d.,]+)*) (\w+)$', val)
        dd = {'b': None, 'h': None, 't': None, 'unit': None, 'label': lab, 'text': val}
        if m:
            nums = [de_num(x) for x in m.group(1).split(' × ')]
            if len(nums) == len(axes):
                for a, n in zip(axes, nums):
                    dd[{'Breite': 'b', 'Höhe': 'h', 'Tiefe': 't'}[a]] = n
                dd['unit'] = m.group(2)
        d['dimensions'] = dd
        break
    # Merkmale + weight (first ul.product-attributes inside the description tab)
    d['merkmale'] = {}
    d['weight_text'] = d['shipping_weight_text'] = None
    m = re.search(r'<ul class="product-attributes[^"]*">(.*?)</ul>', t)
    if m:
        for li in re.findall(r'<li[^>]*>(.*?)</li>', m.group(1)):
            lab = re.search(r'<strong[^>]*>(.*?)</strong>', li)
            if not lab:
                continue
            name = txt(lab.group(1)).rstrip(':').strip()
            vals = [txt(x) for x in re.findall(r'class="tag"[^>]*>(.*?)</(?:a|span)>', li)]
            vals = [v for v in vals if v]
            if name.startswith('Abmessungen'):
                continue
            if name == 'Gewicht':
                d['weight_text'] = vals[0] if vals else None
                continue
            if name == 'Versandgewicht':
                d['shipping_weight_text'] = vals[0] if vals else None
                continue
            d['merkmale'][name] = vals
    # short description
    sd = re.search(r'<div class="shortdesc[^"]*">(.*?)</div>', t)
    d['short_description'] = None
    if sd:
        lis = [txt(re.sub(r'</(b|strong)>(?=\s*[^\s<])', r'</\1> – ', x)) for x in re.findall(r'<li[^>]*>(.*?)</li>', sd.group(1))]
        lis = [x for x in lis if x]
        d['short_description'] = '\n'.join('- ' + x for x in lis) if lis else (txt(sd.group(1)) or None)
    # breadcrumbs (JSON-LD), without "Startseite" and without the product itself
    d['breadcrumb'] = []
    if crumbs:
        items = sorted(crumbs.get('itemListElement') or [], key=lambda x: x.get('position', 0))
        names = [(html.unescape(i.get('name') or ''), i.get('item')) for i in items]
        d['breadcrumb'] = [{'name': n, 'url': u} for n, u in names[1:-1]]
    # child-article variations (swatches / options with data-ref) + free variations
    d['swatches'] = []
    d['options'] = []
    for dl in re.finditer(r'<dl class="var-it[^"]*" id="([^"]*)">(.*?)</dl>', t):
        gid, body = dl.group(1), dl.group(2)
        head = re.search(r'<dt class="var-head[^"]*">(.*?)</dt>', body)
        gname = re.search(r'<span class="color-selected-value">(.*?)</span>', head.group(1)) if head else None
        gname = txt(gname.group(1)) if gname else (txt(head.group(1)) if head else gid)
        gname = re.sub(r'^Bitte (.*) wählen:?$', r'\1', gname).rstrip(':').strip()
        if not gname:
            h4 = re.search(r'<span class="h4">Bitte (.*?) wählen:?</span>', body)
            gname = txt(h4.group(1)) if h4 else gid
        entries = []
        for lm in re.finditer(r'<label[^>]*class="variation[^"]*"[^>]*>|<option[^>]*class="variation"[^>]*>', body):
            tag = lm.group(0)
            ga = lambda a: (lambda mm: html.unescape(mm.group(1)) if mm else None)(re.search(r'\b' + a + r'="([^"]*)"', tag))
            entries.append({'name': ga('data-original'), 'ref': ga('data-ref'), 'value': ga('data-value'),
                            'type': ga('data-type'), 'pos': lm.end()})
        # surcharge: label swatches -> .variation-extra-price .tag following the label; options -> text in option
        for i, e in enumerate(entries):
            end = entries[i + 1]['pos'] if i + 1 < len(entries) else len(body)
            seg = body[e['pos']:end]
            sm = re.search(r'<div class="variation-extra-price[^>]*>(.*?)</div>', seg)
            sur = re.search(r'class="tag"[^>]*>(.*?)</span>', sm.group(1)) if sm else None
            e['surcharge_text'] = txt(sur.group(1)) if sur else None
            if e['type'] == 'option' and not e['surcharge_text']:
                om = re.search(r'^(.*?)</option>', seg)
                ot = txt(om.group(1)) if om else ''
                pm = re.search(r'([+-] ?[\d.,]+ ?€)', ot)
                e['surcharge_text'] = pm.group(1) if pm else None
        if any(e['ref'] for e in entries):
            for e in entries:
                d['swatches'].append({'group': gname, 'name': e['name'], 'ref': e['ref'],
                                      'surcharge_text': e['surcharge_text'], 'type': e['type']})
        elif entries:
            d['options'].append({'group': gname, 'type': entries[0]['type'],
                                 'values': [{'name': e['name'], 'surcharge_text': e['surcharge_text']} for e in entries]})
        elif re.search(r'<input type="text"[^>]*name="eigenschaftwert', body):
            d['options'].append({'group': gname, 'type': 'text', 'values': []})
    # Entwurf vor Fertigung (configurator option)
    ev = re.search(r'Entwurf vor Fertigung(?:(?!Entwurf vor Fertigung).){0,600}?([+-] ?[\d.,]+ ?€)', txt_keep(t))
    d['entwurf'] = None
    if 'Entwurf vor Fertigung' in t:
        d['entwurf'] = {'offered': True, 'price_text': ev.group(1) if ev else None,
                        'price': de_num(ev.group(1)) if ev else None}
    d['has_3d'] = 'mpc3d_cunique_ek_' in t
    return d


def txt_keep(t):
    """Text of the page with scripts removed (used for the configurator option scan)."""
    t = re.sub(r'<script\b.*?</script>', ' ', t, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))


def series_of(name):
    found = []
    for s in SERIES:
        if re.search(r'(?<![A-Za-z0-9])' + re.escape(s) + r'(?![A-Za-z0-9])', name or '', flags=re.I):
            if not any(s in f for f in found):
                found.append(s)
    return found


def main():
    urls = json.load(open(os.path.join(CACHE, 'urls.json')))
    pages = {}       # item_id -> parsed page (+ url)
    non_product = 0
    for u in urls:
        if not is_cached(u):
            continue
        status, final, t = fetch(u)
        if status != 200:
            continue
        d = parse_page(t)
        if not d:
            non_product += 1
            continue
        d['url'] = final
        iid = d['item_id']
        # prefer the canonical/pretty URL over /?a=<id>
        if iid in pages and '/?a=' in u:
            continue
        pages[iid] = d
    parents = {k: v for k, v in pages.items() if v['current'] == k}
    children = {k: v for k, v in pages.items() if v['current'] != k}
    print('product pages: %d (parents %d, child pages %d), non-product pages: %d'
          % (len(pages), len(parents), len(children), non_product))
    missing_parents = sorted({c['current'] for c in children.values()} - set(parents))
    if missing_parents:
        print('WARNING parents referenced by children but not cached:', missing_parents[:20])

    kids_by_parent = {}
    for k, c in children.items():
        kids_by_parent.setdefault(c['current'], []).append(k)

    products = []
    problems = []
    for pid, p in parents.items():
        name = p['h1'] or p['ld_name']
        crumbs = [c['name'] for c in p['breadcrumb']]
        # variation groups as shown on the parent page (child-article variations only)
        groups = []
        for sw in p['swatches']:
            gr = next((g for g in groups if g['group'] == sw['group']), None)
            if not gr:
                gr = {'group': sw['group'], 'values': []}
                groups.append(gr)
            gr['values'].append({'name': sw['name'], 'surcharge_text': sw['surcharge_text'],
                                 'surcharge': de_num(sw['surcharge_text']) if sw['surcharge_text'] else None,
                                 'kArtikel_example': int(sw['ref']) if sw['ref'] else None})
        surch = {(sw['group'], sw['name']): sw['surcharge_text'] for sw in p['swatches']}
        # all child articles: child pages pointing at this parent + every swatch ref
        child_ids = list(dict.fromkeys([sw['ref'] for sw in p['swatches'] if sw['ref']] + sorted(kids_by_parent.get(pid, []), key=int)))
        variants = []
        for r in child_ids:
            c = pages.get(r)
            if not c:
                problems.append('%s: child %s referenced by a swatch but not fetched' % (pid, r))
                attrs = {sw['group']: sw['name'] for sw in p['swatches'] if sw['ref'] == r}
                variants.append({'kArtikel': int(r), 'attributes': attrs, 'colour': attrs.get('Farbe'),
                                 'name': None, 'artikelnummer': None, 'artnr_display': None, 'gtin13': None,
                                 'price': None, 'price_text': None, 'surcharge_text': None, 'surcharge': None,
                                 'url': None, 'has_3d': None})
                continue
            # the child's own selection = entries on its page whose data-ref is the child itself
            attrs = {sw['group']: sw['name'] for sw in c['swatches'] if sw['ref'] == r}
            if not attrs:
                attrs = {sw['group']: sw['name'] for sw in p['swatches'] if sw['ref'] == r}
            sts = [surch.get((g, v)) for g, v in attrs.items() if surch.get((g, v))]
            variants.append({
                'kArtikel': int(r),
                'attributes': attrs,
                'colour': attrs.get('Farbe'),
                'name': c['h1'] or c['ld_name'],
                'artikelnummer': c['mpn'],
                'artnr_display': c['artnr_display'],
                'gtin13': c['gtin13'],
                'price': c['price'],
                'price_text': c['price_text'],
                'surcharge_text': ' / '.join(sts) if sts else None,
                'surcharge': sum(de_num(x) for x in sts) if sts else None,
                'url': c['url'],
                'has_3d': c['has_3d'],
            })
        if p['swatches'] and not kids_by_parent.get(pid):
            problems.append('%s: has variations but no child pages found' % pid)
        # 3D / Entwurf: true if the parent or any child page carries it
        fam = [p] + [pages[r] for r in child_ids if r in pages]
        has3d = any(x['has_3d'] for x in fam)
        ent = next((x['entwurf'] for x in fam if x['entwurf']), None)
        dims = p['dimensions'] or next((pages[r]['dimensions'] for r in child_ids if r in pages and pages[r]['dimensions']), None)
        dims_src = 'parent' if p['dimensions'] else ('child' if dims else None)
        wt = p['weight_text'] or next((pages[r]['weight_text'] for r in child_ids if r in pages and pages[r]['weight_text']), None)
        ser = series_of(name)
        products.append({
            'kArtikel': int(pid),
            'name': name,
            'url': p['canonical'] or p['url'],
            'artikelnummer': p['mpn'],
            'artnr_display': p['artnr_display'],
            'sku': p['sku'],
            'gtin13': p['gtin13'],
            'brand': p['brand'],
            'price': p['price'],
            'price_text': p['price_text'],
            'price_old_text': p['price_old_text'],
            'price_label': p['price_label'],
            'price_note': p['price_note'],
            'price_from': min([v['price'] for v in variants if v['price'] is not None] or [p['price']]) if variants else p['price'],
            'bulk_prices': p['bulk_prices'],
            'availability': p['availability'],
            'category_path': crumbs,
            'main_category': crumbs[0] if crumbs else None,
            'series': ser[0] if ser else None,
            'series_all': ser,
            'short_description': p['short_description'],
            'dimensions': dims,
            'dimensions_source': dims_src,
            'weight_text': wt,
            'weight_kg': de_num(wt) if wt and wt.endswith('kg') else None,
            'shipping_weight_text': p['shipping_weight_text'],
            'merkmale': p['merkmale'],
            'rating': p['rating'],
            'images': p['images'],
            'has_3d': has3d,
            'entwurf_vor_fertigung': ent or {'offered': False, 'price_text': None, 'price': None},
            'variation_groups': groups,
            'colours': next(([v['name'] for v in g['values']] for g in groups if g['group'] == 'Farbe'), []),
            'variants': variants,
            'options': p['options'],
        })
    products.sort(key=lambda x: ((x['main_category'] or '~'), '/'.join(x['category_path']), x['name'] or ''))
    # parents without any shop category = configurator building blocks (fonts, Ausrichtung, Taster, Duebel ...)
    uncategorized = [{k: p[k] for k in ('kArtikel', 'name', 'url', 'artikelnummer', 'price', 'price_text')}
                     for p in products if not p['category_path']]
    products = [p for p in products if p['category_path']]
    out = {'generated': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
           'source': BASE,
           'count': len(products),
           'notes': {
               'price': 'EUR gross incl. 19% MwSt., JSON-LD offers.price of the parent page. For parents with child articles this is the parent record price and can differ from what a customer pays: use price_from (= lowest child price, else price).',
               'price_text': 'Buy-box text exactly as shown (price_label "ab" / "Unverbindliche Preisempfehlung (UVP)" included). "ab" can also mean the lowest Staffelpreis (bulk_prices). price_note e.g. "verbindliches Angebot ueber Ihren Fachpartner". price_old_text = struck-through price.',
               'artikelnummer': 'JSON-LD mpn of the page. artnr_display = the "Artikelnummer:" line printed on the page (only shown on child/simple articles).',
               'dimensions': 'Breite x Hoehe x Tiefe as printed on the page (cm). dimensions_source=child means the parent page shows none and the first colour child was used.',
               'variation_groups': 'Child-article variation groups exactly as on the parent page (Farbe, Anzahl der Klingeltaster, ...), with the surcharge the shop prints next to a value. kArtikel_example = data-ref of that value on the parent page.',
               'colours': 'Values of the Farbe group on the parent page, in shop order and spelling.',
               'variants': 'Every child article (from sitemap child pages whose AktuellerkArtikel = parent, plus swatch data-refs). attributes = the child page\'s own selection; price/artikelnummer/url from the child page; surcharge = sum of the parent-page surcharges of the child\'s values, only where the shop prints one.',
               'options': 'Non-article variations (dropdown/text fields) that do not create a child article.',
               'uncategorized': 'Articles with a product page but no shop category (breadcrumb only "Startseite"). Almost all are configurator building blocks (Schriftart, Ausrichtung, Taster, Duebel, Groessen ...) that are sold only as options of other products. Not counted in count/products.',
               'has_3d': 'Page source of the parent or a child contains mpc3d_cunique_ek_ (3D live configurator).',
           },
           'products': products,
           'uncategorized_count': len(uncategorized),
           'uncategorized': uncategorized}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(problems, open(os.path.join(CACHE, 'parse_problems.json'), 'w'), ensure_ascii=False, indent=1)
    print('wrote %s: %d parents, %d variants; %d problems (cache/parse_problems.json)'
          % (OUT, len(products), sum(len(p['variants']) for p in products), len(problems)))


if __name__ == '__main__':
    main()
