D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build8.py').read())

# ---------- hero text: a portfolio course, with real TCAS70 dates ----------
i=s.index('      <div class="ar-txt">');j=s.index('      <div class="ar-m">',i)
s=s[:i]+'''      <div class="ar-txt">
        <p class="ar-kk rv">คอร์สปั้นพอร์ต ยื่นมหาลัย · สำหรับ ม.6</p>
        <h1 class="rv">Port Express</h1>
        <p class="ar-t rv"><span class="nw">ยังไม่มีพอร์ต?</span> <span class="nw">2 เดือน พร้อมยื่นรอบ Portfolio</span></p>
        <p class="ar-s rv">ทำเกม 3 งานเข้าพอร์ต ทำแฟ้มพอร์ตกับเทรนเนอร์ และซ้อมสัมภาษณ์กับอาจารย์มหาลัย · <b>5,990 บาท</b> <s>9,990</s></p>
        <div class="tl rv" aria-label="ปฏิทิน TCAS70 รอบ 1 Portfolio">
          <p class="tl-h"><span>TCAS70</span> รอบ 1 Portfolio เดินไปพร้อมคอร์ส</p>
          <ol>
            <li data-d="2026-08-15"><em>15 ส.ค. 69</em><b>มหาลัยเริ่มเปิดรับรอบ 1</b></li>
            <li data-d="2026-11-09"><em>9 พ.ย. 69</em><b>เริ่มเรียน Port Express</b></li>
            <li data-d="2027-01-04"><em>ม.ค. 70</em><b>พอร์ตครบ 3 เกม พร้อมยื่น</b></li>
            <li data-d="2027-03-10"><em>10 มี.ค. 70</em><b>ประกาศผลรอบ 1</b></li>
          </ol>
          <p class="tl-n">แต่ละมหาลัยปิดรับรอบ 1 ไม่พร้อมกัน เช็กวันของคณะที่อยากเข้า · ที่มา: ปฏิทิน TCAS70 ของ ทปอ.</p>
        </div>
      </div>
'''+s[j:]
# big senior portfolios around the machine
rep('      <div class="ar-m">','''      <div class="ar-m">
        <div class="ar-ps" aria-hidden="true"><figure class="p1"><img src="img/dek69-6.webp" alt=""><span>จุฬาฯ CEDT</span></figure><figure class="p2"><img src="img/dek69-1.webp" alt=""><span>สจล.</span></figure><figure class="p3"><img src="img/dek69-13.webp" alt=""><span>มหิดล</span></figure><figure class="p4"><img src="img/dek69-11.webp" alt=""><span>เกษตรศาสตร์</span></figure></div>''')

# ---------- startup hamster ----------
s=s.replace('<span class="pod"><img src="img/n-up.webp"','<span class="pod"><img src="img/n-ceo.webp"').replace('<img class="do-i" src="img/n-up.webp"','<img class="do-i" src="img/n-ceo.webp"')

# ---------- results: Apple bento ----------
i=s.index('<section class="proof">');j=s.index('</section>',i)+10
s=s[:i]+'''<section class="pr"><div class="pr-in">
    <h2 class="rv">ผลลัพธ์ที่วัดได้จริง</h2>
    <div class="pr-g">
      <a class="pr-t t1 rv" href="#works" data-pane="sen"><span class="bg"><img src="img/dek69-8.webp" alt=""><img src="img/dek69-12.webp" alt=""><img src="img/dek69-16.webp" alt=""></span><b data-count="48">48</b><p>รุ่นพี่ DEK69<br>ติดมหาวิทยาลัยสายคอม</p></a>
      <a class="pr-t t2 rv" href="#works"><span class="bg"><img src="img/work-eugation-strike.webp" alt=""></span><b data-count="37">37</b><p>ผลงานที่น้องสร้าง<br>และเผยแพร่ให้คนใช้จริง</p></a>
      <a class="pr-t t3 rv" href="#works" data-pane="nsc"><span class="bg"><img src="img/s-showcase2.webp" alt=""></span><b data-count="12">12</b><p>ผลงานเข้ารอบชิง NSC<br>การแข่งขันซอฟต์แวร์ระดับประเทศ</p></a>
    </div>
    <p class="pr-src">ข้อมูลจาก 2025 Success Story ของ Hamster Hub</p>
  </div></section>'''+s[j:]

