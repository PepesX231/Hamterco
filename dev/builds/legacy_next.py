"""Build the parts of the site that are not yet React components into web/public/legacy/.

The old page (new.html + layers, as for slime.html) is rebuilt WITHOUT the layers whose job the Next.js app now does
(home hero, cards, search bar look), then split into:
  legacy.css  - every <style> block, in order
  body.html   - the page body without its header, scripts and styles
  js/NNN.js   - every <script>, in order (run one by one by components/LegacyRuntime.tsx)
  fonts.json  - the Google Fonts stylesheets it uses
Relative img/ paths become /Hamterco/img/.
Usage: python3 dev/builds/legacy_next.py
"""
import glob, json, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP = ['99zzzzzzzzzzzz-herobg.html', '99zzzzzzz-crew.html', '99zzzzzzzzzzzzzzzzz-fx.html', '99zzzzzzzzzzzzzz-q.html']
OUT = os.path.join(ROOT, 'web', 'public', 'legacy')

# 1. build the page with the skipped layers moved aside
tmp = tempfile.mkdtemp()
lay = os.path.join(ROOT, 'dev', 'builds', 'layers')
moved = []
try:
    for n in SKIP:
        p = os.path.join(lay, n)
        if os.path.exists(p):
            shutil.move(p, os.path.join(tmp, n)); moved.append(n)
    page = os.path.join(tmp, 'legacy.html')
    subprocess.check_call([sys.executable, os.path.join(ROOT, 'dev', 'builds', 'theme_slime.py'), os.path.join(ROOT, 'new.html'), page])
    s = open(page).read()
finally:
    for n in moved:
        shutil.move(os.path.join(tmp, n), os.path.join(lay, n))

# the loader is rendered by the Next.js layout itself (so it shows from the first paint); drop the old copy
ld = open(os.path.join(ROOT, 'dev', 'builds', 'parts', 'loader.html')).read()
s = re.sub(r'<div id="hhL".*?</script></div>', '', s, count=1, flags=re.S)

def fix(t):
    return re.sub(r'''(["'(\s=])img/''', r'\1/Hamterco/img/', t)

# 2. split
fonts = re.findall(r'<link[^>]+href="(https://fonts\.googleapis\.com/css2[^"]+)"', s)
css = '\n'.join(m for m in re.findall(r'<style[^>]*>(.*?)</style>', s, flags=re.S))
scripts = []
for m in re.finditer(r'<script([^>]*)>(.*?)</script>', s, flags=re.S):
    attrs, code = m.group(1), m.group(2)
    src = re.search(r'src="([^"]+)"', attrs)
    scripts.append({'src': src.group(1)} if src else {'code': code})
body = re.sub(r'<!doctype[^>]*>|</?html[^>]*>|</?body[^>]*>|<head>.*?</head>|<meta[^>]*>|<title>.*?</title>', '', s, flags=re.S | re.I)
body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.S)
body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.S)
body = re.sub(r'<link[^>]*>', '', body)
# the old header stays in the markup (its scripts need it) but is hidden by LegacyRuntime

# owner: square corners everywhere except true circles and the Hall of Fame (the same rule as the square layer)
def square(css):
    def block(m):
        sel, body = m.group(1), m.group(2)
        if 'h5f' in sel:
            return m.group(0)
        body = re.sub(r'(border(?:-(?:top|bottom)-(?:left|right))?-radius\s*:\s*)([^;}]+)',
                      lambda d: d.group(0) if ('50%' in d.group(2) or d.group(2).strip() in ('0', '0px', 'inherit')) else d.group(1) + '0' + (' !important' if 'important' in d.group(2) else ''), body)
        return sel + '{' + body + '}'
    return re.sub(r'([^{}]+)\{([^{}]*)\}', block, css)
css = square(css)

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(os.path.join(OUT, 'js'))
open(os.path.join(OUT, 'legacy.css'), 'w').write(fix(css))
open(os.path.join(OUT, 'body.html'), 'w').write(fix(body))
names = []
for i, sc in enumerate(scripts):
    if 'src' in sc:
        names.append(sc['src'])
    else:
        n = 'js/%03d.js' % i
        open(os.path.join(OUT, n), 'w').write(fix(sc['code']))
        names.append(n)
json.dump({'fonts': fonts, 'scripts': names}, open(os.path.join(OUT, 'manifest.json'), 'w'), ensure_ascii=False, indent=1)
print('css', len(css), 'body', len(body), 'scripts', len(names))
