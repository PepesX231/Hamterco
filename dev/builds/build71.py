SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build70.py').read())
# ---------- correct the products ----------
s=s.replace('img/w-mrcity.webp','img/w-quest-town.webp').replace('img/w-quest.webp','img/w-quest-app.webp')
s=s.replace('<div class="oc-m oc-biz"><img src="img/w-quest-town.webp" alt="ภาพจากเกม Mr. City"><img src="img/w-phcmap.webp" alt="ภาพจากเกม PHC Map"><img src="img/w-quest-app.webp" alt="ภาพจากเว็บ Hamster Quest"></div>',
 '<div class="oc-m oc-biz"><video src="img/w-hmap.mp4" poster="img/w-hmap.webp" muted loop playsinline autoplay preload="none" aria-label="คลิปเกมสอนเขียน Python ของน้อง"></video><img src="img/w-quest-town.webp" alt="ภาพจากเว็บ Hamster Quest"><img src="img/w-quest-app.webp" alt="หน้าเควสต์ใน Hamster Quest"></div>')
s=s.replace('<p>Mr. City เกมแนะนำที่เที่ยวในสงขลา ขายให้สวนสัตว์สงขลาแล้ว PHC Map เกมสอนเขียน Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน และ Hamster Quest เว็บเรียนที่เล่นเหมือนเกม กำลังเตรียมใช้กับมหาวิทยาลัย</p>',
 '<p>Mr. City เกมเดินเที่ยวสงขลาแบบเดียวกับ Pokémon GO ขายให้สวนสัตว์สงขลาแล้ว PHC Map เกมสอนเขียน Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน และ Hamster Quest เว็บเรียนที่เล่นเหมือนเกม กำลังเตรียมใช้กับมหาวิทยาลัย</p>')
s=s.replace('<span class="ad-im"><img src="img/w-quest-app.webp" alt="" loading="lazy"><img src="img/w-quest-town.webp" alt="" loading="lazy"></span>','<span class="ad-im"><img src="img/w-quest-town.webp" alt="" loading="lazy"><img src="img/w-hmap.webp" alt="" loading="lazy"></span>')
# about rows
s=s.replace('<article class="us"><div class="us-m"><img src="img/w-quest-town.webp" alt="ภาพจากเกม Mr. City" loading="lazy"></div><div class="us-t"><h3>Mr. City</h3><p>เกมแนะนำที่เที่ยวในสงขลา</p>',
 '<article class="us"><div class="us-m us-city" aria-hidden="true"><i class="p1"></i><i class="p2"></i><i class="p3"></i><b>Mr. City</b><span>สงขลา</span></div><div class="us-t"><h3>Mr. City</h3><p>เกมเดินเที่ยวสงขลา แบบเดียวกับ Pokémon GO</p>')
s=s.replace('<dd>ซื้อเกมนี้ไปใช้แนะนำที่เที่ยวในสงขลา</dd>','<dd>ให้นักท่องเที่ยวเดินไปตามที่เที่ยวจริงในสงขลา แล้วเล่นเกมที่จุดนั้น</dd>')
s=s.replace('<div class="us-m"><img src="img/w-phcmap.webp" alt="ภาพจากเกม PHC Map" loading="lazy"></div>','<div class="us-m"><video src="img/w-hmap.mp4" poster="img/w-hmap.webp" muted loop playsinline autoplay preload="none" aria-label="คลิปเกมสอนเขียน Python"></video></div>')
s=s.replace('<div class="us-m"><img src="img/w-quest-app.webp" alt="ภาพจากเว็บ Hamster Quest" loading="lazy"></div>','<div class="us-m"><img src="img/w-quest-town.webp" alt="ภาพจากเว็บ Hamster Quest" loading="lazy"></div>')
# search answer text
s=s.replace('Mr. City เกมแนะนำที่เที่ยวในสงขลา ขายให้สวนสัตว์สงขลาแล้ว','Mr. City เกมเดินเที่ยวสงขลาแบบ Pokémon GO ขายให้สวนสัตว์สงขลาแล้ว')

# ---------- hero: Hamster Hub's own, cinematic ----------
rep('<i class="zq-sky" aria-hidden="true"></i>','<i class="zq-sky" aria-hidden="true"></i><div class="hx-bg" aria-hidden="true"><video src="img/hh-intro.mp4" poster="img/hh-intro.webp" muted loop playsinline autoplay></video></div>')
rep('<p class="zq-lead">Hamster Hub สอนน้องมัธยมสร้างเกม เว็บ และ IoT ของตัวเอง</p>','<p class="zq-lead">Hamster Hub สอนน้องมัธยมสร้างเกม เว็บ และ IoT ที่มีคนใช้จริง</p>')
i=s.index('<div class="zq-ptn">');j=s.index('</div>',s.index('<div class="zq-brand"'))+6
j=s.index('</div>',j-1)  # end of zq-brand
s=s[:i]+'''<ul class="hx-pf"><li><b>48 คน</b><span>รุ่นพี่ติดมหาลัยรอบ Portfolio ปี 2569</span></li><li><b>12 ผลงาน</b><span>เข้ารอบชิงชนะเลิศ NSC ระดับประเทศ</span></li><li><b>ขายได้จริง</b><span>เกม Mr. City ขายให้สวนสัตว์สงขลา</span></li></ul>
      <div class="hx-pt"><span>จัดกิจกรรมร่วมกับ</span><img src="img/p-it.webp" alt="คณะเทคโนโลยีสารสนเทศ สจล."><img src="img/p-iote.webp" alt="IoTE สจล."><img src="img/p-eduverse.webp" alt="EDUverse"></div>'''+s[j+6:]
