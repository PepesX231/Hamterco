D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build22.py').read())
# Port Express page: back to the clean Apple-style hero (drop the pixel/full-bleed overrides)
i=s.index('/* v21b: full-bleed + pixel art */');j=s.index('/* ===== v22 =====',i);s=s[:i]+s[j:]
# Hall of Fame: timed-cards showcase
i=s.index('    <a class="tile hof2 rv"');j=s.index('</a>',i)+4
s=s[:i]+'''    <section class="tile hf3" id="hf3" aria-label="Hall of Fame ผลงานเด่นของน้องๆ ปี 2569">
      <div class="hf3-bg"><img id="hfB0" alt=""><img id="hfB1" alt=""></div>
      <div class="hf3-l" aria-live="polite">
        <p class="hf3-k">HALL OF FAME 2569</p>
        <h3 id="hfN"></h3>
        <p class="hf3-by" id="hfBy"></p>
        <p class="hf3-aw" id="hfAw"></p>
        <a class="hf3-go" href="#works" data-pane="hof">ดูผลงานทั้งหมด</a>
      </div>
      <div class="hf3-cards" id="hfC"></div>
      <div class="hf3-bar"><span class="hf3-p"><i id="hfP"></i></span><b id="hfI"></b></div>
    </section>'''+s[j:]
rep("  /* router */",r'''  /* hall of fame: timed cards, the next work opens into the background */
  (function(){var C=document.getElementById('hfC');if(!C)return;
    var H=[['stressstrike','StressStrike','@วิน','ชนะเลิศ OBEC Roboplayground'],['phi-krahang','ผีกระหัง','@นนท์',''],['eugation-strike','Eugation Strike','@ไผ่',''],['slash-speed','SLASH//SPEED','@ดินสอ',''],
      ['midnight-at-roadside','Midnight at Roadside','@Windy',''],['hot-hot-hot','Hot Hot Hot','@โอม',''],['apocalypis-building','Apocalypis Building','@ฟาร์',''],['escape-rolling','Escape Rolling','@เป๊ป','']];
    var a=0,b=0,tm=0,hold=false,T=4500,B=[document.getElementById('hfB0'),document.getElementById('hfB1')],sec=document.getElementById('hf3');
    C.innerHTML=H.map(function(h,k){return '<button type="button" class="hc3" data-k="'+k+'"><img src="img/work-'+h[0]+'.webp" alt="" loading="lazy"><span>'+h[1]+'</span></button>'}).join('');
    C.querySelectorAll('.hc3').forEach(function(c){c.addEventListener('click',function(){show(+c.dataset.k)})});
    function show(k){var n=H.length;a=(k+n)%n;var h=H[a];
      C.querySelectorAll('.hc3').forEach(function(c,i){var o=(i-a-1+n)%n;c.style.setProperty('--o',o);c.classList.toggle('gone',o>4)});
      b=1-b;B[b].src='img/work-'+h[0]+'.webp';B[b].classList.add('on');B[1-b].classList.remove('on');
      document.getElementById('hfN').textContent=h[1];document.getElementById('hfBy').textContent='เกมที่น้อง '+h[2]+' สร้างเอง';
      var aw=document.getElementById('hfAw');aw.textContent=h[3];aw.style.display=h[3]?'':'none';
      document.getElementById('hfI').textContent=(a+1<10?'0':'')+(a+1);
      var p=document.getElementById('hfP');p.style.animation='none';void p.offsetWidth;p.style.animation='';
      var l=sec.querySelector('.hf3-l');l.classList.remove('in');void l.offsetWidth;l.classList.add('in');
      clearTimeout(tm);tm=setTimeout(tick,T)}
    function tick(){if(hold||!document.querySelector('[data-view="home"].on')){tm=setTimeout(tick,600);return}show(a+1)}
    sec.addEventListener('pointerenter',function(){hold=true;sec.classList.add('hold')});sec.addEventListener('pointerleave',function(){hold=false;sec.classList.remove('hold')});
    show(0)})();
  /* router */''')
