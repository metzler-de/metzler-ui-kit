#!/usr/bin/env python3
"""Step 1: fetch every public page listed in the shop sitemap into cache/.

    python3 crawl.py            # use cache, fetch only what is missing
    python3 crawl.py --refresh  # re-download sitemap and every page

Pass 1 fetches every sitemap URL. Pass 2+ fetches pages that product pages
point to but that the sitemap does not list (parent canonical URLs and
colour-variant children referenced by swatch data-ref -> /?a=<kArtikel>).
"""
import json, os, re, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from shoplib import BASE, CACHE, fetch, is_cached, sitemap_urls

WORKERS = 4  # never raise above 4 (politeness)
REFRESH = '--refresh' in sys.argv


def run(urls, label):
    todo = [u for u in urls if REFRESH or not is_cached(u)]
    print('%s: %d urls, %d to fetch' % (label, len(urls), len(todo)), flush=True)
    done = 0
    errors = []
    t0 = time.time()
    with ThreadPoolExecutor(WORKERS) as ex:
        futs = {ex.submit(fetch, u, REFRESH): u for u in todo}
        for f in as_completed(futs):
            done += 1
            try:
                f.result()
            except Exception as e:
                errors.append((futs[f], str(e)))
            if done % 100 == 0:
                el = time.time() - t0
                print('  %d/%d  %.0fs  (eta %.0fs)' % (done, len(todo), el, el / done * (len(todo) - done)), flush=True)
    for u, e in errors:
        print('  ERROR', u, e)
    return errors


def follow_ups(urls):
    """Parent canonicals / swatch children referenced by cached product pages but not yet fetched."""
    extra = set()
    for u in urls:
        if not is_cached(u):
            continue
        status, final, t = fetch(u)
        if '"@type": "Product"' not in t:
            continue
        t = re.sub(r'\s+', ' ', t)
        m = re.search(r'<link rel="canonical" href="([^"]+)"', t)
        if m and not is_cached(m.group(1)):
            extra.add(m.group(1))
        for tag in re.findall(r'<(?:label|option)\b[^>]*class="variation[^"]*"[^>]*>', t):
            ref = re.search(r'data-ref="(\d+)"', tag)
            if ref:
                extra.add(BASE + '/?a=' + ref.group(1))
    return extra


def main():
    sm = sitemap_urls(refresh=REFRESH)
    urls = [x['url'] for x in sm]
    print('sitemap: %d urls' % len(urls))
    errs = run(urls, 'pass 1 (sitemap)')
    all_urls = list(urls)
    # map kArtikel -> url for pages we already have, so /?a=<id> is only fetched when truly missing
    have_ids = set()
    for u in all_urls:
        if is_cached(u):
            t = fetch(u)[2]
            m = re.search(r"'item_id':\s*'(\d+)'", t)
            if m:
                have_ids.add(m.group(1))
    for p in range(2, 5):
        extra = follow_ups(all_urls)
        extra = {u for u in extra if not (u.startswith(BASE + '/?a=') and u.split('=')[-1] in have_ids)}
        extra -= set(all_urls)
        if not extra:
            break
        errs += run(sorted(extra), 'pass %d (follow-ups)' % p)
        all_urls += sorted(extra)
        for u in extra:
            if is_cached(u):
                m = re.search(r"'item_id':\s*'(\d+)'", fetch(u)[2])
                if m:
                    have_ids.add(m.group(1))
    json.dump(all_urls, open(os.path.join(CACHE, 'urls.json'), 'w'), indent=0)
    print('done: %d urls cached, %d errors' % (len(all_urls), len(errs)))


if __name__ == '__main__':
    main()