assert 'zq-brand' not in s[s.index('<section class="zq"'):s.index('<section class="ft"')]
JS=r'''  /* v71: hero headline keeps one look; videos play only on screen */
  (function(){var h=$('.zq-h');if(h){h.setAttribute('data-f','hx');h.removeAttribute('title');h.addEventListener('click',function(e){e.stopImmediatePropagation()},true)}
    if(!('IntersectionObserver' in window))return;var rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
    var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting&&!rm)v.play().catch(function(){});else v.pause()})},{threshold:.2});
    document.querySelectorAll('.hx-bg video,.oc-biz video,.us-m video').forEach(function(v){v.removeAttribute('autoplay');io.observe(v)})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
CSS=r'''
/* ===== v71: cinematic hero ===== */
.zq{background:#05070D!important;color:#fff;min-height:100svh!important;overflow:hidden}
.zq-sky,.zq-orb,.zq-town,.zq-dc,.zq-fl{display:none!important}
.hx-bg{position:absolute;inset:0;z-index:0;pointer-events:none}
.hx-bg video{width:100%;height:100%;object-fit:cover;opacity:.55}
.hx-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,7,13,.96) 0%,rgba(5,7,13,.82) 38%,rgba(5,7,13,.35) 70%,rgba(5,7,13,.55) 100%),linear-gradient(0deg,#05070D 0%,transparent 30%)}
.zq-top{grid-template-columns:minmax(0,1fr)!important;max-width:1240px!important;position:relative;z-index:2;padding-top:40px!important;padding-bottom:40px!important}
.zq-top>*{max-width:720px}
.zq-lead{color:#C9D6EE!important;font-weight:600!important;margin-bottom:22px!important}
.zq-q{color:#fff!important;font:800 clamp(2.4rem,5.4vw,4.6rem)/1.05 var(--display)!important;margin:0!important;letter-spacing:-.01em}
.zq-h{margin:4px 0 28px!important;min-height:1.15em}
.zq-h[data-f] #zqType,.zq-h #zqType{font:800 clamp(2.4rem,5.4vw,4.6rem)/1.15 var(--display)!important;color:#FFD54A!important;background:none!important;-webkit-text-stroke:0!important;text-shadow:none!important;transform:none!important;box-shadow:none!important;filter:none!important;padding:0!important;letter-spacing:-.01em!important;-webkit-background-clip:border-box!important;background-clip:border-box!important}
.zq-h .zq-cur{background:#FFD54A!important}
.zq-h{cursor:default!important}
.zq-s{background:rgba(255,255,255,.96)!important;box-shadow:0 20px 50px -20px rgba(0,0,0,.6)!important}
.zq-pop>span{color:#9FB0CC!important}
.zq-pop button{background:rgba(255,255,255,.1)!important;color:#fff!important;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)!important;backdrop-filter:none!important}
.zq-pop button:hover{background:rgba(255,255,255,.2)!important}
.hx-pf{list-style:none;margin:44px 0 0;padding:22px 0 0;border-top:1px solid rgba(255,255,255,.14);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;max-width:860px!important}
.hx-pf b{display:block;font:800 clamp(1.4rem,2.2vw,1.9rem)/1.1 var(--display);color:#fff}
.hx-pf span{display:block;margin-top:6px;color:#9FB0CC;font-size:.9rem;line-height:1.45}
.hx-pt{display:flex;flex-wrap:wrap;align-items:center;gap:20px;margin-top:28px}
.hx-pt span{font:600 .82rem var(--display);color:#7F8DA8}
.hx-pt img{height:28px;width:auto;filter:brightness(0) invert(1);opacity:.6}
.zq-more{color:#fff!important}.zq-more i{background:rgba(255,255,255,.12)!important;color:#fff!important}
.zq.ask .hx-pf,.zq.ask .hx-pt{opacity:0;pointer-events:none;transition:opacity .3s}
.zq-sw .zq-res{right:-30%!important}
@media (max-width:1000px){.zq-sw .zq-res{right:0!important}}
@media (max-width:700px){.hx-pf{grid-template-columns:minmax(0,1fr);gap:14px;margin-top:32px}.hx-pf li{display:flex;gap:12px;align-items:baseline}.hx-pf span{margin:0}.hx-bg::after{background:linear-gradient(0deg,#05070D 10%,rgba(5,7,13,.8) 60%,rgba(5,7,13,.6))}.hx-pt img{height:22px}}
/* products */
.oc-biz video,.us-m video{width:100%;height:100%;object-fit:cover;display:block;min-height:0}
.oc-biz video{grid-row:span 2}
.us-city{position:relative;display:flex;flex-direction:column;justify-content:flex-end;padding:28px;background:radial-gradient(circle at 30% 30%,#2F8F6A 0,#1D6B4E 40%,#124834 100%);overflow:hidden}
.us-city::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.08) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.08) 2px,transparent 2px);background-size:56px 56px;transform:rotate(-12deg) scale(1.4)}
.us-city i{position:absolute;width:34px;height:34px;border-radius:50% 50% 50% 0;background:#FFD54A;transform:rotate(-45deg);box-shadow:0 8px 16px rgba(0,0,0,.3)}
.us-city i::after{content:"";position:absolute;inset:10px;border-radius:50%;background:#124834}
.us-city .p1{left:22%;top:22%}.us-city .p2{left:58%;top:34%;background:#fff}.us-city .p3{left:76%;top:14%}
.us-city b{position:relative;font:800 clamp(2rem,4vw,3rem) var(--display);color:#fff}.us-city span{position:relative;color:#CFEBDD;font-weight:700}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v71.html','w').write(s)
print('v71 ok')
