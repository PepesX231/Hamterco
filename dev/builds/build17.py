D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build16.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
LINE='https://page.line.me/jkm4247u?openQrModal=true'
AFO='https://www.hamsterhub.co/allforone'
# ---------- HERO: one big clip that holds everything ----------
i=s.index('  <section class="hb hb2">');j=s.index('  <section class="hp-grid">',i)
s=s[:i]+'''  <section class="hc"><div class="hc-box">
    <video class="hc-v" src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video>
    <span class="hc-sh" aria-hidden="true"></span>
    <div class="hc-tx">
      <p class="hc-logo">PORT EXPRESS</p>
      <h1>เรียน 2 เดือน ได้ผลงานจริง<br><span>ไปยื่นรอบ Portfolio</span></h1>
      <ol class="hc-st"><li><b>1</b>เรียนทำเกมกับพี่ๆ</li><li><b>2</b>ได้ผลงานใส่แฟ้มพอร์ต</li><li><b>3</b>ยื่นรอบ Portfolio ติดมหาลัย</li></ol>
      <p class="hc-p"><b>5,990 บาท</b> <s>9,990</s><span>เริ่ม 9 พ.ย. 2569 · เรียน จันทร์ พุธ ศุกร์</span></p>
      <div class="hc-b"><a class="a1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="a2" href="#portex">ดูรายละเอียด</a></div>
    </div>
    <div class="hc-pr"><span class="fan"><img src="img/dek69-13.webp" alt=""><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""></span><p><b>รุ่นพี่ติดมหาลัยแล้ว 48 คน</b><br>สจล. · จุฬาฯ · มหิดล · เกษตรศาสตร์</p></div>
  </div></section>

'''+s[j:]
# ---------- news + works: stacked full-width, one focus each ----------
rep('<section class="hp-grid"><div class="wrap hg">','<section class="hp-grid"><div class="wrap hg st">')
rep('<p class="t-k" id="afoTag">กิจกรรมถัดไป · รอบชิงชนะเลิศ</p>','<p class="t-k" id="afoTag">ข่าวสาร · กิจกรรมถัดไป</p><h3>All for One University<br>รอบชิงชนะเลิศ</h3>')
# ---------- paths: university goes to courses (many courses, not one) ----------
rep('<a class="f4i rv" href="#portex" style="--bg:#FFF1D6','<a class="f4i rv" href="#courses" style="--bg:#FFF1D6')
s=s.replace('ดู Port Express <b>→</b>','ดูคอร์สทำพอร์ต <b>→</b>',1)
# ---------- courses: show the other courses too ----------
rep('<section class="ct-help">','''<section class="ct-list"><h2>คอร์สอื่นของ Hamster Hub</h2><p>เปิดเป็นรอบ ตอนนี้ยังไม่เปิดรับ กดรับแจ้งเตือนทาง LINE ได้ ภาพคือรุ่นพี่ที่เรียนคอร์สนั้นแล้วติดมหาลัย</p><div class="cgrid" id="crows"></div></section>
    <section class="ct-help">''')
