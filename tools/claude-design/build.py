#!/usr/bin/env python3
"""Build the Metzler Design System (Claude Design) from the local UI Kit.
Source of truth: ~/Documents/Claude/Projects/Metzler UI Kit. Output: ds/out/project/…"""
import json, os, re, shutil, sys, urllib.parse, datetime

KIT = os.path.expanduser('~/Documents/Claude/Projects/Metzler UI Kit')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
P = os.path.join(OUT, 'project')
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
warn = []

def rd(p): return open(os.path.join(KIT, p), encoding='utf-8').read()
def wr(rel, text):
    f = os.path.join(P, rel); os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, 'w', encoding='utf-8').write(text)

# ── asset map: kit path → /_blob/<id> ─────────────────────────────────────
staged = json.load(open(os.path.join(HERE, 'staged.json')))
BLOB = {}
for s in staged:
    BLOB[os.path.normpath(s['src'])] = '/_blob/' + s['blob']
ALIAS = {  # placeholder names used in the kit's doc examples → real kit files
    'product.jpg': 'Pictures/Metzler VDM10 2.0/1122.png',
    'innenstation.webp': 'Pictures/innenstation/metzler-intercom-innenstation-ultra-10-zoll-touchscreen-lan-poe-schwarz.webp',
    'photo.jpg': 'media/craft-xdm10.png',
    'sdm10x.webp': 'Pictures/Metzler VDM10 2.0/1123.png',
    'media/gravur.webp': 'media/ebenhard gravur.webp',
    'media/farben.png': 'media/ebenhard neue farben.png',
    'office.png': 'media/about-office.png',
    'paketbox.webp': 'media/craft-paketbox.webp',
    'logo.svg': 'header/logo.svg',
    'favicon.svg': 'favicon.svg',
}
PAGES = 'https://metzler-de.github.io/metzler-ui-kit/'

def resolve(ref, base=''):
    r = urllib.parse.unquote(ref.split('?')[0].split('#')[0])
    if r.startswith(PAGES): r = r[len(PAGES):]
    if r.startswith(('http:', 'https:', 'data:', '/_blob/', 'mailto:', 'tel:')) or r == '': return None
    cands = [os.path.normpath(os.path.join(base, r)), os.path.normpath(r)]
    for c in cands:
        if c in BLOB: return BLOB[c]
    for c in [r, os.path.basename(r)] + cands:
        if c in ALIAS and os.path.normpath(ALIAS[c]) in BLOB: return BLOB[os.path.normpath(ALIAS[c])]
    return None

IMG_EXT = r'(?:svg|png|jpe?g|webp|gif|mp4|webm)'
def rewrite(text, base='', ctx=''):
    def sub_attr(m):
        new = resolve(m.group(2), base)
        if new is None:
            if not m.group(2).startswith(('http', 'data:', '/_blob/')): warn.append(f'{ctx}: unresolved {m.group(2)}')
            return m.group(0)
        return f'{m.group(1)}{new}{m.group(3)}'
    text = re.sub(r'''((?:src|poster|href)=["'])([^"']+?\.''' + IMG_EXT + r''')(["'])''', sub_attr, text)
    def sub_url(m):
        new = resolve(m.group(2), base)
        return f'url({m.group(1)}{new}{m.group(1)})' if new else m.group(0)
    text = re.sub(r'''url\((["']?)([^"')]+?\.''' + IMG_EXT + r''')\1\)''', sub_url, text)
    # footer §14 uses absolute Pages URLs
    text = re.sub(re.escape(PAGES) + r'([^"\')\s]+)', lambda m: resolve(PAGES + m.group(1)) or m.group(0), text)
    return text

# ── tokens.json ───────────────────────────────────────────────────────────
tok_css = rd('metzler-tokens.css')
root_blocks = re.findall(r':root\s*\{(.*?)\n\}', tok_css, re.S)
decl = []  # (name, value, comment) in source order, first :root blocks only (not media)
for blk in root_blocks:
    for m in re.finditer(r'^\s*--([a-z0-9-]+)\s*:\s*([^;]+);[ \t]*(?:/\*\s*(.*?)\s*\*/)?', blk, re.M):
        decl.append((m.group(1), m.group(2).strip(), (m.group(3) or '').strip()))
seen = set(); D = []
for n, v, c in decl:
    if n in seen: continue
    seen.add(n); D.append((n, v, c))
byname = {n: (v, c) for n, v, c in D}

def usage(n, c, default=''):
    c = re.sub(r'^\d+px\s*[—-]\s*', '', c).strip(' —-')
    return c or default

color = []
SEM_USAGE = {
    'btn-primary-bg': 'Primary button fill.', 'btn-primary-bg-hover': 'Primary button hover fill.',
    'btn-primary-color': 'Text on the primary button.', 'text-heading-color': 'Headings, product names, prices on white or paper.',
    'text-body-color': 'Body paragraphs on white or paper.', 'text-muted-color': 'Captions and metadata on white or paper.',
    'text-placeholder': 'Placeholders and disabled labels.', 'text-link': 'Links on white or paper.',
    'surface-page': 'Page background.', 'surface-card': 'Cards and panels.', 'surface-input-border': 'Default input border.',
    'surface-input-focus': 'Focused input border and focus ring.', 'status-success': 'Success, in stock.',
    'status-error': 'Errors.', 'status-warning': 'Warnings (orange, the only non-token hue in the kit).', 'status-info': 'Info notices.',
}
for n, v, c in D:
    is_color = n.startswith('color-') or n in SEM_USAGE
    if not is_color: continue
    m = re.match(r'var\(--([a-z0-9-]+)\)', v)
    val = '{' + m.group(1) + '}' if m else v.lower() if v.startswith('#') else v.replace(' ', '')
    u = usage(n, c, SEM_USAGE.get(n, ''))
    if n == 'color-graphite-500': u += ' Not for body text: 2.6:1 on white.'
    if n == 'color-mint': u += ' Only on teal-700 / teal-900 grounds (10:1); never on white (1.6:1).'
    color.append({'name': n, 'value': val, 'usage': u or n})

