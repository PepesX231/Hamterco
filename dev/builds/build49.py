import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build48.py').read())
# login: glowing glass button, no hamster
rep('<span class="lg-e" aria-hidden="true"><img src="img/ham-grey.webp" alt=""></span>เข้าสู่ระบบ','<span class="lg-t">เข้าสู่ระบบ</span>')
# hero: clean, no surrounding decoration
s=re.sub(r'<div class="zq-ob" aria-hidden="true">.*?</div>','',s,count=1,flags=re.S)
# headline in a design-tool selection box with VFX
rep('<h1 class="zq-h"><span id="zqType">ยื่นพอร์ตเข้ามหาลัย</span><i class="zq-cur" aria-hidden="true"></i></h1>',
    '<h1 class="zq-h"><span class="zq-box"><span id="zqType">ยื่นพอร์ตเข้ามหาลัย</span><i class="zq-cur" aria-hidden="true"></i><i class="zbh h1" aria-hidden="true"></i><i class="zbh h2" aria-hidden="true"></i><i class="zbh h3" aria-hidden="true"></i><i class="zbh h4" aria-hidden="true"></i><span class="zq-warn" aria-hidden="true"><b>!</b>เปลี่ยนฟอนต์</span><span class="zq-gl" aria-hidden="true"><i></i><i></i><i></i></span></span></h1>')