css=r'''
/* ===== v23: Hall of Fame timed cards ===== */
.hg.st .tile.hf3{display:block!important;position:relative;overflow:hidden;padding:0!important;min-height:clamp(560px,46vw,680px)!important;background:#0A0806;color:#fff;text-align:left}
.hf3-bg img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity 1s,transform 6s linear}
.hf3-bg img.on{opacity:1;transform:scale(1)}
.hf3::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,6,4,.9) 0%,rgba(8,6,4,.6) 42%,rgba(8,6,4,.1) 75%),linear-gradient(0deg,rgba(8,6,4,.8),transparent 40%);pointer-events:none;z-index:1}
.hf3-by{color:#fff!important}.hf3 .hf3-k{color:#F6DF9A!important;-webkit-text-fill-color:#F6DF9A}.hf3 .hf3-aw,.hf3 .hf3-go{color:#1A1206!important}
.hf3-l{position:absolute;z-index:2;left:clamp(24px,5vw,72px);top:50%;transform:translateY(-55%);max-width:min(560px,46%)}
.hf3-l.in>*{animation:tcIn .7s cubic-bezier(.2,.8,.2,1) both}.hf3-l.in>*:nth-child(2){animation-delay:.06s}.hf3-l.in>*:nth-child(3){animation-delay:.12s}.hf3-l.in>*:nth-child(4){animation-delay:.18s}
@keyframes tcIn{from{opacity:0;transform:translateY(24px)}}
.hf3-k{font:800 1rem var(--display);letter-spacing:.08em;background:linear-gradient(90deg,#F6DF9A,#C9A04A);-webkit-background-clip:text;background-clip:text;color:transparent}
.hf3 h3{font:900 clamp(2.6rem,6vw,5.2rem)/1.02 var(--display)!important;letter-spacing:-.02em;margin-top:12px!important;color:#fff!important}
.hf3-by{font:600 1.15rem var(--display);color:rgba(255,255,255,.85);margin-top:14px}
.hf3-aw{display:inline-block;margin-top:14px;font:700 .95rem var(--display);color:#1A1206;background:linear-gradient(90deg,#E8C877,#FFF1C2);padding:5px 14px;border-radius:999px}
.hf3-go{display:table;margin-top:26px;font:700 1.05rem var(--display);color:#1A1206;background:linear-gradient(90deg,#E8C877,#FFF1C2,#E8C877);padding:13px 28px;border-radius:999px;text-decoration:none}
.hf3-go:hover{filter:brightness(1.08)}
.hf3-cards{position:absolute;z-index:2;left:56%;right:0;top:50%;height:clamp(200px,20vw,280px);transform:translateY(-45%)}
.hc3{--o:0;position:absolute;top:0;left:0;width:clamp(150px,13vw,190px);border:0;padding:0;background:none;cursor:pointer;text-align:left;color:#fff;transform:translateX(calc(var(--o) * (clamp(150px,13vw,190px) + 18px)));transition:transform .9s cubic-bezier(.65,0,.2,1),opacity .6s}
.hc3 img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover;border-radius:14px;box-shadow:0 0 0 2px rgba(232,200,119,.5),0 24px 40px -18px rgba(0,0,0,.9);transition:box-shadow .2s}
.hc3:hover img{box-shadow:0 0 0 3px #F6DF9A,0 24px 40px -18px rgba(0,0,0,.9)}
.hc3 span{display:block;font:700 .95rem var(--display);margin-top:10px}
.hc3.gone{opacity:0;pointer-events:none}
.hf3-bar{position:absolute;z-index:2;left:clamp(24px,5vw,72px);right:clamp(24px,5vw,72px);bottom:28px;display:flex;align-items:center;gap:16px}
.hf3-p{flex:1;height:3px;background:rgba(255,255,255,.2);overflow:hidden}
.hf3-p i{display:block;height:100%;background:linear-gradient(90deg,#E8C877,#FFF1C2);transform-origin:left;animation:tcP 4.5s linear forwards}
.hf3.hold .hf3-p i{animation-play-state:paused}
@keyframes tcP{from{transform:scaleX(0)}}
.hf3-bar b{font:800 1.6rem var(--display);color:#F6DF9A;font-variant-numeric:tabular-nums}
@media (max-width:800px){.hf3-l{top:36px;transform:none;max-width:none;right:24px}.hf3-cards{left:24px;top:auto;bottom:70px;transform:none;height:200px}.hc3{width:120px;transform:translateX(calc(var(--o) * 132px))}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v23.html','w').write(s)
print('v23 ok',len(s))
