D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build9.py').read())
LINE='https://page.line.me/jkm4247u?openQrModal=true'
PX='https://www.hamsterhub.co/portex-site/index.html'

# ---------- HERO: the banner is the star, on a handheld ----------
i=s.index('    <div class="wrap ar-in">');j=s.index('    <div class="ar-floor"',i)
s=s[:i]+'''    <div class="wrap hh">
      <p class="ar-kk rv">คอร์สปั้นพอร์ต ยื่นมหาลัย · สำหรับ ม.6</p>
      <h1 class="hh-t rv"><span class="nw">ยังไม่มีพอร์ต?</span> <span class="nw">2 เดือน พร้อมยื่นรอบ Portfolio</span></h1>
      <div class="hh-b rv">
        <p class="hh-p"><b>5,990 บาท</b> <s>9,990</s><span>เริ่ม 9 พ.ย. 2569 · เรียน จ พ ศ · 2 เดือน</span></p>
        <div class="hh-a"><a class="b1" href="#portex">ดูรายละเอียดคอร์ส</a><a class="b2" href="'''+PX+'''" target="_blank" rel="noopener">เว็บ Port Express</a><a class="b3" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE</a></div>
      </div>
      <a class="gb rv" href="#portex" aria-label="ดูรายละเอียดคอร์ส Port Express"><span class="gb-s"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video><span class="gb-sl"></span></span><img class="gb-f" src="img/console.webp" alt=""></a>
    </div>
'''+s[j:]

# ---------- cartridges: what each game gives, and why games count ----------
CART=[('01','BRONZE','#D08A4E','work-escape-rolling','เกมแรก เล่นแล้วสนุก','เขียนโปรแกรมด้วย Unity เป็น และคิดเกมให้คนเล่นแล้วสนุก','น้องเขียนโค้ดได้จริง และทำงานจนจบได้'),
      ('02','SILVER','#B9C2D6','work-slash-speed','เกมที่แตกต่าง ขายได้','ออกแบบให้ต่างจากเกมทั่วไป เก็บความรู้สึกตอนเล่น และฝึกพูดนำเสนอ','น้องคิดเรื่องผู้เล่น ไม่ได้ทำตามสั่ง'),
      ('03','GOLD','#FFD24A','work-apocalypis-building','เกมใหญ่ ทำเป็นทีม','แบ่งสาย Art / Developer / Director ทำเกมขนาดใหญ่ร่วมกับเพื่อน','น้องทำงานเป็นทีมได้ และรู้ว่าตัวเองถนัดอะไร')]
cart=''.join('''<article class="ct" style="--c:%s"><div class="ct-top"><span>GAME %s</span><em>%s</em></div><div class="ct-lb"><img src="img/%s.webp" alt="" loading="lazy"></div>
  <h3>%s</h3><p class="ct-g"><small>ได้ทักษะ</small>%s</p><p class="ct-p"><small>ในพอร์ตบอกกรรมการว่า</small>%s</p></article>'''%c[:1][0:0]+'' if False else '''<article class="ct" style="--c:%s"><div class="ct-top"><span>GAME %s</span><em>%s</em></div><div class="ct-lb"><img src="img/%s.webp" alt="" loading="lazy"></div>
  <h3>%s</h3><p class="ct-g"><small>ได้ทักษะ</small>%s</p><p class="ct-p"><small>ในพอร์ตบอกกรรมการว่า</small>%s</p></article>'''%(c[2],c[0],c[1],c[3],c[4],c[5],c[6]) for c in CART)
rep('  <section class="hp-grid">','''  <section class="cg"><div class="cg-in">
    <p class="cg-k rv">ทำเกม 3 งาน เข้าแฟ้มพอร์ต</p>
    <h2 class="rv">ทำไมเกมใช้ยื่นพอร์ตได้</h2>
    <p class="cg-s rv">คณะสายคอม ไอที และดิจิทัล อยากเห็นผลงานที่น้องลงมือทำเอง เกมหนึ่งเกมโชว์ได้ครบทั้งการเขียนโปรแกรม การออกแบบ และความรับผิดชอบที่ทำงานจนจบ</p>
    <div class="cts">'''+cart+'''</div>
    <div class="cg-tr rv">
      <div><b>48 คน</b><span>รุ่นพี่ DEK69 ยื่นรอบพอร์ตด้วยผลงานแบบนี้แล้วติด</span></div>
      <div><b>ทุก 2 สัปดาห์</b><span>อาจารย์มหาวิทยาลัยฟังผลงาน พร้อมซ้อมสัมภาษณ์</span></div>
      <div><b>5 ครั้ง</b><span>Checkpoint ตรวจงาน บอกชัดว่าต้องแก้อะไร</span></div>
    </div>
  </div></section>

  <section class="hp-grid">''')

