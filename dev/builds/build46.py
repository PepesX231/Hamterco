import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build45.py').read())
def cutb(a,b):
    global s;i=s.index(a);j=s.index(b,i);s=s[:i]+s[j:]
# ---------- hero: drop repeated works, cute town scene, sprite hamster, scroll cue
s=re.sub(r'<div class="zq-fl" aria-hidden="true">.*?</div></div>','',s,count=1,flags=re.S)
s=re.sub(r'<div class="zq-dc" aria-hidden="true">.*?</div>','<div class="zq-town" aria-hidden="true"><img src="img/town.webp" alt=""></div>',s,count=1,flags=re.S)
i=s.index('<span class="zq-ham" id="zqHam"');j=s.index('<i class="zq-paw r"></i></span>',i)+len('<i class="zq-paw r"></i></span>')
s=s[:i]+'<span class="zq-ham" id="zqHam" aria-hidden="true"><span class="zq-ham-in"><i class="zq-spr" id="zqSpr"></i></span></span>'+s[j:]
rep('<p class="zq-pop"><span>คนค้นหาบ่อย</span>','<p class="zq-pop"><span>คนค้นหาบ่อย</span>')
i=s.index('<section class="zq"');j=s.index('</section>',i)
s=s[:j]+'<button type="button" class="zq-more" id="zqMore" aria-label="เลื่อนลงดูต่อ"><i><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></i></button>'+s[j:]
# fonts
s=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/css2\?family=Kanit:wght@800[^"]*">','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kanit:wght@800;900&family=Mitr:wght@700&family=Chakra+Petch:wght@700&family=Sriracha&family=Srisakdi:wght@700&family=Itim&family=Pattaya&family=Charmonman:wght@700&family=Chonburi&display=swap">',s,count=1)
rep("var W2=['ยื่นพอร์ตเข้ามหาลัย','สร้างเกมของตัวเอง','เรียน AI','เขียน Python','ลงแข่ง Game Jam']","var W2=['ยื่นพอร์ตเข้ามหาลัย','สร้างเกมของตัวเอง','ทำหุ่นยนต์ IoT','เรียน AI','สร้างสตาร์ทอัพ','เขียน Python','ลงแข่ง Game Jam','ทำเว็บของตัวเอง']")
# replace old hamster + font JS
cutb('/* search hamster: peeks','  /* activity list */')
# ---------- cards: marketplace style
i=s.index('function cardH(x){');j=s.index('    function render(',i)
s=s[:i]+r'''function cardH(x){var cta=x.k==='course'?(x.open?'ดูรายละเอียดและสมัคร':'รับแจ้งเตือนรอบใหม่'):(x.open?'ดูรายละเอียดงาน':'รับแจ้งเตือนงานหน้า');
      return '<a class="mk'+(x.open?' on':'')+'" href="'+x.url+'" target="_blank" rel="noopener"><span class="mk-i"><img src="'+x.img+'" alt="" loading="lazy"><span class="mk-k">'+(x.k==='course'?'คอร์สเรียน':x.k)+'</span></span><span class="mk-b"><b>'+x.t+'</b><span class="mk-d">'+x.d+'</span><span class="mk-f"><span class="mk-s">'+x.st+'</span>'+(x.pr?'<em>'+x.pr+'</em>':'')+'</span><span class="mk-a">'+cta+'</span></span></a>'}
'''+s[j:]
AR='<div class="mr-ar"><button type="button" class="mr-p" aria-label="เลื่อนไปทางซ้าย"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button><button type="button" class="mr-n" aria-label="เลื่อนไปทางขวา"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>'
rep('<div class="nw2-l"><h3>กิจกรรมล่าสุด</h3><div class="zq-g" id="zqN"></div><a class="nw2-all" href="#activity">ดูกิจกรรมทั้งหมด</a></div>',
    '<div class="mr lt"><div class="mr-l"><h3>กิจกรรมล่าสุด</h3><p>ค่าย เวิร์กชอป และงานแข่งที่จัดไปแล้ว กดรับแจ้งเตือนงานหน้าได้</p><a class="mr-btn" href="#activity">ดูกิจกรรมทั้งหมด</a>'+AR+'</div><div class="mr-r" id="zqN"></div></div>')
rep('<section class="zc2"><div class="zc2-in"><h2>คอร์สเรียน</h2><p>คอร์สที่เปิดรับตอนนี้ และคอร์สที่กดรับแจ้งเตือนรอบใหม่ได้</p><div class="zq-g" id="zqC"></div></div></section>',
    '<section class="zc2 dk"><div class="mr"><div class="mr-l"><h2>คอร์สเรียน</h2><p>ทุกคอร์สจบแล้วน้องได้ผลงานจริงของตัวเอง คอร์สที่ยังไม่เปิดรอบ กดรับแจ้งเตือนได้</p><a class="mr-btn" href="#courses">ดูคอร์สทั้งหมด</a>'+AR+'</div><div class="mr-r" id="zqC"></div></div></section>')
# ---------- what we build + paths (replaces the old block)
i=s.index('<section class="za">');j=s.index('</section>',i)+10
NEW='''<section class="zb"><div class="zb-in">
    <h2>ผลงานของน้องไปไกลกว่าแฟ้มพอร์ต</h2>
    <p class="zb-l">น้องที่เรียนกับเราสร้างผลงานที่ขายได้ มีคนเล่นจริง และไปถึงเวทีระดับประเทศ</p>
    <div class="zb-g">
      <article class="zb-t c1"><div><small>สตาร์ทอัพ</small><h3>ขายได้จริง</h3><p>Mr. City เกมแนะนำที่เที่ยวในสงขลา ขายให้สวนสัตว์สงขลาแล้ว</p></div><figure><img src="img/g-mrcity.webp" alt="" loading="lazy"><figcaption>ภาพประกอบ</figcaption></figure></article>
      <article class="zb-t c2"><div><small>เกมเพื่อการเรียน</small><h3>มีคนเล่นกว่า 1,000 คน</h3><p>PHC Map เกมสอนเขียนโปรแกรม Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน</p></div><figure><img src="img/g-phc.webp" alt="" loading="lazy"><figcaption>ภาพประกอบ</figcaption></figure></article>
      <article class="zb-t c3"><div><small>เวทีระดับประเทศ</small><h3>12 ผลงานเข้ารอบชิง NSC</h3><p>และชนะเลิศ OBEC Roboplayground ด้วยเกมที่เล่นด้วยการบีบอุปกรณ์วัดแรงมือ</p></div><figure><img src="img/s-showcase2.webp" alt="งานโชว์ผลงานของน้องๆ" loading="lazy"></figure></article>
      <article class="zb-t c4"><div><small>เว็บ</small><h3>มหาวิทยาลัยเตรียมใช้</h3><p>Hamster Quest เว็บเรียนที่เล่นเหมือนเกม กำลังเตรียมใช้กับมหาวิทยาลัย</p></div><figure><img src="img/g-quest.webp" alt="" loading="lazy"><figcaption>ภาพประกอบ</figcaption></figure></article>
    </div>
  </div></section>
  <section class="zp"><div class="zp-in">
    <h2>เลือกเส้นทางของน้อง</h2>
    <div class="zp-g">
      <a class="zp-c" href="#" data-q="ยื่นพอร์ต"><img src="img/p-uni.webp" alt="" loading="lazy"><span><b>อยากเข้ามหาลัยรอบพอร์ต</b><em>ทำผลงานจริงใส่แฟ้มพอร์ต แล้วซ้อมตอบคำถามกรรมการจนพร้อม</em><i>ดูคอร์สทำพอร์ต</i></span></a>
      <a class="zp-c" href="#" data-q="สร้างเกม"><img src="img/p-make.webp" alt="" loading="lazy"><span><b>อยากสร้างเกมหรือเว็บเป็น</b><em>ไม่เคยเขียนโค้ดก็เริ่มได้ จบแล้วมีผลงานที่เล่นได้จริงเป็นของตัวเอง</em><i>ดูคอร์สและค่าย</i></span></a>
      <a class="zp-c" href="https://page.line.me/jkm4247u?openQrModal=true" target="_blank" rel="noopener"><img src="img/p-parent.webp" alt="" loading="lazy"><span><b>ผู้ปกครองอยากถามก่อน</b><em>คุยกับทีมเรื่องคอร์ส ราคา และวันเรียน ก่อนตัดสินใจ</em><i>ทัก LINE ถามทีม</i></span></a>
    </div>
  </div></section>'''
s=s[:i]+NEW+s[j:]
JS=r'''
  /* search hamster: 15 fps sprite (0 straight, 1 left, 2 right, 3 blink) */
  (function(){var h=$('#zqHam'),sp=$('#zqSpr'),f=$('#zqForm'),inp=$('#zqIn');if(!h||!sp)return;setTimeout(function(){h.classList.add('up')},600);
    var T=[],add=function(fr,n){for(var i=0;i<n;i++)T.push(fr)};add(0,30);add(3,2);add(0,8);add(1,14);add(0,6);add(2,14);add(0,24);add(3,2);add(0,3);add(3,2);add(0,12);
    var t=0,mode='idle',ov=-1;function draw(fr){sp.style.backgroundPosition=(fr*100/3)+'% 0'}
    setInterval(function(){if(document.hidden)return;var fr=T[t%T.length];t++;if(ov>=0&&fr!==3)fr=ov;draw(fr)},1000/15);
    f.addEventListener('pointerenter',function(){h.classList.add('watch')});f.addEventListener('pointerleave',function(){if(document.activeElement!==inp){h.classList.remove('watch');ov=-1}});
    inp.addEventListener('focus',function(){h.classList.add('watch');ov=0});inp.addEventListener('blur',function(){h.classList.remove('watch');ov=-1});
    inp.addEventListener('input',function(){ov=inp.value.length%2?1:2;h.classList.remove('nod');void h.offsetWidth;h.classList.add('nod')});
    function dive(){h.classList.remove('dive');void h.offsetWidth;h.classList.add('dive');setTimeout(function(){h.classList.remove('dive')},1100)}
    f.addEventListener('submit',dive);document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('.zq-pop [data-q]'))dive()})})();
  /* headline: every phrase gets its own type style */
  (function(){var el=$('#zqType');if(!el)return;var h=el.parentNode,S=['kanit','persona','pencil','elden','glitch','comic','script','block'],k=0,last=el.textContent;h.dataset.f=S[0];
    new MutationObserver(function(){var t=el.textContent;if(t.length<=1&&last.length>1){k=(k+1)%S.length;h.dataset.f=S[k]}last=t}).observe(el,{childList:true,characterData:true,subtree:true})})();
  /* scroll cue: nudges if nobody scrolls */
  (function(){var b=$('#zqMore');if(!b)return;b.addEventListener('click',function(){var n=$('.nw2');if(n)n.scrollIntoView({behavior:'smooth'})});
    var iv=setInterval(function(){if(scrollY>40||!document.querySelector('[data-view="home"].on')){b.classList.remove('nudge');return}b.classList.remove('nudge');void b.offsetWidth;b.classList.add('nudge')},3200);
    addEventListener('scroll',function(){b.classList.toggle('gone',scrollY>80)},{passive:true})})();
  /* rails */
  document.querySelectorAll('.mr').forEach(function(m){var r=m.querySelector('.mr-r');if(!r)return;function st(d){var c=r.querySelector('.mk');r.scrollBy({left:d*((c?c.offsetWidth:300)+18),behavior:'smooth'})}
    m.querySelector('.mr-p').addEventListener('click',function(){st(-1)});m.querySelector('.mr-n').addEventListener('click',function(){st(1)})});
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v46 ===== */
/* hero */
.zq{background:#C4E8FE!important}
.zq::after{display:none}
.zq-town{position:absolute;left:0;right:0;bottom:0;z-index:0;pointer-events:none}
.zq-town img{display:block;width:100%;height:auto;min-height:34vh;object-fit:cover;object-position:50% 100%;-webkit-mask:linear-gradient(transparent,#000 22%);mask:linear-gradient(transparent,#000 22%)}
.zq-top{margin-top:-14vh}
.zq-q{color:#335A86}
.zq-h{background:none!important;-webkit-background-clip:border-box!important;background-clip:border-box!important;color:#0D2E63!important}
.zq-pop button{background:rgba(255,255,255,.85)}
/* typing styles */
.zq-h #zqType{display:inline-block;transition:none}
.zq-h[data-f="kanit"] #zqType{font-family:'Kanit',var(--display);font-weight:900}
.zq-h[data-f="persona"] #zqType{font-family:'Kanit',var(--display);font-weight:900;color:#fff;background:#111;padding:0 .3em .05em;transform:skew(-8deg) rotate(-2deg);box-shadow:.14em .14em 0 #E5222A}
.zq-h[data-f="pencil"] #zqType{font-family:'Itim',var(--display);font-weight:400;color:#3A3F47;transform:rotate(-1.5deg);text-shadow:1px 1px 0 rgba(58,63,71,.35),-1px 0 0 rgba(58,63,71,.2)}
.zq-h[data-f="elden"] #zqType{font-family:'Srisakdi',serif;font-weight:700;letter-spacing:.03em;background:linear-gradient(180deg,#F6E3A6,#B88A2E 60%,#7A5A18);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 2px 6px rgba(120,80,10,.35))}
.zq-h[data-f="glitch"] #zqType{font-family:'Chakra Petch',var(--display);font-weight:700;color:#0D2E63;animation:zqGl .5s steps(2) infinite}
@keyframes zqGl{0%{text-shadow:3px 0 #FF2E63,-3px 0 #08D9D6}50%{text-shadow:-2px 1px #FF2E63,2px -1px #08D9D6}100%{text-shadow:1px -1px #FF2E63,-1px 1px #08D9D6}}
.zq-h[data-f="comic"] #zqType{font-family:'Pattaya',var(--display);color:#FFC531;-webkit-text-stroke:6px #0D2E63;paint-order:stroke fill;transform:rotate(-2deg)}
.zq-h[data-f="script"] #zqType{font-family:'Charmonman',cursive;font-weight:700;color:#B23A68}
.zq-h[data-f="block"] #zqType{font-family:'Chonburi',serif;color:#1C74D9;text-shadow:3px 3px 0 #0D2E63,6px 6px 0 rgba(13,46,99,.25)}
/* sprite hamster */
.zq-ham{width:132px!important;height:96px!important;right:110px!important}
.zq-ham-in{width:132px!important;transform:translateY(64%)}
.zq-ham.up .zq-ham-in{transform:translateY(24%)}
.zq-ham.watch .zq-ham-in{transform:translateY(6%)}
.zq-spr{display:block;width:132px;aspect-ratio:220/188;background:url(img/ham-peek-sprite.webp) 0 0/400% 100% no-repeat;image-rendering:auto}
@media (max-width:700px){.zq-ham{right:84px!important;width:96px!important;height:72px!important}.zq-ham-in,.zq-spr{width:96px!important}}
/* scroll cue */
.zq-more{position:absolute;left:50%;bottom:24px;z-index:3;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:6px;border:0;background:none;cursor:pointer;color:#0D2E63;font:600 .85rem var(--display);transition:opacity .3s}
.zq-more i{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.7);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);box-shadow:0 8px 20px -8px rgba(13,46,99,.4),inset 0 0 0 1px rgba(255,255,255,.8)}
.zq-more svg{width:22px;height:22px}
.zq-more.nudge i{animation:zqNg .9s cubic-bezier(.3,1.6,.5,1)}
@keyframes zqNg{0%,100%{transform:none}15%{transform:translateY(8px)}30%{transform:translateY(-3px)}45%{transform:translateY(6px)}60%{transform:translateY(-2px)}75%{transform:translateY(3px)}}
.zq-more.gone{opacity:0;pointer-events:none}
/* marketplace rails */
.mr{max-width:1320px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:300px minmax(0,1fr);gap:40px;align-items:start}
.nw2 .mr{margin-top:48px}
.mr-l h2,.mr-l h3{font:800 clamp(2rem,3.4vw,2.8rem)/1.1 var(--display);color:#0D2E63}
.mr-l p{color:#4A5874;margin-top:12px;line-height:1.6}
.mr-btn{display:inline-block;margin-top:22px;padding:12px 22px;background:#FFC531;color:#2A1E00;font:800 1rem var(--display);text-decoration:none;box-shadow:0 4px 0 #C99410;transition:transform .1s,box-shadow .1s}
.mr-btn:active{transform:translateY(3px);box-shadow:0 1px 0 #C99410}
.mr-ar{display:flex;gap:10px;margin-top:28px}
.mr-ar button{width:48px;height:48px;border-radius:50%;border:1px solid #CFD9E8;background:#fff;color:#0D2E63;display:grid;place-items:center;cursor:pointer;transition:background .2s,transform .15s}
.mr-ar button:hover{background:#0D2E63;color:#fff}.mr-ar button:active{transform:scale(.92)}
.mr-ar svg{width:20px;height:20px}
.mr-r{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;padding:4px 4px 20px;scrollbar-width:none;margin-right:-24px}
.mr-r::-webkit-scrollbar{display:none}
.mk{flex:0 0 300px;scroll-snap-align:start;display:flex;flex-direction:column;background:#fff;color:#10213F;text-decoration:none;padding:14px;border-radius:6px;box-shadow:0 1px 0 rgba(13,46,99,.06),0 12px 28px -18px rgba(13,46,99,.45);transition:transform .2s,box-shadow .2s}
.mk:hover{transform:translateY(-4px);box-shadow:0 22px 36px -18px rgba(13,46,99,.55)}
.mk-i{position:relative;display:block;aspect-ratio:16/10;overflow:hidden;border-radius:3px;background:#E6ECF4}
.mk-i img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.mk:hover .mk-i img{transform:scale(1.05)}
.mk-i img[src*="afo-logo"]{object-fit:contain;padding:14px;background:#1C74D9}
.mk-k{position:absolute;left:0;bottom:0;padding:4px 10px;background:#FFC531;color:#2A1E00;font:800 .78rem var(--display);box-shadow:inset 0 0 0 2px #2A1E00}
.mk-b{display:flex;flex-direction:column;flex:1;padding-top:12px}
.mk-b b{font:800 1.12rem/1.3 var(--display)}
.mk-d{font-size:.9rem;color:#4A5874;margin-top:4px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.mk-f{display:flex;justify-content:space-between;align-items:baseline;gap:8px;margin-top:auto;padding-top:14px;font-size:.88rem;color:#6B7A94}
.mk.on .mk-s{color:#16803C;font-weight:700}
.mk-f em{font-style:normal;font:800 1.15rem var(--display);color:#0D2E63}
.mk-a{margin-top:12px;text-align:center;padding:9px;font:700 .92rem var(--display);color:#1C74D9;background:#EEF4FC;border-radius:4px}
.mk.on .mk-a{background:#FFC531;color:#2A1E00}
/* dark course band */
.zc2.dk{background:#0B1B36!important;padding:clamp(64px,7vw,104px) 0}
.dk .mr-l h2{color:#FFC531}.dk .mr-l p{color:rgba(255,255,255,.75)}
.dk .mr-ar button{background:transparent;border-color:rgba(255,255,255,.35);color:#fff}.dk .mr-ar button:hover{background:#fff;color:#0B1B36}
.dk .mk{background:#16294A;color:#fff;box-shadow:0 20px 34px -20px rgba(0,0,0,.7)}
.dk .mk-d,.dk .mk-f{color:rgba(255,255,255,.7)}.dk .mk-f em{color:#FFC531}.dk .mk.on .mk-s{color:#7CE3A6}
.dk .mk-a{background:rgba(255,255,255,.1);color:#fff}.dk .mk.on .mk-a{background:#FFC531;color:#2A1E00}
/* search results + courses page use the same cards in a grid */
.zq-res .zq-g,.ctg{display:grid!important;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}
.zq-res .mk,.ctg .mk{flex:auto}
@media (max-width:900px){.mr{grid-template-columns:minmax(0,1fr);gap:20px}.mr-ar{display:none}.mk{flex-basis:78%}.zq-res .zq-g,.ctg{display:flex!important;overflow-x:auto;scroll-snap-type:x mandatory}.zq-res .mk,.ctg .mk{flex:0 0 78%}}
/* what we build */
.zb{background:#fff;padding:clamp(80px,9vw,140px) 16px}
.zb-in{max-width:1240px;margin:0 auto}
.zb h2{font:800 clamp(2.4rem,5vw,4.2rem)/1.1 var(--display);letter-spacing:-.02em;color:#0D2E63;max-width:14em}
.zb-l{font-size:1.25rem;color:#4A5874;margin-top:16px;max-width:34em}
.zb-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:clamp(40px,5vw,64px)}
.zb-t{position:relative;display:flex;flex-direction:column;border-radius:32px;overflow:hidden;min-height:540px}
.zb-t>div{padding:40px 40px 0}
.zb-t small{font:700 1rem var(--display);opacity:.7}
.zb-t h3{font:800 clamp(1.9rem,3vw,2.6rem)/1.15 var(--display);margin-top:6px}
.zb-t p{font-size:1.06rem;line-height:1.6;margin-top:10px;max-width:28em;opacity:.85}
.zb-t figure{position:relative;margin:auto 0 0;padding:28px 40px 0}
.zb-t figure img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:20px 20px 0 0;box-shadow:0 -10px 40px -20px rgba(0,0,0,.3);transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.zb-t:hover figure img{transform:translateY(-8px)}
.zb-t figcaption{position:absolute;right:52px;top:40px;font:600 .75rem var(--display);color:#fff;background:rgba(0,0,0,.45);padding:3px 10px;border-radius:999px}
.zb-t.c1{background:#FFF4DE;color:#5A3A00}.zb-t.c2{background:#E6F1FF;color:#0D2E63}.zb-t.c3{background:#0D2E63;color:#fff}.zb-t.c4{background:#EFEAFF;color:#3A2A7A}
@media (max-width:900px){.zb-g{grid-template-columns:minmax(0,1fr)}.zb-t{min-height:0}.zb-t>div{padding:28px 24px 0}.zb-t figure{padding:22px 24px 0}.zb-t figcaption{right:34px;top:32px}}
/* paths */
.zp{background:#F5F7FB;padding:clamp(72px,8vw,120px) 16px}
.zp-in{max-width:1240px;margin:0 auto}
.zp h2{font:800 clamp(2.2rem,4.4vw,3.4rem) var(--display);color:#0D2E63}
.zp-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:32px}
.zp-c{display:flex;flex-direction:column;background:#fff;border-radius:28px;overflow:hidden;text-decoration:none;color:#10213F;box-shadow:0 20px 40px -28px rgba(13,46,99,.45);transition:transform .25s,box-shadow .25s}
.zp-c:hover{transform:translateY(-6px);box-shadow:0 30px 50px -28px rgba(13,46,99,.55)}
.zp-c img{width:100%;aspect-ratio:4/3;object-fit:cover;transition:transform .6s}
.zp-c:hover img{transform:scale(1.04)}
.zp-c span{display:flex;flex-direction:column;gap:8px;padding:24px 26px 28px;flex:1}
.zp-c b{font:800 1.4rem/1.25 var(--display);color:#0D2E63}
.zp-c em{font-style:normal;color:#4A5874;line-height:1.6}
.zp-c i{font-style:normal;margin-top:auto;padding-top:10px;font:700 1rem var(--display);color:#1C74D9}
@media (max-width:900px){.zp-g{grid-template-columns:minmax(0,1fr)}}
/* seniors: Apple-style stage */
.mc{padding:0!important}
.mc-in{padding:clamp(80px,9vw,130px) 16px 72px!important}
.mc-k{color:#6B7A94!important;font-weight:600}
.mc h2{font-size:clamp(1.6rem,3vw,2.4rem)!important;color:#0D2E63!important}
.mc h2 span{display:block;font:900 clamp(5rem,13vw,10rem)/1 var(--display);letter-spacing:-.04em;margin-top:6px;background:linear-gradient(180deg,#2A86E8,#0D2E63);-webkit-background-clip:text;background-clip:text;color:transparent!important}
.mc-u{display:inline-flex!important;gap:2px!important;padding:4px;border-radius:999px;background:#EEF1F6;margin-top:28px!important}
.mc-u button{border-radius:999px!important;padding:9px 18px!important;color:#4A5874!important;font-weight:600}
.mc-u button[aria-pressed="true"]{background:#fff!important;color:#0D2E63!important;box-shadow:0 2px 8px rgba(13,46,99,.18)}
.mc-u button[aria-pressed="true"] b,.mc-u button b{color:#1C74D9!important}
.mc-st{height:clamp(440px,40vw,560px)!important;margin-top:44px!important}
.mc-c{width:clamp(220px,22vw,310px)!important}
.mc-c img{border-radius:22px!important;box-shadow:0 30px 50px -26px rgba(13,46,99,.55)!important}
.mc-c.on img{box-shadow:0 40px 60px -26px rgba(13,46,99,.6)!important}
.mc-cap{margin-top:34px!important}
.mc-cap p{font-size:1.1rem!important;color:#4A5874!important}.mc-cap p b{font-size:1.25rem;color:#0D2E63!important}.mc-cap p small{color:#1C74D9!important;font-weight:600}
.mc .lk{display:inline-block;margin-top:18px;padding:12px 24px;border-radius:999px;background:#0D2E63;color:#fff!important;text-decoration:none;font-weight:700}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v46.html','w').write(s)
print('v46 ok')
