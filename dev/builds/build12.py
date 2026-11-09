import re
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build11.py').read())
LINE='https://page.line.me/jkm4247u?openQrModal=true'
PX='https://www.hamsterhub.co/portex-site/index.html'

# ---------- banner copy: say plainly what the child gets ----------
R=[('<b class="pb-logo">PORT<br>EXPRESS</b><p class="pb-a">คอร์สปั้นพอร์ต ยื่นมหาลัย</p><p class="pb-b">สำหรับ ม.6 ที่ยังไม่มีพอร์ต</p>',
    '<b class="pb-logo">PORT<br>EXPRESS</b><p class="pb-a">คอร์สช่วยน้อง ม.6<br>ทำพอร์ตยื่นมหาลัย</p><p class="pb-b">ไม่เคยทำผลงานมาก่อน ก็เริ่มได้</p>'),
   ('<p class="pb-h">2 เดือน ทำเกมจริง 3 งาน</p>','<p class="pb-h">ใน 2 เดือน น้องสร้างเกมเองกับมือ 3 เกม</p><p class="pb-b c">ทุกเกมคือผลงานจริง ใส่ลงแฟ้มพอร์ตได้ทันที</p>'),
   ('<figcaption>GAME 1</figcaption>','<figcaption>เกมที่ 1</figcaption>'),('<figcaption>GAME 2</figcaption>','<figcaption>เกมที่ 2</figcaption>'),('<figcaption>GAME 3</figcaption>','<figcaption>เกมที่ 3</figcaption>'),
   ('<ul class="pb-ck"><li>เกม 3 งานเข้าแฟ้ม</li><li>แฟ้มพอร์ต + Pitch Deck</li><li>ซ้อมสัมภาษณ์กับอาจารย์มหาลัย</li></ul>',
    '<div><p class="pb-h">จบคอร์ส ได้แฟ้มพอร์ตพร้อมยื่น</p><ul class="pb-ck"><li>ผลงานเกม 3 ชิ้นในแฟ้ม</li><li>สไลด์นำเสนอผลงาน</li><li>ซ้อมสัมภาษณ์กับอาจารย์มหาลัยจริง</li></ul></div>'),
   ('<p class="pb-h">รุ่นพี่ติดแล้ว 48 คน</p>','<p class="pb-h">รุ่นพี่ที่ทำแบบนี้<br>ติดมหาลัยแล้ว 48 คน</p>')]
for a,b in R: s=s.replace(a,b)

# ---------- hero: one clear promise, controls live on the machine ----------
i=s.index('      <div class="hh-b rv">');j=s.index('      <a class="gb rv"',i)
s=s[:i]+'''      <p class="hh-h rv">จบคอร์ส น้องมีแฟ้มพอร์ตพร้อมยื่นมหาลัย</p>
      <p class="hh-s rv">Port Express คอร์ส 2 เดือนสำหรับ ม.6 ที่ยังไม่มีผลงาน · เริ่ม 9 พ.ย. 2569</p>
'''+s[j:]
i=s.index('      <a class="gb rv"');j=s.index('</a>',i)+4
gb=s[i:j]
inner=gb[gb.index('<span class="gb-s">'):gb.index('<img class="gb-f"')]
s=s[:i]+'''      <div class="gb2 rv">'''+inner.replace('<span class="gb-s">','<a class="gb-s g2" href="#portex" aria-label="ดูรายละเอียดคอร์ส Port Express">').replace('<span class="gb-sl"></span></span>','<span class="gb-sl"></span></a>')+'''<img class="gb-f" src="img/console2.webp" alt="">
        <span class="gb-lcd" aria-label="ราคา 5,990 บาท จากปกติ 9,990 บาท"><b>5,990฿</b><s>9,990</s></span>
        <a class="gk k1" href="#portex"><span>ดูรายละเอียด</span></a>
        <a class="gk k2" href="'''+PX+'''" target="_blank" rel="noopener"><span>เว็บ Port Express</span></a>
        <a class="gk k3" href="'''+LINE+'''" target="_blank" rel="noopener"><span>ทัก LINE</span></a>
        <span class="gk-hint" aria-hidden="true">กดปุ่มบนเครื่องได้เลย</span>
        <span class="gbt b1"></span><span class="gbt b2"></span><span class="gbt b3"></span>
      </div>
      <div class="hh-m"><p><b>5,990 บาท</b> <s>9,990</s></p><div class="hh-a"><a class="b1" href="#portex">ดูรายละเอียด</a><a class="b2" href="'''+PX+'''" target="_blank" rel="noopener">เว็บ Port Express</a><a class="b3" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE</a></div></div>
'''+s[j:]

