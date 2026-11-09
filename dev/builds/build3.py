import re
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
B=open(D+'index_v1_backup.html').read()
exec(open(D+'v2parts/build.py').read())          # rebuilds v2.html from parts
s=open('/home/claude/hamsterhub-home/v2.html').read()
LINE='https://page.line.me/jkm4247u?openQrModal=true'
def rep(a,b,c=1):
    global s
    assert a in s,a[:90];s=s.replace(a,b,c)
def cut(a,b,new=''):
    global s
    i=s.index(a);j=s.index(b,i);s=s[:i]+new+s[j:]
def bcut(a,b):
    i=B.index(a);return B[i:B.index(b,i)]

# ---------- old CSS we bring back (banners, deck, pods, transitions, hero stage) ----------
bstyle=B[B.index('<style>'):B.index('</style>')]
keep=('.f4{','.px-bn','.pxv','.bn{','.banners','.screen{','.bar8','.b8','.pbtn','.blink','.afo-','.cd{','.cd ','.row-st','.sbtn',
      '.dkx','.dk-','.deck','.dc','.flap','.pt','.hx-say','.pod','.bubble','.f4i','@keyframes')
lines=bstyle.split('\n');old=[];i=0
while i<len(lines):
    l=lines[i]
    if l.startswith(keep):
        while l.count('{')>l.count('}') and i+1<len(lines):
            i+=1;l+='\n'+lines[i]
        old.append(l)
    i+=1
oldcss='\n'.join(old)
# ---------- HOME ----------
# hero copy + hamster stage instead of the unclear reel
cut('<p class="h-kick rv">Hamster Hub</p>','<div class="btns rv">','''<p class="h-kick rv">Hamster Hub</p>
    <h1 class="rv"><span class="nw">เปลี่ยนไอเดีย</span><span class="nw">ของน้อง</span><br>ให้เป็น<em>ผลงานจริง</em></h1>
    <p class="h-sub rv">ผลงานที่ใช้ได้จริง ขายได้จริง และพาไปถึงมหาวิทยาลัยที่ใช่ ด้วยเกม แอป และ IoT</p>
    ''')
cut('  <figure class="h-reel rv">','  </section>','''  <div class="wrap"><div class="hx rv" id="hx"><div class="hx3" id="hx3" aria-hidden="true"><canvas id="hxCanvas"></canvas><div class="hx-say" id="hxSay"></div></div>
    <p class="hx-tip">น้องหนู 3 ตัวนี้กำลังเรียน เกม แอป และ IoT ลองคลิก หรือกดค้างแล้วลากดูสิ</p></div></div>
''')
# what parents get (with real images) — after paths
rep('  <section class="proof">','''  <section class="gain"><div class="wrap">
    <h2 class="sec-h rv">ทำเกม ทำแอป แล้วน้องได้อะไร</h2>
    <p class="sec-sub rv">ไม่ได้แค่เล่นคอม ทุกผลงานฝึกทักษะที่ใช้ได้จริงทั้งในมหาวิทยาลัยและการทำงาน</p>
    <div class="gain-g">
      <figure class="rv"><img src="img/work-eugation-strike.webp" alt="" loading="lazy"><figcaption><b>คิดแก้ปัญหาเป็นขั้นตอน</b><span>Eugation Strike ใช้สมการคณิตศาสตร์ยิงศัตรู น้องต้องเข้าใจเรื่องที่สอนก่อนถึงจะออกแบบเกมได้</span></figcaption></figure>
      <figure class="rv"><img src="img/work-stressstrike.webp" alt="" loading="lazy"><figcaption><b>เขียนโปรแกรม ต่ออุปกรณ์ และใช้ AI</b><span>StressStrike มีที่จับวัดแรงกำ (IoT) ต่อกับเกม แล้วเก็บข้อมูลไปวิเคราะห์</span></figcaption></figure>
      <figure class="rv"><img src="img/s-showcase1.webp" alt="" loading="lazy"><figcaption><b>นำเสนอและทำงานเป็นทีม</b><span>ทุกงานจบด้วยการนำเสนอต่อกรรมการหรืออาจารย์มหาวิทยาลัย</span></figcaption></figure>
      <figure class="rv"><img src="img/dek69-12.webp" alt="" loading="lazy" style="object-position:50% 20%"><figcaption><b>พอร์ตที่ใช้ยื่นได้จริง</b><span>รุ่นพี่ DEK69 ใช้ผลงานเหล่านี้ยื่นรอบ Portfolio ติดแล้ว 48 คน</span></figcaption></figure>
    </div>
  </div></section>

  <section class="proof">''')
