#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Metzler Anschlussschemata – Zeichen-Bibliothek (Scene, Leitungen, Beschriftung, Info-Band, Export).

Wird von referenz.py (5 Referenzschemata) und eigenen Schema-Modulen benutzt; gebaut wird mit build.py.

Fachliche Quellen (edelstahl-tuerklingel.de, Stand 09/2026):
  Anschlussvorgaben 2-Draht IP · Anschlussvorgaben LAN/PoE · Checkliste Sprechanlagen
  Systemanleitung XDM10 (Innenstation + MAXIOR) · Anleitung VDM10 2.0 · Systemanleitung SDM10
  Anleitung Sicherheitsmodul · Stromversorgung SDM10 · Produktseiten der Komponenten
"""
import os
import re
import sys
import math
import shutil
import subprocess
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from devices import *  # noqa: E402,F401,F403


# ---- Metzler UI Kit tokens (metzler-tokens.css) --------------------------------
INK = '#1A171B'        # --color-digital-black
TXT2 = '#54545C'       # --color-graphite-700
TXT3 = '#6A6A6A'       # --color-graphite-600
PAPER = '#F5F6FA'      # --color-paper
HAIR = '#E6E6E8'       # --color-graphite-200
BORDER = '#DADADA'     # --color-graphite-300
TEAL = '#015253'       # --color-teal
TEAL50 = '#F2F6F6'     # --color-teal-50
WHITE = '#FFFFFF'

# ---- Leitungsfarben (Aderfarben nach Metzler-Anleitungen) ------------------------
CORE = {
    'red': ('#D7261E', '#7E120D'),
    'yellow': ('#F2C200', '#8A6A00'),
    'black': ('#26262A', '#000000'),
    'brown': ('#8A5A2E', '#4A2E14'),
    'blue': ('#2C6BD0', '#153F82'),
    'green': ('#2E9E4F', '#17602D'),
    'white': ('#FFFFFF', '#7C838B'),
}
LAN_C = ('#3456C8', '#1E347F', '#7D95E8')   # Kabel, Kontur, Glanzlinie
WIRE_W = 1.9     # Aderdicke
PAIR_GAP = 4.2   # Abstand der Adern eines Aderpaars


def text_w(s, size, bold=False):
    """Rough width of Helvetica text (for pills, wrapping)."""
    w = 0.0
    for ch in s:
        if ch in 'il.,:;|!\'ı':
            w += 0.26
        elif ch in 'fjtrI()[]/ ':
            w += 0.32
        elif ch in 'mwMW':
            w += 0.84
        elif ch.isupper() or ch in '–—':
            w += 0.66
        elif ch.isdigit():
            w += 0.56
        else:
            w += 0.54
    return w * size * (1.06 if bold else 1.0)


def wrap(s, size, width, bold=False):
    words, lines, cur = s.split(' '), [], ''
    for wd in words:
        test = (cur + ' ' + wd).strip()
        if text_w(test, size, bold) <= width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def ptsd(pts):
    return 'M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts)


def offset_line(pts, d):
    """Offset an orthogonal (or any) polyline by d (miter joins)."""
    out = []
    n = len(pts)
    for i in range(n):
        if i == 0:
            (x0, y0), (x1, y1) = pts[0], pts[1]
            L = math.hypot(x1 - x0, y1 - y0)
            nx, ny = -(y1 - y0) / L, (x1 - x0) / L
            out.append((x0 + nx * d, y0 + ny * d))
        elif i == n - 1:
            (x0, y0), (x1, y1) = pts[-2], pts[-1]
            L = math.hypot(x1 - x0, y1 - y0)
            nx, ny = -(y1 - y0) / L, (x1 - x0) / L
            out.append((x1 + nx * d, y1 + ny * d))
        else:
            (xa, ya), (xb, yb), (xc, yc) = pts[i - 1], pts[i], pts[i + 1]
            l1 = math.hypot(xb - xa, yb - ya)
            l2 = math.hypot(xc - xb, yc - yb)
            n1 = (-(yb - ya) / l1, (xb - xa) / l1)
            n2 = (-(yc - yb) / l2, (xc - xb) / l2)
            mx, my = n1[0] + n2[0], n1[1] + n2[1]
            ml = math.hypot(mx, my)
            if ml < 1e-9:
                mx, my = n1
            else:
                mx, my = mx / ml, my / ml
            dot = mx * n1[0] + my * n1[1]
            k = d / dot if abs(dot) > 1e-6 else d
            out.append((xb + mx * k, yb + my * k))
    return out


_LAST = [None]


def last_scene():
    """The Scene most recently created (build.py uses it for the layout check)."""
    return _LAST[0]


class Scene:
    def __init__(self, prefix, W, H, bg=PAPER):
        _LAST[0] = self
        self.placed = []
        self.D = Defs(prefix)
        self.W, self.H = W, H
        self.bg = bg
        self.foot = None
        self.L = {k: [] for k in ('bg', 'zones', 'cables', 'devices', 'over', 'labels')}

    def add(self, layer, s):
        self.L[layer].append(s)

    def place(self, dev, x, y, s=1.0):
        p = dev.place(x, y, s)
        self.add('devices', p.svg())
        self.placed.append((dev.name, x, y, dev.w * s, dev.h * s))
        return p

    # ------------------------------------------------------------- layout check
    def check(self):
        """Heuristic layout check: overlapping texts, text on devices, text outside the canvas.

        Returns a list of warning strings (empty = nothing found). Always also look at the PNG.
        """
        boxes = []
        rx = re.compile(r'<text ([^>]*)>(.*?)</text>', re.S)
        for layer in ('over', 'labels'):
            for chunk in self.L[layer]:
                for m in rx.finditer(chunk):
                    at, content = m.group(1), m.group(2)
                    g = lambda k: (re.search(r'\b%s="([^"]*)"' % k, at) or [None, None])[1]
                    if not content.strip() or g('x') is None:
                        continue
                    x, y, size = float(g('x')), float(g('y')), float(g('font-size') or 12)
                    t = (content.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
                         .replace('&quot;', '"'))
                    w = text_w(t, size, (g('font-weight') or '') in ('700', '800', 'bold'))
                    anc = g('text-anchor') or 'start'
                    x0 = x - (w / 2 if anc == 'middle' else w if anc == 'end' else 0)
                    boxes.append((x0, y - 0.78 * size, x0 + w, y + 0.22 * size, t[:40]))
        warn = []

        def inter(a, b):
            return max(0.0, min(a[2], b[2]) - max(a[0], b[0])) * max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
        for i in range(len(boxes)):
            a = boxes[i]
            if a[0] < 0 or a[1] < 0 or a[2] > self.W or a[3] > self.H:
                warn.append('Text außerhalb der Fläche: "%s"' % a[4])
            for b in boxes[i + 1:]:
                if inter(a, b) > 6:
                    warn.append('Texte überlappen: "%s" ↔ "%s"' % (a[4], b[4]))
            for name, dx, dy, dw, dh in self.placed:
                area = (a[2] - a[0]) * (a[3] - a[1])
                if area and inter(a, (dx, dy, dx + dw, dy + dh)) > 0.25 * area:
                    warn.append('Text liegt auf Gerät %s: "%s"' % (name, a[4]))
        return warn

    # ------------------------------------------------------------- structure
    def header(self, title, subtitle, tags=(), link=None):
        self.add('labels', text(40, 52, title, size=24, weight=700, fill=INK, ls=-0.36))
        self.add('labels', text(40, 76, subtitle, size=14, fill=TXT2))
        x = self.W - 40
        if link:
            lt, href = link
            w = text_w(lt, 14, True)
            self.add('labels', '<a href="%s" target="_blank" rel="noopener">%s</a>' % (
                esc(href), text(x, 76, lt, size=14, weight=700, fill=TEAL, anchor='end',
                                style='text-decoration:underline')))
        for t in reversed(tags):
            w = text_w(t, 12, True) + 22
            x0 = x - w
            self.add('labels', rect(x0, 34, w, 24, rx=12, fill=WHITE, stroke=BORDER, stroke_width=1))
            self.add('labels', text(x0 + w / 2, 50.5, t, size=12, weight=700, fill=INK, anchor='middle'))
            x = x0 - 8

    def zone(self, x, y, w, h, label, fill='#FFFFFF', stroke='#E3E5EA'):
        self.add('zones', rect(x, y, w, h, rx=12, fill=fill, stroke=stroke, stroke_width=1))
        self.add('over', text(x + 16, y + 26, label.upper(), size=12, weight=700, fill=TXT3, ls=1.2,
                              stroke=fill, stroke_width=6, stroke_linejoin='round', style='paint-order:stroke'))

    def din_rail(self, x0, x1, ycenter):
        st = self.D.lin('rail', [(0, '#E9EBEE'), (0.2, '#C3C7CC'), (0.5, '#F4F5F7'), (0.8, '#B5BAC0'),
                                 (1, '#D9DCE0')])
        out = [rect(x0, ycenter - 16, x1 - x0, 32, rx=2, fill=st, stroke='#9CA2A9', stroke_width=0.8)]
        x = x0 + 14
        while x < x1 - 24:
            out.append(rect(x, ycenter - 3, 16, 6, rx=3, fill='#9FA5AC'))
            x += 34
        self.add('zones', ''.join(out))

    def caption(self, x, y, title, lines=(), anchor='middle', title_size=14):
        self.add('labels', text(x, y, title, size=title_size, weight=700, fill=INK, anchor=anchor))
        for i, ln in enumerate(lines):
            self.add('labels', text(x, y + 17 + i * 16, ln, size=12, fill=TXT2, anchor=anchor))

    def tlabel(self, x, y, s, anchor='start', color=TXT2, weight=700, size=12):
        """Terminal label with white halo."""
        self.add('over', text(x, y, s, size=size, weight=weight, fill=color, anchor=anchor,
                              stroke='#FFFFFF', stroke_width=3.2, stroke_linejoin='round',
                              style='paint-order:stroke'))

    def pill(self, x, y, s, fill=INK, color='#FFFFFF', size=12):
        w = text_w(s, size, True) + 18
        self.add('over', rect(x - w / 2, y - 10, w, 20, rx=10, fill=fill) +
                 text(x, y + 4.3, s, size=size, weight=700, fill=color, anchor='middle'))

    def step(self, x, y, n):
        self.add('over', circle(x, y, 11, fill=TEAL, stroke='#FFFFFF', stroke_width=2) +
                 text(x, y + 4.4, str(n), size=12, weight=700, fill='#FFFFFF', anchor='middle'))

    # ------------------------------------------------------------- wiring
    def wire(self, pts, color, halo='#FFFFFF', w=WIRE_W, dash=None, layer='cables'):
        fill, edge = CORE[color]
        d = ptsd(pts)
        self.add(layer, path(d, fill='none', stroke=halo, stroke_width=w + 3.4, stroke_linejoin='round',
                             stroke_linecap='round'))
        self.add(layer, path(d, fill='none', stroke=edge, stroke_width=w + 1.1, stroke_linejoin='round',
                             stroke_linecap='round', stroke_dasharray=dash))
        self.add(layer, path(d, fill='none', stroke=fill, stroke_width=w, stroke_linejoin='round',
                             stroke_linecap='round', stroke_dasharray=dash))

    def pair(self, center, colors, ends=None, halo='#FFFFFF', gap=PAIR_GAP):
        """Two-core cable along an orthogonal centre line.

        ends: optional [(x, y), (x, y)] exact terminal points for colors[0] / colors[1];
        the cores leave the pair in the direction of the last segment and drop onto them.
        """
        a = offset_line(center, gap / 2)
        b = offset_line(center, -gap / 2)
        if ends:
            (xl, yl), (xe, ye) = center[-2], center[-1]
            horiz = abs(ye - yl) < 1e-6
            best = None
            for swap in (False, True):
                ca, cb = (b, a) if swap else (a, b)
                pa, pb = [], []
                ok = 0.0
                for core, (tx, ty) in ((ca, ends[0]), (cb, ends[1])):
                    ex, ey = core[-1]
                    ok += math.hypot(ex - tx, ey - ty)
                if best is None or ok < best[0]:
                    best = (ok, swap)
            swap = best[1]
            ca, cb = (b, a) if swap else (a, b)
            ca, cb = list(ca), list(cb)
            for core, (tx, ty) in ((ca, ends[0]), (cb, ends[1])):
                ex, ey = core[-1]
                if horiz:
                    core[-1] = (tx, ey)
                else:
                    core[-1] = (ex, ty) if abs(ex - tx) < 0.01 else (ex, ey)
                    if abs(ex - tx) >= 0.01:
                        core.append((tx, ey))
                if core[-1] != (tx, ty):
                    core.append((tx, ty))
            a, b = ca, cb
        d0 = ptsd(center)
        self.add('cables', path(d0, fill='none', stroke=halo, stroke_width=gap + WIRE_W + 3.6,
                                stroke_linejoin='round', stroke_linecap='round'))
        for pts, col in ((a, colors[0]), (b, colors[1])):
            self.add('cables', path(ptsd(pts), fill='none', stroke=CORE[col][1], stroke_width=WIRE_W + 1.1,
                                    stroke_linejoin='round', stroke_linecap='round'))
        for pts, col in ((a, colors[0]), (b, colors[1])):
            self.add('cables', path(ptsd(pts), fill='none', stroke=CORE[col][0], stroke_width=WIRE_W,
                                    stroke_linejoin='round', stroke_linecap='round'))
        return a, b

    def lan(self, pts, halo='#FFFFFF', plug_end=True, plug_start=False):
        d = ptsd(pts)
        self.add('cables', path(d, fill='none', stroke=halo, stroke_width=9.5, stroke_linejoin='round',
                                stroke_linecap='round'))
        self.add('cables', path(d, fill='none', stroke=LAN_C[1], stroke_width=6.2, stroke_linejoin='round',
                                stroke_linecap='round'))
        self.add('cables', path(d, fill='none', stroke=LAN_C[0], stroke_width=4.4, stroke_linejoin='round',
                                stroke_linecap='round'))
        self.add('cables', path(d, fill='none', stroke=LAN_C[2], stroke_width=1.0, stroke_linejoin='round',
                                stroke_linecap='round', opacity=0.8))
        for on, (p, q) in ((plug_end, (pts[-1], pts[-2])), (plug_start, (pts[0], pts[1]))):
            if not on:
                continue
            (x, y), (xp, yp) = p, q
            ang = math.degrees(math.atan2(y - yp, x - xp))
            self.add('cables', '<g transform="translate(%s %s) rotate(%s)">%s%s%s</g>' % (
                f(x), f(y), f(ang),
                rect(-11, -4.6, 11, 9.2, rx=1.4, fill='#E8EBEF', stroke='#7F8790', stroke_width=0.8),
                rect(-15, -3.2, 4.4, 6.4, rx=1, fill=LAN_C[1]),
                line(-9, -2.6, -2, -2.6, stroke='#B08A2E', stroke_width=0.9)))

    def wlan(self, p, q, label=None):
        (x0, y0), (x1, y1) = p, q
        self.add('cables', line(x0, y0, x1, y1, stroke=TEAL, stroke_width=2, stroke_dasharray='2 6',
                                stroke_linecap='round'))
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        for r in (5, 9.5, 14):
            self.add('over', path('M%s %s a%s %s 0 0 1 %s 0' % (f(mx - r * 0.72), f(my - 6), f(r), f(r),
                                                                f(r * 1.44)),
                                  fill='none', stroke=TEAL, stroke_width=2, stroke_linecap='round'))
        self.add('over', circle(mx, my - 3.6, 2, fill=TEAL))

    # ------------------------------------------------------------- info band
    def card(self, x, y, w, h, title):
        self.add('labels', rect(x, y, w, h, rx=12, fill=WHITE, stroke=HAIR, stroke_width=1))
        self.add('labels', text(x + 20, y + 32, title, size=16, weight=700, fill=INK))
        return x + 20, y + 58

    def steps_block(self, x, y, w, items, size=13):
        for i, s in enumerate(items):
            lines = wrap(s, size, w - 34)
            self.add('labels', circle(x + 10, y - 4.5, 10, fill=TEAL))
            self.add('labels', text(x + 10, y, str(i + 1), size=12, weight=700, fill='#FFFFFF', anchor='middle'))
            for k, ln in enumerate(lines):
                self.add('labels', text(x + 30, y + k * (size + 4), ln, size=size, fill=INK))
            y += len(lines) * (size + 4) + 10
        return y

    def bullets(self, x, y, w, items, size=13):
        for s in items:
            lines = wrap(s, size, w - 16)
            self.add('labels', circle(x + 4, y - 4.5, 2.6, fill=TEAL))
            for k, ln in enumerate(lines):
                self.add('labels', text(x + 16, y + k * (size + 4), ln, size=size, fill=INK))
            y += len(lines) * (size + 4) + 8
        return y

    def legend(self, x, y, w, items, size=13):
        """items: (kind, colors, label) kind in pair|wire|lan|wlan"""
        for kind, cols, lab in items:
            sx0, sx1, sy = x, x + 44, y - 4.5
            if kind == 'pair':
                for dy, c in ((-2.1, cols[0]), (2.1, cols[1])):
                    self.add('labels', line(sx0, sy + dy, sx1, sy + dy, stroke=CORE[c][1], stroke_width=WIRE_W + 1.1,
                                            stroke_linecap='round'))
                    self.add('labels', line(sx0, sy + dy, sx1, sy + dy, stroke=CORE[c][0], stroke_width=WIRE_W,
                                            stroke_linecap='round'))
            elif kind == 'lan':
                self.add('labels', line(sx0, sy, sx1, sy, stroke=LAN_C[1], stroke_width=6.2, stroke_linecap='round'))
                self.add('labels', line(sx0, sy, sx1, sy, stroke=LAN_C[0], stroke_width=4.4, stroke_linecap='round'))
            elif kind == 'wlan':
                self.add('labels', line(sx0, sy, sx1, sy, stroke=TEAL, stroke_width=2, stroke_dasharray='2 6',
                                        stroke_linecap='round'))
            lines = wrap(lab, size, w - 58)
            for k, ln in enumerate(lines):
                self.add('labels', text(x + 58, y + k * (size + 4), ln, size=size, fill=INK))
            y += len(lines) * (size + 4) + 10
        return y

    def footer(self, s):
        self.foot = s

    # ------------------------------------------------------------- info band (3 Karten, gleiche Höhe)
    def _h_steps(self, items, w, size):
        return sum(len(wrap(t, size, w - 34)) * (size + 4) + 10 for t in items)

    def _h_bullets(self, items, w, size):
        return sum(len(wrap(t, size, w - 16)) * (size + 4) + 8 for t in items)

    def _h_legend(self, items, w, size):
        return sum(len(wrap(lab, size, w - 58)) * (size + 4) + 10 for _, _, lab in items)

    def info_band(self, y0, steps, notes, legend, extra=None, size=14):
        cols = ((32, 404), (452, 404), (872, self.W - 32 - 872))
        h_extra = (24 + (size + 4) * len(extra)) if extra else 0
        need = max(self._h_steps(steps, 364, size), self._h_bullets(notes, 364, size),
                   self._h_legend(legend, cols[2][1] - 40, size) + h_extra)
        ch = 58 + need + 14
        x, y = self.card(cols[0][0], y0, cols[0][1], ch, 'So wird angeschlossen')
        self.steps_block(x, y, 364, steps, size=size)
        x, y = self.card(cols[1][0], y0, cols[1][1], ch, 'Wichtig')
        self.bullets(x, y, 364, notes, size=size)
        x, y = self.card(cols[2][0], y0, cols[2][1], ch, 'Leitungen')
        y = self.legend(x, y, cols[2][1] - 40, legend, size=size)
        if extra:
            y += 14
            for k, (t, bold) in enumerate(extra):
                self.add('labels', text(x, y + k * (size + 4), t, size=size, weight=700 if bold else None,
                                        fill=INK if bold else TXT2))
        self.H = y0 + ch + 44

    def svg(self, title, desc):
        self.L['bg'] = [rect(0, 0, self.W, self.H, rx=18, fill=self.bg)]
        if self.foot:
            self.add('labels', text(40, self.H - 20, self.foot, size=12, fill=TXT3))
        body = ''.join(''.join(self.L[k]) for k in ('bg', 'zones', 'cables', 'devices', 'over', 'labels'))
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
                'font-family=\'%s\' role="img" aria-label="%s">\n<title>%s</title>\n<desc>%s</desc>\n%s\n%s\n</svg>\n' % (
                    self.W, self.H, self.W, self.H, FONT, esc(title), esc(title), esc(desc), self.D.svg(), body))


SHOP = 'https://edelstahl-tuerklingel.de/'
FOOT = ('Quelle: Metzler Anschlussvorgaben & Systemanleitungen (edelstahl-tuerklingel.de) · Stand 09/2026 · '
        'Arbeiten an 230 V nur durch eine Elektrofachkraft.')


# ================================================================= Export
def write(svg_text, out_dir, base, pdf=True, png=False):
    """Write <base>.svg (+ .pdf, + .png) into out_dir. Returns the list of written paths."""
    os.makedirs(out_dir, exist_ok=True)
    svg_path = os.path.join(out_dir, base + '.svg')
    with open(svg_path, 'w', encoding='utf-8') as fh:
        fh.write(svg_text)
    out = [svg_path]
    if pdf:
        out.append(svg_to_pdf(svg_path, os.path.join(out_dir, base + '.pdf')))
    if png:
        out.append(svg_to_png(svg_path, os.path.join(out_dir, base + '.png')))
    return out


def _chrome():
    for c in ('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', shutil.which('google-chrome'),
              shutil.which('chromium'), shutil.which('chrome')):
        if c and os.path.exists(c):
            return c
    return None


def _svg_size(txt):
    m = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', txt)
    return (float(m.group(1)), float(m.group(2))) if m else (1280.0, 1100.0)


def _run_chrome(args, out_path, limit=90):
    """Headless Chrome often keeps running after writing its output – stop it once the file is complete."""
    if os.path.exists(out_path):
        os.remove(out_path)
    proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0, sizes = time.time(), []
    try:
        while time.time() - t0 < limit and proc.poll() is None:
            if os.path.exists(out_path):
                sizes.append(os.path.getsize(out_path))
                if len(sizes) >= 3 and sizes[-1] > 0 and sizes[-1] == sizes[-2] == sizes[-3]:
                    break
            time.sleep(0.5)
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(5)
            except subprocess.TimeoutExpired:
                proc.kill()
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        raise RuntimeError('Chrome hat keine Datei erzeugt: ' + out_path)


def svg_to_pdf(svg_path, pdf_path):
    """Vector PDF, fonts embedded. rsvg-convert (brew install librsvg) or headless Chrome as fallback."""
    rsvg = shutil.which('rsvg-convert')
    if rsvg:
        subprocess.run([rsvg, '-f', 'pdf', '-o', pdf_path, svg_path], check=True)
        return pdf_path
    chrome = _chrome()
    if not chrome:
        raise RuntimeError('Kein PDF-Konverter gefunden: "brew install librsvg" (rsvg-convert) oder Google Chrome.')
    txt = open(svg_path, encoding='utf-8').read()
    w, h = _svg_size(txt)
    with tempfile.TemporaryDirectory() as td:
        page = os.path.join(td, 'p.html')
        with open(page, 'w', encoding='utf-8') as fh:
            fh.write('<html><head><style>@page{size:%gpx %gpx;margin:0}html,body{margin:0}</style></head>'
                     '<body>%s</body></html>' % (w, h, txt))
        _run_chrome([chrome, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                     '--user-data-dir=' + os.path.join(td, 'prof'), '--print-to-pdf=' + pdf_path,
                     'file://' + page], pdf_path)
    return pdf_path


def svg_to_png(svg_path, png_path, width=1280):
    """PNG preview for the visual check. rsvg-convert, or headless Chrome (native size) as fallback."""
    rsvg = shutil.which('rsvg-convert')
    if rsvg:
        subprocess.run([rsvg, '-w', str(width), '-o', png_path, svg_path], check=True)
        return png_path
    chrome = _chrome()
    if not chrome:
        raise RuntimeError('Kein PNG-Konverter gefunden: "brew install librsvg" (rsvg-convert) oder Google Chrome.')
    w, h = _svg_size(open(svg_path, encoding='utf-8').read())
    with tempfile.TemporaryDirectory() as td:
        _run_chrome([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                     '--user-data-dir=' + os.path.join(td, 'prof'), '--window-size=%d,%d' % (round(w), round(h)),
                     '--screenshot=' + os.path.abspath(png_path), 'file://' + os.path.abspath(svg_path)], png_path)
    return png_path