# ---------- home: drop the number tiles (confusing, repeated) ----------
i=s.index('<section class="pr">');j=s.index('</section>',i)+10;s=s[:i]+s[j:]

# ---------- courses: cover = the flying banner; only Port Express exists now ----------
i=s.index('<a class="ctb-f" href="#portex"');j=s.index('</a>',s.index('class="pb-pip"',i))+4
s=s[:i]+'<a class="ctb-f" href="#portex" aria-label="ดูรายละเอียด Port Express"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video></a>'+s[j:]
assert 'ctb-f" href="#portex" aria-label="ดูรายละเอียด Port Express"><video' in s
i=s.index('    <section class="ct-list">');j=s.index('    <section class="ct-help">',i);s=s[:i]+s[j:]
rep('<section class="ct-h"><h1>คอร์ส</h1><p>ทุกคอร์สจบด้วยผลงานจริงที่เอาไปใช้ได้ ทั้งยื่นมหาวิทยาลัย ลงแข่ง และต่อยอด</p></section>','<section class="ct-h"><h1>คอร์ส</h1><p>คอร์สที่เปิดรับตอนนี้ จบแล้วน้องได้ผลงานจริงที่เอาไปใช้ยื่นมหาวิทยาลัยได้</p></section>')

# ---------- activity: new event stickers ----------
rep("var MAS={'ค่าย':'n-gamer','เวิร์กชอป':'n-read','แข่งขัน':'n-win','โชว์ผลงาน':'n-walker','โครงการ':'n-maker'}","var MAS={'ค่าย':'ev-st2','เวิร์กชอป':'ev-st3','แข่งขัน':'ev-st4','โชว์ผลงาน':'ev-st1','โครงการ':'ev-st5'}")
rep('<div class="ac-soon"><img src="img/n-peek.webp" alt="" loading="lazy">','<div class="ac-soon"><img src="img/ev-st0.webp" alt="" loading="lazy">')
rep("ST=['n-win','n-gamer','n-walker','n-maker','n-read','afo-ic0','afo-ic1','afo-ic2','n-ceo','n-grad']","ST=['ev-st0','ev-st1','ev-st2','ev-st3','ev-st4','ev-st5','ev-st1','ev-st4','ev-st0','ev-st5']")
rep("for(var k=0;k<10;k++){var an=k/10*6.283","for(var k=0;k<6;k++){var an=k/6*6.283+.5")

# ---------- feed: volume lives on the sound button ----------
i=s.index('  /* feed volume: one slider for every clip */');j=s.index('  /* router */',i)
s=s[:i]+r'''  /* feed volume: the sound button also holds a volume slider */
  (function(){var tk=document.querySelector('.yt .tk');if(!tk)return;var vol=.7;
    tk.querySelectorAll('.tk-mute').forEach(function(b){var w=document.createElement('span');w.className='tk-mw';b.parentNode.insertBefore(w,b);w.appendChild(b);
      var p=document.createElement('span');p.className='tk-vp';p.innerHTML='<input type="range" min="0" max="100" value="70" aria-label="ระดับเสียง">';w.appendChild(p);
      var r=p.querySelector('input');r.addEventListener('input',function(){vol=r.value/100;tk.querySelectorAll('video').forEach(function(v){v.volume=vol});tk.querySelectorAll('.tk-vp input').forEach(function(x){x.value=r.value});
        var on=b.getAttribute('aria-pressed')==='true';if(vol>0&&!on)b.click();if(vol===0&&on)b.click()})});
    tk.querySelectorAll('video').forEach(function(v){v.volume=vol})})();
'''+s[j:]

# ---------- courses transition: smoother ----------
rep("F=[['f1','คอร์ส'],['f2','คอร์ส'],['f3','คอร์ส'],['f4','&gt; คอร์ส_'],['f5','คอร์ส'],['f1','คอร์ส'],['f3','คอร์ส']]","F=[['f1','คอร์ส'],['f2','คอร์ส'],['f3','คอร์ส'],['f4','&gt; คอร์ส_'],['f5','คอร์ส']]")
rep("h+='<span class=\"cs-f '+f[0]+'\" style=\"--d:'+(k*.085).toFixed(3)+'s\">","h+='<span class=\"cs-f '+f[0]+'\" style=\"--d:'+(k*.13).toFixed(3)+'s\">")
rep("var hold={courses:950,","var hold={courses:1000,")