# paths -> old pod display (hamster hop + bubble)
cut('    <div class="tiles">','  </div></section>\n\n  <section class="gain">','''    <div class="f4 p3">
      <a class="f4i rv" href="#portex" style="--bg:#FFF1D6;--ac:#B26A00"><span class="pod"><img src="img/n-grad.webp" alt="" loading="lazy"><i class="bubble">ไปมหาลัยกัน!</i></span><span class="k">พอร์ตโฟลิโอ</span><span class="w">ยื่นมหาลัย</span><span class="d">ทำผลงานเก็บเข้าพอร์ต ซ้อมนำเสนอกับอาจารย์มหาวิทยาลัย</span><span class="pf">รุ่นพี่ DEK69 ติดแล้ว 48 คน</span><span class="go">ดู Port Express <b>→</b></span></a>
      <a class="f4i rv" href="#works" data-pane="real" style="--bg:#E3F3FF;--ac:#1D5FB8"><span class="pod"><img src="img/n-build.webp" alt="" loading="lazy"><i class="bubble">ขายได้จริง!</i></span><span class="k">สตาร์ทอัพ</span><span class="w">สร้างธุรกิจ</span><span class="d">4 ขั้นจากไอเดีย สู่ผลงานที่มีคนใช้และมีรายได้</span><span class="pf">Mr. City ขายให้สวนสัตว์สงขลาแล้ว</span><span class="go">ผลงานที่ใช้งานจริง <b>→</b></span></a>
      <a class="f4i rv" href="#activity" style="--bg:#FFE6EE;--ac:#B23A68"><span class="pod"><img src="img/n-win.webp" alt="" loading="lazy"><i class="bubble">ลุยเลย!</i></span><span class="k">การแข่งขัน</span><span class="w">ลงเวทีจริง</span><span class="d">ค่าย Game Jam และการแข่งขันที่จัดร่วมกับ สจล.</span><span class="pf">12 ผลงานเข้ารอบชิง NSC</span><span class="go">ดูกิจกรรม <b>→</b></span></a>
    </div>
''')
# "open now" -> "coming up" with old banner display
cut('  <section class="open">','  <section class="sen">','''  <section class="open"><div class="wrap">
    <h2 class="sec-h rv">เร็วๆ นี้ที่ Hamster Hub</h2>
    <div class="banners">
      <a class="bn px-bn rv" href="#portex" aria-label="Port Express คอร์สทำพอร์ต 2 เดือน">
        <div class="screen"><video class="pxv" src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video></div>
        <div class="bar8"><div><p class="blink">● เปิดรับสมัคร</p><p class="b8t">Port Express คอร์สทำพอร์ตเกม 2 เดือน สำหรับ ม.6</p><p class="b8s">เริ่ม 1 ธ.ค. เรียน จ พ ศ <span>5,990.-</span></p></div><span class="pbtn gold">▶ ดูรายละเอียด</span></div>
      </a>
      <div class="bn afo-bn rv">
        <span class="afo-tag">กิจกรรมถัดไป · รอบชิงชนะเลิศ</span>
        <div class="afo-hd"><img class="afo-logo" src="img/k-afo-logo.webp" alt="All for One University" loading="lazy"><img class="afo-ic i0" src="img/afo-ic0.webp" alt="" aria-hidden="true"><img class="afo-ic i1" src="img/afo-ic1.webp" alt="" aria-hidden="true"><img class="afo-ic i2" src="img/afo-ic2.webp" alt="" aria-hidden="true"></div>
        <p class="afo-when">14 พ.ย. 2569 ที่ IoTE สจล. ลาดกระบัง</p>
        <div class="cd" aria-label="นับถอยหลังถึงวันแข่ง"><div><b id="cdD">0</b><span>วัน</span></div><div><b id="cdH">0</b><span>ชั่วโมง</span></div><div><b id="cdM">0</b><span>นาที</span></div></div>
        <div class="row-st"><a class="sbtn" href="#activity">ดูกิจกรรมทั้งหมด</a><a class="sbtn alt" href="https://www.hamsterhub.co/allforone" target="_blank" rel="noopener">รายละเอียดงาน</a></div>
      </div>
    </div>
  </div></section>

''')
# seniors -> old deck (auto-plays) with modern uni numbers
cut('  <section class="sen">','  <section class="hof">',bcut('  <section class="dkx">','  <section class="band b-hof c">').replace('<a class="ibtn rv" href="#works" data-go="dek">ดูรุ่นพี่ทั้งหมด <span>→</span></a>','<a class="more rv" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a>').replace('<h2 class="rv">รุ่นพี่ <span class="g">48 คน</span><br>ไปถึงคณะในฝันแล้ว</h2>','<h2 class="rv">รุ่นพี่ 48 คน<br>ไปถึงคณะที่ใช่แล้ว</h2>')+'\n')
# hall of fame block removed from home
cut('  <section class="hof">','  <section class="ptn">','')
# ---------- COURSES: cards with real images ----------
cut('    <section class="ct-list">','    <section class="ct-help">','''    <section class="ct-list"><h2>คอร์สอื่นของ Hamster Hub</h2><p>เปิดรับเป็นรอบ ภาพคือรุ่นพี่ที่เรียนคอร์สนั้นแล้วติดมหาวิทยาลัย</p><div class="cgrid" id="crows"></div></section>
''')
rep("""  $('#crows').innerHTML=C.map(function(c){var al=G.filter(function(x){return x[4]===c[0]}),us=al.map(function(x){return UN[x[2]]}).filter(function(v,k,a){return a.indexOf(v)===k});
    return '<div class="crow"><div><b>'+c[0]+'</b><p>'+c[1]+'</p>'+(al.length?'<p class="al">รุ่นพี่จากคอร์สนี้ติด '+us.join(' ')+'</p>':'')+'</div><a href="'+LINE+'" target="_blank" rel="noopener">แจ้งเตือนเมื่อเปิดรอบ</a></div>'}).join('');""",
"""  var CB=['#FFF1D6','#E3F3FF','#FFE6EE','#E6F7EC','#EEE8FF','#FFF6E2'];
  $('#crows').innerHTML=C.map(function(c,ci){var al=G.filter(function(x){return x[4]===c[0]}),us=al.map(function(x){return UN[x[2]]}).filter(function(v,k,a){return a.indexOf(v)===k});
    var im=al.slice(0,3).map(function(x,k){return '<img src="img/dek69-'+x[0]+'.webp" alt="" loading="lazy" style="--k:'+(k-(Math.min(al.length,3)-1)/2)+'">'}).join('');
    return '<div class="cc"><div class="cc-m" style="background:'+CB[ci]+'">'+im+'<span class="cc-st">รอบถัดไป</span></div><div class="cc-b"><b>'+c[0]+'</b><p>'+c[1]+'</p>'+(al.length?'<p class="al">รุ่นพี่ '+al.length+' คนจากคอร์สนี้ติด '+us.join(' ')+'</p>':'')+'<a href="'+LINE+'" target="_blank" rel="noopener">แจ้งเตือนเมื่อเปิดรอบ</a></div></div>'}).join('');""")
