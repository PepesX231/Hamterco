import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build32.py').read())
# logo back, no peeking hamster on the way home
rep('<img src="img/logo-n.webp" alt="" width="34" height="34">','<img src="img/logo.webp" alt="" width="30" height="30">')
rep('''h='<span class="pt-home"></span><img class="pt-peek" src="img/n-peek.webp" alt="">\'''','''h='<span class="pt-home"></span><span class="pt-lg"><img src="img/logo.webp" alt=""><b>Hamster Hub</b></span>\'''')
rep('<div class="wkz"><img class="wk" src="img/n-up.webp"','<div class="wkz"><img class="wk" src="img/n-gamer.webp"')
# HoF badge -> gold coin
s=s.replace('<i class="h5f-rk">★</i>','<i class="h5f-cn" aria-hidden="true">★</i>')
# activity: drop tape
s=re.sub(r'<div class="axh-tp" aria-hidden="true">.*?</div></div>','',s,count=1,flags=re.S)
# walkers: walk cycle + grabbed pose + dizzy
o=s.index('/* walking hamsters: wander, pick up (dangle + wiggle), drop (squash) */');e=s.index('/* works: a clear "next" guide')
s=s[:o]+r'''/* walking hamsters: waddle walk, grabbed pose, dizzy after a high drop */
  (function(){document.querySelectorAll('.wkz').forEach(function(z){var h=z.querySelector('.wk');if(!h)return;var base=h.getAttribute('src'),D=base.replace('.webp','-d.webp'),K=base.replace('.webp','-k.webp');
      [D,K].forEach(function(u){var i=new Image();i.src=u});
      var sh=document.createElement('i');sh.className='wk-sh';z.insertBefore(sh,h);
      var x=Math.random()*200,y=0,vy=0,dir=1,sp=.55+Math.random()*.25,drag=null,pause=0,seen=false,px=0,ang=0,av=0,ph=0,ko=0,peak=0;
      function pose(p){var u=p==='d'?D:p==='k'?K:base;if(h.getAttribute('src')!==u)h.setAttribute('src',u);h.classList.toggle('ko',p==='k')}
      new IntersectionObserver(function(e){seen=e[0].isIntersecting}).observe(z);
      function step(now){var W=z.clientWidth-h.offsetWidth;if(seen&&W>0){var walking=false,rot=0,bob=0,sq=1;
        if(drag){var vx=x-px;av+=(-vx*1.8-ang)*.14;av*=.85;ang+=av;ang=Math.max(-40,Math.min(40,ang));rot=ang+Math.sin(now/55)*5}
        else if(y<0||vy){vy+=0.9;y+=vy;peak=Math.min(peak,y);rot=ang*=.9;if(y>=0){y=0;var hard=peak<-90;vy=vy>6?-vy*.3:0;
            if(!vy){peak=0;h.classList.remove('land');void h.offsetWidth;h.classList.add('land');if(hard){ko=110;pose('k')}else pose('n')}}}
        else if(ko>0){ko--;if(!ko){pose('n');h.classList.remove('land');void h.offsetWidth;h.classList.add('land')}}
        else if(pause>0){pause--}
        else{x+=dir*sp;walking=true;if(x<0){x=0;dir=1}if(x>W){x=W;dir=-1}if(Math.random()<.004)pause=60+Math.random()*90}
        if(walking){ph+=sp*.16;rot=Math.sin(ph)*7;bob=-Math.abs(Math.sin(ph))*7;sq=1+Math.abs(Math.cos(ph))*.05}else if(!drag&&!y&&!ko){ang=0;rot=Math.sin(now/600)*1.5}
        px=x;h.style.transform='translate('+x+'px,'+(y+bob)+'px) rotate('+rot+'deg) scale('+dir/sq*sq+','+(1/sq)+') scaleX(1)';
        var lift=Math.min(1,-y/160);sh.style.transform='translateX('+(x+h.offsetWidth/2)+'px) translateX(-50%) scale('+(1-lift*.55)*(walking?1-Math.abs(Math.sin(ph))*.15:1)+')';sh.style.opacity=1-lift*.6}
        requestAnimationFrame(step)}
      requestAnimationFrame(step);
      h.addEventListener('pointerdown',function(e){e.preventDefault();var r=z.getBoundingClientRect();drag={dx:e.clientX-r.left-x,dy:e.clientY-r.top-y};ko=0;pose('d');h.classList.add('held');h.classList.remove('land');try{h.setPointerCapture(e.pointerId)}catch(_){}});
      h.addEventListener('pointermove',function(e){if(!drag)return;var r=z.getBoundingClientRect();x=Math.max(0,Math.min(z.clientWidth-h.offsetWidth,e.clientX-r.left-drag.dx));y=Math.max(-240,Math.min(0,e.clientY-r.top-drag.dy))});
      function up(){if(!drag)return;drag=null;vy=0.1;peak=y;h.classList.remove('held');if(y>-4){pose('n')}}
      h.addEventListener('pointerup',up);h.addEventListener('pointercancel',up);
    })})();
  '''+s[e:]
