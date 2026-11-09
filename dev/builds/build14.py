import re
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build13.py').read())
LINE='https://page.line.me/jkm4247u?openQrModal=true'
PX='https://www.hamsterhub.co/portex-site/index.html'
AFO='https://www.hamsterhub.co/allforone'
def need(a):
    assert a in s,a[:70]

# ---------- one-frame banner: start -> what they get -> where it leads ----------
def banner2():
    return '''<div class="bn2" role="img" aria-label="Port Express คอร์สทำพอร์ตยื่นมหาลัยสำหรับน้อง ม.6 เรียนทำเกมกับพี่ๆ 2 เดือน ได้ผลงานใส่แฟ้มพอร์ต แล้วยื่นรอบ Portfolio รุ่นพี่ติดแล้ว 48 คน เริ่ม 9 พ.ย. 5,990 บาท">
  <div class="bn2-l"><b class="bn2-logo">PORT<br>EXPRESS</b><p class="bn2-a">คอร์สทำพอร์ตยื่นมหาลัย<br>สำหรับน้อง ม.6</p><p class="bn2-p">เริ่ม 9 พ.ย. · 5,990 บาท</p></div>
  <ol class="bn2-st">
    <li><span class="bv bv1"><img src="img/work-phi-krahang.webp" alt=""><img src="img/work-stressstrike.webp" alt=""><img src="img/work-midnight-at-roadside.webp" alt=""></span><b>เรียนทำเกม<br>กับพี่ๆ 2 เดือน</b></li>
    <li><span class="bv bv2"><span class="fd"><span class="tb">PORTFOLIO</span><i></i><i></i><i></i><em>READY!</em></span></span><b>ได้ผลงานจริง<br>ใส่แฟ้มพอร์ต</b></li>
    <li><span class="bv bv3"><img src="img/dek69-13.webp" alt=""><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""></span><b>ยื่นรอบ Portfolio<br>ติดมหาลัย</b><small>รุ่นพี่ติดแล้ว 48 คน</small></li>
  </ol>
</div>'''

# ---------- HERO: pixel-art night scene, a console that is almost all screen ----------
for a in ['      <p class="hh-h rv">จบคอร์ส น้องมีแฟ้มพอร์ตพร้อมยื่นมหาลัย</p>\n','      <p class="hh-s rv">Port Express คอร์ส 2 เดือนสำหรับ ม.6 ที่ยังไม่มีผลงาน · เริ่ม 9 พ.ย. 2569</p>\n']:
    need(a);s=s.replace(a,'')
i=s.index('      <div class="gb2 rv">');k=s.index('<div class="hh-m">',i);j=s.index('</div></div>\n',k)+len('</div></div>\n')
s=s[:i]+'''      <div class="c3 rv">
        <img class="c3-f" src="img/console3.webp" alt="">
        <a class="c3-cart" href="#courses" aria-label="ตลับเกมคอร์ส Port Express"><span>PORT EXPRESS</span></a>
        <a class="c3-s" href="#portex" aria-label="ดูรายละเอียดคอร์ส Port Express">'''+banner2()+'''<span class="c3-gl"></span></a>
        <a class="c3-k k1" href="#portex"><span>ดูรายละเอียด</span></a>
        <a class="c3-k k2" href="'''+PX+'''" target="_blank" rel="noopener"><span>สมัครเรียน</span></a>
        <a class="c3-k k3" href="'''+LINE+'''" target="_blank" rel="noopener"><span>ทัก LINE</span></a>
      </div>
      <div class="hh-m"><div class="hh-a"><a class="b1" href="#portex">ดูรายละเอียด</a><a class="b2" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="b3" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE</a></div></div>
'''+s[j:]
rep("var bgT=tex('img/n-hero.webp'","var bgT=tex('img/px-bg.webp'")
rep("V0=.86,V1=.975","V0=.865,V1=.97")
rep("function hh0(o){return Math.min(bh*(.15+.07*o.d),w*(.25+.07*o.d))}","function hh0(o){return Math.min(bh*(.115+.05*o.d),w*(.25+.07*o.d))}")

# ---------- course page banner = the same one-frame banner ----------
i=s.index('<div class="ctb-f px-bnr">');j=s.index('</div></div>',s.index('class="pb-pip"',i))+len('</div></div>')
s=s[:i]+'<div class="ctb-f px-bnr">'+banner2()+'</div>'+s[j:]

