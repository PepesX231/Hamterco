D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build14.py').read())
LINE='https://page.line.me/jkm4247u?openQrModal=true'
PX='https://www.hamsterhub.co/portex-site/index.html'
i=s.index('  <section class="h-hero ar" id="hx">');j=s.index('  <section class="hp-grid">',i)
s=s[:i]+'''  <section class="hb">
    <div class="hb-in">
      <p class="hb-k">คอร์สทำพอร์ตยื่นมหาลัย · สำหรับน้อง ม.6</p>
      <h1 class="hb-t">Port Express</h1>
      <p class="hb-s">เรียน 2 เดือน น้องได้ผลงานจริงไปยื่นรอบ Portfolio</p>
      <ol class="hb-st">
        <li><span class="hb-v v-g"><img src="img/work-phi-krahang.webp" alt=""><img src="img/work-stressstrike.webp" alt=""><img src="img/work-midnight-at-roadside.webp" alt=""></span><b>เรียนทำเกมกับพี่ๆ</b><small>จันทร์ พุธ ศุกร์ · 2 เดือน</small></li>
        <li><span class="hb-v v-f"><span class="fd2"><span class="tb">PORTFOLIO</span><i></i><i></i><i></i><em>READY!</em></span></span><b>ได้ผลงานใส่แฟ้มพอร์ต</b><small>พร้อมสไลด์เล่าผลงาน และซ้อมสัมภาษณ์</small></li>
        <li><span class="hb-v v-p"><img src="img/dek69-13.webp" alt=""><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""></span><b>ยื่นรอบ Portfolio ติดมหาลัย</b><small>รุ่นพี่ติดแล้ว 48 คน</small></li>
      </ol>
      <div class="hb-b">
        <p class="hb-p"><b>5,990 บาท</b> <s>9,990</s><span>เริ่ม 9 พ.ย. 2569</span></p>
        <div class="hb-a"><a class="a1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="a2" href="#portex">ดูรายละเอียด</a><a class="a3" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div>
      </div>
    </div>
    <img class="hb-ham" src="img/n-gamer.webp" alt="">
  </section>

'''+s[j:]
rep('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n','')
# one quiet hamster on courses and works
rep('<section class="ct-h"><h1>คอร์ส</h1>','<section class="ct-h"><img class="pg-ham" src="img/n-maker.webp" alt=""><h1>คอร์ส</h1>')
i=s.index('<aside class="yt-side"');j=s.index('</aside>',i)
s=s[:j]+'<img class="yt-ham" src="img/n-walker.webp" alt="">'+s[j:]
css=r'''
/* ===== v15: hero = one big banner that sells the course ===== */
.hb{position:relative;overflow:hidden;min-height:calc(100svh - 60px);display:flex;align-items:center;color:#fff;
  background:radial-gradient(70% 80% at 50% 0%,#3B1E8C 0%,#1A0E4A 50%,#0E0A26 100%)}
.hb::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.5) 1px,transparent 1.5px);background-size:46px 46px;opacity:.25;pointer-events:none}
.hb-in{position:relative;z-index:1;width:100%;max-width:1240px;margin:0 auto;padding:clamp(40px,6vw,72px) clamp(20px,4vw,40px);text-align:center}
.hb-k{display:inline-block;font:700 clamp(.95rem,1.4vw,1.1rem) var(--display);color:#0B0720;background:#7CF29A;padding:6px 16px;border-radius:999px}
.hb-t{font:400 clamp(2.6rem,7vw,6rem)/1.05 var(--pixel);color:#FFD24A;text-shadow:.07em .07em 0 #E0337E;margin-top:20px;letter-spacing:-.01em}
.hb-s{font:800 clamp(1.3rem,2.6vw,2.1rem)/1.35 var(--display);margin-top:16px}
.hb-st{list-style:none;margin:clamp(32px,4vw,52px) auto 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(20px,4vw,64px);max-width:1080px}
.hb-st li{position:relative;display:flex;flex-direction:column;align-items:center;gap:8px;opacity:0;animation:hbIn .7s cubic-bezier(.2,.8,.2,1) forwards}
.hb-st li:nth-child(1){animation-delay:.15s}.hb-st li:nth-child(2){animation-delay:.55s}.hb-st li:nth-child(3){animation-delay:.95s}
@keyframes hbIn{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
.hb-st li:not(:last-child)::after{content:"";position:absolute;right:calc(clamp(20px,4vw,64px) / -2 - 16px);top:70px;width:32px;height:32px;background:#FFD24A;clip-path:polygon(0 30%,55% 30%,55% 0,100% 50%,55% 100%,55% 70%,0 70%)}
.hb-st b{font:800 clamp(1.1rem,1.8vw,1.45rem)/1.3 var(--display);margin-top:8px}
.hb-st small{color:#C9CDE8;font-size:clamp(.9rem,1.2vw,1rem)}
.hb-st li:last-child small{color:#FFD24A;font-weight:700}
.hb-v{position:relative;display:block;width:min(100%,260px);height:170px}
.v-g img{position:absolute;width:190px;aspect-ratio:16/10;object-fit:cover;border:4px solid #fff;border-radius:10px;box-shadow:0 16px 30px rgba(0,0,0,.45)}
.v-g img:nth-child(1){left:6px;top:52px;transform:rotate(-8deg)}.v-g img:nth-child(2){left:34px;top:24px;transform:rotate(3deg)}.v-g img:nth-child(3){left:62px;top:0;transform:rotate(-2deg)}
.fd2{position:absolute;left:50%;top:0;width:160px;height:168px;margin-left:-80px}
.fd2::before{content:"";position:absolute;inset:22px 0 0;background:#FFB81C;box-shadow:inset 0 -8px 0 #C28A00}
.fd2 .tb{position:absolute;left:0;top:0;height:24px;padding:0 12px;background:#FFB81C;font:400 .55rem/25px var(--pixel);color:#5A3A00}
.fd2 i{position:absolute;left:14px;right:14px;height:34px;background:#fff}
.fd2 i:nth-of-type(1){top:40px}.fd2 i:nth-of-type(2){top:82px}.fd2 i:nth-of-type(3){top:124px}
.fd2 i::before{content:"";position:absolute;left:6px;top:6px;bottom:6px;width:40px;background:#5B3FD6}
.fd2 i:nth-of-type(2)::before{background:#1068DC}.fd2 i:nth-of-type(3)::before{background:#2E9E6B}
.fd2 i::after{content:"";position:absolute;left:54px;right:10px;top:10px;height:5px;background:#E3DAC4;box-shadow:0 9px 0 #E3DAC4}
.fd2 em{position:absolute;right:-26px;bottom:8px;font:400 .8rem var(--pixel);font-style:normal;color:#E0337E;border:3px solid #E0337E;background:rgba(255,255,255,.92);padding:5px 7px;transform:rotate(-12deg);animation:stamp .5s 1.4s cubic-bezier(.2,1.6,.4,1) both}
@keyframes stamp{from{opacity:0;transform:rotate(-12deg) scale(2.2)}}
.v-p img{position:absolute;top:8px;width:96px;aspect-ratio:4/5;object-fit:cover;border:4px solid #fff;border-radius:8px;box-shadow:0 16px 30px rgba(0,0,0,.45)}
.v-p img:nth-child(1){left:14px;transform:rotate(-10deg)}.v-p img:nth-child(2){left:82px;top:0;z-index:1}.v-p img:nth-child(3){left:150px;transform:rotate(10deg)}
.hb-b{display:flex;justify-content:center;align-items:center;gap:20px 36px;flex-wrap:wrap;margin-top:clamp(32px,4vw,48px)}
.hb-p{text-align:left}.hb-p b{font:800 clamp(1.8rem,3vw,2.4rem) var(--display);color:#FFD24A}.hb-p s{color:#8A90B8;margin-left:6px}.hb-p span{display:block;color:#C9CDE8}
.hb-a{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.hb-a a{display:inline-flex;align-items:center;min-height:52px;padding:0 24px;border-radius:999px;font:700 1.05rem var(--display);text-decoration:none;transition:transform .15s,background .2s}
.hb-a a:hover{transform:translateY(-2px)}
.a1{background:#FFD24A;color:#0B0720}.a1:hover{background:#fff}
.a2{color:#fff;box-shadow:inset 0 0 0 2px rgba(255,255,255,.6)}.a2:hover{background:rgba(255,255,255,.12)}
.a3{background:#06C755;color:#fff}
.hb-ham{position:absolute;right:clamp(8px,4vw,60px);bottom:-6px;width:clamp(90px,10vw,150px);z-index:1;pointer-events:none;filter:drop-shadow(0 10px 16px rgba(0,0,0,.4))}
.pg-ham{float:right;width:clamp(90px,10vw,140px);margin:-10px 0 0 16px}
.yt-ham{display:block;width:110px;margin:24px auto 0;opacity:.95}
@media (max-width:900px){.hb-st{grid-template-columns:minmax(0,1fr);gap:28px}.hb-st li:not(:last-child)::after{right:auto;left:50%;top:auto;bottom:-26px;transform:translateX(-50%) rotate(90deg);width:22px;height:22px}.hb-p{text-align:center}.hb-ham{display:none}.yt-ham{display:none}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v15.html','w').write(s)
print('v15 ok',len(s))
