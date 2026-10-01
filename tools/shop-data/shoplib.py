"""Shared fetch + cache helpers for the edelstahl-tuerklingel.de product crawler.

Only public GET requests. Polite: max 4 workers, small delay per request,
retries with exponential backoff. Pages are cached gzip-compressed under
cache/pages/ (the inline <style> blocks and the <header> mega-menu are
stripped before caching: they are identical site chrome and ~50 % of each page).
"""
import gzip, hashlib, json, os, random, re, time, urllib.request, urllib.error

BASE = 'https://edelstahl-tuerklingel.de'
UA = 'Mozilla/5.0'
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
PAGES = os.path.join(CACHE, 'pages')
DELAY = 0.35          # seconds slept by each worker before every network request
RETRIES = 4
os.makedirs(PAGES, exist_ok=True)


def _key(url):
    return hashlib.md5(url.encode()).hexdigest()


def cache_path(url):
    return os.path.join(PAGES, _key(url) + '.html.gz')


def strip_chrome(html):
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.S)
    html = re.sub(r'<header\b.*?</header>', '<header></header>', html, flags=re.S)
    return html


def http_get(url, binary=False):
    """GET with retries/backoff. Returns (status, final_url, body)."""
    last = None
    for attempt in range(RETRIES + 1):
        time.sleep(DELAY + random.random() * 0.15)
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip',
                                                   'Accept-Language': 'de-DE,de;q=0.9'})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    data = gzip.decompress(data)
                if binary:
                    return r.status, r.geturl(), data
                return r.status, r.geturl(), data.decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return e.code, url, ''
            last = e
        except Exception as e:  # timeouts, resets
            last = e
        time.sleep(2 ** attempt + random.random())
    raise RuntimeError('GET failed %s: %s' % (url, last))


def fetch(url, refresh=False):
    """Return (status, final_url, html) using the cache when possible."""
    fn = cache_path(url)
    meta_fn = fn[:-8] + '.json'
    if not refresh and os.path.exists(fn) and os.path.exists(meta_fn):
        meta = json.load(open(meta_fn))
        with gzip.open(fn, 'rt', encoding='utf-8') as f:
            return meta['status'], meta['final_url'], f.read()
    status, final, html = http_get(url)
    html = strip_chrome(html)
    with gzip.open(fn + '.tmp', 'wt', encoding='utf-8') as f:
        f.write(html)
    os.replace(fn + '.tmp', fn)
    json.dump({'url': url, 'status': status, 'final_url': final,
               'fetched': time.strftime('%Y-%m-%dT%H:%M:%S')}, open(meta_fn, 'w'))
    return status, final, html


def is_cached(url):
    fn = cache_path(url)
    return os.path.exists(fn) and os.path.exists(fn[:-8] + '.json')


def sitemap_urls(refresh=False):
    """All <loc> URLs from every sitemap listed in the sitemap index."""
    idx_fn = os.path.join(CACHE, 'sitemap_index.xml')
    if refresh or not os.path.exists(idx_fn):
        open(idx_fn, 'w').write(http_get(BASE + '/export/sitemap_index.xml')[2])
    idx = open(idx_fn).read()
    out = []
    for i, sm in enumerate(re.findall(r'<loc>([^<]+)</loc>', idx)):
        fn = os.path.join(CACHE, 'sitemap_%d.xml' % i)
        if refresh or not os.path.exists(fn):
            data = http_get(sm, binary=True)[2]
            if sm.endswith('.gz'):
                data = gzip.decompress(data)
            open(fn, 'wb').write(data)
        xml = open(fn, encoding='utf-8').read()
        for block in re.findall(r'<url>(.*?)</url>', xml, flags=re.S):
            loc = re.search(r'<loc>([^<]+)</loc>', block).group(1).strip()
            out.append({'url': loc, 'has_image': 'image:image' in block})
    return out
