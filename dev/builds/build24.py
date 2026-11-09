D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build23.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
# hero: stretched clip, buttons inside the banner
i=s.index('    <a class="ov-c" href="#portex"');j=s.index('  </section>',i)
s=s[:i]+'''    <div class="ov-c ov-s" role="link" tabindex="0" aria-label="ดูรายละเอียดคอร์ส Port Express" onclick="if(!event.target.closest('a'))location.hash='portex'"><video src="img/portex-hero.mp4" poster="img/portex-hero.webp" autoplay muted loop playsinline preload="auto" aria-hidden="true"></video>
      <div class="ov-in"><a class="pb1" href="'''+PX+'''" target="_blank" rel="noopener">▶ สมัครเรียน</a><a class="pb2" href="#portex">ดูรายละเอียด</a></div></div>
'''+s[j:]
# move Hall of Fame below "paths"
i=s.index('    <section class="tile hf3"');j=s.index('    </section>',i)+len('    </section>')
hof=s[i:j];s=s[:i]+s[j:]
k=s.index('  <section class="mc">')
s=s[:k]+'  <section class="hp-grid hof-s"><div class="wrap hg st">\n'+hof+'\n  </div></section>\n\n'+s[k:]
# walking hamsters (one per page)
s=s.replace('<img class="pg-ham" src="img/n-maker.webp" alt="">','')
s=s.replace('<img class="yt-ham" src="img/n-walker.webp" alt="">','<div class="wkz sm"><img class="wk" src="img/n-walker.webp" alt="น้องหนู ลากเล่นได้"></div>')
k=s.index('  <section class="hp-grid hof-s">')
s=s[:k]+'  <div class="wkz"><img class="wk" src="img/n-gamer.webp" alt="น้องหนู ลากเล่นได้"></div>\n'+s[k:]
s=s.replace('    <section class="ct-help">','    <div class="wkz"><img class="wk" src="img/n-maker.webp" alt="น้องหนู ลากเล่นได้"></div>\n    <section class="ct-help">',1)
# seniors: background follows the poster in front
s=s.replace('<p class="mc-bg" aria-hidden="true">CONGRATULATIONS</p>','<img class="mc-bgi" id="mcBg" alt="" aria-hidden="true"><p class="mc-bg" aria-hidden="true">CONGRATULATIONS</p>')
rep("function go(k){a=(k+L.length)%L.length;lay();","function go(k){a=(k+L.length)%L.length;lay();var bg=document.getElementById('mcBg');if(bg&&L[a]){bg.style.opacity=0;setTimeout(function(){bg.src='img/dek69-'+L[a][0]+'.webp';bg.style.opacity=1},250)}")
rep("  /* router */",r'''  /* walking hamsters: wander, pick up, drop */
  (function(){document.querySelectorAll('.wkz').forEach(function(z){var h=z.querySelector('.wk');if(!h)return;var x=Math.random()*200,y=0,vy=0,dir=1,sp=.5+Math.random()*.4,drag=null,pause=0,t0=performance.now(),seen=false;
      new IntersectionObserver(function(e){seen=e[0].isIntersecting}).observe(z);
      function step(now){var W=z.clientWidth-h.offsetWidth;if(seen&&W>0){if(drag){}else if(y<0||vy){vy+=0.9;y+=vy;if(y>=0){y=0;vy=vy>6?-vy*.35:0;if(!vy)h.classList.add('land');setTimeout(function(){h.classList.remove('land')},300)}}
        else if(pause>0){pause--}else{x+=dir*sp;if(x<0){x=0;dir=1}if(x>W){x=W;dir=-1}if(Math.random()<.004)pause=60+Math.random()*90}
        var bob=(!drag&&!pause&&!y)?Math.abs(Math.sin(now/120))*-4:0;h.style.transform='translate('+x+'px,'+(y+bob)+'px) scaleX('+dir+')';h.classList.toggle('held',!!drag)}requestAnimationFrame(step)}
      requestAnimationFrame(step);
      h.addEventListener('pointerdown',function(e){e.preventDefault();var r=z.getBoundingClientRect();drag={dx:e.clientX-r.left-x,dy:e.clientY-r.top-y};h.setPointerCapture(e.pointerId)});
      h.addEventListener('pointermove',function(e){if(!drag)return;var r=z.getBoundingClientRect();x=Math.max(0,Math.min(z.clientWidth-h.offsetWidth,e.clientX-r.left-drag.dx));y=Math.min(0,e.clientY-r.top-drag.dy)});
      h.addEventListener('pointerup',function(){if(!drag)return;drag=null;vy=0.1});
    })})();
  /* router */''')
