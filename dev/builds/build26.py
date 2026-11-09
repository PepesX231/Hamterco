D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build25.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
LINE='https://page.line.me/jkm4247u?openQrModal=true'
EXT='href="'+PX+'" target="_blank" rel="noopener"'
# ---------- HERO: light, blue base, readable without watching anything ----------
i=s.index('  <section class="ov">');j=s.index('  <section class="hp-grid">',i)
s=s[:i]+'''  <section class="nh">
    <div class="nh-in">
      <p class="nh-k"><span class="dot"></span>เปิดรับรุ่นใหม่ · เริ่มเรียน 9 พ.ย. 2569</p>
      <h1 class="nh-t">Port Express</h1>
      <p class="nh-s">คอร์สทำพอร์ตยื่นมหาลัย สำหรับน้อง ม.6<br><span>เรียนสร้างเกมด้วย Unity 2 เดือน · จันทร์ พุธ ศุกร์</span></p>
      <div class="nh-pr"><p class="nh-price"><b>5,990</b> บาท</p><p class="nh-was"><s>ปกติ 9,990 บาท</s><em>ประหยัด 4,000</em></p></div>
      <div class="nh-b"><a class="nb1" '''+EXT+'''>สมัครเรียน</a><a class="nb2" '''+EXT+'''>ดูรายละเอียดคอร์ส</a><a class="nb3" href="'''+LINE+'''" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div>
    </div>
    <div class="nh-get">
      <h2>จบคอร์ส น้องได้ 3 อย่างนี้</h2>
      <div class="nh-g">
        <figure><img src="img/work-phi-krahang.webp" alt="ตัวอย่างเกมที่รุ่นพี่สร้าง"><figcaption><b>ผลงานเกมของน้องเอง</b><span>เกมที่น้องเขียนโปรแกรมสร้างเอง ใส่พอร์ตได้ทันที</span></figcaption></figure>
        <figure><img src="img/folio.webp" alt="ภาพประกอบแฟ้มพอร์ตโฟลิโอ"><figcaption><b>แฟ้มพอร์ตพร้อมยื่น</b><span>แฟ้มผลงานและสไลด์เล่าผลงาน ที่พี่ๆ ช่วยแก้จนพร้อมส่ง</span></figcaption></figure>
        <figure><img src="img/photo-class.webp" alt="ห้องเรียน Hamster Hub"><figcaption><b>ซ้อมสัมภาษณ์กับอาจารย์มหาลัย</b><span>นำเสนอผลงานให้อาจารย์ฟัง ก่อนเข้าห้องสัมภาษณ์จริง</span></figcaption></figure>
      </div>
      <p class="nh-proof"><span class="av2"><img src="img/dek69-13.webp" alt=""><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""><img src="img/dek69-11.webp" alt=""></span><span><b>รุ่นพี่ติดมหาลัยแล้ว 48 คน</b> สจล. · จุฬาฯ · มหิดล · เกษตรศาสตร์</span></p>
    </div>
  </section>

'''+s[j:]
# ---------- paths: real pictures, mascot peeks ----------
for m,ph in [('n-grad','dek69-8'),('n-ceo','s-showcase2'),('n-win','s-showcase1')]:
    a='<span class="pod"><img src="img/'+m+'.webp" alt="" loading="lazy">'
    rep(a,'<span class="pod"><img class="ph" src="img/'+ph+'.webp" alt="" loading="lazy"><img class="ms" src="img/'+m+'.webp" alt="" loading="lazy">')
