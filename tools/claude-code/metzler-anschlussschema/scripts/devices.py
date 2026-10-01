# -*- coding: utf-8 -*-
"""
Metzler Anschlussschemata – Geräte-Bibliothek.

Jedes Gerät wird in echten Millimetern gezeichnet (1 Einheit = 1 mm), nach den
Produktfotos auf edelstahl-tuerklingel.de (Stand 09/2026). Platziert wird es mit
Device.place(x, y, s) – die Anschlusspunkte (anchors) werden dabei mitgerechnet.
"""
import math

FONT = '"Helvetica Neue", Helvetica, Arial, sans-serif'


# ----------------------------------------------------------------- basics
def f(n):
    """Compact number formatting for SVG."""
    if isinstance(n, str):
        return n
    s = ('%.2f' % n).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;'))


def attrs(**kw):
    out = []
    for k, v in kw.items():
        if v is None:
            continue
        k = k.rstrip('_').replace('_', '-')
        out.append('%s="%s"' % (k, esc(f(v)) if not isinstance(v, str) else esc(v)))
    return ' '.join(out)


def rect(x, y, w, h, rx=0, **kw):
    return '<rect %s/>' % attrs(x=x, y=y, width=w, height=h, rx=rx or None, **kw)


def circle(cx, cy, r, **kw):
    return '<circle %s/>' % attrs(cx=cx, cy=cy, r=r, **kw)


def line(x1, y1, x2, y2, **kw):
    return '<line %s/>' % attrs(x1=x1, y1=y1, x2=x2, y2=y2, **kw)


def path(d, **kw):
    return '<path %s/>' % attrs(d=d, **kw)


def poly(pts, **kw):
    return '<polygon %s/>' % attrs(points=' '.join('%s,%s' % (f(a), f(b)) for a, b in pts), **kw)


def text(x, y, s, size=4, weight=None, fill='#1A171B', anchor=None, ls=None, family=None,
         style=None, **kw):
    return '<text %s>%s</text>' % (attrs(x=x, y=y, font_size=size, font_weight=weight, fill=fill,
                                         text_anchor=anchor, letter_spacing=ls,
                                         font_family=family, style=style, **kw), esc(s))


def g(children, **kw):
    a = attrs(**kw)
    return '<g%s>%s</g>' % ((' ' + a) if a else '', ''.join(children))


# ----------------------------------------------------------------- defs registry
class Defs:
    """Collects gradients / clip paths once per SVG. IDs are prefixed per scheme."""

    def __init__(self, prefix):
        self.prefix = prefix
        self.items = {}

    def _id(self, name):
        return '%s-%s' % (self.prefix, name)

    def lin(self, name, stops, x1=0, y1=0, x2=0, y2=1):
        i = self._id(name)
        if i not in self.items:
            st = ''.join('<stop offset="%s" stop-color="%s"%s/>' % (
                f(o), c, (' stop-opacity="%s"' % f(op)) if op is not None else '')
                for o, c, op in [(s + (None,))[:3] for s in stops])
            self.items[i] = '<linearGradient id="%s" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient>' % (
                i, f(x1), f(y1), f(x2), f(y2), st)
        return 'url(#%s)' % i

    def rad(self, name, stops, cx=0.5, cy=0.5, r=0.5):
        i = self._id(name)
        if i not in self.items:
            st = ''.join('<stop offset="%s" stop-color="%s"%s/>' % (
                f(o), c, (' stop-opacity="%s"' % f(op)) if op is not None else '')
                for o, c, op in [(s + (None,))[:3] for s in stops])
            self.items[i] = '<radialGradient id="%s" cx="%s" cy="%s" r="%s">%s</radialGradient>' % (
                i, f(cx), f(cy), f(r), st)
        return 'url(#%s)' % i

    def clip(self, name, inner):
        i = self._id(name)
        if i not in self.items:
            self.items[i] = '<clipPath id="%s">%s</clipPath>' % (i, inner)
        return 'url(#%s)' % i

    def svg(self):
        return '<defs>%s</defs>' % ''.join(self.items.values())


# ----------------------------------------------------------------- device container
class Device:
    def __init__(self, svg, w, h, anchors=None, name=''):
        self.svg, self.w, self.h = svg, w, h
        self.anchors = anchors or {}
        self.name = name

    def place(self, x, y, s=1.0):
        return Placed(self, x, y, s)


class Placed:
    def __init__(self, dev, x, y, s):
        self.dev, self.x, self.y, self.s = dev, x, y, s
        self.w, self.h = dev.w * s, dev.h * s

    def a(self, name):
        ax, ay = self.dev.anchors[name]
        return (self.x + ax * self.s, self.y + ay * self.s)

    def pt(self, fx, fy):
        """Point at fraction of the device box."""
        return (self.x + self.w * fx, self.y + self.h * fy)

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def bottom(self):
        return self.y + self.h

    @property
    def right(self):
        return self.x + self.w

    def svg(self):
        return '<g transform="translate(%s %s) scale(%s)">%s</g>' % (f(self.x), f(self.y), f(self.s), self.dev.svg)


# ----------------------------------------------------------------- shared pieces
def metzler_logo(D, cx, cy, size, fill='#6A6C70', square=None, text_fill=None):
    """'[M] METZLER' wordmark as printed on the devices (grey, M in a square)."""
    sq = size * 1.05
    tw = size * 4.35
    x0 = cx - (sq + size * 0.35 + tw) / 2
    sqc = square or fill
    out = [rect(x0, cy - sq * 0.78, sq, sq, rx=sq * 0.08, fill=sqc),
           path('M%s %s l%s %s l%s %s l%s %s' % (
               f(x0 + sq * 0.2), f(cy + sq * 0.02), f(0), f(-sq * 0.62), f(sq * 0.3), f(sq * 0.38),
               f(sq * 0.3), f(-sq * 0.38)), fill='none', stroke='#FFFFFF' if not square else '#FFFFFF',
               stroke_width=sq * 0.13, stroke_linejoin='round'),
           line(x0 + sq * 0.8, cy - sq * 0.6, x0 + sq * 0.8, cy + sq * 0.02, stroke='#FFFFFF',
                stroke_width=sq * 0.13),
           text(x0 + sq + size * 0.35, cy, 'METZLER', size=size, weight=700,
                fill=text_fill or fill, ls=size * 0.04)]
    return ''.join(out)


def steel(D, name='steel', horizontal=True):
    if horizontal:
        return D.lin(name, [(0, '#F4F5F7'), (0.35, '#BFC3C8'), (0.55, '#E9EBEE'), (0.8, '#A8ADB3'), (1, '#DDE0E3')])
    return D.lin(name + 'v', [(0, '#F4F5F7'), (0.35, '#BFC3C8'), (0.55, '#E9EBEE'), (0.8, '#A8ADB3'), (1, '#DDE0E3')],
                 x1=0, y1=0, x2=1, y2=0)


def screw_terminal(cx, cy, r=1.9, body='#1B1C1E', slot='#6B6E73'):
    return (circle(cx, cy, r, fill=body, stroke='#0E0F10', stroke_width=0.3) +
            line(cx - r * 0.62, cy + r * 0.3, cx + r * 0.62, cy - r * 0.3, stroke=slot, stroke_width=r * 0.34,
                 stroke_linecap='round'))


def plug2(cx, cy, w=9.4, h=4.4):
    """Black 2-pole pluggable terminal as on the Metzler distributors (top view)."""
    x, y = cx - w / 2, cy - h / 2
    return (rect(x, y, w, h, rx=h / 2, fill='#1D1E21', stroke='#0B0B0C', stroke_width=0.25) +
            line(cx, y + 0.6, cx, y + h - 0.6, stroke='#56585C', stroke_width=0.35) +
            circle(cx - w * 0.24, cy, 0.75, fill='#3C3E42') + circle(cx + w * 0.24, cy, 0.75, fill='#3C3E42'))


def green_block(x, y, poles, pitch=5.08, h=8.2):
    """Green pluggable screw terminal block (Stockwerksverteiler)."""
    w = poles * pitch
    out = [rect(x, y, w, h, rx=0.6, fill='#2EA04C', stroke='#1B6E33', stroke_width=0.35),
           rect(x, y + h * 0.72, w, h * 0.28, fill='#238A3F')]
    for i in range(poles):
        cx = x + pitch * (i + 0.5)
        out.append(circle(cx, y + h * 0.42, pitch * 0.33, fill='#F2F4F3', stroke='#8FA596', stroke_width=0.3))
        out.append(line(cx - pitch * 0.2, y + h * 0.42, cx + pitch * 0.2, y + h * 0.42, stroke='#9AA39D',
                        stroke_width=0.45))
    return ''.join(out)


def rj45(cx, cy, w=7.6, h=6.2, fill='#1A1B1D'):
    x, y = cx - w / 2, cy - h / 2
    return (rect(x, y, w, h, rx=0.5, fill='#0E0F10', stroke='#5B5E63', stroke_width=0.35) +
            rect(x + w * 0.18, y + h * 0.18, w * 0.64, h * 0.52, fill=fill) +
            rect(x + w * 0.36, y + h * 0.7, w * 0.28, h * 0.18, fill=fill))


# ================================================================= INDOOR STATIONS
def _icon_row(x0, y, w, color, size, labels=True, lab_color=None, lab_size=None):
    """Anruf / Nachricht / Livebild / Einstellungen icons as on the Metzler UI."""
    xs = [x0 + w * p for p in (0.21, 0.40, 0.585, 0.77)]
    s = size
    sw = s * 0.11
    out = []
    # phone with arrow
    x = xs[0]
    out.append(path('M%s %s c%s %s %s %s %s %s l%s %s c%s %s %s %s %s %s z' % (
        f(x - s * 0.42), f(y - s * 0.38), f(-s * 0.1), f(s * 0.5), f(s * 0.35), f(s * 0.95), f(s * 0.85), f(s * 0.8),
        f(s * 0.12), f(-s * 0.2), f(-s * 0.2), f(-s * 0.15), f(-s * 0.35), f(-s * 0.3), f(-s * 0.4), f(-s * 0.55)),
        fill='none', stroke=color, stroke_width=sw, stroke_linejoin='round'))
    out.append(path('M%s %s l%s %s m0 0 h%s m%s 0 v%s' % (
        f(x + s * 0.05), f(y - s * 0.02), f(s * 0.42), f(-s * 0.42), f(-s * 0.22), f(s * 0.22), f(s * 0.22)),
        fill='none', stroke=color, stroke_width=sw, stroke_linecap='round'))
    # picture
    x = xs[1]
    out.append(rect(x - s * 0.45, y - s * 0.35, s * 0.9, s * 0.7, rx=s * 0.06, fill='none', stroke=color,
                    stroke_width=sw))
    out.append(path('M%s %s l%s %s l%s %s l%s %s' % (f(x - s * 0.36), f(y + s * 0.25), f(s * 0.25), f(-s * 0.28),
                                                     f(s * 0.18), f(s * 0.16), f(s * 0.3), f(-s * 0.26)),
                    fill='none', stroke=color, stroke_width=sw))
    out.append(circle(x + s * 0.2, y - s * 0.14, s * 0.07, fill=color))
    # eye
    x = xs[2]
    out.append(path('M%s %s q%s %s %s 0 q%s %s %s 0 z' % (f(x - s * 0.48), f(y), f(s * 0.48), f(-s * 0.46), f(s * 0.96),
                                                         f(-s * 0.48), f(s * 0.46), f(-s * 0.96)),
                    fill='none', stroke=color, stroke_width=sw))
    out.append(circle(x, y, s * 0.15, fill='none', stroke=color, stroke_width=sw))
    # gear
    x = xs[3]
    teeth = []
    for k in range(8):
        a = k * math.pi / 4
        teeth.append(line(x + math.cos(a) * s * 0.3, y + math.sin(a) * s * 0.3, x + math.cos(a) * s * 0.46,
                          y + math.sin(a) * s * 0.46, stroke=color, stroke_width=sw * 1.6, stroke_linecap='round'))
    out += teeth
    out.append(circle(x, y, s * 0.3, fill='none', stroke=color, stroke_width=sw))
    out.append(circle(x, y, s * 0.12, fill='none', stroke=color, stroke_width=sw))
    if labels:
        for xx, lab in zip(xs, ('Anruf', 'Nachricht', 'Livebild', 'Einstellungen')):
            out.append(text(xx, y + s * 1.05, lab, size=lab_size or s * 0.36, fill=lab_color or color,
                            anchor='middle'))
    return ''.join(out)


def _left_tab(D, x, y, r, fill='#FFFFFF', icon='#7C8088'):
    cid = D.clip('lefttab-%s' % f(r), rect(0, -r, r, 2 * r))
    return (('<g transform="translate(%s %s)"><circle cx="0" cy="0" r="%s" fill="%s" clip-path="%s"/>' % (
        f(x), f(y), f(r), fill, cid)) +
        circle(r * 0.42, -r * 0.08, r * 0.2, fill='none', stroke=icon, stroke_width=r * 0.07) +
        line(r * 0.34, r * 0.2, r * 0.5, r * 0.2, stroke=icon, stroke_width=r * 0.07) + '</g>')


