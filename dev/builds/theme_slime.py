# slime.html = new.html layout untouched + "Slime Pad" theme
#   colour pads with little faces (mousepad ref) + glossy slime drips + jelly buttons
# usage: python3 dev/builds/theme_slime.py new.html slime.html
import re, sys, colorsys
src, out = sys.argv[1], sys.argv[2]
s = open(src).read()

# ---- 1. recolour the old blue system to ink / neutral / salmon accent ----
def remap(r, g, b):
    h, l, sa = colorsys.rgb_to_hls(r/255, g/255, b/255)
    if sa < .12 or not (190/360 <= h <= 245/360):
        return None
    if l < .32:   nh, nl, ns = 25/360, min(l, .09), .25       # navy -> warm ink
    elif l > .8:  nh, nl, ns = 36/360, max(l, .93), .9       # pale blue -> cream
    elif sa > .5: nh, nl, ns = 28/360, .45, .8               # bright blue -> deep hamster orange
    else:         nh, nl, ns = 25/360, .32, .1               # slate -> warm grey
    r2, g2, b2 = colorsys.hls_to_rgb(nh, nl, ns)
    return round(r2*255), round(g2*255), round(b2*255)
def hx(m):
    h = m.group(1); w = remap(int(h[:2],16), int(h[2:4],16), int(h[4:],16))
    return m.group(0) if not w else '#%02X%02X%02X' % w
def rg(m):
    w = remap(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return m.group(0) if not w else 'rgba(%d,%d,%d,' % w
def fix(css):
    css = re.sub(r'#([0-9A-Fa-f]{6})\b', hx, css)
    return re.sub(r'rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,', rg, css)
s = re.sub(r'(<style[^>]*>)(.*?)(</style>)', lambda m: m.group(1)+fix(m.group(2))+m.group(3), s, flags=re.S)
s = re.sub(r'style="([^"]*)"', lambda m: 'style="'+fix(m.group(1))+'"', s)

# ---- 2. theme layer (appended last so it wins) ----
s += open(__file__.replace('theme_slime.py', 'theme_slime.css.html')).read()
open(out, 'w').write(s)