# ---------- results: better covers ----------
rep('<span class="bg"><img src="img/dek69-8.webp" alt=""><img src="img/dek69-12.webp" alt=""><img src="img/dek69-16.webp" alt=""></span>',
    '<span class="bg grid6"><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""><img src="img/dek69-13.webp" alt=""><img src="img/dek69-11.webp" alt=""><img src="img/dek69-9.webp" alt=""><img src="img/dek69-14.webp" alt=""></span>')
rep('<span class="bg"><img src="img/work-eugation-strike.webp" alt=""></span>','<span class="bg"><img src="img/work-phi-krahang.webp" alt=""></span>')
rep('<span class="bg"><img src="img/s-showcase2.webp" alt=""></span>','<span class="bg"><img src="img/s-showcase1.webp" alt="" style="object-position:70% 50%"></span>')

# ---------- seniors: center-focus carousel ----------
cut('  <section class="ic">','  <section class="ptn">','''  <section class="mc"><div class="mc-in">
    <p class="mc-bg" aria-hidden="true">CONGRATULATIONS</p>
    <div class="mc-h">
      <p class="mc-k rv">DEK69 · รอบ Portfolio</p>
      <h2 class="rv">รุ่นพี่ติดมหาลัยแล้ว <span>48 คน</span></h2>
      <div class="mc-u rv" role="group" aria-label="ดูตามมหาวิทยาลัย">
        <button type="button" data-u="" aria-pressed="true">ทั้งหมด</button>
        <button type="button" data-u="k" aria-pressed="false">สจล. <b>24</b></button>
        <button type="button" data-u="m" aria-pressed="false">มหิดล <b>9</b></button>
        <button type="button" data-u="c" aria-pressed="false">จุฬาฯ <b>8</b></button>
        <button type="button" data-u="u" aria-pressed="false">เกษตรศาสตร์ <b>7</b></button>
      </div>
    </div>
    <div class="mc-st" id="mcSt" aria-live="polite"></div>
    <div class="mc-cap"><button type="button" id="mcP" aria-label="คนก่อนหน้า">‹</button><p id="mcC"></p><button type="button" id="mcN" aria-label="คนถัดไป">›</button></div>
    <a class="mc-a" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a>
  </div></section>

''')
i=s.index('  /* seniors: tilted wall of posters, three columns drifting */');j=s.index('  /* TCAS timeline: mark where we are */',i)
s=s[:i]+r'''  /* seniors: center-focus carousel that walks by itself */
  (function(){var st=document.getElementById('mcSt');if(!st)return;var on='',L=[],a=0,tm=0,hold=false;
    function build(){L=G.filter(function(g){return !on||g[2]===on});a=0;st.innerHTML=L.map(function(g,k){return '<figure class="mc-c" data-k="'+k+'"><img src="img/dek69-'+g[0]+'.webp" alt="'+g[1]+' '+UN[g[2]]+'" loading="lazy"></figure>'}).join('');
      st.querySelectorAll('.mc-c').forEach(function(c){c.addEventListener('click',function(){go(+c.dataset.k)})});lay()}
    function lay(){var n=L.length,W=st.offsetWidth||1000,gap=Math.min(240,W*.2);st.querySelectorAll('.mc-c').forEach(function(c,k){var o=k-a;if(o>n/2)o-=n;if(o<-n/2)o+=n;var ab=Math.abs(o);
      c.style.transform='translate(-50%,-50%) translateX('+(o*gap)+'px) translateY('+(ab%2?28:0)+'px) scale('+(1-Math.min(ab,4)*.12)+')';c.style.zIndex=20-ab;c.style.opacity=ab>3?0:1;c.style.filter='brightness('+(1-Math.min(ab,3)*.18)+')';c.classList.toggle('on',o===0)});
      var g=L[a];document.getElementById('mcC').innerHTML='<b>'+g[1]+'</b> · '+g[3]+' · '+UN[g[2]]+'<small>จากคอร์ส '+g[4]+'</small>'}
    function go(k){a=(k+L.length)%L.length;lay();clearInterval(tm);tm=setInterval(function(){if(!hold&&document.querySelector('[data-view="home"].on'))go(a+1)},2800)}
    st.addEventListener('pointerenter',function(){hold=true});st.addEventListener('pointerleave',function(){hold=false});
    document.getElementById('mcP').addEventListener('click',function(){go(a-1)});document.getElementById('mcN').addEventListener('click',function(){go(a+1)});
    document.querySelectorAll('.mc-u button').forEach(function(b){b.addEventListener('click',function(){on=b.dataset.u;document.querySelectorAll('.mc-u button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});build();go(0)})});
    addEventListener('resize',lay);build();go(0)})();
'''+s[j:]