def xdm10_monitor(D, color='white', room='2'):
    """XDM10 Innenstation 7'' (Weiß / Schwarz) – 190 × 138 mm, grüne Oberfläche."""
    W, H = 190.0, 138.0
    white = color == 'white'
    body = '#FFFFFF' if white else '#1D1E21'
    edge = '#CFD2D6' if white else '#0B0C0D'
    logo = '#55575C' if white else '#E6E7E9'
    key = '#A3A6AB' if white else '#8B8E93'
    sx, sy, sw, sh = 18.6, 15.6, 153.0, 92.0
    scr = D.lin('xdm-scr', [(0, '#0A3A20'), (0.45, '#0E5A31'), (1, '#0A4526')], x1=0, y1=0, x2=1, y2=0.3)
    clip = D.clip('xdm-scrclip', rect(sx, sy, sw, sh))
    out = [
        rect(0.4, 2.2, W - 0.8, H - 1.6, rx=6, fill='#000000', opacity=0.10),
        rect(0, 0, W, H - 1.2, rx=6, fill=body, stroke=edge, stroke_width=0.9),
        rect(1.6, 1.6, W - 3.2, H - 4.4, rx=4.8, fill='none', stroke='#FFFFFF' if white else '#34363A',
             stroke_width=0.6, opacity=0.9),
        text(W / 2, 10.2, 'METZLER', size=5.6, weight=700, fill=logo, anchor='middle', ls=0.9),
        rect(sx, sy, sw, sh, fill=scr),
        '<g clip-path="%s">' % clip,
        poly([(sx + sw * 0.46, sy), (sx + sw * 0.62, sy), (sx + sw * 0.35, sy + sh), (sx + sw * 0.19, sy + sh)],
             fill='#1D8A4E', opacity=0.18),
        poly([(sx + sw * 0.70, sy), (sx + sw * 0.79, sy), (sx + sw * 0.52, sy + sh), (sx + sw * 0.43, sy + sh)],
             fill='#23A05A', opacity=0.20),
        poly([(sx + sw * 0.86, sy), (sx + sw * 1.02, sy), (sx + sw * 0.8, sy + sh), (sx + sw * 0.64, sy + sh)],
             fill='#1B8448', opacity=0.22),
        '</g>',
    ]
    out.append(_left_tab(D, sx, sy + sh * 0.40, 7.2))
    tx = sx + 14.5
    out.append(text(tx, sy + sh * 0.37, '12:36', size=14, weight=500, fill='#FFFFFF'))
    bx, by = sx + sw * 0.47, sy + sh * 0.27
    out.append(circle(bx, by, 6.4, fill='#0A2A18'))
    out.append(path('M%s %s a3 3 0 0 1 6 0 v2.2 l1.1 1.4 h-8.2 l1.1 -1.4 z' % (f(bx - 3), f(by + 0.3)),
                    fill='none', stroke='#FFFFFF', stroke_width=0.7, transform='translate(0 -1.6)'))
    out.append(text(tx, sy + sh * 0.46, 'Donnerstag, 12.11.2025', size=3.3, fill='#DDF0E3'))
    out.append(text(tx, sy + sh * 0.535, 'Zimmernr.: %s' % room, size=3.3, fill='#DDF0E3'))
    out.append(_icon_row(sx, sy + sh * 0.705, sw, '#FFFFFF', 7.0, lab_size=2.7))
    for i in range(4):
        out.append(rect(sx + sw - 22 + i * 5.0, sy + 3.2, 2.8, 2.8, rx=0.5, fill='none', stroke='#FFFFFF',
                        stroke_width=0.4, opacity=0.75))
    # hardware keys (bottom bezel)
    ky = 124.5
    out.append(circle(14, ky, 0.9, fill=key))
    kx = [W / 2 - 23, W / 2, W / 2 + 23]
    out.append(path('M%s %s c-1 2 1 5 4 6 l1.2 -1.4 -2 -1.6 -1 1 c-1 -0.6 -1.8 -1.7 -2 -2.8 l1 -0.9 -1.5 -2.2 z' % (
        f(kx[0] - 2.4), f(ky - 3.2)), fill='none', stroke=key, stroke_width=0.6))
    out.append(circle(kx[1] - 4, ky, 1.8, fill='none', stroke=key, stroke_width=0.6))
    out.append(path('M%s %s h7 m-2 0 v1.6 m-2 -1.6 v1.2' % (f(kx[1] - 2.2), f(ky)), fill='none', stroke=key,
                    stroke_width=0.6))
    out.append(path('M%s %s q4.5 -3.2 9 0 l-1.3 1.3 -2 -0.6 v-1.1 q-1.2 -0.4 -2.4 0 v1.1 l-2 0.6 z' % (
        f(kx[2] - 4.5), f(ky + 0.6)), fill='none', stroke=key, stroke_width=0.6))
    for i, c in enumerate(('#7F9BDB', '#D77474', '#D77474')):
        out.append(circle(W - 34 + i * 7.2, ky, 1.5, fill='none', stroke=c, stroke_width=0.55))
    anchors = {'bottom': (W / 2, H - 1.2), 'top': (W / 2, 0), 'left': (0, H / 2), 'right': (W, H / 2),
               'b_in': (W / 2 - 8, H - 1.2), 'b_out': (W / 2 + 8, H - 1.2)}
    return Device(''.join(out), W, H, anchors, 'xdm10-is')


def vdm10_home(D, color='white', room='1'):
    """VDM10 / ADM10 Innenstation Home 7'' – 200 × 140 mm, rote Oberfläche."""
    W, H = 200.0, 140.0
    white = color == 'white'
    body = '#FFFFFF' if white else '#1B1C1F'
    edge = '#D3D6DA' if white else '#08090A'
    sx, sy, sw, sh = 21.0, 17.5, 158.0, 91.5
    scr = D.lin('vdm-scr', [(0, '#3F0508'), (0.5, '#8E0F16'), (1, '#44060A')], x1=0, y1=0, x2=1, y2=0.35)
    clip = D.clip('vdm-scrclip', rect(sx, sy, sw, sh))
    out = [rect(0.4, 2.2, W - 0.8, H - 1.6, rx=3.2, fill='#000000', opacity=0.10),
           rect(0, 0, W, H - 1.2, rx=3.2, fill=body, stroke=edge, stroke_width=0.9),
           rect(sx, sy, sw, sh, fill=scr),
           '<g clip-path="%s">' % clip]
    for k in range(9):
        yy = sy + sh * (0.30 + k * 0.055)
        out.append(path('M%s %s C%s %s %s %s %s %s S%s %s %s %s' % (
            f(sx - 5), f(yy + 12), f(sx + sw * 0.25), f(yy + 18), f(sx + sw * 0.40), f(yy - 20),
            f(sx + sw * 0.62), f(yy - 6), f(sx + sw * 0.9), f(yy + 10), f(sx + sw + 5), f(yy - 4)),
            fill='none', stroke='#FF3B45', stroke_width=0.35, opacity=0.35))
    out.append('</g>')
    if not white:
        out.append(poly([(W * 0.62, 0), (W, 0), (W, H * 0.55)], fill='#FFFFFF', opacity=0.05))
    out.append(text(sx + sw / 2, sy + 6.2, 'METZLER INTERCOM', size=2.7, weight=700, fill='#FFFFFF',
                    anchor='middle', ls=0.3))
    out.append(_left_tab(D, sx, sy + sh * 0.40, 7.0))
    tx = sx + 17
    out.append(text(tx, sy + sh * 0.33, '12:00', size=14.5, weight=400, fill='#FFFFFF'))
    out.append(text(tx, sy + sh * 0.43, '1-7-2025  Dienstag', size=3.1, fill='#F6D5D7'))
    out.append(text(tx, sy + sh * 0.50, 'Zimmernr.: %s' % room, size=3.1, fill='#F6D5D7'))
    out.append(circle(sx + sw * 0.885, sy + sh * 0.29, 6.8, fill='#FFFFFF'))
    cx, cy = sx + sw * 0.885, sy + sh * 0.29
    out.append(path('M%s %s h1.6 l2.4 -2 v6 l-2.4 -2 h-1.6 z' % (f(cx - 3), f(cy - 1)), fill='none',
                    stroke='#5A5C60', stroke_width=0.5))
    out.append(path('M%s %s q1.2 1.5 0 3' % (f(cx + 1.6), f(cy - 1.5)), fill='none', stroke='#5A5C60',
                    stroke_width=0.5))
    out.append(_icon_row(sx, sy + sh * 0.705, sw, '#FFFFFF', 7.0, lab_size=2.7))
    for i in range(4):
        out.append(rect(sx + sw - 24 + i * 5.6, sy + 3.0, 3.2, 3.2, rx=0.5, fill='none', stroke='#FFFFFF',
                        stroke_width=0.45, opacity=0.9))
    out.append(text(W / 2, 128.2, 'METZLER', size=5.6, weight=700, fill='#A7AAAF' if white else '#C9CBCE',
                    anchor='middle', ls=0.9))
    out.append(circle(W - 12, 130, 0.9, fill='#8A8D92'))
    anchors = {'bottom': (W / 2, H - 1.2), 'top': (W / 2, 0), 'left': (0, H / 2), 'right': (W, H / 2)}
    return Device(''.join(out), W, H, anchors, 'vdm10-home')


def vdm10_pro(D, room='1'):
    """VDM10 Innenstation Pro 7'' – 180 × 140 mm, Glas schwarz + Aluminium grau, Sensortaste."""
    W, H = 180.0, 140.0
    alu = D.lin('pro-alu', [(0, '#B9BDC3'), (0.5, '#A2A7AE'), (1, '#8F959C')])
    sx, sy, sw, sh = 8.0, 7.5, 164.0, 92.0
    scr = D.lin('vdm-scr', [(0, '#3F0508'), (0.5, '#8E0F16'), (1, '#44060A')], x1=0, y1=0, x2=1, y2=0.35)
    clip = D.clip('pro-clip', rect(0, 0, W, H - 1.2, rx=4))
    out = [rect(0.4, 2.2, W - 0.8, H - 1.6, rx=4, fill='#000000', opacity=0.12),
           '<g clip-path="%s">' % clip,
           rect(0, 0, W, H, fill='#0B0B0C'),
           rect(0, 105, W, H - 105, fill=alu),
           line(0, 105, W, 105, stroke='#6E737A', stroke_width=0.5),
           '</g>',
           rect(0, 0, W, H - 1.2, rx=4, fill='none', stroke='#050505', stroke_width=0.8),
           rect(sx, sy, sw, sh, fill=scr)]
    out.append(text(sx + sw / 2, sy + 6.2, 'METZLER INTERCOM', size=2.7, weight=700, fill='#FFFFFF',
                    anchor='middle', ls=0.3))
    out.append(_left_tab(D, sx, sy + sh * 0.42, 7.0))
    out.append(text(sx + 16, sy + sh * 0.34, '12:00', size=14.5, fill='#FFFFFF'))
    out.append(text(sx + 16, sy + sh * 0.44, '1-7-2025  Dienstag', size=3.1, fill='#F6D5D7'))
    out.append(text(sx + 16, sy + sh * 0.51, 'Zimmernr.: %s' % room, size=3.1, fill='#F6D5D7'))
    out.append(circle(sx + sw * 0.885, sy + sh * 0.30, 6.8, fill='#FFFFFF'))
    out.append(_icon_row(sx, sy + sh * 0.715, sw, '#FFFFFF', 7.0, lab_size=2.7))
    out.append(poly([(W * 0.55, 0), (W * 0.78, 0), (W * 0.40, 105), (W * 0.18, 105)], fill='#FFFFFF', opacity=0.05))
    # key sensor on aluminium strip
    kx, ky = W / 2, 122.5
    out.append(circle(kx - 5, ky, 2.6, fill='none', stroke='#FFFFFF', stroke_width=0.9))
    out.append(path('M%s %s h9 m-2.5 0 v2.2 m-2.6 -2.2 v1.6' % (f(kx - 2.4), f(ky)), fill='none', stroke='#FFFFFF',
                    stroke_width=0.9))
    anchors = {'bottom': (W / 2, H - 1.2), 'top': (W / 2, 0), 'left': (0, H / 2), 'right': (W, H / 2)}
    return Device(''.join(out), W, H, anchors, 'vdm10-pro')