def rem2px(v):
    m = re.match(r'([\d.]+)rem$', v); return f'{float(m.group(1))*16:g}px' if m else v
def num(v):
    try: return float(v)
    except: return v

spacing = [{'name': n, 'value': v, 'usage': (c or rem2px(v)) + ' step.'} for n, v, c in D if n.startswith('space-')]
radius_u = {'radius-sm': 'Badges (2px).', 'radius': 'DEFAULT: buttons, inputs, checkboxes, carousel arrows (4px).',
            'radius-lg': 'Product cards, filter sections, all cards (8px).', 'radius-xl': 'Popups and modals (12px).',
            'radius-pill': 'Fully rounded pills, chips, rating pill.'}
radius = [{'name': n, 'value': v, 'usage': radius_u.get(n, c)} for n, v, c in D if n.startswith('radius')]
shadow_u = {'shadow-card': 'Cards at rest.', 'shadow-hover': 'Card / interactive hover elevation (no lift, no translate).',
            'shadow-modal': 'Modals and popups.', 'shadow-tooltip': 'Tooltips.'}
shadow = [{'name': n, 'value': v, 'usage': shadow_u.get(n, c)} for n, v, c in D if n.startswith('shadow-')]
gradient = [{'name': n, 'value': v, 'usage': {'gradient-brand': 'Dark hero bands, PLP hero (teal-700 → black).',
            'gradient-accent': 'Rare accent fills (mint → teal).'}.get(n, c)} for n, v, c in D if n.startswith('gradient-')]
typescale = [{'name': n, 'value': v, 'usage': c or n.replace('-', ' ')} for n, v, c in D
             if n.startswith(('display-', 'text-')) and not n.endswith('-color') and n not in SEM_USAGE and n != 'text-link' and n != 'text-placeholder']
fontweight = [{'name': n, 'value': v, 'usage': c} for n, v, c in D if n in ('font-regular', 'font-bold', 'font-strong')]
bp = [('bp-sm', '480px', 'Small mobile.'), ('bp-md', '768px', 'Main switch: mobile → desktop (header, footer, layout). Use 48rem in @media.'),
      ('bp-lg', '1024px', 'Tablet landscape.'), ('bp-xl', '1280px', 'Desktop.'), ('bp-2xl', '1440px', 'Wide desktop.'),
      ('bp-3xl', '1600px', 'Max content width (container 100rem).')]
breakpoint = [{'name': a, 'value': b, 'usage': c} for a, b, c in bp]

def size(n):
    v = byname[n][0]; m = re.match(r'clamp\([^,]+,[^,]+,\s*([\d.]+rem)\)', v)
    return (m.group(1) if m else v)
def style(name, pre, sample, use, extra=None):
    s = {'name': name, 'fontSize': size(pre + '-size'), 'lineHeight': num(byname.get(pre + '-lh', ('1.5',))[0]),
         'fontWeight': int(byname.get(pre + '-weight', ('400',))[0]), 'sample': sample, 'usage': use}
    if extra: s.update(extra)
    return s
