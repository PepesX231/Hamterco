D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build20.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
LINE='https://page.line.me/jkm4247u?openQrModal=true'
i=s.index('  <section class="px-hero">');j=s.index('</section>',i)+10
s=s[:i]+'''  <section class="ap">
    <p class="px-crumb ap-cr"><a href="#home">หน้าแรก</a> › <a href="#courses">คอร์ส</a> › Port Express</p>
    <h1 class="ap-t">Port Express</h1>
    <p class="ap-s">คอร์สทำพอร์ต <span>ยื่นมหาลัย</span></p>
    <p class="ap-d">สำหรับน้อง ม.6 ที่ยังไม่มีพอร์ต · เรียน 2 เดือน · เริ่ม 9 พ.ย. 2569</p>
    <div class="ap-b"><a class="b1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="b2" href="#pxPrice">ดูราคา</a></div>
    <div class="ap-v"><span class="ap-gl" aria-hidden="true"></span><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="auto" aria-label="วิดีโอแนะนำคอร์ส Port Express"></video></div>
    <ul class="ap-f">
      <li><b>2 เดือน</b><span>จันทร์ พุธ ศุกร์</span></li>
      <li><b>เกม 3 งาน</b><span>ผลงานใส่แฟ้มพอร์ต</span></li>
      <li><b>5 ครั้ง</b><span>อาจารย์มหาลัยตรวจงาน</span></li>
      <li><b>48 คน</b><span>รุ่นพี่ติดมหาลัยแล้ว</span></li>
    </ul>
    <div class="ap-pr" id="pxPrice"><p><b>5,990 บาท</b> <s>9,990</s> <em>ประหยัด 4,000</em></p><div class="ap-b"><a class="b1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="b2" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div></div>
  </section>'''+s[j:]
css=r'''
/* ===== v21: Port Express page hero, Apple-style ===== */
.ap{text-align:center;padding:clamp(28px,4vw,48px) 20px clamp(56px,7vw,96px);background:radial-gradient(60% 40% at 50% 62%,rgba(91,43,208,.45),transparent 70%)}
.ap-cr{text-align:left;max-width:1120px;margin:0 auto 10px}
.ap-t{font:800 clamp(3rem,8vw,6rem)/1 var(--display);letter-spacing:-.035em;color:#fff}
.ap-s{font:700 clamp(1.5rem,3.4vw,2.6rem) var(--display);margin-top:12px;color:#FFD24A}
.ap-s span{background:linear-gradient(90deg,#7CF29A,#5BC0FF);-webkit-background-clip:text;background-clip:text;color:transparent}
.ap-d{color:#B7BCE0;font-size:clamp(1rem,1.6vw,1.25rem);margin-top:12px}
.ap-b{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-top:24px}
.ap-b a{display:inline-flex;align-items:center;min-height:48px;padding:0 26px;border-radius:999px;font:600 1.05rem var(--display);text-decoration:none;transition:background .2s}
.ap-b .b1{background:#0071E3;color:#fff}.ap-b .b1:hover{background:#0077ED}
.ap-b .b2{color:#2997FF;box-shadow:inset 0 0 0 1.5px #2997FF}.ap-b .b2:hover{background:rgba(41,151,255,.12)}
.ap-v{position:relative;width:min(1180px,100%);margin:clamp(36px,5vw,64px) auto 0}
.ap-gl{position:absolute;inset:10% 8% -4%;background:linear-gradient(90deg,#E0337E,#5B3FD6,#2997FF);filter:blur(70px);opacity:.45}
.ap-v video{position:relative;display:block;width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:22px;box-shadow:0 0 0 1px rgba(255,255,255,.12),0 60px 100px -40px rgba(0,0,0,.9)}
.ap-f{list-style:none;margin:clamp(40px,5vw,64px) auto 0;padding:0;max-width:1000px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}
.ap-f b{display:block;font:800 clamp(1.6rem,3vw,2.4rem) var(--display);color:#fff}.ap-f span{color:#B7BCE0}
.ap-pr{margin-top:clamp(40px,5vw,60px)}.ap-pr p{color:#B7BCE0}.ap-pr b{font:800 clamp(2rem,4vw,3rem) var(--display);color:#fff}.ap-pr s{margin-left:6px}
.ap-pr em{font-style:normal;font-weight:700;color:#0B0720;background:#7CF29A;padding:3px 10px;border-radius:999px;margin-left:8px}
@media (max-width:700px){.ap-f{grid-template-columns:repeat(2,minmax(0,1fr))}.ap-v video{border-radius:14px}}
'''
css+=r'''
/* v21b: full-bleed + pixel art */
.ap{padding-left:0;padding-right:0;background:#0B0A2E url(img/px-sky.webp) 50% 0/cover;image-rendering:pixelated;position:relative}
.ap::before{content:"";position:absolute;inset:0;background:linear-gradient(rgba(11,10,46,.55),rgba(11,10,46,.2) 30%,rgba(11,10,46,.85));pointer-events:none}
.ap>*{position:relative}
.ap-cr{padding:0 20px}
.ap-t{font:400 clamp(2.4rem,7vw,5.6rem)/1.1 var(--pixel)!important;color:#FFD24A!important;text-shadow:.08em .08em 0 #E0337E,0 0 40px rgba(255,210,74,.35);letter-spacing:0!important}
.ap-s{font:800 clamp(1.5rem,3.4vw,2.6rem) var(--display);color:#fff;margin-top:22px}
.ap-s span{background:none;color:#7CF29A;-webkit-text-fill-color:#7CF29A}
.ap-b a{border-radius:0!important;font:700 1.05rem var(--display);padding:0 26px 4px;clip-path:polygon(0 5px,5px 5px,5px 0,calc(100% - 5px) 0,calc(100% - 5px) 5px,100% 5px,100% calc(100% - 5px),calc(100% - 5px) calc(100% - 5px),calc(100% - 5px) 100%,5px 100%,5px calc(100% - 5px),0 calc(100% - 5px));transition:transform .1s steps(2)}
.ap-b a:hover{transform:translateY(3px)}
.ap-b .b1{background:#FFD24A!important;color:#0B0720!important;box-shadow:inset 0 -5px 0 #C28A00!important}
.ap-b .b2{background:#5BC0FF!important;color:#06123A!important;box-shadow:inset 0 -5px 0 #1D5FB8!important}
.ap-v{width:100%!important;margin-left:0;margin-right:0}
.ap-gl{display:none}
.ap-v video{border-radius:0!important;aspect-ratio:auto!important;height:min(78vh,56.25vw);object-fit:cover;box-shadow:0 -8px 0 #0B0720,0 8px 0 #0B0720,0 -14px 0 #5B3FD6,0 14px 0 #5B3FD6!important}
.ap-f{padding:0 20px;gap:16px}
.ap-f li{background:#14185A;padding:18px 14px;box-shadow:0 0 0 4px #2D3590,6px 6px 0 4px #05061E}
.ap-f b{font:400 clamp(1rem,1.8vw,1.4rem)/1.4 var(--pixel)!important;color:#FFD24A!important}
.ap-pr b{font:400 clamp(1.6rem,3.4vw,2.6rem) var(--pixel)!important;color:#FFD24A!important;text-shadow:4px 4px 0 #E0337E}
.ap-pr em{border-radius:0!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v21.html','w').write(s)
print('v21 ok',len(s))
