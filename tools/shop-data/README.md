# shop-data — product knowledge base from edelstahl-tuerklingel.de

Scrapes the public Metzler shop and writes the product knowledge that Claude reads in design/page tasks:

| Output | What |
|---|---|
| `knowledge/products.json` | one entry per **parent** product (all fields, all child articles) |
| `knowledge/products.md` | German overview: counts, price ranges, series, top-rated, 3D coverage, links |
| `knowledge/products/<kategorie>.md` | one compact table per main category (< 150 KB each) |
| `knowledge/products/konfigurator-bausteine.md` | articles with a page but no category (configurator options) |

Only public GET requests. No login, no cart, no forms.

## Re-run

```bash
cd "tools/shop-data"
python3 crawl.py            # fetch missing pages into cache/   (first run ~20 min, 4 workers)
python3 parse.py            # cache -> knowledge/products.json  (offline, ~1 min)
python3 render.py           # products.json -> markdown          (offline, seconds)
python3 verify.py 10        # spot-check 10 random products against the LIVE shop
python3 coverage.py         # optional: every article on every category listing is in products.json?
```

To pick up price/assortment changes, refresh the cache first: `python3 crawl.py --refresh`
(re-downloads sitemap + every page), or simply delete `cache/` and run `crawl.py`.
Python 3.9+, standard library only.

## How it works

- **URLs**: `/export/sitemap_index.xml` → `sitemap_0.xml.gz` (only one sitemap as of Oct 2026; the
  index is read, so more files are picked up automatically). The sitemap lists parents **and** child
  articles, plus Merkmal-value pages, category and CMS pages. Every URL is fetched; a page counts as a
  product when it has JSON-LD `"@type": "Product"`.
- **Follow-ups** (pass 2+): parent canonical URLs and swatch/option `data-ref` children that are not in
  the sitemap are fetched as `/?a=<kArtikel>`.
- **Parent vs child**: on every product page `'item_id'` = this article, `#AktuellerkArtikel` = parent.
  Equal → parent; different → child of that parent.
- **Politeness**: 4 workers max, 0.35–0.5 s sleep before each request, 4 retries with exponential
  backoff. Cache: `cache/pages/<md5(url)>.html.gz` + `.json` meta (status, final URL, fetch time).
  Inline `<style>` blocks and the `<header>` mega-menu are stripped before caching (identical chrome,
  about half of each 1.7 MB page). `cache/` is git-ignored (~350 MB).

## Field sources (never guessed — missing stays `null`/empty)

| Field | Source |
|---|---|
| `name` | `<h1>` of the parent page (= JSON-LD name) |
| `artikelnummer` | JSON-LD `mpn`. `artnr_display` = the "Artikelnummer" row of the page's spec box — on this shop it is **always the kArtikel**, not the mpn |
| `price` / `price_text` | JSON-LD `offers.price` (gross, incl. 19 % MwSt.) / visible buy-box text incl. "ab" (`price_label`). `price_from` = cheapest child article (else `price`) — use it for "ab" prices, because a parent's own JSON-LD price can be lower than any buyable child. `bulk_prices` = Staffelpreise table (an "ab" in the buy box can mean the lowest Staffelpreis). UVP display (XDM10 PRO, "verbindliches Angebot über Ihren Fachpartner") goes to `price_label`/`price_note`. `price_old_text` = struck-through price. **Never** the listing-card microdata (×1000 bug; the `itemprop=price` meta in the buy box has it too) |
| `category_path`, `main_category` | JSON-LD BreadcrumbList without "Startseite" and the product |
| `series` | regex on the name, list `SERIES` in `parse.py` (extend when new families appear) |
| `short_description` | `div.shortdesc` (bullets joined as `- …` lines). The long description is skipped (generic VDM10 block on every page) |
| `dimensions` | spec box `dt.pdp-specs__label` "Breite × Höhe × Tiefe" (or "Breite × Höhe", "Höhe", "Höhe × Tiefe") — B × H × T in cm. `label` tells which axes exist. Parent first, else first child |
| `weight_text`, `shipping_weight_text` | "Gewicht" / "Versandgewicht" rows in `ul.product-attributes` |
| `merkmale` | first `ul.product-attributes`: `<strong>Name:</strong>` + `.tag` values (Material is not shown there) |
| `rating` | JSON-LD `aggregateRating` |
| `images` | JSON-LD Product `image` (lg) |
| `has_3d` | page source of parent or any child contains `mpc3d_cunique_ek_` |
| `entwurf_vor_fertigung` | configurator option "Entwurf vor Fertigung" with its `+x,xx €` (usually only on child pages) |
| `variation_groups`, `colours` | `dl.var-it` groups on the parent page with `label.variation`/`option.variation` (`data-original`, `data-ref`, surcharge `.tag`) |
| `variants` | every child article: sitemap child pages pointing at the parent + all `data-ref`s. `attributes` = the child's own selection (entries on its page whose `data-ref` = itself) |
| `options` | variations that do not create child articles (free text fields, dropdowns) |

Known shop quirks (Oct 2026): the visible buy-box price of XDM10 PRO 5/6 Klingeltaster (UVP 1.499 / 1.549 €)
differs from their JSON-LD price (1.599 / 1.649 €) — both are kept. Some parents' JSON-LD price is below all
their children (e.g. Deckenleuchte Aludra 64,99 € vs. 109,00 € per colour) — see `price_from`.
A product has exactly one breadcrumb, so `main_category` is its primary category even if it is also listed elsewhere.

Parse problems (e.g. a referenced child that could not be fetched) are written to
`cache/parse_problems.json`; the last verification run to `cache/verify_last.json`.

## Files

- `shoplib.py` — fetch with cache/retry/backoff, sitemap reader
- `crawl.py` — step 1, fills the cache
- `parse.py` — step 2, page parser + aggregation into products.json
- `render.py` — step 3, markdown
- `verify.py` — step 4, live spot check (bypasses the cache; uses the same parser, so it catches stale data, not parser bugs)
- `coverage.py` — optional completeness check against all category listings
