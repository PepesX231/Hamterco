import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build31.py').read())
# new logo + new home walker
rep('<img src="img/logo.webp" alt="" width="30" height="30">','<img src="img/logo-n.webp" alt="" width="34" height="34">')
rep('<div class="wkz"><img class="wk" src="img/n-gamer.webp"','<div class="wkz"><img class="wk" src="img/n-up.webp"')
# price: red strike, no savings pill
rep('<em>ประหยัด 4,000</em>','')
# HoF: rank diamonds + slanted name plates
k=[0]
def plate(m):
    k[0]+=1
    return m.group(1)+'<i class="h5f-rk">%d</i>'%k[0]+m.group(2)+'<b class="h5f-nm"><span>'+m.group(3)+'</span></b>'
s=re.sub(r'(<a class="h5f-c[^"]*" href="#works" data-pane="hof">)(<span class="h5f-im">.*?</span>)<b>(.*?)</b>',plate,s)
assert k[0]==5
# activity header
i=s.index('<section class="ac-h">');j=s.index('</section>',i)+10
tape=' ✦ '.join(['ค่าย Game Jam','AI Camp','Hallow Open Hub','All for One University','DEK70 Camp','NSC Software Project','Showcase','เวิร์กชอป AI for Business'])
s=s[:i]+'''<section class="axh">
      <div class="axh-in">
        <div class="axh-t">
          <p class="axh-k"><span>HAMSTER HUB EVENTS</span></p>
          <h1 class="axh-h" data-t="กิจกรรม">กิจกรรม</h1>
          <p class="axh-s">ค่าย เวิร์กชอป การแข่งขัน และงานโชว์ผลงาน<br>ทุกงานน้องได้ลงมือสร้างของจริง</p>
          <ul class="axh-n"><li><b id="axN">20+</b>งานในปี 2569</li><li><b>4</b>แบบ ค่าย · เวิร์กชอป · แข่ง · โชว์</li></ul>
        </div>
        <div class="axh-p" aria-hidden="true">
          <img class="p1" src="img/photo-group.webp" alt=""><img class="p2" src="img/k-hallow.webp" alt=""><img class="p3" src="img/photo-camp.webp" alt=""><img class="p4" src="img/k-aicamp.webp" alt=""><img class="p5" src="img/photo-desk.webp" alt="">
        </div>
      </div>
      <div class="axh-tp" aria-hidden="true"><div><span>'''+tape+' ✦ '+tape+' ✦ '+'''</span></div></div>
    </section>'''+s[j:]
# count from list
rep('/* walking hamsters: wander, pick up, drop */','(function(){var n=document.querySelectorAll(".er").length,e=document.getElementById("axN");if(e&&n)e.textContent=n})();\n  /* walking hamsters: wander, pick up, drop */')
# walkers: pickup animation + stay out of the way
old_js=s[s.index('/* walking hamsters: wander, pick up, drop */'):s.index('/* works: a clear "next" guide')]
new_js=r'''/* walking hamsters: wander, pick up (dangle + wiggle), drop (squash) */
  (function(){document.querySelectorAll('.wkz').forEach(function(z){var h=z.querySelector('.wk');if(!h)return;var sh=document.createElement('i');sh.className='wk-sh';z.insertBefore(sh,h);
      var x=Math.random()*200,y=0,vy=0,dir=1,sp=.45+Math.random()*.3,drag=null,pause=0,seen=false,px=0,ang=0,av=0;
      new IntersectionObserver(function(e){seen=e[0].isIntersecting}).observe(z);
      function step(now){var W=z.clientWidth-h.offsetWidth;if(seen&&W>0){
        if(drag){var vx=x-px;av+=(-vx*1.6-ang)*.12;av*=.86;ang+=av;ang=Math.max(-35,Math.min(35,ang))}
        else{ang*=.8;if(y<0||vy){vy+=0.9;y+=vy;if(y>=0){y=0;vy=vy>6?-vy*.35:0;if(!vy){h.classList.remove('land');void h.offsetWidth;h.classList.add('land')}}}
        else if(pause>0){pause--}else{x+=dir*sp;if(x<0){x=0;dir=1}if(x>W){x=W;dir=-1}if(Math.random()<.004)pause=60+Math.random()*90}}
        px=x;var bob=(!drag&&!pause&&!y)?Math.abs(Math.sin(now/120))*-4:0;
        h.style.transform='translate('+x+'px,'+(y+bob)+'px) rotate('+ang+'deg) scaleX('+dir+')';
        var lift=Math.min(1,-y/160);sh.style.transform='translateX('+(x+h.offsetWidth/2)+'px) translateX(-50%) scale('+(1-lift*.55)+')';sh.style.opacity=1-lift*.6}
        requestAnimationFrame(step)}
      requestAnimationFrame(step);
      h.addEventListener('pointerdown',function(e){e.preventDefault();var r=z.getBoundingClientRect();drag={dx:e.clientX-r.left-x,dy:e.clientY-r.top-y};h.classList.add('held');h.classList.remove('land');try{h.setPointerCapture(e.pointerId)}catch(_){}});
      h.addEventListener('pointermove',function(e){if(!drag)return;var r=z.getBoundingClientRect();x=Math.max(0,Math.min(z.clientWidth-h.offsetWidth,e.clientX-r.left-drag.dx));y=Math.max(-240,Math.min(0,e.clientY-r.top-drag.dy))});
      function up(){if(!drag)return;drag=null;vy=0.1;h.classList.remove('held')}
      h.addEventListener('pointerup',up);h.addEventListener('pointercancel',up);
    })})();
  '''
