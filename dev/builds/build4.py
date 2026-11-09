import re,json
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build3.py').read())       # -> v3.html, s holds v3
LINE='https://page.line.me/jkm4247u?openQrModal=true'
PX='https://www.hamsterhub.co/portex-site/index.html'
AFO='https://www.hamsterhub.co/allforone'

def sec(a,b,new):           # replace from a up to (not incl) b
    cut(a,b,new)

# ================= arcade cabinet component =================
def cabinet(cls,href):
    return ('<a class="arc '+cls+'" href="'+href+'" aria-label="Port Express ดูรายละเอียดคอร์ส">'
     '<span class="arc-mq"><i></i><b>PORT EXPRESS</b><i></i></span>'
     '<span class="arc-scr"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video><span class="arc-gl"></span></span>'
     '<span class="arc-pn"><span class="arc-js"><i></i></span><span class="arc-bt"><i></i><i></i><i></i></span><span class="arc-cn">INSERT COIN</span></span>'
     '<span class="arc-ft"></span></a>')

# ================= HOME =================
sec('  <section class="h-hero">','  <section class="paths">','''  <section class="h-hero hp" id="hx">
    <div class="wrap hp-txt">
      <p class="hp-k rv"><span class="pxdot"></span><span class="pxst">รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</span></p>
      <h1 class="hp-h rv">Port Express</h1>
      <p class="hp-t rv">ม.6 ยังไม่มีพอร์ต? เรียน 2 เดือน ได้เกม 3 งาน พร้อมยื่นมหาลัย</p>
      <p class="hp-m rv">คอร์สทำพอร์ตเกมของ Hamster Hub · เรียน จันทร์ พุธ ศุกร์ · <b>5,990 บาท</b> <s>9,990</s></p>
      <div class="btns rv"><a class="btn btn-p" href="#portex">ดูรายละเอียดคอร์ส</a><a class="btn btn-s more" href="'''+PX+'''" target="_blank" rel="noopener">เข้าเว็บ Port Express</a></div>
    </div>
    <div class="hp-stage">'''+cabinet('hp-arc','#portex')+'''
      <div class="hx3" id="hx3" aria-hidden="true"><canvas id="hxCanvas"></canvas><div class="hx-say" id="hxSay"></div></div>
      <p class="hp-tip">ลองกดค้างที่น้องหนูแล้วยกขึ้นมาดูสิ</p>
    </div>
  </section>

  <section class="hp-grid"><div class="wrap hg">
    <div class="tile t-afo rv">
      <p class="t-k" id="afoTag">กิจกรรมถัดไป · รอบชิงชนะเลิศ</p>
      <div class="afo-hd"><img class="afo-logo" src="img/k-afo-logo.webp" alt="All for One University" loading="lazy"><img class="afo-ic i0" src="img/afo-ic0.webp" alt="" aria-hidden="true"><img class="afo-ic i1" src="img/afo-ic1.webp" alt="" aria-hidden="true"><img class="afo-ic i2" src="img/afo-ic2.webp" alt="" aria-hidden="true"></div>
      <p class="t-s">14 พ.ย. 2569 ที่ IoTE สจล. ลาดกระบัง<br>ทีมที่ผ่านรอบออนไลน์มานำเสนอผลงานจริงต่อกรรมการ</p>
      <div class="cd" id="afoCd" aria-label="นับถอยหลังถึงวันแข่ง"><div><b id="cdD">0</b><span>วัน</span></div><div><b id="cdH">0</b><span>ชั่วโมง</span></div><div><b id="cdM">0</b><span>นาที</span></div></div>
      <div class="t-b"><a class="tb1" href="'''+AFO+'''" target="_blank" rel="noopener">รายละเอียดงาน</a><a class="tb2" href="#activity">กิจกรรมทั้งหมด</a></div>
    </div>
    <a class="tile t-wk rv" href="#works">
      <p class="t-k">ผลงานนักเรียน</p>
      <h3>ผลงานจริงของน้องๆ</h3>
      <p class="t-s">ทุกฉากในคลิปนี้มาจากเกมที่น้องสร้างเอง<br>ดูแบบเลื่อนได้เหมือน TikTok</p>
      <span class="t-b"><span class="tb1">ดูผลงาน</span></span>
      <video src="img/reel.mp4" poster="img/reel-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video>
    </a>
  </div></section>

''')
cut('  <section class="gain">','  <section class="proof">','')
cut('  <section class="open">','  <section class="dkx">','')
rep('<img src="img/n-build.webp" alt="" loading="lazy"><i class="bubble">ขายได้จริง!</i>','<img src="img/n-biz.webp" alt="" loading="lazy"><i class="bubble">ขายได้จริง!</i>')
# seniors -> auto-moving gallery
sec('  <section class="dkx">','  <section class="ptn">','''  <section class="sx">
    <div class="wrap sx-h">
      <div><p class="eyebrow rv">รุ่น DEK69</p><h2 class="rv">รุ่นพี่ 48 คน<br>ไปถึงคณะที่ใช่แล้ว</h2></div>
      <div class="sx-u rv" role="group" aria-label="ดูตามมหาวิทยาลัย">
        <button type="button" data-u="k" style="--c:#E8742A" aria-pressed="false"><b>24</b><span>สจล.</span></button>
        <button type="button" data-u="m" style="--c:#3F5FD0" aria-pressed="false"><b>9</b><span>มหิดล</span></button>
        <button type="button" data-u="c" style="--c:#D9558C" aria-pressed="false"><b>8</b><span>จุฬาฯ</span></button>
        <button type="button" data-u="u" style="--c:#2E9E6B" aria-pressed="false"><b>7</b><span>เกษตรฯ</span></button>
      </div>
    </div>
    <div class="sx-rail" aria-label="โปสเตอร์รุ่นพี่ DEK69"><div class="sx-tr" id="sxT"></div></div>
    <div class="wrap sx-ft"><p id="sxN">ชี้ค้างเพื่อหยุด · แตะมหาวิทยาลัยด้านบนเพื่อดูเฉพาะที่นั่น</p><a class="more" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a></div>
  </section>

''')