# ---------- ACTIVITY: event cards with images ----------
rep("function alist(t){$('#acl').innerHTML=ACT.filter(function(a){return t==='all'||a[3]===t}).map(function(a){return '<div class=\"arow\"><span class=\"d\">'+a[0]+'</span><div><b>'+a[1]+'</b><p>'+a[2]+'</p></div><span class=\"tg\"'+(a[4]?' style=\"background:#FFB81C;color:#0B1640\"':'')+'>'+(a[4]?'กำลังจะมาถึง':a[3])+'</span></div>'}).join('')}",
"""var AIMG={'All for One University รอบชิงชนะเลิศ':'k-afo-logo','IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'},ACOL={'ค่าย':['#FFF1D6','#B26A00'],'เวิร์กชอป':['#E3F3FF','#1D5FB8'],'แข่งขัน':['#FFE6EE','#B23A68'],'โชว์ผลงาน':['#EEE8FF','#5B3FD6'],'โครงการ':['#E6F7EC','#1E7A4C']};
  function alist(t){$('#acl').innerHTML=ACT.filter(function(a){return t==='all'||a[3]===t}).map(function(a){var im=AIMG[a[1]],c=ACOL[a[3]];
    return '<article class="ev'+(a[4]?' up':'')+'"><div class="ev-m" style="background:'+c[0]+';color:'+c[1]+'">'+(im?'<img src="img/'+im+'.webp" alt="" loading="lazy"'+(im==='k-afo-logo'?' class="logo"':'')+'>':'<span class="ev-t">'+a[1]+'</span>')+'<span class="ev-d">'+a[0]+'</span></div><div class="ev-b"><span class="tg" style="color:'+c[1]+'">'+(a[4]?'กำลังจะมาถึง':a[3])+'</span><b>'+a[1]+'</b><p>'+a[2]+'</p></div></article>'}).join('')}""")