# seniors: kept as the center-focus carousel (timed cards reverted)
# ---------- ACTIVITY: no boxes, plain rows ----------
i=s.index('<div data-view="activity">');j=s.index('<!-- ================= WORKS',i)
s=s[:i]+'''<div data-view="activity">
  <div class="wrap">
    <section class="ac-h"><h1>กิจกรรม</h1><p>ค่าย เวิร์กชอป การแข่งขัน และงานโชว์ผลงาน ทุกงานน้องได้ลงมือสร้างของจริง</p></section>
    <section class="au">
      <img class="au-logo" src="img/k-afo-logo.webp" alt="All for One University">
      <div class="au-t">
        <p class="au-k" id="auK">กำลังจะมา · 14 พ.ย. 2569</p>
        <h2>All for One University รอบชิงชนะเลิศ</h2>
        <p>ทีมที่ผ่านรอบออนไลน์ มานำเสนอผลงานจริงต่อกรรมการ ที่ IoTE สจล. ลาดกระบัง</p>
        <p class="au-g"><b>น้องได้</b> นำเสนอผลงานบนเวทีจริง เอาไปเล่าในพอร์ตได้</p>
        <p class="au-c"><span class="cd" id="cdAct"></span><a href="'''+AFO+'''" target="_blank" rel="noopener">ดูรายละเอียดงาน</a></p>
      </div>
    </section>
    <p class="au-n"><img src="img/ev-st0.webp" alt="">กิจกรรมถัดไปกำลังจะประกาศ <a href="'''+LINE+'''" target="_blank" rel="noopener">รับแจ้งเตือนทาง LINE</a></p>
    <h2 class="er-h">จบไปแล้วในปี 2569</h2>
    <ol class="er-l" id="acl"></ol>
    <p class="er-hint">ชี้ที่กิจกรรมเพื่อดูโปสเตอร์</p>
  </div>
  <img class="er-pv" id="erPv" alt="" aria-hidden="true">
</div>

'''+s[j:]
i=s.index('var MAS=');j=s.index('/* countdowns */',i)
s=s[:i]+r'''var MAS={'ค่าย':'ev-st2','เวิร์กชอป':'ev-st3','แข่งขัน':'ev-st4','โชว์ผลงาน':'ev-st1','โครงการ':'ev-st5'},
    GAIN={'ค่าย':'ได้ผลงานกลับไปภายในไม่กี่วัน','เวิร์กชอป':'ได้ลองทักษะใหม่ในวันเดียว','แข่งขัน':'ได้ลงแข่งจริง มีเรื่องเล่าใส่พอร์ต','โชว์ผลงาน':'ได้นำเสนอผลงานต่อคนจริง','โครงการ':'ได้ผลงานส่งเวทีระดับประเทศ'};
  function alist(){var el=$('#acl');if(!el)return;el.innerHTML=ACT.filter(function(a){return !a[4]}).map(function(a){var im=AIMG[a[1]];
    return '<li class="er"'+(im?' data-pv="img/'+im+'.webp"':'')+'><time>'+a[0]+'</time><img class="er-s" src="img/'+MAS[a[3]]+'.webp" alt="" loading="lazy"><div><b>'+a[1]+'</b><p>'+a[2]+'</p><em>น้องได้: '+GAIN[a[3]]+'</em></div></li>'}).join('');
    var pv=$('#erPv');el.querySelectorAll('.er').forEach(function(r){r.addEventListener('pointerenter',function(){if(!r.dataset.pv){pv.classList.remove('on');return}pv.src=r.dataset.pv;pv.classList.add('on')});r.addEventListener('pointerleave',function(){pv.classList.remove('on')})});
    el.addEventListener('pointermove',function(e){pv.style.transform='translate('+(e.clientX+28)+'px,'+(e.clientY-120)+'px) rotate(4deg)'})}
  alist();
  (function(){if(new Date()>new Date('2026-11-14T18:00:00+07:00')){var k=$('#auK');if(k)k.textContent='เพิ่งจบไป · 14 พ.ย. 2569'}})();
  '''+s[j:]