# ---------- transitions: one personality per page ----------
i=s.index('  var PTC={');j=s.index('  var first=true;function route()')
s=s[:i]+r'''  var PTC={courses:1,portex:1,activity:1,works:1,about:1};
  function ptBuild(v){var h='';
    if(v==='courses'){var CC=[['Port Express','#5B3FD6','#FFD24A'],['Port70','#FF8A3D','#fff'],['Project Express','#1068DC','#fff'],['National Project','#0B1640','#FFD24A'],['Python Pro Pack','#0D1117','#3FB950']];
      h='<span class="cf-bg"></span>';CC.forEach(function(c,k){h+='<span class="cf-c" style="--r:'+((k-2)*11)+'deg;--x:'+((k-2)*70)+'vw;--dl:'+(k*.05)+'s;background:'+c[1]+';color:'+c[2]+'"><small>COURSE 0'+(k+1)+'</small><b>'+c[0]+'</b></span>'});h+='<b class="cf-t">คอร์ส</b>'}
    else if(v==='portex'){var c=14,r=8;for(var y=0;y<r;y++)for(var x=0;x<c;x++)h+='<i style="left:'+(x*100/c)+'%;top:'+(y*100/r)+'%;width:'+(100/c+.2)+'%;height:'+(100/r+.2)+'%;--dl:'+(Math.random()*.32).toFixed(2)+'s"></i>';h+='<b class="pt-px">LOADING...</b>'}
    else if(v==='activity'){var nx=document.getElementById('nvNext'),x0=lastXY[0],y0=lastXY[1];h='<span class="ev-c a" style="--x:'+x0+'px;--y:'+y0+'px"></span><span class="ev-c b" style="--x:'+x0+'px;--y:'+y0+'px"></span>';
      for(var k=0;k<26;k++){var an=Math.random()*6.283,d=30+Math.random()*30;h+='<span class="ev-p" style="left:50%;top:50%;--tx:'+(Math.cos(an)*d).toFixed(1)+'vmin;--ty:'+(Math.sin(an)*d).toFixed(1)+'vmin;--rot:'+(Math.random()*720-360).toFixed(0)+'deg;background:'+['#FFB81C','#FF4D6D','#fff','#7CF29A','#5BC0FF'][k%5]+'"></span>'}
      h+='<span class="ev-t"><small>'+(nx?nx.textContent:'')+'</small><b>กิจกรรม</b></span>'}
    else if(v==='works'){h='<span class="t5-cu l"></span><span class="t5-cu r"></span><span class="t5-sp"></span>';for(var k=0;k<22;k++)h+='<span class="t5-d" style="left:'+(25+Math.random()*50).toFixed(1)+'%;top:'+(20+Math.random()*60).toFixed(1)+'%;--dl:'+(Math.random()*.6).toFixed(2)+'s;--s:'+(2+Math.random()*4).toFixed(1)+'px"></span>';h+='<b class="t5-hof"><small>HAMSTER HUB · CLASS OF 2026</small><span>HALL OF FAME</span></b>'}
    else if(v==='about'){h='<span class="pt-band"></span><img class="pt-run" src="img/n-walker.webp" alt="">'}
    else{h='<span class="pt-home"></span><img class="pt-peek" src="img/n-peek.webp" alt="">'}
    pt.className='pt v-'+v;pt.innerHTML=h;void pt.offsetWidth;pt.classList.add('in')}
'''+s[j:]
rep("var hold=PTC[v]?900:620;","var hold={courses:950,portex:760,activity:850,works:1050,about:700}[v]||620;")