# ---------- WORKS: open on the feed first ----------
rep('<button type="button" data-pane="hof" aria-current="true">','<button type="button" data-pane="shorts" aria-current="true" data-first="1">'+ic['shorts']+'ดูแบบเลื่อน</button>\n      <button type="button" data-pane="hof">')
rep('      <button type="button" data-pane="shorts">'+ic['shorts']+'ดูแบบเลื่อน</button>\n','')
rep('<section class="yt-pane on" data-p="hof">','<section class="yt-pane" data-p="hof">')
rep('<section class="yt-pane" data-p="shorts">','<section class="yt-pane on" data-p="shorts">')
rep("var pp=pendingPane||['hof']","var pp=pendingPane||['shorts']")
# ---------- JS: bring back hero, deck, countdown, page transitions ----------
hero=bcut('  /* hero: three.js 2.5D hamster hub on a giant maker desk.','  /* login: hamster pops')
hero=hero.replace("new IntersectionObserver(function(es){play(es[0].isIntersecting&&!reduce)}).observe(hx);","new IntersectionObserver(function(es){play(es[0].isIntersecting&&!reduce&&!!document.querySelector('[data-view=\"home\"].on'))}).observe(hx);")
deck=bcut('  /* DEK69 deck: holo poster on top','  /* Hall of Fame coverflow')
js_add='''
  var inView=function(el){var r=el.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight&&!document.hidden&&document.querySelector('[data-view="home"].on')};
'''+deck+hero+'''
  (function(){function f(){var ms=new Date('2026-11-14T09:00:00+07:00')-new Date();if(ms<0)ms=0;var d=Math.floor(ms/864e5),h=Math.floor(ms/36e5)%24,m=Math.floor(ms/6e4)%60;
    [['#cdD',d],['#cdH',h],['#cdM',m]].forEach(function(x){var e=$(x[0]);if(e)e.textContent=x[1]})}f();setInterval(f,3e4)})();
  /* works: if nobody scrolls the feed, nudge it so it is obvious more is below */
  (function(){var feed=document.querySelector('.tk-feed');if(!feed||reduce)return;var moved=false;feed.addEventListener('scroll',function(){if(feed.scrollTop>40)moved=true},{passive:true});
    setInterval(function(){if(moved||!document.querySelector('[data-p="shorts"].on')||!document.querySelector('[data-view="works"].on'))return;feed.classList.remove('nudge');void feed.offsetWidth;feed.classList.add('nudge')},3800)})();
'''
rep("  /* router */",js_add+"  /* router */")
# transitions
rep('<main id="main">','<div class="pt" id="pt" aria-hidden="true"></div>\n<main id="main">')
pt=bcut("  var lastXY=[innerWidth/2,innerHeight/2];","  var first=true;function route()")
pt=pt.replace("else if(v==='works'){h='<span class=\"pt-cl l\"></span><span class=\"pt-cl r\"></span><span class=\"pt-gl\"></span>';for(var k=0;k<14;k++)h+='<em class=\"pt-sp\" style=\"left:'+(30+Math.random()*40).toFixed(1)+'%;top:'+(38+Math.random()*24).toFixed(1)+'%;--dl:'+(.25+Math.random()*.5).toFixed(2)+'s\">✦</em>';h+='<b class=\"pt-hof\"><small>Hamster Hub · Class of 2026</small>Hall of Fame</b>'}",
 "else if(v==='works'){h='<span class=\"pt-sw\"></span><span class=\"pt-ph\"><i></i><i></i><i></i></span>'}")
