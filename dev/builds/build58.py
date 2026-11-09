import random,math
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build57.py').read())
def ey(pts,f):
    X=f*1000
    for i in range(1,len(pts)):
        if X<=pts[i][0]:
            a,b=pts[i-1],pts[i];k=(X-a[0])/((b[0]-a[0]) or 1);return a[1]+(b[1]-a[1])*k
    return pts[-1][1]
# fewer shards
import re
def thin(m):
    items=re.findall(r'<i class="sd[^>]*></i>',m.group(2));return m.group(1)+''.join(items[::3])+'</div>'
s=re.sub(r'(<div class="rsd (?:t|b)" aria-hidden="true">)(.*?)</div>',thin,s,flags=re.S)
# remove dotted inner lines
s=re.sub(r'<polyline class="in" points="[^"]*"/>','',s)
# holy waves following the crack, inside the rift
def wave(pts,off,amp,per,ph,bottom=False):
    out=[]
    for X in range(0,1001,6):
        y=ey(pts,X/1000)+off+amp*math.sin(X/per*6.283+ph)
        out.append('%d,%.1f'%(X,(48-y) if bottom else y))
    return ' '.join(out)
WT='<svg class="h5f-wv t" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="hwg" x1="0" x2="1"><stop offset="0" stop-color="#FFF6D6"/><stop offset=".5" stop-color="#F2C055"/><stop offset="1" stop-color="#FFF6D6"/></linearGradient></defs>'+''.join('<polyline class="w%d" points="%s"/>'%(k,wave(T,o,a,p,ph)) for k,(o,a,p,ph) in enumerate([(9,2.2,70,0),(15,3,120,1.7),(21,1.8,46,3.1)]))+'</svg>'
WB='<svg class="h5f-wv b" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true">'+''.join('<polyline class="w%d" points="%s"/>'%(k,wave(B,o,a,p,ph,True)) for k,(o,a,p,ph) in enumerate([(9,2.2,80,.6),(15,3,110,2.2),(21,1.8,52,4)]))+'</svg>'
rep('<svg class="h5f-rt t"',WT+'<svg class="h5f-rt t"')
# holy weapons planted in the crack (outside the clip)
SWORD='<svg viewBox="0 0 24 84"><defs><linearGradient id="hbl" x1="0" x2="1"><stop offset="0" stop-color="#FFF8E4"/><stop offset=".5" stop-color="#F6D78A"/><stop offset=".51" stop-color="#D9A441"/><stop offset="1" stop-color="#B9832A"/></linearGradient></defs><circle class="hl" cx="12" cy="13" r="10.5"/><circle cx="12" cy="4" r="3" class="gd"/><rect x="10.4" y="7" width="3.2" height="12" rx="1" class="gp"/><path d="M1.5 21c3.5 0 6-1.6 7-3h7c1 1.4 3.5 3 7 3v2.4c-3.5 0-6 .8-7 1.6h-7c-1-.8-3.5-1.6-7-1.6z" class="gd"/><path d="M9 25h6l-.7 46L12 82l-2.3-11z" fill="url(#hbl)" class="bl"/><path d="M12 27v44" class="fl"/></svg>'
SPEAR='<svg viewBox="0 0 24 84"><circle class="hl" cx="12" cy="8" r="9"/><rect x="11" y="2" width="2" height="54" rx="1" class="gp"/><path d="M8.5 55h7l-1 2h-5z" class="gd"/><path d="M12 56l5.5 9L12 83l-5.5-18z" fill="url(#hbl)" class="bl"/><path d="M12 59v20" class="fl"/></svg>'
random.seed(77)
def weapons(pts,side,xs):
    out=''
    for i,f in enumerate(xs):
        y=ey(pts,f);h=random.choice([96,110,124]);w=round(h*24/84);rot=random.randint(-24,24);kind=SWORD if i%3!=1 else SPEAR
        if side=='t': top=round(-30+y-h+24)
        else: top=round(30-y-24);rot=180+rot
        out+='<i class="hw%s" style="left:%.1f%%;top:%dpx;width:%dpx;height:%dpx;--r:%ddeg;--dl:-%.1fs">%s</i>'%(' m' if i%2 else '',f*100,top,w,h,rot,random.uniform(0,5),kind)
    return out
HT='<div class="hwz t" aria-hidden="true">'+weapons(T,'t',[.07,.2,.36,.63,.8,.93])+'</div>'
HB='<div class="hwz b" aria-hidden="true">'+weapons(B,'b',[.12,.3,.55,.72,.9])+'</div>'
rep('<div class="rsd t" aria-hidden="true">',HT+'<div class="rsd t" aria-hidden="true">')
i=s.index('<div class="rsd b" aria-hidden="true">');s=s[:i]+HB+s[i:]
css=r'''
/* ===== v58: holy rift edge ===== */
.h5f-wv{position:absolute;left:0;width:100%;height:48px;z-index:4;pointer-events:none;overflow:visible}
.h5f-wv.t{top:0}.h5f-wv.b{bottom:0}
.h5f-wv polyline{fill:none;stroke:url(#hwg);vector-effect:non-scaling-stroke;stroke-linecap:round;stroke-width:1.6;stroke-dasharray:160 90;animation:hwF 6s linear infinite}
.h5f-wv .w1{stroke-width:1.1;stroke-dasharray:90 140;animation-duration:9s;animation-direction:reverse;opacity:.8}
.h5f-wv .w2{stroke-width:.8;stroke-dasharray:40 60;animation-duration:4.5s;opacity:.6}
@keyframes hwF{to{stroke-dashoffset:-500}}
.hwz{position:relative;height:0;z-index:7;pointer-events:none;overflow-x:clip;overflow-y:visible}
.hw{position:absolute;display:block;margin-left:-17px;transform-origin:50% calc(100% - 24px);transform:rotate(var(--r));animation:hwB 4.6s ease-in-out var(--dl) infinite}
.hw svg{display:block;width:100%;height:100%;overflow:visible}
.hw .gd{fill:#E9B94A;stroke:#5B3B0C;stroke-width:.8}
.hw .gp{fill:#7A4E14;stroke:#3E2706;stroke-width:.6}
.hw .bl{stroke:#6B4A12;stroke-width:.7}
.hw .fl{stroke:rgba(255,255,255,.75);stroke-width:.6}
.hw .hl{fill:none;stroke:rgba(255,226,150,.85);stroke-width:.9;stroke-dasharray:3 2.2;transform-origin:center;transform-box:fill-box;animation:hwH 7s linear infinite}
@keyframes hwH{to{transform:rotate(360deg)}}
@keyframes hwB{0%,100%{filter:brightness(1) drop-shadow(0 0 1.5px rgba(255,215,120,.9))}50%{filter:brightness(1.3) drop-shadow(0 0 3px #FFE39A)}}
.hw.m{animation-duration:5.8s}
@media (max-width:700px){.hw{transform:rotate(var(--r)) scale(.72)}.hwz .hw:nth-child(even){display:none}.hwz.b{display:none}}
@media (prefers-reduced-motion:reduce){.h5f-wv polyline,.hw,.hw .hl{animation:none}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v58.html','w').write(s)
print('v58 ok')
