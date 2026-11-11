# hamster.html = new.html layout, warm hamster theme (colour remap + small override layer)
import re,sys
src,out=sys.argv[1],sys.argv[2]
s=open(src).read()
M={ # blues/navy -> warm ink / hamster gold
'#0D2E63':'#1E1A17','#0B1640':'#1E1A17','#123B7A':'#2E2722','#082F5F':'#1E1A17','#0D4A94':'#2E2722','#155FB5':'#C9711F',
'#1C74D9':'#D9822B','#1068DC':'#D9822B','#1C5FC8':'#C9711F','#4DA3F0':'#F0A24B','#0066CC':'#B8641A',
'#B3D8FF':'#F5C98C','#D9ECFF':'#FBE3C2','#EEF6FF':'#FFF4E3','#D6E6FF':'#FBE3C2','#EAF2FF':'#FFF4E3','#EAF1FB':'#EEECE8','#F2F5FA':'#EEECE8',
'#DCE4F0':'#E3DDD4','#4A5874':'#5E5953','#6B7A94':'#7A736B','#2B3A55':'#3A332D','#F5F5F7':'#EEECE8','#2D3590':'#3A332D','#5B6CFF':'#F0A24B','#cfd6ff':'#FFE2B5',
}
RG={'13,46,99':'60,35,10','77,163,240':'240,162,75','28,116,217':'217,130,43','11,22,64':'30,26,23'}
import colorsys
def warm(r,g,b):
  h,l,sa=colorsys.rgb_to_hls(r/255,g/255,b/255)
  if sa<.12 or not (190/360<=h<=245/360): return None
  if l<.3: h2,s2=28/360,min(sa,.18)      # dark navy -> warm ink
  elif l>.82: h2,s2=36/360,min(sa,.75)   # pale blue -> cream
  else: h2,s2=30/360,max(sa,.6)          # mid blue -> hamster orange
  r2,g2,b2=colorsys.hls_to_rgb(h2,l if l>.82 or l<.3 else min(l,.55),s2)
  return int(r2*255+.5),int(g2*255+.5),int(b2*255+.5)
def hexw(m):
  h=m.group(1);w=warm(int(h[:2],16),int(h[2:4],16),int(h[4:],16))
  return m.group(0) if not w else '#%02X%02X%02X'%w
def rgbw(m):
  w=warm(int(m.group(1)),int(m.group(2)),int(m.group(3)))
  return m.group(0) if not w else 'rgba(%d,%d,%d,'%w
def fix(css):
  for a,b in M.items(): css=re.sub(re.escape(a),b,css,flags=re.I)
  for a,b in RG.items(): css=re.sub(r'rgba\(\s*'+a.replace(',',r'\s*,\s*'),'rgba('+b,css)
  css=re.sub(r'#([0-9A-Fa-f]{6})\b',hexw,css)
  css=re.sub(r'rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,',rgbw,css)
  return css
s=re.sub(r'(<style[^>]*>)(.*?)(</style>)',lambda m:m.group(1)+fix(m.group(2))+m.group(3),s,flags=re.S)
s=re.sub(r'style="([^"]*)"',lambda m:'style="'+fix(m.group(1))+'"',s)
s=re.sub(r'(<svg.*?</svg>)',lambda m:fix(m.group(1)),s,flags=re.S)
LAYER='''<link href="https://fonts.googleapis.com/css2?family=Kanit:wght@500;600;700;800&display=swap" rel="stylesheet">
<style id="hamster-theme">
:root{--display:"Kanit","IBM Plex Sans Thai",system-ui,sans-serif;--ink:#1E1A17;--mute:#5E5953;--alt:#EEECE8;--navy:#1E1A17;--link:#B8641A}
html,body{background:#EEECE8}
.nav{background:rgba(238,236,232,.86)!important;border-bottom-color:rgba(30,26,23,.07)!important}
/* hero = the golden hamster pad, still fits the first screen */
.zq{margin:12px clamp(10px,1.4vw,20px) 0;border-radius:clamp(32px,4vw,56px);min-height:calc(100svh - 84px)!important;background:#F0A24B!important}
.zq-sky{background:radial-gradient(60% 55% at 50% 38%,#FFE2B5 0%,rgba(255,226,181,0) 70%)!important}
.zq-q{color:rgba(30,26,23,.72)!important}
.zq-s{background:#fff!important;border-color:transparent!important;box-shadow:0 18px 40px -20px rgba(90,45,0,.55)!important}
.zq-go{background:#1E1A17!important;box-shadow:none!important}
.zq-pop{color:rgba(30,26,23,.7)!important}.zq-pop button{background:rgba(255,255,255,.55)!important;border-color:transparent!important;color:#1E1A17!important}
.zq-pop button:hover{background:#fff!important}
.zq-more{color:#1E1A17!important}
h1:not(.zq-h),h2,h3{font-family:var(--display)}
.zq-ham{width:210px!important;height:150px!important;right:70px!important}.zq-hb{width:176px!important;margin:0 auto}.zq-sw{margin-top:104px!important}
.login::after{background:#F0A24B!important}.login,.login *{border-color:#1E1A17}
.nav a[href*="hamsterhub.co/login"]{background:#1E1A17!important;box-shadow:none!important;color:#fff!important}
@media(max-width:640px){.zq-ham{width:130px!important;height:96px!important;right:24px!important}.zq-hb{width:108px!important}.zq{margin:8px 8px 0}.zq-sw{margin-top:62px!important}}
</style>'''
s=s+LAYER
open(out,'w').write(s)
