D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build26.py').read())
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
PX='https://www.hamsterhub.co/portex-site/index.html'
LINE='https://page.line.me/jkm4247u?openQrModal=true'
EXT='href="'+PX+'" target="_blank" rel="noopener"'
hb2=open(SP+'hb2.html').read().replace('href="#portex"',EXT)
hb2=hb2.replace('<p class="hb2-n">Port Express · เริ่ม 9 พ.ย. 2569 · เรียน จ พ ศ</p>','<p class="hb2-n">Port Express · เริ่มเรียน 9 พ.ย. 2569 · เรียนสร้างเกมด้วย Unity · จันทร์ พุธ ศุกร์</p>')
hb2=hb2.replace('<p class="hb-p"><b>5,990 บาท</b> <s>9,990</s></p>','<p class="hb-p"><b>5,990 บาท</b> <s>9,990</s><em>ประหยัด 4,000</em></p>')
# ---------- hero: back to the block that sells the course ----------
i=s.index('  <section class="nh">');j=s.index('  <section class="hp-grid">',i)
fit='''  <section class="fit"><div class="fit-in">
    <div class="fit-h"><p class="fit-k">ยังไม่แน่ใจว่าเหมาะไหม</p><h2>ตอบ 3 ข้อ ดูว่าคอร์สนี้เหมาะกับน้องไหม</h2><p>ใช้เวลาไม่ถึง 10 วินาที ข้ามได้ ไม่ต้องกรอกชื่อหรือเบอร์</p></div>
    <form class="fit-q" id="fitQ" onsubmit="return false">
      <fieldset><legend>1. ตอนนี้น้องเรียนชั้นไหน</legend><label><input type="radio" name="g" value="m6">ม.6</label><label><input type="radio" name="g" value="m45">ม.4–5</label><label><input type="radio" name="g" value="o">อื่นๆ</label></fieldset>
      <fieldset><legend>2. มีผลงานไว้ยื่นพอร์ตแล้วหรือยัง</legend><label><input type="radio" name="p" value="no">ยังไม่มี</label><label><input type="radio" name="p" value="some">มีบ้าง</label><label><input type="radio" name="p" value="yes">มีพร้อมแล้ว</label></fieldset>
      <fieldset><legend>3. น้องสนใจสายไหน</legend><label><input type="radio" name="t" value="game">เกม</label><label><input type="radio" name="t" value="app">แอป / เว็บ</label><label><input type="radio" name="t" value="iot">IoT</label><label><input type="radio" name="t" value="any">ยังไม่รู้</label></fieldset>
    </form>
    <div class="fit-r" id="fitR" aria-live="polite"><p>เลือกคำตอบครบ 3 ข้อ แล้วผลจะขึ้นตรงนี้</p></div>
  </div></section>

'''
s=s[:i]+hb2+fit+s[j:]
# ---------- Hall of Fame: the gold row version ----------
i=s.index('    <section class="tile hz"');j=s.index('    </section>',i)+len('    </section>')
s=s[:i]+open(SP+'hof2.html').read()+s[j:]
# ---------- paths + about: real photos from the team ----------
s=s.replace('<img class="ph" src="img/s-showcase2.webp"','<img class="ph" src="img/w-revoice.webp"').replace('<img class="ph" src="img/s-showcase1.webp"','<img class="ph" src="img/team-group.webp"')
s=s.replace('<img class="b1" src="img/photo-camp.webp" alt="น้องๆ ในค่าย Hamster Hub" loading="lazy">','<img class="b1" src="img/team-group.webp" alt="น้องๆ Hamster Hub ในงานโชว์ผลงาน" loading="lazy">')
s=s.replace('<figure><img src="img/s-showcase1.webp" alt=""><figcaption><b>12 ผลงาน</b>','<figure><img src="img/w-revoice.webp" alt="ReVoice ผลงานของน้องไอดิน"><figcaption><b>12 ผลงาน</b>')
# ---------- fit finder logic ----------
rep("  /* router */",r'''  /* fit finder: ask before selling */
  (function(){var f=document.getElementById('fitQ'),r=document.getElementById('fitR');if(!f)return;
    f.addEventListener('change',function(){var d=new FormData(f),g=d.get('g'),p=d.get('p'),t=d.get('t');if(!g||!p||!t)return;
      var line='<a class="fb2" href="'''+LINE+r'''" target="_blank" rel="noopener">ทัก LINE ให้ทีมแนะนำ</a>';
      if(g==='m6'&&p!=='yes'&&(t==='game'||t==='any')){r.className='fit-r ok';r.innerHTML='<p class="fr-k">เหมาะกับน้อง</p><h3>Port Express</h3><p>น้องอยู่ ม.6 และยังต้องการผลงานใส่พอร์ต คอร์สนี้พาทำเกมของตัวเองใน 2 เดือน ทันยื่นรอบ Portfolio</p><p class="fr-p"><b>5,990 บาท</b> · เริ่ม 9 พ.ย. 2569</p><div class="fr-b"><a class="fb1" '''+EXT.replace('"','\\"').replace('\\"','"')+r'''>ดูรายละเอียดและสมัครเรียน</a>'+line+'</div>'}
      else if(p==='yes'){r.className='fit-r';r.innerHTML='<p class="fr-k">น้องมีผลงานแล้ว</p><h3>ลองให้ทีมดูพอร์ตก่อน</h3><p>ทีมช่วยดูว่าผลงานที่มีพร้อมยื่นแล้วหรือยัง และควรเพิ่มอะไร</p><div class="fr-b">'+line+'</div>'}
      else{r.className='fit-r';r.innerHTML='<p class="fr-k">มีคอร์สที่เหมาะกว่า</p><h3>'+(t==='app'?'สายแอปและเว็บ':t==='iot'?'สาย IoT':'คอร์สปูพื้นฐาน')+'</h3><p>'+(g==='m45'?'น้องยังมีเวลาก่อนยื่น ทำผลงานใหญ่ขึ้นได้อีก':'คอร์สสายนี้เปิดเป็นรอบ')+' ทักทีมให้แนะนำรอบที่เหมาะกับน้อง</p><div class="fr-b">'+line+'</div>'}})})();
  /* router */''')