rep('<h2 class="rv">น้องอยากไปทางไหน<br>Hamster Hub พาไปได้</h2>','<h2 class="rv">น้องอยากไปทางไหน<br>Hamster Hub พาไปได้</h2><p class="sk rv">เราสอนทำ <b>เกม</b> · <b>Roblox</b> · <b>เว็บ</b> · <b>IoT</b> ให้น้องมีผลงานจริงของตัวเอง</p>')
# ---------- seniors: first look back, crisp, in brand blue ----------
i=s.index('/* seniors bg = current poster */');j=s.index('/* ===== v25',i)
s=s[:i]+s[j:]
s=s.replace('<img class="mc-bgi" id="mcBg" alt="" aria-hidden="true">','')
s=s.replace('.mc-c img{-webkit-box-reflect:below 10px linear-gradient(transparent 72%,rgba(255,255,255,.22))}','')
# ---------- courses: price you can see ----------
rep('<div><b>Port Express</b><span>คอร์สปั้นพอร์ต ยื่นมหาลัย สำหรับ ม.6 · เริ่ม 9 พ.ย. 2569 · <em>5,990 บาท</em></span></div>',
    '<div><b>Port Express</b><span>คอร์สทำพอร์ตยื่นมหาลัย สำหรับ ม.6 · เริ่ม 9 พ.ย. 2569 · เรียน 2 เดือน</span><p class="ctb-p"><strong>5,990 บาท</strong><s>9,990</s><em>ประหยัด 4,000</em></p></div>')
# ---------- about: lead with the wins ----------
rep('<section class="ab-h">','''<section class="ab-win"><div class="wrap"><p class="aw-k">ผลงานของน้องๆ Hamster Hub</p>
    <div class="aw-g">
      <figure><img src="img/dek69-8.webp" alt=""><figcaption><b>48 คน</b><span>รุ่นพี่ DEK69 ติดมหาลัยรอบ Portfolio</span></figcaption></figure>
      <figure><img src="img/work-stressstrike.webp" alt=""><figcaption><b>ชนะเลิศ</b><span>OBEC Roboplayground ด้วยเกม StressStrike</span></figcaption></figure>
      <figure><img src="img/s-showcase1.webp" alt=""><figcaption><b>12 ผลงาน</b><span>เข้ารอบชิงชนะเลิศ NSC การแข่งขันพัฒนาโปรแกรมระดับประเทศ</span></figcaption></figure>
      <figure><img src="img/real-0.webp" alt=""><figcaption><b>ขายได้จริง</b><span>เกม Mr. City ขายให้สวนสัตว์สงขลา</span></figcaption></figure>
    </div></div></section>
  <section class="ab-h">''')
# ---------- works: tell people how to move ----------
rep("  /* router */",r'''  /* works: a clear "next" guide until they scroll once */
  (function(){var tk=document.querySelector('.yt .tk'),f=tk&&tk.querySelector('.tk-feed');if(!f)return;var g=document.createElement('button');g.type='button';g.className='tk-guide';
    g.innerHTML='เลื่อนลง หรือกดตรงนี้<br>เพื่อดูผลงานถัดไป <b>↓</b>';tk.appendChild(g);g.addEventListener('click',function(){f.scrollBy({top:f.clientHeight,behavior:'smooth'})});
    f.addEventListener('scroll',function(){if(f.scrollTop>40)g.classList.add('hide')},{passive:true})})();
  /* router */''')