# ---------- activity: no lines; upcoming as a band ----------
i=s.index('    <section class="au">');j=s.index('    <h2 class="er-h">',i)
s=s[:i]+'''    <section class="au2">
      <div class="au2-in">
        <div class="au2-t">
          <p class="au-k" id="auK">กำลังจะมา · 14 พ.ย. 2569</p>
          <h2>All for One University<br>รอบชิงชนะเลิศ</h2>
          <p>ทีมที่ผ่านรอบออนไลน์ มานำเสนอผลงานจริงต่อกรรมการ ที่ IoTE สจล. ลาดกระบัง</p>
          <p class="au-g"><b>น้องได้</b> นำเสนอผลงานบนเวทีจริง เอาไปเล่าในพอร์ตได้</p>
          <div class="au2-c"><span class="cd" id="cdAct"></span><a href="'''+AFO+'''" target="_blank" rel="noopener">ดูรายละเอียดงาน</a></div>
        </div>
        <div class="au2-v"><img class="lg" src="img/k-afo-logo.webp" alt="All for One University"><img class="ic i0" src="img/afo-ic0.webp" alt=""><img class="ic i1" src="img/afo-ic1.webp" alt=""><img class="ic i2" src="img/afo-ic2.webp" alt=""></div>
      </div>
    </section>
    <p class="au-n"><img src="img/ev-st0.webp" alt="">กิจกรรมถัดไปกำลังจะประกาศ <a href="'''+LINE+'''" target="_blank" rel="noopener">รับแจ้งเตือนทาง LINE</a></p>
'''+s[j:]
# ---------- about: real screenshot where we have one ----------
rep('<li class="rv"><img src="img/real-2.webp" alt="" loading="lazy"><b>StressStrike</b>','<li class="rv"><img class="ph" src="img/work-stressstrike.webp" alt="ภาพจากเกม StressStrike" loading="lazy"><b>StressStrike</b>')
rep('<p class="rw-n">ภาพประกอบเป็นภาพวาด</p>','<p class="rw-n">Mr. City, PHC Map และ Hamster Quest ยังใช้ภาพวาดประกอบ รอภาพจริงจากทีม</p>')
# ---------- hall of fame bug: unscope the old avatar rule ----------
s=s.replace('.av{display:flex;flex:none;min-width:112px}','.ql .av{display:flex;flex:none;min-width:112px}')
css=r'''
/* ===== v17 ===== */
.hc{padding:12px 12px 0}
.hc-box{position:relative;overflow:hidden;min-height:max(560px,calc(100svh - 84px));background:#0A0B2E;color:#fff;display:flex;align-items:center}
.hc-v{position:absolute;top:50%;right:0;width:max(205%,calc((100svh - 84px) * 2.2));transform:translateY(-50%);aspect-ratio:16/9;object-fit:cover}
.hc-sh{position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,8,34,.97) 0%,rgba(8,8,34,.95) 46%,rgba(8,8,34,.4) 64%,rgba(8,8,34,0) 78%),linear-gradient(0deg,rgba(8,8,34,.75),transparent 35%)}
.hc-tx{position:relative;z-index:1;padding:clamp(28px,5vw,80px);max-width:720px}
.hc-logo{font:400 clamp(1rem,1.8vw,1.4rem) var(--pixel);color:#FFD24A;text-shadow:3px 3px 0 #E0337E}
.hc h1{font:800 clamp(2.2rem,4.6vw,4.2rem)/1.15 var(--display);letter-spacing:-.025em;margin-top:18px}
.hc h1 span{color:#FFD24A}
.hc-st{list-style:none;margin:28px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px 8px;align-items:center}
.hc-st li{display:flex;align-items:center;gap:10px;font:700 clamp(.95rem,1.3vw,1.1rem) var(--display)}
.hc-st li:not(:last-child)::after{content:"";width:18px;height:14px;margin:0 6px;background:#FFD24A;clip-path:polygon(0 30%,55% 30%,55% 0,100% 50%,55% 100%,55% 70%,0 70%)}
.hc-st b{display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:#7CF29A;color:#0B0720;font:800 .9rem var(--display)}
.hc-p{margin-top:28px}.hc-p b{font:800 clamp(1.8rem,3vw,2.4rem) var(--display);color:#FFD24A}.hc-p s{color:#8A90B8;margin-left:6px}.hc-p span{display:block;color:#C9CDE8;margin-top:2px}
.hc-b{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}
.hc-b a{display:inline-flex;align-items:center;min-height:52px;padding:0 26px;border-radius:999px;font:700 1.05rem var(--display);text-decoration:none;transition:transform .15s,background .2s}
.hc-b a:hover{transform:translateY(-2px)}
.hc-pr{position:absolute;right:clamp(16px,3vw,40px);bottom:clamp(16px,3vw,36px);z-index:1;display:flex;align-items:center;gap:14px;padding:12px 18px 12px 12px;border-radius:999px;background:rgba(10,8,34,.6);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);box-shadow:inset 0 0 0 1px rgba(255,255,255,.15)}
.hc-pr .fan{display:flex}.hc-pr .fan img{width:40px;height:40px;border-radius:50%;object-fit:cover;object-position:60% 40%;border:2px solid #0A0B2E;margin-left:-12px}.hc-pr .fan img:first-child{margin-left:0}
.hc-pr p{font-size:.85rem;color:#C9CDE8;line-height:1.4}.hc-pr b{color:#fff;font-size:.95rem}
/* news + works stacked */
.hg.st{grid-template-columns:minmax(0,1fr)!important}
.hg.st .tile{min-height:clamp(420px,38vw,520px)!important;display:grid!important;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);align-items:center;text-align:left;padding:clamp(28px,5vw,72px)!important;gap:24px 48px}
.hg.st .t-afo>*{grid-column:1}.hg.st .t-afo .afo-hd{grid-column:2;grid-row:1/6;justify-self:center}
.hg.st .t-afo .afo-logo{width:min(100%,480px)}
.hg.st .t-afo .cd,.hg.st .t-b{justify-content:flex-start}
.hg.st .t-wk>*{grid-column:1}.hg.st .t-wk video{left:auto!important;right:0;top:0;bottom:0;width:58%!important;height:100%!important;-webkit-mask:linear-gradient(90deg,transparent,#000 30%)!important;mask:linear-gradient(90deg,transparent,#000 30%)!important}
.hg.st .t-wk{grid-template-rows:auto auto auto auto;align-content:center}
.hg.st .tile h3{margin-top:4px}
/* seniors: stage with spotlight and reflections */
.mc-in{background:radial-gradient(40% 60% at 50% -10%,rgba(255,230,170,.28),transparent 70%),radial-gradient(70% 30% at 50% 100%,rgba(124,90,255,.35),transparent 70%),linear-gradient(#0A0820,#160C3A 60%,#0A0716)!important}
.mc-bg{opacity:.5}
.mc-c img{-webkit-box-reflect:below 10px linear-gradient(transparent 72%,rgba(255,255,255,.22))}
/* courses list back */
.ct-list{margin-top:64px}.ct-list h2{font:800 clamp(1.6rem,3vw,2.2rem) var(--display)}.ct-list>p{color:var(--mute);margin-top:6px}
/* activity: band, no lines */
.au2{margin:24px calc(50% - 50vw) 0;background:#1068DC radial-gradient(rgba(255,255,255,.14) 1.5px,transparent 1.5px) 0 0/22px 22px;color:#fff}
.au2-in{max-width:1120px;margin:0 auto;padding:clamp(44px,6vw,80px) clamp(20px,4vw,40px);display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:32px;align-items:center}
.au2 .au-k{color:#FFD24A}.au2 h2{font:800 clamp(2rem,4vw,3.2rem)/1.12 var(--display);margin-top:8px}
.au2 p{color:rgba(255,255,255,.85);margin-top:12px;line-height:1.6}
.au2 .au-g{color:#fff!important}.au2 .au-g b{color:#7CF29A;margin-right:6px}
.au2-c{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-top:22px}
.au2-c .cd{font:800 1.6rem var(--display);color:#FFD24A;background:none;padding:0}
.au2-c a{color:#0B1640;background:#fff;font-weight:700;text-decoration:none;padding:12px 22px;border-radius:999px}.au2-c a:hover{background:#FFD24A}
.au2-v{position:relative}.au2-v .lg{width:100%;transform:rotate(-4deg);filter:drop-shadow(4px 0 0 #fff) drop-shadow(-4px 0 0 #fff) drop-shadow(0 4px 0 #fff) drop-shadow(0 -4px 0 #fff) drop-shadow(0 24px 30px rgba(0,0,0,.3))}
.au2-v .ic{position:absolute;width:22%;animation:psF 5s ease-in-out infinite}.au2-v .i0{left:-6%;top:-14%}.au2-v .i1{right:-4%;top:-10%;animation-delay:-2s}.au2-v .i2{right:6%;bottom:-18%;animation-delay:-3s}
.er-l{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:36px 28px}
.er{display:grid!important;grid-template-columns:64px minmax(0,1fr)!important;grid-template-rows:auto auto;gap:2px 14px!important;align-items:start!important;border:0!important;padding:0!important}
.er time{grid-column:2;font-size:.85rem}.er-s{grid-row:1/3;width:64px!important}
.er>div{grid-column:2}
@media (max-width:900px){.hc-box{flex-direction:column;align-items:stretch}.hc-v{position:relative;top:auto;transform:none;width:100%}.hc-sh{display:none}.hc-pr{position:relative;right:auto;bottom:auto;margin:0 20px 20px;border-radius:18px}
  .hg.st .tile{grid-template-columns:minmax(0,1fr);text-align:center}.hg.st .t-afo .afo-hd{grid-column:1;grid-row:auto}.hg.st .t-afo .cd,.hg.st .t-b{justify-content:center}.hg.st .t-wk video{width:100%!important;top:auto;height:45%!important;-webkit-mask:linear-gradient(transparent,#000 30%)!important;mask:linear-gradient(transparent,#000 30%)!important}
  .au2-in{grid-template-columns:minmax(0,1fr)}.er-l{grid-template-columns:minmax(0,1fr)}}
@media (min-width:901px) and (max-width:1100px){.er-l{grid-template-columns:repeat(2,minmax(0,1fr))}}
.rw img.ph{aspect-ratio:1;object-fit:cover;border-radius:18px}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v17.html','w').write(s)
print('v17 ok',len(s))
