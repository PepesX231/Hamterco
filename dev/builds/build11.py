import re
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build10.py').read())
LINE='https://page.line.me/jkm4247u?openQrModal=true'
PX='https://www.hamsterhub.co/portex-site/index.html'

# ---------- the banner itself: a 4-scene story of what the course is ----------
def banner(cls=''):
    return '''<div class="pb '''+cls+'''" aria-label="Port Express คอร์สปั้นพอร์ตยื่นมหาลัย สำหรับ ม.6: 2 เดือน ทำเกม 3 งาน ทำแฟ้มพอร์ต ซ้อมสัมภาษณ์ รุ่นพี่ติดแล้ว 48 คน">
  <span class="pb-sky" aria-hidden="true"></span>
  <div class="sc s1"><img class="pb-ham" src="img/n-grad.webp" alt=""><div class="pb-tx"><b class="pb-logo">PORT<br>EXPRESS</b><p class="pb-a">คอร์สปั้นพอร์ต ยื่นมหาลัย</p><p class="pb-b">สำหรับ ม.6 ที่ยังไม่มีพอร์ต</p></div></div>
  <div class="sc s2"><p class="pb-h">2 เดือน ทำเกมจริง 3 งาน</p><div class="pb-gs"><figure><img src="img/work-escape-rolling.webp" alt=""><figcaption>GAME 1</figcaption></figure><figure><img src="img/work-slash-speed.webp" alt=""><figcaption>GAME 2</figcaption></figure><figure><img src="img/work-apocalypis-building.webp" alt=""><figcaption>GAME 3</figcaption></figure></div></div>
  <div class="sc s3"><div class="pb-fd"><span class="tab">PORTFOLIO</span><span class="pg p1"></span><span class="pg p2"></span><span class="pg p3"></span><b class="stamp">READY!</b></div><ul class="pb-ck"><li>เกม 3 งานเข้าแฟ้ม</li><li>แฟ้มพอร์ต + Pitch Deck</li><li>ซ้อมสัมภาษณ์กับอาจารย์มหาลัย</li></ul></div>
  <div class="sc s4"><div class="pb-fan"><img src="img/dek69-13.webp" alt=""><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""><img src="img/dek69-11.webp" alt=""></div><div class="pb-tx r"><p class="pb-h">รุ่นพี่ติดแล้ว 48 คน</p><p class="pb-b">สจล. · จุฬาฯ · มหิดล · เกษตรศาสตร์</p><p class="pb-p">เริ่ม 9 พ.ย. · 5,990 บาท</p></div></div>
  <span class="pb-pip" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
</div>'''
s=s.replace('<span class="gb-s"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video><span class="gb-sl"></span></span>','<span class="gb-s">'+banner()+'<span class="gb-sl"></span></span>',1)
# bigger console, shorter top
rep('<h1 class="hh-t rv">','<h1 class="hh-t rv" style="display:none">')
rep('<p class="ar-kk rv">คอร์สปั้นพอร์ต ยื่นมหาลัย · สำหรับ ม.6</p>\n      <h1','<h1 class="sr">Port Express คอร์สปั้นพอร์ต ยื่นมหาลัย สำหรับ ม.6</h1>\n      <h1')

# ---------- home: the "why games" block leaves; it lives on the course page now ----------
i=s.index('  <section class="cg">');j=s.index('  <section class="hp-grid">',i);cgblock=s[i:j];s=s[:i]+s[j:]

# ---------- results ----------
rep('<span class="bg"><img src="img/work-phi-krahang.webp" alt=""></span>','<span class="bg"><img src="img/works-mosaic.webp" alt=""></span>')
rep('<p>ผลงานเข้ารอบชิง NSC<br>การแข่งขันซอฟต์แวร์ระดับประเทศ</p>','<p>ผลงานเข้ารอบชิงชนะเลิศ NSC<br><small>NSC คือการแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย</small></p>')