def vdm10_ultra(D, room='1'):
    """VDM10 Innenstation Ultra 10,1'' – 254 × 166 mm, schwarz."""
    W, H = 254.0, 166.0
    sx, sy, sw, sh = 12.0, 11.0, 230.0, 132.0
    scr = D.lin('vdm-scr', [(0, '#3F0508'), (0.5, '#8E0F16'), (1, '#44060A')], x1=0, y1=0, x2=1, y2=0.35)
    clip = D.clip('ultra-clip', rect(sx, sy, sw, sh))
    out = [rect(0.4, 2.2, W - 0.8, H - 1.6, rx=4, fill='#000000', opacity=0.12),
           rect(0, 0, W, H - 1.2, rx=4, fill='#1B1C1F', stroke='#070708', stroke_width=0.9),
           rect(sx, sy, sw, sh, fill=scr), '<g clip-path="%s">' % clip]
    for k in range(10):
        yy = sy + sh * (0.30 + k * 0.05)
        out.append(path('M%s %s C%s %s %s %s %s %s S%s %s %s %s' % (
            f(sx - 5), f(yy + 16), f(sx + sw * 0.25), f(yy + 24), f(sx + sw * 0.40), f(yy - 26),
            f(sx + sw * 0.62), f(yy - 8), f(sx + sw * 0.9), f(yy + 14), f(sx + sw + 5), f(yy - 6)),
            fill='none', stroke='#FF3B45', stroke_width=0.45, opacity=0.35))
    out.append('</g>')
    out.append(poly([(W * 0.58, 0), (W, 0), (W, H * 0.5)], fill='#FFFFFF', opacity=0.05))
    out.append(text(sx + sw / 2, sy + 8.5, 'METZLER INTERCOM', size=3.6, weight=700, fill='#FFFFFF',
                    anchor='middle', ls=0.4))
    out.append(_left_tab(D, sx, sy + sh * 0.42, 9.5))
    out.append(text(sx + 24, sy + sh * 0.33, '12:00', size=21, fill='#FFFFFF'))
    out.append(text(sx + 24, sy + sh * 0.43, '1-7-2025  Dienstag', size=4.4, fill='#F6D5D7'))
    out.append(text(sx + 24, sy + sh * 0.50, 'Zimmernr.: %s' % room, size=4.4, fill='#F6D5D7'))
    out.append(circle(sx + sw * 0.885, sy + sh * 0.29, 9.5, fill='#FFFFFF'))
    out.append(_icon_row(sx, sy + sh * 0.705, sw, '#FFFFFF', 10.0, lab_size=3.8))
    out.append(circle(W - 12, H - 7, 1.0, fill='#77797E'))
    anchors = {'bottom': (W / 2, H - 1.2), 'top': (W / 2, 0), 'left': (0, H / 2), 'right': (W, H / 2)}
    return Device(''.join(out), W, H, anchors, 'vdm10-ultra')


# ================================================================= DOOR STATIONS
def xdm10_maxior(D, names=('Vossmann',)):
    """XDM10 MAXIOR Türstation – 135 × 293 mm, Glasfront schwarz, Namensschilder austauschbar."""
    W, H = 135.0, 293.0
    glass_h = 163.0
    glass = D.lin('max-glass', [(0, '#1B1C1F'), (0.45, '#070708'), (1, '#0F1012')], x1=0, y1=0, x2=0.4, y2=1)
    lower = D.lin('max-low', [(0, '#35363A'), (1, '#27282B')], x1=0, y1=0, x2=1, y2=1)
    tag = D.lin('max-tag', [(0, '#FBFBFC'), (0.5, '#E4E6E9'), (1, '#CFD2D6')])
    clip = D.clip('max-clip', rect(0, 0, W, H, rx=6.5))
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, rx=6.5, fill='#000000', opacity=0.18),
           '<g clip-path="%s">' % clip,
           rect(0, 0, W, glass_h, fill=glass),
           poly([(W * 0.52, 0), (W * 0.83, 0), (W * 0.38, glass_h), (W * 0.10, glass_h)], fill='#FFFFFF',
                opacity=0.045),
           rect(0, glass_h, W, H - glass_h, fill=lower),
           rect(0, glass_h, W, 3.6, fill=steel(D)),
           line(29, glass_h + 3.6, 29, H, stroke='#1C1D20', stroke_width=0.9),
           line(29.9, glass_h + 3.6, 29.9, H, stroke='#404145', stroke_width=0.5),
           line(106, glass_h + 3.6, 106, H, stroke='#1C1D20', stroke_width=0.9),
           line(106.9, glass_h + 3.6, 106.9, H, stroke='#404145', stroke_width=0.5),
           '</g>',
           rect(0, 0, W, H, rx=6.5, fill='none', stroke='#0A0A0B', stroke_width=0.8)]
    # status icons (phone, mic, lock open, lock closed)
    ic = '#6D7075'
    ix, iy = 33.0, 44.0
    out.append(path('M%s %s c-0.3 1.5 0.9 3 2.3 3.2 l0.5 -0.8 -1 -0.8 -0.5 0.4 c-0.5 -0.3 -0.8 -0.8 -0.9 -1.3 l0.5 -0.4 -0.7 -1 z' % (
        f(ix - 1), f(iy - 1.6)), fill=ic))
    out.append(rect(ix + 5.2, iy - 1.8, 1.3, 2.4, rx=0.6, fill=ic))
    out.append(path('M%s %s q0 1.6 1.65 1.6 q1.65 0 1.65 -1.6' % (f(ix + 4.2), f(iy - 0.4)), fill='none', stroke=ic,
                    stroke_width=0.35))
    for k, closed in ((0, True), (1, False)):
        lx = ix + 11 + k * 6
        out.append(rect(lx - 1.3, iy - 0.8, 2.6, 2.1, rx=0.3, fill=ic))
        out.append(path('M%s %s v-0.9 a1 1 0 0 1 2 0%s' % (f(lx - 1), f(iy - 0.8), ' v0.9' if closed else ''),
                        fill='none', stroke=ic, stroke_width=0.4))
    out.append(circle(32, 55, 1.5, fill='#1E1F22', stroke='#3F4145', stroke_width=0.4))
    cx, cy = W / 2, 70.0
    out.append(circle(cx, cy, 8.8, fill='#0D0E10', stroke='#33353A', stroke_width=0.7))
    out.append(circle(cx, cy, 6.0, fill='#17191C', stroke='#4A4D52', stroke_width=0.6))
    out.append(circle(cx, cy, 3.6, fill=D.rad('max-lens', [(0, '#5B6878'), (0.6, '#222833'), (1, '#0C0E12')])))
    out.append(circle(cx - 1.2, cy - 1.2, 1.0, fill='#A7B3C2', opacity=0.8))
    out.append(rect(cx - 7.5, 94, 15, 1.9, rx=0.95, fill='#26272A', stroke='#4B4C50', stroke_width=0.4))
    out.append(metzler_logo(D, cx, 157.5, 3.9, fill='#6C6E72'))
    n = len(names)
    ys = {1: [212.0], 2: [200.0, 228.0], 3: [196.0, 225.5, 255.0]}[n]
    for nm, ty in zip(names, ys):
        out.append(rect(36.5, ty - 5.6, 62, 11.2, rx=0.8, fill=tag, stroke='#B4B8BD', stroke_width=0.4))
        out.append(text(W / 2, ty + 1.9, nm, size=5.4, fill='#1A1A1C', anchor='middle', ls=0.15))
    out.append(circle(W / 2, 272, 0.9, fill='#141517'))
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 230), 'right': (W, 230),
               'bus': (W / 2 - 14, H), 'rs485': (W / 2 + 14, H)}
    return Device(''.join(out), W, H, anchors, 'xdm10-maxior')


def vdm10_colson(D, name='VOSSBERG', buttons=None):
    """VDM10 2.0 Colson Türstation – anthrazit, Kamera-Band, gravierter Name, Leuchttaster."""
    W, H = 135.0, 267.0
    plate = D.lin('col-plate', [(0, '#343D49'), (0.5, '#232A33'), (1, '#2E3641')], x1=0, y1=0, x2=1, y2=0)
    band = D.lin('col-band', [(0, '#1C1D20'), (0.5, '#0C0D0F'), (1, '#1A1B1E')])
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=plate, stroke='#15191E', stroke_width=0.8),
           rect(0, 9, W, 1.4, fill=steel(D)),
           rect(0, H - 13, W, 1.4, fill=steel(D)),
           rect(0, 38, W, 46, fill=band),
           line(0, 38, W, 38, stroke='#475160', stroke_width=0.5),
           line(0, 84, W, 84, stroke='#475160', stroke_width=0.5)]
    cx, cy = W / 2, 61.0
    out.append(circle(cx, cy, 18, fill='#0A0B0D', stroke='#2A2D31', stroke_width=0.6))
    for r, n, op in ((16.2, 64, 0.9), (13.8, 56, 0.75), (11.6, 48, 0.55)):
        out.append(circle(cx, cy, r, fill='none', stroke='#D9DDE2', stroke_width=0.9,
                          stroke_dasharray='%s %s' % (f(2 * math.pi * r / n * 0.42), f(2 * math.pi * r / n * 0.58)),
                          opacity=op))
    out.append(circle(cx, cy, 9.5, fill='#050607', stroke='#33363B', stroke_width=0.6))
    out.append(circle(cx, cy, 6.2, fill=D.rad('col-lens', [(0, '#5D6A7B'), (0.55, '#1C212A'), (1, '#07080A')])))
    out.append(circle(cx - 2, cy - 2, 1.4, fill='#B8C4D2', opacity=0.75))
    out.append(path('M%s %s a8 8 0 0 1 6 0' % (f(cx - 3), f(cy - 7.4)), fill='none', stroke='#3FBF6B',
                    stroke_width=0.8))
    for k in range(2):
        out.append(rect(cx - 19, 88.5 + k * 3, 38, 1.5, rx=0.75, fill='#15181C', stroke='#434B56', stroke_width=0.3))
    out.append(text(cx, 105.5, name, size=7.2, fill='#D4D9E0', anchor='middle', ls=3.4, weight=300))
    out.append(line(0, 112, W, 112, stroke='#3A4350', stroke_width=0.5))
    if not buttons:
        by = 222.0
        out.append(circle(cx, by, 9.6, fill=steel(D, 'st-ring')))
        out.append(circle(cx, by, 7.4, fill='#FFFFFF', opacity=0.95))
        out.append(circle(cx, by, 5.9, fill=D.rad('col-btn', [(0, '#F1F3F5'), (0.7, '#C9CDD2'), (1, '#9AA0A7')])))
    else:
        for i, nm in enumerate(buttons):
            by = 150 + i * 26
            out.append(circle(30, by, 8.2, fill=steel(D, 'st-ring')))
            out.append(circle(30, by, 6.3, fill='#FFFFFF', opacity=0.95))
            out.append(circle(30, by, 5.0, fill=D.rad('col-btn', [(0, '#F1F3F5'), (0.7, '#C9CDD2'), (1, '#9AA0A7')])))
            out.append(rect(46, by - 7, 80, 14, fill='none', stroke='#3D4653', stroke_width=0.5))
            out.append(text(86, by + 2, nm, size=5.6, fill='#D4D9E0', anchor='middle', ls=0.6))
    out.append(metzler_logo(D, cx, H - 4.2, 3.4, fill='#B7BDC6', text_fill='#C5CAD2'))
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 190), 'right': (W, 190),
               'bus': (W / 2 - 14, H), 'rs485': (W / 2 + 14, H)}
    return Device(''.join(out), W, H, anchors, 'vdm10-colson')


def _sdm_display(D, gx, gy, gw, gh, seed=7):
    """SDM10 glass front with portrait touch UI (08:35, Netzwerk-Hintergrund, Rezeption/Büros/PIN-Code)."""
    sx, sy = gx + gw * 0.103, gy + gh * 0.174
    sw, sh = gw * 0.794, gh * 0.684
    disp = D.lin('sdm-disp', [(0, '#0A1426'), (0.55, '#1B3963'), (1, '#0B1528')])
    clip = D.clip('sdm-clip-%d-%d' % (int(gx), int(gy)), rect(sx, sy, sw, sh))
    k = sw / 108.0
    out = [rect(gx - 2 * k, gy - 2 * k, gw + 4 * k, gh + 4 * k, fill='#1A2027', stroke='#3A4350', stroke_width=0.6),
           rect(gx, gy, gw, gh, fill='#07090C'),
           poly([(gx + gw * 0.55, gy), (gx + gw * 0.8, gy), (gx + gw * 0.25, gy + gh), (gx, gy + gh)], fill='#FFFFFF',
                opacity=0.04),
           rect(sx, sy, sw, sh, fill=disp), '<g clip-path="%s">' % clip]
    import random
    rnd = random.Random(seed)
    pts = [(sx + rnd.random() * sw, sy + sh * (0.38 + rnd.random() * 0.34)) for _ in range(34)]
    for i, (px, py) in enumerate(pts):
        for qx, qy in pts[i + 1:i + 3]:
            if abs(px - qx) < 30 * k:
                out.append(line(px, py, qx, qy, stroke='#8FB7F0', stroke_width=0.25 * k, opacity=0.5))
        out.append(circle(px, py, (0.55 + rnd.random() * 0.6) * k, fill='#DCE9FF', opacity=0.85))
    out.append('</g>')
    out.append(text(sx + 6 * k, sy + 16 * k, '08:35', size=11 * k, weight=700, fill='#FFFFFF'))
    out.append(text(sx + 45 * k, sy + 11.5 * k, '01.02.2024', size=2.7 * k, fill='#DCE6F5'))
    out.append(text(sx + 45 * k, sy + 15.2 * k, 'Donnerstag', size=2.7 * k, fill='#DCE6F5'))
    for (bx, by, bw, lab) in ((sx + 3 * k, sy + 124 * k, sw - 6 * k, 'Rezeption'),
                              (sx + 3 * k, sy + 146 * k, sw / 2 - 4.5 * k, 'Büros'),
                              (sx + sw / 2 + 1.5 * k, sy + 146 * k, sw / 2 - 4.5 * k, '••• PIN-Code')):
        out.append(rect(bx, by, bw, 18 * k, rx=1.2 * k, fill='#2B3441', opacity=0.92))
        out.append(text(bx + bw / 2, by + 11.3 * k, lab, size=3.6 * k, fill='#FFFFFF', anchor='middle'))
    for j, fx in enumerate((0.13, 0.28, 0.43, 0.57, 0.72, 0.87)):
        out.append(circle(gx + gw * fx, gy + gh * 0.117, (3.2 if j in (0, 5) else 1.6) * k, fill='#15181D',
                          stroke='#2F343B', stroke_width=0.4))
    out.append(metzler_logo(D, gx + gw / 2, gy + gh - 12 * k, 5.0 * k, fill='#E6E8EB'))
    return ''.join(out)