# ================= COURSES =================
sec('    <a class="ct-feat" href="#portex">','    <section class="ct-list">','''    <div class="ct-px">
      '''+cabinet('ct-arc','#portex')+'''
      <div class="ct-pi">
        <p class="blink pxst">● รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</p>
        <h2 class="pxf">PORT<br>EXPRESS</h2>
        <p class="ct-pt">คอร์สทำพอร์ตเกม 2 เดือน สำหรับ ม.6 ที่ยังไม่มีพอร์ต จบได้เกม 3 งานพร้อมยื่นมหาลัย</p>
        <ul class="ct-pf"><li><small>START</small>9 พ.ย. 2569</li><li><small>DAYS</small>จ · พ · ศ</li><li><small>LOOT</small>3 เกม</li></ul>
        <p class="ct-pp"><b>5,990 ฿</b><s>9,990</s></p>
        <div class="ct-pb"><a class="pbtn gold" href="#portex">▶ ดูรายละเอียด</a><a class="pbtn blue" href="'''+PX+'''" target="_blank" rel="noopener">เว็บ Port Express</a></div>
      </div>
    </div>
''')
rep("""var CB=['#FFF1D6','#E3F3FF','#FFE6EE','#E6F7EC','#EEE8FF','#FFF6E2'];""","""var CB=['','','','','',''],MO=['70','EXPRESS','NSC','฿','&gt;&gt;&gt; run()','START'];""")
rep("""'<div class="cc"><div class="cc-m" style="background:'+CB[ci]+'">'+im+'<span class="cc-st">รอบถัดไป</span></div>""","""'<div class="cc"><div class="cc-m th'+ci+'"><i class="mo" aria-hidden="true">'+MO[ci]+'</i>'+im+'<span class="cc-st">รอบถัดไป</span></div>""")

# ================= PORT EXPRESS (pixel arcade page) =================
RK=[('1','BRONZE','#D08A4E','สัปดาห์ 1–3','9 – 29 พ.ย.','ทำเกมให้สนุกเป็น','เกมที่ 1 เกมแรกที่เล่นแล้วสนุก',
     [('Intro to Game Design','หลักคิดออกแบบเกมให้สนุก'),('Unity Tricks','ใช้ Unity สร้างเกมได้คล่องมือ'),('Level Design','ออกแบบด่านให้เล่นแล้วอยากไปต่อ'),('3D Map & Environment','สร้างฉากและแผนที่ 3 มิติ'),('Basic AI','ทำศัตรูที่คิดเองได้')]),
    ('2','SILVER','#B9C2D6','สัปดาห์ 4–6','30 พ.ย. – 20 ธ.ค.','ออกแบบเกมให้ขายได้','เกมที่ 2 เกมที่แตกต่างและขายได้',
     [('Game Feel Technique','เล่นแล้วลื่น มันมือ'),('Animation','ตัวละครขยับแล้วมีชีวิต'),('Camera Direction','คุมกล้องให้เกมดูเป็นหนัง'),('Intermediate AI','ศัตรูฉลาดขึ้น เล่นแล้วท้าทาย'),('Pitching Tricks','พูดนำเสนอให้กรรมการอยากได้')]),
    ('3','GOLD','#FFD24A','สัปดาห์ 7–8','21 ธ.ค. – ต้น ม.ค.','เกมใหญ่ ทำเป็นทีม','เกมที่ 3 เกม Scale ใหญ่แบบกลุ่ม',
     [('สาย Art','แมพขั้นสูง ปั้นโมเดล 3 มิติ จัดแสง'),('สาย Developer','Advance AI และเขียนโค้ดเป็นระบบ (OOP)'),('สาย Director','คุมทีม และวางแผนงานให้ทันกำหนด')])]
rk=''
for n,nm,c,wk,dt,t,loot,tp in RK:
    rk+=('<article class="rk" style="--c:'+c+'"><header><span class="rk-n">RANK '+n+'</span><span class="rk-m">'+nm+'</span></header>'
         '<p class="rk-w"><b>'+wk+'</b> · '+dt+'</p><h3>'+t+'</h3><ul>'+''.join('<li><b>'+a+'</b>'+b+'</li>' for a,b in tp)+'</ul>'
         '<p class="rk-l"><small>LOOT</small>'+loot+'</p></article>')