# ---------- seniors: BE AN ICON style ----------
cut('  <section class="cy">','  <section class="ptn">','''  <section class="ic">
    <div class="ic-in">
      <div class="ic-l">
        <p class="ic-k rv">DEK69 · รอบ Portfolio</p>
        <h2 class="rv">ติดแล้ว<br><span>48 คน</span></h2>
        <p class="ic-s rv">รุ่นพี่ที่ยื่นมหาลัยด้วยผลงานที่ทำกับ Hamster Hub</p>
        <div class="ic-u rv" role="group" aria-label="ดูตามมหาวิทยาลัย">
          <button type="button" data-u="k" style="--c:#FF8A3D" aria-pressed="false"><b>24</b><span>สจล.</span></button>
          <button type="button" data-u="m" style="--c:#7D9BFF" aria-pressed="false"><b>9</b><span>มหิดล</span></button>
          <button type="button" data-u="c" style="--c:#FF7EB6" aria-pressed="false"><b>8</b><span>จุฬาฯ CEDT</span></button>
          <button type="button" data-u="u" style="--c:#4FD69C" aria-pressed="false"><b>7</b><span>เกษตรศาสตร์</span></button>
        </div>
        <a class="ic-a rv" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a>
      </div>
      <div class="ic-r" aria-label="โปสเตอร์รุ่นพี่ DEK69"><div class="ic-pl" id="icPl"></div></div>
    </div>
  </section>

''')
i=s.index('  /* seniors: a slowly turning 3D ring of posters */');j=s.index('  /* router */',i)
s=s[:i]+r'''  /* seniors: tilted wall of posters, three columns drifting */
  (function(){var P=document.getElementById('icPl');if(!P)return;var on=null;
    function card(g){return '<figure><img src="img/dek69-'+g[0]+'.webp" alt="'+g[1]+' '+UN[g[2]]+'" loading="lazy"></figure>'}
    function build(){var L=G.filter(function(g){return !on||g[2]===on}),a=L.slice();while(a.length<9)a=a.concat(L);var cols=[[],[],[]];a.forEach(function(g,k){cols[k%3].push(g)});
      P.innerHTML=cols.map(function(c,k){var h=c.map(card).join('');return '<div class="ic-c c'+k+'" style="--d:'+(c.length*5)+'s"><div>'+h+h+'</div></div>'}).join('')}
    build();document.querySelectorAll('.ic-u button').forEach(function(b){b.addEventListener('click',function(){on=on===b.dataset.u?null:b.dataset.u;document.querySelectorAll('.ic-u button').forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.u===on))});build()})})})();
  /* TCAS timeline: mark where we are */
  (function(){var now=new Date(),li=document.querySelectorAll('.tl li'),k=-1;li.forEach(function(e,n){if(new Date(e.dataset.d+'T00:00:00+07:00')<=now)k=n});
    li.forEach(function(e,n){e.classList.toggle('done',n<k);e.classList.toggle('here',n===k+1)})})();
'''+s[j:]

# ---------- grand page transitions ----------
i=s.index('  function ptBuild(v){');j=s.index('  var first=true;function route()')
s=s[:i]+r'''  var PTC={courses:['#5B3FD6','#FFD24A','#0B0720','COURSES','คอร์ส','หลายคอร์ส หลายสไตล์'],portex:['#FF3EA5','#39E0FF','#0B0720','PORT EXPRESS','Port Express','คอร์สปั้นพอร์ต ยื่นมหาลัย'],
    activity:['#FF4D6D','#FFB81C','#0B1640','EVENTS','กิจกรรม',''],works:['#8A6A1E','#E8C877','#050505','HALL OF FAME','ผลงาน','Class of 2026'],about:['#FF8A3D','#FFE7C2','#16161A','ABOUT US','เกี่ยวกับเรา','Hamster Hub']};
  function ptBuild(v){var h='',c=PTC[v];
    if(c){var k=c[5];if(v==='activity'){var nx=document.getElementById('nvNext');k=nx?nx.textContent:''}
      var row=(c[3]+' · ').repeat(6);
      h='<span class="gp a" style="--c:'+c[0]+'"></span><span class="gp b" style="--c:'+c[1]+'"></span><span class="gp z" style="--c:'+c[2]+'"><span class="gm r1">'+row+'</span><span class="gm r2">'+row+'</span>'+
        '<span class="gc'+(v==='works'?' gold':'')+'"><small style="color:'+c[1]+'">'+k+'</small><b>'+c[4]+'</b><span class="gl" style="background:'+c[1]+'"></span></span></span>'}
    else{h='<span class="pt-home"></span><img class="pt-peek" src="img/n-peek.webp" alt="">'}
    pt.className='pt v-'+v;pt.innerHTML=h;void pt.offsetWidth;pt.classList.add('in')}
'''+s[j:]
rep("var hold={works:1050,activity:900,courses:760,portex:760}[v]||620;","var hold=PTC[v]?900:620;")
rep("ptT=setTimeout(function(){show();pt.classList.add('out');","ptT=setTimeout(function(){show();var vw=document.querySelector('[data-view].on');if(vw&&PTC[v]){vw.classList.remove('pg-in');void vw.offsetWidth;vw.classList.add('pg-in')}pt.classList.add('out');")

