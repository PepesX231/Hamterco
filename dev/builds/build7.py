D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build6.py').read())
cut('      <div class="ar-txt">','      <div class="ar-m">','''      <div class="ar-txt">
        <p class="ar-ks rv"><span class="ar-tc">TCAS70 · รอบ 1 Portfolio</span><span class="ar-k"><span class="pxdot"></span><span class="pxst">รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</span></span></p>
        <h1 class="rv">Port Express</h1>
        <p class="ar-t rv"><span class="nw">คอร์สพาน้อง ม.6</span> <span class="nw">เข้ารอบ Portfolio</span></p>
        <p class="ar-s rv">ยังไม่มีพอร์ต? 2 เดือน ได้แฟ้มพอร์ตพร้อมยื่น · 5,990 บาท <s>9,990</s></p>
        <div class="pf rv" aria-label="แฟ้มพอร์ตที่น้องจะได้">
          <div class="pf-tab">PORTFOLIO · TCAS70</div>
          <ul>
            <li><span class="ck"></span><b>เกมที่เล่นได้จริง 3 งาน</b><small>ขึ้น itch.io กรรมการกดเล่นได้ทันที</small></li>
            <li><span class="ck"></span><b>แฟ้มพอร์ต + Pitch Deck</b><small>แก้กับเทรนเนอร์จนพร้อมส่ง</small></li>
            <li><span class="ck"></span><b>ซ้อมสัมภาษณ์กับอาจารย์มหาลัย</b><small>ฟังผลงานทุก 2 สัปดาห์ ตรวจ 5 ครั้ง</small></li>
          </ul>
          <div class="pf-ft"><span class="av"><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""><img src="img/dek69-13.webp" alt=""><img src="img/dek69-11.webp" alt=""></span><p><b>รุ่นพี่ DEK69 ยื่นรอบพอร์ตติดแล้ว 48 คน</b><br>สจล. · จุฬาฯ CEDT · มหิดล · เกษตรศาสตร์</p></div>
        </div>
      </div>
''')
rep('<span class="stk s2">เรียน จ · พ · ศ<b>เริ่ม 9 พ.ย.</b></span>','<span class="stk s2">ทันยื่น<b>รอบ Portfolio</b></span>')
css=r'''
/* v7: portfolio round + generated floor */
.ar-ks{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.ar-tc{font:700 .95rem var(--display);color:#0B0720;background:#FFD24A;padding:6px 14px;border-radius:999px}
.ar h1{margin-top:16px;font-size:clamp(1.7rem,3.1vw,2.9rem)!important;white-space:nowrap}
.ar-t{font:800 clamp(1.4rem,2.4vw,2rem)/1.3 var(--display);margin-top:12px}
.ar-s{color:#C9CDE8;margin-top:8px}.ar-s s{color:#8A90B8}
.pf{position:relative;margin-top:22px;max-width:500px;background:#FFFDF6;color:#1D1D1F;border-radius:6px 18px 18px 18px;padding:20px 22px 16px;box-shadow:0 30px 50px -24px rgba(0,0,0,.7),6px 6px 0 #E8DEC4;transform:rotate(-1deg)}
.pf ul{gap:8px!important}
.pf-tab{position:absolute;left:0;top:-26px;height:26px;padding:0 14px;display:flex;align-items:center;background:#FFFDF6;border-radius:10px 10px 0 0;font:400 .55rem var(--pixel);letter-spacing:.12em;color:#B0306A}
.pf ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.pf li{display:grid;grid-template-columns:24px 1fr;column-gap:12px;align-items:start}
.pf li b{font:700 1rem var(--display)}.pf li small{grid-column:2;color:#6E6E73;font-size:.85rem}
.ck{grid-row:1/3;width:22px;height:22px;border-radius:6px;border:2px solid #2E9E6B;position:relative;margin-top:2px}
.ck::after{content:"";position:absolute;left:6px;top:1px;width:6px;height:12px;border:solid #2E9E6B;border-width:0 3px 3px 0;transform:rotate(45deg) scale(0);animation:ckIn .35s cubic-bezier(.3,1.8,.5,1) forwards}
.pf li:nth-child(1) .ck::after{animation-delay:.6s}.pf li:nth-child(2) .ck::after{animation-delay:.9s}.pf li:nth-child(3) .ck::after{animation-delay:1.2s}
@keyframes ckIn{to{transform:rotate(45deg) scale(1)}}
.pf-ft{display:flex;align-items:center;gap:12px;margin-top:14px;padding-top:12px;border-top:1.5px dashed #E3DAC4}
.av{display:flex;flex:none;min-width:112px}.av img{flex:none}.av img{width:34px;height:34px;border-radius:50%;object-fit:cover;object-position:62% 42%;border:2px solid #FFFDF6;margin-left:-10px}.av img:first-child{margin-left:0}
.pf-ft p{font-size:.82rem;color:#6E6E73;line-height:1.45}.pf-ft b{color:#1D1D1F;font-size:.9rem}
.ar-in{align-items:center;padding-bottom:calc(var(--floor) + 10px)}
.ar-txt{padding-bottom:0!important}
.ar-floor{height:calc(var(--floor) + 90px);background:url(img/ar-floor.webp) 50% 0/cover no-repeat,#120A33;box-shadow:none;-webkit-mask:linear-gradient(transparent,#000 90px);mask:linear-gradient(transparent,#000 90px)}
.ar-floor::before{display:none}
@media (max-width:900px){.pf{margin-left:auto;margin-right:auto;text-align:left}.ar-ks{justify-content:center}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v7.html','w').write(s)
print('v7 ok',len(s))