portex='''<div data-view="portex" class="pxp">
  <section class="px-hero"><div class="wrap px-hg">
    <div class="px-info">
      <p class="px-crumb"><a href="#home">หน้าแรก</a> › <a href="#courses">คอร์ส</a> › Port Express</p>
      <p class="blink pxst">● รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</p>
      <h1 class="pxf px-h">PORT<br>EXPRESS</h1>
      <p class="px-t">ม.6 ยังไม่มีพอร์ต? เรียน 2 เดือน ได้เกม 3 งาน พร้อมยื่นมหาลัย</p>
      <ul class="px-st"><li><small>START</small>9 พ.ย. 2569</li><li><small>DAYS</small>จ · พ · ศ</li><li><small>TIME</small>2 เดือน</li><li><small>LOOT</small>เกม 3 งาน</li><li><small>SAVE</small>5 Checkpoint</li></ul>
      <p class="px-pr"><span class="coin"></span><b>5,990 ฿</b><s>9,990</s><em>ประหยัด 4,000</em></p>
      <div class="px-bt"><a class="pbtn gold" href="'''+PX+'''" target="_blank" rel="noopener">▶ เข้าเว็บ Port Express</a><a class="pbtn blue" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div>
    </div>
    '''+cabinet('px-arc',PX).replace('href="'+PX+'"','href="'+PX+'" target="_blank" rel="noopener"')+'''
  </div></section>

  <section class="px-sec"><div class="wrap">
    <p class="px-eb">SELECT STAGE</p>
    <h2>2 เดือน เรียนอะไรบ้าง</h2>
    <p class="px-lead">ไล่เลื่อน Rank เหมือนเล่นเกม จบแต่ละ Rank ได้เกม 1 งานเข้าพอร์ต ทุกหัวข้อสอนด้วย Unity โปรแกรมที่สตูดิโอเกมใช้จริง</p>
    <div class="px-tl" aria-hidden="true"><span style="--c:#D08A4E;flex:3">BRONZE<small>สัปดาห์ 1–3</small></span><span style="--c:#B9C2D6;flex:3">SILVER<small>สัปดาห์ 4–6</small></span><span style="--c:#FFD24A;flex:2">GOLD<small>สัปดาห์ 7–8</small></span></div>
    <div class="rks">'''+rk+'''</div>
  </div></section>

  <section class="px-sec px-cp"><div class="wrap">
    <p class="px-eb">SAVE POINT</p>
    <h2>ตรวจงาน 5 ครั้ง ไม่ปล่อยให้หลง</h2>
    <p class="px-lead">ทุก Checkpoint มีอาจารย์มหาวิทยาลัยฟังผลงาน ให้คำแนะนำว่าผ่านอะไรแล้ว ต้องแก้อะไร พร้อมซ้อมสัมภาษณ์</p>
    <ol class="cps"><li><i>1</i>CHECKPOINT</li><li><i>2</i>CHECKPOINT</li><li><i>3</i>CHECKPOINT</li><li><i>4</i>CHECKPOINT</li><li><i>5</i>CHECKPOINT</li><li class="g"><i>★</i>RANK UP</li></ol>
  </div></section>

  <section class="px-sec"><div class="wrap">
    <p class="px-eb">INVENTORY</p>
    <h2>จบคอร์ส ได้อะไรติดตัวไป</h2>
    <div class="inv">
      <div><span class="sl">x3</span><b>เกมที่เล่นได้จริง</b><p>ขึ้น itch.io มีลิงก์ให้กรรมการกดเล่นได้ทันที</p></div>
      <div><span class="sl">PDF</span><b>Pitch Deck และพอร์ต</b><p>แก้กับเทรนเนอร์จนพร้อมส่ง</p></div>
      <div><span class="sl">5+</span><b>นำเสนอต่อคนจริง</b><p>พูดรู้เรื่อง ไม่สั่นตอนเข้าห้องสัมภาษณ์</p></div>
      <div><span class="sl">2W</span><b>อาจารย์มหาลัยเห็นงาน</b><p>ฟังผลงานทุก 2 สัปดาห์</p></div>
    </div>
  </div></section>

  <section class="px-sec px-dm"><div class="wrap">
    <p class="px-eb">REPLAY</p>
    <h2>ระดับงานที่น้องจะได้ทำ</h2>
    <p class="px-lead">StressStrike โดยน้องวิน ชนะเลิศ OBEC Roboplayground และเข้ารอบสุดท้าย TICTA</p>
    <div class="cx-demo px-scr"><video controls playsinline preload="none" poster="img/work-stressstrike.webp" src="https://www.hamsterhub.co/godang/hall-of-fame/videos/stressstrike.mp4"></video></div>
  </div></section>

  <section class="px-sec"><div class="wrap">
    <p class="px-eb">HIGH SCORE</p>
    <h2>รุ่นพี่ที่เรียนกับเราแล้วติดมหาวิทยาลัย</h2>
    <p class="px-lead">DEK69 ติดแล้ว 48 คน สจล. 24 · มหิดล 9 · จุฬาฯ 8 · เกษตรศาสตร์ 7</p>
    <ul class="cx-seniors" id="cxSen"></ul>
  </div></section>

  <section class="px-sec"><div class="wrap px-nr">
    <p class="px-eb">HELP</p>
    <h2>คำถามที่ถามบ่อย</h2>
    <div class="cx-faq">
      <details><summary>ไม่เคยทำเกมเลย เรียนได้ไหม</summary><p>ได้ Rank 1 เริ่มจากศูนย์ สอนตั้งแต่ใช้ Unity และคิดเกมให้สนุก ก่อนขยับไปงานที่ยากขึ้น</p></details>
      <details><summary>ต่างจากคอร์ส Standard ยังไง</summary><p>เนื้อหาครบทุกหัวข้อเท่ากัน Standard เรียน 5 เดือน ราคา 9,990 บาท ส่วน Port Express อัดให้จบใน 2 เดือน ราคา 5,990 บาท สำหรับ ม.6 ที่เวลาก่อนยื่นพอร์ตเหลือน้อย</p></details>
      <details><summary>ผู้ปกครองจะรู้ได้ยังไงว่าลูกไปถึงไหนแล้ว</summary><p>มี Checkpoint 5 ครั้ง แต่ละครั้งบอกว่าผ่านอะไรแล้ว ต้องแก้อะไร ถามความคืบหน้ากับทีมทาง LINE ได้ตลอด</p></details>
      <details><summary>เรียนออนไลน์หรือที่ไหน กี่โมง</summary><p>ดูรายละเอียดได้ที่เว็บ Port Express หรือถามทีมทาง LINE @smart-school</p></details>
    </div>
  </div></section>

  <section class="px-sec px-end"><div class="wrap">
    <p class="pxf px-rd">READY<br>PLAYER?</p>
    <div class="px-bt" style="justify-content:center"><a class="pbtn gold" href="'''+PX+'''" target="_blank" rel="noopener">▶ เข้าเว็บ Port Express</a><a class="pbtn blue" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div>
  </div></section>
  <div class="cx-bar"><span><b>5,990 บาท</b> <s>9,990</s><br><small class="pxst">เริ่ม 9 พ.ย. 2569</small></span><a href="'''+PX+'''" target="_blank" rel="noopener">เข้าเว็บ Port Express</a></div>
</div>

'''
sec('<div data-view="portex">','<!-- ================= ACTIVITY ================= -->',portex)