tokens = {
    'name': 'Metzler Design System', 'version': 1,
    'meta': {'source': 'github', 'repo': 'metzler-de/metzler-ui-kit', 'ref': 'main@' + os.popen(f'git -C "{KIT}" rev-parse --short HEAD').read().strip(),
             'kitVersion': '1.9', 'paths': {'tokens': ['metzler-tokens.css'], 'docs': ['FOR-CLAUDE.md', 'SECTIONS.md', 'COMPONENTS.md', 'ICONS.md', 'BRANDBOOK.md'],
             'assets': ['header/', 'footer/', 'media/', 'Pictures/', 'subcategory_photos/']}, 'synced': NOW[:10]},
    'color': {'themes': [{'id': 'light', 'name': 'Light'}], 'note': 'One light theme. Dark bands are sections (teal-700 / teal-900 / gradient-brand), not a theme.', 'tokens': color},
    'type': {
        'fonts': [],
        'families': {'family': '"Helvetica Neue", Helvetica, Arial, sans-serif', 'family-windows': 'Arial, "Helvetica Neue", Helvetica, sans-serif'},
        'note': 'System stack only, no web font. Helvetica Neue on macOS, Arial first on Windows.',
        'groups': [
            {'name': 'Display', 'family': 'family', 'note': 'Fluid: display-1 = clamp(3rem, 9vw, 5rem), display-2 = clamp(3rem, 7vw, 3.5rem); shown at max.', 'styles': [
                style('display-1', 'display-1', 'Türsprechanlagen', 'Hero headline, one per page.', {'letterSpacing': '-0.04em'}),
                style('display-2', 'display-2', 'Neue Sprechanlage.', 'Section hero on dark bands.', {'letterSpacing': '-0.04em'}),
                style('display-3', 'display-3', 'In drei Schritten', 'Large section titles.', {'letterSpacing': '-0.03em'}),
                style('display-4', 'display-4', 'Gute Gründe', 'Editorial titles (Craft Story, About).', {'letterSpacing': '-0.02em'})]},
            {'name': 'Headings', 'family': 'family', 'note': 'Responsive: h1–h4 shrink below 64rem and 48rem (see bundle.css).', 'styles': [
                style('h1', 'text-h1', 'Video-Türsprechanlage XDM10', 'Page title (PDP / PLP).'),
                style('h2', 'text-h2', 'Technische Details', 'Section heading.'),
                style('h3', 'text-h3', 'Lieferumfang', 'Card and block heading.'),
                style('h4', 'text-h4', 'Häufige Fragen', 'Small headings, footer column heads.')]},
            {'name': 'Body', 'family': 'family', 'styles': [
                style('body-xl', 'text-body-xl', 'Einfach nachrüsten – ohne neue Kabel.', 'Intro / callout copy.'),
                style('body-lg', 'text-body-lg', 'Die XDM10 ersetzt Ihre alte Klingel.', 'Lead paragraphs.'),
                style('body', 'text-body', 'Wetterfest nach IP65 und aus Edelstahl gefertigt.', 'Default body copy, graphite-800 on white.'),
                style('body-sm', 'text-body-sm', 'inkl. MwSt., zzgl. Versand', 'Secondary copy, labels.'),
                {'name': 'caption', 'fontSize': byname['text-caption-size'][0], 'lineHeight': num(byname['text-caption-lh'][0]), 'fontWeight': 400,
                 'sample': 'Art.-Nr. 31101', 'usage': 'Captions and metadata, graphite-600.'},
                {'name': 'overline', 'fontSize': '0.75rem', 'lineHeight': 1.4, 'fontWeight': 700, 'letterSpacing': '0.15em',
                 'sample': 'VIDEO-TÜRSPRECHANLAGE', 'usage': 'Eyebrow above headings: UPPERCASE, teal on light, mint on dark.'}]}]},
    'spacing': {'note': '4px base; always rem.', 'tokens': spacing},
    'radius': {'tokens': radius},
    'shadow': {'note': 'Hover raises the shadow only. Never translate / lift elements on hover.', 'tokens': shadow},
    'typescale': {'note': 'The kit\'s type variables, usable as var(--text-h1-size) etc.', 'tokens': typescale[:60]},
    'fontweight': {'tokens': fontweight},
    'gradient': {'tokens': gradient},
    'breakpoint': {'note': 'Reference values; write media queries in rem (48rem = 768px).', 'tokens': breakpoint},
}
if len(typescale) > 60: warn.append(f'typescale has {len(typescale)} tokens, only 60 kept')
wr('tokens.json', json.dumps(tokens, ensure_ascii=False, indent=1))

# ── doc parsing helpers ────────────────────────────────────────────────────
def chapters(md):
    parts = re.split(r'\n(?=## )', md); out = {}
    for p in parts:
        t = p.split('\n', 1)[0].strip()
        if t.startswith('## '): out[t[3:].strip()] = p
    return out
def blocks(ch):
    return [(lang, code) for lang, code in re.findall(r'```(\w*)\n(.*?)```', ch, re.S)]
def is_css(code):
    c = code.strip()
    return not c.startswith('<') and '{' in c and ':' in c

COMP = chapters(rd('COMPONENTS.md')); SECT = chapters(rd('SECTIONS.md')); FC = chapters(rd('FOR-CLAUDE.md'))
ARROW = '<svg width="12" height="10" viewBox="0 0 14 12" fill="none"><path d="M1 6h12M7 1l6 5-6 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ── bundle.css ─────────────────────────────────────────────────────────────
css_parts = ['/* Metzler Design System v1.9 — stylesheet for previews and Claude Design pages.\n'
             '   Generated from the local UI Kit (FOR-CLAUDE.md, COMPONENTS.md, SECTIONS.md). tokens.css loads first. */\n']
# responsive heading sizes (media blocks of metzler-tokens.css)
media = re.findall(r'(@media[^{]+\{\s*:root\s*\{.*?\}\s*\})', tok_css, re.S)
css_parts.append('/* ── Responsive type (from metzler-tokens.css) ── */\n' + '\n'.join(media) + '\n')
css_parts.append('/* ── Base ── */\nbody { font-family: var(--font-family); color: var(--color-graphite-800); }\n')
for key in ['3 · Typography — Rules and CSS', '4 · Container & Layout', '9 · Section Patterns', '10 · Cards', '15 · Mobile Rules', '16 · Grids']:
    for lang, code in blocks(FC[key]):
        if lang == 'css' or is_css(code): css_parts.append(f'/* ── FOR-CLAUDE §{key} ── */\n' + code)
COMP_CSS_SKIP = {'Introduction', 'Favicon', 'Colors', 'Border Radius', 'Typography'}
for name, ch in COMP.items():
    if name in COMP_CSS_SKIP: continue
    for lang, code in blocks(ch):
        if is_css(code): css_parts.append(f'/* ── COMPONENTS · {name} ── */\n' + code)
for name, ch in SECT.items():
    for lang, code in blocks(ch):
        if lang == 'css': css_parts.append(f'/* ── SECTIONS · {name} ── */\n' + code)
footer_css = [c for l, c in blocks(FC['14 · Footer']) if l == 'css'][0]
css_parts.append('/* ── Footer (FOR-CLAUDE §14) ── */\n' + footer_css)
bundle = rewrite('\n'.join(css_parts), '', 'bundle.css')
bundle = bundle.replace('</style', '<\\/style').replace('var(--color-teal-dark)', 'var(--color-teal-700)')
# guard: selectors that would leak outside a component
for m in re.finditer(r'(?m)^\s*(html|\*|:root)\s*[,{]', bundle): warn.append('global selector in bundle.css: ' + m.group(1))
wr('components/bundle.css', bundle)

