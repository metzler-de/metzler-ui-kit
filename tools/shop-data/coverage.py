#!/usr/bin/env python3
"""Optional completeness check: are all articles listed on the shop's category pages in products.json?

    python3 coverage.py

Collects every category URL seen in breadcrumbs, walks each listing (pages _s2, _s3 ...), reads the
kArtikel of every listed card (result-wrapper_buy_form_<id>) and compares with products.json
(parents, children and uncategorized). Listing pages are cached like product pages.
Writes cache/coverage_last.json.
"""
import json, os, re
from concurrent.futures import ThreadPoolExecutor
from shoplib import CACHE, fetch
from parse import OUT, parse_page


def harvest(url):
    ids, n, pg = [], None, 1
    while pg <= 40:
        t = re.sub(r'\s+', ' ', fetch(url if pg == 1 else '%s_s%d' % (url, pg))[2])
        if n is None:
            m = re.search(r'(\d+) Artikel<', t)
            n = int(m.group(1)) if m else 0
        new = [x for x in dict.fromkeys(re.findall(r'result-wrapper_buy_form_(\d+)', t)) if x not in ids]
        if not new:
            break
        ids += new
        if len(ids) >= n:
            break
        pg += 1
    return url, n, ids


def main():
    d = json.load(open(OUT, encoding='utf-8'))
    known = {}
    for p in d['products']:
        known[str(p['kArtikel'])] = 'parent'
        for v in p['variants']:
            known[str(v['kArtikel'])] = 'child'
    for p in d.get('uncategorized', []):
        known[str(p['kArtikel'])] = 'uncategorized'
    cats = set()
    for p in d['products']:
        pg = parse_page(fetch(p['url'])[2])
        for c in pg['breadcrumb']:
            if c['url']:
                cats.add(c['url'])
    with ThreadPoolExecutor(4) as ex:
        res = list(ex.map(harvest, sorted(cats)))
    listed = {}
    for url, n, ids in res:
        for i in ids:
            listed.setdefault(i, url)
    missing = {i: u for i, u in listed.items() if i not in known}
    short = [(u, n, len(ids)) for u, n, ids in res if n and len(ids) < n]
    out = {'categories': len(cats), 'listed_articles': len(listed),
           'in_knowledge': len(listed) - len(missing), 'missing': missing,
           'listings_not_fully_read': short}
    json.dump(out, open(os.path.join(CACHE, 'coverage_last.json'), 'w'), indent=1)
    print('categories %d, distinct listed articles %d, missing from products.json %d, listings short %d'
          % (len(cats), len(listed), len(missing), len(short)))
    for i, u in list(missing.items())[:30]:
        print('  missing', i, u)
    for s in short[:20]:
        print('  short listing', s)


if __name__ == '__main__':
    main()
