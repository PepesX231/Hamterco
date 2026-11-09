import random,json
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build56.py').read())
# ---------- login: crisp pill with a comet of light running the border
i=s.index('<i class="lg-orb" aria-hidden="true"></i>');s=s[:i]+'<i class="lg-cm" aria-hidden="true"></i>'+s[i+len('<i class="lg-orb" aria-hidden="true"></i>'):]
# ---------- walker on the rift edge
rep('<div class="wkz"><img class="wk" src="img/n-gamer.webp"','<div class="wkz wkz-rift" id="wkRift"><img class="wk" src="img/n-gamer.webp"')
rep("h.style.transform='translate('+x+'px,'+(y+bob)+'px) rotate('+rot+'deg)","var gy=z.__g?z.__g(x+h.offsetWidth/2):0;h.style.transform='translate('+x+'px,'+(y+bob+gy)+'px) rotate('+rot+'deg)")
rep("sh.style.transform='translateX('+(x+h.offsetWidth/2)+'px) translateX(-50%)","sh.style.transform='translate('+(x+h.offsetWidth/2)+'px,'+(z.__g?z.__g(x+h.offsetWidth/2):0)+'px) translateX(-50%)")
# ---------- shards + embers around the rift
random.seed(41)
def shards(n,side):
    out=''
    for k in range(n):
        x=random.uniform(2,98);sz=random.randint(6,18);y=random.randint(-8,40) if side=='t' else random.randint(-40,8)
        pts=['%d%% %d%%'%(random.randint(0,40),random.randint(0,30)),'%d%% %d%%'%(random.randint(60,100),random.randint(10,50)),'%d%% %d%%'%(random.randint(20,70),random.randint(70,100))]
        out+='<i class="sd %s" style="left:%.1f%%;top:%dpx;width:%dpx;height:%dpx;clip-path:polygon(%s);--d:%.1fs;--dl:-%.1fs;--dx:%dpx;--dy:%dpx;--r:%ddeg"></i>'%(random.choice(['g','k','k','w']),x,y,sz,int(sz*1.3),','.join(pts),random.uniform(5,9),random.uniform(0,8),random.randint(-24,24),(-1 if side=='t' else 1)*random.randint(18,46),random.randint(-160,160))
    return out