css=r'''
/* ===== v24 ===== */
.ov{background:#1A1460!important}
.ov .ov-c.ov-s{position:relative;display:block;width:100%!important;max-width:none;height:min(calc(100svh - 60px),56.25vw);cursor:pointer;overflow:hidden}
.ov-s video{position:absolute;inset:0;width:100%;height:100%;object-fit:fill!important}
.ov-bar3{display:none}
.ov-in{position:absolute;right:3.5%;bottom:6%;display:flex;gap:14px;z-index:2}
.ov-in a{display:inline-flex;align-items:center;min-height:clamp(44px,3.6vw,60px);padding:0 clamp(18px,2vw,32px) 5px;font:800 clamp(.95rem,1.25vw,1.25rem) var(--display);text-decoration:none;transition:transform .1s steps(2);
  clip-path:polygon(0 6px,6px 6px,6px 0,calc(100% - 6px) 0,calc(100% - 6px) 6px,100% 6px,100% calc(100% - 6px),calc(100% - 6px) calc(100% - 6px),calc(100% - 6px) 100%,6px 100%,6px calc(100% - 6px),0 calc(100% - 6px))}
.ov-in a:hover{transform:translateY(4px)}
.ov-in .pb1{background:#FFD24A;color:#0B0720;box-shadow:inset 0 -6px 0 #C28A00;animation:kp3 1.6s ease-in-out infinite}
@keyframes kp3{50%{filter:brightness(1.15)}}
.ov-in .pb2{background:#5BC0FF;color:#06123A;box-shadow:inset 0 -6px 0 #1D5FB8}
@media (max-width:700px){.ov .ov-c.ov-s{height:62vw}.ov-in{right:3%;bottom:4%;gap:6px}.ov-in a{min-height:34px;padding:0 10px 4px;font-size:.78rem}}
/* walkers */
.wkz{position:relative;height:150px;max-width:1120px;margin:0 auto;touch-action:none}
.wkz.sm{height:120px;margin-top:20px}
.wk{position:absolute;left:0;bottom:6px;height:120px;cursor:grab;user-select:none;-webkit-user-drag:none;filter:drop-shadow(0 8px 6px rgba(0,0,0,.18));will-change:transform}
.wkz.sm .wk{height:96px}
.wk.held{cursor:grabbing;filter:drop-shadow(0 22px 14px rgba(0,0,0,.25))}
.wk.land{animation:sq .3s}
@keyframes sq{40%{scale:1.08 .9}}
.wkz::after{content:"";position:absolute;left:0;right:0;bottom:4px;height:2px;background:repeating-linear-gradient(90deg,#E3E3E8 0 8px,transparent 8px 14px)}
.yt .wkz::after{background:repeating-linear-gradient(90deg,#333 0 8px,transparent 8px 14px)}
.hof-s{padding-top:0!important}
/* seniors bg = current poster */
.mc-in{background:#0A0716!important}
.mc-bgi{position:absolute;inset:-10%;width:120%;height:120%;object-fit:cover;object-position:50% 30%;filter:blur(40px) saturate(1.4) brightness(.45);transition:opacity .6s;pointer-events:none}
.mc-in::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 50% at 50% 60%,transparent,rgba(10,7,22,.75));pointer-events:none}
.mc-in>*:not(.mc-bgi){position:relative}
.mc-bg{position:absolute!important;opacity:.6}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v24.html','w').write(s)
print('v24 ok',len(s))