# ---------- courses transition: calm blue ----------
i=s.index("    if(v==='courses'){var F=");j=s.index("    else if(v==='portex')",i)
s=s[:i]+"    if(v==='courses'){h='<span class=\"cv a\"></span><span class=\"cv b\"></span><b class=\"cv-t\">คอร์ส</b>'}\n"+s[j:]
css=r'''
/* ===== v26: brand blue base ===== */
:root{--b50:#EEF6FF;--b100:#D9ECFF;--b200:#B3D8FF;--b400:#4DA3F0;--b600:#1C74D9;--b700:#155FB5;--b800:#0D4A94;--b900:#082F5F;--yel:#FFC531}
/* hero */
.nh{background:linear-gradient(180deg,var(--b50) 0%,#fff 62%);padding:clamp(40px,5vw,72px) 20px clamp(48px,6vw,80px);text-align:center;color:var(--b900)}
.nh-k{display:inline-flex;align-items:center;gap:8px;font:700 1rem var(--display);color:var(--b800);background:var(--b100);padding:7px 16px;border-radius:999px}
.nh-k .dot{width:8px;height:8px;border-radius:50%;background:#1BB55C;box-shadow:0 0 0 4px rgba(27,181,92,.2)}
.nh-t{font:800 clamp(3rem,7vw,5.6rem)/1 var(--display);letter-spacing:-.035em;margin-top:18px;color:var(--b900)}
.nh-s{font:700 clamp(1.3rem,2.4vw,1.9rem)/1.35 var(--display);margin-top:14px;color:var(--b900)}
.nh-s span{display:block;font:500 clamp(1rem,1.4vw,1.15rem) var(--display);color:#4A5B75;margin-top:6px}
.nh-pr{display:flex;justify-content:center;align-items:flex-end;gap:18px;flex-wrap:wrap;margin-top:24px}
.nh-price{font:700 1.4rem var(--display);color:var(--b900)}.nh-price b{font:800 clamp(3rem,6vw,4.4rem)/1 var(--display);color:var(--b700);letter-spacing:-.02em;margin-right:6px}
.nh-was{text-align:left;color:#4A5B75;font-size:1rem;}
.nh-was em{display:block;font-style:normal;text-decoration:none;font:800 1rem var(--display);color:#3A2A00;background:var(--yel);padding:3px 12px;border-radius:999px;margin-top:6px;width:max-content}
.nh-b{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:26px}
.nh-b a{display:inline-flex;align-items:center;min-height:52px;padding:0 28px;border-radius:999px;font:700 1.05rem var(--display);text-decoration:none;transition:background .2s,transform .15s}
.nh-b a:hover{transform:translateY(-2px)}
.nb1{background:var(--b600);color:#fff}.nb1:hover{background:var(--b700)}
.nb2{color:var(--b700);box-shadow:inset 0 0 0 2px var(--b600)}.nb2:hover{background:var(--b50)}
.nb3{color:#06A84A}.nb3:hover{background:#E8F9EF}
.nh-get{max-width:1180px;margin:clamp(40px,5vw,64px) auto 0}
.nh-get h2{font:800 clamp(1.5rem,2.6vw,2.1rem) var(--display);color:var(--b900)}
.nh-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:24px;text-align:left}
.nh-g figure{margin:0;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 0 0 1px var(--b100),0 24px 40px -28px rgba(8,47,95,.35)}
.nh-g img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover}
.nh-g figcaption{padding:18px 20px 22px}
.nh-g b{display:block;font:800 1.25rem var(--display);color:var(--b900)}.nh-g span{display:block;color:#4A5B75;margin-top:4px;line-height:1.5}
.nh-proof{display:inline-flex;align-items:center;gap:14px;margin-top:28px;color:#4A5B75;flex-wrap:wrap;justify-content:center}
.nh-proof b{color:var(--b900);margin-right:6px}
.av2{display:flex}.av2 img{width:40px;height:40px;border-radius:50%;object-fit:cover;object-position:60% 40%;border:3px solid #fff;margin-left:-12px;box-shadow:0 0 0 1px var(--b100)}.av2 img:first-child{margin-left:0}
@media (max-width:800px){.nh-g{grid-template-columns:minmax(0,1fr)}.nh-was{text-align:center}.nh-was em{margin:6px auto 0}}
/* paths: real pictures */
.sk{margin-top:12px;color:#4A5B75;font-size:1.1rem;text-align:center}.sk b{color:var(--b700)}
.f4.p3 .pod{position:relative;display:block;width:100%;max-width:300px;height:auto;margin:0 auto;background:none!important}
.f4.p3 .pod .ph{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:18px;box-shadow:0 20px 34px -22px rgba(8,47,95,.45);max-height:none}
.f4.p3 .pod .ms{position:absolute;right:-14px;bottom:-18px;width:96px;height:auto;max-height:none}
.f4.p3 .pod .bubble{right:auto;left:10px;top:10px}
/* seniors: first look, brand blue, crisp */
.mc-in{background:radial-gradient(60% 70% at 50% 58%,#1C74D9 0%,#0D3E80 45%,#061633 100%)!important}
.mc-in::after{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.55) 1px,transparent 1.5px);background-size:56px 56px;opacity:.25;pointer-events:none}
.mc-in>*{position:relative;z-index:1}.mc-bg{position:absolute!important;z-index:0;color:rgba(255,255,255,.07)!important;opacity:1}
/* courses price */
.ctb-p{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-top:10px}
.ctb-p strong{font:800 clamp(2.2rem,4vw,3rem)/1 var(--display);color:var(--b700)}.ctb-p s{color:var(--mute)}
.ctb-p em{font-style:normal;font:800 .95rem var(--display);color:#3A2A00;background:var(--yel);padding:3px 12px;border-radius:999px}
/* activity: a colour to hold on to */
[data-view="activity"] .ac-h{margin:0 calc(50% - 50vw);padding:clamp(40px,5vw,64px) calc(50vw - 50% + 0px);background:linear-gradient(180deg,var(--b50),#fff)}
[data-view="activity"] .ac-h h1{color:var(--b800)}
.er b{color:var(--b900)}.er-h{color:var(--b800)}
/* about wins */
.ab-win{padding:clamp(40px,5vw,64px) 0;background:linear-gradient(180deg,var(--b50),#fff)}
.aw-k{font:800 clamp(1.5rem,2.6vw,2.1rem) var(--display);color:var(--b900);text-align:center}
.aw-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:26px}
.aw-g figure{margin:0;background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 0 0 1px var(--b100)}
.aw-g img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.aw-g figcaption{padding:16px 18px 20px}.aw-g b{display:block;font:800 1.9rem var(--display);color:var(--b700)}.aw-g span{color:#4A5B75}
@media (max-width:900px){.aw-g{grid-template-columns:repeat(2,minmax(0,1fr))}}
/* works guide */
.tk-guide{position:absolute;right:84px;bottom:110px;z-index:8;border:0;cursor:pointer;text-align:right;font:700 1rem/1.35 var(--display);color:#0B1F3A;background:#fff;padding:12px 16px;border-radius:16px;box-shadow:0 12px 30px rgba(0,0,0,.35);transition:opacity .3s,transform .3s;animation:gd 1.6s ease-in-out infinite}
.tk-guide b{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:var(--b600);color:#fff;margin-left:6px}
.tk-guide.hide{opacity:0;transform:translateY(10px);pointer-events:none;animation:none}
@keyframes gd{50%{transform:translateY(6px)}}
@media (max-width:700px){.tk-guide{right:70px;bottom:140px;font-size:.9rem}}
/* courses transition: calm */
.cv{position:absolute;left:0;right:0;bottom:0;height:100%;transform:translateY(100%);animation:cvIn .55s cubic-bezier(.7,0,.2,1) forwards}
.cv.a{background:var(--b100)}.cv.b{background:var(--b600);animation-delay:.08s}
@keyframes cvIn{to{transform:none}}
.pt.out .cv{transform:none;animation:cvOut .6s cubic-bezier(.7,0,.2,1) forwards}.pt.out .cv.a{animation-delay:.08s}
@keyframes cvOut{to{transform:translateY(-100%)}}
.cv-t{position:absolute;left:50%;top:50%;transform:translate(-50%,-40%);font:800 clamp(3rem,8vw,6rem) var(--display);color:#fff;opacity:0;animation:cvT .45s .35s forwards}
@keyframes cvT{to{opacity:1;transform:translate(-50%,-50%)}}
.pt.out .cv-t{opacity:1;animation:fadeOut .2s forwards}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
rep("var hold={courses:1000,","var hold={courses:750,")
open('/home/claude/hamsterhub-home/v26.html','w').write(s)
print('v26 ok',len(s))
