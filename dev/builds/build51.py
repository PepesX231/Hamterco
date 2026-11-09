SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build50.py').read())
rep('<button type="submit">ค้นหา</button>','<button type="submit" class="zq-go"><span>ค้นหา</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>')
rep("x.k==='course'?'Hamster Hub คอร์สเรียน':'Hamster Hub '+x.k","x.k==='course'?'คอร์สเรียน':x.k")
rep("if(ov>=0&&fr!==3)fr=ov;","if(ov>=0&&fr!==3)fr=ov;else if(window.__hamLook!=null&&fr!==3)fr=window.__hamLook;")
JS=r'''
  /* hero play: hamster eyes follow the cursor; click the empty sky for confetti */
  (function(){var z=$('.zq'),h=$('#zqHam');if(!z||!h)return;var tm=0;
    z.addEventListener('pointermove',function(e){var r=h.getBoundingClientRect(),dx=e.clientX-(r.left+r.width/2);window.__hamLook=dx<-80?1:dx>80?2:0;clearTimeout(tm);tm=setTimeout(function(){window.__hamLook=null},1600)});
    var C=['#FF7A1A','#FFB36B','#FFD9B8','#E85D04','#fff'];
    z.addEventListener('click',function(e){if(e.target.closest('a,button,input,form,.zq-h,.zq-sug'))return;if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;
      for(var i=0;i<16;i++){var p=document.createElement('i');p.className='zq-cf';var a=Math.random()*6.283,v=60+Math.random()*120;p.style.left=e.clientX+'px';p.style.top=e.clientY+'px';p.style.background=C[i%C.length];
        p.style.setProperty('--x',(Math.cos(a)*v).toFixed(0)+'px');p.style.setProperty('--y',(Math.sin(a)*v-60).toFixed(0)+'px');p.style.setProperty('--r',(Math.random()*720-360).toFixed(0)+'deg');document.body.appendChild(p);setTimeout(function(q){return function(){q.remove()}}(p),1100)}})})();
  /* search button: magnetic + spark burst on press */
  (function(){var b=$('.zq-go');if(!b||!matchMedia('(hover:hover)').matches)return;
    b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.translate=((e.clientX-r.left-r.width/2)*.18)+'px '+((e.clientY-r.top-r.height/2)*.25)+'px';b.style.setProperty('--gx',(e.clientX-r.left)+'px')});
    b.addEventListener('pointerleave',function(){b.style.translate=''});
    b.addEventListener('click',function(){for(var i=0;i<8;i++){var s=document.createElement('i');s.className='zq-sp';s.style.setProperty('--a',(i*45)+'deg');b.appendChild(s);setTimeout(function(q){return function(){q.remove()}}(s),600)}})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v51: orange and white ===== */
:root{--or:#FF7A1A;--or2:#E85D04;--or3:#FFF1E6}
/* hero warm sky */
.zq{background:radial-gradient(70% 60% at 50% 0%,#FFE3CC 0%,rgba(255,227,204,0) 70%),linear-gradient(#FFF4EA,#fff 75%)!important}
.zq-q{color:var(--or2)!important}
.zq-pop button:hover{color:var(--or2)!important;background:var(--or3)!important}
.zq-sug button:hover{background:var(--or3)!important}
.zq-sw::before{background:radial-gradient(50% 120% at 0% 50%,rgba(255,122,26,.9),transparent 70%),radial-gradient(50% 120% at 100% 50%,rgba(255,170,90,.9),transparent 70%),radial-gradient(60% 100% at 50% 50%,rgba(255,210,170,.6),transparent 70%)!important}
.zq-sw.lit .zq-s{box-shadow:0 0 0 1.5px #fff,0 0 0 3px rgba(255,122,26,.35),0 20px 40px -16px rgba(232,93,4,.3)!important}
.zq-cur{background:var(--or)!important}
/* headline: no yellow styles */
.zq-h[data-f="cartoon"] #zqType{color:#fff!important;-webkit-text-stroke:6px var(--or2)!important;text-shadow:5px 5px 0 #3A1A05}
.zq-h[data-f="boom"] #zqType{-webkit-text-stroke:5px #8A2A00!important;background:radial-gradient(circle,#FFB36B 0 40%,var(--or) 60%,transparent 62%)!important}
.zq-h[data-f="ragnarok"] #zqType{color:#FF8A3D!important;text-shadow:0 0 18px rgba(255,110,30,.6),3px 3px 0 #5A1A00!important}
.zq-h[data-f="elden"] #zqType{background:linear-gradient(180deg,#E8D3A0,#9A6E22 60%,#5E4210)!important;-webkit-background-clip:text!important;background-clip:text!important}
/* search button */
.zq-go{position:relative;display:inline-flex!important;align-items:center;gap:6px;overflow:visible!important;background:linear-gradient(135deg,#FF9A3D,var(--or) 50%,var(--or2))!important;color:#fff!important;padding:12px 22px!important;transition:translate .15s ease-out,box-shadow .25s,transform .12s!important;box-shadow:0 6px 16px -6px rgba(232,93,4,.6)}
.zq-go::before{content:"";position:absolute;inset:0;border-radius:inherit;background:radial-gradient(60px circle at var(--gx,50%) 50%,rgba(255,255,255,.45),transparent 70%);opacity:0;transition:opacity .2s}
.zq-go:hover::before{opacity:1}
.zq-go:hover{box-shadow:0 10px 24px -6px rgba(232,93,4,.75)}
.zq-go svg{width:0;height:18px;opacity:0;transition:width .25s,opacity .25s,transform .25s}
.zq-go:hover svg{width:18px;opacity:1}
.zq-go:active svg{transform:translateX(5px)}
.zq-sp{position:absolute;left:50%;top:50%;width:4px;height:12px;margin:-6px 0 0 -2px;border-radius:2px;background:var(--or);pointer-events:none;transform:rotate(var(--a)) translateY(0);animation:zqSp .55s ease-out forwards}
@keyframes zqSp{to{transform:rotate(var(--a)) translateY(-42px);opacity:0}}
.zq-cf{position:fixed;z-index:200;width:9px;height:9px;border-radius:2px;pointer-events:none;box-shadow:0 0 0 1px rgba(232,93,4,.25);animation:zqCf 1.1s cubic-bezier(.2,.7,.3,1) forwards}
@keyframes zqCf{to{transform:translate(var(--x),calc(var(--y) + 140px)) rotate(var(--r));opacity:0}}
/* login: orange, calm */
.login{background:var(--or)!important;color:#fff!important;box-shadow:0 4px 12px -4px rgba(232,93,4,.55)!important}
.login::before{display:none!important}
.login::after{display:none!important}
.login:hover{background:var(--or2)!important;box-shadow:0 6px 16px -4px rgba(232,93,4,.65)!important}
/* cards: tidier, orange accents */
.ak-k{left:18px;right:auto!important;top:16px!important;padding:4px 10px;border-radius:6px;background:rgba(255,255,255,.9);color:var(--or2)!important;font-size:.8rem!important;text-shadow:none!important}
.ak::after{background:linear-gradient(180deg,transparent 40%,rgba(20,10,4,.55) 65%,rgba(20,10,4,.9) 100%)!important}
.ak-s em{color:#FFB36B!important}
.ak.on .ak-a{background:var(--or)!important;color:#fff!important}
.ak-dots button.on{background:var(--or)!important}
.mr-btn,.mr-btn:hover{color:var(--or2)!important}
.mr-rw .mr-ar button,.mr-rw .mr-ar button:hover{color:var(--or2)!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v51.html','w').write(s)
print('v51 ok')
