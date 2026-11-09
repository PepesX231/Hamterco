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

JS=r'''  /* v71: hero headline keeps one look; videos play only on screen */
  (function(){
    if(!('IntersectionObserver' in window))return;var rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
    var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting&&!rm)v.play().catch(function(){});else v.pause()})},{threshold:.2});
    document.querySelectorAll('.hx-bg video,.oc-biz video,.us-m video').forEach(function(v){v.removeAttribute('autoplay');io.observe(v)})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
CSS=r'''
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
open('/home/claude/hamsterhub-home/v71p.html','w').write(s)
print('v71p ok')
