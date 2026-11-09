import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build49.py').read())
# ---------- hamster sprite (based on the doodle references)
s=s.replace("background:url(img/ham-peek3.webp) 0 0/400% 100% no-repeat","background:url(img/ham-peek5.webp) 0 0/400% 100% no-repeat")
s=s.replace("aspect-ratio:180/144;","aspect-ratio:180/149;")
# ---------- headline: back to the plain typing line, many styles
i=s.index('<h1 class="zq-h">');j=s.index('</h1>',i)+5
s=s[:i]+'<h1 class="zq-h" title="กดเพื่อเปลี่ยนสไตล์"><span id="zqType">ยื่นพอร์ตเข้ามหาลัย</span><i class="zq-cur" aria-hidden="true"></i></h1>'+s[j:]
s=s.replace('family=Chonburi&display=swap','family=Chonburi&family=Mali:wght@700&family=Sarabun:wght@800&display=swap',1)
old=s[s.index('/* headline: every phrase gets its own type style */'):s.index('  /* scroll cue: nudges if nobody scrolls */')]
s=s.replace(old,r'''/* headline: every phrase gets its own type style; click to switch */
  (function(){var el=$('#zqType');if(!el)return;var h=el.closest('.zq-h'),S=['kanit','persona','got','ragnarok','elden','pencil','pencil2b','pen','cartoon','doraemon','robot','ai','glitch','hacker','curtain','computer','boom','fan'],k=0,last=el.textContent;h.dataset.f=S[0];
    function next(){k=(k+1)%S.length;h.dataset.f=S[k];h.classList.remove('sw');void h.offsetWidth;h.classList.add('sw')}
    new MutationObserver(function(){var t=el.textContent;if(t.length<=1&&last.length>1)next();last=t}).observe(el,{childList:true,characterData:true,subtree:true});
    h.addEventListener('click',next)})();
''')
# ---------- cards: equal Apple-style cards
i=s.index('function cardH(x){');j=s.index('    function render(',i)
s=s[:i]+r'''function cardH(x){var cta=x.k==='course'?(x.open?'สมัครเรียน':'รับแจ้งเตือน'):(x.open?'ดูรายละเอียด':'รับแจ้งเตือน');
      return '<a class="ak'+(x.open?' on':'')+'" href="'+x.url+'" target="_blank" rel="noopener"><img class="ak-i" src="'+x.img+'" alt="" loading="lazy"><span class="ak-k">'+(x.k==='course'?'Hamster Hub คอร์สเรียน':'Hamster Hub '+x.k)+'</span><span class="ak-b"><b>'+x.t+'</b><span class="ak-d">'+x.d+'</span><span class="ak-s">'+(x.open?'<i></i>':'')+x.st+(x.pr?' <em>'+x.pr+'</em>':'')+'</span></span><span class="ak-a">'+cta+'</span></a>'}
'''+s[j:]
s=s.replace("$$('#zqG .mk')","$$('#zqG .ak')").replace("var c=r.querySelector('.mk');","var c=r.querySelector('.ak');")
# ---------- login: neon rim
JS=r'''
  /* rails: page dots */
  (function(){document.querySelectorAll('.mr-r').forEach(function(r){var d=document.createElement('div');d.className='ak-dots';(r.closest('.mr-rw')||r).after(d);
      function build(){var n=r.querySelectorAll('.ak').length;if(d.childElementCount!==n){d.innerHTML='';for(var i=0;i<n;i++){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','การ์ดที่ '+(i+1));(function(i){b.addEventListener('click',function(){var c=r.querySelectorAll('.ak')[i];r.scrollTo({left:c.offsetLeft-r.offsetLeft,behavior:'smooth'})})})(i);d.appendChild(b)}}upd()}
      function upd(){var cs=r.querySelectorAll('.ak'),a=0,best=1e9;cs.forEach(function(c,i){var x=Math.abs(c.offsetLeft-r.offsetLeft-r.scrollLeft);if(x<best){best=x;a=i}});[].forEach.call(d.children,function(b,i){b.classList.toggle('on',i===a)})}
      r.addEventListener('scroll',function(){requestAnimationFrame(upd)},{passive:true});new MutationObserver(build).observe(r,{childList:true});build()})})();
  /* search focus: the sky glow pulls in around the bar */
  (function(){var sw=$('.zq-sw'),inp=$('#zqIn');if(!sw)return;inp.addEventListener('focus',function(){sw.classList.remove('lit');void sw.offsetWidth;sw.classList.add('lit')});inp.addEventListener('blur',function(){sw.classList.remove('lit')})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v50 ===== */
/* hamster: only the eyes show until you point at the search */
.zq-sw .zq-ham,.zq-sw .zq-ham.up{bottom:100%!important;width:76px!important;right:128px!important;transform:translateY(31px)!important;transition:transform .5s cubic-bezier(.3,1.6,.5,1)!important}
.zq-sw .zq-spr{width:76px!important}
.zq-sw:hover .zq-ham.up,.zq-sw .zq-ham.up.watch,.zq-sw:focus-within .zq-ham.up{transform:translateY(6px)!important}
.zq-sw .zq-ham.dive{animation:zqDv3 1s cubic-bezier(.5,0,.3,1)!important}
@keyframes zqDv3{0%{transform:translateY(6px)}25%{transform:translateY(-10px)}55%,80%{transform:translateY(70px)}100%{transform:translateY(34px)}}
@media(max-width:700px){.zq-sw .zq-ham{right:84px!important;width:60px!important}.zq-sw .zq-spr{width:60px!important}.zq-sw .zq-ham,.zq-sw .zq-ham.up{transform:translateY(27px)!important}}
/* headline styles */
.zq-h{cursor:pointer;user-select:none;min-height:1.35em}
.zq-h #zqType{display:inline-block;padding:0 .08em;transition:none}
.zq-h.sw #zqType{animation:zqPop .45s cubic-bezier(.3,1.6,.5,1)}
@keyframes zqPop{0%{transform:scale(.85);filter:blur(4px);opacity:.3}100%{transform:none;filter:none;opacity:1}}
.zq-h[data-f="kanit"] #zqType{font-family:'Kanit';font-weight:900;color:#0D2E63}
.zq-h[data-f="persona"] #zqType{font-family:'Kanit';font-weight:900;color:#fff;background:#111;padding:0 .3em .05em;transform:skew(-8deg) rotate(-2deg);box-shadow:.14em .14em 0 #E5222A}
.zq-h[data-f="got"] #zqType{font-family:'Srisakdi',serif;font-weight:700;letter-spacing:.08em;background:linear-gradient(180deg,#F4F6F8 0%,#9AA3AD 45%,#5B636C 55%,#DDE2E7 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 2px 0 #2B3036) drop-shadow(0 6px 10px rgba(0,0,0,.35))}
.zq-h[data-f="ragnarok"] #zqType{font-family:'Chonburi',serif;color:#F7D36A;-webkit-text-stroke:2px #3A1E06;paint-order:stroke fill;text-shadow:0 0 18px rgba(255,190,60,.7),3px 3px 0 #7A2B00;transform:skew(-4deg)}
.zq-h[data-f="elden"] #zqType{font-family:'Srisakdi',serif;font-weight:700;letter-spacing:.03em;background:linear-gradient(180deg,#F6E3A6,#B88A2E 60%,#7A5A18);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 10px rgba(230,190,90,.55))}
.zq-h[data-f="pencil"] #zqType{font-family:'Itim';font-weight:400;color:#4A4F57;transform:rotate(-1.5deg);text-shadow:1px 1px 0 rgba(74,79,87,.35),-1px 0 0 rgba(74,79,87,.2)}
.zq-h[data-f="pencil2b"] #zqType{font-family:'Mali';font-weight:700;background:repeating-linear-gradient(115deg,#2E3135 0 2px,#5A5F66 2px 3px,#2E3135 3px 5px);-webkit-background-clip:text;background-clip:text;color:transparent;transform:rotate(1deg)}
.zq-h[data-f="pen"] #zqType{font-family:'Charmonman',cursive;font-weight:700;color:#1E3FB8}
.zq-h[data-f="cartoon"] #zqType{font-family:'Pattaya';color:#FFC531;-webkit-text-stroke:6px #0D2E63;paint-order:stroke fill;transform:rotate(-2deg)}
.zq-h[data-f="doraemon"] #zqType{font-family:'Mitr';font-weight:700;color:#14A3EF;-webkit-text-stroke:3px #111;paint-order:stroke fill;text-shadow:4px 4px 0 #fff,6px 6px 0 #E8302A}
.zq-h[data-f="robot"] #zqType{font-family:'Chakra Petch';font-weight:700;letter-spacing:.06em;background:linear-gradient(180deg,#E9EEF5,#8B97A8 50%,#3E4A5C 52%,#B9C3D0);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 1px #1C74D9) drop-shadow(0 4px 8px rgba(28,116,217,.35))}
.zq-h[data-f="ai"] #zqType{font-family:'Kanit';font-weight:800;background:linear-gradient(90deg,#4F7BFF,#B45CFF,#FF6FB1,#4F7BFF);background-size:300% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:zqAi 3s linear infinite}
@keyframes zqAi{to{background-position:300% 0}}
.zq-h[data-f="glitch"] #zqType{font-family:'Chakra Petch';font-weight:700;color:#0D2E63;animation:zqGl .5s steps(2) infinite}
@keyframes zqGl{0%{text-shadow:3px 0 #FF2E63,-3px 0 #08D9D6}50%{text-shadow:-2px 1px #FF2E63,2px -1px #08D9D6}100%{text-shadow:1px -1px #FF2E63,-1px 1px #08D9D6}}
.zq-h[data-f="hacker"] #zqType{font-family:'Sarabun';font-weight:800;color:#3BFF7A;background:#07130B repeating-linear-gradient(0deg,rgba(59,255,122,.08) 0 2px,transparent 2px 4px);padding:0 .3em;border-radius:6px;text-shadow:0 0 8px rgba(59,255,122,.8)}
.zq-h[data-f="curtain"] #zqType{font-family:'Kanit';font-weight:900;color:#7A1020;-webkit-mask:linear-gradient(90deg,#000 50%,transparent 50%) 0 0/200% 100%;mask:linear-gradient(90deg,#000 50%,transparent 50%) 0 0/200% 100%;animation:zqCur 1.2s cubic-bezier(.7,0,.2,1) both}
@keyframes zqCur{from{-webkit-mask-position:100% 0;mask-position:100% 0}to{-webkit-mask-position:0 0;mask-position:0 0}}
.zq-h[data-f="computer"] #zqType{font-family:'Chakra Petch';font-weight:700;color:#1C74D9;letter-spacing:.04em;text-shadow:2px 0 0 #0D2E63,0 2px 0 #0D2E63,2px 2px 0 #0D2E63,4px 4px 0 rgba(13,46,99,.25)}
.zq-h[data-f="boom"] #zqType{font-family:'Pattaya';color:#fff;-webkit-text-stroke:5px #B3140C;paint-order:stroke fill;padding:.1em .5em;background:radial-gradient(circle,#FFE14A 0 40%,#FF8A00 60%,transparent 62%);animation:zqBm .5s cubic-bezier(.3,1.8,.5,1)}
@keyframes zqBm{0%{transform:scale(.3) rotate(-10deg)}60%{transform:scale(1.15) rotate(4deg)}100%{transform:none}}
.zq-h[data-f="fan"] #zqType{font-family:'Kanit';font-weight:900;color:#1C74D9;animation:zqFan 2.2s cubic-bezier(.5,0,.5,1) infinite}
@keyframes zqFan{0%,60%{transform:rotateX(0)}80%{transform:rotateX(360deg)}100%{transform:rotateX(360deg)}}
/* login: black pill, neon rim (reference 4) */
@property --lga{syntax:"<angle>";inherits:false;initial-value:0deg}
.login{color:#F3EEFF!important;background:#07040F!important;padding:9px 22px!important;box-shadow:inset 0 0 0 1.5px rgba(214,190,255,.95),0 0 10px rgba(160,90,255,.75),0 0 26px rgba(130,60,255,.45)!important}
.login::before{inset:-2px!important;border-radius:999px;z-index:0!important;opacity:0!important;padding:2px;background:conic-gradient(from var(--lga),transparent 0 70%,#fff 80%,#C9A6FF 85%,transparent 95%)!important;-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask:linear-gradient(#000 0 0) content-box exclude,linear-gradient(#000 0 0);animation:lgSpin 1.6s linear infinite!important;transition:opacity .3s}
@keyframes lgSpin{to{--lga:360deg}}
.login::after{background:#8A4BFF!important;opacity:.45!important}
.login:hover{box-shadow:inset 0 0 0 1.5px #fff,0 0 14px rgba(180,110,255,.95),0 0 40px rgba(140,70,255,.6)!important}
.login:hover::before{opacity:1!important}
.login:hover::after{opacity:.9!important}
/* search: scrollable suggestions; glow pulls in on focus (reference 7) */
.zq-sug{max-height:min(300px,42vh);overflow-y:auto;overscroll-behavior:contain;scrollbar-width:thin}
.zq-sw:focus-within~.zq-more,.zq:has(.zq-sug:not([hidden])) .zq-more{opacity:0;pointer-events:none}
.zq-sw::before{content:"";position:absolute;left:-14px;right:-14px;top:-14px;height:calc(100% - 0px);max-height:92px;border-radius:999px;z-index:-1;pointer-events:none;opacity:0;transform:scale(2.4,4);
  background:radial-gradient(50% 120% at 0% 50%,rgba(255,122,69,.9),transparent 70%),radial-gradient(50% 120% at 100% 50%,rgba(61,123,255,.95),transparent 70%),radial-gradient(60% 100% at 50% 50%,rgba(150,180,255,.6),transparent 70%);filter:blur(16px);transition:opacity .5s,transform .7s cubic-bezier(.2,.8,.2,1)}
.zq-sw.lit::before{opacity:.9;transform:scale(1)}
.zq-sw .zq-s{transition:box-shadow .4s,transform .25s}
.zq-sw.lit .zq-s{box-shadow:0 0 0 1.5px rgba(255,255,255,.9),0 0 0 3px rgba(120,140,255,.35),0 20px 40px -16px rgba(13,46,99,.35)!important}
.zq{transition:background-color .5s}
/* equal cards (Apple-style) */
.ak{position:relative;flex:0 0 min(560px,82vw);height:330px;border-radius:22px;overflow:hidden;display:block;color:#fff;text-decoration:none;scroll-snap-align:start;background:#0D2E63;box-shadow:0 18px 40px -26px rgba(13,46,99,.6);transition:transform .35s cubic-bezier(.2,.8,.2,1)}
.ak:hover{transform:translateY(-4px)}
.ak-i{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.ak:hover .ak-i{transform:scale(1.04)}
.ak-i[src*="afo-logo"]{object-fit:contain;padding:30px 30px 120px;background:#1C74D9}
.ak::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.38) 0%,transparent 24%,transparent 42%,rgba(5,14,32,.82) 70%,rgba(5,14,32,.95) 100%);pointer-events:none}
.ak-k{position:absolute;right:20px;top:16px;z-index:1;font:700 .95rem var(--display);text-shadow:0 1px 8px rgba(0,0,0,.4)}
.ak-b{position:absolute;left:22px;right:170px;bottom:20px;z-index:1;display:flex;flex-direction:column;gap:2px}
.ak-b b{font:800 1.3rem/1.25 var(--display)}
.ak-d{font-size:.9rem;color:rgba(255,255,255,.85);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ak-s{font-size:.85rem;color:rgba(255,255,255,.75);margin-top:4px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.ak-s i{width:8px;height:8px;border-radius:50%;background:#3DDC84}
.ak-s em{font-style:normal;font:800 1.05rem var(--display);color:#FFD54A;margin-left:4px}
.ak-a{position:absolute;right:18px;bottom:20px;z-index:1;padding:11px 20px;border-radius:999px;background:#fff;color:#111;font:600 .95rem var(--display);transition:transform .2s,background .2s}
.ak.on .ak-a{background:#FFC531;color:#2A1E00}
.ak:hover .ak-a{transform:scale(1.05)}
.mr-r{gap:18px!important}
.ak-dots{display:flex;justify-content:center;gap:10px;margin-top:22px}
.ak-dots button{width:8px;height:8px;border-radius:999px;border:0;padding:0;background:#C3CBD8;cursor:pointer;transition:width .35s,background .3s}
.ak-dots button.on{width:36px;background:#0D2E63}
.zq-res .zq-g,.ctg{grid-template-columns:repeat(auto-fill,minmax(440px,1fr))!important}
.zq-res .ak,.ctg .ak{flex:none;width:auto}
@media (max-width:700px){.ak{height:300px;flex-basis:86vw}.ak-b{right:18px;bottom:72px}.ak-a{left:22px;right:auto;bottom:18px}.zq-res .zq-g,.ctg{display:flex!important;overflow-x:auto;scroll-snap-type:x mandatory}.zq-res .ak,.ctg .ak{flex:0 0 86vw}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v50.html','w').write(s)
print('v50 ok')