def _sdm_plate(D):
    return D.lin('sdm-plate', [(0, '#303843'), (0.5, '#222931'), (1, '#2D353F')], x1=0, y1=0, x2=1, y2=0)


def sdm10x(D):
    """SDM10X Türstation mit Gesichtserkennung – 194 × 330 mm, Touch-Display hochkant."""
    W, H = 194.0, 330.0
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=_sdm_plate(D), stroke='#141920', stroke_width=0.8),
           _sdm_display(D, 29.0, 40.0, 136.0, 247.0)]
    for side in (6.0, W - 6.0):
        for k in range(4):
            out.append(rect(side - 1.2, 176 + k * 5.2, 2.4, 3.2, rx=0.6, fill='#0E1216'))
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 200), 'right': (W, 200),
               'pwr': (W / 2 - 18, H), 'lan': (W / 2, H), 'rs485': (W / 2 + 18, H)}
    return Device(''.join(out), W, H, anchors, 'sdm10x')


def sdm10h(D, number='25'):
    """SDM10H – 180 × 445 mm, beleuchtete Hausnummer + Touch-Display."""
    W, H = 180.0, 445.0
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=_sdm_plate(D), stroke='#141920', stroke_width=0.8)]
    for sw_, col, op in ((5.0, '#3E7BFF', 0.30), (2.6, '#7FA9FF', 0.55), (1.2, '#E6EFFF', 1.0)):
        out.append(text(W / 2, 118, number, size=86, weight=700, fill='#1E2632' if sw_ == 1.2 else 'none',
                        stroke=col, stroke_width=sw_, opacity=op, anchor='middle', ls=-2))
    out.append(line(W * 0.2, 128, W * 0.8, 128, stroke='#9BBDFF', stroke_width=1.6, opacity=0.9))
    out.append(circle(W / 2, 14, 0.9, fill='#11161C'))
    out.append(circle(W / 2, 172, 0.9, fill='#11161C'))
    out.append(_sdm_display(D, 26.0, 190.0, 128.0, 232.0, seed=9))
    for side in (6.0, W - 6.0):
        for k in range(4):
            out.append(rect(side - 1.2, 300 + k * 5.2, 2.4, 3.2, rx=0.6, fill='#0E1216'))
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 300), 'right': (W, 300),
               'pwr': (W / 2 - 18, H), 'lan': (W / 2, H), 'rs485': (W / 2 + 18, H)}
    return Device(''.join(out), W, H, anchors, 'sdm10h')


def sdm10s(D, number='25', street='Kühlwetterstraße'):
    """SDM10S Video-Türsprechsäule (Stele) – 200 × 1600 mm, Display oben, Straßenname senkrecht."""
    W, H = 200.0, 1600.0
    out = [rect(-24, H - 30, W + 48, 30, rx=4, fill='#1B2027'),
           rect(3, 6, W - 3, H - 36, fill='#000000', opacity=0.16),
           rect(0, 0, W, H - 30, fill=_sdm_plate(D), stroke='#141920', stroke_width=1.2),
           _sdm_display(D, 26.0, 26.0, 148.0, 268.0, seed=11),
           text(W / 2, 420, number, size=96, weight=700, fill='#F2F4F7', anchor='middle', ls=-2),
           '<g transform="translate(%s %s) rotate(-90)">%s</g>' % (
               f(W / 2 + 34), f(1480), text(0, 0, street, size=104, weight=500, fill='#F2F4F7'))]
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 900), 'right': (W, 900),
               'pwr': (W / 2 - 30, H), 'lan': (W / 2, H), 'rs485': (W / 2 + 30, H)}
    return Device(''.join(out), W, H, anchors, 'sdm10s')


# ================================================================= DIN-RAIL MODULES
def _din_body(D, W, H, name):
    """White DIN distributor housing (top ridge, raised front, bottom ridge, red DIN clip)."""
    ridge = D.lin('din-ridge', [(0, '#F7F8F9'), (1, '#E3E6E9')])
    front = D.lin('din-front', [(0, '#FFFFFF'), (1, '#F1F2F4')])
    return ''.join([
        rect(1.2, 2.8, W - 1.2, H - 1.4, rx=1.6, fill='#000000', opacity=0.12),
        rect(0, 0, W, H, rx=1.6, fill=ridge, stroke='#C9CDD2', stroke_width=0.6),
        rect(4, 19.5, W - 8, H - 41, rx=1.4, fill=front, stroke='#D8DBDF', stroke_width=0.5),
        line(4, 19.5, W - 4, 19.5, stroke='#C5C9CE', stroke_width=0.45),
        line(4, H - 21.5, W - 4, H - 21.5, stroke='#C5C9CE', stroke_width=0.45),
        rect(W / 2 - 6, H - 0.2, 12, 2.6, rx=1.0, fill='#C23B30'),
    ])


def dist_vdm10_vt6(D):
    """VDM10-VT6-2.0 · 2-Draht Video-/Audioverteiler (6 Kanäle, LAN, 24 VDC) – 144 × 90 mm."""
    W, H = 144.0, 90.0
    lab = '#5E6166'
    out = [_din_body(D, W, H, 'vt6')]
    out += [plug2(16, 8.2), plug2(29, 8.2)]
    out += [text(16, 15.6, 'IN', size=2.6, fill=lab, anchor='middle'),
            text(29, 15.6, 'OUT', size=2.6, fill=lab, anchor='middle')]
    out.append(rect(55, 4.8, 84, 7, rx=3.5, fill='none', stroke='#9EA3A9', stroke_width=0.4))
    xs = [62.5 + i * 12.1 for i in range(6)]
    for i, x in enumerate(xs):
        out.append(plug2(x, 8.2, w=9.2))
        out.append(text(x, 15.6, 'CH%d' % (i + 1), size=2.6, fill=lab, anchor='middle'))
        out.append(text(x, 3.7, '−  +', size=1.9, fill=lab, anchor='middle'))
    out.append(text(57.2, 7.4, 'MAX', size=1.35, fill=lab))
    out.append(text(57.2, 9.3, '6W', size=1.35, fill=lab))
    out.append(text(135.4, 7.4, 'MAX', size=1.35, fill=lab))
    out.append(text(135.4, 9.3, '16W', size=1.35, fill=lab))
    out.append(circle(11, 27, 1.1, fill='#B9BDC2'))
    out.append(text(14, 28, 'POWER', size=2.6, fill='#8A8E94'))
    out.append(metzler_logo(D, W / 2 - 4, 47, 6.2, fill='#6A6C70'))
    out.append(circle(113, 45.8, 1.1, fill='#B9BDC2'))
    out.append(text(116, 46.8, 'RESET', size=2.6, fill='#8A8E94'))
    out.append(rj45(12, H - 8.5, w=8.6, h=7.0))
    out.append(text(12, H - 14.2, 'LAN', size=2.4, fill=lab, anchor='middle'))
    for x, t in ((34, 'IN'), (42.5, 'OUT')):
        out.append(text(x, H - 13.5, t, size=2.2, fill=lab, anchor='middle'))
        out.append(circle(x, H - 8.8, 1.1, fill='#4B4E53'))
    for i in range(6):
        x = 55 + i * 8.6
        out.append(text(x, H - 13.5, 'CH%d' % (i + 1), size=2.2, fill=lab, anchor='middle'))
        out.append(circle(x, H - 8.8, 1.1, fill='#4B4E53'))
    out.append(text(118, H - 13.5, '+  −', size=2.6, fill=lab, anchor='middle'))
    out.append(plug2(118, H - 8.8, w=8.8, h=4.2))
    out.append(text(124.5, H - 7.4, '24 VDC', size=2.5, fill=lab))
    anchors = {'IN': (16, 3.9), 'OUT': (29, 3.9), 'PWR': (118, H - 6.2), 'LAN': (12, H)}
    for i, x in enumerate(xs):
        anchors['CH%d' % (i + 1)] = (x, 3.9)
    return Device(''.join(out), W, H, anchors, 'vt6')


def dist_xdm10_6ch(D):
    """XDM10 2-Draht-BUS Verteiler (Set „8 Anschlüsse“: IN, OUT, CH1–CH6, 48 VDC) – 144 × 92 mm."""
    W, H = 144.0, 92.0
    lab = '#5E6166'
    out = [_din_body(D, W, H, 'x6')]
    out += [plug2(16, 8.2), plug2(29, 8.2)]
    out += [text(16, 15.6, 'IN', size=2.6, fill=lab, anchor='middle'),
            text(29, 15.6, 'OUT', size=2.6, fill=lab, anchor='middle')]
    out.append(rect(55, 4.8, 84, 7, rx=3.5, fill='none', stroke='#9EA3A9', stroke_width=0.4))
    xs = [62.5 + i * 12.1 for i in range(6)]
    for i, x in enumerate(xs):
        out.append(plug2(x, 8.2, w=9.2))
        out.append(text(x, 15.6, 'CH%d' % (i + 1), size=2.6, fill=lab, anchor='middle'))
    out.append(circle(11, 27, 1.1, fill='#B9BDC2'))
    out.append(text(14, 28, 'POWER', size=2.6, fill='#8A8E94'))
    out.append(metzler_logo(D, W / 2 - 4, 48, 6.2, fill='#6A6C70'))
    out.append(circle(113, 46.8, 1.1, fill='#B9BDC2'))
    out.append(text(116, 47.8, 'RESET', size=2.6, fill='#8A8E94'))
    for x, t in ((30, 'IN'), (39, 'OUT')):
        out.append(text(x, H - 13.5, t, size=2.2, fill=lab, anchor='middle'))
        out.append(circle(x, H - 8.8, 1.1, fill='#4B4E53'))
    for i in range(6):
        x = 53 + i * 9.0
        out.append(text(x, H - 13.5, 'CH%d' % (i + 1), size=2.2, fill=lab, anchor='middle'))
        out.append(circle(x, H - 8.8, 1.1, fill='#4B4E53'))
    out.append(text(118, H - 13.5, '+  −', size=2.6, fill=lab, anchor='middle'))
    out.append(plug2(118, H - 8.8, w=8.8, h=4.2))
    out.append(text(124.5, H - 7.4, '48 VDC', size=2.5, fill=lab))
    anchors = {'IN': (16, 3.9), 'OUT': (29, 3.9), 'PWR': (118, H - 6.2)}
    for i, x in enumerate(xs):
        anchors['CH%d' % (i + 1)] = (x, 3.9)
    return Device(''.join(out), W, H, anchors, 'x6')


def dist_xdm10_vt4(D):
    """XDM10-VT4 · 2-Draht Video-/Audioverteiler (4 Kanäle, 48 VDC) – 144 × 90 mm."""
    W, H = 144.0, 90.0
    lab = '#5E6166'
    out = [_din_body(D, W, H, 'vt4')]
    out += [plug2(15, 8.2), plug2(27, 8.2), plug2(52, 8.2), plug2(64, 8.2)]
    out.append(rect(78, 4.8, 61, 7, rx=3.5, fill='none', stroke='#9EA3A9', stroke_width=0.4))
    xs = [86 + i * 12.6 for i in range(4)]
    for i, x in enumerate(xs):
        out.append(plug2(x, 8.2, w=9.2))
        out.append(text(x, 15.6, 'CH%d' % (i + 1), size=2.6, fill=lab, anchor='middle'))
    out.append(text(133.6, 7.4, 'MAX', size=1.35, fill=lab))
    out.append(text(133.6, 9.3, '30W', size=1.35, fill=lab))
    out.append(circle(11, 27, 1.1, fill='#B9BDC2'))
    out.append(text(14, 28, 'POWER', size=2.6, fill='#8A8E94'))
    out.append(metzler_logo(D, W / 2 - 4, 47, 6.2, fill='#6A6C70'))
    out.append(circle(113, 45.8, 1.1, fill='#B9BDC2'))
    out.append(text(116, 46.8, 'RESET', size=2.6, fill='#8A8E94'))
    for x in (18, 26, 38, 46):
        out.append(circle(x, H - 8.8, 1.1, fill='#4B4E53'))
    for i in range(4):
        x = 60 + i * 9.5
        out.append(text(x, H - 13.5, 'CH%d' % (i + 1), size=2.2, fill=lab, anchor='middle'))
        out.append(circle(x, H - 8.8, 1.1, fill='#4B4E53'))
    out.append(text(118, H - 13.5, '+  −', size=2.6, fill=lab, anchor='middle'))
    out.append(plug2(118, H - 8.8, w=8.8, h=4.2))
    out.append(text(124.5, H - 7.4, '48 VDC', size=2.5, fill=lab))
    anchors = {'PWR': (118, H - 6.2)}
    for i, x in enumerate(xs):
        anchors['CH%d' % (i + 1)] = (x, 3.9)
    return Device(''.join(out), W, H, anchors, 'vt4')


