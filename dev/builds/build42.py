import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build41.py').read())
CHEV='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHEVR=CHEV.replace('M15 5l-7 7 7 7','M9 5l7 7-7 7')
# ---------- Hall of Fame as a visionOS gallery
i=s.index('<section class="h5f"');j=s.index('</section>',i)+10
s=s[:i]+'''<section class="vg" aria-label="Hall of Fame ผลงานเด่นปี 2569">
    <div class="vg-env" aria-hidden="true"><img src="img/g-gallery.webp" alt=""><i class="vg-amb" id="vgAmb"></i></div>
    <div class="vg-bar"><span class="vg-dots" aria-hidden="true"><i></i><i></i><i></i></span><b>HALL OF FAME</b><span class="vg-sub">ผลงานเด่นของน้องๆ ปี 2569</span></div>
    <div class="vg-st" id="vgSt" tabindex="0" aria-roledescription="carousel"></div>
    <div class="vg-orn">
      <button type="button" class="vg-btn" id="vgP" aria-label="ผลงานก่อนหน้า">'''+CHEV+'''</button>
      <div class="vg-who"><span class="vg-av" id="vgAv"></span><span><b id="vgN"></b><small id="vgBy"></small></span></div>
      <span class="vg-ct" id="vgCt"></span>
      <button type="button" class="vg-btn" id="vgX" aria-label="ผลงานถัดไป">'''+CHEVR+'''</button>
    </div>
    <a class="vg-go" href="#works" data-pane="hof">ดูผลงานทั้งหมด</a>
  </section>'''+s[j:]
# ---------- home: works by track
WX='''<section class="wx" aria-label="ผลงานของน้องๆ แยกตามสาย">
    <div class="wx-env" aria-hidden="true"><img id="wxBg" src="img/work-phi-krahang.webp" alt=""></div>
    <div class="wx-in">
      <h2>ผลงานจริงของน้องๆ</h2>
      <p class="wx-l">น้องที่เรียนกับเราสร้างผลงานได้หลายแบบ เลือกดูตามสายที่สนใจ</p>
      <div class="wx-seg" role="tablist" aria-label="สายผลงาน"><i class="wx-ind" id="wxInd"></i>
        <button type="button" role="tab" data-k="game" aria-selected="true">เกม</button><button type="button" role="tab" data-k="startup" aria-selected="false">สตาร์ทอัพ</button><button type="button" role="tab" data-k="web" aria-selected="false">เว็บและแอป</button><button type="button" role="tab" data-k="iot" aria-selected="false">IoT</button></div>
      <div class="wx-w">
        <div class="wx-win"><div class="wx-bar"><span class="vg-dots" aria-hidden="true"><i></i><i></i><i></i></span><span id="wxUrl"></span></div>
          <div class="wx-m"><img id="wxImg" src="img/work-phi-krahang.webp" alt=""><span class="wx-tag" id="wxTag" hidden>ภาพประกอบ</span></div>
          <div class="wx-d"><b id="wxT"></b><p id="wxD"></p><em id="wxR"></em></div></div>
        <ul class="wx-list" id="wxList"></ul>
      </div>
    </div>
  </section>
  '''