# ================= ACTIVITY: by status =================
rep('<p>ค่าย เวิร์กชอป การแข่งขัน งานโชว์ผลงาน และโครงการระยะยาว ตลอดทั้งปี ทุกงานน้องได้ลงมือสร้างของจริง</p>','<p>ค่าย เวิร์กชอป การแข่งขัน และงานโชว์ผลงาน ตลอดทั้งปี ทุกงานน้องได้ลงมือสร้างของจริง</p>')
rep('<h2>All for One University รอบชิงชนะเลิศ</h2>','<h2>All for One University รอบชิงชนะเลิศ</h2>')
rep('<span class="k">กิจกรรมถัดไป</span>','<span class="k">กำลังจะมา · กิจกรรมถัดไป</span>')
cut('    <div class="ac-types">','    <div class="ac-list" id="acl"></div>','''    <div class="ac-sh"><h2>จบไปแล้วในปี 2569</h2><p>ดูว่าแต่ละงานน้องๆ ได้ทำอะไร กิจกรรมแบบนี้จะกลับมาอีก กดติดตามได้ท้ายหน้า</p></div>
''')
rep('    <div class="ac-list" id="acl"></div>\n','''    <div class="ac-list" id="acl"></div>
    <div class="ac-fl"><div><b>อยากรู้ก่อนเมื่อมีกิจกรรมใหม่</b><p>ค่าย เวิร์กชอป และการแข่งขัน ประกาศทาง LINE และ Facebook ก่อนที่อื่น</p></div><div class="btns"><a class="btn btn-line" href="'''+LINE+'''" target="_blank" rel="noopener">LINE @smart-school</a><a class="btn btn-s" href="https://www.facebook.com/HamsterHubThailand" target="_blank" rel="noopener">Facebook</a></div></div>
''')
i=s.index("function alist(t){");j=s.index("/* countdowns */",i)
s=s[:i]+"""var MAS={'ค่าย':'n-gamer','เวิร์กชอป':'n-read','แข่งขัน':'n-win','โชว์ผลงาน':'n-walker','โครงการ':'n-maker'},TN={'โครงการ':'โปรเจกต์ส่งประกวด'};
  function alist(){$('#acl').innerHTML=ACT.filter(function(a){return !a[4]}).map(function(a){var im=AIMG[a[1]],c=ACOL[a[3]];
    return '<article class="ev done"><div class="ev-m" style="background:'+c[0]+';color:'+c[1]+'">'+(im?'<img src="img/'+im+'.webp" alt="" loading="lazy"'+(im==='k-afo-logo'?' class="logo"':'')+'>':'<span class="ev-mas"><img src="img/'+MAS[a[3]]+'.webp" alt="" loading="lazy"><em>'+a[1]+'</em></span>')+'<span class="ev-d">'+a[0]+'</span><span class="ev-x">จบแล้ว</span></div><div class="ev-b"><span class="tg" style="color:'+c[1]+'">'+(TN[a[3]]||a[3])+'</span><b>'+a[1]+'</b><p>'+a[2]+'</p></div></article>'}).join('')}
  alist();
  """+s[j:]

# ================= NAV: real classes + new hover personalities =================
rep('<a class="v" href="#courses">คอร์ส</a><a class="v" href="#activity">กิจกรรม</a><a class="v" href="#works">ผลงาน</a><a class="v" href="#about">เกี่ยวกับเรา</a>',
    '<a class="v nv-c" href="#courses"><span>คอร์ส</span></a><a class="v nv-a" href="#activity"><span class="roll"><span>กิจกรรม</span><span class="nx" id="nvNext">ถัดไป 14 พ.ย.</span></span></a><a class="v nv-w" href="#works"><span>ผลงาน</span></a><a class="v nv-b" href="#about"><span>เกี่ยวกับเรา</span></a>')
cut('/* nav: four small personalities */','/* works transition: a phone swipe */','')

# ================= ABOUT: pictures =================
rep('''<figure class="ab-ph rv"><img src="img/ab-photos.webp" alt="น้องๆ Hamster Hub ทั้งในค่ายและออนไลน์" loading="lazy" style="max-width:620px;margin:0 auto"><figcaption>น้องๆ Hamster Hub ทั้งที่ สจล. และในห้องเรียนออนไลน์</figcaption></figure>''',
'''<div class="wrap"><div class="ab-bento rv"><img class="b1" src="img/photo-camp.webp" alt="น้องๆ ในค่าย Hamster Hub" loading="lazy"><img class="b2" src="img/photo-group.webp" alt="น้องๆ ถ่ายรูปรวม" loading="lazy"><img class="b3" src="img/photo-class.webp" alt="ห้องเรียน" loading="lazy"><img class="b4" src="img/photo-desk.webp" alt="น้องกำลังทำผลงาน" loading="lazy"><img class="b5" src="img/s-showcase1.webp" alt="ผลงานที่นำไปโชว์" loading="lazy"></div></div>''')
rep('<div class="do3"><div class="rv"><h3>พาเข้ามหาวิทยาลัย</h3>','<div class="do3"><div class="rv"><img class="do-i" src="img/n-grad.webp" alt="" loading="lazy"><h3>พาเข้ามหาวิทยาลัย</h3>')
rep('<div class="rv"><h3>พาสร้างสตาร์ทอัพ</h3>','<div class="rv"><img class="do-i" src="img/n-biz.webp" alt="" loading="lazy"><h3>พาสร้างสตาร์ทอัพ</h3>')
rep('<div class="rv"><h3>พาลงเวทีจริง</h3>','<div class="rv"><img class="do-i" src="img/n-win.webp" alt="" loading="lazy"><h3>พาลงเวทีจริง</h3>')

# ================= JS =================
# drop the old deck code (deck markup is gone)
i=s.index('  /* DEK69 deck: holo poster on top');j=s.index('  /* hero: three.js 2.5D',i);s=s[:i]+s[j:]
# hero: transparent stage (no room), floor height exported for the cabinet, clicks on hamsters do not open links
rep("R=new T.WebGLRenderer({canvas:cv,antialias:true})","R=new T.WebGLRenderer({canvas:cv,antialias:true,alpha:true})")
rep("bg.position.z=-50;S.add(bg);","bg.position.z=-50;bg.visible=false;S.add(bg);")
rep("uMin=.5-(w/bw)/2+.05;","hx.style.setProperty('--floor',Math.round((1-V0)*bh)+'px');uMin=.5-(w/bw)/2+.05;")
rep("if(down(e,e.clientX,e.clientY)){e.preventDefault();","if(down(e,e.clientX,e.clientY)){window.__hxD=Date.now();e.preventDefault();")
rep("if(down(e,t.clientX,t.clientY))e.preventDefault()},{passive:false});","if(down(e,t.clientX,t.clientY)){window.__hxD=Date.now();e.preventDefault()}},{passive:false});\n    hx.addEventListener('click',function(e){if(Date.now()-(window.__hxD||0)<1500){e.preventDefault();e.stopPropagation()}},true);")
extra='''
  /* Port Express status (starts 9 Nov 2569) */
  (function(){var n=new Date(),a=new Date('2026-11-09T00:00:00+07:00'),b=new Date('2027-01-10T00:00:00+07:00'),t=n<a?'รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569':n<b?'รุ่นนี้กำลังเรียนอยู่ · เริ่ม 9 พ.ย. 2569':'ทัก LINE ถามรอบถัดไป';
    $$('.pxst').forEach(function(e){e.textContent=(e.classList.contains('blink')?'● ':'')+t})})();
  /* AFO tile: after the day it says so */
  (function(){if(new Date()>new Date('2026-11-14T18:00:00+07:00')){var t=$('#afoTag');if(t)t.textContent='เพิ่งจบไป · รอบชิงชนะเลิศ';var c=$('#afoCd');if(c)c.style.display='none';var nv=$('#nvNext');if(nv)nv.textContent='ดูทั้งหมด'}})();
  /* seniors: an always-moving gallery */
  (function(){var tr=$('#sxT');if(!tr)return;var on=null;
    function card(g){return '<figure class="sx-c"><img src="img/dek69-'+g[0]+'.webp" alt="'+g[1]+' '+UN[g[2]]+'" loading="lazy"><figcaption><b>'+g[1]+'</b><span style="--c:'+UC[g[2]]+'">'+UN[g[2]]+'</span><small>'+g[3]+'</small></figcaption></figure>'}
    function fill(){var L=G.filter(function(g){return !on||g[2]===on});var a=L.slice();while(a.length<8)a=a.concat(L);tr.innerHTML=a.concat(a).map(card).join('');tr.style.setProperty('--dur',(a.length*3.2)+'s');
      tr.style.animation='none';void tr.offsetWidth;tr.style.animation=''}
    fill();$$('.sx-u button').forEach(function(b){b.addEventListener('click',function(){on=on===b.dataset.u?null:b.dataset.u;$$('.sx-u button').forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.u===on))});fill()})})})();
'''
rep("  /* router */",extra+"  /* router */")