# vars used but not defined anywhere
defined = {t['name'] for fam in ('color', 'spacing', 'radius', 'shadow', 'typescale', 'fontweight', 'gradient', 'breakpoint') for t in tokens[fam]['tokens']}
defined |= {'font-family', 'font-family-windows'}
defined |= set(re.findall(r'--([a-z0-9-]+)\s*:', bundle))
used = set(re.findall(r'var\(--([a-z0-9-]+)', bundle))
missing = sorted(used - defined)
if missing: warn.append('vars used in bundle.css but undefined: ' + ', '.join(missing))

# ── previews + READMEs ─────────────────────────────────────────────────────
def preview(group, height, title, body, extra_css='', subtitle=''):
    sub = f' subtitle="{subtitle}"' if subtitle else ''
    return (f'<!-- @dsCard group="{group}" height={height}{sub} -->\n<!doctype html>\n<html lang="de">\n<head><meta charset="utf-8"><title>{title}</title>\n'
            f'<style>body{{margin:0;padding:1.5rem;background:var(--color-white);font-family:var(--font-family);color:var(--color-graphite-800)}}'
            f'.pv-label{{font:700 0.6875rem/1.4 var(--font-family);letter-spacing:.08em;text-transform:uppercase;color:var(--color-graphite-600);margin:1.25rem 0 .5rem}}'
            f'.pv-label:first-child{{margin-top:0}}.pv-row{{display:flex;flex-wrap:wrap;gap:.75rem;align-items:center}}{extra_css}</style>\n'
            f'</head>\n<body>\n{body}\n</body>\n</html>\n')

def comp_body(ch, name):
    out = []; label = None
    for seg in re.split(r'(?m)^(###\s+.*)$', ch):
        if seg.startswith('###'): label = seg[3:].strip(); continue
        for lang, code in blocks(seg):
            c = code.strip()
            if not c.startswith('<'): continue
            c = c.replace('<svg …/>', ARROW).replace('<svg …>', ARROW)
            if label and label.lower() != 'css definitions': out.append(f'<div class="pv-label">{label}</div>')
            out.append(f'<div class="pv-row">{c}</div>' if len(c) < 1500 else c)
    return rewrite('\n'.join(out), '', 'components/' + name)

def comp_readme(title, ch, lead):
    body = re.sub(r'^## .*\n', '', ch, count=1).strip()
    body = rewrite(body, '', 'readme ' + title)
    return f'# {title}\n\n{lead}\n\n{body}\n'

COMPONENTS = [  # (Comp, chapter, group, height, lead)
    ('Button', 'Buttons', 'Actions', 360, 'Buttons: .btn with .btn-primary (main CTA), .btn-secondary, .btn-proceed (with arrow) and .btn-white on dark; sizes .btn-lg / .btn-sm, .btn-block.'),
    ('Links', 'Links', 'Actions', 220, 'Text links in teal on light and mint on dark, with and without arrow.'),
    ('NavigationArrows', 'Navigation Arrows', 'Actions', 180, 'Square carousel arrows with var(--radius); controls only, never step numbers.'),
    ('Pagination', 'Pagination', 'Actions', 220, 'Page navigation for listings and reviews.'),
    ('FileDownload', 'File Download', 'Actions', 220, 'Download row for PDFs (manuals, datasheets) on product pages.'),
    ('FormElements', 'Form Elements', 'Forms', 1200, 'Inputs with floating labels, selects, checkboxes, radios, textarea and error states.'),
    ('QuantityCounter', 'Quantity Counter', 'Forms', 180, 'Minus / value / plus stepper for cart quantities.'),
    ('FilterChips', 'Filter Chips', 'Forms', 160, 'Removable filter chips for listing filters.'),
    ('Configurator', 'Configurator', 'Forms', 320, 'Option tiles used in product configurators.'),
    ('Alerts', 'Alerts', 'Feedback', 460, 'Inline alerts for info, success, warning and error.'),
    ('Tooltip', 'Tooltip', 'Feedback', 220, 'Short help text on hover or focus.'),
    ('Badge', 'Badge', 'Feedback', 180, 'Small status and sale badges (radius-sm).'),
    ('Modal', 'Modal', 'Feedback', 760, 'Popups and modals with radius-xl and shadow-modal.'),
    ('Tabs', 'Tabs', 'Navigation', 220, 'Section tabs such as Beschreibung · Bewertungen · Downloads · Technische Details.'),
    ('Stepper', 'Stepper', 'Navigation', 240, 'Step indicator for checkout and configurators.'),
    ('Breadcrumbs', 'Breadcrumbs', 'Navigation', 200, 'Breadcrumbs, always left-aligned; light and dark variants.'),
    ('Typography', 'Typography', 'Content', 760, 'The type scale in use: display, headings, body and overline.'),
    ('Lists', 'Lists', 'Content', 420, 'Check lists, feature lists and definition lists.'),
    ('Table', 'Table', 'Content', 320, 'Spec and comparison tables.'),
    ('ProductCards', 'Product Cards', 'Content', 660, 'Product cards for listings and cross-selling (radius-lg, shadow-hover on hover, no lift).'),
    ('SpacersDividers', 'Spacers & Dividers', 'Content', 460, 'Spacing steps and hairline dividers.'),
]
comps_written = []