s=s.replace("background:url(img/ham-peek2.webp) 0 0/400% 100% no-repeat","background:url(img/ham-peek3.webp) 0 0/400% 100% no-repeat")
s=s.replace("aspect-ratio:180/161;","aspect-ratio:180/144;")
# font-switch triggers the glitch moment
rep("if(t.length<=1&&last.length>1){k=(k+1)%S.length;h.dataset.f=S[k]}","if(t.length<=1&&last.length>1){k=(k+1)%S.length;h.dataset.f=S[k];h.classList.remove('sw');void h.offsetWidth;h.classList.add('sw')}")
JS=r'''
  /* login button: light follows the cursor, burst on press */
  (function(){var b=$('.login');if(!b)return;b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.setProperty('--mx',(e.clientX-r.left)+'px');b.style.setProperty('--my',(e.clientY-r.top)+'px')});
    b.addEventListener('pointerdown',function(e){var r=b.getBoundingClientRect(),i=document.createElement('i');i.className='lg-burst';i.style.left=(e.clientX-r.left)+'px';i.style.top=(e.clientY-r.top)+'px';b.appendChild(i);setTimeout(function(){i.remove()},700)})})();
  /* rails: arrows at the screen edges, centred on the cards */
  (function(){document.querySelectorAll('.mr').forEach(function(m){var r=m.querySelector('.mr-r'),ar=m.querySelector('.mr-ar');if(!r||!ar)return;var w=document.createElement('div');w.className='mr-rw';r.parentNode.insertBefore(w,r);w.appendChild(r);w.appendChild(ar);
})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v49 ===== */
/* login: dark glass with glow */
.login{position:relative;overflow:visible;isolation:isolate;padding:9px 20px!important;border:0!important;border-radius:999px!important;color:#fff!important;background:radial-gradient(120px circle at var(--mx,50%) var(--my,50%),rgba(130,150,255,.35),transparent 60%),linear-gradient(180deg,#1B2350,#0A0F2C)!important;
  box-shadow:inset 0 0 0 1px rgba(150,170,255,.55),inset 0 1px 0 rgba(255,255,255,.25),0 6px 18px -6px rgba(60,80,220,.6)!important;transition:transform .2s,box-shadow .3s}
.login::before{content:"";position:absolute;inset:0;border-radius:inherit;z-index:-1;background:radial-gradient(1px 1px at 20% 40%,#fff,transparent),radial-gradient(1px 1px at 70% 60%,#cfd6ff,transparent),radial-gradient(1px 1px at 45% 75%,#fff,transparent),radial-gradient(1px 1px at 85% 30%,#cfd6ff,transparent);opacity:.7;animation:lgTw 2.4s ease-in-out infinite alternate}
@keyframes lgTw{to{opacity:.2;transform:translateX(3px)}}
.login::after{content:"";position:absolute;left:12%;right:12%;bottom:-10px;height:14px;border-radius:50%;z-index:-2;background:#5B6CFF;filter:blur(10px);opacity:.55;transition:opacity .3s,transform .3s}
.login:hover{transform:translateY(-1px);box-shadow:inset 0 0 0 1px rgba(170,190,255,.85),inset 0 1px 0 rgba(255,255,255,.35),0 10px 26px -6px rgba(80,100,255,.8)!important}
.login:hover::after{opacity:1;transform:scaleX(1.15)}
.login:active{transform:scale(.96)}
.lg-t{position:relative;font-weight:700}
.lg-burst{position:absolute;width:10px;height:10px;margin:-5px 0 0 -5px;border-radius:50%;pointer-events:none;box-shadow:0 0 0 0 rgba(150,170,255,.8);animation:lgB .7s ease-out forwards}
@keyframes lgB{to{box-shadow:0 0 0 46px rgba(150,170,255,0);opacity:0}}
.login .peekw,.lg-e{display:none!important}
/* hero headline VFX */
.zq-box{position:relative;display:inline-block;padding:6px 22px 10px;margin-top:10px;outline:1.5px solid rgba(28,116,217,.55);outline-offset:0}
.zq-box .zbh{position:absolute;width:10px;height:10px;background:#fff;border:1.5px solid #1C74D9;border-radius:2px}
.zq-box .h1{left:-5px;top:-5px}.zq-box .h2{right:-5px;top:-5px}.zq-box .h3{left:-5px;bottom:-5px}.zq-box .h4{right:-5px;bottom:-5px}
.zq-warn{position:absolute;left:-6px;top:-38px;display:flex;align-items:center;gap:6px;padding:4px 10px 4px 6px;border-radius:6px;background:linear-gradient(90deg,#FF3E7F,#C13BFF);color:#fff;font:700 .78rem var(--display);white-space:nowrap;opacity:0;transform:translateY(6px) scale(.9);pointer-events:none}
.zq-warn b{display:grid;place-items:center;width:16px;height:16px;border-radius:3px;background:#fff;color:#E5306E;font-size:.72rem}
.zq-gl{position:absolute;right:-14px;top:-24px;width:120px;height:22px;opacity:0;pointer-events:none}
.zq-gl i{position:absolute;left:0;right:0;height:7px}
.zq-gl i:nth-child(1){top:0;background:linear-gradient(90deg,#2BD9FE 0 18%,#FF3E7F 18% 34%,#FFE14A 34% 52%,#6A5BFF 52% 70%,#fff 70% 82%,#25D366 82%)}
.zq-gl i:nth-child(2){top:8px;left:18px;background:linear-gradient(90deg,#6A5BFF,#2B3CFF);box-shadow:inset 0 0 0 1px #fff}
.zq-gl i:nth-child(3){top:15px;left:-8px;right:30px;background:repeating-linear-gradient(90deg,#fff 0 6px,transparent 6px 10px)}
.zq-h.sw .zq-warn{animation:zqWarn 1.6s cubic-bezier(.3,1.6,.5,1)}
@keyframes zqWarn{0%{opacity:0;transform:translateY(6px) scale(.8)}12%{opacity:1;transform:none}80%{opacity:1;transform:none}100%{opacity:0;transform:translateY(-4px)}}
.zq-h.sw .zq-gl{animation:zqGlx .5s steps(5)}
@keyframes zqGlx{0%{opacity:1;transform:translateX(0)}20%{transform:translateX(-14px) scaleX(1.2)}40%{opacity:0}60%{opacity:1;transform:translateX(8px)}80%{transform:translateX(-4px) scaleX(.8)}100%{opacity:0}}
.zq-h.sw #zqType{animation:zqJit .35s steps(3)}
@keyframes zqJit{33%{transform:translate(2px,-1px)}66%{transform:translate(-2px,1px)}}
@media (max-width:700px){.zq-box{padding:4px 12px 8px}.zq-gl{display:none}}
@media (prefers-reduced-motion:reduce){.zq-h.sw .zq-warn,.zq-h.sw .zq-gl,.zq-h.sw #zqType{animation:none}}
/* doodle hamster: a little bigger */
.zq-sw .zq-ham{width:96px!important}.zq-sw .zq-ham.up{transform:translateY(0)!important}.zq-sw:hover .zq-ham,.zq-sw .zq-ham.watch{transform:translateY(-22px)!important}@media(max-width:700px){.zq-sw .zq-ham,.zq-sw .zq-ham.up,.zq-sw:hover .zq-ham{transform:translateY(14px)!important}}.zq-sw .zq-spr{width:96px!important}
/* rails: link without a box; arrows at the screen edges */
.mr-l{grid-template-columns:minmax(0,1fr) auto!important;grid-template-areas:"t b" "p b"!important}
.mr-btn{background:none!important;color:#1C74D9!important;padding:6px 0!important;border-radius:0!important;font:700 1.05rem var(--display)!important;display:inline-flex!important;align-items:center;gap:8px;position:relative}
.mr-btn::after{content:"";width:9px;height:9px;border-right:2.5px solid currentColor;border-top:2.5px solid currentColor;transform:rotate(45deg);transition:transform .25s}
.mr-btn::before{content:"";position:absolute;left:0;right:22px;bottom:0;height:2px;background:currentColor;transform:scaleX(0);transform-origin:left;transition:transform .3s}
.mr-btn:hover::before{transform:scaleX(1)}.mr-btn:hover::after{transform:translateX(4px) rotate(45deg)}
.mr-btn:hover{background:none!important;color:#0D2E63!important}
.mr-rw{position:relative}
.mr-rw .mr-ar{position:absolute;inset:0;pointer-events:none;display:block!important}
.mr-rw .mr-ar button{position:absolute;top:50%;margin-top:-28px;width:56px!important;height:56px!important;border:0!important;background:none!important;box-shadow:none!important;-webkit-backdrop-filter:none;backdrop-filter:none;color:#0D2E63!important;pointer-events:auto;filter:drop-shadow(0 2px 6px rgba(255,255,255,.9));transition:transform .2s,opacity .2s;opacity:.65}
.mr-rw .mr-ar button:hover{background:none!important;color:#1C74D9!important;opacity:1;transform:scale(1.15)}
.mr-rw .mr-p{left:calc((100% - 100vw)/2 + 18px)}.mr-rw .mr-n{right:calc((100% - 100vw)/2 + 26px)}
.mr-rw .mr-ar svg{width:36px!important;height:36px!important}
@media (max-width:900px){.mr-rw .mr-ar{display:none!important}}
/* equal-height cards */
.mk{height:300px}
.mk:not(.on) .mk-i{aspect-ratio:auto!important;height:158px;flex:none}.mk.on .mk-i{width:55%!important}
.mk.on{height:300px}
@media (max-width:900px){.mk.on .mk-i{width:100%!important;height:auto!important;aspect-ratio:16/9!important}.mk,.mk.on{height:auto!important}.mk:not(.on) .mk-i{height:auto;aspect-ratio:16/9!important}}
/* courses page: the hamster walks on the top edge of the next box */
[data-view="courses"] .wkz{height:96px;margin:24px auto 0}
[data-view="courses"] .wkz{position:relative;z-index:2}[data-view="courses"] .wkz .wk{bottom:-6px!important}[data-view="courses"] .wkz .wk-sh{display:none}
[data-view="courses"] .ct-fit{margin-top:0!important}
[data-view="courses"] .ct-fit .fit{margin-top:0!important;padding-top:0!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v49.html','w').write(s)
print('v49 ok')