css=r'''
/* ===== v9 ===== */
.ar-kk{display:inline-block;font:700 1rem var(--display);color:#0B0720;background:#FFD24A;padding:7px 14px 9px;box-shadow:inset 0 -4px 0 #C28A00;clip-path:polygon(0 4px,4px 4px,4px 0,calc(100% - 4px) 0,calc(100% - 4px) 4px,100% 4px,100% calc(100% - 4px),calc(100% - 4px) calc(100% - 4px),calc(100% - 4px) 100%,4px 100%,4px calc(100% - 4px),0 calc(100% - 4px))}
.ar-s{max-width:560px;line-height:1.6}.ar-s b{color:#FFD24A}
.tl{margin-top:26px;max-width:580px}
.tl-h{font:700 1.05rem var(--display);display:flex;align-items:center;gap:10px}
.tl-h span{font:400 .6rem var(--pixel);color:#0B0720;background:#9FE7FF;padding:6px 8px 7px;box-shadow:inset 0 -3px 0 #39A0C8}
.tl ol{list-style:none;margin:18px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));position:relative}
.tl ol::before{content:"";position:absolute;left:6px;right:6px;top:7px;height:4px;background:repeating-linear-gradient(90deg,#3A3290 0 8px,transparent 8px 12px)}
.tl li{position:relative;padding:26px 8px 0 0;display:grid;gap:3px}
.tl li::before{content:"";position:absolute;left:0;top:0;width:18px;height:18px;background:#0B0720;box-shadow:0 0 0 3px #3A3290}
.tl li.done::before{background:#7CF29A;box-shadow:0 0 0 3px #2E9E6B}
.tl li.here::before{background:#FFD24A;box-shadow:0 0 0 3px #C28A00,0 0 18px #FFD24A;animation:bl 1s steps(1) infinite}
.tl li.here::after{content:"ตอนนี้";position:absolute;left:24px;top:-1px;font:700 .72rem var(--display);color:#0B0720;background:#FFD24A;padding:1px 6px}
.tl em{font-style:normal;font:400 .55rem var(--pixel);color:#9FE7FF;line-height:1.6}
.tl b{font:600 .88rem/1.35 var(--display);color:#E8EAF8}
.tl li.done b{color:#9AA0C8}
.tl-n{margin-top:14px;font-size:.78rem;color:#8A90B8}
.ar-m{position:relative}
.ar-ps{position:absolute;inset:0;z-index:-1;pointer-events:none}
.ar-ps figure{position:absolute;margin:0;width:clamp(150px,13vw,200px);box-shadow:0 30px 40px -20px rgba(0,0,0,.8)}
.ar-ps img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border:4px solid #fff}
.ar-ps span{position:absolute;left:8px;bottom:8px;font:700 .78rem var(--display);color:#0B0720;background:#7CF29A;padding:3px 8px;box-shadow:inset 0 -3px 0 #2E9E6B}
.ar-ps .p1{left:-2%;top:6%;transform:rotate(-12deg)}.ar-ps .p2{left:-5%;top:46%;transform:rotate(-5deg)}
.ar-ps .p3{right:-6%;top:3%;transform:rotate(10deg)}.ar-ps .p4{right:-12%;top:44%;transform:rotate(5deg)}
.ar-ps figure{animation:psF 6s ease-in-out infinite}.ar-ps .p2{animation-delay:-2s}.ar-ps .p3{animation-delay:-4s}.ar-ps .p4{animation-delay:-1s}
@keyframes psF{50%{translate:0 -10px}}
/* full-bleed apple tiles */
.hp-grid{padding:12px 0 0}
.hp-grid .hg{max-width:none;padding:0 12px;gap:12px}
.hp-grid .tile{min-height:clamp(560px,48vw,700px);border-radius:24px}
/* results bento */
.pr{padding:12px 12px 0}
.pr-in{border-radius:24px;background:#F5F5F7;padding:clamp(56px,7vw,90px) clamp(16px,3vw,40px) 40px}
.pr h2{text-align:center;font:700 clamp(2rem,4vw,3rem) var(--display);letter-spacing:-.02em}
.pr-g{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:12px;margin-top:40px}
.pr-t{position:relative;overflow:hidden;min-height:420px;border-radius:22px;padding:30px;display:flex;flex-direction:column;justify-content:flex-end;color:#fff;text-decoration:none;background:#0B0B14}
.pr-t .bg{position:absolute;inset:0;display:flex}
.pr-t .bg img{flex:1;min-width:0;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.pr-t:hover .bg img{transform:scale(1.06)}
.pr-t::after{content:"";position:absolute;inset:0;background:linear-gradient(transparent 20%,rgba(5,5,15,.92))}
.pr-t b,.pr-t p{position:relative;z-index:1}
.pr-t b{font:800 clamp(5rem,9vw,8.5rem)/.9 var(--display);letter-spacing:-.04em;background:linear-gradient(180deg,#fff 30%,var(--g));-webkit-background-clip:text;background-clip:text;color:transparent}
.pr-t p{font:600 1.05rem/1.45 var(--display);color:rgba(255,255,255,.88);margin-top:10px}
.t1{--g:#FFD24A}.t2{--g:#7CF29A}.t3{--g:#9FC2FF}
.pr-src{text-align:center;color:var(--mute);font-size:.85rem;margin-top:24px}
/* seniors: BE AN ICON */
.ic{padding:12px 12px 0}
.ic-in{position:relative;overflow:hidden;border-radius:24px;background:radial-gradient(70% 90% at 80% 50%,#2A1470,#0A0716 70%);color:#fff;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);min-height:clamp(620px,56vw,780px)}
.ic-l{position:relative;z-index:2;padding:clamp(40px,6vw,90px) clamp(24px,5vw,80px);display:flex;flex-direction:column;justify-content:center}
.ic-k{font:400 .7rem var(--pixel);color:#FFD24A;letter-spacing:.1em}
.ic h2{font:800 clamp(3.4rem,8vw,7.2rem)/.95 var(--display);letter-spacing:-.04em;margin-top:16px}
.ic h2 span{background:linear-gradient(90deg,#FFD24A,#FF7EB6 60%,#9F8BFF);-webkit-background-clip:text;background-clip:text;color:transparent}
.ic-s{color:rgba(255,255,255,.7);margin-top:16px;font-size:1.05rem}
.ic-u{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:28px;max-width:420px}
.ic-u button{display:flex;align-items:baseline;gap:10px;padding:12px 14px;border:0;border-radius:14px;background:rgba(255,255,255,.06);color:#fff;cursor:pointer;text-align:left;box-shadow:inset 3px 0 0 var(--c);transition:background .2s}
.ic-u b{font:800 1.8rem/1 var(--display);color:var(--c)}.ic-u span{font:600 .95rem var(--display)}
.ic-u button:hover{background:rgba(255,255,255,.12)}
.ic-u button[aria-pressed="true"]{background:var(--c);color:#0A0716}.ic-u button[aria-pressed="true"] b{color:#0A0716}
.ic-a{margin-top:24px;align-self:flex-start;color:#0A0716;background:#fff;font:600 1rem var(--display);text-decoration:none;padding:12px 22px;border-radius:999px}
.ic-a:hover{background:#FFD24A}
.ic-r{position:relative;overflow:hidden}
.ic-pl{position:absolute;left:-10%;right:-25%;top:-30%;bottom:-30%;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;transform:rotate(-12deg)}
.ic-c{overflow:hidden}
.ic-c>div{display:grid;gap:18px;animation:icU var(--d) linear infinite}
.ic-c.c1>div{animation-name:icD}
.ic-r:hover .ic-c>div{animation-play-state:paused}
@keyframes icU{to{transform:translateY(calc(-50% - 9px))}}@keyframes icD{from{transform:translateY(calc(-50% - 9px))}to{transform:none}}
.ic-c figure{margin:0}
.ic-c img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:16px;box-shadow:0 20px 40px -20px rgba(0,0,0,.8);transition:transform .3s}
.ic-c img:hover{transform:scale(1.04)}
.ic-r::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,#0A0716 0%,transparent 22%),linear-gradient(#0A0716,transparent 14%,transparent 86%,#0A0716)}
/* grand transitions */
.gp{position:absolute;inset:-10% -20%;background:var(--c);transform:translateX(-120%) skewX(-14deg);animation:gpIn .6s cubic-bezier(.75,0,.2,1) forwards}
.gp.b{animation-delay:.07s}.gp.z{animation-delay:.14s;overflow:hidden;display:block}
@keyframes gpIn{to{transform:translateX(0) skewX(-14deg)}}
.pt.out .gp{transform:translateX(0) skewX(-14deg);animation:gpOut .7s cubic-bezier(.75,0,.2,1) forwards}
.pt.out .gp.z{animation-delay:0s}.pt.out .gp.b{animation-delay:.07s}.pt.out .gp.a{animation-delay:.14s}
@keyframes gpOut{to{transform:translateX(125%) skewX(-14deg)}}
.gm{position:absolute;left:0;white-space:nowrap;font:800 clamp(4rem,12vw,10rem)/1 var(--display);color:transparent;-webkit-text-stroke:1.5px rgba(255,255,255,.14);transform:skewX(14deg)}
.gm.r1{top:16%;animation:gmL 6s linear infinite}.gm.r2{top:68%;animation:gmR 6s linear infinite}
@keyframes gmL{from{translate:0 0}to{translate:-40% 0}}@keyframes gmR{from{translate:-40% 0}to{translate:0 0}}
.gc{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) skewX(14deg);display:grid;justify-items:center;gap:10px;text-align:center}
.gc small{font:600 clamp(.9rem,1.6vw,1.15rem) var(--display);opacity:0;animation:fadeIn .3s .55s forwards}
.gc b{font:800 clamp(3.6rem,11vw,9rem)/1 var(--display);color:#fff;letter-spacing:-.03em;clip-path:inset(100% 0 0 0);animation:gcUp .55s .38s cubic-bezier(.2,.9,.2,1) forwards}
@keyframes gcUp{to{clip-path:inset(-10% -5% -20% -5%)}}
.gc .gl{display:block;height:6px;width:0;animation:glW .5s .6s cubic-bezier(.2,.9,.2,1) forwards}
@keyframes glW{to{width:min(320px,60vw)}}
.gc.gold b{background:linear-gradient(100deg,#8A6A1E 0%,#F6DF9A 25%,#FFF6D6 35%,#C9A04A 50%,#F6DF9A 70%,#8A6A1E 100%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:gcUp .55s .38s cubic-bezier(.2,.9,.2,1) forwards,t5shine 1.4s .5s linear forwards}
.pt.out .gc{transition:transform .5s,opacity .4s;transform:translate(-50%,-50%) skewX(14deg) scale(1.15);opacity:0}
[data-view].pg-in{animation:pgIn .9s cubic-bezier(.2,.8,.2,1)}
@keyframes pgIn{from{opacity:0;transform:translateY(60px) scale(.97)}}
@media (max-width:1000px){.ar-ps .p2,.ar-ps .p4{display:none}.pr-g{grid-template-columns:minmax(0,1fr)}.ic-in{grid-template-columns:minmax(0,1fr)}.ic-r{height:520px}}
@media (max-width:600px){.tl ol{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:18px}.tl ol::before{display:none}.ar-ps{display:none}.pr-t{min-height:340px}.ic-u{grid-template-columns:minmax(0,1fr)}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v9.html','w').write(s)
print('v9 ok',len(s))