# ---------- seniors: no round buttons; ovals only on hover ----------
rep('<div class="mc-cap"><button type="button" id="mcP" aria-label="คนก่อนหน้า">‹</button><p id="mcC"></p><button type="button" id="mcN" aria-label="คนถัดไป">›</button></div>','<div class="mc-cap"><p id="mcC"></p></div>')
rep("document.getElementById('mcP').addEventListener('click',function(){go(a-1)});document.getElementById('mcN').addEventListener('click',function(){go(a+1)});","")
rep('<a class="mc-a" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a>','<a class="lk" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a>')

# ---------- home ends with a clear next step ----------
rep('  <section class="ptn">','''  <section class="end"><div class="end-in">
    <h2 class="rv">อยากให้น้องมีผลงานจริงเป็นของตัวเอง</h2>
    <p class="rv">เลือกคอร์สที่ใช่ หรือทัก LINE ให้ทีมแนะนำตามชั้นเรียนและเป้าหมายของน้อง</p>
    <div class="end-b rv"><a class="e1" href="#courses">ดูคอร์สทั้งหมด</a><a class="e2" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE ปรึกษาทีม</a></div>
  </div></section>

  <section class="ptn">''',1)

# ---------- courses: plain banner with a pixel frame, no cabinet ----------
cut('    <div class="ct-cab">','    <section class="ct-list">','''    <div class="ctb">
      <a class="ctb-f" href="#portex" aria-label="ดูรายละเอียด Port Express">'''+banner('wide')+'''</a>
      <div class="ctb-b"><div><b>Port Express</b><span>คอร์สปั้นพอร์ต ยื่นมหาลัย สำหรับ ม.6 · เริ่ม 9 พ.ย. 2569 · <em>5,990 บาท</em></span></div>
        <div class="hh-a"><a class="b1" href="#portex">ดูรายละเอียดคอร์ส</a><a class="b2" href="'''+PX+'''" target="_blank" rel="noopener">เว็บ Port Express</a></div></div>
    </div>
''')
# ---------- Port Express page: banner instead of cabinet, local buy bar, why-games as a detail ----------
s=re.sub(r'<div class="cab c-px">.*?<div class="cab-kick"></div>\n</div>','<div class="ctb-f px-bnr">'+banner()+'</div>',s,count=1,flags=re.S)
rep('<div data-view="portex" class="pxp">','''<div data-view="portex" class="pxp">
  <div class="pxln"><div class="wrap pxln-in"><b>Port Express</b><span class="pxst">รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</span><a href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a></div></div>''')
why='''      <details class="why"><summary>ทำไมเกมใช้ยื่นพอร์ตได้</summary><div>
        <p>คณะสายคอม ไอที และดิจิทัล อยากเห็นผลงานที่น้องลงมือทำเอง เกมหนึ่งเกมโชว์ได้ครบทั้งการเขียนโปรแกรม การออกแบบ และความรับผิดชอบที่ทำงานจนจบ ใน Port Express น้องทำ 3 เกม แต่ละเกมบอกกรรมการคนละเรื่อง</p>
        <ul><li><b>เกมที่ 1 เกมแรกที่เล่นสนุก</b> บอกว่าน้องเขียนโค้ดได้จริงและทำงานจนจบได้</li><li><b>เกมที่ 2 เกมที่แตกต่าง ขายได้</b> บอกว่าน้องคิดเรื่องผู้เล่น ไม่ได้ทำตามสั่ง</li><li><b>เกมที่ 3 เกมใหญ่ทำเป็นทีม</b> บอกว่าน้องทำงานเป็นทีมได้และรู้ว่าตัวเองถนัดอะไร</li></ul>
        <p>Hamster Hub ไม่ได้สอนแค่เกม ยังมีคอร์สเว็บ แอป และ IoT ให้เลือกตามคณะที่น้องอยากเข้า</p></div></details>
'''
rep('      <details><summary>ไม่เคยทำเกมเลย เรียนได้ไหม</summary>',why+'      <details><summary>ไม่เคยทำเกมเลย เรียนได้ไหม</summary>')