s=s.replace(old_js,new_js)
css=r'''
/* ===== v32 ===== */
.brand img{border-radius:0;object-fit:contain}
/* hero bigger, red old price */
.hq-in{max-width:1560px;grid-template-columns:minmax(0,.9fr) minmax(0,1.35fr)}.hq-s{max-width:1560px}
.hq-h{font-size:clamp(2.6rem,4.1vw,4.4rem)}
.hq-p b{font-size:clamp(3.2rem,5vw,4.4rem)}
.hq-p s{color:#FF5A5A;font:700 1.4rem var(--display);text-decoration-thickness:2px}
.hq-m li{font-size:1.2rem}
@media(max-width:900px){.hq-h{font-size:2.3rem}}
/* HoF: compact, game-UI frame, floating cards */
.h5f{padding:clamp(40px,4.5vw,64px) 16px clamp(40px,4vw,56px);
  background:radial-gradient(40% 50% at 50% 0%,rgba(255,206,110,.16),transparent 70%),
  repeating-linear-gradient(45deg,rgba(232,200,119,.035) 0 1px,transparent 1px 28px),repeating-linear-gradient(-45deg,rgba(232,200,119,.035) 0 1px,transparent 1px 28px),
  linear-gradient(#100B05,#070503)}
.h5f-sp{opacity:.45}
.h5f-fx::before{opacity:.6}
.h5f-fx::after{content:"";position:absolute;inset:16px;pointer-events:none;--c:rgba(232,200,119,.55);
  background:linear-gradient(var(--c),var(--c)) 0 0/34px 2px,linear-gradient(var(--c),var(--c)) 0 0/2px 34px,
  linear-gradient(var(--c),var(--c)) 100% 0/34px 2px,linear-gradient(var(--c),var(--c)) 100% 0/2px 34px,
  linear-gradient(var(--c),var(--c)) 0 100%/34px 2px,linear-gradient(var(--c),var(--c)) 0 100%/2px 34px,
  linear-gradient(var(--c),var(--c)) 100% 100%/34px 2px,linear-gradient(var(--c),var(--c)) 100% 100%/2px 34px;background-repeat:no-repeat}
.h5f-k{font-size:.95rem;letter-spacing:.04em}
.h5f-t{font-size:clamp(2.4rem,5.4vw,4.6rem)}
.h5f-s{font-size:1rem;margin-top:8px}
.h5f-r{margin-top:clamp(28px,3vw,40px);max-width:1040px;gap:clamp(14px,2vw,28px);align-items:center}
.h5f-c{max-width:180px;animation:h5Fl 4.5s ease-in-out infinite;padding-bottom:26px}
.h5f-c.mid{max-width:220px}
.h5f-c:nth-child(2){animation-delay:-.9s}.h5f-c:nth-child(3){animation-delay:-1.8s}.h5f-c:nth-child(4){animation-delay:-2.7s}.h5f-c:nth-child(5){animation-delay:-3.6s}
@keyframes h5Fl{0%,100%{translate:0 0}50%{translate:0 -14px}}
.h5f-c::after{content:"";position:absolute;left:15%;right:15%;bottom:-6px;height:14px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,200,90,.35),transparent);animation:h5Sh 4.5s ease-in-out infinite;animation-delay:inherit}
@keyframes h5Sh{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(.7);opacity:.5}}
.h5f-im{border-radius:12px}.h5f-im img{border-radius:10px}
.h5f-rk{position:absolute;z-index:3;top:-12px;left:50%;width:30px;height:30px;margin-left:-15px;display:grid;place-items:center;font:800 .9rem var(--display);font-style:normal;color:#1A1206;
  background:linear-gradient(135deg,#FFF1C2,#E8C877 50%,#B8862A);transform:rotate(45deg);border-radius:5px;box-shadow:0 0 0 2px #120D05,0 0 16px rgba(255,200,90,.7)}
.h5f-rk::first-line{}
.h5f-c .h5f-rk{line-height:1}.h5f-rk{text-indent:0}
.h5f-nm{position:relative;z-index:2;display:block!important;width:fit-content;margin:-14px auto 0!important;padding:5px 16px;transform:skewX(-14deg);
  background:linear-gradient(90deg,#2A1D08,#4A3410 50%,#2A1D08);box-shadow:inset 0 0 0 1px rgba(246,223,154,.6),0 6px 14px rgba(0,0,0,.6)}
.h5f-nm span{display:block;transform:skewX(14deg);font:700 .92rem var(--display);color:#FFF1C2;white-space:nowrap}
.h5f-c em{top:24px}
.h5f-go{margin-top:28px;border-radius:0;clip-path:polygon(12px 0,100% 0,calc(100% - 12px) 100%,0 100%);padding:12px 34px}
@media (prefers-reduced-motion:reduce){.h5f-c,.h5f-c::after{animation:none}}
/* activity header */
.ac-h{display:none}
.axh{position:relative;overflow:hidden;margin:0 calc(50% - 50vw);color:#fff;isolation:isolate;
  background:radial-gradient(50% 70% at 80% 40%,rgba(77,163,240,.45),transparent 70%),radial-gradient(40% 60% at 10% 100%,rgba(255,197,49,.18),transparent 70%),linear-gradient(160deg,#0A2250,#061633)}
.axh::before{content:"";position:absolute;inset:0;z-index:-1;background:repeating-linear-gradient(-55deg,rgba(255,255,255,.03) 0 2px,transparent 2px 22px)}
.axh-in{max-width:1180px;margin:0 auto;padding:clamp(48px,6vw,88px) 24px clamp(40px,5vw,72px);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:32px;align-items:center}
.axh-k span{display:inline-block;font:800 .85rem var(--display);letter-spacing:.14em;color:#2A1E00;background:var(--yel);padding:6px 18px;clip-path:polygon(10px 0,100% 0,calc(100% - 10px) 100%,0 100%)}
.axh-h{position:relative;font:900 clamp(4rem,10vw,8.5rem)/1.05 var(--display);letter-spacing:-.03em;margin-top:14px;color:#fff;
  text-shadow:1px 1px 0 #4DA3F0,2px 2px 0 #4DA3F0,3px 3px 0 #1C74D9,4px 4px 0 #1C74D9,5px 5px 0 #155FB5,6px 6px 0 #155FB5,7px 7px 0 #0D4A94,8px 8px 0 #0D4A94,14px 18px 30px rgba(0,0,0,.45);
  animation:axIn .8s cubic-bezier(.2,1.4,.4,1) both}
@keyframes axIn{from{transform:translateY(30px) scale(.9);opacity:0}}
.axh-s{font:500 1.2rem/1.55 var(--display);color:rgba(255,255,255,.82);margin-top:18px}
.axh-n{list-style:none;padding:0;margin:26px 0 0;display:flex;gap:28px;flex-wrap:wrap}
.axh-n li{font-size:.95rem;color:rgba(255,255,255,.75)}.axh-n b{display:block;font:800 2.2rem/1 var(--display);color:var(--yel);margin-bottom:4px}
.axh-p{position:relative;height:clamp(300px,30vw,400px)}
.axh-p img{position:absolute;object-fit:cover;border:5px solid #fff;border-radius:6px;box-shadow:0 24px 40px -14px rgba(0,0,0,.6);animation:axF 6s ease-in-out infinite}
.axh-p .p1{width:58%;aspect-ratio:16/10;left:4%;top:6%;rotate:-6deg}
.axh-p .p2{width:36%;aspect-ratio:1;right:0;top:0;rotate:7deg;animation-delay:-1.5s}
.axh-p .p3{width:40%;aspect-ratio:4/3;left:0;bottom:4%;rotate:4deg;animation-delay:-3s}
.axh-p .p4{width:50%;aspect-ratio:16/8;right:6%;bottom:12%;rotate:-4deg;animation-delay:-4.2s}
.axh-p .p5{width:30%;aspect-ratio:1;left:38%;top:36%;rotate:-10deg;z-index:2;animation-delay:-2.2s}
@keyframes axF{0%,100%{translate:0 0}50%{translate:0 -10px}}
.axh-tp{position:relative;transform:rotate(-1.6deg);margin:0 -20px -6px;background:var(--yel);color:#2A1E00;overflow:hidden;box-shadow:0 -6px 20px rgba(0,0,0,.25)}
.axh-tp div{display:flex;width:max-content;animation:axT 40s linear infinite}
.axh-tp span{font:800 1.05rem var(--display);padding:12px 0;white-space:nowrap}
@keyframes axT{to{transform:translateX(-50%)}}
@media (max-width:900px){.axh-in{grid-template-columns:minmax(0,1fr)}.axh-p{height:260px}}
@media (prefers-reduced-motion:reduce){.axh-p img,.axh-tp div{animation:none}}
/* walkers: smaller, quieter, with a pick-up pose */
.wkz{height:104px}.wk{height:88px;bottom:4px;transition:filter .2s}
.wkz.sm .wk{height:76px}
.wk-sh{position:absolute;left:0;bottom:0;width:60px;height:10px;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.18),transparent);pointer-events:none}
.wk.held{animation:wkUp .5s cubic-bezier(.3,1.6,.5,1),wkKick .28s ease-in-out .5s infinite alternate;filter:drop-shadow(0 18px 14px rgba(0,0,0,.22))}
@keyframes wkUp{0%{scale:1 1}30%{scale:.85 1.18}60%{scale:1.08 .94}100%{scale:1 1}}
@keyframes wkKick{from{scale:1 1}to{scale:1.03 .97}}
.wk.land{animation:wkLand .45s cubic-bezier(.3,1.6,.5,1)}
@keyframes wkLand{0%{scale:1.25 .72}50%{scale:.92 1.08}100%{scale:1 1}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v32.html','w').write(s)
print('v32 ok')
s=s.replace('.hq-h{font-size:clamp(2.6rem,4.1vw,4.4rem)}','.hq-h{font-size:clamp(2.4rem,3.35vw,4.2rem)}',1)
open('/home/claude/hamsterhub-home/v32.html','w').write(s)
s=re.sub(r'<i class="h5f-rk">\d</i>','<i class="h5f-rk">★</i>',s)
s=s.replace('.h5f-rk::first-line{}','.h5f-rk{transform:none!important;background:none!important;box-shadow:none!important;color:#1A1206;font-size:.85rem;isolation:isolate}.h5f-rk::before{content:"";position:absolute;inset:0;z-index:-1;border-radius:5px;transform:rotate(45deg);background:linear-gradient(135deg,#FFF1C2,#E8C877 50%,#B8862A);box-shadow:0 0 0 2px #120D05,0 0 16px rgba(255,200,90,.7)}',1)
open('/home/claude/hamsterhub-home/v32.html','w').write(s)
