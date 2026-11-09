import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build28.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
LINE='https://page.line.me/jkm4247u?openQrModal=true'
EXT='href="'+PX+'" target="_blank" rel="noopener"'
# ---------- HERO ----------
i=s.index('<section class="hb hb2">');j=s.index('</section>',i)+10
s=s[:i]+'''<section class="hq"><div class="hq-in">
    <div class="hq-tx">
      <p class="hq-k">Port Express · คอร์สทำพอร์ตยื่นมหาลัย สำหรับ ม.6</p>
      <h1 class="hq-h">เรียน 2 เดือน<br><span>มีผลงานจริงไปยื่นพอร์ต</span></h1>
      <ul class="hq-m"><li><small>เริ่มเรียน</small>9 พ.ย. 2569</li><li><small>วันเรียน</small>จันทร์ พุธ ศุกร์</li><li><small>สอนอะไร</small>สร้างเกมด้วย Unity</li></ul>
      <div class="hq-p"><b>5,990</b><span>บาท</span><s>9,990</s><em>ประหยัด 4,000</em></div>
      <div class="hq-b"><a class="go" '''+EXT+'''>สมัครเรียน</a><a class="ln" href="'''+LINE+'''" target="_blank" rel="noopener">มีคำถาม ทัก LINE ถามทีม</a></div>
    </div>
    <a class="hq-v" '''+EXT+''' aria-label="ดูรายละเอียดคอร์ส Port Express"><video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video></a>
  </div>
  <ol class="hq-s">
    <li><img src="img/work-phi-krahang.webp" alt=""><div><small>ขั้นที่ 1</small><b>เรียนทำเกมกับพี่ๆ</b><span>ไม่เคยทำมาก่อนก็เริ่มได้</span></div></li>
    <li><img src="img/folio.webp" alt=""><div><small>ขั้นที่ 2</small><b>ได้ผลงานใส่แฟ้มพอร์ต</b><span>พร้อมสไลด์เล่าผลงาน และซ้อมสัมภาษณ์</span></div></li>
    <li><img src="img/dek69-13.webp" alt="" style="object-position:50% 25%"><div><small>ขั้นที่ 3</small><b>ยื่นรอบ Portfolio</b><span>รุ่นพี่ติดมหาลัยแล้ว 48 คน</span></div></li>
  </ol>
</section>'''+s[j:]
# ---------- paths: only pictures that explain themselves ----------
s=re.sub(r'<img class="ms" src="img/[a-z-]+\.webp" alt="" loading="lazy"><i class="bubble">[^<]*</i>','',s)
s=s.replace('<img class="ph" src="img/team-group.webp"','<img class="ph" src="img/k-gamejam.webp"')
# ---------- static mascots out ----------
s=s.replace('<img class="hf-tr" src="img/n-win.webp" alt="">','')
s=re.sub(r'<img class="do-i" src="img/[a-z-]+\.webp" alt="" loading="lazy">','',s)
s=s.replace('<p class="au-n"><img src="img/ev-st0.webp" alt="">','<p class="au-n">')
s=re.sub(r'<li class="rv"><img src="img/real-\d\.webp" alt="" loading="lazy">','<li class="rv">',s)
s=s.replace('<p class="rw-n">Mr. City, PHC Map และ Hamster Quest ยังใช้ภาพวาดประกอบ รอภาพจริงจากทีม</p>','')
s=s.replace('<figure><img src="img/real-0.webp" alt=""><figcaption><b>ขายได้จริง</b>','<figure class="nopic"><figcaption><b>ขายได้จริง</b>')
s=s.replace("<img class=\"er-s\" src=\"img/'+MAS[a[3]]+'.webp\" alt=\"\" loading=\"lazy\">","<span class=\"er-c\" style=\"--c:'+ACOL[a[3]][1]+'\">'+a[3]+'</span>")
# ---------- Hall of Fame: no boxes, no clipped edges ----------
i=s.index('<section class="hp-grid hof-s">');j=s.index('</section>',i)+10
F=[('stressstrike','StressStrike','ชนะเลิศ OBEC'),('phi-krahang','ผีกระหัง',''),('eugation-strike','Eugation Strike',''),('slash-speed','SLASH//SPEED',''),('escape-rolling','Escape Rolling','')]
s=s[:i]+'''<section class="h5f" aria-label="Hall of Fame">
    <p class="h5f-k">ผลงานเด่นของน้องๆ ปี 2569</p>
    <h2 class="h5f-t">HALL OF FAME</h2>
    <p class="h5f-s">ทุกเกมด้านล่าง น้องๆ เขียนโปรแกรมสร้างเองกับมือ</p>
    <div class="h5f-r">'''+''.join('<a class="h5f-c" href="#works" data-pane="hof" style="--i:%d"><img src="img/work-%s.webp" alt="" loading="lazy"><b>%s</b>%s</a>'%(k-2,f[0],f[1],('<em>'+f[2]+'</em>' if f[2] else '')) for k,f in enumerate(F))+'''</div>
    <a class="h5f-go" href="#works" data-pane="hof">ดูผลงานทั้งหมด</a>
  </section>'''+s[j:]
