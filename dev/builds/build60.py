import re,json
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build59.py').read())
# ---- 1. aurora: render textures once, animate with GPU transforms only
i=s.index('/* Hall of Fame: golden aurora curtains */');j=s.index('  /* walker follows the rift',i)
s=s[:i]+r'''/* Hall of Fame: aurora textures drawn once, moved by the GPU */
  (function(){var host=$('#h5Au');if(!host)return;var W=1024,H=420;
    function tex(seed,R){var c=document.createElement('canvas');c.width=W;c.height=H;var x=c.getContext('2d');x.globalCompositeOperation='lighter';
      R.forEach(function(r,k){for(var i=0;i<W;i+=2){var u=i/W,P=6.2832,yc=H*(r.y+r.a*Math.sin(u*r.f*P+seed)+.03*Math.sin(u*11*P/11*2+k+seed)),hh=H*r.h*(.6+.4*Math.sin(u*4*P/4*2+k*1.7+seed)),
          st=.5+.5*Math.sin(u*96*P/6.2832*6.2832/6.2832+k*3)*Math.sin(u*38*P/6.2832+seed),al=r.k*(.10+.22*st)*(.6+.4*Math.sin(u*2*P+k+seed));
          var g=x.createLinearGradient(0,yc-hh,0,yc+hh*.25);g.addColorStop(0,'rgba('+r.c+',0)');g.addColorStop(.75,'rgba('+r.c+','+al.toFixed(3)+')');g.addColorStop(.86,'rgba(255,255,240,'+Math.min(1,al*1.4).toFixed(3)+')');g.addColorStop(1,'rgba('+r.c+',0)');x.fillStyle=g;x.fillRect(i,yc-hh,2,hh*1.25)}});
      return c.toDataURL('image/webp',.82)}
    var A=tex(0,[{y:.30,a:.08,f:2,h:.34,c:[255,214,120],k:.9},{y:.52,a:.07,f:1,h:.3,c:[236,170,70],k:.8}]),
        B=tex(2,[{y:.42,a:.10,f:3,h:.26,c:[255,240,190],k:.75},{y:.34,a:.05,f:4,h:.16,c:[255,252,236],k:.6}]);
    var d=document.createElement('div');d.className='h5f-au2';d.setAttribute('aria-hidden','true');d.innerHTML='<i style="background-image:url('+A+')"></i><i style="background-image:url('+B+')"></i>';host.replaceWith(d)})();
  /* pause every Hall of Fame animation while it is off screen */
  (function(){var sec=$('.h5f');if(!sec)return;var all=[sec].concat([].slice.call(document.querySelectorAll('.rau,.rsd,#wkRift')));
    new IntersectionObserver(function(e){var off=!e[0].isIntersecting;all.forEach(function(n){n.classList.toggle('zz-off',off)})},{rootMargin:'120px'}).observe(sec)})();
'''+s[j:]
# ---- 2. edge strands: two static textures, cross-faded
i=s.index('/* rift edge: short aurora strands spilling out of the crack */');j=s.index('  /* activity list */',i)
s=s[:i]+r'''/* rift edge: strands drawn once per size, two variants cross-fade */
  (function(){var sec=$('.h5f'),hT=$('#rauT'),hB=$('#rauB');if(!sec||!hT)return;var ET='''+json.dumps([[x/1000,y] for x,y in T])+''',EB='''+json.dumps([[x/1000,y] for x,y in B])+''',H=96,M=50,lastW=0;
    function ey(E,f){for(var i=1;i<E.length;i++){if(f<=E[i][0]){var a=E[i-1],b=E[i],k=(f-a[0])/((b[0]-a[0])||1);return a[1]+(b[1]-a[1])*k}}return E[E.length-1][1]}
    function strip(W,E,up,ph){var c=document.createElement('canvas');c.width=W;c.height=H;var x=c.getContext('2d');x.shadowColor='rgba(255,190,70,.55)';x.shadowBlur=4;
      for(var i=0;i<W;i+=2){var f=i/W,e=ey(E,f),y0=up?(M+e):(H-M-e),n=Math.sin(f*70+ph)*Math.sin(f*23-ph*.6)+Math.sin(f*140+ph*1.7)*.35,len=Math.max(0,10+30*(.5+.5*n)),al=Math.min(1,.45+.55*(.5+.5*n));
        var g=x.createLinearGradient(0,y0,0,up?y0-len:y0+len);g.addColorStop(0,'rgba(232,160,40,'+al.toFixed(3)+')');g.addColorStop(.3,'rgba(246,196,84,'+(al*.8).toFixed(3)+')');g.addColorStop(1,'rgba(255,224,140,0)');x.fillStyle=g;x.fillRect(i,up?y0-len:y0,1.4,len)}
      return c}
    function build(){var Wc=sec.clientWidth;if(!Wc||Math.abs(Wc-lastW)<4)return;lastW=Wc;var W=Math.min(1200,Math.round(Wc/1.5));
      [[hT,ET,true],[hB,EB,false]].forEach(function(o){var host=o[0];host.innerHTML='';[0,2.4].forEach(function(ph,k){var c=strip(W,o[1],o[2],ph);c.className='rv'+k;c.style.width=Wc+'px';c.style.height=H+'px';host.appendChild(c)})})}
    var tm;new ResizeObserver(function(){clearTimeout(tm);tm=setTimeout(build,150)}).observe(sec);build()})();
'''+s[j:]
rep('<div class="rau t" aria-hidden="true"><canvas id="rauT"></canvas></div>','<div class="rau t" aria-hidden="true"><div id="rauT"></div></div>')
rep('<div class="rau b" aria-hidden="true"><canvas id="rauB"></canvas></div>','<div class="rau b" aria-hidden="true"><div id="rauB"></div></div>')
# ---- 3. walker on the rift: no layout reads every frame
i=s.index('/* walker follows the rift');j=s.index("})();",i)+5
s=s[:i]+r'''/* walker follows the rift's top edge (offsets cached) */
  (function(){var z=$('#wkRift'),sec=$('.h5f');if(!z||!sec)return;var E='''+json.dumps([[x/1000,y] for x,y in T])+''',o=null;
    function ey(f){for(var i=1;i<E.length;i++){if(f<=E[i][0]){var a=E[i-1],b=E[i],k=(f-a[0])/((b[0]-a[0])||1);return a[1]+(b[1]-a[1])*k}}return E[E.length-1][1]}
    function m(){var zr=z.getBoundingClientRect(),sr=sec.getBoundingClientRect();o={dx:zr.left-sr.left,w:sr.width,dy:sr.top-(zr.bottom-4)}}
    new ResizeObserver(m).observe(sec);addEventListener('resize',m);
    z.__g=function(lx){if(!o||!o.w)m();var f=(o.dx+lx)/o.w;return o.dy+ey(Math.max(0,Math.min(1,f)))}})();'''+s[j:]