css=r'''
/* ===== v27 ===== */
.hb2{margin:12px 12px 0;border-radius:28px;min-height:auto!important}
.hb-p em{font-style:normal;font:800 .9rem var(--display);color:#3A2A00;background:var(--yel);padding:3px 12px;border-radius:999px;margin-left:10px;vertical-align:middle}
.hb2 .hb-p b{font-size:clamp(2.2rem,3.6vw,3rem)!important}
/* fit finder */
.fit{padding:12px 12px 0}
.fit-in{background:var(--b50);border-radius:28px;padding:clamp(32px,5vw,56px);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr) minmax(0,1fr);gap:28px;align-items:start}
.fit-k{font:700 .95rem var(--display);color:var(--b700)}
.fit-h h2{font:800 clamp(1.5rem,2.4vw,2rem)/1.25 var(--display);color:var(--b900);margin-top:6px}
.fit-h p:last-child{color:#4A5B75;margin-top:8px;font-size:.95rem}
.fit-q{display:grid;gap:16px}
.fit-q fieldset{border:0;margin:0;padding:0}
.fit-q legend{font:700 1rem var(--display);color:var(--b900);margin-bottom:8px}
.fit-q label{display:inline-flex;align-items:center;margin:0 6px 6px 0;padding:9px 16px;border-radius:999px;background:#fff;box-shadow:inset 0 0 0 1.5px var(--b200);font:600 .95rem var(--display);color:var(--b800);cursor:pointer;transition:background .15s,box-shadow .15s}
.fit-q label:hover{box-shadow:inset 0 0 0 1.5px var(--b600)}
.fit-q input{position:absolute;opacity:0;pointer-events:none}
.fit-q label:has(input:checked){background:var(--b600);color:#fff;box-shadow:none}
.fit-q label:has(input:focus-visible){outline:2px solid var(--b900);outline-offset:2px}
.fit-r{background:#fff;border-radius:20px;padding:22px;box-shadow:0 0 0 1px var(--b100);min-height:180px;color:#4A5B75}
.fit-r.ok{box-shadow:0 0 0 2px var(--b600)}
.fr-k{font:700 .9rem var(--display);color:var(--b700)}.fit-r h3{font:800 1.6rem var(--display);color:var(--b900);margin-top:4px}
.fit-r p{margin-top:6px;line-height:1.55}.fr-p b{color:var(--b700);font-size:1.3rem}
.fr-b{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.fr-b a{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:999px;font:700 .95rem var(--display);text-decoration:none}
.fb1{background:var(--b600);color:#fff}.fb2{background:#06C755;color:#fff}
@media (max-width:1000px){.fit-in{grid-template-columns:minmax(0,1fr)}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v27.html','w').write(s)
print('v27 ok',len(s),s.count('#portex'))
