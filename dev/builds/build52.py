SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build50.py').read())
# search button with arrow
rep('<button type="submit">ค้นหา</button>','<button type="submit" class="zq-go"><span>ค้นหา</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>')
# hamster: drawn body + live eyes
rep('<i class="zq-spr" id="zqSpr"></i>','<span class="zq-hb" id="zqSpr"><img src="img/ham-noeye.webp" alt=""><i class="ze l"><b></b></i><i class="ze r"><b></b></i><i class="zq-bur" aria-hidden="true"></i></span>')
# login
rep('<span class="lg-t">เข้าสู่ระบบ</span>','<svg class="lg-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8.5" r="3.6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M5 19.5c1.4-3.3 4-4.8 7-4.8s5.6 1.5 7 4.8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span class="lg-t">เข้าสู่ระบบ</span><svg class="lg-ar" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
# fonts: drop the explosion style
rep("'computer','boom','fan']","'computer','fan']")
# cards like the reference: picture, then text, round action, meta row
i=s.index('function cardH(x){');j=s.index('    function render(',i)
s=s[:i]+r'''function cardH(x){var bell='<svg viewBox="0 0 24 24"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z M10 20a2 2 0 0 0 4 0" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/></svg>',arr='<svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      cal='<svg viewBox="0 0 24 24"><rect x="4" y="5.5" width="16" height="14" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',tag='<svg viewBox="0 0 24 24"><path d="M4 12.5V5h7.5l8.5 8.5-7.5 7.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="8.5" cy="9" r="1.4" fill="currentColor"/></svg>';
      var lab=x.k==='course'?'คอร์สเรียน':x.k;
      return '<a class="qv'+(x.open?' on':'')+'" href="'+x.url+'" target="_blank" rel="noopener" aria-label="'+x.t+'"><span class="qv-im"><img src="'+x.img+'" alt="" loading="lazy">'+(x.open?'<span class="qv-live">เปิดรับ</span>':'')+'</span><span class="qv-row"><span class="qv-tx"><b>'+x.t+'</b><span class="qv-d">'+x.d+'</span></span><span class="qv-btn" title="'+(x.open?'ดูรายละเอียด':'รับแจ้งเตือน')+'">'+(x.open?arr:bell)+'</span></span><span class="qv-meta"><span>'+cal+x.st+'</span><span>'+tag+(x.pr?'<em>'+x.pr+'</em>':lab)+'</span></span></a>'}
'''+s[j:]
s=s.replace("$$('#zqG .ak')","$$('#zqG .qv')").replace("'.ak'","'.qv'")
JS=r'''
  /* hamster eyes look at the cursor in any direction; blink; act on search */
  (function(){var h=$('#zqHam');if(!h)return;var E=h.querySelectorAll('.ze b');
    document.addEventListener('pointermove',function(e){var r=h.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height*.46,dx=e.clientX-cx,dy=e.clientY-cy,d=Math.hypot(dx,dy)||1,k=Math.min(1,d/260);
      E.forEach(function(b){b.style.transform='translate('+(dx/d*k*38).toFixed(1)+'%,'+(dy/d*k*38).toFixed(1)+'%)'})});
    var f=$('#zqForm');function act(){h.classList.remove('act');void h.offsetWidth;h.classList.add('act');setTimeout(function(){h.classList.remove('act')},1500)}
    f.addEventListener('submit',act);document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('.zq-pop [data-q],.zq-sug [data-q]'))act()})})();
  /* hero play: click the empty sky for confetti */
  (function(){var z=$('.zq');if(!z)return;var C=['#1C74D9','#4DA3F0','#B3D8FF','#0D2E63','#fff','#FFC531'];
    z.addEventListener('click',function(e){if(e.target.closest('a,button,input,form,.zq-h,.zq-sug'))return;if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;
      for(var i=0;i<16;i++){var p=document.createElement('i');p.className='zq-cf';var a=Math.random()*6.283,v=60+Math.random()*120;p.style.left=e.clientX+'px';p.style.top=e.clientY+'px';p.style.background=C[i%C.length];
        p.style.setProperty('--x',(Math.cos(a)*v).toFixed(0)+'px');p.style.setProperty('--y',(Math.sin(a)*v-60).toFixed(0)+'px');p.style.setProperty('--r',(Math.random()*720-360).toFixed(0)+'deg');document.body.appendChild(p);setTimeout(function(q){return function(){q.remove()}}(p),1100)}})})();
  /* search button: magnetic + sparks */
  (function(){var b=$('.zq-go');if(!b)return;
    if(matchMedia('(hover:hover)').matches){b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.translate=((e.clientX-r.left-r.width/2)*.18)+'px '+((e.clientY-r.top-r.height/2)*.25)+'px';b.style.setProperty('--gx',(e.clientX-r.left)+'px')});b.addEventListener('pointerleave',function(){b.style.translate=''})}
    b.addEventListener('click',function(){for(var i=0;i<8;i++){var s=document.createElement('i');s.className='zq-sp';s.style.setProperty('--a',(i*45)+'deg');b.appendChild(s);setTimeout(function(q){return function(){q.remove()}}(s),600)}})})();
  /* login: light follows the cursor */
  (function(){var b=$('.login');if(!b)return;b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.setProperty('--mx',(e.clientX-r.left)+'px')})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v52 ===== */
/* hamster with live eyes */
.zq-hb{position:relative;display:block;width:76px}
.zq-hb img{display:block;width:100%;height:auto}
.zq-spr{background:none!important}
.ze{position:absolute;top:46.2%;width:9.4%;aspect-ratio:1;margin:-4.7% 0 0 -4.7%;animation:zeBl 4.6s infinite}
.ze.l{left:33.5%}.ze.r{left:67.6%}
.ze b{position:absolute;inset:0;border-radius:50%;background:#1A1210;transition:transform .12s ease-out}
.ze b::after{content:"";position:absolute;left:22%;top:16%;width:34%;height:34%;border-radius:50%;background:#fff}
@keyframes zeBl{0%,93%,100%{transform:scaleY(1)}95%,97%{transform:scaleY(.12)}}
.zq-bur{position:absolute;left:50%;top:30%;width:2px;height:2px;pointer-events:none}
/* search action: hop, spin, sparkle, dive */
.zq-sw .zq-ham.act{animation:zqAct 1.45s cubic-bezier(.4,0,.2,1)!important}
@keyframes zqAct{0%{transform:translateY(31px)}18%{transform:translateY(-34px) rotate(0)}38%{transform:translateY(-40px) rotate(360deg) scale(1.08)}55%{transform:translateY(-30px) rotate(360deg)}72%,86%{transform:translateY(90px) rotate(360deg) scale(.7)}100%{transform:translateY(31px) rotate(360deg)}}
.zq-ham.act .ze{animation:zeHp 1.45s}
@keyframes zeHp{15%,58%{transform:scaleY(.12)}}
.zq-ham.act .zq-bur{animation:zqBurst .6s .35s ease-out}
.zq-ham.act .zq-bur{box-shadow:0 -30px 0 2px #FFC531,26px -15px 0 2px #4DA3F0,26px 15px 0 2px #FFC531,0 30px 0 2px #4DA3F0,-26px 15px 0 2px #FFC531,-26px -15px 0 2px #4DA3F0;opacity:0}
@keyframes zqBurst{0%{opacity:1;transform:scale(.2)}100%{opacity:0;transform:scale(1.6)}}
/* headline: no clipped glyphs */
.zq-h{overflow:visible;line-height:1.3}
.zq-h #zqType{padding:.22em .24em;margin:-.22em -.24em}
.zq-h[data-f="persona"] #zqType,.zq-h[data-f="hacker"] #zqType{margin:0}
.zq-h[data-f="cartoon"] #zqType{color:#fff!important;-webkit-text-stroke:6px #1C74D9!important;text-shadow:5px 5px 0 #0D2E63}
/* search button */
.zq-go{position:relative;display:inline-flex!important;align-items:center;gap:6px;overflow:visible!important;background:linear-gradient(135deg,#4DA3F0,#1C74D9 55%,#155FB5)!important;color:#fff!important;transition:translate .15s ease-out,box-shadow .25s!important;box-shadow:0 6px 16px -6px rgba(28,116,217,.6)}
.zq-go::before{content:"";position:absolute;inset:0;border-radius:inherit;background:radial-gradient(60px circle at var(--gx,50%) 50%,rgba(255,255,255,.45),transparent 70%);opacity:0;transition:opacity .2s}
.zq-go:hover::before{opacity:1}
.zq-go svg{width:0;height:18px;opacity:0;transition:width .25s,opacity .25s}
.zq-go:hover svg{width:18px;opacity:1}
.zq-sp{position:absolute;left:50%;top:50%;width:4px;height:12px;margin:-6px 0 0 -2px;border-radius:2px;background:#4DA3F0;pointer-events:none;transform:rotate(var(--a));animation:zqSp .55s ease-out forwards}
@keyframes zqSp{to{transform:rotate(var(--a)) translateY(-42px);opacity:0}}
.zq-cf{position:fixed;z-index:200;width:9px;height:9px;border-radius:2px;pointer-events:none;animation:zqCf 1.1s cubic-bezier(.2,.7,.3,1) forwards}
@keyframes zqCf{to{transform:translate(var(--x),calc(var(--y) + 140px)) rotate(var(--r));opacity:0}}
/* login: gradient ring, icon swap, shine */
@property --lgb{syntax:"<angle>";inherits:false;initial-value:0deg}
.login{display:inline-flex!important;align-items:center;gap:8px;overflow:hidden!important;color:#fff!important;padding:9px 18px 9px 14px!important;background:radial-gradient(90px circle at var(--mx,30%) 50%,rgba(120,170,255,.35),transparent 70%),linear-gradient(135deg,#123B7A,#0D2E63)!important;
  box-shadow:0 6px 16px -8px rgba(13,46,99,.7)!important;transition:transform .2s,box-shadow .25s!important}
.login::before{display:block!important;content:""!important;position:absolute;inset:0!important;border-radius:inherit;padding:1.5px;opacity:1!important;z-index:0!important;background:conic-gradient(from var(--lgb),#4DA3F0,#9B7BFF,#FFC531,#4DA3F0)!important;-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask:linear-gradient(#000 0 0) content-box exclude,linear-gradient(#000 0 0);animation:lgRot 4s linear infinite!important}
@keyframes lgRot{to{--lgb:360deg}}
.login::after{display:block!important;content:""!important;position:absolute;top:0;bottom:0;left:-40%;width:30%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-20deg);filter:none!important;opacity:1!important;animation:lgSh 4.5s ease-in-out infinite;border-radius:0;height:auto;right:auto}
@keyframes lgSh{0%,70%{left:-40%}100%{left:130%}}
.lg-ic,.lg-ar{position:relative;z-index:1;width:18px;height:18px;flex:none;transition:transform .3s,opacity .3s,width .3s}
.lg-ar{width:0;opacity:0;transform:translateX(-6px)}
.lg-t{position:relative;z-index:1}
.login:hover{transform:translateY(-1px);box-shadow:0 10px 22px -8px rgba(28,116,217,.75)!important}
.login:hover .lg-ar{width:18px;opacity:1;transform:none}
.login:hover .lg-ic{transform:scale(.9) rotate(-8deg)}
.login:active{transform:scale(.96)}
/* reference-style cards */
.qv{flex:0 0 300px;scroll-snap-align:start;display:flex;flex-direction:column;text-decoration:none;color:#10213F}
.qv-im{position:relative;display:block;aspect-ratio:4/3;border-radius:18px;overflow:hidden;background:#E6ECF4}
.qv-im img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.qv:hover .qv-im img{transform:scale(1.05)}
.qv-im img[src*="afo-logo"]{object-fit:contain;padding:22px;background:#1C74D9}
.qv-live{position:absolute;left:12px;top:12px;display:flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;background:rgba(255,255,255,.92);color:#16803C;font:700 .78rem var(--display)}
.qv-live::before{content:"";width:7px;height:7px;border-radius:50%;background:#22C55E}
.qv-row{display:flex;align-items:flex-start;gap:12px;margin-top:14px}
.qv-tx{flex:1;min-width:0}
.qv-tx b{display:block;font:700 1.1rem/1.3 var(--display)}
.qv-d{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;color:#6B7A94;font-size:.92rem;line-height:1.5;margin-top:4px}
.qv-btn{flex:none;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;color:#1C74D9;box-shadow:inset 0 0 0 1px #DCE4F0;transition:background .2s,color .2s,transform .2s}
.qv-btn svg{width:18px;height:18px}
.qv:hover .qv-btn{background:#1C74D9;color:#fff;transform:scale(1.06)}
.qv.on .qv-btn{background:#1C74D9;color:#fff;box-shadow:none}
.qv-meta{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px;font-size:.84rem;color:#6B7A94}
.qv-meta span{display:inline-flex;align-items:center;gap:6px}
.qv-meta svg{width:15px;height:15px;color:#94A3B8}
.qv-meta em{font-style:normal;font-weight:800;color:#0D2E63}
.qv.on .qv-meta span:first-child{color:#16803C;font-weight:600}
.zq-g .qv.in{animation:mkIn .5s cubic-bezier(.2,.8,.2,1) both}
.zq-res .zq-g,.ctg{grid-template-columns:repeat(auto-fill,minmax(260px,1fr))!important;gap:28px 22px!important}
.zq-res .gk,.ctg .qv{flex:none}
.mr-r{gap:22px!important}
@media (max-width:700px){.qv{flex-basis:76vw}.zq-res .zq-g,.ctg{display:flex!important;overflow-x:auto;scroll-snap-type:x mandatory}.zq-res .gk,.ctg .qv{flex:0 0 76vw}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v52.html','w').write(s)
print('v52 ok')
