SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build44.py').read())
# fonts for the typing headline
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kanit:wght@800&family=Mitr:wght@700&family=Chakra+Petch:wght@700&family=Bai+Jamjuree:wght@700&family=Sriracha&display=swap">'
rep('<section class="zq" aria-label="ค้นหาคอร์สและกิจกรรม">',FONTS+'<section class="zq" aria-label="ค้นหาคอร์สและกิจกรรม">')
# remove the gaming hamster, add a floor of the kids' games
rep('<img class="zq-hm" src="img/n-gamer.webp" alt="">','')
WALL=['stressstrike','phi-krahang','eugation-strike','slash-speed','escape-rolling','hot-hot-hot','midnight-at-roadside','apocalypis-building','beyond-the-board','micro-immersive-sim']
floor='<div class="zq-fl" aria-hidden="true"><div class="zq-fl-in">'+''.join('<img src="img/work-%s.webp" alt="">'%w for w in WALL*2)+'</div></div>'
rep('<div class="zq-dc" aria-hidden="true">',floor+'<div class="zq-dc" aria-hidden="true">')
# peeking hamster on the search bar
HAM='''<span class="zq-ham" id="zqHam" aria-hidden="true"><span class="zq-ham-in"><svg viewBox="0 0 140 110">
  <ellipse cx="34" cy="30" rx="16" ry="15" fill="#F2A13A"/><ellipse cx="34" cy="31" rx="9" ry="8" fill="#FFC9B0"/>
  <ellipse cx="106" cy="30" rx="16" ry="15" fill="#F2A13A"/><ellipse cx="106" cy="31" rx="9" ry="8" fill="#FFC9B0"/>
  <ellipse cx="70" cy="70" rx="56" ry="48" fill="#F2A13A"/>
  <path d="M28 82c6-22 24-30 42-30s36 8 42 30c-8 16-24 24-42 24s-34-8-42-24z" fill="#FFF3E2"/>
  <g class="zq-eyes"><g class="zq-pu"><ellipse cx="50" cy="66" rx="7.5" ry="9" fill="#2B1A12"/><circle cx="52.5" cy="62.5" r="2.6" fill="#fff"/><ellipse cx="90" cy="66" rx="7.5" ry="9" fill="#2B1A12"/><circle cx="92.5" cy="62.5" r="2.6" fill="#fff"/></g></g>
  <ellipse cx="38" cy="82" rx="8" ry="5" fill="#FF9DA7" opacity=".6"/><ellipse cx="102" cy="82" rx="8" ry="5" fill="#FF9DA7" opacity=".6"/>
  <path d="M66 78q4 3 8 0" stroke="#2B1A12" stroke-width="2.4" fill="none" stroke-linecap="round"/><ellipse cx="70" cy="75" rx="3.4" ry="2.4" fill="#E2747F"/>
</svg></span><i class="zq-paw l"></i><i class="zq-paw r"></i></span>'''
rep('<form class="zq-s" id="zqForm" role="search">','<form class="zq-s" id="zqForm" role="search">'+HAM)
# courses page: same cards, every course the same size
i=s.index('<div class="ctb">');j=s.index('<section class="ct-list">');k=s.index('</section>',j)+10
s=s[:i]+'<div class="zq-g ctg" id="zqC2"></div>'+s[k:]
rep("    $('#zqC').innerHTML=IT.filter(function(x){return x.k==='course'}).map(cardH).join('');","    $('#zqC').innerHTML=IT.filter(function(x){return x.k==='course'}).map(cardH).join('');if($('#zqC2'))$('#zqC2').innerHTML=$('#zqC').innerHTML;")
rep("<p>คอร์สที่เปิดรับตอนนี้ จบแล้วน้องได้ผลงานจริงที่เอาไปใช้ยื่นมหาวิทยาลัยได้</p>","<p>ทุกคอร์สจบแล้วน้องได้ผลงานจริงของตัวเอง คอร์สที่ยังไม่เปิดรอบ กดรับแจ้งเตือนได้</p>")
JS=r'''
  /* search hamster: peeks, looks around, blinks, watches the search, dives in on submit */
  (function(){var h=$('#zqHam'),f=$('#zqForm'),inp=$('#zqIn');if(!h)return;setTimeout(function(){h.classList.add('up')},700);
    var pu=h.querySelector('.zq-pu');
    function look(x,y){pu.style.transform='translate('+x+'px,'+y+'px)'}
    f.addEventListener('pointerenter',function(){h.classList.add('watch');look(-4,5)});
    f.addEventListener('pointerleave',function(){if(document.activeElement!==inp){h.classList.remove('watch');pu.style.transform=''}});
    inp.addEventListener('focus',function(){h.classList.add('watch');look(-4,5)});
    inp.addEventListener('blur',function(){h.classList.remove('watch');pu.style.transform=''});
    inp.addEventListener('input',function(){var t=Math.min(1,inp.value.length/26);look(-6+t*12,5);h.classList.remove('nod');void h.offsetWidth;h.classList.add('nod')});
    f.addEventListener('submit',function(){h.classList.remove('dive');void h.offsetWidth;h.classList.add('dive');setTimeout(function(){h.classList.remove('dive')},1100)});
    document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('.zq-pop [data-q]')){h.classList.remove('dive');void h.offsetWidth;h.classList.add('dive');setTimeout(function(){h.classList.remove('dive')},1100)}})})();
  /* headline: each phrase in its own typeface */
  (function(){var el=$('#zqType');if(!el)return;var F=["'Kanit'","'Mitr'","'Chakra Petch'","'Bai Jamjuree'","'Sriracha'"],k=0,last=el.textContent;
    new MutationObserver(function(){var t=el.textContent;if(t.length<=1&&last.length>1){k=(k+1)%F.length;el.style.fontFamily=F[k]+',var(--display)'}last=t}).observe(el,{childList:true,characterData:true,subtree:true})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v45 ===== */
/* poster cards: the photo is the card, text sits on a dark fade so it always reads */
.zk{position:relative!important;display:block!important;aspect-ratio:4/5;border-radius:24px!important;overflow:hidden!important;color:#fff!important;background:#0D2E63!important;box-shadow:0 24px 40px -26px rgba(13,46,99,.7)!important;transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s!important}
.zk:hover{transform:translateY(-6px)!important;box-shadow:0 34px 50px -26px rgba(13,46,99,.75)!important}
.zk-i{position:absolute!important;inset:0;width:100%!important;height:100%!important;aspect-ratio:auto!important;border-radius:0!important;box-shadow:none!important;transform:none!important}
.zk-i img{width:100%;height:100%;object-fit:cover}
.zk:hover .zk-i img{transform:scale(1.06)}
.zk-b{position:absolute!important;left:0;right:0;bottom:0;padding:90px 18px 18px!important;background:linear-gradient(rgba(5,18,40,0),rgba(5,18,40,.9) 32%,rgba(5,18,40,.97));display:flex;flex-direction:column;gap:4px}
.zk-k,.zk-k.c{color:#fff!important;background:rgba(255,255,255,.18)!important;-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);box-shadow:inset 0 0 0 1px rgba(255,255,255,.28)}
.zk-b b{color:#fff;font-size:1.2rem!important}
.zk-d{color:rgba(255,255,255,.82)!important;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.zk-s{color:rgba(255,255,255,.7)!important;padding-top:6px!important}
.zk.on .zk-s{color:#7CE3A6!important}
.zk-s em{color:#fff!important}
.zk-a{color:#fff!important;align-self:flex-start;margin-top:10px;padding:8px 16px;border-radius:999px;background:rgba(255,255,255,.16);box-shadow:inset 0 0 0 1px rgba(255,255,255,.3);font-size:.88rem!important}
.zk.on .zk-a{background:#FFC531!important;color:#2A1E00!important;box-shadow:none}
.zk-i img[src*="afo-logo"]{object-fit:contain;padding:28px 28px 120px}
.ctg{margin-top:28px}
.zk-i img[src*="portex"]{height:56%;object-position:50% 50%}
@media (max-width:700px){
  .zq-g{display:flex!important;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:16px -16px 0;padding:4px 16px 16px;scrollbar-width:none}
  .zq-g::-webkit-scrollbar{display:none}
  .zk{flex:0 0 78%!important;scroll-snap-align:start;aspect-ratio:4/5!important;flex-direction:column!important}
  .zk-i{width:100%!important}.zk-b{padding:80px 16px 16px!important}.zk-d{display:-webkit-box!important}
  .zq-res .zq-g{flex-direction:row}
}
/* grand floor of the kids' games */
.zq-fl{position:absolute;left:-20%;right:-20%;bottom:0;height:34%;z-index:0;perspective:900px;pointer-events:none;
  -webkit-mask:linear-gradient(transparent,#000 70%);mask:linear-gradient(transparent,#000 70%)}
.zq-fl-in{position:absolute;left:0;bottom:-30%;width:200%;display:grid;grid-template-columns:repeat(10,1fr);gap:18px;transform-origin:50% 100%;transform:rotateX(58deg);animation:zqFl 60s linear infinite}
.zq-fl-in img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:14px;opacity:.85}
@keyframes zqFl{to{translate:-50% 0}}
.zq::after{content:"";position:absolute;inset:auto 0 0 0;height:40%;z-index:0;pointer-events:none;background:linear-gradient(rgba(228,237,250,0),rgba(228,237,250,.35))}
@media (prefers-reduced-motion:reduce){.zq-fl-in{animation:none}}
@media (max-width:700px){.zq-fl{height:40%}}
/* typing headline */
#zqType{transition:none}
.zq-h{min-height:1.3em}
/* the hamster */
.zq-s{position:relative}
.zq-ham{position:absolute;right:120px;bottom:calc(100% - 14px);width:108px;height:86px;overflow:hidden;pointer-events:none;z-index:-1}
.zq-ham-in{position:absolute;left:0;bottom:0;width:108px;transform:translateY(62%);transition:transform .6s cubic-bezier(.3,1.6,.5,1)}
.zq-ham.up .zq-ham-in{transform:translateY(16%)}
.zq-ham.watch .zq-ham-in{transform:translateY(4%)}
.zq-ham svg{display:block;width:100%!important;height:auto!important;color:inherit}
.zq-eyes{transform-origin:70px 66px;animation:zqBlink 4.2s infinite}
@keyframes zqBlink{0%,92%,100%{transform:scaleY(1)}94%,96%{transform:scaleY(.1)}}
.zq-pu{transition:transform .25s ease-out;animation:zqLook 6s ease-in-out infinite}
.zq-ham.watch .zq-pu{animation:none}
@keyframes zqLook{0%,20%{transform:translateX(0)}28%,42%{transform:translateX(-5px)}50%,64%{transform:translateX(5px)}72%,100%{transform:translateX(0)}}
.zq-ham.nod .zq-ham-in{animation:zqNod .3s ease-out}
@keyframes zqNod{50%{translate:0 3px}}
.zq-paw{position:absolute;bottom:2px;width:22px;height:14px;border-radius:50%;background:#FFF3E2;box-shadow:0 0 0 2px #F2A13A;opacity:0;transition:opacity .3s .3s}
.zq-paw.l{left:20px}.zq-paw.r{right:20px}
.zq-ham.up .zq-paw{opacity:1}
.zq-ham.dive .zq-ham-in{animation:zqDive 1.1s cubic-bezier(.5,0,.3,1)}
.zq-ham.dive .zq-paw{opacity:0;transition:none}
@keyframes zqDive{0%{transform:translateY(4%)}18%{transform:translateY(-8%) scale(1.05,.95)}45%{transform:translateY(110%) scale(.9,1.1)}70%{transform:translateY(110%)}100%{transform:translateY(16%)}}
@media (max-width:700px){.zq-ham{right:86px;width:84px;height:66px}.zq-ham-in{width:84px}}
@media (prefers-reduced-motion:reduce){.zq-eyes,.zq-pu{animation:none}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v45.html','w').write(s)
print('v45 ok')