def meanwell_hdr30(D, volts='24', amps='1.5', watts='36', model=None):
    """MEAN WELL HDR-30 Hutschienennetzteil (35 × 90 mm), wie in den Metzler-Sets."""
    W, H = 35.0, 90.0
    body = D.lin('mw-body', [(0, '#3A3C40'), (0.5, '#2B2D30'), (1, '#222427')], x1=0, y1=0, x2=1, y2=0)
    out = [rect(1.0, 2.5, W - 1.0, H - 1.0, rx=1.2, fill='#000000', opacity=0.16),
           rect(0, 0, W, H, rx=1.2, fill=body, stroke='#151618', stroke_width=0.6),
           rect(3, 14, W - 6, H - 28, rx=0.8, fill='#303236', stroke='#1B1C1E', stroke_width=0.4),
           line(0, 14, W, 14, stroke='#1A1B1D', stroke_width=0.5),
           line(0, H - 14, W, H - 14, stroke='#1A1B1D', stroke_width=0.5)]
    out += [screw_terminal(10.5, 7, 2.4), screw_terminal(24.5, 7, 2.4)]
    out += [text(10.5, 12.6, '−V', size=2.2, fill='#C9CCD1', anchor='middle'),
            text(24.5, 12.6, '+V', size=2.2, fill='#C9CCD1', anchor='middle')]
    out.append(circle(5, 17.6, 1.5, fill='none', stroke='#9EA2A8', stroke_width=0.4))
    out.append(circle(30.5, 17.4, 0.9, fill='#47D16B'))
    out.append(rect(10.5, 23, 14, 8.5, rx=0.6, fill='none', stroke='#D5D8DC', stroke_width=0.5))
    out.append(text(17.5, 29.6, 'MW', size=5.2, weight=700, fill='#D5D8DC', anchor='middle', style='font-style:italic'))
    out.append(text(17.5, 35.5, 'MEAN WELL', size=2.6, weight=700, fill='#D5D8DC', anchor='middle'))
    out.append(text(17.5, 46, 'INPUT:', size=2.3, weight=700, fill='#C9CCD1', anchor='middle'))
    out.append(text(17.5, 49.3, '100-240VAC', size=2.3, fill='#C9CCD1', anchor='middle'))
    out.append(text(17.5, 57.5, 'OUTPUT:', size=2.3, weight=700, fill='#C9CCD1', anchor='middle'))
    out.append(text(17.5, 61.3, '%sV ⎓ %sA' % (volts, amps), size=2.9, weight=700, fill='#E6E8EB', anchor='middle'))
    out.append(text(17.5, 67.5, model or ('HDR-30-%s' % volts), size=2.3, fill='#9EA2A8', anchor='middle'))
    out += [screw_terminal(10.5, H - 7, 2.4), screw_terminal(24.5, H - 7, 2.4)]
    out += [text(10.5, H - 11.2, 'N', size=2.2, fill='#C9CCD1', anchor='middle'),
            text(24.5, H - 11.2, 'L', size=2.2, fill='#C9CCD1', anchor='middle')]
    anchors = {'V-': (10.5, 4.6), 'V+': (24.5, 4.6), 'N': (10.5, H - 4.6), 'L': (24.5, H - 4.6),
               'OUT': (17.5, 4.6), 'AC': (17.5, H - 4.6)}
    return Device(''.join(out), W, H, anchors, 'hdr30')


def meanwell_hdr150_48(D):
    """MEAN WELL HDR-150-48 (105 × 90 mm) – 48 V Transformator im XDM10-Set „8 Anschlüsse“."""
    W, H = 105.0, 90.0
    body = D.lin('mw-body', [(0, '#3A3C40'), (0.5, '#2B2D30'), (1, '#222427')], x1=0, y1=0, x2=1, y2=0)
    out = [rect(1.0, 2.5, W - 1.0, H - 1.0, rx=1.2, fill='#000000', opacity=0.16),
           rect(0, 0, W, H, rx=1.2, fill=body, stroke='#151618', stroke_width=0.6),
           line(0, 15, W, 15, stroke='#1A1B1D', stroke_width=0.5),
           line(0, H - 15, W, H - 15, stroke='#1A1B1D', stroke_width=0.5),
           rect(8, 20, W - 16, H - 40, rx=0.8, fill='#303236', stroke='#1B1C1E', stroke_width=0.4)]
    xs = [16, 27, 38, 49]
    for x in xs:
        out.append(screw_terminal(x, 7.5, 2.6))
    for x, t in zip(xs, ('−V', '−V', '+V', '+V')):
        out.append(text(x, 13.4, t, size=2.3, fill='#C9CCD1', anchor='middle'))
    out.append(circle(60, 7.5, 1.7, fill='none', stroke='#9EA2A8', stroke_width=0.45))
    out.append(text(66, 8.6, 'Vo Adj.', size=2.2, fill='#9EA2A8'))
    out.append(circle(94, 7.5, 1.0, fill='#47D16B'))
    out.append(rect(13, 26, 15, 9, rx=0.6, fill='none', stroke='#D5D8DC', stroke_width=0.5))
    out.append(text(20.5, 32.8, 'MW', size=5.6, weight=700, fill='#D5D8DC', anchor='middle', style='font-style:italic'))
    out.append(text(33, 32.8, 'HDR-150-48', size=5.0, weight=700, fill='#E6E8EB'))
    out.append(text(13, 42.5, 'INPUT: 100-240VAC 1.8A 50/60Hz', size=2.5, fill='#C9CCD1'))
    out.append(text(13, 47.5, 'OUTPUT: 48V ⎓ 3.2A  (153.6W)', size=2.5, weight=700, fill='#E6E8EB'))
    out.append(text(13, 52.5, 'MEAN WELL · DIN-rail power supply', size=2.3, fill='#9EA2A8'))
    for i, c in enumerate(('#C9CCD1',) * 4):
        out.append(rect(62 + i * 7, 57, 5.5, 5.5, rx=0.6, fill='none', stroke=c, stroke_width=0.35))
    out += [screw_terminal(22, H - 7.5, 2.6), screw_terminal(33, H - 7.5, 2.6)]
    out += [text(22, H - 12.2, 'N', size=2.3, fill='#C9CCD1', anchor='middle'),
            text(33, H - 12.2, 'L', size=2.3, fill='#C9CCD1', anchor='middle')]
    anchors = {'V-': (16, 4.9), 'V+': (49, 4.9), 'V-i': (27, 4.9), 'V+i': (38, 4.9), 'OUT': (32.5, 4.9),
               'N': (22, H - 4.9), 'L': (33, H - 4.9), 'AC': (27.5, H - 4.9)}
    return Device(''.join(out), W, H, anchors, 'hdr150')


def stockwerksverteiler(D, flipped=False):
    """Stockwerksverteiler 2-Draht (XDM10-VTS) – 70,6 × 60 mm, grüne Klemmen IN/OUT + CH1–CH4.

    flipped=True: um 180° gedreht montiert (CH1–CH4 oben, IN/OUT unten), Beschriftung lesbar.
    """
    W, H = 70.6, 60.0
    if flipped:
        out = [rect(-8.5, 17, 12, 13, rx=4, fill='#F4F5F6', stroke='#CDD1D5', stroke_width=0.5),
               circle(-3.2, 23.5, 2.6, fill='#FFFFFF', stroke='#C3C7CC', stroke_width=0.6),
               rect(W - 3.5, 17, 12, 13, rx=4, fill='#F4F5F6', stroke='#CDD1D5', stroke_width=0.5),
               circle(W + 3.2, 23.5, 2.6, fill='#FFFFFF', stroke='#C3C7CC', stroke_width=0.6),
               rect(0.8, 2.2, W - 0.8, H - 1, rx=3, fill='#000000', opacity=0.12),
               rect(0, 0, W, H, rx=3, fill='#FFFFFF', stroke='#CDD1D5', stroke_width=0.6),
               rect(12.6, 0, 45.5, 12.5, rx=1, fill='#232427')]
        xs = []
        for i in range(4):
            x0 = 13.7 + i * 11.0
            out.append(green_block(x0, 1.8, 2, pitch=5.08))
            xs.append(x0 + 5.08)
            out.append(text(x0 + 5.08, 18.2, 'CH%d' % (i + 1), size=2.1, fill='#A2A6AB', anchor='middle'))
            out.append(text(x0 + 5.08, 21.4, 'MAX20W', size=1.8, fill='#A2A6AB', anchor='middle'))
        out += [rect(34.6, H - 12.5, 23.5, 12.5, rx=1, fill='#232427'),
                green_block(35.7, H - 10.3, 2, pitch=5.08), green_block(46.4, H - 10.3, 2, pitch=5.08),
                text(40.8, H - 15.4, 'IN', size=2.6, fill='#A2A6AB', anchor='middle'),
                text(51.5, H - 15.4, 'OUT', size=2.6, fill='#A2A6AB', anchor='middle')]
        anchors = {'IN': (40.8, H), 'OUT': (51.5, H)}
        for i, x in enumerate(xs):
            anchors['CH%d' % (i + 1)] = (x, 0)
        return Device(''.join(out), W, H, anchors, 'vts')
    out = [rect(-8.5, 30, 12, 13, rx=4, fill='#F4F5F6', stroke='#CDD1D5', stroke_width=0.5),
           circle(-3.2, 36.5, 2.6, fill='#FFFFFF', stroke='#C3C7CC', stroke_width=0.6),
           rect(W - 3.5, 30, 12, 13, rx=4, fill='#F4F5F6', stroke='#CDD1D5', stroke_width=0.5),
           circle(W + 3.2, 36.5, 2.6, fill='#FFFFFF', stroke='#C3C7CC', stroke_width=0.6),
           rect(0.8, 2.2, W - 0.8, H - 1, rx=3, fill='#000000', opacity=0.12),
           rect(0, 0, W, H, rx=3, fill='#FFFFFF', stroke='#CDD1D5', stroke_width=0.6),
           rect(12.5, 0, 23.5, 12.5, rx=1, fill='#232427'),
           green_block(13.6, 1.8, 2, pitch=5.08), green_block(24.3, 1.8, 2, pitch=5.08),
           text(18.7, 17.8, 'IN', size=2.6, fill='#A2A6AB', anchor='middle'),
           text(29.4, 17.8, 'OUT', size=2.6, fill='#A2A6AB', anchor='middle'),
           rect(12.5, H - 12.5, 45.5, 12.5, rx=1, fill='#232427')]
    xs = []
    for i in range(4):
        x0 = 13.6 + i * 11.0
        out.append(green_block(x0, H - 10.3, 2, pitch=5.08))
        xs.append(x0 + 5.08)
        out.append(text(x0 + 5.08, H - 18.4, 'MAX20W', size=1.8, fill='#A2A6AB', anchor='middle'))
        out.append(text(x0 + 5.08, H - 15.2, 'CH%d' % (i + 1), size=2.1, fill='#A2A6AB', anchor='middle'))
    anchors = {'IN': (18.7, 0), 'OUT': (29.4, 0)}
    for i, x in enumerate(xs):
        anchors['CH%d' % (i + 1)] = (x, H)
    return Device(''.join(out), W, H, anchors, 'vts')


