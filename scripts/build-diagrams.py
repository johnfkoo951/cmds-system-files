#!/usr/bin/env python3
"""Render the Pele diagrams in diagrams/src/<slug>-{en,ko}.md and inline them into
index.html / docs/index.html between
    <!-- diagram:<slug>:begin -->  ...  <!-- diagram:<slug>:end -->
Each marker pair receives one <figure> holding the en and ko variants, each at two
widths (720 desktop, 340 phone). Theme follows the page: the SVGs use var(--pele-*)
and assets/pele/cmds-pele.css maps them from the page tokens (data-cp-theme="auto").

Usage: build-diagrams.py [--only slug,slug] [--check]
  --check   render + compare, change nothing (exit 1 if a page would change)
Requires /Users/yohankoo/DEV/cmds-pele (pele-render.py, Playwright Chromium).
"""
import argparse, html, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC, OUT = ROOT / 'diagrams' / 'src', ROOT / 'diagrams' / 'out'
PAGES = [ROOT / 'index.html', ROOT / 'docs' / 'index.html']
PELE_RENDER = Path('/Users/yohankoo/DEV/cmds-pele/bin/pele-render.py')
PY = Path.home() / '.pyenv/versions/3.13.12/bin/python3'
FONT = '"Pretendard", "SF Pro Text", -apple-system, system-ui, sans-serif'
MONO = "ui-monospace, 'SF Mono', Menlo, Monaco, Consolas, monospace"
WIDTHS = [680, 340]  # 680 fits 1:1 inside the 720px content column minus card padding
LANGS = ['en', 'ko']


def caption_of(md: str) -> str:
    """Italic line right after the closing fence is the caption (vault convention)."""
    m = re.search(r'^```\s*$\n\s*\*(.+?)\*\s*$', md, re.M)
    return m.group(1).strip() if m else ''


def render(slug: str, lang: str) -> dict:
    src = SRC / f'{slug}-{lang}.md'
    out = OUT / f'{slug}-{lang}'
    cmd = [str(PY), str(PELE_RENDER), str(src), '-o', str(out), '--theme', 'auto', '--profile', 'screen',
           '--widths', ','.join(map(str, WIDTHS)), '--format', 'json', '--font', FONT, '--mono', MONO]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f'pele-render failed for {src.name}:\n{r.stdout}\n{r.stderr}')
    report = json.loads((out / 'pele-render.json').read_text())
    res = report['results'][0]
    if not res.get('ok'):
        sys.exit(f'{src.name}: {res.get("error")} {res.get("detail", "")}')
    data = json.loads((out / f"{res['name']}.json").read_text())
    data['caption'] = caption_of(src.read_text()) or data.get('caption') or ''
    return data


def caption_html(text: str) -> str:
    """Escape, then turn `code` spans into <code>."""
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', html.escape(text, quote=False))


def fragment(slug: str, variants: dict) -> str:
    """variants: {lang: data}"""
    parts = [f'<figure class="cmds-figure diagram-card" data-diagram="{slug}">']
    for lang in LANGS:
        d = variants[lang]
        alt = html.escape(d.get('alt') or d['caption'] or slug, quote=True)
        parts.append(f'<div class="diagram-lang {lang}-only" lang="{lang}">')
        for w in WIDTHS:
            v = d['variants'][str(w)]
            parts.append(f'<div class="cmds-pele cp-w{w}" data-cp-theme="auto" role="img" aria-label="{alt}" style="--w:{v["width"]}px">{v["svg"]}</div>')
        parts.append('</div>')
    cap = ''.join(f'<span class="{lang}-only">{caption_html(variants[lang]["caption"])}</span>' for lang in LANGS if variants[lang]['caption'])
    if cap:
        parts.append(f'<figcaption>{cap}</figcaption>')
    parts.append('</figure>')
    return '\n'.join(parts)


def inject(page: Path, slug: str, frag: str, check: bool) -> bool:
    text = page.read_text()
    pat = re.compile(rf'(<!-- diagram:{re.escape(slug)}:begin -->)(.*?)(<!-- diagram:{re.escape(slug)}:end -->)', re.S)
    m = pat.search(text)
    if not m:
        return False
    new = f'{m.group(1)}\n{frag}\n{m.group(3)}'
    if m.group(0) == new:
        return True
    if not check:
        page.write_text(text[:m.start()] + new + text[m.end():])
    inject.changed.append(f'{page.relative_to(ROOT)}#{slug}')
    return True
inject.changed = []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    slugs = sorted({p.name.rsplit('-', 1)[0] for p in SRC.glob('*-en.md')})
    if a.only:
        slugs = [s for s in slugs if s in a.only.split(',')]
    if not slugs:
        sys.exit('no diagram sources in diagrams/src')
    manifest = {}
    for slug in slugs:
        variants = {lang: render(slug, lang) for lang in LANGS}
        frag = fragment(slug, variants)
        placed = [str(p.relative_to(ROOT)) for p in PAGES if inject(p, slug, frag, a.check)]
        sizes = {lang: {w: [variants[lang]['variants'][str(w)]['width'], variants[lang]['variants'][str(w)]['height']] for w in WIDTHS} for lang in LANGS}
        manifest[slug] = {'type': variants['en']['type'], 'pele': variants['en']['pele'], 'cmdsPele': variants['en']['cmdsPele'],
                          'profile': 'screen', 'font': FONT, 'pages': placed, 'sizes': sizes, 'bytes': len(frag.encode()),
                          'caption': {lang: variants[lang]['caption'] for lang in LANGS}}
        flag = '' if placed else '  (no marker on any page!)'
        print(f"{slug:<16} {variants['en']['type']:<10} " + " ".join(f"{l}{w}={sizes[l][w]}" for w in WIDTHS for l in LANGS) + f" {len(frag)//1024}KB -> {', '.join(placed) or '-'}{flag}")
    if not a.check:
        (ROOT / 'diagrams' / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + '\n')
    if inject.changed:
        print(('would change: ' if a.check else 'updated: ') + ', '.join(inject.changed))
        if a.check:
            sys.exit(1)
    else:
        print('pages already up to date')


if __name__ == '__main__':
    main()
