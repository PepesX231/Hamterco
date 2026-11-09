import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build47.py').read())
# login: only ears peek above the button
rep('<img class="lg-h" src="img/ham-grey.webp" alt="">เข้าสู่ระบบ','<span class="lg-e" aria-hidden="true"><img src="img/ham-grey.webp" alt=""></span>เข้าสู่ระบบ')
# hero decoration: real works + 3D icons
i=s.index('<div class="zq-ob" aria-hidden="true">');j=s.index('</div>',i)+6
items=[('w','work-stressstrike','a'),('i','i3-pad','b'),('w','work-phi-krahang','c'),('i','i3-rocket','d'),('w','work-eugation-strike','e'),('i','i3-bot','f'),('w','work-slash-speed','g'),('i','i3-cap','h')]
s=s[:i]+'<div class="zq-ob" aria-hidden="true">'+''.join('<img class="%s %s" src="img/%s.webp" alt="">'%('ow' if t=='w' else 'oi',c,n) for t,n,c in items)+'</div>'+s[j:]
# hamster behind the search bar
rep('<span class="zq-btw"><span class="zq-ham" id="zqHam" aria-hidden="true"><i class="zq-spr" id="zqSpr"></i></span><button type="submit">ค้นหา</button></span></form>','<button type="submit">ค้นหา</button></form>')
rep('<form class="zq-s" id="zqForm" role="search">','<div class="zq-sw"><span class="zq-ham" id="zqHam" aria-hidden="true"><i class="zq-spr" id="zqSpr"></i></span><form class="zq-s" id="zqForm" role="search">')
i=s.index('<form class="zq-s" id="zqForm"');j=s.index('</form>',i)+7
SUG='<div class="zq-sug" id="zqSug" hidden><p>ลองค้นหา</p>'+''.join('<button type="button" data-q="%s"><img src="img/%s.webp" alt="">%s<small>%s</small></button>'%(q,ic,q,d) for q,ic,d in [('ยื่นพอร์ต','i3-cap','คอร์สทำพอร์ตยื่นมหาลัย'),('สร้างเกม','i3-pad','คอร์สและค่ายสร้างเกม'),('IoT','i3-bot','หุ่นยนต์และอุปกรณ์ IoT'),('สตาร์ทอัพ','i3-rocket','ทำผลงานที่ต่อยอดเป็นธุรกิจ')])+'</div></div>'
s=s[:j]+SUG+s[j:]
s=s.replace("background:url(img/ham-head-sprite.webp) 0 0/400% 100% no-repeat","background:url(img/ham-peek2.webp) 0 0/400% 100% no-repeat")
# rails: header row; arrows to the right
for nm in ['zqN','zqC']:
    pass