# ---- 4. login comet: transform rotation instead of animating a custom property
rep('<i class="lg-cm" aria-hidden="true"></i>','<i class="lg-cm" aria-hidden="true"></i><i class="lg-in" aria-hidden="true"></i>')
css=r'''
/* ===== v60: performance ===== */
/* aurora layers move on the compositor */
.h5f-au2{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.h5f-au2 i{position:absolute;left:0;top:0;width:200%;height:100%;background-size:50% 100%;background-repeat:repeat-x;will-change:transform;animation:au2 48s linear infinite}
.h5f-au2 i:nth-child(2){animation-duration:70s;animation-direction:reverse;opacity:.9}
@keyframes au2{to{transform:translate3d(-50%,0,0)}}
.h5f-au{display:none!important}
/* edge strands: two baked textures cross-fade */
.rau>div{position:absolute;left:0}
.rau.t>div{top:-80px}.rau.b>div{top:-10px}
.rau canvas{position:absolute;left:0;top:0;filter:none!important;will-change:opacity}
.rau canvas.rv1{opacity:0;animation:rvX 2.6s ease-in-out infinite alternate}
.rau canvas.rv0{animation:rvX 2.6s ease-in-out infinite alternate-reverse}
@keyframes rvX{from{opacity:0}to{opacity:1}}
/* cheaper glows: animate opacity of pre-rendered layers, not filters */
.h5f-rt{will-change:opacity;animation:rtF2 3.2s ease-in-out infinite}
.h5f-rt.b{animation-delay:-1.6s}
.h5f-rt polyline{animation:none!important;filter:drop-shadow(0 0 4px #FFD36B) drop-shadow(0 0 10px rgba(255,190,70,.8))!important}
@keyframes rtF2{0%,100%{opacity:.8}45%{opacity:1}50%{opacity:.6}55%{opacity:1}}
.h5f-tear .g{animation:none!important;stroke-width:28!important;opacity:.75}
.h5f-tear{will-change:opacity;animation:tearO 4s ease-in-out infinite}
@keyframes tearO{0%,100%{opacity:.8}50%{opacity:1}}
.h5f-tear .c{animation:tearDraw 2.4s cubic-bezier(.6,0,.2,1) .2s forwards!important}
.sd{filter:none!important;will-change:transform,opacity}
.sd.g,.sd.w{box-shadow:none}
.h5f-du b{box-shadow:0 0 6px 1px rgba(255,210,110,.7);will-change:transform}
.h5f-du b:nth-child(3n){display:none}
.h5f-c{will-change:transform}
/* paused while off screen */
.zz-off,.zz-off *,.zz-off *::before,.zz-off *::after{animation-play-state:paused!important}
/* login comet: rotate a layer instead of repainting a gradient */
.login{overflow:hidden!important;isolation:isolate}
.lg-cm{inset:auto!important;left:50%!important;top:50%!important;width:180%!important;height:auto!important;aspect-ratio:1;padding:0!important;translate:-50% -50%;-webkit-mask:none!important;mask:none!important;filter:none!important;z-index:0;
  background:conic-gradient(from 0deg,transparent 0 60%,rgba(127,196,255,.2) 70%,#7FC4FF 86%,#fff 90%,transparent 93%)!important;animation:cmR2 3.2s linear infinite!important;will-change:transform}
@keyframes cmR2{to{transform:rotate(360deg)}}
.login:hover .lg-cm{animation-duration:1.1s!important}
.lg-in{position:absolute;inset:2px;border-radius:inherit;background:linear-gradient(180deg,#16336B,#0D2350);z-index:0;pointer-events:none}
.login:hover .lg-in{background:linear-gradient(180deg,#1C4489,#123068)}
.lg-t{position:relative;z-index:1}
/* skip rendering of sections far below the screen */
.zb,.zp,.mc,.ptn,.end{content-visibility:auto;contain-intrinsic-size:auto 900px}
/* lighter blur on the sticky nav */
.nav{-webkit-backdrop-filter:blur(12px)!important;backdrop-filter:blur(12px)!important}
@media (prefers-reduced-motion:reduce){.h5f-au2 i,.rau canvas,.h5f-rt,.h5f-tear,.lg-cm{animation:none!important}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v60.html','w').write(s)
print('v60 ok')