# ---------- ABOUT: what each real-world project is, in one line, with a picture ----------
i=s.index('<section class="ab-real">');j=s.index('</section>',i)+10
s=s[:i]+'''<section class="ab-real"><div class="wrap"><h2 class="sec-h rv">ผลงานของน้องที่มีคนใช้จริง</h2>
    <ul class="rw">
      <li class="rv"><img src="img/real-0.webp" alt="" loading="lazy"><b>Mr. City</b><p>เกมแนะนำที่เที่ยวในสงขลา</p><em>ขายให้สวนสัตว์สงขลาแล้ว</em></li>
      <li class="rv"><img src="img/real-1.webp" alt="" loading="lazy"><b>PHC Map</b><p>เกมสอนเขียนโปรแกรม Python</p><em>ใช้สอนเด็กไปแล้วกว่า 1,000 คน</em></li>
      <li class="rv"><img src="img/real-2.webp" alt="" loading="lazy"><b>StressStrike</b><p>เกมที่เล่นด้วยการบีบอุปกรณ์วัดแรงมือ</p><em>ชนะเลิศ OBEC Roboplayground</em></li>
      <li class="rv"><img src="img/real-3.webp" alt="" loading="lazy"><b>Hamster Quest</b><p>เว็บเรียนที่เล่นเหมือนเกม</p><em>กำลังเตรียมใช้กับมหาวิทยาลัย</em></li>
    </ul><p class="rw-n">ภาพประกอบเป็นภาพวาด</p></div></section>'''+s[j:]