JS=r'''
  /* search: suggestions on focus, staggered results on submit */
  (function(){var f=$('#zqForm'),inp=$('#zqIn'),sg=$('#zqSug'),h=$('#zqHam');if(!f||!sg)return;
    function open(){if(!inp.value)sg.hidden=false}function close(){sg.hidden=true}
    inp.addEventListener('focus',open);inp.addEventListener('input',function(){sg.hidden=!!inp.value});
    document.addEventListener('pointerdown',function(e){if(!e.target.closest('.zq-sw'))close()});
    sg.addEventListener('click',function(e){var b=e.target.closest('[data-q]');if(b)close()});
    function stagger(){$$('#zqG .mk').forEach(function(c,i){c.style.animationDelay=(i*70)+'ms';c.classList.remove('in');void c.offsetWidth;c.classList.add('in')})}
    f.addEventListener('submit',function(){close();inp.blur();f.classList.remove('go');void f.offsetWidth;f.classList.add('go');setTimeout(function(){stagger();var r=$('#zqRes');if(r&&!r.hidden)r.scrollIntoView({behavior:'smooth',block:'start'})},380)});
    document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('[data-q]')&&e.target.closest('.zq')){f.classList.remove('go');void f.offsetWidth;f.classList.add('go');setTimeout(stagger,380)}})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v48 ===== */
/* login: ears only, head on hover */
.login{position:relative;padding-left:16px!important}
.lg-h{display:none}
.lg-e{position:absolute;left:18px;bottom:100%;width:40px;height:9px;overflow:hidden;pointer-events:none;transition:height .35s cubic-bezier(.3,1.6,.5,1)}
.lg-e img{position:absolute;left:0;top:0;width:40px;height:auto}
.login:hover .lg-e,.login:focus-visible .lg-e{height:24px}
/* hero background like a soft sky that fades to white */
.zq{background:radial-gradient(70% 60% at 50% 0%,#D6E6FF 0%,rgba(214,230,255,0) 70%),linear-gradient(#EAF2FF,#fff 75%)!important}
.zq-ob img{animation:zqF 7s ease-in-out infinite;filter:none}
.zq-ob .ow{width:clamp(150px,13vw,210px);aspect-ratio:4/3;object-fit:cover;border-radius:16px;box-shadow:0 20px 40px -18px rgba(13,46,99,.35);border:4px solid #fff}
.zq-ob .oi{width:clamp(76px,6.4vw,104px);filter:drop-shadow(0 14px 16px rgba(13,46,99,.2))}
.zq-ob .a{left:5%;top:14%;rotate:-6deg}.zq-ob .b{left:19%;top:9%;animation-delay:-2s}
.zq-ob .c{left:3%;top:50%;rotate:4deg;animation-delay:-3s}.zq-ob .d{left:17%;bottom:12%;animation-delay:-1s}
.zq-ob .e{right:5%;top:12%;rotate:6deg;animation-delay:-2.5s}.zq-ob .f{right:19%;top:10%;animation-delay:-4s}
.zq-ob .g{right:4%;top:50%;rotate:-5deg;animation-delay:-1.5s}.zq-ob .h{right:17%;bottom:12%;animation-delay:-3.5s}
@media (max-width:1100px){.zq-ob .c,.zq-ob .g,.zq-ob .b,.zq-ob .f{display:none}}
@media (max-width:700px){.zq-ob .ow{width:96px;border-width:3px}.zq-ob .oi{width:54px}.zq-ob .a{left:3%;top:6%}.zq-ob .e{right:3%;top:6%}.zq-ob .d{left:5%;bottom:14%}.zq-ob .h{right:5%;bottom:14%}}
/* hamster lives behind the search bar */
.zq-sw{position:relative;z-index:6;max-width:720px;margin:28px auto 0;isolation:isolate}
.zq-sw .zq-s{position:relative;z-index:1;margin:0!important;transition:transform .25s,box-shadow .25s}
.zq-sw:hover .zq-s{transform:translateY(-2px);box-shadow:0 18px 44px -16px rgba(13,46,99,.32)!important}
.zq-sw .zq-ham{position:absolute!important;right:120px!important;left:auto!important;bottom:calc(100% - 26px)!important;top:auto!important;width:84px!important;height:auto!important;z-index:0!important;overflow:visible!important;transform:translateY(46px);opacity:1;transition:transform .55s cubic-bezier(.3,1.6,.5,1);pointer-events:none}
.zq-sw .zq-ham.up{transform:translateY(18px)}
.zq-sw:hover .zq-ham,.zq-sw .zq-ham.watch{transform:translateY(0)}
.zq-sw .zq-ham.dive{animation:zqDv2 1s cubic-bezier(.5,0,.3,1)}
@keyframes zqDv2{0%{transform:translateY(0)}25%{transform:translateY(-16px)}55%{transform:translateY(70px)}80%{transform:translateY(70px)}100%{transform:translateY(18px)}}
.zq-sw .zq-spr{display:block;width:84px!important;aspect-ratio:180/161;background-size:400% 100%!important}
@media (max-width:700px){.zq-sw .zq-ham{right:80px!important;width:64px!important}.zq-sw .zq-spr{width:64px!important}}
/* search press + suggestions */
.zq-s button{border-radius:999px;transition:transform .12s,background .2s}
.zq-s button:active{transform:scale(.94)}
.zq-s.go{animation:zqGo .45s cubic-bezier(.3,1.4,.5,1)}
@keyframes zqGo{30%{transform:scale(.985)}}
.zq-s.go::after{content:"";position:absolute;inset:-1px;border-radius:999px;pointer-events:none;background:linear-gradient(90deg,transparent,rgba(28,116,217,.35),transparent) -100% 0/50% 100% no-repeat;animation:zqSw .5s ease-out forwards}
@keyframes zqSw{to{background-position:200% 0}}
.zq-sug{position:absolute;left:0;right:0;top:calc(100% + 10px);z-index:5;padding:10px;border-radius:20px;background:rgba(255,255,255,.88);-webkit-backdrop-filter:blur(24px) saturate(160%);backdrop-filter:blur(24px) saturate(160%);box-shadow:0 24px 50px -20px rgba(13,46,99,.35),inset 0 0 0 1px rgba(13,46,99,.08);text-align:left;animation:zqSg .25s cubic-bezier(.2,.8,.2,1)}
@keyframes zqSg{from{opacity:0;transform:translateY(-6px)}}
.zq-sug p{font:600 .82rem var(--display);color:#6B7A94;padding:6px 10px}
.zq-sug button{display:grid;grid-template-columns:40px 1fr;grid-template-rows:auto auto;column-gap:12px;width:100%;align-items:center;border:0;background:none;text-align:left;padding:8px 10px;border-radius:12px;cursor:pointer;font:700 1rem var(--display);color:#0D2E63}
.zq-sug button img{grid-row:1/3;width:40px;height:40px;object-fit:contain}
.zq-sug button small{font:400 .85rem var(--body);color:#6B7A94}
.zq-sug button:hover{background:#EEF4FC}
.zq-pop button{border-radius:10px!important}
.zq-g .mk.in{animation:mkIn .5s cubic-bezier(.2,.8,.2,1) both}
@keyframes mkIn{from{opacity:0;transform:translateY(18px) scale(.98)}}
/* rails: header row, actions on the right, no pills */
.mr{display:block!important}
.mr-l{display:grid;grid-template-columns:minmax(0,1fr) auto auto;grid-template-areas:"t b a" "p b a";column-gap:14px;align-items:end;margin-bottom:28px}
.mr-l h2,.mr-l h3{grid-area:t}.mr-l p{grid-area:p;margin-top:8px!important;max-width:40em}
.mr-btn{grid-area:b;margin:0!important;border-radius:12px!important;padding:13px 20px!important}
.mr-ar{grid-area:a;margin:0!important}
.mr-ar button{border-radius:12px!important;width:46px!important;height:46px!important}
.mr-r{margin-right:0!important}
@media (max-width:900px){.mr-l{grid-template-columns:1fr;grid-template-areas:"t" "p" "b"}.mr-btn{justify-self:start;margin-top:16px!important}}
/* landscape cards; the open course is wider */
.mk{flex:0 0 380px!important;border-radius:18px!important}
.mk-i{aspect-ratio:16/9!important}
.mk-k{border-radius:6px!important}
.mk-b{padding:14px 16px 16px!important}
.mk-b b{font-size:1.08rem!important}
.mk-d{-webkit-line-clamp:1!important}
.mk-f{padding-top:10px!important}
.mk-a{margin-top:8px!important}
.mk.on{flex-basis:700px!important;flex-direction:row!important}
.mk.on{align-items:stretch;height:260px}.mk.on .mk-i{width:60%;flex:none;aspect-ratio:auto!important;height:100%!important}
.mk.on .mk-b{padding:22px!important;justify-content:center}
.mk.on .mk-b b{font-size:1.5rem!important}
.mk.on .mk-d{-webkit-line-clamp:2!important;font-size:.95rem}.mk.on .mk-f{margin-top:12px!important}
.mk.on .mk-a{border-radius:10px!important}
.ctg .mk.on,.zq-res .mk.on{grid-column:span 2}
@media (max-width:900px){.mk{flex-basis:82%!important}.mk.on{flex-direction:column!important;flex-basis:86%!important;height:auto}.mk.on .mk-i{width:100%;aspect-ratio:16/9!important}.ctg .mk.on,.zq-res .mk.on{grid-column:auto}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v48.html','w').write(s)
print('v48 ok')