css=r'''
/* ===== v33 ===== */
.brand img{border-radius:50%}
/* home transition: logo instead of a mascot */
.pt-lg{position:fixed;left:50%;top:50%;z-index:3;display:flex;align-items:center;gap:14px;transform:translate(-50%,-50%) scale(.6);opacity:0;transition:transform .45s cubic-bezier(.2,1.4,.4,1),opacity .3s}
.pt-lg img{width:72px;height:72px;border-radius:50%;box-shadow:0 10px 30px rgba(0,0,0,.15)}.pt-lg b{font:800 2rem var(--display);color:var(--b800)}
.pt.in .pt-lg{transform:translate(-50%,-50%) scale(1);opacity:1;transition-delay:.12s}.pt.out .pt-lg{opacity:0;transform:translate(-50%,-60%) scale(.9);transition-delay:0s}
/* HoF gold coin */
.h5f-cn{position:absolute;z-index:3;top:-12px;right:-12px;width:38px;height:38px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-size:1rem;color:#6B4300;
  background:radial-gradient(circle at 35% 30%,#FFF6D6 0 12%,#F3D27A 35%,#C9952E 70%,#8A5A00);box-shadow:inset 0 0 0 3px rgba(255,241,194,.55),inset 0 0 0 5px rgba(138,90,0,.5),0 6px 14px rgba(0,0,0,.55),0 0 18px rgba(255,200,90,.45);
  text-shadow:0 1px 0 rgba(255,241,194,.8);transform:rotate(-12deg)}
.h5f-cn::after{content:"";position:absolute;inset:0;border-radius:50%;background:linear-gradient(115deg,transparent 40%,rgba(255,255,255,.8) 50%,transparent 60%) -150% 0/250% 100% no-repeat;animation:h5Coin 3.6s ease-in-out infinite}
@keyframes h5Coin{0%,60%{background-position:-150% 0}100%{background-position:150% 0}}
.h5f-c em{top:14px;left:12px}
/* activity header: photo-backed, cinematic */
.axh{background:linear-gradient(90deg,rgba(6,22,51,.96) 0%,rgba(6,22,51,.86) 45%,rgba(10,34,80,.55) 100%),url(img/photo-group.webp) center 30%/cover}
.axh::before{background:radial-gradient(60% 80% at 85% 20%,rgba(77,163,240,.45),transparent 70%),linear-gradient(115deg,transparent 55%,rgba(255,197,49,.14) 55.2% 57%,transparent 57.2% 60%,rgba(77,163,240,.18) 60.2% 61%,transparent 61.2%),repeating-linear-gradient(0deg,rgba(255,255,255,.035) 0 1px,transparent 1px 4px)}
.axh::after{content:"";position:absolute;left:0;right:0;bottom:0;height:5px;z-index:1;background:linear-gradient(90deg,var(--yel),#4DA3F0)}
.axh-in{padding-bottom:clamp(56px,6vw,96px)}
/* walkers */
.wk{transform-origin:50% 100%;transition:none}
.wk.held{animation:wkUp .45s cubic-bezier(.3,1.6,.5,1)}
.wk.ko{height:52px}.wkz.sm .wk.ko{height:44px}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v33.html','w').write(s)
print('v33 ok')
s=s.replace('rgba(10,34,80,.55) 100%),url(img/photo-group.webp)','rgba(10,34,80,.72) 100%),url(img/photo-group.webp)',1)
open('/home/claude/hamsterhub-home/v33.html','w').write(s)
s=s.replace('<i class="h5f-cn" aria-hidden="true">★</i>','')
assert 'class="h5f-cn"' not in s
open('/home/claude/hamsterhub-home/v33.html','w').write(s)
s=s.replace('<s>9,990</s><em>ประหยัด 4,000</em>','<s>9,990</s>')
assert 'ประหยัด' not in s
s=s.replace('/* ---------- footer ---------- */','.ctb-p s{color:#E5484D;font-weight:700;font-size:1.25rem;text-decoration-thickness:2px}\n/* ---------- footer ---------- */',1)
open('/home/claude/hamsterhub-home/v33.html','w').write(s)