css=r'''
/* ===== v14 ===== */
/* hero: pixel night scene, no floor */
.ar{background:#120A33 url(img/px-bg.webp) 50% 100%/cover no-repeat!important;--floor:150px}
.ar-wall,.ar-floor,.ar-neon{display:none!important}
.ar .hx3{z-index:4!important}
.hh{position:relative;z-index:2;padding-top:0;padding-bottom:calc(var(--floor) - 34px)!important}
.ar-tip{color:rgba(255,255,255,.75);text-shadow:0 1px 2px #000}
.c3{position:relative;width:min(1100px,100%,calc((100svh - 350px) * 1.54));margin:0 auto;aspect-ratio:1147/745;container-type:inline-size;filter:drop-shadow(0 0 40px rgba(255,62,165,.25)) drop-shadow(0 30px 30px rgba(0,0,0,.55))}
.c3-f{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2}
.c3-s{position:absolute;left:3.49%;top:25.91%;width:92.76%;height:59.73%;display:block;overflow:hidden;background:#0B0A2E;z-index:1}
.c3-gl{position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,0,0,.08) 0 2px,transparent 2px 4px),linear-gradient(120deg,rgba(255,255,255,.1) 0 10%,transparent 24%)}
.c3-cart{position:absolute;left:34.7%;top:2.82%;width:30.34%;height:18.66%;z-index:3;display:grid;place-items:center;background:linear-gradient(#FFD24A,#FFB81C);text-decoration:none;box-shadow:inset 0 -.5cqw 0 #C28A00}
.c3-cart span{font:400 2.2cqw var(--pixel);color:#3A1E00;text-shadow:.15cqw .15cqw 0 rgba(255,255,255,.5)}
.c3-k{position:absolute;top:88.59%;width:12.5%;height:7.52%;z-index:3;display:grid;place-items:center;text-decoration:none;cursor:pointer;transition:transform .08s steps(2)}
.c3-k.k1{left:28.68%}.c3-k.k2{left:43.59%}.c3-k.k3{left:58.59%}
.c3-k span{font:800 1.45cqw var(--display);color:#14102E;white-space:nowrap}
.c3-k::after{content:"";position:absolute;inset:-.35cqw;border:.25cqw solid transparent;transition:border-color .15s,box-shadow .15s}
.c3-k:hover{transform:translateY(.3cqw)}
.c3-k:hover::after,.c3-k:focus-visible::after{border-color:#FFD24A;box-shadow:0 0 1.4cqw #FFD24A}
.c3-k.k2::after{border-color:#FFD24A;animation:kp 1.6s ease-in-out infinite}
@keyframes kp{50%{box-shadow:0 0 1.6cqw #FFD24A}}
.c3-k.k2 span::before{content:"▼";position:absolute;left:50%;top:-3.2cqw;transform:translateX(-50%);font-size:1.4cqw;color:#FFD24A;animation:kb .8s ease-in-out infinite alternate}
@keyframes kb{to{transform:translate(-50%,.6cqw)}}
.hh-m{display:none}
/* one-frame banner */
.bn2{position:absolute;inset:0;container-type:inline-size;display:grid;grid-template-columns:29cqw 1fr;align-items:center;gap:3cqw;padding:0 4cqw;color:#fff;font-family:var(--display);
  background:radial-gradient(60% 90% at 70% 40%,#3B1E8C,#160B3E 60%,#0A0716) ;overflow:hidden}
.bn2::before{content:"";position:absolute;inset:0;background-image:radial-gradient(#fff 1px,transparent 1.5px);background-size:7cqw 7cqw;opacity:.25;pointer-events:none}
.bn2-l{position:relative}
.bn2-logo{display:block;font:400 4.6cqw/1.12 var(--pixel);color:#FFD24A;text-shadow:.45cqw .45cqw 0 #E0337E}
.bn2-a{font:800 2.5cqw/1.3 var(--display);margin-top:1.6cqw}
.bn2-p{display:inline-block;margin-top:1.6cqw;font:700 1.8cqw var(--display);color:#0B0720;background:#7CF29A;padding:.5cqw 1.3cqw}
.bn2-st{position:relative;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:4cqw}
.bn2-st li{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:1.4cqw;animation:stp 6s infinite}
.bn2-st li:nth-child(2){animation-delay:2s}.bn2-st li:nth-child(3){animation-delay:4s}
@keyframes stp{0%,30%{transform:translateY(-.8cqw)}36%,100%{transform:none}}
.bn2-st li:not(:last-child)::after{content:"";position:absolute;right:-3.2cqw;top:6.5cqw;width:2.4cqw;height:2.4cqw;background:#FFD24A;clip-path:polygon(0 30%,55% 30%,55% 0,100% 50%,55% 100%,55% 70%,0 70%)}
.bn2-st b{font:800 2cqw/1.3 var(--display)}
.bn2-st small{font:700 1.5cqw var(--display);color:#FFD24A;margin-top:-.6cqw}
.bv{position:relative;width:16cqw;height:14cqw;display:block}
.bv1 img{position:absolute;width:12cqw;aspect-ratio:16/10;object-fit:cover;border:.35cqw solid #fff;border-radius:.6cqw;box-shadow:0 1cqw 2cqw rgba(0,0,0,.5)}
.bv1 img:nth-child(1){left:0;top:4.6cqw;transform:rotate(-8deg)}.bv1 img:nth-child(2){left:2cqw;top:2.3cqw;transform:rotate(3deg)}.bv1 img:nth-child(3){left:4cqw;top:0;transform:rotate(-2deg)}
.fd{position:absolute;left:2cqw;top:0;width:12cqw;height:13.5cqw}
.fd::before{content:"";position:absolute;inset:1.6cqw 0 0;background:#FFB81C;box-shadow:inset 0 -.6cqw 0 #C28A00}
.fd .tb{position:absolute;left:0;top:0;height:1.8cqw;padding:0 1cqw;background:#FFB81C;font:400 .8cqw/1.9cqw var(--pixel);color:#5A3A00}
.fd i{position:absolute;left:1.2cqw;right:1.2cqw;height:2.8cqw;background:#fff}
.fd i:nth-of-type(1){top:3.2cqw}.fd i:nth-of-type(2){top:6.6cqw}.fd i:nth-of-type(3){top:10cqw}
.fd i::before{content:"";position:absolute;left:.5cqw;top:.5cqw;bottom:.5cqw;width:3cqw;background:#5B3FD6}
.fd i:nth-of-type(2)::before{background:#1068DC}.fd i:nth-of-type(3)::before{background:#2E9E6B}
.fd em{position:absolute;right:-2cqw;bottom:.6cqw;font:400 1.2cqw var(--pixel);font-style:normal;color:#E0337E;border:.3cqw solid #E0337E;background:rgba(255,255,255,.9);padding:.4cqw .6cqw;transform:rotate(-12deg)}
.bv3 img{position:absolute;top:1cqw;width:7.4cqw;aspect-ratio:4/5;object-fit:cover;border:.3cqw solid #fff;box-shadow:0 1cqw 2cqw rgba(0,0,0,.5)}
.bv3 img:nth-child(1){left:0;transform:rotate(-10deg)}.bv3 img:nth-child(2){left:4.3cqw;top:0;z-index:1}.bv3 img:nth-child(3){left:8.6cqw;transform:rotate(10deg)}
.px-bnr{aspect-ratio:1064/445!important;overflow:hidden}
/* seniors: timed cards */
.tc{position:relative;margin:12px 12px 0;overflow:hidden;color:#fff;background:#0A0716;min-height:clamp(600px,52vw,760px)}
.tc-bg img{position:absolute;inset:-4%;width:108%;height:108%;object-fit:cover;object-position:50% 30%;filter:blur(6px) brightness(.5) saturate(1.15);opacity:0;transform:scale(1.08);transition:opacity 1s,transform 5s linear}
.tc-bg img.on{opacity:1;transform:scale(1)}
.tc::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,7,22,.88) 0%,rgba(10,7,22,.45) 50%,rgba(10,7,22,.1) 100%);pointer-events:none}
.tc-in{position:relative;z-index:1;max-width:1240px;margin:0 auto;padding:clamp(40px,5vw,64px) clamp(20px,4vw,48px);display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);grid-template-rows:auto 1fr auto;gap:24px 40px;min-height:inherit}
.tc-top{grid-column:1/-1;display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.tc-k{font:700 1.1rem var(--display);color:#FFD24A}
.tc-u{display:flex;gap:4px;flex-wrap:wrap}
.tc-u button{border:0;background:none;color:rgba(255,255,255,.65);font:600 .95rem var(--display);padding:8px 14px;border-radius:999px;cursor:pointer;transition:background .2s,color .2s}
.tc-u button:hover{background:rgba(255,255,255,.14);color:#fff}
.tc-u button[aria-pressed="true"]{color:#fff;text-decoration:underline;text-decoration-color:#FFD24A;text-decoration-thickness:2px;text-underline-offset:7px}
.tc-l{align-self:center}
.tc-l.in>*{animation:tcIn .7s cubic-bezier(.2,.8,.2,1) both}.tc-l.in>*:nth-child(2){animation-delay:.06s}.tc-l.in>*:nth-child(3){animation-delay:.12s}.tc-l.in>*:nth-child(4){animation-delay:.18s}
@keyframes tcIn{from{opacity:0;transform:translateY(24px)}}
.tc-uni{display:inline-block;font:700 1rem var(--display);color:#fff;background:var(--c,#FF8A3D);padding:4px 14px;border-radius:999px}
.tc h2{font:800 clamp(3rem,7vw,6rem)/1 var(--display);letter-spacing:-.03em;margin-top:16px}
.tc-f{font:600 clamp(1.1rem,1.8vw,1.4rem) var(--display);margin-top:14px}
.tc-cs{color:rgba(255,255,255,.75);margin-top:6px}
.tc .lk{margin-top:20px;margin-left:-20px}
.tc-cards{position:relative;align-self:center;height:clamp(300px,30vw,420px)}
.tc-c{--o:0;position:absolute;top:50%;left:0;border:0;padding:0;background:none;cursor:pointer;width:clamp(120px,11vw,160px);transform:translate(calc(var(--o) * (clamp(120px,11vw,160px) + 16px) + clamp(80px,9vw,140px)),-30%);transition:transform .9s cubic-bezier(.65,0,.2,1),width .9s cubic-bezier(.65,0,.2,1),opacity .6s;color:#fff;text-align:left}
.tc-c img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:14px;box-shadow:0 20px 40px -18px rgba(0,0,0,.8)}
.tc-c span{display:grid;margin-top:8px}.tc-c b{font:700 .95rem var(--display)}.tc-c small{color:rgba(255,255,255,.65);font-size:.82rem}
.tc-c.on{width:clamp(220px,22vw,300px);transform:translate(-20px,-50%)}
.tc-c.on span{display:none}
.tc-c.gone{opacity:0;pointer-events:none}
.tc-c:not(.on):hover img{outline:3px solid #FFD24A}
.tc-bar{grid-column:1/-1;display:flex;align-items:center;gap:16px}
.tc-p{flex:1;height:3px;background:rgba(255,255,255,.18);overflow:hidden}
.tc-p i{display:block;height:100%;background:#FFD24A;transform-origin:left;animation:tcP 4.2s linear forwards}
.tc.hold .tc-p i{animation-play-state:paused}
@keyframes tcP{from{transform:scaleX(0)}}
.tc-bar b{font:700 1.1rem var(--display);font-variant-numeric:tabular-nums}
/* activity: no boxes */
.au{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(24px,5vw,64px);align-items:center;margin-top:20px;padding:24px 0 32px;border-bottom:1px solid var(--hair)}
.au-logo{width:100%;max-width:440px;transform:rotate(-4deg);filter:drop-shadow(0 18px 24px rgba(16,104,220,.25))}
.au-k{font:700 1rem var(--display);color:#E0337E}
.au h2{font:800 clamp(1.8rem,3.4vw,2.6rem)/1.15 var(--display);margin-top:8px}
.au p{color:var(--mute);margin-top:10px;line-height:1.6}
.au-g{color:var(--ink)!important}.au-g b{color:#2E9E6B;margin-right:6px}
.au-c{display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.au-c .cd{font:800 1.4rem var(--display);color:var(--ink);background:none;padding:0}
.au-c a{color:#1068DC;font-weight:600;text-decoration:none;padding:8px 14px;margin-left:-14px;border-radius:999px}.au-c a:hover{background:#E8F1FF}
.au-n{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:22px;font:700 1.1rem var(--display)}
.au-n img{width:64px}
.au-n a{color:#06C755;text-decoration:none;font-weight:600;padding:6px 12px;border-radius:999px}.au-n a:hover{background:#E6F9EE}
.er-h{font:800 clamp(1.6rem,3vw,2.2rem) var(--display);margin-top:64px}
.er-l{list-style:none;margin:16px 0 0;padding:0}
.er{display:grid;grid-template-columns:150px 72px minmax(0,1fr);gap:20px;align-items:center;padding:18px 0;border-top:1px solid var(--hair);cursor:default}
.er:last-child{border-bottom:1px solid var(--hair)}
.er time{font:700 1rem var(--display);color:var(--mute)}
.er-s{width:72px;transition:transform .3s cubic-bezier(.3,1.6,.5,1)}
.er:hover .er-s{transform:rotate(-8deg) scale(1.12)}
.er b{font:700 1.15rem var(--display)}.er p{color:var(--mute);font-size:.95rem;margin-top:2px}
.er em{display:block;font-style:normal;font-weight:600;color:#2E9E6B;font-size:.95rem;margin-top:4px}
.er-hint{color:var(--mute);font-size:.85rem;margin:14px 0 80px}
.er-pv{position:fixed;left:0;top:0;width:260px;pointer-events:none;z-index:40;opacity:0;transition:opacity .2s;border-radius:10px;box-shadow:0 30px 50px -20px rgba(0,0,0,.5)}
.er-pv.on{opacity:1}
/* about: real-world projects */
.rw{list-style:none;margin:36px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px}
.rw li{text-align:center}
.rw img{width:min(100%,220px);aspect-ratio:1;object-fit:contain}
.rw b{display:block;font:800 1.3rem var(--display);margin-top:10px}.rw p{color:var(--ink);margin-top:4px}
.rw em{display:inline-block;font-style:normal;font-weight:700;color:#2E9E6B;margin-top:8px}
.rw-n{text-align:center;color:var(--mute);font-size:.8rem;margin-top:24px}
@media (max-width:900px){.au{grid-template-columns:minmax(0,1fr)}.au-logo{max-width:300px}.rw{grid-template-columns:repeat(2,minmax(0,1fr))}
  .tc-in{grid-template-columns:minmax(0,1fr)}.tc-cards{height:280px}}
@media (max-width:700px){.c3 .bn2{grid-template-columns:1fr;text-align:center;padding:0 3cqw}.c3 .bn2-st{display:none}.c3 .bn2-logo{font-size:8cqw}.c3 .bn2-a{font-size:5cqw}.c3 .bn2-p{font-size:3.6cqw}.c3-k span,.c3-k.k2 span::before{display:none}.hh-m{display:grid;justify-items:center;margin-top:16px}
  .er{grid-template-columns:56px minmax(0,1fr);gap:4px 14px}.er time{grid-column:1/-1}.er-s{width:56px}.er-pv,.er-hint{display:none}
  .tc-c{transform:translate(calc(var(--o) * 108px + 70px),-30%);width:96px}.tc-c.on{width:170px;transform:translate(-10px,-50%)}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v14.html','w').write(s)
print('v14 ok',len(s))
