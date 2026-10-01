#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baut Metzler-Anschlussschemata als SVG + PDF (+ PNG zur Sichtkontrolle).

  python3 build.py --list                                  # verfügbare Schemata
  python3 build.py --out ./schemata                         # alle 5 Referenzschemata
  python3 build.py --out ./schemata vdm10-lan-poe --png     # eines (id oder Dateiname)
  python3 build.py --module mein_schema.py --out . --png    # eigenes Schema-Modul mit SCHEMES-Liste

Ein Schema-Modul definiert   SCHEMES = [(id, dateiname_ohne_endung, funktion), ...]
und jede Funktion gibt den SVG-Text zurück (siehe neues_schema.py).
Nach jedem Lauf werden Layout-Warnungen ausgegeben – trotzdem immer das PNG ansehen.
"""
import argparse
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import scheme  # noqa: E402


def load(module_path):
    if not module_path:
        import referenz
        return referenz.SCHEMES
    spec = importlib.util.spec_from_file_location('schema_modul', os.path.abspath(module_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SCHEMES


def main():
    ap = argparse.ArgumentParser(description='Metzler Anschlussschemata bauen (SVG + PDF).')
    ap.add_argument('ids', nargs='*', help='nur diese ids / Dateinamen bauen')
    ap.add_argument('--module', help='eigenes Schema-Modul (.py mit SCHEMES)')
    ap.add_argument('--out', default='.', help='Ausgabeordner (Standard: aktueller Ordner)')
    ap.add_argument('--no-pdf', action='store_true', help='kein PDF erzeugen')
    ap.add_argument('--png', action='store_true', help='zusätzlich PNG-Vorschau (1280 px)')
    ap.add_argument('--list', action='store_true', help='Schemata auflisten')
    a = ap.parse_args()

    schemes = load(a.module)
    if a.list:
        for sid, base, _ in schemes:
            print('%-28s %s' % (sid, base))
        return 0
    built = 0
    for sid, base, fn in schemes:
        if a.ids and sid not in a.ids and base not in a.ids:
            continue
        svg = fn()
        warns = scheme.last_scene().check()
        for path in scheme.write(svg, a.out, base, pdf=not a.no_pdf, png=a.png):
            print('geschrieben:', path)
        for w in warns:
            print('  ⚠', w)
        built += 1
    if not built:
        print('Nichts gebaut – id prüfen (--list).')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