pt=pt.replace("if(v==='courses'){","if(v==='courses'||v==='portex'){")
rep("  addEventListener('hashchange',show);show();",pt+"""  var first=true;function route(){var v=(location.hash||'#home').slice(1);if(views.indexOf(v)<0)v='home';
    if(first||reduce){first=false;show();return}
    clearTimeout(ptT);ptBuild(v);var hold=v==='activity'?700:620;ptT=setTimeout(function(){show();pt.classList.add('out');ptT=setTimeout(function(){pt.className='pt';pt.innerHTML=''},1000)},hold)}
  addEventListener('hashchange',route);route();""")
# hero needs three.js
rep('<script>\n(function(){','<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n<script>\n(function(){')
# remove now-unused home grid code safely
rep("var hg=$('#hgrid');if(hg)","var hg=$('#hgrid');if(hg&&0)")
rep("  $('#srow').innerHTML=mix.map(function(i){return sfig(G[i])}).join('');","  if($('#srow'))$('#srow').innerHTML=mix.map(function(i){return sfig(G[i])}).join('');")
rep("ufilter($$('#ulg button'),function(){return $$('#srow figure')});","")
rep("$('#sPrev').addEventListener('click',function(){$('#srow').scrollBy({left:-480,behavior:'smooth'})});$('#sNext').addEventListener('click',function(){$('#srow').scrollBy({left:480,behavior:'smooth'})});","")
# ---------- CSS ----------
newcss=oldcss+'''
/* ===== v3 ===== */
.hx{position:relative;margin-top:40px}
.hx3{position:relative;height:clamp(300px,42vw,520px);border-radius:24px;overflow:hidden;background:#F3E6CF}
.hx3 canvas{position:absolute;inset:0;width:100%;height:100%;display:block}
.hx-say{position:absolute;left:0;top:0;z-index:3;background:#fff;color:#0B1640;font:700 1rem var(--display);padding:8px 13px;border-radius:14px;white-space:nowrap;box-shadow:0 10px 24px -10px rgba(0,0,0,.35);opacity:0;pointer-events:none;margin:-40px 0 0 -10px}
.hx-say.on{animation:sayIn 1.6s cubic-bezier(.2,.8,.25,1.4) forwards}
.hx-tip{color:var(--mute);font-size:.92rem;text-align:center;margin-top:12px}
.p3{grid-template-columns:repeat(3,minmax(0,1fr))!important;margin-top:56px}
.nw{white-space:nowrap;display:inline-block}
.pbtn{white-space:nowrap}
@media(max-width:700px){.f4.p3{grid-template-columns:1fr!important;gap:28px}.f4.p3 .f4i img{max-height:150px;width:auto}.bar8{flex-wrap:wrap;gap:10px}}
.f4i .k{font:600 .95rem var(--display);color:var(--ac)}
.f4i .pf{font:600 .95rem var(--display);color:var(--ink);background:var(--bg);padding:4px 12px;border-radius:999px}
.gain{padding:clamp(80px,10vw,120px) 0;background:var(--alt)}
.gain-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:44px}
.gain-g figure{margin:0;background:#fff;border-radius:20px;overflow:hidden}
.gain-g img{width:100%;aspect-ratio:4/3;object-fit:cover}
.gain-g figcaption{padding:18px 18px 22px}
.gain-g b{display:block;font:700 1.15rem/1.35 var(--display)}
.gain-g span{display:block;color:var(--mute);font-size:.95rem;margin-top:6px;line-height:1.55}
.open .banners{margin-top:40px}
.afo-tag{font-size:.9rem!important}
.dkx .more{display:inline-block;margin-top:8px}
.cgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:20px}
.cc{border-radius:20px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px #ECECF0;display:flex;flex-direction:column}
.cc-m{position:relative;height:210px;display:flex;justify-content:center;align-items:flex-end;overflow:hidden}
.cc-m img{width:120px;aspect-ratio:4/5;object-fit:cover;border-radius:10px;margin:0 -16px -26px;transform:rotate(calc(var(--k) * 8deg)) translateY(calc(var(--k) * var(--k) * 10px));box-shadow:0 14px 26px -14px rgba(0,0,0,.5);transition:transform .4s cubic-bezier(.3,1.5,.5,1)}
.cc:hover .cc-m img{transform:rotate(calc(var(--k) * 12deg)) translateY(calc(var(--k) * var(--k) * 10px - 10px))}
.cc-st{position:absolute;left:14px;top:14px;background:rgba(11,22,64,.85);color:#fff;font:600 .8rem var(--display);padding:4px 10px;border-radius:999px}
.cc-b{padding:18px 20px 22px;display:flex;flex-direction:column;gap:4px;flex:1}
.cc-b b{font:700 1.3rem var(--display)}
.cc-b p{color:var(--mute)}
.cc-b .al{color:var(--ink);font-size:.9rem}
.cc-b a{margin-top:auto;align-self:flex-start;color:var(--line);font-weight:700;text-decoration:none;border:1.5px solid var(--line);border-radius:999px;padding:7px 14px;margin-top:12px}
.cc-b a:hover{background:var(--line);color:#fff}
.ac-list{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.ev{border-radius:20px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px #ECECF0;display:flex;flex-direction:column;transition:transform .3s,box-shadow .3s}
.ev:hover{transform:translateY(-4px);box-shadow:0 20px 40px -24px rgba(0,0,0,.35)}
.ev-m{position:relative;aspect-ratio:16/9;display:grid;place-items:center;overflow:hidden}
.ev-m img{width:100%;height:100%;object-fit:cover}
.ev-m img.logo{width:70%;height:auto;object-fit:contain}
.ev-t{font:800 clamp(1.3rem,2vw,1.7rem)/1.2 var(--display);text-align:center;padding:0 18px}
.ev-d{position:absolute;left:12px;bottom:12px;background:#fff;color:var(--ink);font:700 .85rem var(--display);padding:5px 10px;border-radius:8px;box-shadow:0 4px 12px -6px rgba(0,0,0,.3)}
.ev-b{padding:16px 18px 20px}
.ev-b .tg{font:700 .82rem var(--display)}
.ev-b b{display:block;font:700 1.15rem/1.35 var(--display);margin-top:2px}
.ev-b p{color:var(--mute);font-size:.95rem;margin-top:4px}
.ev.up{box-shadow:0 0 0 2px var(--gold)}
/* nav: four small personalities */
.nav-in>a.v:nth-of-type(1)::before{content:"";position:absolute;left:-12px;top:50%;width:7px;height:9px;margin-top:-5px;background:#5B3FD6;clip-path:polygon(0 0,100% 50%,0 100%);opacity:0}
.nav-in>a.v:nth-of-type(1):hover::before{opacity:1;animation:pxBlink .5s steps(2) infinite}
.nav-in>a.v:nth-of-type(1):hover{text-shadow:2px 2px 0 #D6D0FF}
.nav-in>a.v:nth-of-type(2)::before{content:"";position:absolute;right:-10px;top:4px;width:6px;height:6px;border-radius:50%;background:#FF4D6D;transform:scale(0);transition:transform .3s cubic-bezier(.3,1.8,.5,1)}
.nav-in>a.v:nth-of-type(2):hover::before{transform:scale(1)}
.nav-in>a.v:nth-of-type(3)::before{content:"";position:absolute;left:-14px;top:50%;width:10px;height:10px;margin-top:-5px;border-radius:3px;background:#0B0B0F;clip-path:polygon(25% 10%,90% 50%,25% 90%);transform:scale(0);transition:transform .3s cubic-bezier(.3,1.8,.5,1)}
.nav-in>a.v:nth-of-type(3):hover::before{transform:scale(1)}
.nav-in>a.v:nth-of-type(4)::before{content:"";position:absolute;left:50%;top:-11px;width:22px;height:9px;margin-left:-11px;background:url(img/n-peek.webp) 50% 0/100% auto no-repeat;transform:translateY(8px);opacity:0;transition:transform .3s cubic-bezier(.3,1.8,.5,1),opacity .2s}
.nav-in>a.v:nth-of-type(4):hover::before{transform:none;opacity:1}
@keyframes pxBlink{50%{opacity:.2}}
/* works transition: a phone swipe */
.pt-sw{position:absolute;inset:0;background:#0F0F0F;transform:translateY(100%);animation:swIn .5s cubic-bezier(.7,0,.2,1) forwards}
.pt.out .pt-sw{animation:swOut .55s cubic-bezier(.7,0,.2,1) forwards;transform:none}
@keyframes swIn{to{transform:none}}@keyframes swOut{to{transform:translateY(-100%)}}
.pt-ph{position:absolute;left:50%;top:50%;width:150px;height:260px;margin:-130px 0 0 -75px;border-radius:24px;border:3px solid #fff;overflow:hidden;opacity:0;animation:fadeIn .2s .3s forwards}
.pt-ph i{display:block;height:100%;background:linear-gradient(160deg,#FFB81C,#FF4D6D);animation:phs .5s .35s cubic-bezier(.7,0,.2,1) forwards}
.pt-ph i:nth-child(2){background:linear-gradient(160deg,#1068DC,#5B3FD6)}.pt-ph i:nth-child(3){background:linear-gradient(160deg,#2E9E6B,#0B1640)}
@keyframes phs{to{transform:translateY(-100%)}}
.pt.out .pt-ph{animation:fadeOut .2s forwards;opacity:1}
/* feed: no static peek; a nudge instead */
.yt .tk{--tk-ih:var(--tk-h)}.yt .tk-item{margin-bottom:0!important;border-radius:0!important}
.yt .tk-feed.nudge{animation:nudge 1s cubic-bezier(.3,.7,.3,1)}
@keyframes nudge{30%{transform:translateY(-46px)}55%{transform:translateY(0)}72%{transform:translateY(-14px)}100%{transform:none}}
@media (max-width:1000px){.p3{grid-template-columns:minmax(0,1fr)!important}.gain-g{grid-template-columns:repeat(2,minmax(0,1fr))}.cgrid,.ac-list{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:900px){.banners{grid-template-columns:minmax(0,1fr)!important}.dk-in{grid-template-columns:minmax(0,1fr)!important}}
@media (max-width:600px){.gain-g,.cgrid,.ac-list{grid-template-columns:minmax(0,1fr)}.nav-in>a.v::before{display:none}}
'''
rep('/* ---------- footer ---------- */',newcss+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v3.html','w').write(s)
print('v3 ok',len(s))