def sicherheitsmodul(D):
    """Metzler Sicherheitsmodul mit Hutschienenhalter – schwarz, 20 Schraubklemmen, POWER-LED."""
    W, H = 118.0, 76.0
    out = [rect(1.2, 2.8, W - 1.2, H - 1.4, rx=1.4, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, rx=1.4, fill='#18191B', stroke='#0A0A0B', stroke_width=0.6),
           rect(0, 0, W, 22, rx=1.4, fill='#1F2023'),
           rect(5, 2.2, 8, 3.6, fill='#2A2B2E')]
    xs = []
    for i in range(20):
        grp = 0 if i < 10 else 1
        x = 9.0 + i * 5.05 + grp * 3.0
        xs.append(x)
        out.append(rect(x - 2.1, 3.0, 4.2, 4.6, fill='#F2F3F5', stroke='#9EA3A9', stroke_width=0.25))
        out.append(text(x, 6.6, str(i + 1), size=2.6, fill='#1A1A1C', anchor='middle', weight=700))
        out.append(screw_terminal(x, 13.0, 1.9, body='#E9EBEE', slot='#6F7479'))
    out.append(rect(14, 24.5, W - 28, H - 28, rx=3, fill='#1C1D20', stroke='#2E3034', stroke_width=0.6))
    out.append(rect(22, 30, W - 44, H - 38, rx=4, fill='#131416', stroke='#D8DADD', stroke_width=0.7))
    out.append(circle(30, 36, 1.4, fill='#E0332B'))
    out.append(text(30, 41.2, 'POWER', size=2.1, fill='#C9CCD1', anchor='middle'))
    out.append(metzler_logo(D, W / 2 + 6, 38.6, 5.2, fill='#E9EAEC'))
    for r in range(4):
        out.append(line(27, 46 + r * 4.3, 55, 46 + r * 4.3, stroke='#8E9297', stroke_width=0.25))
        out.append(line(63, 46 + r * 4.3, 91, 46 + r * 4.3, stroke='#8E9297', stroke_width=0.25))
    out.append(rect(27, 44, 28, 17.2, fill='none', stroke='#8E9297', stroke_width=0.3))
    out.append(rect(63, 44, 28, 17.2, fill='none', stroke='#8E9297', stroke_width=0.3))
    circle_l = circle(6, H / 2 + 8, 2.6, fill='#8E9297', stroke='#5C6065', stroke_width=0.4)
    circle_r = circle(W - 6, H / 2 + 8, 2.6, fill='#8E9297', stroke='#5C6065', stroke_width=0.4)
    out += [circle_l, circle_r]
    anchors = {}
    for i, x in enumerate(xs):
        anchors['T%d' % (i + 1)] = (x, 0)
    return Device(''.join(out), W, H, anchors, 'sm')


def tueroeffner(D):
    """Elektrischer Türöffner (Schließblech, 12 V DC) – Frontansicht 26 × 110 mm."""
    W, H = 26.0, 110.0
    st = steel(D, 'strike', horizontal=False)
    out = [rect(0.8, 2, W - 0.8, H - 1, rx=1.5, fill='#000000', opacity=0.14),
           rect(0, 0, W, H, rx=1.5, fill=st, stroke='#8F959C', stroke_width=0.6),
           circle(W / 2, 8, 2.1, fill='#C7CBD0', stroke='#7D838A', stroke_width=0.5),
           circle(W / 2, H - 8, 2.1, fill='#C7CBD0', stroke='#7D838A', stroke_width=0.5),
           rect(6, 30, W - 12, 50, rx=1, fill='#5C6168', stroke='#3F444A', stroke_width=0.5),
           path('M%s %s h%s a4 4 0 0 1 0 8 h-%s z' % (f(8), f(46), f(W - 16), f(W - 16)), fill='#9CA2A9',
                stroke='#6B7178', stroke_width=0.4)]
    anchors = {'bottom': (W / 2, H), 'left': (0, H / 2), 'right': (W, H / 2)}
    return Device(''.join(out), W, H, anchors, 'strike')


def poe_switch(D, ports=4):
    """Metzler VDM10 PoE-Switch 4 × PoE (105 × 28 mm) bzw. 8 × Gigabit PoE (218 × 28 mm) – Frontansicht."""
    W = 105.0 if ports == 4 else 217.6
    H = 28.0
    body = D.lin('sw-body', [(0, '#4A5A70'), (0.12, '#34435A'), (1, '#27344A')])
    out = [rect(1.0, 2.4, W - 1.0, H - 1.0, rx=1.6, fill='#000000', opacity=0.16),
           rect(0, 0, W, H, rx=1.6, fill=body, stroke='#1B2533', stroke_width=0.6),
           line(1, 1.2, W - 1, 1.2, stroke='#6C7D95', stroke_width=0.5)]
    out.append(circle(7, 10, 0.9, fill='#5BE37D'))
    out.append(text(9.2, 10.9, 'PWR', size=2.1, fill='#D5DBE4'))
    out.append(circle(7, 16, 0.9, fill='#F0B03A'))
    out.append(text(9.2, 16.9, 'PoE-MAX', size=2.1, fill='#D5DBE4'))
    x0 = 24.0
    pitch = 11.2 if ports == 4 else 13.6
    anchors = {}
    for i in range(ports):
        x = x0 + i * pitch + pitch / 2
        out.append(rj45(x, 15.5, w=9.2, h=7.8))
        out.append(circle(x - 2.4, 9.6, 0.6, fill='#5BE37D'))
        out.append(circle(x + 2.4, 9.6, 0.6, fill='#F0B03A'))
        out.append(text(x, 24.4, str(i + 1), size=2.0, fill='#D5DBE4', anchor='middle'))
        anchors['P%d' % (i + 1)] = (x, H)
    if ports == 4:
        out.append(rect(x0 + 0.6, 22.2, pitch * 2 - 1.2, 0.9, fill='#D0342C'))
    ux = x0 + ports * pitch + pitch / 2 + 2
    out.append(rect(ux - 5.6, 10.7, 11.2, 9.6, rx=0.5, fill='none', stroke='#D5DBE4', stroke_width=0.35))
    out.append(rj45(ux, 15.5, w=9.2, h=7.8))
    out.append(text(ux, 24.4, 'UPLINK', size=1.9, fill='#D5DBE4', anchor='middle'))
    anchors['UP'] = (ux, H)
    if ports == 8:
        sx = ux + 15
        out.append(rect(sx - 5, 11.5, 10, 7.8, rx=0.5, fill='#0E0F10', stroke='#8C96A6', stroke_width=0.4))
        out.append(text(sx, 24.4, 'SFP', size=1.9, fill='#D5DBE4', anchor='middle'))
    out.append(text(x0, 5.6, 'LINK/ACT   PoE', size=1.9, fill='#D5DBE4'))
    anchors['DC'] = (W - 4, H / 2)
    return Device(''.join(out), W, H, anchors, 'poe%d' % ports)


def router(D):
    """Internet-Router (generisch, weiß) – nur zur Einordnung, kein Metzler-Produkt."""
    W, H = 120.0, 34.0
    out = [rect(18, -26, 3.2, 30, rx=1.6, fill='#E8EAED', stroke='#B9BEC4', stroke_width=0.5),
           rect(W - 21, -26, 3.2, 30, rx=1.6, fill='#E8EAED', stroke='#B9BEC4', stroke_width=0.5),
           rect(1, 3, W - 1, H - 2, rx=5, fill='#000000', opacity=0.12),
           rect(0, 0, W, H, rx=5, fill='#FFFFFF', stroke='#C8CCD1', stroke_width=0.7),
           rect(0, H - 9, W, 9, rx=4, fill='#EEF0F3'),
           line(4, H - 9, W - 4, H - 9, stroke='#D3D7DC', stroke_width=0.5)]
    for i in range(4):
        out.append(circle(W - 40 + i * 7.5, H - 4.5, 1.0, fill='#35C26B' if i < 3 else '#C7CBD1'))
    cx, cy = 36, 17
    for r in (4.5, 8.0, 11.5):
        out.append(path('M%s %s a%s %s 0 0 1 %s 0' % (f(cx - r * 0.72), f(cy), f(r), f(r), f(r * 1.44)),
                        fill='none', stroke='#2EA3D8', stroke_width=1.3, stroke_linecap='round'))
    out.append(circle(cx, cy + 2.2, 1.4, fill='#2EA3D8'))
    anchors = {'bottom': (W / 2, H), 'left': (0, H / 2), 'right': (W, H / 2), 'lan': (W / 2 + 22, H)}
    return Device(''.join(out), W, H, anchors, 'router')


def plug_adapter(D, label='48 V DC'):
    """Steckernetzteil (Euro/Schuko) – z. B. für den PoE-Switch."""
    W, H = 34.0, 46.0
    out = [rect(1, 2.5, W - 1, H - 1, rx=4, fill='#000000', opacity=0.15),
           rect(0, 0, W, H, rx=4, fill='#26272A', stroke='#101113', stroke_width=0.6),
           rect(4, 4, W - 8, 10, rx=2, fill='#303236'),
           circle(W / 2 - 6, 9, 1.6, fill='#9EA2A8'), circle(W / 2 + 6, 9, 1.6, fill='#9EA2A8'),
           text(W / 2, 27, label, size=4.2, weight=700, fill='#E6E8EB', anchor='middle'),
           text(W / 2, 33, '100–240 V AC', size=2.8, fill='#9EA2A8', anchor='middle')]
    anchors = {'dc': (W / 2, H), 'top': (W / 2, 0)}
    return Device(''.join(out), W, H, anchors, 'adapter')


def wall_socket(D):
    """Schuko-Steckdose 230 V – 60 × 60 mm."""
    W, H = 60.0, 60.0
    out = [rect(1, 2, W - 1, H - 1, rx=8, fill='#000000', opacity=0.1),
           rect(0, 0, W, H, rx=8, fill='#FFFFFF', stroke='#CBCFD4', stroke_width=0.7),
           circle(W / 2, H / 2, 19, fill='#F2F3F5', stroke='#D3D7DC', stroke_width=0.7),
           circle(W / 2 - 7, H / 2, 2.4, fill='#5D6167'), circle(W / 2 + 7, H / 2, 2.4, fill='#5D6167'),
           rect(W / 2 - 2.5, H / 2 - 19, 5, 3, fill='#C9CDD2'), rect(W / 2 - 2.5, H / 2 + 16, 5, 3, fill='#C9CDD2')]
    anchors = {'center': (W / 2, H / 2), 'bottom': (W / 2, H), 'top': (W / 2, 0)}
    return Device(''.join(out), W, H, anchors, 'socket')


def smartphone(D):
    W, H = 38.0, 76.0
    out = [rect(0, 0, W, H, rx=6, fill='#1B1C1F', stroke='#0B0B0C', stroke_width=0.6),
           rect(2.5, 6, W - 5, H - 12, rx=2, fill=D.lin('ph-scr', [(0, '#16253F'), (1, '#0C1424')])),
           text(W / 2, 20, 'Hik-Connect', size=3.4, weight=700, fill='#FFFFFF', anchor='middle'),
           rect(7, 26, W - 14, 18, rx=1.5, fill='#2C3B57'),
           circle(W / 2 - 7, 56, 3.6, fill='#D43A33'), circle(W / 2 + 7, 56, 3.6, fill='#2DB35A'),
           rect(W / 2 - 5, 2.5, 10, 1.4, rx=0.7, fill='#3A3C40')]
    return Device(''.join(out), W, H, {'top': (W / 2, 0), 'bottom': (W / 2, H), 'left': (0, H / 2)}, 'phone')


def exit_button(D):
    """Ausgangstaster (Aufputz) – 50 × 50 mm."""
    W, H = 50.0, 50.0
    out = [rect(1, 2, W - 1, H - 1, rx=5, fill='#000000', opacity=0.12),
           rect(0, 0, W, H, rx=5, fill='#F7F8F9', stroke='#C6CAD0', stroke_width=0.7),
           circle(W / 2, H / 2, 13, fill=steel(D, 'st-ring')),
           circle(W / 2, H / 2, 9.5, fill='#E9EBEE', stroke='#A7ACB2', stroke_width=0.5),
           text(W / 2, H / 2 + 2.6, 'EXIT', size=6.2, weight=700, fill='#4A4E54', anchor='middle')]
    return Device(''.join(out), W, H, {'bottom': (W / 2, H), 'left': (0, H / 2), 'right': (W, H / 2)}, 'exit')


# ================================================================= WEITERE TÜRSTATIONEN (VDM10 2.0 · ADM10)
def _plate(D):
    return D.lin('col-plate', [(0, '#343D49'), (0.5, '#232A33'), (1, '#2E3641')], x1=0, y1=0, x2=1, y2=0)


def _ring_button(D, cx, cy, r):
    """Edelstahl-Klingeltaster mit weißem Leuchtring."""
    return (circle(cx, cy, r, fill=steel(D, 'st-ring')) + circle(cx, cy, r * 0.79, fill='#FFFFFF', opacity=0.95) +
            circle(cx, cy, r * 0.62, fill=D.rad('col-btn', [(0, '#F1F3F5'), (0.7, '#C9CDD2'), (1, '#9AA0A7')])))


def _dot_camera(D, cx, cy, r=18):
    """Kamera mit Punkt-Ring (Colson / Niko / Neo)."""
    out = [circle(cx, cy, r, fill='#0A0B0D', stroke='#2A2D31', stroke_width=0.6)]
    for rr, n, op in ((r * 0.9, 64, 0.9), (r * 0.77, 56, 0.75), (r * 0.64, 48, 0.55)):
        out.append(circle(cx, cy, rr, fill='none', stroke='#D9DDE2', stroke_width=0.9,
                          stroke_dasharray='%s %s' % (f(2 * math.pi * rr / n * 0.42), f(2 * math.pi * rr / n * 0.58)),
                          opacity=op))
    out.append(circle(cx, cy, r * 0.53, fill='#050607', stroke='#33363B', stroke_width=0.6))
    out.append(circle(cx, cy, r * 0.34, fill=D.rad('col-lens', [(0, '#5D6A7B'), (0.55, '#1C212A'), (1, '#07080A')])))
    out.append(circle(cx - r * 0.11, cy - r * 0.11, r * 0.08, fill='#B8C4D2', opacity=0.75))
    out.append(path('M%s %s a%s %s 0 0 1 %s 0' % (f(cx - r * 0.17), f(cy - r * 0.41), f(r * 0.44), f(r * 0.44),
                                                  f(r * 0.34)), fill='none', stroke='#3FBF6B', stroke_width=0.8))
    return ''.join(out)


