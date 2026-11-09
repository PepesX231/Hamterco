import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build46.py').read())
# login: grey hamster avatar inside the button
rep('<span class="peekw" aria-hidden="true"><span class="hd"><img src="img/n-peek.webp" alt=""></span></span>เข้าสู่ระบบ','<img class="lg-h" src="img/ham-grey.webp" alt="">เข้าสู่ระบบ')
# hero: white, floating chibi objects
rep('<div class="zq-town" aria-hidden="true"><img src="img/town.webp" alt=""></div>','<div class="zq-ob" aria-hidden="true">'+''.join('<img class="o%d" src="img/co-%s.webp" alt="">'%(i,n) for i,n in enumerate(['pad','bot','rocket','laptop','cap','bulb']))+'</div>')
# hamster on the search button
i=s.index('<span class="zq-ham" id="zqHam"');j=s.index('</span></span>',i)+len('</span></span>')
s=s[:i]+s[j:]
rep('<button type="submit">ค้นหา</button></form>','<span class="zq-btw"><span class="zq-ham" id="zqHam" aria-hidden="true"><i class="zq-spr" id="zqSpr"></i></span><button type="submit">ค้นหา</button></span></form>')
# what we build
i=s.index('<section class="zb">');j=s.index('</section>',i)+10
T=[('cs-shop','ขายได้จริง','Mr. City เกมแนะนำที่เที่ยวในสงขลา ขายให้สวนสัตว์สงขลาแล้ว','สตาร์ทอัพ'),
   ('cs-play','มีคนเล่นกว่า 1,000 คน','PHC Map เกมสอนเขียนโปรแกรม Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน','เกม'),
   ('cs-trophy','12 ผลงานเข้ารอบชิง NSC','และชนะเลิศ OBEC Roboplayground ด้วยเกมที่เล่นด้วยการบีบอุปกรณ์วัดแรงมือ','IoT และการแข่งขัน'),
   ('cs-web','มหาวิทยาลัยเตรียมใช้','Hamster Quest เว็บเรียนที่เล่นเหมือนเกม กำลังเตรียมใช้กับมหาวิทยาลัย','เว็บ')]
s=s[:i]+'''<section class="zb"><div class="zb-in">
    <h2>ผลงานของน้องไปไกลกว่าแฟ้มพอร์ต</h2>
    <p class="zb-l">น้องที่เรียนกับเราสร้างผลงานที่ขายได้ มีคนเล่นจริง และไปถึงเวทีระดับประเทศ</p>
    <div class="zb-g">'''+''.join('<article class="zb-t"><img src="img/%s.webp" alt="" loading="lazy"><small>%s</small><h3>%s</h3><p>%s</p></article>'%(a,d,b,c) for a,b,c,d in T)+'''</div>
  </div></section>'''+s[j:]
# paths: chibi stickers
for old,new in [('img/p-uni.webp','img/cs-uni.webp'),('img/p-make.webp','img/cs-make.webp'),('img/p-parent.webp','img/cs-parent.webp')]:
    rep('<img src="'+old+'" alt="" loading="lazy">','<span class="zp-im"><img src="'+new+'" alt="" loading="lazy"></span>')