CUSTOM = {
 'Tooltip': """<div class="pv-label">Positions (shown open)</div>
<div class="pv-row" style="padding:3.5rem 1rem 3.5rem 8rem;gap:6rem">
  <span class="tooltip-wrapper"><button class="btn btn-secondary">Oben</button><span class="tooltip tooltip-top" style="opacity:1">Versandkostenfrei ab 50 €</span></span>
  <span class="tooltip-wrapper"><button class="btn btn-secondary">Unten</button><span class="tooltip tooltip-bottom" style="opacity:1">In 3–5 Werktagen bei Ihnen</span></span>
  <span class="tooltip-wrapper"><button class="btn btn-secondary">Hell</button><span class="tooltip tooltip-top tooltip-light" style="opacity:1">Lasergravur inklusive</span></span>
</div>
<div class="pv-label">Multiline</div>
<div class="pv-row" style="padding:0 1rem 5.5rem">
  <span class="tooltip-wrapper"><button class="btn btn-primary">Info</button><span class="tooltip tooltip-bottom tooltip-multiline" style="opacity:1;left:0;transform:none">Die XDM10 nutzt Ihre vorhandene 2-Draht-Klingelleitung, es sind keine neuen Kabel nötig.</span></span>
</div>""",
 'SpacersDividers': """<div class="pv-label">Spacers (shown tinted)</div>
<div style="display:grid;gap:.5rem;max-width:40rem">
  <div style="display:flex;align-items:center;gap:1rem"><div class="spacer-s" style="width:12rem;background:var(--color-teal-100)"></div><span class="caption">.spacer-s · 1.5rem / 24px</span></div>
  <div style="display:flex;align-items:center;gap:1rem"><div class="spacer-m" style="width:12rem;background:var(--color-teal-100)"></div><span class="caption">.spacer-m · 3rem / 48px</span></div>
  <div style="display:flex;align-items:center;gap:1rem"><div class="spacer-l" style="width:12rem;background:var(--color-teal-100)"></div><span class="caption">.spacer-l · 6rem / 96px</span></div>
</div>
<div class="pv-label">Dividers</div>
<p class="caption">.divider-s · 1rem margin</p><hr class="divider-s">
<p class="caption">.divider-m · 2rem margin</p><hr class="divider-m">
<p class="caption">.divider-l · 4rem margin</p><hr class="divider-l">""",
 'Typography': """<p class="overline">Video-Türsprechanlage</p>
<div class="display-1">Türsprechanlagen</div>
<div class="display-2" style="margin-top:1rem">Neue Sprechanlage.</div>
<div class="display-3" style="margin-top:1rem">In drei Schritten</div>
<div class="display-4" style="margin-top:1rem">Gute Gründe</div>
<h1 style="margin-top:1.5rem">Video-Türsprechanlage XDM10</h1>
<h2>Technische Details</h2>
<h3>Lieferumfang</h3>
<h4>Häufige Fragen</h4>
<p class="body-lg">Die XDM10 ersetzt Ihre alte Klingel – ohne neue Kabel.</p>
<p>Wetterfest nach IP65, aus Edelstahl gefertigt und in Deutschland graviert.</p>
<p class="body-sm">inkl. MwSt., zzgl. Versand</p>
<p class="caption">Art.-Nr. 31101 · Lieferzeit 3–5 Werktage</p>""",
}
for comp, chap, group, h, lead in COMPONENTS:
    ch = COMP[chap]
    body = CUSTOM.get(comp) or comp_body(ch, comp)
    if not body.strip(): warn.append(f'{comp}: no html'); continue
    wr(f'components/{comp}/preview.html', preview(group, h, comp, body))
    wr(f'components/{comp}/README.md', comp_readme(comp, ch, lead))
    comps_written.append(comp)

# Header family: canonical files from header/
def header_preview(fname, comp, group, h, lead, chap_keys):
    src = rd('header/' + fname)
    src = re.sub(r'<link[^>]+metzler-tokens\.css[^>]*>', '', src)
    src = rewrite(src, 'header', 'components/' + comp)
    src = src.replace('<!DOCTYPE html>', '').replace('<!doctype html>', '')
    wr(f'components/{comp}/preview.html', f'<!-- @dsCard group="{group}" height={h} -->\n<!doctype html>\n' + src.strip() + '\n')
    txt = '\n\n'.join(re.sub(r'^## .*\n', '', COMP[k], count=1).strip() for k in chap_keys if k in COMP)
    fc7 = FC['7 · Header']
    wr(f'components/{comp}/README.md', f'# {comp}\n\n{lead}\n\n**Canonical source:** `header/{fname}` in the kit. Copy it verbatim; never rebuild the header.\n\n' + rewrite(txt, 'header') + '\n\n## Rules (FOR-CLAUDE §7)\n\n' + rewrite(re.sub(r'^## .*\n', '', fc7, count=1), 'header') + '\n')
    comps_written.append(comp)
header_preview('preview.html', 'Header', 'Navigation', 620, 'The full shop header: trust bar, logo + search + account/cart, category navigation with mega menus, fixed at the top.', ['Header'])
header_preview('preview-sticky.html', 'HeaderSticky', 'Navigation', 360, 'The compact sticky header shown after the first scroll (.is-sticky), with the side menu.', ['Header · Sticky'])
header_preview('preview-mobile-sticky.html', 'HeaderMobile', 'Navigation', 560, 'The mobile header (< 48rem) with hamburger drawer.', ['Header · Mobile'])
header_preview('preview-megamenu.html', 'HeaderMegaMenu', 'Navigation', 640, 'The Briefkästen mega menu with category tiles and a promo tile.', [])

# Footer
fc14 = FC['14 · Footer']
f_html = [c for l, c in blocks(fc14) if l == 'html'][0]
wr('components/Footer/preview.html', preview('Navigation', 760, 'Footer', rewrite(f_html, '', 'Footer'), 'body{padding:0}'))
wr('components/Footer/README.md', '# Footer\n\nThe fixed shop footer (5 columns, shipping + payment + rating row, 13 legal links, „Vertrag widerrufen“ button, copyright), background color-teal-700. Copy it exactly; never invent columns or links.\n\n'
   + rewrite(re.sub(r'^## .*\n', '', fc14, count=1), '', 'Footer README') + '\n')
