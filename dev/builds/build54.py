SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build53.py').read())
# login: text only, glass-light pill
i=s.index('<img class="lg-ic" src="img/ham-ico.webp" alt="">');s=s[:i]+s[i+len('<img class="lg-ic" src="img/ham-ico.webp" alt="">'):]
i=s.index('<svg class="lg-ar"');j=s.index('</svg>',i)+6;s=s[:i]+'<i class="lg-orb" aria-hidden="true"></i>'+s[j:]
# no auto scrolling on search
s=s.replace(";var r=$('#zqRes');if(r&&!r.hidden)r.scrollIntoView({behavior:'smooth',block:'start'})","")
s=s.replace("$('.zq').scrollIntoView({behavior:'smooth'})","")
# activity deck
rep('<h2 class="er-h">จบไปแล้วในปี 2569</h2>','<section class="dq" aria-label="ไทม์ไลน์กิจกรรม"><h2 class="dq-h">มีอะไรเกิดขึ้นบ้าง</h2><div class="dq-st" id="dqSt"></div><p class="dq-cap">กดการ์ดด้านหลังเพื่อดูงานนั้น</p></section>\n    <h2 class="er-h">จบไปแล้วในปี 2569</h2>')
JS=r'''
  /* search results open in a panel under the bar, no page jump */
  (function(){var sw=$('.zq-sw'),r=$('#zqRes');if(!sw||!r)return;sw.appendChild(r);
    var x=document.createElement('button');x.type='button';x.className='zq-x';x.setAttribute('aria-label','ปิดผลค้นหา');x.innerHTML='&times;';r.prepend(x);
    x.addEventListener('click',function(){r.hidden=true});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')r.hidden=true});
    document.addEventListener('pointerdown',function(e){if(!e.target.closest('.zq-sw')&&!e.target.closest('.zq-pop'))r.hidden=true})})();
  /* sky gathers into the bar as a soft orb (no hard edges) */
  (function(){var z=$('.zq'),sw=$('.zq-sw');if(!z||!sw)return;var o=document.createElement('i');o.className='zq-orb';o.setAttribute('aria-hidden','true');sw.prepend(o)})();
  /* login: the light follows the cursor */
  (function(){var b=$('.login');if(!b)return;b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.setProperty('--ox',((e.clientX-r.left)/r.width*100)+'%')});b.addEventListener('pointerleave',function(){b.style.removeProperty('--ox')})})();
  /* activity deck */
  (function(){var st=$('#dqSt');if(!st)return;var AI3={'All for One University รอบชิงชนะเลิศ':'k-afo','IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'},
      D={'ค่าย':'photo-camp','เวิร์กชอป':'photo-class','แข่งขัน':'k-gamejam','โชว์ผลงาน':'s-showcase1','โครงการ':'photo-group'};
    var L=ACT.slice(0,7).map(function(a){var p=a[0].split(' ');return {d:p[0],m:p[1]||'',t:a[1],x:a[2],k:a[3],up:!!a[4],img:'img/'+(AI3[a[1]]||D[a[3]])+'.webp'}});
    st.innerHTML=L.map(function(c,i){return '<button type="button" class="dq-c" data-i="'+i+'"><span class="dq-chip">'+(c.up?'<b>SOON</b>':'<b>'+c.m+'</b><small>'+c.d+'</small>')+'</span><img src="'+c.img+'" alt="" loading="lazy"><span class="dq-tx"><small>'+(c.up?'กำลังจะมา '+c.d+' '+c.m:c.k+' · '+c.d+' '+c.m)+'</small><b>'+c.t+'</b><span>'+c.x+'</span></span></button>'}).join('');
    var C=[].slice.call(st.children),ord=C.map(function(_,i){return i});
    function lay(){var w=st.clientWidth,base=Math.min(400,w*.6),step=Math.min(78,(w-base)/(ord.length-1));ord.forEach(function(ci,p){var c=C[ci];c.style.width=base+'px';c.style.transform='translateX('+(p*step)+'px) translateY('+(p*7)+'px) scale('+(1-p*.035)+')';c.style.zIndex=50-p;c.classList.toggle('on',p===0);c.tabIndex=0});
      st.style.setProperty('--sw',(base+step*(ord.length-1))+'px')}
    C.forEach(function(c,ci){c.addEventListener('click',function(){var p=ord.indexOf(ci);if(p===0)return;ord=ord.slice(p).concat(ord.slice(0,p));lay()})});
    new ResizeObserver(lay).observe(st);lay()})();
  /* tilt + light on cards across the site */
  (function(){if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
    document.addEventListener('pointermove',function(e){var c=e.target.closest&&e.target.closest('.qv-im,.zb-t,.zp-c,.dq-c.on');document.querySelectorAll('.tl-on').forEach(function(x){if(x!==c){x.classList.remove('tl-on');x.style.removeProperty('--rx');x.style.removeProperty('--ry')}});if(!c)return;
      var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.classList.add('tl-on');c.style.setProperty('--rx',(-y*7)+'deg');c.style.setProperty('--ry',(x*9)+'deg');c.style.setProperty('--lx',(x+.5)*100+'%');c.style.setProperty('--ly',(y+.5)*100+'%')},{passive:true})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v54 ===== */
/* login: dark glass pill lit from the right (reference) */
.login{gap:0!important;padding:8px 22px!important;color:#EAF4FF!important;letter-spacing:.01em;font-weight:600!important;
  background:radial-gradient(70px 40px at var(--ox,96%) 50%,rgba(220,240,255,.95),rgba(120,190,255,.55) 35%,transparent 72%),linear-gradient(90deg,#0B1631 0%,#0F2550 45%,#1E4E9A 80%,#3F86E0 100%)!important;
  box-shadow:inset 0 0 0 1px rgba(160,205,255,.35),inset 0 1px 0 rgba(255,255,255,.18),0 0 18px -4px rgba(90,170,255,.55)!important;transition:box-shadow .3s,transform .2s,background .2s!important}
.login::before{display:block!important;content:""!important;inset:0!important;padding:0!important;border-radius:inherit;background:radial-gradient(1px 1px at 20% 35%,rgba(255,255,255,.6),transparent),radial-gradient(1px 1px at 40% 70%,rgba(255,255,255,.4),transparent),radial-gradient(1px 1px at 62% 30%,rgba(255,255,255,.5),transparent)!important;-webkit-mask:none!important;mask:none!important;animation:none!important;opacity:.8!important}
.login::after{display:none!important}
.lg-orb{position:absolute;right:-6px;top:50%;width:28px;height:28px;margin-top:-14px;border-radius:50%;background:radial-gradient(circle,#fff,rgba(140,200,255,.6) 45%,transparent 70%);filter:blur(2px);opacity:.85;pointer-events:none;transition:right .4s,opacity .3s}
.login:hover{transform:translateY(-1px);box-shadow:inset 0 0 0 1px rgba(190,225,255,.6),inset 0 1px 0 rgba(255,255,255,.25),0 0 26px -2px rgba(100,180,255,.75)!important}
.login:hover .lg-orb{opacity:0}
.lg-t{text-shadow:0 0 10px rgba(150,200,255,.35)}
/* focus: remove the boxy sky shrink and the side glow; use one soft orb */
.zq.fx .zq-sky{transform:none!important;opacity:0!important}
.zq-sky{transition:opacity .9s ease!important}
.zq-sw::before{display:none!important}
.zq-s.go::after{display:none!important}
.zq-orb{position:absolute;left:50%;top:50%;width:118%;height:240%;translate:-50% -50%;border-radius:50%;z-index:-1;pointer-events:none;
  background:radial-gradient(closest-side,rgba(77,163,240,.9),rgba(140,195,255,.55) 50%,transparent 100%);filter:blur(24px);opacity:0;transform:scale(3.2);transition:opacity .8s ease,transform 1s cubic-bezier(.2,.8,.2,1)}
.zq.fx .zq-orb{opacity:.85;transform:scale(1)}
/* search results panel */
.zq-sw .zq-res{position:absolute!important;left:-80px;right:-80px;top:calc(100% + 14px);z-index:7;max-height:min(480px,58vh);overflow:auto;overscroll-behavior:contain;margin:0!important;padding:18px 18px 22px!important;border-radius:22px;background:rgba(255,255,255,.9)!important;-webkit-backdrop-filter:blur(26px) saturate(160%);backdrop-filter:blur(26px) saturate(160%);box-shadow:0 30px 60px -24px rgba(13,46,99,.4),inset 0 0 0 1px rgba(13,46,99,.08)!important;text-align:left;animation:zqSg .3s cubic-bezier(.2,.8,.2,1)}
.zq-sw .zq-res .zq-r{font:700 .9rem var(--display);color:#4A5874;margin:0 40px 4px 2px}
.zq-sw .zq-res .zq-g{grid-template-columns:repeat(auto-fill,minmax(200px,1fr))!important;gap:18px 14px!important;margin-top:10px}
.zq-sw .zq-res .qv-d,.zq-sw .zq-res .qv-meta span:last-child{display:none}
.zq-sw .zq-res .qv-btn{width:34px;height:34px}
.zq-x{position:absolute;right:12px;top:10px;width:32px;height:32px;border-radius:50%;border:0;background:#EEF2F8;color:#0D2E63;font-size:1.3rem;line-height:1;cursor:pointer}
.zq-x:hover{background:#DCE4F0}
.zq-sw:has(.zq-res:not([hidden])) .zq-sug{display:none}
.zq:has(.zq-res:not([hidden])) .zq-more{opacity:0;pointer-events:none}
@media (max-width:700px){.zq-sw .zq-res{left:0;right:0}.zq-sw .zq-res .zq-g{display:grid!important;grid-template-columns:1fr 1fr!important}}
/* activity deck */
.dq{margin:56px 0 24px;text-align:center}
.dq-h{font:800 clamp(1.9rem,3.4vw,2.8rem) var(--display);color:#0D2E63}
.dq-st{position:relative;height:500px;max-width:900px;margin:34px auto 0}
.dq-c{position:absolute;left:0;top:0;height:470px;padding:0;border:0;border-radius:24px;background:#fff;text-align:left;cursor:pointer;overflow:hidden;transform-origin:0 50%;
  box-shadow:0 1px 2px rgba(13,46,99,.06),0 18px 40px -22px rgba(13,46,99,.45);transition:transform .7s cubic-bezier(.2,.8,.2,1),box-shadow .3s}
.dq-c img{position:absolute;left:0;right:0;top:0;width:100%;height:62%;object-fit:cover;opacity:0;transition:opacity .4s}
.dq-c.on img{opacity:1}
.dq-chip{position:absolute;right:10px;top:14px;z-index:2;display:grid;justify-items:center;min-width:52px;padding:7px 8px;border-radius:14px;background:#EEF2F8;color:#0D2E63;font:800 .95rem/1.1 var(--display)}
.dq-chip small{font:500 .8rem var(--body);color:#6B7A94}
.dq-c.on .dq-chip{background:#111;color:#fff}.dq-c.on .dq-chip small{color:#BBB}
.dq-tx{position:absolute;left:0;right:0;bottom:0;padding:22px 24px 26px;display:flex;flex-direction:column;gap:4px;opacity:0;transition:opacity .35s .15s}
.dq-c.on .dq-tx{opacity:1}
.dq-tx small{color:#1C74D9;font:700 .85rem var(--display)}.dq-tx b{font:800 1.35rem/1.25 var(--display);color:#0D2E63}.dq-tx span{color:#4A5874;font-size:.95rem}
.dq-c:not(.on):hover{box-shadow:0 24px 46px -22px rgba(13,46,99,.55)}
.dq-cap{margin-top:12px;color:#6B7A94;font-size:.9rem}
@media (max-width:700px){.dq-st{height:430px}.dq-c{height:410px}}
/* tilt + light */
.qv-im,.zb-t,.zp-c,.dq-c.on{transform-style:preserve-3d}
.tl-on{transform:perspective(900px) rotateX(var(--rx)) rotateY(var(--ry)) translateY(-4px)!important;transition:transform .12s ease-out!important}
.tl-on::after{content:"";position:absolute;inset:0;pointer-events:none;border-radius:inherit;background:radial-gradient(320px circle at var(--lx) var(--ly),rgba(255,255,255,.22),transparent 60%);z-index:3}
.qv-im,.zb-t,.zp-c{position:relative}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v54.html','w').write(s)
print('v54 ok')