def _round_camera(D, cx, cy, r=13):
    """Runde Kamera ohne Punkt-Ring (Kian / Horizon)."""
    return ''.join([
        circle(cx, cy, r, fill='#0B0C0E', stroke='#2B2E33', stroke_width=0.8),
        circle(cx, cy, r * 0.62, fill=D.rad('col-lens', [(0, '#5D6A7B'), (0.55, '#1C212A'), (1, '#07080A')])),
        circle(cx - r * 0.18, cy - r * 0.18, r * 0.12, fill='#B8C4D2', opacity=0.75),
        path('M%s %s a%s %s 0 0 1 %s 0' % (f(cx - r * 0.28), f(cy - r * 0.55), f(r * 0.6), f(r * 0.6), f(r * 0.56)),
             fill='none', stroke='#3FBF6B', stroke_width=0.8),
        path('M%s %s a%s %s 0 0 1 %s 0' % (f(cx - r * 0.2), f(cy - r * 0.45), f(r * 0.5), f(r * 0.5), f(r * 0.4)),
             fill='none', stroke='#D8463C', stroke_width=0.6, opacity=0.8)])


def _bell(cx, cy, s, color):
    return path('M%s %s a%s %s 0 0 1 %s 0 v%s l%s %s h-%s l%s -%s z' % (
        f(cx - s * 0.32), f(cy + s * 0.12), f(s * 0.32), f(s * 0.32), f(s * 0.64), f(s * 0.22), f(s * 0.12), f(s * 0.16),
        f(s * 0.88), f(s * 0.12), f(s * 0.16)), fill='none', stroke=color, stroke_width=s * 0.08,
        stroke_linejoin='round') + circle(cx, cy + s * 0.58, s * 0.08, fill=color)


def _name_rows(D, W, names, cy_center, pitch, tag_x=27.0, tag_w=68.0, tag_h=10.5, band=True):
    tag = D.lin('max-tag', [(0, '#FBFBFC'), (0.5, '#E4E6E9'), (1, '#CFD2D6')])
    n = len(names)
    out = []
    for i, nm in enumerate(names):
        y = cy_center + (i - (n - 1) / 2.0) * pitch
        if band:
            out.append(rect(0, y - pitch * 0.42, W, pitch * 0.84, fill='#1C222A', opacity=0.65))
            out.append(line(0, y - pitch * 0.42, W, y - pitch * 0.42, stroke='#3B4451', stroke_width=0.4))
        out.append(rect(tag_x, y - tag_h / 2, tag_w, tag_h, rx=0.6, fill=tag, stroke='#B4B8BD', stroke_width=0.4))
        out.append(text(tag_x + tag_w / 2, y + tag_h * 0.17, nm, size=tag_h * 0.5, fill='#1A1A1C', anchor='middle'))
        bx = tag_x + tag_w + 4
        out.append(rect(bx, y - tag_h / 2, tag_h, tag_h, rx=0.6, fill='none', stroke='#59626F', stroke_width=0.4))
        out.append(_bell(bx + tag_h / 2, y - tag_h * 0.18, tag_h * 0.55, '#D5DAE1'))
    return ''.join(out)


def _std_anchors(W, H, side_y):
    return {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, side_y), 'right': (W, side_y),
            'bus': (W / 2 - 14, H), 'rs485': (W / 2 + 14, H), 'pwr': (W / 2 + 28, H)}


def vdm10_kian(D, name='Steinbach'):
    """VDM10 2.0 Kian – runde Kamera, Lautsprechergitter, erhabenes Namensschild, Leuchttaster."""
    W, H = 135.0, 271.0
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=_plate(D), stroke='#15191E', stroke_width=0.8),
           circle(W * 0.5, H * 0.075, 0.8, fill='#11161C'), circle(W * 0.7, H * 0.1, 0.8, fill='#11161C'),
           _round_camera(D, W / 2, H * 0.255, 13.5)]
    for r in range(2):
        for c in range(5):
            out.append(rect(24 + c * 17.6, H * 0.372 + r * 4.2, 13, 2.2, rx=1.1, fill='#15181C', stroke='#3D4552',
                            stroke_width=0.3))
    out.append(rect(26, H * 0.605, W - 52, H * 0.08, fill='#1E242C', stroke='#3A4350', stroke_width=0.5))
    out.append(text(W / 2, H * 0.655, name, size=7.2, fill='#D6DBE2', anchor='middle', ls=0.5))
    out.append(_ring_button(D, W / 2, H * 0.775, 9.6))
    out.append(circle(W / 2, H * 0.868, 0.8, fill='#11161C'))
    out.append(metzler_logo(D, W / 2, H - 4.2, 3.4, fill='#B7BDC6', text_fill='#C5CAD2'))
    return Device(''.join(out), W, H, _std_anchors(W, H, 190), 'vdm10-kian')


def vdm10_niko(D, name='VOSSBERG'):
    """VDM10 2.0 Niko – wie Colson, zusätzlich Fingerabdruck-Leser im schwarzen Band."""
    W, H = 135.0, 288.0
    band = D.lin('col-band', [(0, '#1C1D20'), (0.5, '#0C0D0F'), (1, '#1A1B1E')])
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=_plate(D), stroke='#15191E', stroke_width=0.8),
           rect(0, 9, W, 1.4, fill=steel(D)), rect(0, H - 13, W, 1.4, fill=steel(D)),
           rect(0, 44, W, 54, fill=band), _dot_camera(D, W / 2, 71, 18)]
    for k in range(2):
        out.append(rect(W / 2 - 19, 101 + k * 3, 38, 1.5, rx=0.75, fill='#15181C', stroke='#434B56', stroke_width=0.3))
    out.append(text(W / 2, 119, name, size=7.2, fill='#D4D9E0', anchor='middle', ls=3.4, weight=300))
    out.append(line(0, 127, W, 127, stroke='#3A4350', stroke_width=0.5))
    out.append(rect(0, 157, W, 55, fill='#0D0E10'))
    out.append(rect(W / 2 - 8.5, 171, 17, 26, rx=2.2, fill='#1A1B1E', stroke='#3A3D42', stroke_width=0.6))
    out.append(rect(W / 2 - 6, 174, 12, 20, rx=1.6, fill='#0F1012', stroke='#2C2E33', stroke_width=0.4))
    out.append(_ring_button(D, W / 2, 236, 7.8))
    out.append(metzler_logo(D, W / 2, H - 4.2, 3.4, fill='#B7BDC6', text_fill='#C5CAD2'))
    return Device(''.join(out), W, H, _std_anchors(W, H, 200), 'vdm10-niko')


def vdm10_neo(D, names=('Vossmann',)):
    """VDM10 2.0 Neo – austauschbare Namensschilder mit Glocken-Symbol (1–6 Klingeltaster)."""
    W, H = 135.0, 280.0
    band = D.lin('col-band', [(0, '#1C1D20'), (0.5, '#0C0D0F'), (1, '#1A1B1E')])
    n = max(1, len(names))
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=_plate(D), stroke='#15191E', stroke_width=0.8),
           rect(0, 9, W, 1.4, fill=steel(D)), rect(0, H - 13, W, 1.4, fill=steel(D)),
           rect(0, 45, W, 42, fill=band), _dot_camera(D, W / 2, 66, 17)]
    for k in range(2):
        out.append(rect(W / 2 - 19, 91 + k * 3, 38, 1.5, rx=0.75, fill='#15181C', stroke='#434B56', stroke_width=0.3))
    out.append(line(0, 106, W, 106, stroke='#3A4350', stroke_width=0.5))
    pitch = min(28.0, 134.0 / n)
    center = 185.0 + min(n - 1, 2) * 5.5
    out.append(_name_rows(D, W, names, center, pitch, tag_h=min(10.5, pitch * 0.5)))
    out.append(circle(W / 2, H - 22, 0.8, fill='#11161C'))
    out.append(metzler_logo(D, W / 2, H - 4.2, 3.4, fill='#B7BDC6', text_fill='#C5CAD2'))
    return Device(''.join(out), W, H, _std_anchors(W, H, 190), 'vdm10-neo')


def vdm10_horizon(D, lines=('Familie', 'Zimmermann')):
    """VDM10 2.0 Horizon – modulare Türstation mit Touch-Display-Modul (VDM10-TDM)."""
    W, H = 135.0, 247.0
    glass = D.lin('tdm-glass', [(0, '#1C222A'), (0.5, '#0B0D10'), (1, '#161A20')], x1=0, y1=0, x2=1, y2=1)
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=_plate(D), stroke='#15191E', stroke_width=0.8),
           circle(W * 0.62, 9, 0.8, fill='#11161C'), circle(W * 0.66, 21, 0.8, fill='#11161C'),
           _round_camera(D, W / 2, H * 0.185, 17)]
    rows = ((-8, 1), (-4, 3), (0, 5), (4, 3), (8, 1))
    for dy, cnt in rows:
        for c in range(cnt):
            x = W / 2 + (c - (cnt - 1) / 2.0) * 9.6
            out.append(rect(x - 3.8, H * 0.37 + dy - 0.8, 7.6, 1.6, rx=0.8, fill='#15181C', stroke='#3D4552',
                            stroke_width=0.3))
    for x in (W / 2 - 39, W / 2 + 33):
        out.append(rect(x, H * 0.37 - 0.8, 6, 1.6, rx=0.8, fill='#15181C', stroke='#3D4552', stroke_width=0.3))
    gx, gy, gw, gh = 31.0, H * 0.535, 73.0, 80.0
    out.append(rect(gx - 1.5, gy - 1.5, gw + 3, gh + 3, rx=1.2, fill='#2A313B', stroke='#46505D', stroke_width=0.5))
    out.append(rect(gx, gy, gw, gh, fill=glass))
    out.append(_bell(W / 2, gy + 16, 9, '#FFFFFF'))
    for k, ln in enumerate(lines):
        out.append(text(W / 2, gy + 41 + k * 8.5, ln, size=7.2, fill='#FFFFFF', anchor='middle'))
    out.append(circle(W / 2 - 2.5, gy + gh - 12, 1.6, fill='none', stroke='#C9CFD7', stroke_width=0.6))
    out.append(path('M%s %s h5 m-1.4 0 v1.2' % (f(W / 2 - 0.9), f(gy + gh - 12)), fill='none', stroke='#C9CFD7',
                    stroke_width=0.6))
    out.append(circle(W / 2, H - 16, 0.8, fill='#11161C'))
    out.append(metzler_logo(D, W / 2, H - 4.6, 3.4, fill='#B7BDC6', text_fill='#C5CAD2'))
    return Device(''.join(out), W, H, _std_anchors(W, H, 170), 'vdm10-horizon')


def adm10_dominik(D, name='HOFFMANN'):
    """ADM10 Dominik – Audio-Türstation (ohne Kamera), schwarzes Namensband, Leuchtring-Taster – 133 × 245 mm."""
    W, H = 133.0, 245.0
    band = D.lin('adm-band', [(0, '#111214'), (0.5, '#26282C'), (1, '#111214')])
    clip = D.clip('dom-clip', rect(0, 0, W, H, rx=4))
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, rx=4, fill='#000000', opacity=0.18),
           '<g clip-path="%s">' % clip, rect(0, 0, W, H, fill=_plate(D)),
           line(0, 77, W, 77, stroke='#0D0F12', stroke_width=1.2), line(0, 82, W, 82, stroke='#0D0F12', stroke_width=1.2),
           rect(0, 86, W, 49, fill=band)]
    for k in range(9):
        out.append(line(0, 89 + k * 5, W, 89 + k * 5, stroke='#FFFFFF', stroke_width=0.25, opacity=0.06))
    out += [line(0, 140, W, 140, stroke='#0D0F12', stroke_width=1.2), line(0, 145, W, 145, stroke='#0D0F12', stroke_width=1.2),
            '</g>', rect(0, 0, W, H, rx=4, fill='none', stroke='#15191E', stroke_width=0.8),
            circle(W * 0.69, 17, 0.8, fill='#11161C'),
            text(W / 2, 113.5, name, size=7.6, fill='#DCE1E8', anchor='middle', ls=3.4, weight=300),
            circle(W / 2, 191, 13.4, fill='none', stroke='#FFFFFF', stroke_width=1.7),
            circle(W / 2, 191, 14.6, fill='none', stroke='#FFFFFF', stroke_width=0.6, opacity=0.35),
            circle(W / 2, 224, 0.8, fill='#11161C'),
            metzler_logo(D, W / 2, H - 5.4, 3.4, fill='#B7BDC6', text_fill='#C5CAD2')]
    return Device(''.join(out), W, H, _std_anchors(W, H, 170), 'adm10-dominik')