# ---------- feed: fill the screen + volume ----------
rep("  /* router */",r'''  /* feed volume: one slider for every clip */
  (function(){var tk=document.querySelector('.yt .tk');if(!tk)return;var w=document.createElement('label');w.className='tk-vol';
    w.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z" fill="currentColor"/><path d="M15.5 9a4 4 0 0 1 0 6M18 6.5a7.5 7.5 0 0 1 0 11" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg><span class="sr">ระดับเสียง</span><input type="range" min="0" max="100" value="0" aria-label="ระดับเสียง">';
    tk.appendChild(w);var r=w.querySelector('input');
    r.addEventListener('input',function(){var val=r.value/100;tk.querySelectorAll('video').forEach(function(v){v.volume=val});var on=document.querySelector('.tk-mute[aria-pressed="true"]');
      var item=[].slice.call(tk.querySelectorAll('.tk-item')).filter(function(it){var b=it.getBoundingClientRect();return b.top>=-10&&b.top<innerHeight/2})[0],mb=item&&item.querySelector('.tk-mute');
      if(val>0&&!on&&mb)mb.click();if(val===0&&on&&mb)mb.click();r.style.setProperty('--v',r.value+'%')});
    tk.addEventListener('click',function(e){var b=e.target.closest('.tk-mute');if(!b)return;setTimeout(function(){var on=b.getAttribute('aria-pressed')==='true';if(on&&+r.value===0){r.value=70;tk.querySelectorAll('video').forEach(function(v){v.volume=.7})}if(!on)r.value=0;r.style.setProperty('--v',r.value+'%')},0)})})();
  /* router */''')

# ---------- transitions ----------
i=s.index("    if(v==='courses'){var CC=");j=s.index("    else if(v==='portex')",i)
s=s[:i]+r'''    if(v==='courses'){var F=[['f1','คอร์ส'],['f2','คอร์ส'],['f3','คอร์ส'],['f4','&gt; คอร์ส_'],['f5','คอร์ส'],['f1','คอร์ส'],['f3','คอร์ส']];
      h='<span class="cs">';F.forEach(function(f,k){h+='<span class="cs-f '+f[0]+'" style="--d:'+(k*.085).toFixed(3)+'s"><b>'+f[1]+'</b></span>'});
      h+='<span class="cs-end"><small>หลายคอร์ส หลายสไตล์ เลือกที่ใช่</small><b>คอร์ส</b></span></span>'}
'''+s[j:]
i=s.index("    else if(v==='activity'){");j=s.index("    else if(v==='works')",i)
s=s[:i]+r'''    else if(v==='activity'){var nx=document.getElementById('nvNext'),x0=lastXY[0],y0=lastXY[1],ST=['n-win','n-gamer','n-walker','n-maker','n-read','afo-ic0','afo-ic1','afo-ic2','n-ceo','n-grad'];h='<span class="ev-w"><span class="ev-c a" style="--x:'+x0+'px;--y:'+y0+'px"></span><span class="ev-c b" style="--x:'+x0+'px;--y:'+y0+'px"></span>';
      for(var k=0;k<10;k++){var an=k/10*6.283+Math.random()*.4,d=34+Math.random()*10;h+='<img class="ev-s" src="img/'+ST[k]+'.webp" alt="" style="--tx:'+(Math.cos(an)*d).toFixed(1)+'vmin;--ty:'+(Math.sin(an)*d*.8).toFixed(1)+'vmin;--rot:'+(Math.random()*40-20).toFixed(0)+'deg;--dl:'+(.3+k*.025).toFixed(3)+'s">'}
      h+='<span class="ev-t"><small>'+(nx?nx.textContent:'')+'</small><b>กิจกรรม</b></span></span>'}
'''+s[j:]
rep("h+='<b class=\"t5-hof\"><small>HAMSTER HUB · CLASS OF 2026</small><span>HALL OF FAME</span></b>'}","h+='<span class=\"t5-fl\"></span><img class=\"t5-tr\" src=\"img/n-win.webp\" alt=\"\"><b class=\"t5-hof\"><small>HAMSTER HUB · CLASS OF 2026</small><span>HALL OF FAME</span></b>'}")