css=r'''
/* ===== v29 ===== */
/* hero: calm navy, clear type scale */
.hq{margin:12px 12px 0;border-radius:28px;overflow:hidden;color:#fff;background:radial-gradient(60% 80% at 78% 30%,rgba(28,116,217,.45),transparent 70%),linear-gradient(160deg,#0B2550 0%,#081A3A 100%);padding:clamp(40px,5vw,72px) clamp(24px,5vw,72px) clamp(28px,4vw,48px)}
.hq-in{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:clamp(28px,4vw,64px);align-items:center}
.hq-k{font:600 1rem var(--display);color:var(--b200)}
.hq-h{font:800 clamp(2.4rem,4.4vw,4rem)/1.12 var(--display);letter-spacing:-.025em;margin-top:14px}
.hq-h span{color:var(--yel)}
.hq-m{list-style:none;margin:26px 0 0;padding:0;display:flex;gap:28px;flex-wrap:wrap}
.hq-m li{font:700 1.1rem var(--display)}.hq-m small{display:block;font:500 .85rem var(--display);color:var(--b200);margin-bottom:2px}
.hq-p{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-top:28px}
.hq-p b{font:800 clamp(2.8rem,4.4vw,3.6rem)/1 var(--display);letter-spacing:-.02em}.hq-p span{font:700 1.3rem var(--display)}
.hq-p s{color:var(--b200);margin-left:6px}.hq-p em{font-style:normal;font:800 .9rem var(--display);color:#3A2A00;background:var(--yel);padding:4px 12px;border-radius:999px}
.hq-b{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-top:24px}
.hq-b .go{display:inline-flex;align-items:center;min-height:54px;padding:0 34px;border-radius:999px;background:var(--yel);color:#2A1E00;font:800 1.1rem var(--display);text-decoration:none;transition:transform .15s,filter .2s}
.hq-b .go:hover{transform:translateY(-2px);filter:brightness(1.05)}
.hq-b .ln{color:#7CE3A6;font-weight:600;text-decoration:none;padding:8px 12px;margin-left:-12px;border-radius:999px}.hq-b .ln:hover{background:rgba(124,227,166,.12)}
.hq-v{display:block;border-radius:20px;overflow:hidden;box-shadow:0 0 0 1px rgba(255,255,255,.12),0 40px 70px -30px rgba(0,0,0,.7)}
.hq-v video{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}
.hq-s{list-style:none;margin:clamp(32px,4vw,48px) auto 0;padding:0;max-width:1240px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.hq-s li{display:flex;align-items:center;gap:14px;padding:12px;border-radius:18px;background:rgba(255,255,255,.06)}
.hq-s img{width:84px;height:64px;object-fit:cover;border-radius:12px;flex:none}
.hq-s small{display:block;font:600 .8rem var(--display);color:var(--b200)}.hq-s b{display:block;font:700 1.05rem var(--display)}.hq-s span{display:block;font-size:.88rem;color:rgba(255,255,255,.7)}
@media (max-width:900px){.hq-in,.hq-s{grid-template-columns:minmax(0,1fr)}.hq-v{order:-1}}
/* paths without mascots */
.f4.p3 .pod .ph{aspect-ratio:4/3}
/* no dashed floors */
.wkz::after{display:none}
/* Hall of Fame */
.h5f{position:relative;margin:12px 12px 0;border-radius:28px;overflow:hidden;text-align:center;color:#fff;padding:clamp(56px,7vw,96px) 16px clamp(48px,6vw,80px);
  background:radial-gradient(50% 60% at 50% 0%,rgba(255,206,110,.28),transparent 70%),linear-gradient(#120D05,#060402)}
.h5f-k{font:700 1.05rem var(--display);color:#F3D88E}
.h5f-t{font:900 clamp(3rem,9vw,7.6rem)/1 var(--display);letter-spacing:.04em;margin-top:10px;background:linear-gradient(100deg,#E8C877 0%,#FFF1C2 25%,#FFFFFF 33%,#F6DF9A 50%,#E8C877 100%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:hfS 6s linear infinite}
.h5f-s{color:rgba(255,246,214,.85);margin-top:12px;font-size:1.1rem}
.h5f-r{display:flex;justify-content:center;align-items:flex-start;gap:clamp(12px,1.6vw,24px);margin:clamp(36px,4vw,56px) auto 0;max-width:1200px;padding:0 8px}
.h5f-c{--i:0;flex:1;min-width:0;max-width:230px;text-decoration:none;color:#fff;transform:translateY(calc(var(--i) * var(--i) * 10px)) rotate(calc(var(--i) * 3deg));transition:transform .35s cubic-bezier(.3,1.4,.5,1)}
.h5f-c img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:18px;box-shadow:0 0 0 1px rgba(246,223,154,.35),0 30px 50px -24px rgba(0,0,0,.9),0 0 40px -10px rgba(255,200,90,.35)}
.h5f-c b{display:block;font:700 1rem var(--display);margin-top:12px}
.h5f-c em{display:inline-block;font-style:normal;font:700 .8rem var(--display);color:#1A1206;background:#F3D88E;padding:2px 10px;border-radius:999px;margin-top:6px}
.h5f-c:hover{transform:translateY(-10px) rotate(0)}
.h5f-go{display:inline-block;margin-top:36px;font:700 1.05rem var(--display);color:#1A1206;background:linear-gradient(90deg,#E8C877,#FFF1C2,#E8C877);padding:13px 30px;border-radius:999px;text-decoration:none}
@media (max-width:700px){.h5f-c:nth-child(1),.h5f-c:nth-child(5){display:none}.h5f-c{transform:none}}
/* seniors: clean stage */
.mc-in{background:radial-gradient(45% 55% at 50% 55%,rgba(120,180,255,.22),transparent 70%),linear-gradient(180deg,#0A2148 0%,#0D2E63 60%,#0A2148 100%)!important}
.mc-in::after,.mc-bg{display:none!important}
/* activity list: colored tag instead of a sticker */
.er{grid-template-columns:minmax(0,1fr)!important}.er-c{display:inline-block;font:700 .8rem var(--display);color:var(--c);background:color-mix(in srgb,var(--c) 12%,#fff);padding:3px 10px;border-radius:999px;margin-bottom:6px}
.er time{grid-column:auto!important}.er>div{grid-column:auto!important}
/* about */
.aw-g figure.nopic{background:var(--b600);color:#fff;display:flex;align-items:flex-end}.aw-g figure.nopic b{color:#fff}.aw-g figure.nopic span{color:rgba(255,255,255,.85)}
.rw li{padding:22px;border-radius:20px;background:var(--b50);text-align:left}.rw img.ph{display:block;margin-bottom:12px}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v29.html','w').write(s)
print('v29 ok',len(s),s.count('n-grad'),s.count('class="ms"'))
css2=r'''
.hq-h{font-size:clamp(2.2rem,3.5vw,3.4rem)}
.er-c{width:fit-content;justify-self:start}
.rw ul{align-items:start}.rw li img{display:none}
'''
s=s.replace('/* ---------- footer ---------- */',css2+'\n/* ---------- footer ---------- */',1)
open('/home/claude/hamsterhub-home/v29.html','w').write(s)
s=s.replace('.rw li img{display:none}','.rw li img{display:none}\n.ct-help{display:none}',1)
open('/home/claude/hamsterhub-home/v29.html','w').write(s)
