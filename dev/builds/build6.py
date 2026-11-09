D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build5.py').read())          # -> v5, s holds it; cab() available
AFO='https://www.hamsterhub.co/allforone'

cut('  <section class="h-hero h5" id="hx">','  <section class="paths">','''  <section class="h-hero ar" id="hx">
    <div class="ar-wall" aria-hidden="true"><span class="ar-neon">HAMSTER HUB ARCADE</span></div>
    <div class="wrap ar-in">
      <div class="ar-txt">
        <p class="ar-k rv"><span class="pxdot"></span><span class="pxst">รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</span></p>
        <h1 class="rv">Port Express</h1>
        <p class="ar-t rv">ม.6 ยังไม่มีพอร์ต?<br>เรียน 2 เดือน ได้เกม 3 งาน พร้อมยื่นมหาลัย</p>
        <ul class="ar-f rv"><li><b>5,990 บาท</b><s>9,990</s></li><li><b>จ · พ · ศ</b>วันเรียน</li><li><b>5 ครั้ง</b>ตรวจงานกับอาจารย์มหาลัย</li></ul>
        <p class="ar-h rv">กดปุ่มบนตู้ได้เลย ▸</p>
      </div>
      <div class="ar-m">'''+cab('c-hero')+'''</div>
    </div>
    <div class="ar-floor" aria-hidden="true"></div>
    <div class="hx3" id="hx3" aria-hidden="true"><canvas id="hxCanvas"></canvas><div class="hx-say" id="hxSay"></div></div>
    <p class="ar-tip">ลองกดค้างที่น้องหนูแล้วยกขึ้นมาดูสิ</p>
  </section>

  <section class="hp-grid"><div class="wrap hg">
    <div class="tile t-afo rv">
      <p class="t-k" id="afoTag">กิจกรรมถัดไป · รอบชิงชนะเลิศ</p>
      <div class="afo-hd"><img class="afo-logo" src="img/k-afo-logo.webp" alt="All for One University" loading="lazy"><img class="afo-ic i0" src="img/afo-ic0.webp" alt="" aria-hidden="true"><img class="afo-ic i1" src="img/afo-ic1.webp" alt="" aria-hidden="true"><img class="afo-ic i2" src="img/afo-ic2.webp" alt="" aria-hidden="true"></div>
      <p class="t-s">14 พ.ย. 2569 · IoTE KMITL 2026 Showcase ที่ สจล.<br>ทีมที่ผ่านรอบออนไลน์มานำเสนอผลงานจริงต่อกรรมการ</p>
      <div class="cd" id="afoCd" aria-label="นับถอยหลังถึงวันแข่ง"><div><b id="cdD">0</b><span>วัน</span></div><div><b id="cdH">0</b><span>ชั่วโมง</span></div><div><b id="cdM">0</b><span>นาที</span></div></div>
      <div class="t-b"><a class="tb1" href="'''+AFO+'''" target="_blank" rel="noopener">รายละเอียดงาน</a><a class="tb2" href="#activity">กิจกรรมทั้งหมด</a></div>
    </div>
    <a class="tile t-wk rv" href="#works">
      <p class="t-k">Hall of Fame</p>
      <h3>ผลงานจริงของน้องๆ</h3>
      <p class="t-s">ทุกฉากในคลิปนี้มาจากเกมที่น้องสร้างเอง<br>ดูแบบเลื่อนได้เหมือน TikTok</p>
      <span class="t-b"><span class="tb1">ดูผลงาน</span></span>
      <video src="img/reel.mp4" poster="img/reel-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video>
    </a>
  </div></section>

''')
rep("IW=1536,IH=864,V0=.935,V1=.965","IW=1536,IH=864,V0=.79,V1=.965")
rep("hx.style.setProperty('--feet',Math.round((1-(V0+V1)/2)*bh)+'px');","hx.style.setProperty('--floor',Math.round((1-V0)*bh)+'px');")