rep('IW=1536,IH=864,V0=.79,V1=.965','IW=1536,IH=864,V0=.86,V1=.975')
css=r'''
/* ===== v10 ===== */
.hh{position:relative;z-index:2;text-align:center;padding-bottom:calc(var(--floor) * .55)}
.ar .hh-t{font:800 clamp(1.9rem,4vw,3.4rem)/1.2 var(--display)!important;letter-spacing:-.02em;margin-top:16px;color:#fff;text-shadow:none;white-space:normal}
.gb{position:relative;display:block;width:min(1000px,100%);margin:clamp(24px,3vw,36px) auto 0;aspect-ratio:1345/546;filter:drop-shadow(0 0 50px rgba(255,62,165,.28)) drop-shadow(0 40px 40px rgba(0,0,0,.6));transition:transform .3s}
.gb:hover{transform:translateY(-4px)}
.gb-s{position:absolute;left:21.1%;top:11.5%;width:57.6%;height:71.1%;overflow:hidden;background:#05061E}
.gb-s video{width:100%;height:100%;object-fit:cover;display:block}
.gb-sl{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.12) 0 2px,transparent 2px 4px),linear-gradient(125deg,rgba(255,255,255,.12) 0 12%,transparent 26%)}
.gb-f{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.hh-b{display:flex;justify-content:center;align-items:center;gap:20px 28px;flex-wrap:wrap;margin-top:20px}
.hh-p{text-align:left;color:#C9CDE8}.hh-p b{font:400 1.3rem var(--pixel);color:#FFD24A}.hh-p s{color:#8A90B8;margin-left:6px}.hh-p span{display:block;font-size:.9rem;margin-top:6px}
.hh-a{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.hh-a a{display:inline-flex;align-items:center;min-height:48px;padding:0 20px 4px;font:700 1rem var(--display);text-decoration:none;clip-path:polygon(0 4px,4px 4px,4px 0,calc(100% - 4px) 0,calc(100% - 4px) 4px,100% 4px,100% calc(100% - 4px),calc(100% - 4px) calc(100% - 4px),calc(100% - 4px) 100%,4px 100%,4px calc(100% - 4px),0 calc(100% - 4px));transition:transform .1s steps(2)}
.hh-a a:hover{transform:translateY(2px)}
.hh-a .b1{background:#FFD24A;color:#0B0720;box-shadow:inset 0 -4px 0 #C28A00}.hh-a .b2{background:#5BC0FF;color:#06123A;box-shadow:inset 0 -4px 0 #1D5FB8}.hh-a .b3{background:#3FDC7E;color:#06240F;box-shadow:inset 0 -4px 0 #1B7F43}
.ar .ar-kk{margin:0}
/* cartridges */
.cg{padding:12px 12px 0}
.cg-in{background:#0E0A26;color:#fff;padding:clamp(60px,8vw,110px) clamp(16px,4vw,64px);text-align:center}
.cg-k{font:600 1rem var(--display);color:#7CF29A}
.cg h2{font:800 clamp(2rem,4.4vw,3.4rem)/1.15 var(--display);letter-spacing:-.02em;margin-top:8px}
.cg-s{max-width:720px;margin:14px auto 0;color:#C9CDE8;line-height:1.7;font-size:1.05rem}
.cts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;max-width:1120px;margin:48px auto 0;text-align:left}
.ct{position:relative;background:#2A2470;padding:0 18px 22px;clip-path:polygon(0 0,calc(100% - 28px) 0,100% 28px,100% 100%,0 100%);box-shadow:inset 0 -6px 0 #1A1550;transition:transform .3s}
.ct:hover{transform:translateY(-6px)}
.ct-top{display:flex;justify-content:space-between;align-items:center;height:44px;margin:0 -18px;padding:0 40px 0 18px;background:repeating-linear-gradient(90deg,#1F1A5A 0 6px,#2A2470 6px 12px)}
.ct-top span{font:400 .62rem var(--pixel);color:#fff}.ct-top em{font-style:normal;font:400 .55rem var(--pixel);color:#14102E;background:var(--c);padding:5px 7px}
.ct-lb{margin-top:14px;background:#fff;padding:8px;box-shadow:0 0 0 4px var(--c)}
.ct-lb img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}
.ct h3{font:800 1.35rem var(--display);margin-top:18px}
.ct p{margin-top:12px;color:#D6D9F0;font-size:.95rem;line-height:1.55}
.ct small{display:block;font:400 .5rem var(--pixel);color:var(--c);letter-spacing:.06em;margin-bottom:6px}
.ct-p{padding-top:12px;border-top:3px dashed #3F3896}
.cg-tr{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;max-width:1120px;margin:40px auto 0}
.cg-tr div{display:grid;gap:6px;padding:22px;background:rgba(255,255,255,.05);text-align:left}
.cg-tr b{font:800 1.6rem var(--display);color:#FFD24A}.cg-tr span{color:#C9CDE8;font-size:.95rem}
/* plain rectangles, apple style */
.hp-grid .tile,.pr-in,.pr-t,.mc-in{border-radius:0!important}
/* results covers */
.pr-t .bg.grid6{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr)}
.pr-t .bg.grid6 img{width:100%;height:100%;object-position:50% 30%}
/* seniors: center focus */
.mc{padding:12px 12px 0}
.mc-in{position:relative;overflow:hidden;background:radial-gradient(60% 70% at 50% 60%,#3B1E8C 0%,#160B3E 55%,#0A0716 100%);color:#fff;padding:clamp(60px,7vw,96px) 16px 56px;text-align:center}
.mc-bg{position:absolute;left:50%;top:56%;transform:translate(-50%,-50%);font:800 clamp(4rem,13vw,13rem)/1 var(--display);color:rgba(255,255,255,.05);white-space:nowrap;pointer-events:none;letter-spacing:.02em}
.mc-h{position:relative}
.mc-k{font:600 1rem var(--display);color:#FFD24A}
.mc h2{font:800 clamp(2.2rem,5vw,4rem)/1.1 var(--display);letter-spacing:-.02em;margin-top:8px}
.mc h2 span{color:#FFD24A}
.mc-u{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin-top:22px}
.mc-u button{border:0;cursor:pointer;color:#fff;font:600 .95rem var(--display);padding:9px 16px;border-radius:999px;background:rgba(255,255,255,.08);box-shadow:inset 0 0 0 1px rgba(255,255,255,.16);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}
.mc-u b{color:#FFD24A;margin-left:4px}
.mc-u button[aria-pressed="true"]{background:#fff;color:#0A0716}.mc-u button[aria-pressed="true"] b{color:#B26A00}
.mc-st{position:relative;height:clamp(380px,36vw,470px);margin-top:28px}
.mc-c{position:absolute;left:50%;top:50%;margin:0;width:clamp(200px,20vw,280px);cursor:pointer;transition:transform .7s cubic-bezier(.2,.8,.2,1),opacity .5s,filter .5s}
.mc-c img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:18px;box-shadow:0 30px 50px -20px rgba(0,0,0,.8)}
.mc-c.on img{box-shadow:0 0 0 3px #FFD24A,0 40px 60px -20px rgba(0,0,0,.9)}
.mc-cap{position:relative;display:flex;justify-content:center;align-items:center;gap:18px;margin-top:10px}
.mc-cap p{min-width:min(460px,70vw);font-size:1rem;color:rgba(255,255,255,.85)}
.mc-cap p b{color:#fff}.mc-cap p small{display:block;color:#FFD24A;font-size:.88rem;margin-top:2px}
.mc-cap button{width:44px;height:44px;border-radius:50%;border:0;background:rgba(255,255,255,.12);color:#fff;font-size:1.5rem;cursor:pointer}
.mc-cap button:hover{background:#fff;color:#0A0716}
.mc-a{display:inline-block;margin-top:22px;color:#0A0716;background:#fff;font:600 1rem var(--display);text-decoration:none;padding:12px 22px;border-radius:999px}
/* transitions: courses = a hand of course cards */
.cf-bg{position:absolute;inset:0;background:radial-gradient(70% 70% at 50% 60%,#2B1D70,#0B0720);opacity:0;animation:fadeIn .25s forwards}
.pt.out .cf-bg{opacity:1;animation:fadeOut .45s .25s forwards}
.cf-c{position:absolute;left:50%;top:56%;width:min(210px,30vw);aspect-ratio:3/4;padding:18px;display:flex;flex-direction:column;justify-content:flex-end;border-radius:14px;box-shadow:0 30px 50px -20px rgba(0,0,0,.7),inset 0 0 0 2px rgba(255,255,255,.18);transform-origin:50% 130%;transform:translate(-50%,70vh) rotate(0deg);animation:cfIn .6s cubic-bezier(.2,.9,.3,1.15) var(--dl) forwards}
.cf-c small{font:400 .5rem var(--pixel);opacity:.8}.cf-c b{font:800 clamp(1rem,2vw,1.4rem)/1.15 var(--display);margin-top:6px}
@keyframes cfIn{to{transform:translate(-50%,-50%) rotate(var(--r))}}
.pt.out .cf-c{transform:translate(-50%,-50%) rotate(var(--r));animation:cfOut .55s cubic-bezier(.6,0,.4,1) var(--dl) forwards}
@keyframes cfOut{to{transform:translate(calc(-50% + var(--x)),-160%) rotate(calc(var(--r) * 3));opacity:0}}
.cf-t{position:absolute;left:50%;top:14%;transform:translateX(-50%);font:800 clamp(2.6rem,7vw,5rem)/1 var(--display);color:#fff;opacity:0;animation:fadeIn .3s .35s forwards}
.pt.out .cf-t{opacity:1;animation:fadeOut .2s forwards}
/* activity = a burst from where you clicked */
.ev-c{position:absolute;inset:0;clip-path:circle(0 at var(--x) var(--y));animation:evIn .55s cubic-bezier(.7,0,.2,1) forwards}
.ev-c.a{background:#FF4D6D}.ev-c.b{background:#0B1640;animation-delay:.12s}
@keyframes evIn{to{clip-path:circle(150% at var(--x) var(--y))}}
.pt.out .ev-c{clip-path:circle(150% at 50% 50%);animation:evOut .6s cubic-bezier(.7,0,.2,1) forwards}
.pt.out .ev-c.a{animation-delay:.1s}
@keyframes evOut{to{clip-path:circle(0 at 50% 50%)}}
.ev-p{position:absolute;width:12px;height:12px;opacity:0;animation:evP .9s .35s cubic-bezier(.1,.8,.3,1) forwards}
.ev-p:nth-child(3n){border-radius:50%}.ev-p:nth-child(4n){width:6px;height:16px}
@keyframes evP{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(var(--tx),var(--ty)) rotate(var(--rot))}}
.ev-t{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) scale(.6);display:grid;justify-items:center;gap:8px;opacity:0;animation:evT .45s .3s cubic-bezier(.3,1.6,.5,1) forwards}
.ev-t small{font:700 clamp(1rem,2vw,1.3rem) var(--display);color:#FFB81C}.ev-t b{font:800 clamp(3.4rem,10vw,8rem)/1 var(--display);color:#fff}
@keyframes evT{to{opacity:1;transform:translate(-50%,-50%) scale(1)}}
.pt.out .ev-t{opacity:1;transform:translate(-50%,-50%);animation:fadeOut .2s forwards}
@media (max-width:1000px){.cts,.cg-tr{grid-template-columns:minmax(0,1fr);max-width:520px}}
@media (max-width:600px){.ar .hh-t .nw{white-space:normal}.ar .hh-t{font-size:1.7rem!important}.hh-p{text-align:center}.gb{width:112%;margin-left:-6%}.mc-cap p{min-width:0;font-size:.9rem}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v10.html','w').write(s)
print('v10 ok',len(s))
