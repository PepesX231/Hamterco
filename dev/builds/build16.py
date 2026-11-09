D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build15.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
LINE='https://page.line.me/jkm4247u?openQrModal=true'
i=s.index('  <section class="hb">');j=s.index('  <section class="hp-grid">',i)
old=s[i:j]
steps=old[old.index('<ol class="hb-st">'):old.index('</ol>')+5]
s=s[:i]+'''  <section class="hb hb2">
    <div class="hb2-top">
      <div class="hb2-tx">
        <p class="hb-k">คอร์สทำพอร์ตยื่นมหาลัย · สำหรับน้อง ม.6</p>
        <h1 class="hb2-h">เรียน 2 เดือน<br>ได้ผลงานจริง<br><span>ไปยื่นรอบ Portfolio</span></h1>
        <p class="hb2-n">Port Express · เริ่ม 9 พ.ย. 2569 · เรียน จ พ ศ</p>
        <div class="hb2-b"><p class="hb-p"><b>5,990 บาท</b> <s>9,990</s></p>
          <div class="hb-a"><a class="a1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="a2" href="#portex">ดูรายละเอียด</a></div></div>
        <a class="hb2-line" href="'''+LINE+'''" target="_blank" rel="noopener">มีคำถาม ทัก LINE ถามทีมได้เลย</a>
      </div>
      <a class="hb2-sc" href="#portex" aria-label="ดูรายละเอียดคอร์ส Port Express">
        <span class="glow" aria-hidden="true"></span>
        <span class="fr"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video></span>
        <img class="hb2-ham" src="img/n-gamer.webp" alt="">
      </a>
    </div>
    '''+steps+'''
  </section>

'''+s[j:]
css=r'''
/* ===== v16: banner = headline + course key art + 3-step strip ===== */
.hb2{flex-direction:column;justify-content:center;gap:clamp(28px,4vw,48px);padding:clamp(40px,5vw,64px) clamp(20px,4vw,48px) clamp(32px,4vw,48px);
  background:radial-gradient(55% 70% at 72% 38%,#5B2BD0 0%,rgba(91,43,208,0) 70%),radial-gradient(40% 50% at 15% 90%,rgba(224,51,126,.35),transparent 70%),#0E0A26}
.hb2::before{opacity:.18}
.hb2-top{position:relative;z-index:1;width:100%;max-width:1280px;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(24px,4vw,64px);align-items:center}
.hb2-h{font:800 clamp(2.4rem,4.8vw,4.4rem)/1.12 var(--display);letter-spacing:-.025em;margin-top:22px}
.hb2-h span{color:#FFD24A}
.hb2-n{color:#C9CDE8;margin-top:16px;font-size:clamp(1rem,1.3vw,1.1rem)}
.hb2-b{display:flex;align-items:center;gap:16px 28px;flex-wrap:wrap;margin-top:28px}
.hb2-b .hb-a{justify-content:flex-start}
.hb2-line{display:inline-block;margin-top:16px;color:#7CF29A;font-weight:600;text-decoration:none;padding:6px 12px;margin-left:-12px;border-radius:999px}
.hb2-line:hover{background:rgba(124,242,154,.12)}
.hb2-sc{position:relative;display:block;transform:perspective(1400px) rotateY(-9deg) rotateX(3deg);transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.hb2-sc:hover{transform:perspective(1400px) rotateY(-3deg) rotateX(1deg) translateY(-6px)}
.hb2-sc .glow{position:absolute;inset:8% 6%;background:linear-gradient(90deg,#FF3EA5,#5BC0FF);filter:blur(60px);opacity:.55}
.hb2-sc .fr{position:relative;display:block;padding:10px;background:#1B1446;border-radius:20px;box-shadow:0 0 0 2px rgba(255,255,255,.12),0 50px 80px -30px rgba(0,0,0,.8)}
.hb2-sc video{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:12px}
.hb2-ham{position:absolute;right:-18px;bottom:-34px;width:clamp(90px,9vw,130px);transform:rotate(6deg);filter:drop-shadow(0 12px 16px rgba(0,0,0,.45))}
.hb2 .hb-st{position:relative;z-index:1;margin:0;max-width:1180px;width:100%;padding-top:clamp(20px,3vw,32px);border-top:1px solid rgba(255,255,255,.14)}
.hb2 .hb-st li{flex-direction:row;align-items:center;text-align:left;gap:16px}
.hb2 .hb-v{zoom:.48;flex:none;width:260px}
.hb2 .hb-st b{margin-top:0;font-size:clamp(1rem,1.4vw,1.2rem)}
.hb2 .hb-st li>b,.hb2 .hb-st li>small{display:block}
.hb2 .hb-st li{display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:16px;align-items:center}
.hb2 .hb-st .hb-v{grid-row:1/3}
.hb2 .hb-st b{align-self:end}.hb2 .hb-st small{align-self:start}
.hb2 .hb-st li:not(:last-child)::after{top:50%;margin-top:-12px;width:24px;height:24px}
.hb2>.hb-ham{display:none}
@media (max-width:900px){.hb2-top{grid-template-columns:minmax(0,1fr);text-align:center}.hb2-b{justify-content:center}.hb2-b .hb-a{justify-content:center}.hb2-sc{transform:none;max-width:560px;margin:0 auto}
  .hb2 .hb-st li:not(:last-child)::after{top:auto;margin:0;left:62px;bottom:-24px}.hb2 .hb-st{gap:34px}.hb2-ham{right:-6px;bottom:-26px}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
s=s.replace('<b>ยื่นรอบ Portfolio ติดมหาลัย</b>','<b><span class="nw">ยื่นรอบ Portfolio</span> <span class="nw">ติดมหาลัย</span></b>')
open('/home/claude/hamsterhub-home/v16.html','w').write(s)
print('v16 ok',len(s))