css=r'''
/* ===== v6: arcade hero ===== */
.ar{position:relative;overflow:hidden;padding:clamp(48px,6vw,80px) 0 0;min-height:calc(100vh - 60px);min-height:calc(100svh - 60px);color:#fff;--floor:170px;
  background:radial-gradient(60% 70% at 72% 40%,#4A1FA8 0%,#20104F 45%,#0B0720 80%)}
.ar-wall{position:absolute;inset:0 0 var(--floor) 0;background:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px) 0 0/100% 34px,linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px) 0 0/34px 100%}
.ar-neon{position:absolute;left:4%;top:14%;font:400 clamp(.7rem,1.3vw,1rem) var(--pixel);color:#FF7AC6;letter-spacing:.2em;text-shadow:0 0 6px #FF3EA5,0 0 18px #FF3EA5;opacity:.55;writing-mode:vertical-rl;animation:neonF 6s steps(1) infinite}
@keyframes neonF{0%,92%,96%{opacity:.55}94%,98%{opacity:.15}}
.ar-in{position:relative;z-index:2;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(20px,4vw,60px);align-items:end;padding-bottom:calc(var(--floor) - 26px)}
.ar-txt{align-self:center;padding-bottom:40px;text-align:left}
.ar-k{display:inline-flex;align-items:center;gap:8px;font:600 .95rem var(--display);color:#7CF29A;background:rgba(124,242,154,.1);box-shadow:inset 0 0 0 1px rgba(124,242,154,.35);padding:6px 14px;border-radius:999px}
.ar h1{font:400 clamp(2.4rem,5.4vw,4.6rem)/1.05 var(--pixel);color:#FFD24A;text-shadow:.07em .07em 0 #E0337E,0 0 30px rgba(255,210,74,.35);margin-top:20px;letter-spacing:-.01em}
.ar-t{font:700 clamp(1.25rem,2.2vw,1.7rem)/1.4 var(--display);margin-top:20px}
.ar-f{list-style:none;padding:0;margin:24px 0 0;display:flex;flex-wrap:wrap;gap:10px}
.ar-f li{padding:10px 14px;border-radius:14px;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);color:#C9CDE8;font-size:.88rem;display:grid}
.ar-f b{color:#fff;font:700 1.05rem var(--display)}.ar-f s{color:#8A90B8;font-size:.85rem}
.ar-f li:first-child b{color:#FFD24A}
.ar-h{margin-top:22px;font:400 .7rem var(--pixel);color:#9FE7FF;animation:bl 1.2s steps(1) infinite}
.ar-m{display:flex;justify-content:center}
.c-hero{font-size:clamp(10px,1.08vw,14px)}
.ar-floor{position:absolute;left:0;right:0;bottom:0;height:var(--floor);z-index:1;
  background:radial-gradient(circle,#FF3EA5 0 2px,transparent 3px) 0 0/48px 48px,radial-gradient(circle,#39E0FF 0 2px,transparent 3px) 24px 24px/48px 48px,
  linear-gradient(45deg,transparent 46%,rgba(255,210,74,.2) 47% 53%,transparent 54%) 12px 30px/48px 48px,linear-gradient(-45deg,transparent 46%,rgba(124,242,154,.16) 47% 53%,transparent 54%) 36px 6px/48px 48px,#150B3A;
  box-shadow:inset 0 50px 60px -10px rgba(11,7,32,.92)}
.ar-floor::before{content:"";position:absolute;left:0;right:0;top:0;height:3px;background:linear-gradient(90deg,transparent,#FF3EA5 20%,#39E0FF 80%,transparent);box-shadow:0 0 18px #FF3EA5}
.ar .hx3{position:absolute;inset:0;z-index:3;pointer-events:none;background:none;border-radius:0;height:auto}
.ar-tip{position:absolute;left:0;right:0;bottom:10px;z-index:2;text-align:center;font-size:.82rem;color:rgba(255,255,255,.55)}
.ar .cab{filter:drop-shadow(0 0 40px rgba(255,62,165,.25)) drop-shadow(0 30px 30px rgba(0,0,0,.6))}
@media (max-width:900px){.ar-in{grid-template-columns:minmax(0,1fr)}.ar-txt{padding-bottom:0;text-align:center}.ar-f{justify-content:center}.c-hero{font-size:clamp(10px,2.7vw,14px)}.ar-neon{display:none}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v6.html','w').write(s)
print('v6 ok',len(s))