# ================= fonts =================
rep('family=Anuphan:wght@500;600;700&','family=Anuphan:wght@500;600;700&family=Press+Start+2P&')
rep('  --display:"Anuphan"','  --pixel:"Press Start 2P","Anuphan",monospace;\n  --display:"Anuphan"')

# ================= CSS =================
css=r'''
/* ===== v4 ===== */
.pxf{font-family:var(--pixel);letter-spacing:.02em;line-height:1.15}
/* arcade cabinet */
.arc{display:block;position:relative;width:520px;max-width:100%;text-decoration:none;filter:drop-shadow(0 30px 30px rgba(11,22,64,.25));transition:transform .25s steps(3)}
.arc:hover{transform:translateY(-4px)}
.arc-mq{display:flex;align-items:center;justify-content:center;gap:14px;height:64px;margin:0 22px;background:#140F3A;border:6px solid #0B0A24;border-bottom:0;box-shadow:inset 0 -6px 0 #2D3590}
.arc-mq b{font:400 clamp(.8rem,1.9vw,1.15rem) var(--pixel);color:#FFD24A;text-shadow:0 0 12px rgba(255,210,74,.7),3px 3px 0 #B0306A}
.arc-mq i{width:10px;height:10px;background:#FF4D6D;box-shadow:0 0 10px #FF4D6D;animation:bl .8s steps(1) infinite}
.arc-mq i:last-child{background:#7CF29A;box-shadow:0 0 10px #7CF29A;animation-delay:.4s}
.arc-scr{display:block;position:relative;background:#241E66;padding:16px 16px 18px;border:6px solid #0B0A24;box-shadow:inset 6px 0 0 #3A33A0,inset -6px 0 0 #1A1550}
.arc-scr video{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;background:#05061E;border:4px solid #05061E}
.arc-gl{position:absolute;inset:20px 20px 22px;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,0,0,.14) 0 2px,transparent 2px 4px)}
.arc-pn{display:flex;align-items:center;gap:22px;height:68px;padding:0 26px;margin:0 -10px;background:#2D3590;border:6px solid #0B0A24;clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}
.arc-js{position:relative;width:18px;height:34px;background:#0B0A24}
.arc-js i{position:absolute;left:-7px;top:-12px;width:32px;height:24px;background:#FF4D6D;box-shadow:inset -4px -4px 0 #B0306A}
.arc:hover .arc-js{transform:rotate(-14deg);transform-origin:50% 100%}
.arc-bt{display:flex;gap:10px}.arc-bt i{width:20px;height:20px;background:#FFD24A;box-shadow:inset -3px -3px 0 #B07A00}
.arc-bt i:nth-child(2){background:#7CF29A;box-shadow:inset -3px -3px 0 #2E9E6B}.arc-bt i:nth-child(3){background:#5BC0FF;box-shadow:inset -3px -3px 0 #1D5FB8}
.arc:hover .arc-bt i:nth-child(1){animation:press .3s steps(2) 2}
@keyframes press{50%{transform:translateY(3px);box-shadow:none}}
.arc-cn{margin-left:auto;font:400 .62rem var(--pixel);color:#C9CDE8;animation:bl 1.2s steps(1) infinite}
.arc-ft{display:block;height:26px;margin:0 30px;background:#140F3A;border:6px solid #0B0A24;border-top:0}
/* home hero: Port Express like a product launch */
.hp{padding-top:clamp(56px,7vw,88px);padding-bottom:0;background:#fff;overflow:hidden;--floor:170px}
.hp-txt{text-align:center}
.hp-k{display:inline-flex;align-items:center;gap:8px;font:600 .95rem var(--display);color:#B26A00;background:#FFF4DC;padding:6px 14px;border-radius:999px}
.pxdot{width:8px;height:8px;background:#FF4D6D;animation:bl 1s steps(1) infinite}
.hp-h{font:700 clamp(3rem,8vw,6rem)/1 var(--display);letter-spacing:-.03em;margin-top:18px}
.hp-t{font:600 clamp(1.25rem,2.6vw,1.9rem)/1.35 var(--display);margin-top:14px}
.hp-m{color:var(--mute);margin-top:10px}.hp-m s{color:var(--hair)}
.hp .btns{justify-content:center;margin-top:24px}
.hp-stage{position:relative;margin:40px auto 0;height:clamp(420px,46vw,620px);background:linear-gradient(transparent calc(100% - var(--floor)),#F3EEE6 calc(100% - var(--floor)),#ECE4D8)}
.hp-stage::before{content:"";position:absolute;left:0;right:0;bottom:calc(var(--floor) - 1px);height:2px;background:#E2D7C6}
.hp-arc{position:absolute;left:50%;bottom:calc(var(--floor) - 18px);transform:translateX(-50%);width:min(500px,74%)}
.hp-arc:hover{transform:translate(-50%,-4px)}
.hp .hx3{position:absolute;inset:0;z-index:3;pointer-events:none;background:none;border-radius:0;height:auto}
.hp-tip{position:absolute;left:0;right:0;bottom:8px;text-align:center;color:#9A8B74;font-size:.85rem;z-index:2}
/* apple-style tiles */
.hp-grid{padding:16px 0 0}
.hg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;max-width:1240px}
.tile{position:relative;min-height:560px;border-radius:28px;overflow:hidden;padding:48px 32px 0;text-align:center;display:flex;flex-direction:column;align-items:center;text-decoration:none;color:#fff}
.tile .t-k{font:600 .95rem var(--display);color:#FFD24A}
.tile h3{font:700 clamp(2rem,3.4vw,2.8rem)/1.1 var(--display);margin-top:10px}
.tile .t-s{color:rgba(255,255,255,.88);margin-top:10px;line-height:1.6}
.t-b{display:flex;gap:12px;justify-content:center;margin-top:20px;flex-wrap:wrap;position:relative;z-index:2}
.tb1,.tb2{display:inline-flex;align-items:center;min-height:42px;padding:0 20px;border-radius:999px;font:600 .98rem var(--display);text-decoration:none}
.tb1{background:#fff;color:#0B1640}.tb2{color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.7)}
.tb1:hover{background:#FFD24A}.tb2:hover{background:rgba(255,255,255,.12)}
.t-afo{background:#1068DC;background-image:radial-gradient(rgba(255,255,255,.14) 1.5px,transparent 1.5px);background-size:22px 22px}
.t-afo .afo-hd{margin-top:18px;position:relative}
.t-afo .afo-logo{width:min(100%,340px)}
.t-afo .cd{margin-top:20px;justify-content:center}
.t-wk{background:#0B0B0F;justify-content:flex-start}
.t-wk video{position:absolute;left:0;right:0;bottom:0;width:100%;height:56%;object-fit:cover;-webkit-mask:linear-gradient(transparent,#000 30%);mask:linear-gradient(transparent,#000 30%)}
.t-wk:hover .tb1{background:#FFD24A}
/* seniors: always-moving gallery */
.sx{padding:clamp(80px,10vw,120px) 0;background:#F5F5F7;overflow:hidden}
.sx-h{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}
.sx-h h2{font:700 clamp(2.2rem,4.4vw,3.4rem)/1.12 var(--display);letter-spacing:-.02em}
.sx-u{display:flex;gap:10px;flex-wrap:wrap}
.sx-u button{display:flex;flex-direction:column;align-items:flex-start;min-width:92px;padding:12px 16px;border-radius:18px;border:0;background:#fff;cursor:pointer;box-shadow:0 0 0 1px #E3E3E8;transition:transform .2s,box-shadow .2s}
.sx-u b{font:700 2rem/1 var(--display);color:var(--c)}.sx-u span{font:600 .9rem var(--display);color:var(--mute);margin-top:4px}
.sx-u button:hover{transform:translateY(-3px)}
.sx-u button[aria-pressed="true"]{box-shadow:0 0 0 2.5px var(--c)}
.sx-rail{margin-top:44px;-webkit-mask:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);mask:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.sx-tr{display:flex;gap:20px;width:max-content;animation:sxm var(--dur,60s) linear infinite}
.sx-rail:hover .sx-tr{animation-play-state:paused}
@keyframes sxm{to{transform:translateX(calc(-50% - 10px))}}
.sx-c{margin:0;width:250px;flex:none;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 18px 40px -26px rgba(0,0,0,.35);transition:transform .35s cubic-bezier(.3,1.4,.5,1)}
.sx-c:hover{transform:translateY(-8px) scale(1.03)}
.sx-c img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}
.sx-c figcaption{padding:14px 16px 18px;display:grid;gap:4px}
.sx-c b{font:700 1.1rem var(--display)}
.sx-c span{justify-self:start;font:600 .8rem var(--display);color:#fff;background:var(--c);padding:2px 10px;border-radius:999px}
.sx-c small{color:var(--mute);font-size:.88rem}
.sx-ft{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-top:22px;flex-wrap:wrap}
.sx-ft p{color:var(--mute);font-size:.9rem}
/* courses: Port Express arcade banner + themed cards */
.ct-px{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(24px,4vw,56px);align-items:center;padding:clamp(28px,4vw,48px);background:#0E1040;border-radius:28px;color:#fff;background-image:radial-gradient(rgba(255,255,255,.12) 1px,transparent 1px);background-size:18px 18px;box-shadow:0 0 0 4px #2D3590;margin-top:8px}
.ct-arc{width:100%}
.ct-pi .pxf{font-size:clamp(1.8rem,3.6vw,2.8rem);color:#FFD24A;text-shadow:4px 4px 0 #B0306A;margin-top:12px}
.ct-pt{color:#C9CDE8;margin-top:14px;line-height:1.6}
.ct-pf,.px-st{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 0;padding:0;list-style:none}
.ct-pf li,.px-st li{background:#05061E;box-shadow:0 0 0 3px #2D3590;padding:8px 12px;font:600 .95rem var(--display);color:#fff}
.ct-pf small,.px-st small{display:block;font:400 .55rem var(--pixel);color:#7CF29A;margin-bottom:4px}
.ct-pp{margin-top:18px}.ct-pp b{font:400 1.3rem var(--pixel);color:#FFD24A}.ct-pp s{color:#8A90B8;margin-left:10px}
.ct-pb,.px-bt{display:flex;gap:14px;flex-wrap:wrap;margin-top:20px}
.pbtn.blue{--c:#5BC0FF;--t:#06123A;--s:#1D5FB8}
.cc-m .mo{position:absolute;inset:0;display:grid;place-items:center;font-style:normal;font:800 5rem/1 var(--display);opacity:.9;pointer-events:none}
.th0{background:#FF8A3D}.th0 .mo{color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.75);font-size:9rem}
.th1{background:#1068DC repeating-linear-gradient(115deg,transparent 0 26px,rgba(255,255,255,.12) 26px 30px)}.th1 .mo{color:rgba(255,255,255,.22);font-style:italic;font-size:3.2rem}
.th2{background:radial-gradient(circle at 50% 30%,#2B3A8A,#0B1640)}.th2 .mo{color:#FFD24A;opacity:.3;font-size:6rem;letter-spacing:.1em}
.th3{background:#E6F7EC linear-gradient(rgba(30,122,76,.12) 1px,transparent 1px) 0 0/100% 26px}.th3 .mo{color:rgba(30,122,76,.22);font-size:8rem}
.th4{background:#0D1117}.th4 .mo{font:600 1.6rem ui-monospace,Menlo,monospace;color:#3FB950;place-items:start;padding:18px 20px}
.th5{background:#FFF1D6 radial-gradient(#F3D79B 1.5px,transparent 1.5px) 0 0/16px 16px}.th5 .mo{font-family:var(--pixel);font-size:2.2rem;color:rgba(178,106,0,.25)}
.cc-m img{position:relative;z-index:1}.cc-st{z-index:2}
/* Port Express page: everything is an arcade */
.pxp{background:#0B0B2A;color:#fff;background-image:radial-gradient(rgba(255,255,255,.08) 1px,transparent 1px);background-size:22px 22px}
.px-hero{padding:clamp(40px,6vw,80px) 0}
.px-hg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,5vw,64px);align-items:center}
.px-crumb{color:#8A90B8;font-size:.9rem;margin-bottom:14px}.px-crumb a{color:#C9CDE8}
.px-h{font-size:clamp(2.4rem,5.6vw,4.4rem);color:#FFD24A;text-shadow:5px 5px 0 #B0306A;margin-top:14px}
.px-t{font:700 clamp(1.2rem,2.2vw,1.6rem)/1.4 var(--display);margin-top:18px}
.px-pr{display:flex;align-items:center;gap:14px;margin-top:22px;flex-wrap:wrap}
.px-pr .coin{width:22px;height:22px;background:#FFD24A;box-shadow:inset -4px -4px 0 #B07A00;animation:spin 1s steps(4) infinite}
@keyframes spin{50%{transform:scaleX(.3)}}
.px-pr b{font:400 1.6rem var(--pixel);color:#FFD24A}.px-pr s{color:#8A90B8}.px-pr em{font-style:normal;font:600 .9rem var(--display);color:#06123A;background:#7CF29A;padding:3px 10px}
.px-arc{width:100%}
.px-sec{padding:clamp(64px,8vw,104px) 0;border-top:4px solid #1A1D5C}
.px-eb{font:400 .75rem var(--pixel);color:#7CF29A;letter-spacing:.1em}
.px-sec h2{font:700 clamp(1.9rem,3.6vw,2.8rem)/1.2 var(--display);margin-top:12px}
.px-lead{color:#C9CDE8;max-width:640px;margin-top:12px;line-height:1.7}
.px-tl{display:flex;margin-top:36px;box-shadow:0 0 0 4px #2D3590}
.px-tl span{background:var(--c);color:#14102E;font:400 .7rem var(--pixel);padding:12px 14px;border-right:4px solid #0B0B2A}
.px-tl span:last-child{border:0}.px-tl small{display:block;font:600 .85rem var(--display);margin-top:6px}
.rks{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:24px}
.rk{background:#14185A;box-shadow:0 0 0 4px var(--c),8px 8px 0 4px #05061E;padding:22px 22px 24px;display:flex;flex-direction:column}
.rk header{display:flex;justify-content:space-between;align-items:center}
.rk-n{font:400 .8rem var(--pixel);color:var(--c)}
.rk-m{font:400 .6rem var(--pixel);color:#14102E;background:var(--c);padding:6px 8px}
.rk-w{color:#C9CDE8;margin-top:14px;font-size:.92rem}.rk-w b{color:#fff}
.rk h3{font:700 1.4rem var(--display);margin-top:6px}
.rk ul{list-style:none;margin:16px 0 0;padding:0;display:grid;gap:10px}
.rk li{padding-left:18px;position:relative;color:#C9CDE8;font-size:.92rem;line-height:1.5}
.rk li::before{content:"";position:absolute;left:0;top:7px;width:8px;height:8px;background:var(--c)}
.rk li b{display:block;color:#fff;font:600 .98rem var(--display)}
.rk-l{margin-top:auto;padding-top:18px;font:600 .95rem var(--display);color:var(--c)}
.rk-l small{display:block;font:400 .55rem var(--pixel);color:#7CF29A;margin-bottom:6px}
.cps{list-style:none;padding:0;margin:36px 0 0;display:flex;gap:0;flex-wrap:wrap}
.cps li{flex:1;min-width:110px;position:relative;display:flex;flex-direction:column;align-items:center;gap:10px;font:400 .55rem var(--pixel);color:#8A90B8;padding-top:4px}
.cps li::before{content:"";position:absolute;top:24px;left:0;right:0;height:6px;background:repeating-linear-gradient(90deg,#2D3590 0 10px,transparent 10px 14px)}
.cps i{position:relative;z-index:1;display:grid;place-items:center;width:46px;height:46px;font:400 .9rem var(--pixel);font-style:normal;background:#14185A;color:#fff;box-shadow:0 0 0 4px #5BC0FF}
.cps li.g i{background:#FFD24A;color:#14102E;box-shadow:0 0 0 4px #fff}.cps li.g{color:#FFD24A}
.inv{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:32px}
.inv>div{background:#14185A;box-shadow:0 0 0 4px #2D3590;padding:20px}
.inv .sl{display:grid;place-items:center;width:64px;height:64px;background:#05061E;box-shadow:inset 0 0 0 4px #3A33A0;font:400 .85rem var(--pixel);color:#FFD24A}
.inv b{display:block;font:700 1.1rem var(--display);margin-top:14px}.inv p{color:#C9CDE8;font-size:.92rem;margin-top:4px}
.px-scr{max-width:860px;margin-top:28px;box-shadow:0 0 0 6px #0B0A24,0 0 0 12px #2D3590;border-radius:0!important}
.px-scr video{border-radius:0!important}
.pxp .cx-seniors{margin-top:28px}.pxp .cx-seniors li{background:#14185A;box-shadow:0 0 0 3px #2D3590;border-radius:0;color:#fff}
.pxp .cx-seniors span{color:#C9CDE8}.pxp .cx-seniors em{color:#FFD24A}
.px-nr{max-width:820px}
.pxp .cx-faq details{background:#14185A!important;border:0!important;box-shadow:0 0 0 3px #2D3590;margin-bottom:12px;border-radius:0!important}.pxp .cx-faq summary{color:#fff}.pxp .cx-faq p{color:#C9CDE8}
.px-end{text-align:center}.px-rd{font-size:clamp(2rem,6vw,4rem);color:#FFD24A;text-shadow:5px 5px 0 #B0306A}
.blink.pxst{font:600 .95rem var(--display);color:#7CF29A}
/* activity by status */
.ac-sh{margin-top:56px}.ac-sh h2{font:700 clamp(1.6rem,3vw,2.2rem) var(--display)}.ac-sh p{color:var(--mute);margin-top:6px}
.ac-list{margin-top:24px}
.ev-mas{display:flex;align-items:center;gap:14px;padding:0 20px;width:100%;height:100%}
.ev-mas img{width:42%!important;height:auto!important;object-fit:contain!important;filter:drop-shadow(0 8px 10px rgba(0,0,0,.15))}
.ev-mas em{font:800 clamp(1.1rem,1.7vw,1.4rem)/1.25 var(--display);font-style:normal;text-align:left}
.ev-x{position:absolute;right:12px;top:12px;background:rgba(29,29,31,.82);color:#fff;font:600 .8rem var(--display);padding:4px 10px;border-radius:999px}
.ev.done .ev-m>img{filter:saturate(.85)}
.ac-fl{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin:40px 0 80px;padding:28px 30px;border-radius:24px;background:#F5F5F7}
.ac-fl b{font:700 1.3rem var(--display)}.ac-fl p{color:var(--mute);margin-top:4px}
/* nav: 4 personalities, none repeat */
.nav-in>a.v>span{display:inline-block}
.nav-in>a.nv-c::after{left:0;right:auto;bottom:-2px;height:4px;width:0;transform:none;background:repeating-linear-gradient(90deg,#5B3FD6 0 6px,transparent 6px 8px);transition:none}
.nav-in>a.nv-c:hover::after,.nav-in>a.nv-c[aria-current="page"]::after{width:100%;transition:width .5s steps(6)}
.nav-in>a.nv-c:hover>span{color:#5B3FD6;text-shadow:2px 2px 0 #FFD24A;animation:pxj .4s steps(2) 2}
@keyframes pxj{50%{transform:translate(1px,-2px)}}
.nav-in>a.nv-a>.roll{display:inline-block;position:relative;height:1.5em;clip-path:inset(-3px -80px);vertical-align:bottom}
.nav-in>a.nv-a>.roll>span{display:block;transition:transform .45s cubic-bezier(.5,1.6,.4,1)}
.nav-in>a.nv-a .nx{position:absolute;left:50%;top:0;transform:translate(-50%,110%);color:#FF4D6D;font-weight:600;white-space:nowrap}
.nav-in>a.nv-a:hover>.roll>span:first-child{transform:translateY(-110%)}.nav-in>a.nv-a:hover .nx{transform:translate(-50%,0)}
.nav-in>a.nv-w::after{background:#FF0033;height:3px;bottom:-2px;transform-origin:left}
.nav-in>a.nv-w::before{display:block;content:"";position:absolute;left:0;bottom:-6px;width:11px;height:11px;border-radius:50%;background:#FF0033;opacity:0}
.nav-in>a.nv-w:hover::after{animation:scrub 1.6s linear infinite}.nav-in>a.nv-w:hover::before{opacity:1;animation:head 1.6s linear infinite}
@keyframes scrub{from{transform:scaleX(0)}to{transform:scaleX(1)}}@keyframes head{from{left:-5px}to{left:calc(100% - 5px)}}
@property --sw{syntax:"<angle>";inherits:false;initial-value:0deg}
.nav-in>a.nv-b::after{left:-14px;right:-14px;top:-4px;bottom:-4px;height:auto;transform:none;pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 40' preserveAspectRatio='none'%3E%3Cpath d='M8 22C10 8 60 3 104 9c16 3 14 22-6 26-30 6-80 4-88-8-3-5 6-13 26-15' fill='none' stroke='%23FFB81C' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E") 0 0/100% 100% no-repeat;
  -webkit-mask:conic-gradient(from 200deg,#000 var(--sw),transparent 0);mask:conic-gradient(from 200deg,#000 var(--sw),transparent 0);transition:--sw .5s ease-out}
.nav-in>a.nv-b:hover::after,.nav-in>a.nv-b[aria-current="page"]::after{--sw:360deg}
/* about pictures */
.ab-bento{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:200px 200px;gap:12px;margin-top:40px}
.ab-bento img{width:100%;height:100%;object-fit:cover;border-radius:20px}
.ab-bento .b1{grid-row:1/3}
.do-i{width:110px;height:110px;object-fit:contain;margin-bottom:8px}
.rimg img{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:12px;margin-bottom:10px}
@media (max-width:1000px){.hg,.px-hg,.ct-px{grid-template-columns:minmax(0,1fr)}.rks{grid-template-columns:minmax(0,1fr)}.inv{grid-template-columns:repeat(2,minmax(0,1fr))}.tile{min-height:520px}}
@media (max-width:600px){.hp-stage{height:430px}.hp-arc{width:82%}.arc-mq{height:48px;margin:0 14px}.arc-pn{height:52px;gap:14px;padding:0 16px}.arc-cn{display:none}.arc-scr{padding:10px}
  .tile{min-height:500px;padding:36px 20px 0}.t-wk{min-height:540px}.t-wk video{height:44%}.tile h3{font-size:1.9rem}.inv{grid-template-columns:minmax(0,1fr)}.px-tl small{font-size:.72rem}.px-tl span{font-size:.5rem;padding:10px 8px}.cps li{min-width:33%;margin-bottom:18px}
  .ab-bento{grid-template-columns:1fr 1fr;grid-template-rows:180px 120px 120px}.ab-bento .b1{grid-row:auto;grid-column:1/3}.sx-c{width:200px}
  .th0 .mo{font-size:7rem}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
assert not re.search(r'(?<!\d)1 ธ.ค',s)
open('/home/claude/hamsterhub-home/v4.html','w').write(s)
print('v4 ok',len(s))