css=r'''
/* ===== v11 ===== */
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.gb{width:min(1280px,100%)}
.hh{padding-top:4px}
.hh-b{margin-top:0}
/* the story banner (sizes follow the banner's own width) */
.pb{position:absolute;inset:0;container-type:inline-size;overflow:hidden;background:#0B0A2E;color:#fff;font-family:var(--display)}
.pb-sky{position:absolute;inset:0;background:radial-gradient(70% 90% at 75% 30%,#3B1E8C 0%,#160B3E 55%,#0A0716 100%)}
.pb-sky::before{content:"";position:absolute;inset:0;background-image:radial-gradient(#fff 1px,transparent 1.5px),radial-gradient(#9FE7FF 1px,transparent 1.5px);background-size:9cqw 9cqw,13cqw 13cqw;background-position:0 0,4cqw 6cqw;opacity:.5}
.sc{position:absolute;inset:0;display:flex;align-items:center;gap:4cqw;padding:0 7cqw;opacity:0;animation:pbS 16s infinite}
.s2{animation-delay:4s;flex-direction:column;justify-content:center;gap:3cqw}.s3{animation-delay:8s}.s4{animation-delay:12s}
@keyframes pbS{0%{opacity:0}2.5%,22.5%{opacity:1}25%,100%{opacity:0}}
.sc>*,.pb-gs figure,.pb-ck li,.pb-fan img,.pg,.stamp{animation:pbI 16s infinite both}
@keyframes pbI{0%{opacity:0;transform:translateY(3cqw) scale(.94)}3%,100%{opacity:1;transform:none}}
.s1 .pb-ham{width:24cqw;filter:drop-shadow(0 1cqw 2cqw rgba(0,0,0,.5))}
.pb-logo{display:block;font:400 6.6cqw/1.12 var(--pixel);color:#FFD24A;text-shadow:.6cqw .6cqw 0 #E0337E}
.pb-a{font:800 4.2cqw/1.25 var(--display);margin-top:2.4cqw}
.pb-b{font:600 2.7cqw/1.4 var(--display);color:#C9CDE8;margin-top:1cqw}
.s1 .pb-tx{animation-delay:.25s}
.pb-h{font:800 4.6cqw/1.2 var(--display)}
.s2 .pb-h{animation-delay:4s}
.pb-gs{display:flex;gap:2.4cqw;animation:none!important}
.pb-gs figure{margin:0;width:24cqw;background:#2A2470;padding:1cqw;box-shadow:0 0 0 .5cqw #FFD24A}
.pb-gs figure:nth-child(1){animation-delay:4.3s}.pb-gs figure:nth-child(2){animation-delay:4.6s;box-shadow:0 0 0 .5cqw #5BC0FF}.pb-gs figure:nth-child(3){animation-delay:4.9s;box-shadow:0 0 0 .5cqw #3FDC7E}
.pb-gs img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover}
.pb-gs figcaption{font:400 1.6cqw var(--pixel);margin-top:1cqw;color:#FFD24A}
.pb-fd{position:relative;flex:none;width:30cqw;height:33cqw;animation-delay:8s!important}
.pb-fd::before{content:"";position:absolute;inset:3cqw 0 0;background:#FFB81C;box-shadow:inset 0 -1.2cqw 0 #C28A00}
.pb-fd .tab{position:absolute;left:0;top:0;height:3.4cqw;padding:0 2cqw;background:#FFB81C;font:400 1.5cqw/3.6cqw var(--pixel);color:#5A3A00}
.pg{position:absolute;left:3cqw;right:3cqw;height:7cqw;background:#fff;box-shadow:inset 0 0 0 .4cqw #E3DAC4}
.pg.p1{top:6.5cqw;animation-delay:8.4s!important}.pg.p2{top:14.5cqw;animation-delay:8.7s!important}.pg.p3{top:22.5cqw;animation-delay:9s!important}
.pg::before{content:"";position:absolute;left:1cqw;top:1cqw;bottom:1cqw;width:8cqw;background:#5B3FD6}
.pg.p2::before{background:#1068DC}.pg.p3::before{background:#2E9E6B}
.pg::after{content:"";position:absolute;left:12cqw;right:1.6cqw;top:2cqw;height:1cqw;background:#E3DAC4;box-shadow:0 2.2cqw 0 #E3DAC4}
.stamp{position:absolute;right:-3cqw;bottom:2cqw;font:400 2.6cqw var(--pixel);color:#E0337E;border:.5cqw solid #E0337E;padding:1cqw 1.4cqw;transform:rotate(-12deg);background:rgba(255,255,255,.85);animation:pbStamp 16s infinite both!important;animation-delay:9.6s!important}
@keyframes pbStamp{0%{opacity:0;transform:rotate(-12deg) scale(2.4)}2%,100%{opacity:1;transform:rotate(-12deg) scale(1)}}
.pb-ck{list-style:none;margin:0;padding:0;display:grid;gap:2cqw;animation:none!important}
.pb-ck li{font:700 3.3cqw var(--display);display:flex;align-items:center;gap:1.6cqw}
.pb-ck li::before{content:"";flex:none;width:3cqw;height:3cqw;background:#7CF29A;box-shadow:inset 0 -.6cqw 0 #2E9E6B}
.pb-ck li:nth-child(1){animation-delay:8.5s}.pb-ck li:nth-child(2){animation-delay:8.9s}.pb-ck li:nth-child(3){animation-delay:9.3s}
.pb-fan{position:relative;flex:none;width:44cqw;height:40cqw;animation:none!important}
.pb-fan img{position:absolute;top:2cqw;width:17cqw;aspect-ratio:4/5;object-fit:cover;border:.5cqw solid #fff;box-shadow:0 2cqw 3cqw rgba(0,0,0,.5)}
.pb-fan img:nth-child(1){left:0;transform:rotate(-12deg);animation-delay:12.2s}.pb-fan img:nth-child(2){left:9cqw;top:0;transform:rotate(-4deg);animation-delay:12.4s}
.pb-fan img:nth-child(3){left:18cqw;top:0;transform:rotate(4deg);animation-delay:12.6s}.pb-fan img:nth-child(4){left:27cqw;transform:rotate(12deg);animation-delay:12.8s}
.pb-tx.r{animation-delay:12.3s}
.pb-p{display:inline-block;margin-top:2.4cqw;font:700 2.8cqw var(--display);color:#0B0720;background:#FFD24A;padding:.8cqw 1.8cqw}
.pb-pip{position:absolute;left:50%;bottom:3cqw;transform:translateX(-50%);display:flex;gap:1cqw}
.pb-pip i{width:1.4cqw;height:1.4cqw;background:rgba(255,255,255,.25);animation:pbP 16s steps(1) infinite}
.pb-pip i:nth-child(2){animation-delay:4s}.pb-pip i:nth-child(3){animation-delay:8s}.pb-pip i:nth-child(4){animation-delay:12s}
@keyframes pbP{0%,24.9%{background:#FFD24A}25%,100%{background:rgba(255,255,255,.25)}}
@media (prefers-reduced-motion:reduce){.sc,.sc *{animation:none!important}.s1{opacity:1}}
/* courses + course page: plain banner with a pixel frame */
.ctb{margin-top:8px}
.ctb-f{position:relative;display:block;aspect-ratio:2/1;box-shadow:0 0 0 6px #0B0720,0 0 0 12px #5B3FD6,0 0 0 18px #0B0720,14px 14px 0 18px #FFD24A;margin:18px;transition:transform .15s steps(2)}
a.ctb-f:hover{transform:translate(-3px,-3px)}
.ctb-f.wide{aspect-ratio:2/1}
.ctb-b{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin:44px 0 0}
.ctb-b b{display:block;font:800 1.6rem var(--display)}.ctb-b span{color:var(--mute)}.ctb-b em{font-style:normal;color:var(--ink);font-weight:700}
.px-bnr{width:100%}
.pxln{position:sticky;top:60px;z-index:50;background:rgba(11,11,42,.9);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);border-bottom:1px solid rgba(255,255,255,.1)}
.pxln-in{display:flex;align-items:center;gap:16px;height:52px}
.pxln b{font:700 1.1rem var(--display);color:#fff}.pxln span{color:#9AA0C8;font-size:.9rem;margin-right:auto}
.pxln a{font:700 .95rem var(--display);color:#0B0720;background:#FFD24A;padding:7px 16px;border-radius:999px;text-decoration:none}
.pxln a:hover{background:#fff}
.why summary{color:#FFD24A!important}.why ul{margin:6px 0 12px;padding-left:20px;color:#C9CDE8;display:grid;gap:6px}.why b{color:#fff}
/* results text */
.pr-t p small{display:block;font:500 .85rem var(--display);color:rgba(255,255,255,.7);margin-top:4px}
/* seniors: text controls, oval appears on hover */
.mc-u button{background:none!important;box-shadow:none!important;-webkit-backdrop-filter:none;backdrop-filter:none;color:rgba(255,255,255,.65);transition:background .2s,color .2s}
.mc-u button:hover{background:rgba(255,255,255,.12)!important;color:#fff}
.mc-u button[aria-pressed="true"]{background:none!important;color:#fff!important;text-decoration:underline;text-decoration-color:#FFD24A;text-decoration-thickness:2px;text-underline-offset:8px}
.mc-u button[aria-pressed="true"] b{color:#FFD24A!important}
.lk{display:inline-block;margin-top:18px;color:#fff;font:600 1.05rem var(--display);text-decoration:none;padding:10px 20px;border-radius:999px;transition:background .2s,color .2s}
.lk:hover{background:#fff;color:#0A0716}
.mc-c{transition:transform .9s cubic-bezier(.2,.8,.2,1),opacity .6s,filter .6s}
/* home closing */
.end{padding:12px 12px 0}
.end-in{background:#F5F5F7;text-align:center;padding:clamp(64px,8vw,110px) 20px}
.end h2{font:800 clamp(2rem,4.4vw,3.4rem)/1.15 var(--display);letter-spacing:-.02em}
.end p{color:var(--mute);margin-top:12px;font-size:1.1rem}
.end-b{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:28px}
.end-b a{display:inline-flex;align-items:center;min-height:50px;padding:0 26px;border-radius:999px;font:600 1.05rem var(--display);text-decoration:none}
.e1{background:#1D1D1F;color:#fff}.e1:hover{background:#000}.e2{background:#06C755;color:#fff}.e2:hover{filter:brightness(.95)}
/* feed: video fills the screen; volume slider */
.yt .tk-stage{position:absolute!important;inset:0!important;padding:0!important;z-index:0}
.yt .tk-frame{width:100%!important;height:100%!important;max-width:none!important;border-radius:0!important;aspect-ratio:auto!important}
.yt .tk-frame .tk-shot,.yt .tk-frame .tk-vid{object-fit:cover!important;width:100%;height:100%}
.yt .tk-shade{z-index:1}
.yt .tk-cap,.yt .tk-rail,.yt .tk-hint{z-index:2}
.tk-vol{position:absolute;right:20px;top:58px;z-index:6;display:flex;align-items:center;gap:8px;padding:8px 12px;border-radius:999px;background:rgba(0,0,0,.45);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);color:#fff;cursor:pointer}
.tk .tk-vol svg{width:20px!important;height:20px!important;flex:none}
.tk-vol input{width:110px;accent-color:#FFD24A;--v:0%}
/* transitions: courses = style montage */
.cs{position:absolute;inset:0;overflow:hidden}
.cs-f{position:absolute;inset:0;display:grid;place-items:center;opacity:0;animation:csF .09s var(--d) steps(1)}
@keyframes csF{0%,99%{opacity:1}100%{opacity:0}}
.cs-f b{font:800 clamp(5rem,18vw,15rem)/1 var(--display)}
.cs-f.f1{background:#5B3FD6}.cs-f.f1 b{color:#FFD24A;font-family:var(--pixel),var(--display);text-shadow:.06em .06em 0 #E0337E}
.cs-f.f2{background:#E60012;background-image:linear-gradient(115deg,transparent 46%,#0B0B0F 46% 60%,transparent 60%)}.cs-f.f2 b{color:#fff;transform:skewX(-14deg) rotate(-6deg);-webkit-text-stroke:4px #0B0B0F;paint-order:stroke fill}
.cs-f.f3{background:#1068DC}.cs-f.f3 b{color:#fff;text-shadow:4px 4px 0 #0B1640,8px 8px 0 #0B1640,12px 12px 0 #0B1640}
.cs-f.f4{background:#0D1117}.cs-f.f4 b{color:#3FB950;font-family:ui-monospace,Menlo,monospace;font-size:clamp(3rem,11vw,9rem)}
.cs-f.f5{background:#FFF1D6}.cs-f.f5 b{color:transparent;-webkit-text-stroke:3px #B26A00}
.cs-end{position:absolute;inset:0;display:grid;place-items:center;align-content:center;gap:14px;background:#0B0720;opacity:0;animation:csE .2s .6s forwards}
@keyframes csE{to{opacity:1}}
.cs-end small{font:600 clamp(1rem,2vw,1.3rem) var(--display);color:#FFD24A}
.cs-end b{font:800 clamp(4.4rem,14vw,11rem)/1 var(--display);color:#fff;animation:csB .5s .6s cubic-bezier(.2,1.4,.4,1) both}
@keyframes csB{from{transform:scale(1.6);filter:blur(10px)}}
.pt.out .cs{animation:csOut .55s cubic-bezier(.7,0,.2,1) forwards}
.pt.out .cs-f{animation:none}
.pt.out .cs-end{opacity:1;animation:none}
@keyframes csOut{from{clip-path:inset(0 0 0 0)}to{clip-path:inset(50% 0 50% 0)}}
/* activity: burst of our own stickers */
.ev-s{position:absolute;left:50%;top:50%;width:clamp(70px,10vw,130px);margin:-60px 0 0 -60px;opacity:0;animation:evS .7s var(--dl) cubic-bezier(.2,1.3,.4,1) forwards;filter:drop-shadow(0 10px 12px rgba(0,0,0,.35))}
@keyframes evS{from{opacity:0;transform:translate(0,0) scale(.2) rotate(0)}to{opacity:1;transform:translate(var(--tx),var(--ty)) scale(1) rotate(var(--rot))}}
.pt.out .ev-w{animation:evW .45s cubic-bezier(.6,0,.4,1) forwards}
.pt.out .ev-c{animation:none;clip-path:circle(150% at 50% 50%)}
.pt.out .ev-s{opacity:1;transform:translate(var(--tx),var(--ty)) rotate(var(--rot));animation:none}
@keyframes evW{to{opacity:0;transform:scale(1.15)}}
.ev-w{position:absolute;inset:0}
/* works: trophy hamster + flashes */
.t5-tr{position:absolute;left:50%;bottom:-40%;width:clamp(100px,11vw,160px);transform:translateX(-50%);animation:t5up .7s .45s cubic-bezier(.2,1.2,.4,1) forwards;filter:drop-shadow(0 0 30px rgba(255,214,120,.6))}
@keyframes t5up{to{bottom:3%}}
.v-works .t5-hof{top:36%}
.t5-fl{position:absolute;inset:0;background:#fff;opacity:0;animation:t5fl 1.1s .5s steps(1)}
@keyframes t5fl{0%{opacity:.5}6%{opacity:0}40%{opacity:.35}44%{opacity:0}}
.pt.out .t5-tr{bottom:3%;animation:fadeOut .25s forwards}
@media (max-width:600px){.ctb-f{margin:12px;box-shadow:0 0 0 4px #0B0720,0 0 0 8px #5B3FD6,0 0 0 12px #0B0720,8px 8px 0 12px #FFD24A}.tk-vol{top:auto;bottom:16px;left:16px;right:auto}.tk-vol input{width:80px}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v11.html','w').write(s)
print('v11 ok',len(s))
