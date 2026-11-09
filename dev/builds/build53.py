SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build52.py').read())
# login icon: hamster head
i=s.index('<svg class="lg-ic"');j=s.index('</svg>',i)+6
s=s[:i]+'<img class="lg-ic" src="img/ham-ico.webp" alt="">'+s[j:]
# sky layer for the focus effect
rep('<section class="zq" aria-label="ค้นหาคอร์สและกิจกรรม">','<section class="zq" aria-label="ค้นหาคอร์สและกิจกรรม"><i class="zq-sky" aria-hidden="true"></i>')
# blue-only confetti
s=s.replace("var C=['#1C74D9','#4DA3F0','#B3D8FF','#0D2E63','#fff','#FFC531'];","var C=['#1C74D9','#4DA3F0','#B3D8FF','#0D2E63','#fff','#7FC0FF'];")
# no hop/spin on search: just dive and pop up
s=s.replace("f.addEventListener('submit',act);document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('.zq-pop [data-q],.zq-sug [data-q]'))act()})","")
JS=r'''
  /* hamster turns its whole head toward the cursor */
  (function(){var h=$('#zqHam'),hb=h&&h.querySelector('.zq-hb');if(!hb||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var tx=0,ty=0,cx=0,cy=0,run=false;
    document.addEventListener('pointermove',function(e){var r=h.getBoundingClientRect(),dx=e.clientX-(r.left+r.width/2),dy=e.clientY-(r.top+r.height*.45),d=Math.hypot(dx,dy)||1,k=Math.min(1,d/320);tx=dx/d*k;ty=dy/d*k;if(!run){run=true;requestAnimationFrame(loop)}});
    function loop(){cx+=(tx-cx)*.12;cy+=(ty-cy)*.12;hb.style.transform='translate('+(cx*5).toFixed(2)+'px,'+(cy*3).toFixed(2)+'px) rotate('+(cx*9).toFixed(2)+'deg) rotateY('+(cx*26).toFixed(2)+'deg) rotateX('+(-cy*22).toFixed(2)+'deg)';
      if(Math.abs(tx-cx)>.002||Math.abs(ty-cy)>.002)requestAnimationFrame(loop);else run=false}})();
  /* focus: the sky gathers into the search bar */
  (function(){var z=$('.zq'),inp=$('#zqIn'),sw=$('.zq-sw');if(!z||!inp)return;
    function place(){var r=sw.getBoundingClientRect(),zr=z.getBoundingClientRect();z.style.setProperty('--fx',(r.left+r.width/2-zr.left)+'px');z.style.setProperty('--fy',(r.top+r.height/2-zr.top)+'px')}
    inp.addEventListener('focus',function(){place();z.classList.add('fx')});inp.addEventListener('blur',function(){z.classList.remove('fx')})})();
  /* site-wide feel: scroll progress, back to top, ripple on buttons */
  (function(){var bar=document.createElement('i');bar.className='sp-bar';document.body.appendChild(bar);
    var top=document.createElement('button');top.type='button';top.className='to-top';top.setAttribute('aria-label','กลับขึ้นด้านบน');top.innerHTML='<svg viewBox="0 0 24 24"><path d="M12 19V6M6 11l6-6 6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>';document.body.appendChild(top);
    top.addEventListener('click',function(){scrollTo({top:0,behavior:'smooth'})});
    function u(){var m=document.documentElement.scrollHeight-innerHeight;bar.style.transform='scaleX('+(m>0?scrollY/m:0)+')';top.classList.toggle('on',scrollY>innerHeight*1.2)}
    addEventListener('scroll',u,{passive:true});addEventListener('hashchange',function(){setTimeout(u,60)});u();
    document.addEventListener('pointerdown',function(e){var b=e.target.closest&&e.target.closest('button,.mr-btn,.lbtn,.qv-btn,.zp-c i,.fit button,.btn');if(!b||b.classList.contains('vg-c'))return;var r=b.getBoundingClientRect(),d=Math.max(r.width,r.height)*2,i=document.createElement('i');i.className='rp';i.style.width=i.style.height=d+'px';i.style.left=(e.clientX-r.left-d/2)+'px';i.style.top=(e.clientY-r.top-d/2)+'px';
      if(getComputedStyle(b).position==='static')b.style.position='relative';b.style.overflow=b.style.overflow||'hidden';b.appendChild(i);setTimeout(function(){i.remove()},600)})})();
  /* nav: sliding indicator under the current page */
  (function(){var nav=$('.nav-in');if(!nav)return;var ind=document.createElement('i');ind.className='nv-ind';nav.appendChild(ind);
    function go(){var a=nav.querySelector('a.v[aria-current="page"]');if(!a){ind.style.opacity=0;return}var r=a.getBoundingClientRect(),n=nav.getBoundingClientRect();ind.style.opacity=1;ind.style.width=(r.width-16)+'px';ind.style.transform='translateX('+(r.left-n.left+8)+'px)'}
    addEventListener('hashchange',function(){setTimeout(go,80);setTimeout(go,1300)});addEventListener('resize',go);setTimeout(go,300)})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v53 ===== */
/* hero: sky layer that gathers into the bar on focus */
.zq{background:#fff!important}
.zq-sky{position:absolute;inset:0;z-index:0;pointer-events:none;background:radial-gradient(70% 60% at 50% 0%,#D6E6FF 0%,rgba(214,230,255,0) 70%),linear-gradient(#EAF2FF,#fff 75%);transform-origin:var(--fx,50%) var(--fy,60%);transition:transform .8s cubic-bezier(.7,0,.2,1),opacity .8s cubic-bezier(.7,0,.2,1)}
.zq.fx .zq-sky{transform:scale(.08,.04);opacity:0}
.zq-top,.zq-res{position:relative;z-index:1}.zq-top{width:100%;max-width:820px;margin-left:auto;margin-right:auto}.zq-sw{width:min(630px,100%)}.zq-more{z-index:2}
.zq-sw::before{background:radial-gradient(50% 120% at 0% 50%,rgba(77,163,240,.95),transparent 70%),radial-gradient(50% 120% at 100% 50%,rgba(28,116,217,.95),transparent 70%),radial-gradient(60% 100% at 50% 50%,rgba(179,216,255,.8),transparent 70%)!important;transition:opacity .5s .35s,transform .7s .3s cubic-bezier(.2,.8,.2,1)!important}
.zq-sw.lit .zq-s{box-shadow:0 0 0 1.5px #fff,0 0 0 3px rgba(77,163,240,.45),0 20px 40px -16px rgba(13,46,99,.35)!important}
.zq-ham.act .zq-bur{display:none}
/* hamster head turn */
.zq-sw .zq-ham{perspective:260px}
.zq-hb{transform-style:preserve-3d;will-change:transform}
/* search press: dive down and pop back */
.zq-sw .zq-ham.dive{animation:zqDv4 1.05s cubic-bezier(.5,0,.3,1)!important}
@keyframes zqDv4{0%{transform:translateY(6px)}20%{transform:translateY(-6px)}50%,70%{transform:translateY(80px)}88%{transform:translateY(-4px)}100%{transform:translateY(6px)}}
/* login: slimmer, lighter, hamster icon */
.login{padding:6px 16px 6px 8px!important;gap:7px!important;background:radial-gradient(80px circle at var(--mx,30%) 50%,rgba(255,255,255,.28),transparent 70%),linear-gradient(135deg,#3B8EEA,#1C74D9)!important;box-shadow:0 4px 12px -6px rgba(28,116,217,.6)!important;font-size:.95rem}
.login::before{background:conic-gradient(from var(--lgb),rgba(255,255,255,.9),rgba(179,216,255,.4),rgba(255,255,255,.9))!important;padding:1px!important}
.lg-ic{width:24px!important;height:24px!important;border-radius:50%;background:#fff;object-fit:contain;padding:1px}
.login:hover .lg-ic{transform:rotate(-10deg) scale(1.08)!important}
.login:hover{box-shadow:0 8px 18px -6px rgba(28,116,217,.7)!important}
/* site-wide details */
.sp-bar{position:fixed;left:0;right:0;top:0;height:3px;z-index:120;background:linear-gradient(90deg,#4DA3F0,#1C74D9);transform-origin:0 50%;transform:scaleX(0);pointer-events:none}
.to-top{position:fixed;right:22px;bottom:22px;z-index:110;width:46px;height:46px;border-radius:50%;border:0;display:grid;place-items:center;color:#fff;background:#1C74D9;box-shadow:0 10px 24px -8px rgba(13,46,99,.55);cursor:pointer;opacity:0;transform:translateY(16px) scale(.8);pointer-events:none;transition:opacity .3s,transform .35s cubic-bezier(.3,1.6,.5,1),background .2s}
.to-top.on{opacity:1;transform:none;pointer-events:auto}
.to-top:hover{background:#155FB5;transform:translateY(-3px)}
.to-top svg{width:20px;height:20px}
.rp{position:absolute;border-radius:50%;background:rgba(255,255,255,.4);transform:scale(0);pointer-events:none;animation:rpA .6s ease-out forwards;mix-blend-mode:overlay}
@keyframes rpA{to{transform:scale(1);opacity:0}}
.nav-in{position:relative}
.nv-ind{display:none!important;position:absolute;left:0;bottom:6px;height:2.5px;border-radius:2px;background:#1C74D9;opacity:0;transition:transform .45s cubic-bezier(.3,1.3,.5,1),width .45s,opacity .3s;pointer-events:none}
.nav-in a.v{transition:color .2s}
.nav-in a.v:hover{color:#1C74D9}
a,button{-webkit-tap-highlight-color:transparent}
button:active:not(.vg-c):not(.zq-go),.lbtn:active,.mr-btn:active{transform:scale(.97)}
:focus-visible{outline:3px solid rgba(28,116,217,.55);outline-offset:3px;border-radius:8px}
.er{transition:transform .25s,box-shadow .25s}
.er:hover{transform:translateY(-3px)}
.zb-t,.zp-c,.qv{will-change:transform}
::selection{background:#B3D8FF;color:#0D2E63}
@media (prefers-reduced-motion:reduce){.zq-sky{transition:none}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v53.html','w').write(s)
print('v53 ok')