rep('<section class="zh">',WX+'<section class="zh">')
JS=r'''
  /* Hall of Fame: visionOS-style gallery */
  (function(){var st=$('#vgSt');if(!st)return;var n=W.length,a=0,tm=0,hold=false;
    st.innerHTML=W.map(function(w,i){var aw=AW[w[0]];return '<button type="button" class="vg-c" data-i="'+i+'" aria-label="'+w[1]+'"><img src="img/work-'+w[0]+'.webp" alt="" loading="lazy">'+(aw?'<span class="vg-aw">'+aw+'</span>':'')+'<span class="vg-cap"><b>'+w[1]+'</b><small>เกมที่น้อง @'+NK[w[0]][0]+' สร้างเอง</small></span></button>'}).join('');
    var C=st.querySelectorAll('.vg-c');
    function lay(){C.forEach(function(c,i){var d=((i-a)%n+n+n/2)%n-n/2;d=Math.round(d);var ad=Math.abs(d);
      c.style.transform='translate(-50%,-50%) translateX('+(d*34)+'%) translateZ('+(-ad*140)+'px) rotateY('+(d===0?0:(d<0?32:-32))+'deg) scale('+(d===0?1:.82)+')';
      c.style.opacity=ad>2?0:(d===0?1:.62-ad*.12);c.style.zIndex=10-ad;c.classList.toggle('on',d===0);c.tabIndex=ad>2?-1:0;c.style.pointerEvents=ad>2?'none':''});
      var w=W[a];$('#vgN').textContent=w[1];$('#vgBy').textContent='@'+NK[w[0]][0]+' '+NK[w[0]][1];$('#vgAv').textContent=NK[w[0]][0].charAt(0);$('#vgCt').textContent=(a+1)+' / '+n;
      $('#vgAmb').style.backgroundImage='url(img/work-'+w[0]+'.webp)'}
    function go(k){a=(k+n)%n;lay();clearTimeout(tm);tm=setTimeout(tick,5200)}
    function tick(){if(hold||!document.querySelector('[data-view="home"].on')){tm=setTimeout(tick,800);return}go(a+1)}
    C.forEach(function(c){c.addEventListener('click',function(){var i=+c.dataset.i;if(i===a){location.hash='#works'}else go(i)})});
    $('#vgP').addEventListener('click',function(){go(a-1)});$('#vgX').addEventListener('click',function(){go(a+1)});
    st.addEventListener('keydown',function(e){if(e.key==='ArrowLeft'){go(a-1);e.preventDefault()}if(e.key==='ArrowRight'){go(a+1);e.preventDefault()}});
    var sx=null;st.addEventListener('pointerdown',function(e){sx=e.clientX});st.addEventListener('pointerup',function(e){if(sx!=null&&Math.abs(e.clientX-sx)>40)go(a+(e.clientX<sx?1:-1));sx=null});
    var root=$('.vg');root.addEventListener('pointerenter',function(){hold=true});root.addEventListener('pointerleave',function(){hold=false});
    go(0)})();
  /* home: works by track */
  (function(){var L=$('#wxList');if(!L)return;
    var T={game:[['phi-krahang','ผีกระหัง','เกมสยองขวัญ 2D ที่น้อง @นนท์ สร้างเอง','img/work-phi-krahang.webp',''],['eugation-strike','Eugation Strike','เกมยิงที่ต้องแก้สมการ โดยน้อง @ไผ่','img/work-eugation-strike.webp',''],['slash-speed','SLASH//SPEED','เกมแอ็กชันความเร็วสูง โดยน้อง @ดินสอ','img/work-slash-speed.webp',''],['roblox','เกมบน Roblox','ผลงาน Roblox ของพี่มิคกี้','img/w-roblox.webp','']],
      startup:[['mrcity','Mr. City','เกมแนะนำที่เที่ยวในสงขลา','img/g-mrcity.webp','ขายให้สวนสัตว์สงขลาแล้ว',1]],
      web:[['quest','Hamster Quest','เว็บเรียนที่เล่นเหมือนเกม','img/g-quest.webp','กำลังเตรียมใช้กับมหาวิทยาลัย',1],['phc','PHC Map','เกมสอนเขียนโปรแกรม Python','img/g-phc.webp','ใช้สอนเด็กไปแล้วกว่า 1,000 คน',1]],
      iot:[['stressstrike','StressStrike','เกมที่เล่นด้วยการบีบอุปกรณ์วัดแรงมือ ต่อเซนเซอร์เข้ากับเกม','img/work-stressstrike.webp','ชนะเลิศ OBEC Roboplayground']]};
    var cur='game';
    function show(it){$('#wxImg').src=it[3];$('#wxBg').src=it[3];$('#wxT').textContent=it[1];$('#wxD').textContent=it[2];$('#wxR').textContent=it[4];$('#wxR').hidden=!it[4];$('#wxTag').hidden=!it[5];$('#wxUrl').textContent=it[1];
      var w=$('.wx-win');w.classList.remove('sw');void w.offsetWidth;w.classList.add('sw');$$('#wxList li').forEach(function(li){li.classList.toggle('on',li.dataset.id===it[0])})}
    function tab(k){cur=k;var b=$('.wx-seg [data-k="'+k+'"]');$$('.wx-seg button').forEach(function(x){x.setAttribute('aria-selected',String(x===b))});
      var ind=$('#wxInd');ind.style.width=b.offsetWidth+'px';ind.style.transform='translateX('+b.offsetLeft+'px)';
      L.innerHTML=T[k].map(function(it){return '<li data-id="'+it[0]+'"><button type="button"><img src="'+it[3]+'" alt=""><span><b>'+it[1]+'</b><small>'+it[2]+'</small></span></button></li>'}).join('');
      $$('#wxList li').forEach(function(li,i){li.querySelector('button').addEventListener('click',function(){show(T[k][i])})});show(T[k][0])}
    $$('.wx-seg button').forEach(function(b){b.addEventListener('click',function(){tab(b.dataset.k)})});
    addEventListener('resize',function(){tab(cur)});setTimeout(function(){tab('game')},50)})();
  /* search: loading dots while matching */
  (function(){var f=$('#zqForm');if(!f)return;var btn=f.querySelector('button'),t0=btn.textContent;f.addEventListener('submit',function(){btn.classList.add('ld');btn.innerHTML='<i></i><i></i><i></i>';setTimeout(function(){btn.classList.remove('ld');btn.textContent=t0},520)})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v42: visionOS-style glass ===== */
:root{--gl:rgba(255,255,255,.14);--gl2:rgba(255,255,255,.24);--glb:rgba(255,255,255,.28)}
.glass,.vg-bar,.vg-orn,.vg-go,.wx-seg,.wx-win,.wx-list{-webkit-backdrop-filter:blur(28px) saturate(170%);backdrop-filter:blur(28px) saturate(170%)}
/* Hall of Fame gallery */
.vg{position:relative;overflow:hidden;isolation:isolate;padding:28px 16px 40px;min-height:min(820px,100svh);display:flex;flex-direction:column;align-items:center;color:#fff}
.vg-env{position:absolute;inset:0;z-index:-1}
.vg-env img{width:100%;height:100%;object-fit:cover;filter:blur(3px) brightness(.62);transform:scale(1.04)}
.vg-amb{position:absolute;inset:-10%;background:center/cover no-repeat;filter:blur(80px) saturate(150%);opacity:.38;mix-blend-mode:screen;transition:background-image .6s}
.vg-env::after{content:"";position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.25),transparent 30%,transparent 70%,rgba(0,0,0,.45))}
.vg-bar{display:flex;align-items:center;gap:14px;padding:10px 22px 10px 16px;border-radius:999px;background:var(--gl);box-shadow:inset 0 0 0 1px var(--glb),0 10px 30px rgba(0,0,0,.25)}
.vg-dots{display:inline-flex;gap:6px}.vg-dots i{width:10px;height:10px;border-radius:50%;background:#FF5F57}.vg-dots i:nth-child(2){background:#FEBC2E}.vg-dots i:nth-child(3){background:#28C840}
.vg-bar b{font:800 1.05rem var(--display);letter-spacing:.06em;color:#F6DF9A}.vg-sub{font-size:.9rem;color:rgba(255,255,255,.75)}
.vg-st{position:relative;width:100%;max-width:1200px;height:clamp(340px,40vw,520px);margin-top:26px;perspective:1600px;transform-style:preserve-3d;outline:0;touch-action:pan-y}
.vg-c{position:absolute;left:50%;top:50%;width:clamp(260px,34vw,500px);aspect-ratio:4/3;border:0;padding:0;border-radius:28px;overflow:hidden;cursor:pointer;background:#111;
  box-shadow:0 0 0 1px rgba(255,255,255,.35),0 40px 80px -30px rgba(0,0,0,.85);transition:transform .8s cubic-bezier(.2,.8,.2,1),opacity .6s;transform-style:preserve-3d}
.vg-c img{width:100%;height:100%;object-fit:cover;display:block}
.vg-c::after{content:"";position:absolute;inset:0;border-radius:inherit;box-shadow:inset 0 0 0 1px rgba(255,255,255,.25),inset 0 1px 0 rgba(255,255,255,.5);pointer-events:none}
.vg-cap{position:absolute;left:14px;right:14px;bottom:14px;display:flex;flex-direction:column;gap:2px;text-align:left;padding:12px 16px;border-radius:18px;background:rgba(30,30,30,.38);-webkit-backdrop-filter:blur(22px) saturate(160%);backdrop-filter:blur(22px) saturate(160%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.22);color:#fff;opacity:0;transform:translateY(10px);transition:opacity .4s .25s,transform .4s .25s}
.vg-cap b{font:800 1.25rem var(--display)}.vg-cap small{font-size:.88rem;color:rgba(255,255,255,.82)}
.vg-c.on .vg-cap{opacity:1;transform:none}
.vg-aw{position:absolute;top:14px;left:14px;padding:6px 12px;border-radius:999px;font:700 .82rem var(--display);color:#3A2A00;background:rgba(246,223,154,.92);box-shadow:0 6px 16px rgba(0,0,0,.3)}
.vg-c:focus-visible{outline:3px solid #fff;outline-offset:4px}
.vg-orn{display:flex;align-items:center;gap:12px;margin-top:22px;padding:8px;border-radius:999px;background:var(--gl);box-shadow:inset 0 0 0 1px var(--glb),0 12px 30px rgba(0,0,0,.3)}
.vg-btn{width:44px;height:44px;border-radius:50%;border:0;display:grid;place-items:center;background:rgba(255,255,255,.12);color:#fff;cursor:pointer;transition:background .2s,transform .15s}
.vg-btn svg{width:20px;height:20px}.vg-btn:hover{background:rgba(255,255,255,.28)}.vg-btn:active{transform:scale(.92)}
.vg-who{display:flex;align-items:center;gap:10px;min-width:220px;padding:0 6px}
.vg-av{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font:800 1rem var(--display);color:#3A2A00;background:linear-gradient(135deg,#FFF1C2,#E8C877)}
.vg-who b{display:block;font:700 1rem var(--display)}.vg-who small{display:block;font-size:.8rem;color:rgba(255,255,255,.72);max-width:230px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.vg-ct{font:600 .85rem var(--display);color:rgba(255,255,255,.75);padding:0 6px;font-variant-numeric:tabular-nums}
.vg-go{margin-top:18px;padding:12px 26px;border-radius:999px;background:var(--gl);box-shadow:inset 0 0 0 1px var(--glb);color:#fff;font:700 1rem var(--display);text-decoration:none;transition:background .2s}
.vg-go:hover{background:var(--gl2)}
@media (max-width:700px){.vg-sub{display:none}.vg-st{height:300px}.vg-c{width:78vw}.vg-who{min-width:0}.vg-who small{max-width:120px}.vg-ct{display:none}}
/* works by track */
.wx{position:relative;overflow:hidden;isolation:isolate;padding:clamp(64px,7vw,104px) 16px;color:#fff}
.wx-env{position:absolute;inset:0;z-index:-1;background:#0D2E63}
.wx-env img{position:absolute;inset:-12%;width:124%;height:124%;object-fit:cover;filter:blur(70px) saturate(160%) brightness(.7);transition:opacity .5s}
.wx-in{max-width:1180px;margin:0 auto}
.wx h2{font:800 clamp(2.2rem,4.4vw,3.4rem)/1.1 var(--display)}
.wx-l{color:rgba(255,255,255,.82);font-size:1.1rem;margin-top:10px}
.wx-seg{position:relative;display:inline-flex;margin-top:28px;padding:5px;border-radius:999px;background:rgba(255,255,255,.14);box-shadow:inset 0 0 0 1px rgba(255,255,255,.25)}
.wx-seg button{position:relative;z-index:1;border:0;background:none;color:#fff;font:700 1rem var(--display);padding:10px 22px;border-radius:999px;cursor:pointer;transition:color .25s}
.wx-seg button[aria-selected="true"]{color:#0D2E63}
.wx-ind{position:absolute;left:0;top:5px;bottom:5px;border-radius:999px;background:#fff;box-shadow:0 6px 18px rgba(0,0,0,.25);transition:transform .45s cubic-bezier(.3,1.3,.5,1),width .45s}
.wx-w{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:20px;margin-top:28px;align-items:start}
.wx-win{border-radius:28px;overflow:hidden;background:rgba(255,255,255,.12);box-shadow:inset 0 0 0 1px rgba(255,255,255,.28),0 40px 70px -30px rgba(0,0,0,.6)}
.wx-win.sw .wx-m img{animation:wxIn .55s cubic-bezier(.2,.8,.2,1)}
@keyframes wxIn{from{opacity:0;transform:scale(1.04)}}
.wx-bar{display:flex;align-items:center;gap:14px;padding:12px 16px}
.wx-bar span:last-child{flex:1;text-align:center;font-size:.82rem;color:rgba(255,255,255,.7);background:rgba(0,0,0,.18);border-radius:999px;padding:5px 12px;margin-right:46px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.wx-m{position:relative;aspect-ratio:16/10;margin:0 12px;border-radius:18px;overflow:hidden;background:#fff}
.wx-m img{width:100%;height:100%;object-fit:cover;display:block}
.wx-tag{position:absolute;right:10px;bottom:10px;font:600 .75rem var(--display);color:#fff;background:rgba(0,0,0,.45);padding:3px 10px;border-radius:999px}
.wx-d{padding:16px 20px 22px}.wx-d b{font:800 1.5rem var(--display)}.wx-d p{color:rgba(255,255,255,.82);margin-top:4px}
.wx-d em{display:inline-block;margin-top:10px;font-style:normal;font:700 .9rem var(--display);color:#2A1E00;background:var(--yel);padding:4px 12px;border-radius:999px}
.wx-list{list-style:none;margin:0;padding:8px;border-radius:28px;background:rgba(255,255,255,.1);box-shadow:inset 0 0 0 1px rgba(255,255,255,.22);display:grid;gap:4px}
.wx-list button{width:100%;display:flex;align-items:center;gap:14px;border:0;background:none;color:#fff;text-align:left;padding:10px;border-radius:20px;cursor:pointer;transition:background .2s}
.wx-list img{width:72px;height:54px;border-radius:12px;object-fit:cover;flex:none}
.wx-list b{display:block;font:700 1rem var(--display)}.wx-list small{display:block;font-size:.84rem;color:rgba(255,255,255,.72);line-height:1.4}
.wx-list button:hover{background:rgba(255,255,255,.1)}
.wx-list li.on button{background:rgba(255,255,255,.22);box-shadow:inset 0 0 0 1px rgba(255,255,255,.3)}
@media (max-width:900px){.wx-w{grid-template-columns:minmax(0,1fr)}.wx-seg{display:flex;overflow-x:auto;max-width:100%}.wx-seg button{padding:10px 16px;white-space:nowrap}}
.wx-d em[hidden],.wx-tag[hidden]{display:none}
/* small touches */
.zq-s button.ld{display:inline-flex;gap:5px;align-items:center;justify-content:center;min-width:86px}
.zq-s button.ld i{width:7px;height:7px;border-radius:50%;background:#fff;animation:ldB .6s ease-in-out infinite alternate}
.zq-s button.ld i:nth-child(2){animation-delay:.15s}.zq-s button.ld i:nth-child(3){animation-delay:.3s}
@keyframes ldB{from{opacity:.3;transform:translateY(2px)}to{opacity:1;transform:translateY(-2px)}}
.zk-i img{transition:transform .5s cubic-bezier(.2,.8,.2,1)}.zk:hover .zk-i img{transform:scale(1.05)}
/* works page sidebar: glass like the reference */
.yt-side{background:rgba(24,24,24,.72);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border-right:1px solid rgba(255,255,255,.08)}
.yt-side button{border-radius:14px;transition:background .2s,padding .2s}
.yt-side button[aria-current="true"]{background:rgba(255,255,255,.12);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
@media (prefers-reduced-motion:reduce){.vg-c,.wx-ind{transition:none}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v42.html','w').write(s)
print('v42 ok')