comps_written.append('Footer')

# Sections
SECTION_NAMES = [('Section 01', 'SupportKontakt'), ('Section 02', 'NeueFeatures'), ('Section 03', 'OeffnungSlider'), ('Section 04', 'FAQ'),
                 ('Section 05', 'Gesichtserkennung'), ('Section 06', 'EditorialQA'), ('Section 07', 'ProductHero'), ('Section 08', 'FeatureDetail'),
                 ('Section 09', 'FeatureDuo'), ('Section 10', 'XDM10Hero'), ('Section 11', 'DreiSchritte'), ('Section 12', 'SpecCallouts'),
                 ('Section 13', 'AboutHero'), ('Section 14', 'CraftStory')]
for prefix, comp in SECTION_NAMES:
    key = next(k for k in SECT if k.startswith(prefix))
    ch = SECT[key]
    htmls = [c for l, c in blocks(ch) if l == 'html']
    body = rewrite('\n'.join(htmls), '', 'components/' + comp)
    title = key.split('·', 1)[1].strip() if '·' in key else key
    wr(f'components/{comp}/preview.html', preview('Sections', 720, comp, body, 'body{padding:0}', subtitle=prefix))
    what = re.search(r'\*\*What:\*\*\s*(.+)', ch)
    lead = (what.group(1).strip() if what else title)
    wr(f'components/{comp}/README.md', f'# {comp}\n\n{lead}\n\n' + rewrite(re.sub(r'^## .*\n', '', ch, count=1).strip(), '', 'readme ' + comp) + '\n')
    comps_written.append(comp)

# ── brand book sections (further *.md) ─────────────────────────────────────
def section_md(fname, title, drop_intro=True):
    s = rd(fname)
    s = re.sub(r'^# .*\n', f'# {title}\n', s, count=1)
    return rewrite(s, '', fname)
wr('guidelines/10-page-brief.md', section_md('FOR-CLAUDE.md', 'Page brief (FOR-CLAUDE)'))
wr('guidelines/20-sections-and-blueprints.md', section_md('SECTIONS.md', 'Sections and page blueprints'))
wr('guidelines/30-brandbook.md', section_md('BRANDBOOK.md', 'Brandbook'))
wr('guidelines/40-icons.md', section_md('ICONS.md', 'Icons: inline SVG code'))
wr('guidelines/50-changelog.md', section_md('CHANGELOG.md', 'Changelog'))

# ── README ────────────────────────────────────────────────────────────────
logo = BLOB['header/logo.svg']; logo_w = BLOB['footer/Metzler_Logo_footer.svg']
README = f"""Metzler GmbH makes stainless-steel outdoor hardware — video intercoms (XDM10, VDM10, SDM10), mailboxes, parcel boxes, doorbells and house numbers — sold on edelstahl-tuerklingel.de. This system is the shop's UI: calm, precise, product first. Everything here comes from the Metzler UI Kit v1.9 and is the only source for Metzler web styles.

## Content fundamentals

- **All customer-facing copy is German**, including labels, placeholders, CTAs, alt text and error messages. Address customers with **„Sie“**, never „du“.
- Tone: factual, reassuring, specific. Lead with the product benefit and real numbers („Wetterfest nach IP65“, „Lieferung in 3–5 Werktagen“). No exclamation-mark hype, no emoji.
- Use the shop's own terms: Türsprechanlage, Video-Türsprechanlage, Innenstation, Briefkasten, Paketbox, Türklingel, Hausnummer, Namensschild, Gravur, Klingeltaster, 2-Draht-BUS, Komplettset.
- Prices: „ab 899,00 €“, „inkl. MwSt., zzgl. Versand“. Product names: „Metzler Video-Türsprechanlage XDM10“. Never invent prices, dimensions or discounts; take them from the live shop.
- Headlines: sentence case. Eyebrows (`overline`): UPPERCASE, `color-teal` on light, `color-mint` on dark.

## Visual foundations

- **Color.** Page ground `color-paper` (#F5F6FA); cards and panels `color-white`. Brand color is `color-teal` (#015253): primary CTAs, links, active states, focus; hover `color-teal-600`. Headlines `color-digital-black`, body `color-graphite-800`, secondary `color-graphite-700`, captions `color-graphite-600`. Dark bands: `color-teal-900` or `gradient-brand`; the footer is always `color-teal-700`; links and icons on dark are `color-mint`. `color-metzler-rot` only for the logo square and sale badges, `color-red` for errors, `color-green` for availability and success, `color-star` for rating stars only. Never use raw hex in a design: always the tokens.
- **Type.** One family: `--font-family` ("Helvetica Neue", Helvetica, Arial). Scale: `display-1…4` for heroes, `h1…h4`, `body-xl`, `body-lg`, `body`, `body-sm`, `caption`, `overline`. Weights 400 / 500 / 600 / 700 (800 only for the wordmark).
- **Units and layout.** All sizes in rem (16px = 1rem). Content sits in `.container`: max-width exactly 100rem, side padding inside the container, never on `<section>`, `<header>` or `<footer>`. The main breakpoint is 48rem (768px). Mobile-first.
- **Spacing.** 4px steps `space-1 … space-16`. Sections breathe: `section--lg` / `section--md` paddings from the section patterns.
- **Shape.** Buttons, inputs, carousel arrows: `radius` (4px). All cards: `radius-lg` (8px). Popups and modals: `radius-xl`. Pills and chips: `radius-pill`. Badges: `radius-sm`.
- **Depth and motion.** `shadow-card` at rest, `shadow-hover` on hover. **Never lift, translate or scale elements on hover** („no jumping“): only color, border or shadow change, 0.15s.
- **Imagery.** Real Metzler product photos only (see Product imagery and Navigation assets): stainless steel, anthracite RAL 7016, clean light backgrounds. No stock people or illustrations in place of products.
- **Accessibility.** Body text `color-graphite-800` on white (12.8:1). `color-graphite-500` is for placeholders and disabled states only (2.6:1 — not for readable text). Focus: 2px `color-teal` outline with 2px offset.

## Iconography

81 icons in the **Icons** asset group: 24×24 viewBox, 1.8 stroke, round caps and joins, `stroke="currentColor"`. The tiles are inked in `color-graphite-900` for display; in designs **paste the inline SVG from the „Icons: inline SVG code“ chapter** so the icon takes the text color. Icon containers are 2.5rem squares with `radius-lg` and a teal tint `rgba(1,82,83,0.08)`. Never use external icon libraries or emoji.

## Logo

- Metzler logo (red M-square + METZLER wordmark): `metzler-logo.svg` on light grounds, `metzler-logo-white.svg` on `color-teal-700` / dark. Use the files, never redraw or recolor the mark. Rules and incorrect usage: see the Brandbook chapter.

## Building a page

1. Start from a page blueprint (Sections and page blueprints chapter) and stack ready-made **Sections** (SupportKontakt, NeueFeatures, FAQ, ProductHero, XDM10Hero, SpecCallouts …) before designing anything new.
2. Always use the canonical **Header** and **Footer** components exactly as they are.
3. Build everything else from the components (Button, FormElements, ProductCards, Tabs, Breadcrumbs, Alerts, Modal …) and `components/bundle.css` classes. Reuse the closest existing token or component; if something truly does not exist, ask instead of inventing a value.
4. Check: rem only, tokens only, container 100rem, German copy, no hover lift, one dark hero per page at most, FAQ is the last content section before the footer.
"""
wr('README.md', README)

