#!/usr/bin/env python3
"""Step 4: spot-check N random parents of knowledge/products.json against the LIVE shop (no cache).

    python3 verify.py            # 10 random products
    python3 verify.py 25 1234    # 25 products, random seed 1234

Compares price, Art.-Nr. (mpn), name and the colour list of the parent page, plus price and
Art.-Nr. of one random colour variant per product. Prints a table and writes cache/verify_last.json.
"""
import json, os, random, sys
from shoplib import BASE, CACHE, http_get, strip_chrome
from parse import parse_page, OUT


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else random.randrange(10 ** 6)
    rnd = random.Random(seed)
    data = json.load(open(OUT, encoding='utf-8'))
    sample = rnd.sample(data['products'], n)
    rows, ok_all = [], True
    for p in sample:
        live = parse_page(strip_chrome(http_get(p['url'])[2]))
        r = {'kArtikel': p['kArtikel'], 'name': p['name'], 'url': p['url'], 'checks': {}}
        if not live:
            r['checks']['page'] = 'NOT A PRODUCT PAGE LIVE'
            ok_all = False
            rows.append(r)
            continue
        c = r['checks']
        c['name'] = (p['name'] == (live['h1'] or live['ld_name']), p['name'], live['h1'])
        c['price'] = (p['price'] == live['price'], p['price'], live['price'])
        c['artikelnummer'] = (p['artikelnummer'] == live['mpn'], p['artikelnummer'], live['mpn'])
        kc = [v['colour'] for v in p['variants']]
        lc = [s['name'] for s in live['swatches']]
        c['colours'] = (kc == lc, kc, lc)
        if p['variants']:
            v = rnd.choice(p['variants'])
            if v['url']:
                lv = parse_page(strip_chrome(http_get(v['url'])[2]))
                c['variant %s price' % v['kArtikel']] = (lv is not None and v['price'] == lv['price'], v['price'], lv and lv['price'])
                c['variant %s Art.-Nr.' % v['kArtikel']] = (lv is not None and v['artikelnummer'] == lv['mpn'], v['artikelnummer'], lv and lv['mpn'])
        r['ok'] = all(x[0] for x in c.values())
        ok_all &= r['ok']
        rows.append(r)
        print('%s  %-8s %s' % ('OK  ' if r['ok'] else 'DIFF', p['kArtikel'], p['name']))
        for k, (good, a, b) in c.items():
            if not good:
                print('      %s: knowledge=%r live=%r' % (k, a, b))
            else:
                print('      %s: %s' % (k, a if not isinstance(a, list) else '%d colours' % len(a)))
    json.dump({'seed': seed, 'all_ok': ok_all, 'rows': rows}, open(os.path.join(CACHE, 'verify_last.json'), 'w'),
              ensure_ascii=False, indent=1)
    print('seed=%d  result: %d/%d products match' % (seed, sum(1 for r in rows if r.get('ok')), len(rows)))


if __name__ == '__main__':
    main()
