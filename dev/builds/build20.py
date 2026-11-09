D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build19.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
i=s.index('  <section class="ov"><div class="ov-c" id="ovc">');j=s.index('  <section class="hp-grid">',i)
s=s[:i]+'''  <section class="ov">
    <h1 class="sr">Port Express คอร์สพาน้อง ม.6 ทำพอร์ตยื่นมหาลัย เรียนทำเกมกับพี่ๆ 2 เดือน ได้ผลงานจริงใส่แฟ้มพอร์ต รุ่นพี่ติดมหาลัยแล้ว 48 คน เริ่ม 9 พ.ย. 2569 ราคา 5,990 บาท</h1>
    <a class="ov-c" href="#portex" aria-label="ดูรายละเอียดคอร์ส Port Express"><video src="img/portex-hero.mp4" poster="img/portex-hero.webp" autoplay muted loop playsinline preload="auto" aria-hidden="true"></video></a>
    <div class="ov-bar2"><p class="ov-p2"><b>Port Express</b> · 5,990 บาท · เริ่ม 9 พ.ย. 2569</p>
      <div class="ov-b2"><a class="a1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="a2" href="#portex">ดูรายละเอียด</a></div></div>
  </section>

'''+s[j:]
css=r'''
/* ===== v20: the edited clip carries the info ===== */
.ov a.ov-c{display:block;width:min(100%,calc((100svh - 160px) * 16 / 9))}
.ov-c video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ov-bar2{width:min(100%,calc((100svh - 160px) * 16 / 9));margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px 20px;flex-wrap:wrap;padding:16px 4px 4px}
.ov-p2{font:600 1.1rem var(--display);color:var(--mute)}.ov-p2 b{color:var(--ink)}
.ov-b2{display:flex;gap:10px}
.ov-b2 a{display:inline-flex;align-items:center;min-height:48px;padding:0 24px;border-radius:999px;font:700 1rem var(--display);text-decoration:none;transition:transform .15s,background .2s}
.ov-b2 .a1{background:#FFD24A;color:#0B0720}.ov-b2 .a1:hover{background:#FFC21A}
.ov-b2 .a2{color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--hair)}.ov-b2 .a2:hover{background:var(--alt)}
@media (max-width:700px){.ov-c{aspect-ratio:16/9!important}.ov-c video{position:absolute!important}.ov-bar2{flex-direction:column;align-items:stretch;text-align:center}.ov-b2{justify-content:center}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v20.html','w').write(s)
print('v20 ok',len(s))