def adm10_kai(D, names=('Steinbach-Kehl',), number='24', street='BREITENBACHWEG'):
    """ADM10 Kai – Audio-Türstation mit Hausnummer, Straße und austauschbaren Namensschildern (1–6)."""
    W, H = 135.0, 280.0
    numg = D.lin('kai-num', [(0, '#F6F7F8'), (0.5, '#C3C8CE'), (1, '#EEF0F2')], x1=0, y1=0, x2=1, y2=1)
    n = max(1, len(names))
    out = [rect(1.5, 3.5, W - 1.5, H - 1.5, fill='#000000', opacity=0.18),
           rect(0, 0, W, H, fill=_plate(D), stroke='#15191E', stroke_width=0.8),
           rect(0, 9, W, 1.4, fill=steel(D)), rect(0, H - 13, W, 1.4, fill=steel(D)),
           text(W / 2, 77, number, size=66, weight=200, fill=numg, stroke='#8E949B', stroke_width=0.4,
                anchor='middle', ls=-1),
           text(W / 2, 88, street, size=3.6, fill='#C9CFD7', anchor='middle', ls=1.7)]
    for k in range(2):
        out.append(rect(W / 2 - 19, 98 + k * 3, 38, 1.5, rx=0.75, fill='#15181C', stroke='#434B56', stroke_width=0.3))
    pitch = 14.0
    last = 221.0 if n >= 2 else 218.0
    center = last - (n - 1) * pitch / 2.0
    out.append(_name_rows(D, W, names, center, pitch, tag_x=30.0, tag_w=62.0, tag_h=9.0, band=False))
    for i in range(n + 1):
        y = center + (i - n / 2.0) * pitch
        out.append(line(0, y, W, y, stroke='#4A5462', stroke_width=0.5, opacity=0.8))
    out.append(circle(W / 2, H * 0.92, 0.8, fill='#11161C'))
    out.append(metzler_logo(D, W / 2, H - 4.2, 3.4, fill='#B7BDC6', text_fill='#C5CAD2'))
    return Device(''.join(out), W, H, _std_anchors(W, H, 190), 'adm10-kai')


# ================================================================= ADM10 INNENSTATION
def adm10_monitor(D, color='white'):
    """ADM10 Innenstation Home 7'' (LAN oder 2-Draht) – 200 × 140 mm, dunkle 4-Kachel-Oberfläche."""
    W, H = 200.0, 140.0
    white = color == 'white'
    sx, sy, sw, sh = 21.0, 17.5, 158.0, 91.5
    out = [rect(0.4, 2.2, W - 0.8, H - 1.6, rx=3.2, fill='#000000', opacity=0.10),
           rect(0, 0, W, H - 1.2, rx=3.2, fill='#FFFFFF' if white else '#1B1C1F', stroke='#D3D6DA' if white else '#08090A',
                stroke_width=0.9),
           rect(sx, sy, sw, sh, fill='#1B1C1F'),
           line(sx + sw / 2, sy + 8, sx + sw / 2, sy + sh, stroke='#2F3135', stroke_width=0.5),
           line(sx, sy + 8 + (sh - 8) / 2, sx + sw, sy + 8 + (sh - 8) / 2, stroke='#2F3135', stroke_width=0.5)]
    tiles = (('Anrufen', 'phone'), ('Tür Öffnen', 'key'), ('Stummschalten deaktiviert', 'bell'), ('Einstellungen', 'gear'))
    for i, (lab, ic) in enumerate(tiles):
        cx = sx + sw * (0.25 if i % 2 == 0 else 0.75)
        cy = sy + 8 + (sh - 8) * (0.25 if i < 2 else 0.75) - 3
        if ic == 'phone':
            out.append(path('M%s %s c-0.6 3 1.6 6.4 4.6 7 l1.2 -1.6 -2 -1.6 -1 0.8 c-1 -0.6 -1.7 -1.6 -1.9 -2.6 l0.9 -0.9 -1.4 -2.2 z' % (
                f(cx - 3), f(cy - 3.4)), fill='#FFFFFF'))
        elif ic == 'key':
            out.append(circle(cx - 1.6, cy - 1.4, 2.4, fill='#FFFFFF'))
            out.append(path('M%s %s l4.4 4.4 m-1.4 -1.4 l1.4 -1.4 m-0.2 3 l1.2 -1.2' % (f(cx - 0.2), f(cy)),
                            fill='none', stroke='#FFFFFF', stroke_width=1.2, stroke_linecap='round'))
        elif ic == 'bell':
            out.append(_bell(cx, cy - 2, 7, '#FFFFFF'))
        else:
            for k in range(8):
                a = k * math.pi / 4
                out.append(line(cx + math.cos(a) * 2.6, cy + math.sin(a) * 2.6, cx + math.cos(a) * 4.0, cy + math.sin(a) * 4.0,
                                stroke='#FFFFFF', stroke_width=1.3, stroke_linecap='round'))
            out.append(circle(cx, cy, 2.8, fill='#FFFFFF'))
            out.append(circle(cx, cy, 1.2, fill='#1B1C1F'))
        out.append(text(cx, cy + 10.5, lab, size=2.6, fill='#FFFFFF', anchor='middle'))
    for i in range(4):
        out.append(rect(sx + sw - 22 + i * 5.0, sy + 2.6, 2.8, 2.8, rx=0.5, fill='none', stroke='#FFFFFF',
                        stroke_width=0.4, opacity=0.75))
    out.append(rect(sx + sw / 2 - 2, sy + 2.6, 3.4, 2.6, rx=0.3, fill='none', stroke='#FFFFFF', stroke_width=0.4))
    out.append(text(W / 2, 128.2, 'METZLER', size=5.6, weight=700, fill='#A7AAAF' if white else '#C9CBCE',
                    anchor='middle', ls=0.9))
    out.append(circle(W - 12, 130, 0.9, fill='#8A8D92'))
    anchors = {'bottom': (W / 2, H - 1.2), 'top': (W / 2, 0), 'left': (0, H / 2), 'right': (W, H / 2)}
    return Device(''.join(out), W, H, anchors, 'adm10-home')


# ================================================================= PAKETBOXEN · BRIEFKÄSTEN MIT SPRECHANLAGE
def paketbox_saeule(D, name='Familie Metzler', number='27', street='Bachstraße'):
    """Paketbox-Säule mit Video-Türsprechanlage (Zivo 2 · Bispo 2) – Frontansicht 503 × 1603 mm."""
    W, H = 503.0, 1603.0
    body = D.lin('pb-body', [(0, '#34363A'), (0.5, '#2A2C30'), (1, '#222428')], x1=0, y1=0, x2=1, y2=0)
    tag = D.lin('pb-tag', [(0, '#F4F5F6'), (0.5, '#C9CDD2'), (1, '#E9EBEE')], x1=0, y1=0, x2=1, y2=1)
    out = [rect(6, 12, W - 6, H - 6, fill='#000000', opacity=0.16),
           rect(0, 0, W, H, fill=body, stroke='#141518', stroke_width=2),
           rect(0, 0, W, 150, fill='#0B0B0D'),
           rect(70, 45, 62, 62, rx=6, fill='#16171A', stroke='#3A3C40', stroke_width=2),
           circle(101, 76, 16, fill=D.rad('pb-lens', [(0, '#5D6A7B'), (0.6, '#1C212A'), (1, '#07080A')])),
           circle(245, 70, 5, fill='#1E1F22', stroke='#4A4C50', stroke_width=1.5), circle(245, 92, 2.5, fill='#3A3C40'),
           circle(415, 76, 22, fill='none', stroke='#6D7075', stroke_width=3),
           circle(415, 76, 12, fill='#1C1D20'),
           rect(130, 185, 245, 50, rx=4, fill=tag, stroke='#8E949B', stroke_width=1.5),
           text(252.5, 218, name, size=24, fill='#1A1A1C', anchor='middle'),
           rect(30, 330, W - 60, 14, rx=3, fill=steel(D)),
           rect(36, 560, 330, 120, fill=tag, stroke='#8E949B', stroke_width=1.5),
           text(56, 640, street, size=22, fill='#54595F'),
           line(250, 578, 250, 662, stroke='#3A3C40', stroke_width=3),
           text(262, 655, number, size=86, weight=300, fill='#2A2C30'),
           rect(30, 760, W - 60, 14, rx=3, fill=steel(D)),
           rect(30, 800, W - 60, 760, rx=4, fill='none', stroke='#1A1B1E', stroke_width=3),
           circle(440, 1010, 9, fill='#9EA3A9', stroke='#6B7076', stroke_width=2)]
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 400), 'right': (W, 400),
               'bus': (W / 2 - 60, H), 'rs485': (W / 2 + 60, H)}
    return Device(''.join(out), W, H, anchors, 'paketbox-saeule')


def paketbox_videomodul(D, name='Säckler/Hartmann', street='Krautgartenweg', number='40'):
    """Paketbox mit Videomodul (VM300/VM400) – Frontansicht 440 × 955 mm."""
    W, H = 440.0, 955.0
    body = D.lin('pv-body', [(0, '#34404D'), (0.5, '#25303B'), (1, '#2E3A46')], x1=0, y1=0, x2=1, y2=0)
    tag = D.lin('pb-tag', [(0, '#F4F5F6'), (0.5, '#C9CDD2'), (1, '#E9EBEE')], x1=0, y1=0, x2=1, y2=1)
    out = [rect(6, 12, W - 6, H - 6, fill='#000000', opacity=0.16),
           rect(0, 0, W, H, fill=body, stroke='#141A21', stroke_width=2),
           rect(0, 0, W, 118, fill='#0A0B0D'),
           circle(70, 58, 20, fill='none', stroke='#9EA3A9', stroke_width=3),
           _bell(70, 52, 22, '#C9CFD7'),
           circle(368, 52, 20, fill='#16171A', stroke='#3A3C40', stroke_width=2),
           circle(368, 52, 11, fill=D.rad('pb-lens', [(0, '#5D6A7B'), (0.6, '#1C212A'), (1, '#07080A')])),
           rect(240, 140, 175, 28, fill=tag, stroke='#8E949B', stroke_width=1.2),
           text(405, 160, name, size=17, fill='#2A2C30', anchor='end'),
           rect(16, 125, W - 32, 285, rx=4, fill='none', stroke='#1A2028', stroke_width=3),
           rect(0, 555, W, 82, fill=tag, stroke='#8E949B', stroke_width=1.2),
           text(26, 606, street, size=30, fill='#54595F'),
           line(300, 568, 300, 624, stroke='#3A3C40', stroke_width=3),
           text(312, 618, number, size=64, weight=300, fill='#2A2C30'),
           rect(16, 650, W - 32, 290, rx=4, fill='none', stroke='#1A2028', stroke_width=3),
           circle(56, 880, 9, fill='#9EA3A9', stroke='#6B7076', stroke_width=2)]
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 300), 'right': (W, 300),
               'bus': (W / 2 - 50, H), 'rs485': (W / 2 + 50, H)}
    return Device(''.join(out), W, H, anchors, 'paketbox-videomodul')


def briefkasten_vdm10(D, name='Bahnmüller'):
    """Briefkasten mit VDM10 2.0 (BK212-VDM10) – Frontansicht 392 × 604 mm."""
    W, H = 392.0, 604.0
    body = D.lin('pv-body', [(0, '#34404D'), (0.5, '#25303B'), (1, '#2E3A46')], x1=0, y1=0, x2=1, y2=0)
    out = [rect(5, 10, W - 5, H - 5, fill='#000000', opacity=0.16),
           rect(0, 0, W, H, fill=body, stroke='#141A21', stroke_width=2),
           rect(0, 40, W, 9, fill=steel(D)),
           rect(0, 49, W, 75, fill='#0A0B0D'),
           circle(62, 86, 22, fill='none', stroke='#C9CFD7', stroke_width=2.4),
           text(62, 90, name, size=8, fill='#C9CFD7', anchor='middle'),
           circle(330, 84, 20, fill='#16171A', stroke='#3A3C40', stroke_width=2),
           circle(330, 84, 10, fill=D.rad('pb-lens', [(0, '#5D6A7B'), (0.6, '#1C212A'), (1, '#07080A')])),
           rect(0, 124, W, 9, fill=steel(D)),
           rect(14, 150, W - 28, 48, rx=3, fill='none', stroke='#1A2028', stroke_width=3),
           rect(14, 205, W - 28, 345, rx=3, fill='none', stroke='#1A2028', stroke_width=3),
           circle(W / 2, 258, 8, fill='#9EA3A9', stroke='#6B7076', stroke_width=2),
           rect(0, 558, W, 9, fill=steel(D)),
           text(W - 16, 592, 'Zeitungen', size=22, weight=300, fill='#C9CFD7', anchor='end')]
    anchors = {'bottom': (W / 2, H), 'top': (W / 2, 0), 'left': (0, 300), 'right': (W, 300),
               'bus': (W / 2 - 40, H), 'rs485': (W / 2 + 40, H)}
    return Device(''.join(out), W, H, anchors, 'briefkasten-vdm10')