# asset group READMEs
GROUP_NOTES = {
    'Logos': 'Metzler logos. `metzler-logo.svg` (red M-square + digital-black wordmark) on light grounds; `metzler-logo-white.svg` on color-teal-700 and other dark grounds; `favicon.svg` for every page head. Never recolor or redraw.',
    'Icons': 'The 81 kit icons, inked in color-graphite-900 (#1A1A1F) for these tiles. For designs paste the inline SVG from the „Icons: inline SVG code“ chapter, which uses currentColor. Star, pdf-badge, guarantee and packaging symbols have fixed colors.',
    'Payment & Shipping': 'Footer badges, 53×30 white cards: shipping partners DPD, DHL, Hasenauer & Koch; payment methods SEPA, Amex, Visa, Amazon Pay, Klarna, PayPal, Mastercard, Apple Pay, Google Pay, Vorkasse. Use in this order.',
    'Social': 'White single-ink social icons for the footer (Pinterest, Facebook, Instagram, YouTube, X) on 35px round tiles at rgba(255,255,255,0.1).',
    'Awards & Reviews': 'Computer Bild TopShop badges 2023–2025 and 3 Jahre (footer „Qualität“), plus the review-source badges for the rating pill: all, Trusted Shops, Google, Trustpilot.',
    'Navigation': 'Category thumbnails for the header mega menus and sub-category navigation (Briefkästen, Paketboxen, Sprechanlagen, Türklingeln, Hausnummern, Kameras, Leuchten).',
    'Product imagery': 'Real Metzler product and brand photography used by the sections (XDM10 hero and detail, VDM10 2.0, Innenstation, craft and about images, engraving, colours, review photos) and one product video.',
}
TILES = {'Logos': 'l', 'Icons': 'xs', 'Payment & Shipping': 's', 'Social': 'xs', 'Awards & Reviews': 's', 'Navigation': 'm', 'Product imagery': 'l'}
GROUP_ORDER = ['Logos', 'Icons', 'Payment & Shipping', 'Social', 'Awards & Reviews', 'Navigation', 'Product imagery']
for g in GROUP_ORDER: wr(f'assets/{g}/README.md', f'# {g}\n\n{GROUP_NOTES[g]}\n')