# sprite: head-only frames
rep("background:url(img/ham-peek-sprite.webp) 0 0/400% 100% no-repeat","background:url(img/ham-head-sprite.webp) 0 0/400% 100% no-repeat")
JS=r'''
  /* hero objects follow the mouse */
  (function(){var z=$('.zq');if(!z||!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var I=z.querySelectorAll('.zq-ob img'),D=[1.2,.7,1.4,.9,1.1,.6],tx=0,ty=0,cx=0,cy=0,run=false;
    z.addEventListener('pointermove',function(e){tx=e.clientX/innerWidth-.5;ty=e.clientY/innerHeight-.5;if(!run){run=true;requestAnimationFrame(loop)}});
    function loop(){cx+=(tx-cx)*.07;cy+=(ty-cy)*.07;I.forEach(function(im,i){im.style.translate=(-cx*46*D[i])+'px '+(-cy*34*D[i])+'px'});if(Math.abs(tx-cx)>.001||Math.abs(ty-cy)>.001)requestAnimationFrame(loop);else run=false}})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v47 ===== */
/* login avatar */
.login{display:inline-flex!important;align-items:center;gap:8px;padding-left:6px!important}
.lg-h{width:28px;height:28px;object-fit:contain;transition:transform .35s cubic-bezier(.3,1.8,.5,1)}
.login:hover .lg-h{transform:rotate(-12deg) scale(1.15)}
/* hero: white stage with floating chibi objects */
.zq{background:#fff!important}
.zq-top{margin-top:0!important}
.zq-ob{position:absolute;inset:0;z-index:0;pointer-events:none}
.zq-ob img{position:absolute;width:clamp(70px,7vw,110px);filter:drop-shadow(0 14px 18px rgba(13,46,99,.14));animation:zqF 6s ease-in-out infinite}
.zq-ob .o0{left:12%;top:18%;rotate:-12deg}.zq-ob .o1{left:7%;top:52%;animation-delay:-1.5s}.zq-ob .o2{left:20%;bottom:12%;rotate:10deg;animation-delay:-3s}
.zq-ob .o3{right:11%;top:16%;rotate:8deg;animation-delay:-2s}.zq-ob .o4{right:6%;top:50%;rotate:-8deg;animation-delay:-4s}.zq-ob .o5{right:19%;bottom:13%;animation-delay:-.8s}
@keyframes zqF{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
@media (max-width:900px){.zq-ob .o1,.zq-ob .o4{display:none}.zq-ob img{width:58px;opacity:.9}.zq-ob .o0{left:4%;top:8%}.zq-ob .o3{right:4%;top:8%}.zq-ob .o2{left:6%;bottom:16%}.zq-ob .o5{right:6%;bottom:16%}}
.zq-s{background:#fff!important;border:1px solid #DCE4F0!important;box-shadow:0 12px 40px -16px rgba(13,46,99,.25)!important}
.zq-pop button{background:#F2F5FA!important;border-color:transparent!important}
.zq-more i{background:#F2F5FA;box-shadow:none}
/* the hamster sits on the search button */
.zq-btw{position:relative;display:inline-flex}
.zq-btw .zq-ham{position:absolute!important;left:50%!important;right:auto!important;bottom:calc(100% - 10px)!important;top:auto!important;width:44px!important;height:auto!important;overflow:visible!important;z-index:2!important;transform:translateX(-50%) translateY(18px) scale(.6);opacity:0;transition:transform .5s cubic-bezier(.3,1.7,.5,1),opacity .3s;pointer-events:none}
.zq-btw .zq-ham.up{transform:translateX(-50%);opacity:1}
.zq-btw .zq-ham.watch{transform:translateX(-50%) translateY(-4px) rotate(-6deg)}
.zq-btw .zq-ham.nod{animation:zqNod2 .25s ease-out}
@keyframes zqNod2{50%{margin-bottom:-3px}}
.zq-btw .zq-ham.dive{animation:zqDv 1.1s cubic-bezier(.5,0,.3,1)}
@keyframes zqDv{0%{transform:translateX(-50%)}20%{transform:translateX(-50%) translateY(-14px) scale(1.1)}45%{transform:translateX(-50%) translateY(26px) scale(.3);opacity:0}70%{transform:translateX(-50%) translateY(26px) scale(.3);opacity:0}100%{transform:translateX(-50%);opacity:1}}
.zq-btw .zq-spr{display:block;width:44px!important;aspect-ratio:140/125;background-size:400% 100%}
.zq-btw button{position:relative;z-index:1}
/* rails: Apple-style */
.zc2.dk{background:#F5F5F7!important}
.dk .mr-l h2{color:#0D2E63!important}.dk .mr-l p{color:#4A5874!important}
.mr-btn{border-radius:999px!important;background:#0D2E63!important;color:#fff!important;box-shadow:none!important;padding:12px 24px!important;font-weight:700!important}
.mr-btn:hover{background:#1C74D9!important}
.mr-ar button,.dk .mr-ar button{background:rgba(255,255,255,.7)!important;border:0!important;color:#0D2E63!important;box-shadow:inset 0 0 0 1px rgba(13,46,99,.12),0 6px 16px -10px rgba(13,46,99,.4);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px)}
.mr-ar button:hover{background:#0D2E63!important;color:#fff!important}
.mk,.dk .mk{border-radius:22px!important;padding:0!important;background:#fff!important;color:#10213F!important;overflow:hidden;box-shadow:0 2px 6px rgba(13,46,99,.05),0 18px 40px -24px rgba(13,46,99,.35)!important}
.mk:hover{transform:translateY(-6px) scale(1.01)!important}
.mk-i{border-radius:0!important}
.mk-k{left:12px!important;bottom:12px!important;border-radius:999px;padding:4px 12px!important;background:rgba(255,255,255,.85)!important;color:#0D2E63!important;box-shadow:none!important;-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);font-weight:700!important}
.mk-b{padding:16px 18px 18px!important}
.dk .mk-d,.dk .mk-f{color:#4A5874!important}.dk .mk-f em,.mk-f em{color:#0D2E63!important}
.dk .mk.on .mk-s,.mk.on .mk-s{color:#16803C!important}
.mk-a,.dk .mk-a{background:none!important;color:#1C74D9!important;text-align:left!important;padding:0!important;margin-top:12px!important}
.mk.on .mk-a,.dk .mk.on .mk-a{background:#FFC531!important;color:#2A1E00!important;text-align:center!important;padding:10px!important;border-radius:999px!important}
/* what we build */
.zb-g{grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:16px!important}
.zb-t{min-height:0!important;align-items:center;text-align:center;padding:32px 24px 34px;border-radius:28px!important;background:#F5F5F7!important;color:#10213F!important;transition:transform .3s}
.zb-t:hover{transform:translateY(-6px)}
.zb-t img{width:72%;max-width:190px;aspect-ratio:1;object-fit:contain;transition:transform .5s cubic-bezier(.3,1.6,.5,1)}
.zb-t:hover img{transform:scale(1.08) rotate(-3deg)}
.zb-t small{margin-top:18px;font:700 .9rem var(--display);color:#1C74D9;opacity:1}
.zb-t h3{font:800 clamp(1.4rem,2vw,1.8rem)/1.2 var(--display)!important;color:#0D2E63;margin-top:6px}
.zb-t p{font-size:.95rem!important;color:#4A5874;opacity:1!important;margin-top:8px}
@media (max-width:1000px){.zb-g{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media (max-width:560px){.zb-g{grid-template-columns:minmax(0,1fr)!important}}
/* paths: stickers on soft tiles */
.zp{background:#fff!important}
.zp-c{background:#F5F5F7!important;box-shadow:none!important}
.zp-c:hover{box-shadow:0 24px 40px -26px rgba(13,46,99,.4)!important}
.zp-im{display:grid!important;place-items:center;padding:24px!important;height:300px;flex:none!important}
.zp-c:nth-child(1) .zp-im{background:#FFF4DE}.zp-c:nth-child(2) .zp-im{background:#E6F1FF}.zp-c:nth-child(3) .zp-im{background:#FFE9EF}
.zp-im img{width:auto!important;max-width:80%;max-height:252px;aspect-ratio:auto!important;object-fit:contain!important;transition:transform .5s cubic-bezier(.3,1.6,.5,1)}
.zp-c:hover .zp-im img{transform:scale(1.06) rotate(-2deg)}
/* seniors: clear glass, no reflection */
.mc-c img{-webkit-box-reflect:none!important}
.mc-u{background:rgba(255,255,255,.35)!important;box-shadow:inset 0 0 0 1px rgba(13,46,99,.12),0 10px 30px -18px rgba(13,46,99,.35);-webkit-backdrop-filter:blur(18px) saturate(160%);backdrop-filter:blur(18px) saturate(160%)}
.mc-u button[aria-pressed="true"]{background:rgba(255,255,255,.75)!important;box-shadow:inset 0 0 0 1px rgba(255,255,255,.9),0 4px 12px -4px rgba(13,46,99,.25)!important}
.mc .lk{background:rgba(255,255,255,.35)!important;color:#0D2E63!important;box-shadow:inset 0 0 0 1px rgba(13,46,99,.15),0 10px 24px -16px rgba(13,46,99,.35);-webkit-backdrop-filter:blur(18px);backdrop-filter:blur(18px)}
.mc .lk:hover{background:rgba(255,255,255,.7)!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v47.html','w').write(s)
print('v47 ok')