s=s.replace("$('#crows').innerHTML=","if($('#crows'))$('#crows').innerHTML=")
css=r'''
/* ===== v12 ===== */
.hh-h{font:800 clamp(1.9rem,4.2vw,3.4rem)/1.2 var(--display);letter-spacing:-.02em;color:#fff}
.hh-s{color:#C9CDE8;margin-top:10px;font-size:clamp(1rem,1.5vw,1.15rem)}
.gb2{position:relative;width:min(1240px,100%);margin:clamp(22px,3vw,34px) auto 0;aspect-ratio:1390/555;container-type:inline-size;filter:drop-shadow(0 0 50px rgba(255,62,165,.25)) drop-shadow(0 40px 40px rgba(0,0,0,.6))}
.gb-s.g2{left:23.6%;top:8.65%;width:52.8%;height:58.9%;display:block}
.gb2 .gb-f{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.gb-lcd{position:absolute;left:6.19%;top:63.24%;width:10.43%;height:13.87%;display:grid;place-items:center;align-content:center;gap:.2cqw;background:#0F1A10;box-shadow:inset 0 0 1cqw rgba(0,0,0,.8)}
.gb-lcd b{font:400 1.25cqw var(--pixel);color:#7CF29A;text-shadow:0 0 .6cqw rgba(124,242,154,.7)}
.gb-lcd s{font:600 .85cqw var(--display);color:#5A7A5C}
.gk{position:absolute;top:75.86%;width:12.23%;height:12.97%;display:grid;place-items:center;text-decoration:none;color:#14102E;transition:transform .1s steps(2),filter .2s}
.gk.k1{left:28.35%}.gk.k2{left:43.81%}.gk.k3{left:59.42%}
.gk span{font:800 1.25cqw/1.15 var(--display);text-align:center;padding:0 .5cqw}
.gk::after{content:"";position:absolute;inset:-.25cqw;box-shadow:0 0 0 .25cqw transparent;transition:box-shadow .2s}
.gk:hover{transform:translateY(.25cqw)}
.gk:hover::after,.gk:focus-visible::after{box-shadow:0 0 0 .3cqw #FFD24A,0 0 1.6cqw #FFD24A}
.gk.k1::before{content:"";position:absolute;left:-1.3cqw;top:50%;width:.8cqw;height:1cqw;margin-top:-.5cqw;background:#FFD24A;clip-path:polygon(0 0,100% 50%,0 100%);animation:bl .9s steps(1) infinite}
.gk-hint{position:absolute;left:28.35%;top:90%;font:600 1cqw var(--display);color:#9FE7FF}
.gbt{position:absolute;width:3.2%;height:7.4%;border-radius:.4cqw;cursor:default}
.hh-m{display:none}
.ar-floor{background-image:url(img/ar-floor2.webp)!important}
.t-wk video{height:74%!important;-webkit-mask:linear-gradient(transparent,#000 18%)!important;mask:linear-gradient(transparent,#000 18%)!important}
.ctb-f video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.pb-b.c{text-align:center}
.s3 .pb-h{font-size:4cqw;margin-bottom:2.4cqw}
.s4 .pb-h{font-size:4cqw;line-height:1.25}
.ev-mas img{width:52%!important}
.ac-soon img{width:130px}
/* feed volume on the sound button */
.tk-vol{display:none!important}
.tk-mw{position:relative;display:block}
.tk-vp{position:absolute;right:calc(100% + 8px);top:50%;transform:translateY(-50%) scaleX(.6);transform-origin:right;opacity:0;pointer-events:none;padding:10px 14px;border-radius:999px;background:rgba(0,0,0,.6);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);transition:opacity .2s,transform .2s}
.tk-mw:hover .tk-vp,.tk-mw:focus-within .tk-vp{opacity:1;pointer-events:auto;transform:translateY(-50%)}
.tk-vp input{width:110px;accent-color:#FFD24A;display:block}
/* courses transition: crossfades, then a calm exit */
.cs-f{animation:csF2 .26s var(--d) ease both!important;animation-fill-mode:none!important}
@keyframes csF2{0%{opacity:0;transform:scale(1.06)}25%,70%{opacity:1;transform:none}100%{opacity:0}}
.cs-end{animation:csE .3s .62s forwards!important}
.pt.out .cs{animation:csOut2 .6s cubic-bezier(.6,0,.3,1) forwards!important}
@keyframes csOut2{to{opacity:0;transform:scale(1.06);filter:blur(10px)}}
@media (max-width:700px){.gk span,.gk-hint,.gk.k1::before{display:none}.gb-lcd b{font-size:2.2cqw}.gb-lcd s{display:none}
  .hh-m{display:grid;justify-items:center;gap:12px;margin-top:18px}.hh-m p{color:#C9CDE8}.hh-m b{font:400 1.2rem var(--pixel);color:#FFD24A}.hh-m s{color:#8A90B8}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v12.html','w').write(s)
print('v12 ok',len(s))