rep('<section class="h5f" aria-label="Hall of Fame">','<div class="rsd t" aria-hidden="true">'+shards(22,'t')+'</div><section class="h5f" aria-label="Hall of Fame">')
i=s.index('<section class="h5f"');j=s.index('</section>',i)+10
s=s[:j]+'<div class="rsd b" aria-hidden="true">'+shards(18,'b')+'</div>'+s[j:]
# inner offset crack lines
tp2=' '.join('%d,%d'%(x,min(47,y+9)) for x,y in T); bp2=' '.join('%d,%d'%(x,max(1,48-y-9)) for x,y in B)
rep('<svg class="h5f-rt t" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polyline points="'+tp+'"/></svg>','<svg class="h5f-rt t" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polyline class="in" points="'+tp2+'"/><polyline points="'+tp+'"/></svg>')
rep('<svg class="h5f-rt b" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polyline points="'+bp+'"/></svg>','<svg class="h5f-rt b" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polyline class="in" points="'+bp2+'"/><polyline points="'+bp+'"/></svg>')
# ---------- sharper aurora: curtain strands
i=s.index('/* Hall of Fame: flowing golden aurora */');j=s.index('  /* activity list */',i)
EDGE=json.dumps([[x/1000,y] for x,y in T])
s=s[:i]+r'''/* Hall of Fame: golden aurora curtains */
  (function(){var c=$('#h5Au');if(!c)return;var x=c.getContext('2d'),W=960,H=540,t=0,on=false,rq=0,red=matchMedia('(prefers-reduced-motion:reduce)').matches;c.width=W;c.height=H;
    var R=[{y:.26,a:.08,f:1.3,s:.22,h:.34,c:[255,214,120],k:.9},{y:.40,a:.10,f:2.1,s:-.18,h:.26,c:[255,240,190],k:.7},{y:.55,a:.07,f:1.0,s:.15,h:.3,c:[236,170,70],k:.8},{y:.33,a:.05,f:3.2,s:.3,h:.16,c:[255,252,236],k:.55}];
    function draw(){x.clearRect(0,0,W,H);x.globalCompositeOperation='lighter';
      R.forEach(function(r,k){for(var i=0;i<=W;i+=2){var u=i/W,yc=H*(r.y+r.a*Math.sin(u*r.f*6.28+t*r.s)+.03*Math.sin(u*11+t*r.s*2.4+k)),hh=H*r.h*(.6+.4*Math.sin(u*4.2+t*.5+k*1.7)),
          st=.5+.5*Math.sin(u*90+k*3+t*.9)*Math.sin(u*37-t*.4),al=r.k*(.10+.22*st)*(.6+.4*Math.sin(u*6-t*.7+k));
          var g=x.createLinearGradient(0,yc-hh,0,yc+hh*.25);g.addColorStop(0,'rgba('+r.c+',0)');g.addColorStop(.75,'rgba('+r.c+','+al.toFixed(3)+')');g.addColorStop(.86,'rgba(255,255,240,'+(al*1.4).toFixed(3)+')');g.addColorStop(1,'rgba('+r.c+',0)');
          x.fillStyle=g;x.fillRect(i,yc-hh,2,hh*1.25)}})}
    function loop(){rq=0;if(!on)return;t+=.014;draw();rq=requestAnimationFrame(loop)}
    new IntersectionObserver(function(e){on=e[0].isIntersecting&&!red;if(on&&!rq)rq=requestAnimationFrame(loop)}).observe(c);draw()})();
  /* walker follows the rift's top edge */
  (function(){var z=$('#wkRift'),sec=$('.h5f');if(!z||!sec)return;var E='''+EDGE+''';
    function ey(f){for(var i=1;i<E.length;i++){if(f<=E[i][0]){var a=E[i-1],b=E[i],k=(f-a[0])/((b[0]-a[0])||1);return a[1]+(b[1]-a[1])*k}}return E[E.length-1][1]}
    z.__g=function(lx){var zr=z.getBoundingClientRect(),sr=sec.getBoundingClientRect();var f=(zr.left+lx-sr.left)/sr.width;return (sr.top+ey(Math.max(0,Math.min(1,f))))-(zr.bottom-4)}})();
'''+s[j:]
css=r'''
/* ===== v57 ===== */
/* login: crisp, with a comet tracing the border */
@property --cm{syntax:"<angle>";inherits:false;initial-value:0deg}
.login{animation:none!important;background:linear-gradient(180deg,#16336B,#0D2350)!important;padding:8px 20px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.18),inset 0 0 0 1px rgba(130,180,255,.28),0 6px 16px -8px rgba(13,46,99,.7)!important}
.login::before{display:none!important}
.lg-cm{position:absolute;inset:-1px;border-radius:inherit;padding:2px;pointer-events:none;background:conic-gradient(from var(--cm),transparent 0 55%,rgba(127,196,255,.15) 62%,#7FC4FF 84%,#fff 91%,transparent 93%);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask:linear-gradient(#000 0 0) content-box exclude,linear-gradient(#000 0 0);animation:cmR 3.2s linear infinite;filter:drop-shadow(0 0 4px rgba(127,196,255,.9))}
@keyframes cmR{to{--cm:360deg}}
.lg-t{animation:none!important;text-shadow:none!important;color:#fff}
.login:hover{background:linear-gradient(180deg,#1C4489,#123068)!important;transform:translateY(-1px);box-shadow:inset 0 1px 0 rgba(255,255,255,.25),inset 0 0 0 1px rgba(150,200,255,.5),0 0 0 4px rgba(77,163,240,.15),0 10px 22px -8px rgba(28,116,217,.7)!important}
.login:hover .lg-cm{animation-duration:1.1s}
.lg-orb{display:none!important}
/* aurora: sharp curtains */
.h5f-au{filter:blur(1.5px) saturate(130%) brightness(1.2)!important;inset:0!important;width:100%!important;height:100%!important}
/* layered crack: inner faint line */
.h5f-rt polyline.in{stroke:rgba(255,215,130,.45)!important;stroke-width:1.2!important;stroke-dasharray:6 10;filter:drop-shadow(0 0 6px rgba(255,190,70,.6))!important;animation:inD 3s linear infinite!important}
@keyframes inD{to{stroke-dashoffset:-64}}
/* shards breaking off the rift */
.rsd{position:relative;height:0;z-index:5;pointer-events:none;overflow-x:clip;overflow-y:visible}
.rsd.t{top:-6px}.rsd.b{top:-38px}
.sd{position:absolute;display:block;animation:sdF var(--d) ease-in-out var(--dl) infinite}
.sd.k{background:linear-gradient(135deg,#2A1F0E,#0B0805);box-shadow:none;outline:1px solid rgba(255,214,130,.5);outline-offset:-1px}
.sd.g{background:linear-gradient(135deg,#FFF1C2,#E2A93A);filter:drop-shadow(0 0 6px rgba(255,190,70,.9))}
.sd.w{background:#FFF8E2;filter:drop-shadow(0 0 8px #FFD36B)}
@keyframes sdF{0%{transform:translate(0,0) rotate(0);opacity:0}15%{opacity:1}100%{transform:translate(var(--dx),var(--dy)) rotate(var(--r));opacity:0}}
/* the walker above the rift: walks on the edge, lit by the gold */
.wkz-rift{position:relative;z-index:6;margin-bottom:-4px}
.wkz-rift .wk{filter:drop-shadow(0 0 10px rgba(255,200,90,.55)) drop-shadow(0 6px 4px rgba(0,0,0,.25))}
.wkz-rift .wk-sh{background:radial-gradient(closest-side,rgba(255,200,90,.55),transparent)!important}
@media (prefers-reduced-motion:reduce){.sd,.lg-cm,.h5f-rt polyline.in{animation:none!important}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v57.html','w').write(s)
print('v57 ok')