# ── Cover ──────────────────────────────────────────────────────────────────
COVER = """<!-- @dsCard height=320 -->
<!doctype html>
<html lang="de">
<head><meta charset="utf-8"><title>Cover</title>
<style>
  body{margin:0;background:var(--color-paper);font-family:var(--font-family);}
  .cv{position:relative;width:960px;height:320px;overflow:hidden;background:var(--color-paper);}
  svg{position:absolute;left:0;top:0}
  .deep{fill:var(--color-teal-900)} .teal{fill:var(--color-teal)} .foot{fill:var(--color-teal-700)}
  .mint{fill:var(--color-mint)} .rot{fill:var(--color-metzler-rot)} .tint{fill:var(--color-teal-100)}
  .tile{fill:var(--color-teal)} .sq{rx:var(--radius-sm)}
  .name{position:absolute;left:48px;bottom:58px;margin:0;font-weight:700;font-size:64px;line-height:.95;letter-spacing:-0.02em;color:var(--color-digital-black);white-space:nowrap}
  .tag{position:absolute;left:48px;bottom:30px;margin:0;font-size:14px;line-height:1.4;color:var(--color-graphite-700);max-width:440px}
</style></head>
<body>
<div class="cv">
<svg width="960" height="120" viewBox="0 0 960 120" aria-hidden="true">
  <!-- blocks: teal-900 slab 432×120, teal 192×120, teal-700 144×120, mint 64×64, metzler-rot 48×48 (the logo's M-square), teal-100 128×120
       arrangement: top band of unequal flush strips (the shop composes in horizontal bands: trust bar, nav, hero)
       pattern row: geometric, modular, dense UI → small square tiles on space-4 (16px) pitch cut from the teal-900 slab, echoing the M-square
       steps and radii: 16px pitch (space-4), 8px tiles, radius-sm corners; strips on 16px multiples -->
  <rect class="deep" x="0" y="0" width="432" height="120"/>
  <g>
    <!-- 3 rows × 12 tiles = 36 units -->
    <rect class="tile sq" x="208" y="24" width="8" height="8"/><rect class="tile sq" x="224" y="24" width="8" height="8"/><rect class="tile sq" x="240" y="24" width="8" height="8"/><rect class="tile sq" x="256" y="24" width="8" height="8"/><rect class="tile sq" x="272" y="24" width="8" height="8"/><rect class="tile sq" x="288" y="24" width="8" height="8"/><rect class="tile sq" x="304" y="24" width="8" height="8"/><rect class="tile sq" x="320" y="24" width="8" height="8"/><rect class="tile sq" x="336" y="24" width="8" height="8"/><rect class="tile sq" x="352" y="24" width="8" height="8"/><rect class="tile sq" x="368" y="24" width="8" height="8"/><rect class="tile sq" x="384" y="24" width="8" height="8"/>
    <rect class="tile sq" x="208" y="56" width="8" height="8"/><rect class="tile sq" x="224" y="56" width="8" height="8"/><rect class="tile sq" x="240" y="56" width="8" height="8"/><rect class="tile sq" x="256" y="56" width="8" height="8"/><rect class="tile sq" x="272" y="56" width="8" height="8"/><rect class="tile sq" x="288" y="56" width="8" height="8"/><rect class="tile sq" x="304" y="56" width="8" height="8"/><rect class="tile sq" x="320" y="56" width="8" height="8"/><rect class="tile sq" x="336" y="56" width="8" height="8"/><rect class="tile sq" x="352" y="56" width="8" height="8"/><rect class="tile sq" x="368" y="56" width="8" height="8"/><rect class="tile sq" x="384" y="56" width="8" height="8"/>
    <rect class="tile sq" x="208" y="88" width="8" height="8"/><rect class="tile sq" x="224" y="88" width="8" height="8"/><rect class="tile sq" x="240" y="88" width="8" height="8"/><rect class="tile sq" x="256" y="88" width="8" height="8"/><rect class="tile sq" x="272" y="88" width="8" height="8"/><rect class="tile sq" x="288" y="88" width="8" height="8"/><rect class="tile sq" x="304" y="88" width="8" height="8"/><rect class="tile sq" x="320" y="88" width="8" height="8"/><rect class="tile sq" x="336" y="88" width="8" height="8"/><rect class="tile sq" x="352" y="88" width="8" height="8"/><rect class="tile sq" x="368" y="88" width="8" height="8"/><rect class="tile sq" x="384" y="88" width="8" height="8"/>
  </g>
  <rect class="teal" x="432" y="0" width="192" height="120"/>
  <rect class="foot" x="624" y="0" width="144" height="120"/>
  <rect class="mint" x="768" y="0" width="64" height="64"/>
  <rect class="rot sq" x="784" y="72" width="32" height="32"/>
  <rect class="tint" x="832" y="0" width="128" height="120"/>
</svg>
<p class="name">Metzler Design System</p>
<p class="tag">Die Oberfläche von edelstahl-tuerklingel.de — ruhig, präzise, Produkt zuerst.</p>
</div>
</body>
</html>
"""
wr('components/Cover/preview.html', COVER)

# ── index ─────────────────────────────────────────────────────────────────
asset_groups = {}
for g in GROUP_ORDER:
    files = {}; order = []
    for s in staged:
        if s['group'] != g: continue
        key = re.sub(r'[^A-Za-z0-9_./-]', lambda m: ''.join('~%02x' % b for b in m.group(0).encode()), s['name'])
        files[key] = {'name': s['name'], 'blob': s['blob'], 'size': s['size'], 'type': s['type']}
        order.append(s['name'])
    asset_groups[g] = {'name': g, 'tile': TILES[g], 'order': order, 'files': files}
index = {'v': 3, 'layout': 'files', 'createdOnFiles': {'v': 1, 'at': NOW}, 'title': 'Metzler Design System', 'namespace': 'Metzler',
         'libraries': [], 'sections': {}, 'groups': GROUP_ORDER, 'assetGroups': asset_groups, 'blobs': {}, 'docs': {'readme': 'project/README.md', 'sections': []},
         'lastChange': {'by': 'Mykhailo Ruban', 'at': NOW, 'via': 'Claude Code · metzler-de/metzler-ui-kit@' + tokens['meta']['ref'].split('@')[1],
                        'note': 'Built from the local Metzler UI Kit v1.9: tokens, brand book, 40 components and sections, header, footer, 193 assets.'}}
wr('design-system.json', json.dumps(index, ensure_ascii=False, indent=1))

# ── report ────────────────────────────────────────────────────────────────
files = []
for root, _, fs in os.walk(P):
    for f in fs: files.append(os.path.relpath(os.path.join(root, f), OUT))
print('files:', len(files), ' components:', len(comps_written))
big = [(f, os.path.getsize(os.path.join(OUT, f))) for f in files if os.path.getsize(os.path.join(OUT, f)) > 200_000]
print('large files:', big)
print('colors', len(color), 'typescale', len(typescale), 'spacing', len(spacing))
print('WARNINGS:'); [print(' -', w) for w in warn]
json.dump(sorted(files), open(os.path.join(HERE, 'files.json'), 'w'), indent=0)
