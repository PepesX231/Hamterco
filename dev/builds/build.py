import re,os
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/v2parts/'
R=lambda f:open(D+f).read()
LINE='https://page.line.me/jkm4247u?openQrModal=true'
shell=R('shell.html').replace('/*CX*/',R('cx.css')).replace('/*TK*/','.yt .tk{--tk-h:calc(100svh - 60px)}\n@media (max-width:900px){.yt .tk{--tk-h:calc(100svh - 118px)}}\n'+R('tk.css')+'\n@media (min-width:1100px){.yt .tk{display:block}}\n.yt .tk-index,.yt .tk-scrim{display:none!important}.yt .tk-all{display:none!important}')

ic={'home':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>',
'shorts':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 9.5v5l4-2.5z" fill="currentColor"/></svg>',
'sen':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg>',
'nsc':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 6H4v1a4 4 0 0 0 4 4M16 6h4v1a4 4 0 0 1-4 4M12 13v4M8 20h8"/></svg>',
'real':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 7h18v13H3z"/><path d="M8 7V4h8v3"/></svg>'}

body='''
<a href="#main" style="position:absolute;left:-999px">ข้ามไปเนื้อหา</a>
<header class="nav"><div class="nav-in">
  <a class="brand" href="#home"><img src="img/logo.webp" alt="" width="30" height="30">Hamster Hub</a>
  <a class="v" href="#courses">คอร์ส</a><a class="v" href="#activity">กิจกรรม</a><a class="v" href="#works">ผลงาน</a><a class="v" href="#about">เกี่ยวกับเรา</a>
  <a class="lbtn" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE</a>
  '''+R('login.html')+'''
  <button class="menu" id="menuBtn" type="button" aria-expanded="false" aria-controls="drawer" aria-label="เปิดเมนู"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 8h16M4 16h16"/></svg></button>
</div>
<nav class="drawer" id="drawer" hidden aria-label="เมนู"><a href="#courses">คอร์ส</a><a href="#activity">กิจกรรม</a><a href="#works">ผลงาน</a><a href="#about">เกี่ยวกับเรา</a><a href="'''+LINE+'''" target="_blank" rel="noopener" style="color:#06C755">ทัก LINE</a><a href="https://www.hamsterhub.co/login" target="_blank" rel="noopener">เข้าสู่ระบบ</a></nav>
</header>

<main id="main">
<!-- ================= HOME ================= -->
<div data-view="home">
  <section class="h-hero"><div class="wrap">
    <p class="h-kick rv">Hamster Hub</p>
    <h1 class="rv">สร้างคนรุ่นใหม่<br>ที่มี<em>ผลงานจริง</em></h1>
    <p class="h-sub rv">ผลงานที่ใช้ได้จริง ขายได้จริง และพาน้องไปถึงมหาวิทยาลัยที่ใช่ ด้วยเกม แอป และ IoT</p>
    <div class="btns rv"><a class="btn btn-p" href="#courses">ดูคอร์สที่เปิดรับ</a><a class="btn btn-s more" href="#works">ดูผลงานของน้องๆ</a></div>
  </div>
  <figure class="h-reel rv"><video src="img/reel.mp4" poster="img/reel-poster.webp" autoplay muted loop playsinline preload="metadata" aria-label="ภาพจากเกมที่น้องๆ Hamster Hub สร้างเอง"></video>
    <figcaption class="h-cap"><span>ภาพทั้งหมดในคลิปนี้มาจาก<b>เกมที่น้องๆ สร้างเอง</b></span><span>SLASH//SPEED · Escape Rolling · Apocalypse Building · Eugation Strike · StressStrike</span></figcaption></figure>
  </section>

  <section class="paths"><div class="wrap">
    <h2 class="rv">น้องอยากไปทางไหน<br>Hamster Hub พาไปได้</h2>
    <div class="tiles">
      <div class="tile rv"><div class="t-in"><p class="t-k">พอร์ตโฟลิโอ</p><h3>ยื่นมหาวิทยาลัย<br>ด้วยผลงานจริง</h3><p>ทำเกมและแอปเก็บเข้าพอร์ต ซ้อมนำเสนอกับอาจารย์มหาวิทยาลัย</p><span class="t-proof">รุ่นพี่ DEK69 ติดแล้ว 48 คน</span>
        <div class="t-l"><a class="more" href="#portex">Port Express</a><a class="more" href="#works" data-pane="sen">ดูรุ่นพี่</a></div></div>
        <div class="t-img"><img src="img/dek69-6.webp" alt="" loading="lazy" style="object-position:50% 25%"></div></div>
      <div class="tile dark rv"><div class="t-in"><p class="t-k">สตาร์ทอัพ</p><h3>จากไอเดีย<br>สู่ของที่ขายได้</h3><p>4 ขั้น ตั้งแต่ออกแบบนวัตกรรม จนต่อยอดเป็นธุรกิจที่มีรายได้</p><span class="t-proof">Mr. City ขายให้สวนสัตว์สงขลาแล้ว</span>
        <div class="t-l"><a class="more" href="#works" data-pane="real">ผลงานที่ใช้งานจริง</a></div></div>
        <div class="t-img"><img src="img/work-stressstrike.webp" alt="" loading="lazy"></div></div>
      <div class="tile rv"><div class="t-in"><p class="t-k">การแข่งขัน</p><h3>ลงเวที<br>ระดับประเทศ</h3><p>ค่าย Game Jam และการแข่งขันที่จัดร่วมกับ สจล.</p><span class="t-proof">12 ผลงานเข้ารอบชิง NSC</span>
        <div class="t-l"><a class="more" href="#activity">ดูกิจกรรม</a><a class="more" href="#works" data-pane="nsc">ผลงาน NSC</a></div></div>
        <div class="t-img"><img src="img/s-showcase1.webp" alt="" loading="lazy"></div></div>
    </div>
  </div></section>

  <section class="proof"><div class="wrap">
    <h2 class="rv">ผลลัพธ์ปี 2568</h2>
    <div class="nums">
      <div class="rv"><b data-count="48">48</b><span>รุ่นพี่ DEK69<br>ติดมหาวิทยาลัยสายคอม</span></div>
      <div class="rv"><b data-count="37">37</b><span>ผลงานที่น้องสร้าง<br>และเผยแพร่ให้คนใช้จริง</span></div>
      <div class="rv"><b data-count="12">12</b><span>ผลงานเข้ารอบชิง<br>การแข่งขันซอฟต์แวร์ระดับประเทศ</span></div>
    </div>
    <p class="src">ข้อมูลจาก 2025 Success Story ของ Hamster Hub</p>
  </div></section>

  <section class="open"><div class="wrap">
    <h2 class="sec-h rv">เปิดรับตอนนี้</h2>
    <div class="open-g">
      <a class="oc rv" href="#portex"><div class="oc-m"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video></div>
        <div class="oc-b"><span class="st">คอร์ส · เปิดรับสมัคร</span><h3>Port Express</h3><p>ทำพอร์ตเกม 2 เดือน สำหรับ ม.6 ได้ 3 เกมพร้อมยื่น</p><div class="oc-f"><span class="pr">5,990 บาท<s>9,990</s></span><span class="more">เริ่ม 1 ธ.ค. ดูรายละเอียด</span></div></div></a>
      <a class="oc rv" href="#activity"><div class="oc-m afo"><img src="img/k-afo-logo.webp" alt="All for One University" loading="lazy"></div>
        <div class="oc-b"><span class="st" style="color:#1068DC">กิจกรรม · รอบชิงชนะเลิศ</span><h3>All for One University</h3><p>14 พ.ย. 2569 ที่ IoTE สจล. ลาดกระบัง</p><div class="oc-f"><span class="pr" id="cdHome">อีก 0 วัน</span><span class="more">ดูกิจกรรม</span></div></div></a>
    </div>
  </div></section>

  <section class="sen">
    <div class="wrap c"><h2 class="sec-h rv">รุ่นพี่ 48 คน ไปถึงคณะที่ใช่แล้ว</h2><p class="sec-sub rv">รุ่น DEK69 ที่ใช้ผลงานจาก Hamster Hub ยื่นรอบ Portfolio</p>
      <div class="ubar rv" aria-hidden="true"><i style="flex:24;background:#E8742A"></i><i style="flex:9;background:#3F5FD0"></i><i style="flex:8;background:#D9558C"></i><i style="flex:7;background:#2E9E6B"></i></div>
      <div class="ulg rv" id="ulg"><button type="button" data-u="all" aria-pressed="true">ทั้งหมด</button><button type="button" data-u="k" aria-pressed="false"><i style="background:#E8742A"></i>สจล. <b>24</b></button><button type="button" data-u="m" aria-pressed="false"><i style="background:#3F5FD0"></i>มหิดล <b>9</b></button><button type="button" data-u="c" aria-pressed="false"><i style="background:#D9558C"></i>จุฬาฯ <b>8</b></button><button type="button" data-u="u" aria-pressed="false"><i style="background:#2E9E6B"></i>เกษตรศาสตร์ <b>7</b></button></div>
    </div>
    <div class="srow-wrap"><div class="srow" id="srow"></div>
      <div class="sarrows"><button type="button" id="sPrev" aria-label="ก่อนหน้า">‹</button><button type="button" id="sNext" aria-label="ถัดไป">›</button></div></div>
  </section>

  <section class="hof"><div class="wrap">
    <h2 class="sec-h rv">Hall of Fame 2569</h2><p class="sec-sub rv">10 ผลงานเด่นของปี คัดจากผลงานทั้งหมด 37 ชิ้น</p>
    <div class="hgrid" id="hgrid"></div>
    <div class="btns rv"><a class="btn btn-w" href="#works" style="background:#fff;color:#0B0B0F">ดูผลงานทั้งหมด</a></div>
  </div></section>

  <section class="ptn"><div class="wrap"><p>จัดกิจกรรมร่วมกับ</p><div class="logos"><img src="img/p-it.webp" alt="คณะเทคโนโลยีสารสนเทศ สจล." loading="lazy"><img src="img/p-iote.webp" alt="IoTE สจล." loading="lazy"><img src="img/p-eduverse.webp" alt="EDUverse" loading="lazy"></div></div></section>
</div>

<!-- ================= COURSES ================= -->
<div data-view="courses">
  <div class="wrap">
    <section class="ct-h"><h1>คอร์ส</h1><p>ทุกคอร์สจบด้วยผลงานจริงที่เอาไปใช้ได้ ทั้งยื่นมหาวิทยาลัย ลงแข่ง และต่อยอด</p></section>
    <a class="ct-feat" href="#portex"><div class="m"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video></div>
      <div class="b"><span class="st">เปิดรับสมัคร</span><h2>Port Express</h2><p>คอร์สทำพอร์ตเกม 2 เดือน สำหรับน้อง ม.6 ที่ยังไม่มีพอร์ต</p>
        <div class="facts"><span>เริ่ม 1 ธ.ค. 2569</span><span>จันทร์ พุธ ศุกร์</span><span>ได้ 3 เกม</span></div>
        <p class="pr">5,990 บาท<s>9,990</s></p><span class="go">ดูรายละเอียดคอร์ส</span></div></a>
    <section class="ct-list"><h2>คอร์สอื่นของ Hamster Hub</h2><p>เปิดรับเป็นรอบ กดรับแจ้งเตือนทาง LINE เมื่อเปิดรอบใหม่</p><div id="crows" style="margin-top:14px"></div></section>
    <section class="ct-help"><h2>ไม่แน่ใจว่าคอร์สไหนเหมาะ</h2><p>บอกทีมว่าน้องเรียนชั้นไหนและอยากไปทางไหน ทีมจะแนะนำให้</p><div class="btns"><a class="btn btn-line" href="'''+LINE+'''" target="_blank" rel="noopener">ปรึกษาทีมทาง LINE</a></div></section>
  </div>
</div>

'''+R('portex.html')+'''

<!-- ================= ACTIVITY ================= -->
<div data-view="activity">
  <div class="wrap">
    <section class="ac-h"><h1>กิจกรรม</h1><p>ค่าย เวิร์กชอป การแข่งขัน งานโชว์ผลงาน และโครงการระยะยาว ตลอดทั้งปี ทุกงานน้องได้ลงมือสร้างของจริง</p></section>
    <a class="ac-next" href="https://www.hamsterhub.co/allforone" target="_blank" rel="noopener"><div class="m"><img src="img/k-afo-logo.webp" alt="All for One University" loading="lazy"></div>
      <div class="b"><span class="k">กิจกรรมถัดไป</span><h2>All for One University รอบชิงชนะเลิศ</h2><p>14 พ.ย. 2569 ที่ IoTE สจล. ลาดกระบัง ทีมที่ผ่านรอบออนไลน์นำผลงานจริงมานำเสนอต่อคณะกรรมการ</p><span class="cd" id="cdAct">อีก 0 วัน</span><span class="more" style="color:#7DB7FF">ดูรายละเอียดงาน</span></div></a>
    <div class="ac-types">
      <div><b>ค่าย</b><p>2–5 วัน ทำผลงานให้เสร็จพร้อมรุ่นพี่ดูแล</p></div>
      <div><b>เวิร์กชอป</b><p>เรียนทักษะเฉพาะเรื่องในวันเดียว</p></div>
      <div><b>แข่งขันและ Game Jam</b><p>สร้างผลงานในเวลาจำกัด แล้วนำเสนอต่อกรรมการ</p></div>
      <div><b>โครงการระยะยาว</b><p>ทำโปรเจกต์ส่งเวทีระดับประเทศหลายเดือน</p></div>
    </div>
    <div class="ac-f" id="acf" role="group" aria-label="กรองกิจกรรม"><button type="button" data-t="all" aria-pressed="true">ทั้งหมด</button><button type="button" data-t="ค่าย" aria-pressed="false">ค่าย</button><button type="button" data-t="เวิร์กชอป" aria-pressed="false">เวิร์กชอป</button><button type="button" data-t="แข่งขัน" aria-pressed="false">แข่งขันและ Game Jam</button><button type="button" data-t="โชว์ผลงาน" aria-pressed="false">โชว์ผลงาน</button><button type="button" data-t="โครงการ" aria-pressed="false">โครงการ</button></div>
    <div class="ac-list" id="acl"></div>
  </div>
</div>

<!-- ================= WORKS ================= -->
<div data-view="works">
  <div class="yt">
    <aside class="yt-side" aria-label="หมวดผลงาน">
      <button type="button" data-pane="hof" aria-current="true">'''+ic['home']+'''Hall of Fame</button>
      <button type="button" data-pane="shorts">'''+ic['shorts']+'''ดูแบบเลื่อน</button>
      <hr><small>สำรวจ</small>
      <button type="button" data-pane="sen">'''+ic['sen']+'''รุ่นพี่ที่ติดมหาลัย</button>
      <button type="button" data-pane="nsc">'''+ic['nsc']+'''ผลงานเข้ารอบ NSC</button>
      <button type="button" data-pane="real">'''+ic['real']+'''ผลงานที่ใช้งานจริง</button>
    </aside>
    <div class="yt-main">
      <section class="yt-pane on" data-p="hof"><div class="yt-pad"><h1>Hall of Fame 2569</h1><p>10 ผลงานเด่นของปี กดที่ผลงานเพื่อดูคลิป</p>
        <div class="chips" id="hofChips"><button type="button" data-f="all" aria-pressed="true">ทั้งหมด</button><button type="button" data-f="vid" aria-pressed="false">มีคลิปผลงาน</button><button type="button" data-f="aw" aria-pressed="false">ได้รางวัล</button></div>
        <div class="vgrid" id="vgrid"></div></div></section>
      <section class="yt-pane" data-p="shorts">'''+R('tk.html')+'''</section>
      <section class="yt-pane" data-p="sen"><div class="yt-pad"><h1>รุ่นพี่ DEK69 ที่ติดมหาวิทยาลัย</h1><p>รุ่นพี่ทั้งหมด 48 คน ด้านล่างคือคนที่ประกาศโปสเตอร์แล้ว 17 คน</p><div class="chips" id="senChips"></div><div class="sgrid" id="sgrid"></div></div></section>
      <section class="yt-pane" data-p="nsc"><div class="yt-pad"><h1>ผลงานเข้ารอบชิง NSC</h1><p>NSC คือการแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย ผลงานของน้องๆ เข้ารอบชิง 12 ผลงาน</p>
        <div class="nsc">'''+''.join('<div>%s</div>'%t for t in ["Revoice","mrCity","Whiskered Odyssey","Noar","Veggie Dash","Time Keeper","Ayutthaya","Shadow Maze","Plant Create World","Salmon Crisis","Z.O.O","Lyno"])+'''</div>
        <div class="nsc-img"><img src="img/s-showcase1.webp" alt="Revoice และ Lyno" loading="lazy"><img src="img/s-showcase2.webp" alt="Time Keeper และ Z.O.O" loading="lazy"></div></div></section>
      <section class="yt-pane" data-p="real"><div class="yt-pad"><h1>ผลงานที่ใช้งานจริง</h1><p>ไม่ได้หยุดแค่ในห้องเรียน ผลงานเหล่านี้มีคนใช้หรือซื้อไปแล้ว</p>
        <div class="real"><div><b>Mr. City</b><p>เกมส่งเสริมการท่องเที่ยวสงขลา ขายให้สวนสัตว์สงขลาแล้ว</p></div><div><b>PHC Map</b><p>เกมสอนเขียน Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน</p></div><div><b>Hamster Quest</b><p>แพลตฟอร์มเรียนแบบเกม กำลังเตรียมใช้กับมหาวิทยาลัย</p></div><div><b>โปรเจกต์สวนลุม</b><p>เปลี่ยนการออกกำลังกายตอนเย็นให้เป็นเกม</p></div></div></div></section>
    </div>
  </div>
</div>

<!-- ================= ABOUT ================= -->
<div data-view="about">
  <section class="ab-h"><div class="wrap"><h1 class="rv">Hamster Hub คือผู้คน<br>ที่สร้างเด็กให้มีผลงานจริง</h1>
    <p class="rv">ผลงานที่ใช้ได้จริง ขายได้จริง และพาไปถึงมหาวิทยาลัยที่ใช่ เราสอน พาสร้าง และพาลงเวทีจริง ตั้งแต่เกม แอป จนถึง IoT</p></div>
    <figure class="ab-ph rv"><img src="img/ab-photos.webp" alt="น้องๆ Hamster Hub ทั้งในค่ายและออนไลน์" loading="lazy" style="max-width:620px;margin:0 auto"><figcaption>น้องๆ Hamster Hub ทั้งที่ สจล. และในห้องเรียนออนไลน์</figcaption></figure></section>
  <section class="ab-do"><div class="wrap"><h2 class="sec-h rv">เราทำอะไร</h2>
    <div class="do3"><div class="rv"><h3>พาเข้ามหาวิทยาลัย</h3><p>คอร์สทำพอร์ต ซ้อมนำเสนอกับอาจารย์มหาวิทยาลัย รุ่นพี่ DEK69 ติดแล้ว 48 คน</p><a class="more" href="#courses">ดูคอร์ส</a></div>
      <div class="rv"><h3>พาสร้างสตาร์ทอัพ</h3><p>4 ขั้นจากออกแบบนวัตกรรม พัฒนาผลงาน จนต่อยอดเป็นธุรกิจที่มีรายได้</p><a class="more" href="#works" data-pane="real">ผลงานที่ใช้งานจริง</a></div>
      <div class="rv"><h3>พาลงเวทีจริง</h3><p>ค่าย Game Jam และการแข่งขันร่วมกับ สจล. ผลงานเข้ารอบชิง NSC 12 ผลงาน</p><a class="more" href="#activity">ดูกิจกรรม</a></div></div></div></section>
  <section class="ab-real"><div class="wrap"><h2 class="sec-h rv">ผลงานที่ออกไปอยู่ในโลกจริง</h2>
    <div class="rgrid"><div class="rv"><b>Mr. City</b><p>เกมส่งเสริมการท่องเที่ยวสงขลา ขายให้สวนสัตว์สงขลาแล้ว</p></div><div class="rv"><b>PHC Map</b><p>เกมสอน Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน</p></div><div class="rv"><b>StressStrike</b><p>ชนะเลิศ OBEC Roboplayground และเข้ารอบสุดท้าย TICTA</p></div><div class="rv"><b>Hamster Quest</b><p>แพลตฟอร์มเรียนแบบเกม กำลังเตรียมใช้กับมหาวิทยาลัย</p></div></div></div></section>
  <section class="ab-res"><div class="wrap"><h2 class="sec-h rv">2025 Success Story</h2><img class="rv" src="img/s-success.webp" alt="สรุปผลลัพธ์ปี 2025 ของ Hamster Hub" loading="lazy"></div></section>
  <section class="ptn"><div class="wrap"><p>จัดกิจกรรมร่วมกับ</p><div class="logos"><img src="img/p-it.webp" alt="คณะเทคโนโลยีสารสนเทศ สจล." loading="lazy"><img src="img/p-iote.webp" alt="IoTE สจล." loading="lazy"><img src="img/p-eduverse.webp" alt="EDUverse" loading="lazy"></div></div></section>
  <section class="ab-ct"><div class="wrap"><h2>คุยกับทีม Hamster Hub</h2><p>ถามเรื่องคอร์ส กิจกรรม หรือการร่วมงานได้ทาง LINE</p>
    <div class="btns"><a class="btn btn-line" href="'''+LINE+'''" target="_blank" rel="noopener">LINE @smart-school</a><button type="button" class="cprow" data-copy="@smart-school">คัดลอก LINE ID <span></span></button></div>
    <div class="btns" style="margin-top:14px"><a class="more" style="color:#9CC3FF" href="https://www.facebook.com/HamsterHubThailand" target="_blank" rel="noopener">Facebook</a><a class="more" style="color:#9CC3FF" href="https://www.instagram.com/hamsterhub_ig/" target="_blank" rel="noopener">Instagram</a></div></div></section>
</div>
</main>

<footer><div class="wrap">
  <div class="fcols">
    <div><h4>คอร์ส</h4><ul><li><a href="#portex">Port Express</a></li><li><a href="#courses">คอร์สทั้งหมด</a></li></ul></div>
    <div><h4>กิจกรรม</h4><ul><li><a href="#activity">กิจกรรมทั้งหมด</a></li><li><a href="https://www.hamsterhub.co/allforone" target="_blank" rel="noopener">All for One University</a></li></ul></div>
    <div><h4>ผลงาน</h4><ul><li><a href="#works">Hall of Fame</a></li><li><a href="#works" data-pane="sen">รุ่นพี่ DEK69</a></li></ul></div>
    <div><h4>ติดต่อ</h4><ul><li><a href="'''+LINE+'''" target="_blank" rel="noopener">LINE @smart-school</a></li><li><a href="https://www.facebook.com/HamsterHubThailand" target="_blank" rel="noopener">Facebook</a></li><li><a href="https://www.instagram.com/hamsterhub_ig/" target="_blank" rel="noopener">Instagram</a></li></ul></div>
  </div>
  <p class="flegal">© 2569 Hamster Hub · ตัวเลขจาก 2025 Success Story ของ Hamster Hub</p>
</div></footer>
'''

AWARDS={'stressstrike':'ชนะเลิศ OBEC Roboplayground'}
VID=['stressstrike','eugation-strike','slash-speed','apocalypis-building','escape-rolling']
ACT=[('14 พ.ย. 2569','All for One University รอบชิงชนะเลิศ','รอบออนไซต์ที่ IoTE สจล.','แข่งขัน',1),
('7 พ.ย. 2569','IoTE KMITL 2026 Showcase (Hallow Open House)','โชว์ผลงานออนไลน์ ไลฟ์ YouTube เข้าร่วมฟรี','โชว์ผลงาน',0),
('ต.ค. 2569','All for One University รอบออนไลน์','แข่งสร้างผลงานเทค 4 วันด้วย AI','แข่งขัน',0),
('14–16 ส.ค.','SciGame Lab Camp','ค่ายสร้างเกมวิทยาศาสตร์','ค่าย',0),
('31 มี.ค. – 31 ก.ค.','NSC Software Project 2026','ทำโปรเจกต์ส่งการแข่งขันซอฟต์แวร์ระดับประเทศ','โครงการ',0),
('20 มิ.ย.','AI for Business','เวิร์กชอปใช้ AI ในธุรกิจ','เวิร์กชอป',0),
('19–21 มิ.ย.','AI Camp Season 2','สร้างเกมหรือเว็บด้วย AI ใน 3 วัน สาย Unity / Roblox / Web App','ค่าย',0),
('10–12 มิ.ย.','Game Pee Camp','ค่ายสร้างเกมสยองขวัญ','ค่าย',0),
('1–29 มิ.ย.','StarLight','โครงการพัฒนาผลงานตลอดเดือน','โครงการ',0),
('8–13 พ.ค.','Intelligence Camp EP-2','ค่ายพัฒนาทักษะ','ค่าย',0),
('24–27 เม.ย.','GameJam X ปีที่ 5','แข่งสร้างเกมในเวลาจำกัด','แข่งขัน',0),
('20–22 มี.ค.','Dek-70 Camp','ค่ายเตรียมพอร์ตสำหรับ DEK70','ค่าย',0),
('13–15 มี.ค.','Intelligence Camp','ค่ายพัฒนาทักษะ','ค่าย',0),
('27 ก.พ. – 6 มี.ค.','Python x Hunter Camp','ค่ายเขียน Python','ค่าย',0),
('30 ม.ค. – 1 ก.พ.','Dek70 Camp','ค่ายเตรียมพอร์ตสำหรับ DEK70','ค่าย',0),
('23–25 ม.ค.','Tech Booster for Teens','เวิร์กชอปเทคโนโลยีสำหรับวัยรุ่น','เวิร์กชอป',0),
('12–16 ม.ค.','Python Adventure Camp','ค่ายเขียน Python แบบผจญภัย','ค่าย',0),
('10–11 ม.ค.','Kid Day','กิจกรรมวันเด็ก','เวิร์กชอป',0)]
import json
js='''
<script>
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $=function(s){return document.querySelector(s)},$$=function(s){return Array.prototype.slice.call(document.querySelectorAll(s))};
'''+R('data.js')+'''
  var AW='''+json.dumps(AWARDS,ensure_ascii=False)+''',VID='''+json.dumps(VID)+''',ACT='''+json.dumps(ACT,ensure_ascii=False)+''';
  var NK={stressstrike:['วิน','นายอัศวิน วิทูรย์ นิตยวรรธนะ'],'beyond-the-board':['กัปตัน','นายเพชรรัตน์ โกรเพ็ชร'],'eugation-strike':['ไผ่','นายณัฐภัทร์ ผลพิบูลสุนทร'],'slash-speed':['ดินสอ','นายชสาส เล่ามาขาว'],'micro-immersive-sim':['เพชร','นายสุวิจักษณ์ จันทร์รุ่งวิจิตต์'],'phi-krahang':['นนท์','นายธนดล นนสิทธิ์'],'midnight-at-roadside':['Windy','นายทัศน์ เล่าพัฒนาเกษม'],'hot-hot-hot':['โอม','นายวรวิช รุ่งปิน'],'apocalypis-building':['ฟาร์','นายรามิตร บุตรลักษณ์'],'escape-rolling':['เป๊ป','นายคชพล จิรธรานนท์']};
  var LINE='%LINE%';
  function card(w,i,cls){var n=NK[w[0]],v=VID.indexOf(w[0])>-1,a=AW[w[0]];
    return '<button type="button" class="'+cls+'" data-i="'+i+'" data-vid="'+(v?1:0)+'" data-aw="'+(a?1:0)+'"><span class="th"><img src="img/work-'+w[0]+'.webp" alt="" loading="lazy">'+(v?'<span class="badge pl">▶ มีคลิป</span>':'')+'</span><span class="by"><span class="av">'+n[0].charAt(0)+'</span><span><b>'+w[1]+'</b><span>@'+n[0]+' · '+n[1]+'</span>'+(a?'<span class="aw">'+a+'</span>':'<span>ผลงานปี 2569</span>')+'</span></span></button>'}
  /* home: hall of fame grid (6) */
  var hg=$('#hgrid');if(hg)hg.innerHTML=W.slice(0,6).map(function(w,i){return card(w,i,'hw rv')}).join('').replace(/class="badge pl"/g,'class="pl"');
  /* works: grid */
  $('#vgrid').innerHTML=W.map(function(w,i){return card(w,i,'vc')}).join('');
  $$('#hofChips button').forEach(function(b){b.addEventListener('click',function(){$$('#hofChips button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});var f=b.dataset.f;$$('#vgrid .vc').forEach(function(c){c.hidden=!(f==='all'||(f==='vid'&&c.dataset.vid==='1')||(f==='aw'&&c.dataset.aw==='1'))})})});
  /* seniors */
  var mix=[5,0,12,10,2,6,13,11,3,7,14,1,8,15,4,9,16];
  function sfig(g){return '<figure data-u="'+g[2]+'"><img src="img/dek69-'+g[0]+'.webp" alt="'+g[1]+'" loading="lazy"><figcaption><b>'+g[1]+'</b><span>'+g[3]+' · '+UN[g[2]]+'<br>คอร์ส '+g[4]+'</span></figcaption></figure>'}
  $('#srow').innerHTML=mix.map(function(i){return sfig(G[i])}).join('');
  $('#sgrid').innerHTML=G.map(sfig).join('');
  $('#senChips').innerHTML='<button type="button" data-u="all" aria-pressed="true">ทั้งหมด 17</button>'+['k','m','c','u'].map(function(k){return '<button type="button" data-u="'+k+'" aria-pressed="false">'+UN[k]+' '+G.filter(function(g){return g[2]===k}).length+'</button>'}).join('');
  function ufilter(btns,figs){btns.forEach(function(b){b.addEventListener('click',function(){btns.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});figs().forEach(function(f){f.hidden=!(b.dataset.u==='all'||f.dataset.u===b.dataset.u)})})})}
  ufilter($$('#ulg button'),function(){return $$('#srow figure')});ufilter($$('#senChips button'),function(){return $$('#sgrid figure')});
  $('#sPrev').addEventListener('click',function(){$('#srow').scrollBy({left:-480,behavior:'smooth'})});$('#sNext').addEventListener('click',function(){$('#srow').scrollBy({left:480,behavior:'smooth'})});
  /* courses list */
  var C=[['Port70','คอร์สทำพอร์ตสำหรับน้อง DEK70'],['Project Express','ทำโปรเจกต์ให้เสร็จไวเพื่อยื่นพอร์ต'],['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ'],['Business Project','ทำโปรเจกต์ที่ต่อยอดเป็นธุรกิจ'],['Python Pro Pack','เรียนเขียนโปรแกรมด้วย Python'],['Hamstarter','คอร์สเริ่มต้นสำหรับคนที่ยังไม่มีผลงาน']];
  $('#crows').innerHTML=C.map(function(c){var al=G.filter(function(x){return x[4]===c[0]}),us=al.map(function(x){return UN[x[2]]}).filter(function(v,k,a){return a.indexOf(v)===k});
    return '<div class="crow"><div><b>'+c[0]+'</b><p>'+c[1]+'</p>'+(al.length?'<p class="al">รุ่นพี่จากคอร์สนี้ติด '+us.join(' ')+'</p>':'')+'</div><a href="'+LINE+'" target="_blank" rel="noopener">แจ้งเตือนเมื่อเปิดรอบ</a></div>'}).join('');
  /* activity list */
  function alist(t){$('#acl').innerHTML=ACT.filter(function(a){return t==='all'||a[3]===t}).map(function(a){return '<div class="arow"><span class="d">'+a[0]+'</span><div><b>'+a[1]+'</b><p>'+a[2]+'</p></div><span class="tg"'+(a[4]?' style="background:#FFB81C;color:#0B1640"':'')+'>'+(a[4]?'กำลังจะมาถึง':a[3])+'</span></div>'}).join('')}
  alist('all');$$('#acf button').forEach(function(b){b.addEventListener('click',function(){$$('#acf button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});alist(b.dataset.t)})});
  /* countdowns */
  function cd(){var d=Math.ceil((new Date('2026-11-14T09:00:00+07:00')-new Date())/864e5),t=d>0?'อีก '+d+' วัน':'วันนี้';['#cdHome','#cdAct'].forEach(function(s){var e=$(s);if(e)e.textContent=t})}cd();
  /* portex seniors */
  var cs=$('#cxSen');if(cs)cs.innerHTML=[5,6,9,0,12,10,3,15].map(function(i){var g=G[i];return '<li><img src="img/dek69-'+g[0]+'.webp" alt="'+g[1]+'" loading="lazy"><b>'+g[1]+'</b><span>'+g[3]+'<br>'+UN[g[2]]+'</span><em>เรียนคอร์ส '+g[4]+'</em></li>'}).join('');
  /* copy */
  document.addEventListener('click',function(e){var b=e.target.closest('[data-copy]');if(!b)return;var t=b.dataset.copy,done=function(){var o=b.firstChild.textContent;b.firstChild.textContent='คัดลอกแล้ว ';setTimeout(function(){b.firstChild.textContent=o},1600)};
    if(navigator.clipboard)navigator.clipboard.writeText(t).then(done,done);else done()});
  /* works panes */
  function pane(p){$$('.yt-side button').forEach(function(b){b.setAttribute('aria-current',String(b.dataset.pane===p))});$$('.yt-pane').forEach(function(s){s.classList.toggle('on',s.dataset.p===p)})}
  $$('.yt-side button').forEach(function(b){b.addEventListener('click',function(){pane(b.dataset.pane);scrollTo(0,0)})});
  $('#vgrid').addEventListener('click',function(e){var c=e.target.closest('.vc');if(!c)return;pane('shorts');scrollTo(0,0);var i=+c.dataset.i;setTimeout(function(){var b=document.querySelector('.tk-index-btn[data-tk-go="'+(i+1)+'"]');if(b)b.click()},80)});
  if(hg)hg.addEventListener('click',function(e){var c=e.target.closest('.hw');if(!c)return;pendingPane=['shorts',+c.dataset.i];location.hash='works'});
  var pendingPane=null;
  document.addEventListener('click',function(e){var a=e.target.closest('a[data-pane]');if(a)pendingPane=[a.dataset.pane]});
  /* reveal + count */
  function count(el){var to=+el.dataset.count;if(reduce||!to)return;var t0=null;el.textContent='0';(function f(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/1100);el.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(performance.now())}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;e.target.classList.add('in');Array.prototype.forEach.call(e.target.querySelectorAll('[data-count]'),count);io.unobserve(e.target)})},{rootMargin:'0px 0px -8% 0px'});
  function arm(){$$('[data-view].on .rv:not(.in)').forEach(function(el){io.observe(el)})}
  /* router */
  var views=['home','courses','portex','activity','works','about'],menuBtn=$('#menuBtn'),drawer=$('#drawer');
  var titles={home:'Hamster Hub',courses:'คอร์ส | Hamster Hub',portex:'Port Express | Hamster Hub',activity:'กิจกรรม | Hamster Hub',works:'ผลงาน | Hamster Hub',about:'เกี่ยวกับเรา | Hamster Hub'};
  function show(){var h=(location.hash||'#home').slice(1);if(views.indexOf(h)<0)h='home';
    $$('[data-view]').forEach(function(v){v.classList.toggle('on',v.dataset.view===h)});
    $$('.nav-in a.v').forEach(function(a){if(a.getAttribute('href')==='#'+(h==='portex'?'courses':h))a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
    document.title=titles[h];drawer.hidden=true;menuBtn.setAttribute('aria-expanded','false');window.scrollTo(0,0);
    if(h==='works'){var pp=pendingPane||['hof'];pendingPane=null;pane(pp[0]);if(pp[1]!=null)setTimeout(function(){var b=document.querySelector('.tk-index-btn[data-tk-go="'+(pp[1]+1)+'"]');if(b)b.click()},120)}
    $$('video[autoplay]').forEach(function(v){if(v.closest('[data-view].on')){var p=v.play();if(p&&p.catch)p.catch(function(){})}else v.pause()});
    arm()}
  menuBtn.addEventListener('click',function(){var o=drawer.hidden;drawer.hidden=!o;menuBtn.setAttribute('aria-expanded',String(o))});
  addEventListener('hashchange',show);show();
})();
</script>
<script>
'''+R('tk.js')+'''
</script>
'''
js=js.replace('%LINE%',LINE)
open('/home/claude/hamsterhub-home/v2.html','w').write(shell+body+js)
print('ok',len(shell+body+js))
