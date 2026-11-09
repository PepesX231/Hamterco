import random
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build55.py').read())
random.seed(23)
def edge(depth):
    pts=[];x=0
    while x<1000:
        pts.append((x,random.randint(4,depth)));x+=random.randint(22,64)
    pts.append((1000,random.randint(4,depth)));return pts
T=edge(44);B=edge(44)
clip='polygon('+','.join('%.1f%% %dpx'%(x/10,y) for x,y in T)+','+','.join('%.1f%% calc(100%% - %dpx)'%(x/10,y) for x,y in reversed(B))+')'
tp=' '.join('%d,%d'%(x,y) for x,y in T); bp=' '.join('%d,%d'%(x,48-y) for x,y in B)
# central tear behind the title
random.seed(5);tear=[(500,0)];y=0
while y<110:
    y+=random.randint(14,30);tear.append((500+random.randint(-26,26),y))
tl=' '.join('%d,%d'%p for p in tear)
FX='''<canvas class="h5f-au" id="h5Au" aria-hidden="true"></canvas>
<svg class="h5f-rt t" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polyline points="'''+tp+'''"/></svg>
<svg class="h5f-rt b" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polyline points="'''+bp+'''"/></svg>
<svg class="h5f-tear" viewBox="440 0 120 120" aria-hidden="true"><polyline class="g" points="'''+tl+'''"/><polyline class="c" points="'''+tl+'''"/></svg>'''
rep('<section class="h5f" aria-label="Hall of Fame">','<section class="h5f" aria-label="Hall of Fame">'+FX)
JS=r'''
  /* Hall of Fame: flowing golden aurora */
  (function(){var c=$('#h5Au');if(!c)return;var x=c.getContext('2d'),W=480,H=270,t=0,on=false,rq=0,red=matchMedia('(prefers-reduced-motion:reduce)').matches;c.width=W;c.height=H;
    var R=[{y:.30,a:.10,f:1.6,s:.35,w:.16,c:[255,206,110]},{y:.46,a:.12,f:2.3,s:-.28,w:.12,c:[255,236,180]},{y:.62,a:.09,f:1.2,s:.22,w:.2,c:[230,160,60]},{y:.38,a:.07,f:3.1,s:.5,w:.07,c:[255,250,230]}];
    function draw(){x.clearRect(0,0,W,H);x.globalCompositeOperation='lighter';
      R.forEach(function(r,k){for(var i=0;i<=W;i+=4){var u=i/W,yc=H*(r.y+r.a*Math.sin(u*r.f*6.28+t*r.s)+.04*Math.sin(u*9+t*r.s*2.3+k)),th=H*r.w*(.55+.45*Math.sin(u*5+t*.6+k*2)),al=.18+.16*Math.sin(u*7-t*.8+k);
        var g=x.createLinearGradient(0,yc-th,0,yc+th);g.addColorStop(0,'rgba('+r.c+',0)');g.addColorStop(.5,'rgba('+r.c+','+al.toFixed(3)+')');g.addColorStop(1,'rgba('+r.c+',0)');x.fillStyle=g;x.fillRect(i,yc-th,4,th*2)}})}
    function loop(){rq=0;if(!on)return;t+=.016;draw();rq=requestAnimationFrame(loop)}
    new IntersectionObserver(function(e){on=e[0].isIntersecting&&!red;if(on&&!rq)rq=requestAnimationFrame(loop)}).observe(c);draw()})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v56: Hall of Fame as a golden rift ===== */
.h5f{clip-path:'''+clip+''';margin:-30px 0!important;padding-top:clamp(80px,8vw,110px)!important;padding-bottom:clamp(76px,7vw,100px)!important;position:relative;z-index:2}
.h5f-sp{display:none!important}
.h5f-fx::before{display:none!important}
.h5f-au{position:absolute;inset:-10% -5%;width:110%;height:120%;z-index:0;pointer-events:none;filter:blur(18px) saturate(150%) brightness(1.35);opacity:1;mix-blend-mode:screen}
.h5f-fx::after{display:none!important}
.h5f-fx{z-index:1}
.h5f-r,.h5f-k,.h5f-t,.h5f-s,.h5f-go{position:relative;z-index:3}
.h5f-rt{position:absolute;left:0;width:100%;height:48px;z-index:4;pointer-events:none;overflow:visible}
.h5f-rt.t{top:0}.h5f-rt.b{bottom:0}
.h5f-rt polyline{fill:none;stroke:#FFF3C8;stroke-width:3;vector-effect:non-scaling-stroke;stroke-linejoin:bevel;filter:drop-shadow(0 0 4px #FFD36B) drop-shadow(0 0 12px rgba(255,190,70,.9)) drop-shadow(0 0 26px rgba(255,170,40,.6));animation:rtF 3.2s ease-in-out infinite}
.h5f-rt.b polyline{animation-delay:-1.6s}
@keyframes rtF{0%,100%{opacity:.75}45%{opacity:1}50%{opacity:.55}55%{opacity:1}}
.h5f-tear{position:absolute;left:50%;top:0;width:120px;height:clamp(70px,7vw,96px);transform:translateX(-50%);z-index:1;pointer-events:none;overflow:visible}
.h5f-tear polyline{fill:none;stroke-linejoin:bevel}
.h5f-tear .g{stroke:rgba(255,200,90,.55);stroke-width:26;filter:blur(14px);animation:tearG 4s ease-in-out infinite}
.h5f-tear .c{stroke:#FFF6D8;stroke-width:2;filter:drop-shadow(0 0 6px #FFD36B) drop-shadow(0 0 18px rgba(255,190,70,.9));stroke-dasharray:1200;stroke-dashoffset:1200;animation:tearDraw 2.4s cubic-bezier(.6,0,.2,1) .2s forwards,tearF 3s ease-in-out 2.6s infinite}
@keyframes tearDraw{to{stroke-dashoffset:0}}
@keyframes tearG{0%,100%{opacity:.5;stroke-width:22}50%{opacity:1;stroke-width:34}}
@keyframes tearF{0%,100%{opacity:1}50%{opacity:.6}}
@media (prefers-reduced-motion:reduce){.h5f-rt polyline,.h5f-tear .g,.h5f-tear .c{animation:none;stroke-dashoffset:0}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v56.html','w').write(s)
print('v56 ok')
