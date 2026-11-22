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
# owner, 22 พ.ย.: drop the small explaining lines under headings (he pointed at each one), and the rules between rows
css += '''
html body section.hbx .oc-hd p,html body section.hbx .oc-k,html body section.hbx .oc-t>h3,html body .h5f .h5f-s,html body .mr.lt .mr-l p,html body .t-s{display:none!important}
html body section.hbx .ocl,html body section.hbx .ocl li,html body section.hbx .oc-r,html body section.hbx .oc-t,html body section.hbx .oc-tx{border:0!important;box-shadow:none!important}
html body section.hbx .ocl li{padding-top:.35em!important;padding-bottom:.35em!important}
'''
css = square(css)

def mini(c):
    c = re.sub(r'/\*.*?\*/', '', c, flags=re.S)
    c = re.sub(r'\s+', ' ', c)
    c = re.sub(r'\s*([{};,>])\s*', r'\1', c)
    return c.replace(';}', '}')
css = mini(css)

# "คอร์ส" became Hams Route (22 พ.ย.): every link to the old courses view now opens the Hams Route pages
R = '/Hamterco/next/routes/'
body = body.replace('<a class="v nv-c" href="#courses"><span>คอร์ส</span></a>', '<a class="v nv-c" href="' + R + '"><span>Hams Route</span></a>')
body = body.replace('<a href="#courses">คอร์ส</a>', '<a href="' + R + '">Hams Route</a>')
body = body.replace('href="#courses">ดูคอร์สทั้งหมด', 'href="' + R + '">ดู Hams Route ทั้งหมด')
body = body.replace('href="#courses">คอร์สทั้งหมด', 'href="' + R + '">Hams Route ทั้งหมด')
body = body.replace('href="#courses"', 'href="' + R + '"')
fi = body.find('<footer')
if fi > -1:
    body = body[:fi] + body[fi:].replace('>คอร์ส<', '>Hams Route<')

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(os.path.join(OUT, 'js'))
open(os.path.join(OUT, 'legacy.css'), 'w').write(fix(css))
open(os.path.join(OUT, 'body.html'), 'w').write(fix(body))
# let the Next.js pages run the old page transition when moving between pages (LegacyRuntime)
PT_OLD = "pt.className='pt v-'+v;pt.innerHTML=h;void pt.offsetWidth;pt.classList.add('in')}"
PT_NEW = PT_OLD + "window.HH_pt={build:ptBuild,out:function(){pt.classList.add('out');clearTimeout(ptT);ptT=setTimeout(function(){pt.className='pt';pt.innerHTML=''},1150)}};"
for sc in scripts:
    if 'code' in sc and PT_OLD in sc['code']:
        sc['code'] = sc['code'].replace(PT_OLD, PT_NEW).replace('<b class="cv-t">คอร์ส</b>', '<b class="cv-t">Hams Route</b>')
    # the search answers' "all courses" link opens Hams Route now
    if 'code' in sc:
        sc['code'] = sc['code'].replace("a=el('a','ia-lk','ดูคอร์สทั้งหมด');a.href='#courses'", "a=el('a','ia-lk','ดู Hams Route');a.href='" + R + "'")

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
