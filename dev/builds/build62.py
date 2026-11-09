SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build61.py').read())
# walkers: no layout reads per frame
rep("var x=Math.random()*200,y=0,vy=0,","var cw=z.clientWidth,hw=h.offsetWidth||60;new ResizeObserver(function(){cw=z.clientWidth;hw=h.offsetWidth||hw}).observe(z);\n      var x=Math.random()*200,y=0,vy=0,")
rep("function step(now){var W=z.clientWidth-h.offsetWidth;if(seen&&W>0)","function step(now){var W=cw-hw;if(seen&&W>0)")
s=s.replace("z.__g?z.__g(x+h.offsetWidth/2):0","z.__g?z.__g(x+hw/2):0").replace("'translate('+(x+h.offsetWidth/2)+'px,'","'translate('+(x+hw/2)+'px,'")
# walker loop sleeps when off screen
rep("new IntersectionObserver(function(e){seen=e[0].isIntersecting}).observe(z);","var rq=0;new IntersectionObserver(function(e){seen=e[0].isIntersecting;if(seen&&!rq)rq=requestAnimationFrame(step)}).observe(z);")
rep("        requestAnimationFrame(step)}\n      requestAnimationFrame(step);","        rq=seen?requestAnimationFrame(step):0}\n      rq=requestAnimationFrame(step);")
css=r'''
/* ===== v62: performance pass 3 ===== */
@keyframes hfS1{from{background-position:120% 0}to{background-position:0 0}}
.h5f-t{animation:hfS1 2.6s cubic-bezier(.3,.7,.3,1) 1 both!important}
.h5f-im::after{animation:none!important}
.h5f-c:hover .h5f-im::after{animation:h5Sheen 1.6s ease-out 1!important}
.sd:nth-child(2n){display:none}
.rau.t canvas,.rau.b canvas{top:0!important}
.h5f{contain:none!important}
.h5f-rt polyline{filter:drop-shadow(0 0 4px #FFD36B) drop-shadow(0 0 12px rgba(255,190,70,.9)) drop-shadow(0 0 26px rgba(255,170,40,.6))!important}
.h5f-rt,.h5f-tear,.rau,.rau canvas,.h5f-au2 i{will-change:opacity,transform;backface-visibility:hidden}
.h5f-du b:nth-child(4n+2){display:none}
.h5f-du b:nth-child(3n+1){display:none}
.zz-off,.zz-off *,.zz-off *::before,.zz-off *::after{animation-play-state:paused!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
# pause any home/about section's animations when it is off screen
js=r'''  /* v62: sections off screen stop animating */
  (function(){if(!('IntersectionObserver' in window))return;var io=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('zz-off',!e.isIntersecting)})},{rootMargin:'160px'});
    document.querySelectorAll('[data-view] > section:not(.h5f), [data-view] > .zq, .hp-grid, .zc2, .zb, .zp, .mc, .end, .ptn, .au2, .ab-win, .ab-h, .ab-do, .ab-real, .ab-res, .ab-ct').forEach(function(n){if(!n.classList.contains('h5f'))io.observe(n)})})();
'''
rep('  /* activity list */',js+'  /* activity list */')
open('/home/claude/hamsterhub-home/v62.html','w').write(s)
print('v62 ok')
