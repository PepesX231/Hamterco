SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build68.py').read())
# ================= A. hero: Hamster Hub's own look =================
rep('<p class="zq-q">น้องอยาก...</p>','<p class="zq-lead"><img src="img/hh-mascot.webp" alt="">Hamster Hub สอนน้องมัธยมสร้างเกม เว็บ และ IoT ของตัวเอง</p><p class="zq-q">น้องอยาก...</p>')
i=s.index('<p class="zq-pop">');j=s.index('</p>',i)+4
s=s[:j]+'<div class="zq-ptn"><span>จัดกิจกรรมร่วมกับ</span><img src="img/p-it.webp" alt="คณะเทคโนโลยีสารสนเทศ สจล."><img src="img/p-iote.webp" alt="IoTE สจล."><img src="img/p-eduverse.webp" alt="EDUverse"></div><div class="zq-brand" aria-hidden="true"><i class="zb-ring"></i><img src="img/hh-mascot.webp" alt=""></div>'+s[j:]
# ================= B. home: what Hamster Hub builds, startup first =================
rep('<h2 id="ocH">เราไม่ได้สอนแค่ทำพอร์ต<br>เราสอนให้น้องสร้างของจริง</h2><p>น้องที่นี่ทำแอปที่ช่วยคนได้ เกมที่มีคนเล่นจริง ผลงานที่ขายได้ และพอร์ตที่พาติดมหาลัย</p>',
    '<h2 id="ocH">สิ่งที่ Hamster Hub สร้าง</h2><p>สตาร์ทอัพที่ขายได้จริง รุ่นพี่ที่ติดมหาลัย ผลงานที่ชนะระดับประเทศ และเกมที่มีคนเล่นจริง ทั้งหมดสร้างโดยน้องมัธยม</p>')
import re
arts=re.findall(r'\n  <article class="oc-r[^"]*">.*?</article>\n',s[s.index('<section class="oc"'):s.index('<dialog class="oc-dlg"')],re.S)
assert len(arts)==4,len(arts)
rev,biz,game,uni=arts
biz2='''
  <article class="oc-r oc-big">
    <div class="oc-m oc-biz"><img src="img/w-mrcity.webp" alt="ภาพจากเกม Mr. City"><img src="img/w-phcmap.webp" alt="ภาพจากเกม PHC Map"><img src="img/w-quest.webp" alt="ภาพจากเว็บ Hamster Quest"></div>
    <div class="oc-t"><span class="oc-k">สร้างสตาร์ทอัพ</span>
      <h3>ผลงานของน้อง ขายได้และมีคนใช้จริง</h3>
      <p>Mr. City เกมแนะนำที่เที่ยวในสงขลา ขายให้สวนสัตว์สงขลาแล้ว PHC Map เกมสอนเขียน Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน และ Hamster Quest เว็บเรียนที่เล่นเหมือนเกม กำลังเตรียมใช้กับมหาวิทยาลัย</p>
      <ol class="oc-st"><li>คิดไอเดีย</li><li>ทำผลงาน</li><li>พัฒนาเชิงลึก</li><li>เป็นสตาร์ทอัพ</li></ol>
      <a class="oc-lk" href="#about">ดูว่ามีคนใช้จริงยังไง</a>
    </div>
  </article>
'''
uni2=uni.replace('<article class="oc-r rv2">','<article class="oc-r">')
rev2=rev.replace('<article class="oc-r">','<article class="oc-r rv2">').replace('สร้างของที่ช่วยคนได้จริง','ชนะระดับประเทศ')
game2=game
blk=''.join(arts)
s=s.replace(blk,biz2+uni2+rev2+game2.replace('<article class="oc-r">','<article class="oc-r">'))
s=s.replace('<h3>เกมของน้อง มีคนเล่นแล้วกว่า 1,000 คน</h3>','<h3>เกมที่น้องสร้างเองทั้งเกม</h3>').replace('<p>PHC Map เกมสอนเขียนโปรแกรม Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน ส่วน LYNO ของน้องดา, Time Keeper บน Roblox ของพี่มิคกี้ และ Z.O.O. ของพี่ไอซ์ คือเกมที่น้องสร้างเองทั้งเกม</p>','<p>LYNO เกมปริศนา 3 มิติของน้องดา, Time Keeper เกมผจญภัยบน Roblox ของพี่มิคกี้ และ Z.O.O. เกมสืบสวนของพี่ไอซ์ ปีนี้มีเกมของน้องๆ 10 เกมใน Hall of Fame</p>')

# ================= C. about: startup leads, then uni and competitions; real use explained =================
i=s.index('<section class="ab-do">');j=s.index('<section class="ab-res">')
ABOUT='''<section class="ab-do2"><div class="wrap"><h2 class="sec-h">เราทำอะไร</h2>
    <a class="ad-big" href="#about-real"><span class="ad-im"><img src="img/w-quest.webp" alt="" loading="lazy"><img src="img/w-mrcity.webp" alt="" loading="lazy"></span><span class="ad-tx"><small>สิ่งที่เราภูมิใจที่สุด</small><b>พาน้องสร้างสตาร์ทอัพ</b><span>เปลี่ยนไอเดียของน้องให้เป็นโปรดักต์จริงใน 4 ขั้น ตั้งแต่ออกแบบนวัตกรรม ทำผลงานกับเพื่อนในคอมมูนิตี้ พัฒนาเชิงลึก จนต่อยอดเป็นสตาร์ทอัพที่มีรายได้</span><ol class="oc-st"><li>คิดไอเดีย</li><li>ทำผลงาน</li><li>พัฒนาเชิงลึก</li><li>เป็นสตาร์ทอัพ</li></ol></span></a>
    <div class="ad-two">
      <a class="ad-s" href="#works" data-pane="sen"><span class="ad-si"><img src="img/dek69-6.webp" alt="" loading="lazy"><img src="img/dek69-3.webp" alt="" loading="lazy"><img src="img/dek69-13.webp" alt="" loading="lazy"></span><b>พาเข้ามหาวิทยาลัย</b><span>คอร์สทำพอร์ต และซ้อมนำเสนอกับอาจารย์มหาวิทยาลัย ปี 2569 รุ่นพี่ติดรอบ Portfolio 48 คน</span><em>ดูรุ่นพี่ที่ติดแล้ว</em></a>
      <a class="ad-s" href="#activity"><span class="ad-si one"><img src="img/sc-revoice.webp" alt="" loading="lazy"></span><b>พาลงเวทีจริง</b><span>ค่าย Game Jam และการแข่งขันร่วมกับ สจล. 12 ผลงานเข้ารอบชิง NSC (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย)</span><em>ดูกิจกรรม</em></a>
    </div></div></section>
  <section class="ab-use" id="about-real"><div class="wrap"><h2 class="sec-h">ผลงานของน้องที่มีคนใช้จริง</h2><p class="ab-use-s">ไม่ใช่แค่งานส่งครู แต่ละชิ้นมีคนใช้งานจริงแบบนี้</p>
    <article class="us"><div class="us-m"><img src="img/w-mrcity.webp" alt="ภาพจากเกม Mr. City" loading="lazy"></div><div class="us-t"><h3>Mr. City</h3><p>เกมแนะนำที่เที่ยวในสงขลา</p>
      <dl><div><dt>ใครใช้</dt><dd>สวนสัตว์สงขลา</dd></div><div><dt>ใช้ยังไง</dt><dd>ซื้อเกมนี้ไปใช้แนะนำที่เที่ยวในสงขลา</dd></div><div><dt>ผลลัพธ์</dt><dd class="ok">ขายได้แล้ว</dd></div></dl></div></article>
    <article class="us rv2"><div class="us-m"><img src="img/w-phcmap.webp" alt="ภาพจากเกม PHC Map" loading="lazy"></div><div class="us-t"><h3>PHC Map</h3><p>เกมสอนเขียนโปรแกรม Python</p>
      <dl><div><dt>ใครใช้</dt><dd>เด็กที่เริ่มเรียนเขียนโปรแกรม</dd></div><div><dt>ใช้ยังไง</dt><dd>เล่นผ่านด่านบนแผนที่ แต่ละด่านคือบทเรียน Python</dd></div><div><dt>ผลลัพธ์</dt><dd class="ok">ใช้สอนเด็กไปแล้วกว่า 1,000 คน</dd></div></dl></div></article>
    <article class="us"><div class="us-m"><img src="img/w-quest.webp" alt="ภาพจากเว็บ Hamster Quest" loading="lazy"></div><div class="us-t"><h3>Hamster Quest</h3><p>เว็บเรียนที่เล่นเหมือนเกม</p>
      <dl><div><dt>ใครใช้</dt><dd>น้องที่เรียนกับ Hamster Hub และมหาวิทยาลัยที่กำลังเตรียมนำไปใช้</dd></div><div><dt>ใช้ยังไง</dt><dd>ทำเควสต์ เก็บรางวัล และเรียนรู้ทีละขั้นเหมือนเล่นเกม</dd></div><div><dt>ผลลัพธ์</dt><dd class="ok">กำลังเตรียมใช้กับมหาวิทยาลัย</dd></div></dl></div></article>
  </div></section>
  '''
s=s[:i]+ABOUT+s[j:]

# ================= D. activity page, rebuilt =================
a=s.index('<div data-view="activity">');b=s.index('<!-- ================= WORKS ================= -->')
ACTV='''<div data-view="activity">
  <section class="av-h"><div class="av-in">
    <h1>กิจกรรม</h1>
    <p>ค่าย เวิร์กชอป และการแข่งขัน ที่น้องได้ลงมือสร้างของจริงภายในไม่กี่วัน เหมาะกับน้องที่อยากลองก่อนเรียนคอร์สยาว</p>
  </div></section>
  <section class="av-next"><div class="av-in">
    <div class="avn">
      <div class="avn-m"><img src="img/afo-hero.webp" alt="All for One University"><span class="avn-tag" id="avnTag">กิจกรรมถัดไป</span></div>
      <div class="avn-t">
        <p class="avn-d">วันเสาร์ที่ 14 พ.ย. 2569 ที่ IoTE สจล. ลาดกระบัง</p>
        <h2>All for One University รอบชิงชนะเลิศ</h2>
        <p>ทีมที่ผ่านรอบออนไลน์ มานำเสนอผลงานจริงต่อกรรมการ</p>
        <p class="avn-g"><b>น้องได้</b>ขึ้นเวทีนำเสนอผลงานจริง เอาไปเล่าในพอร์ตได้</p>
        <div class="avn-cd" id="avnCd" aria-label="นับถอยหลังถึงวันงาน"><div><b>0</b><span>วัน</span></div><div><b>0</b><span>ชั่วโมง</span></div><div><b>0</b><span>นาที</span></div></div>
        <div class="avn-b"><a class="b1" href="https://www.hamsterhub.co/allforone" target="_blank" rel="noopener">ดูรายละเอียดงาน</a><a class="b2" href="https://page.line.me/jkm4247u?openQrModal=true" target="_blank" rel="noopener">รับแจ้งเตือนทาง LINE</a></div>
      </div>
    </div>
  </div></section>
  <section class="av-all"><div class="av-in">
    <div class="av-top"><h2>ปี 2569 เราจัดไปแล้ว <span id="avCount">17</span> งาน</h2>
      <div class="av-f" id="avF" role="group" aria-label="เลือกประเภทกิจกรรม"></div></div>
    <div class="av-g" id="avG"></div>
  </div></section>
  <section class="av-ph"><div class="av-in">
    <h2>บรรยากาศจริงในกิจกรรม</h2>
    <div class="av-pg"><img src="img/team-group.webp" alt="รูปรวมน้องๆ และทีม" loading="lazy"><img src="img/photo-camp.webp" alt="น้องๆ ในค่าย" loading="lazy"><img src="img/photo-class.webp" alt="น้องๆ ในห้องเรียน" loading="lazy"><img src="img/photo-desk.webp" alt="น้องๆ ทำงานที่โต๊ะคอม" loading="lazy"><img src="img/photo-group.webp" alt="น้องๆ ถ่ายรูปรวม" loading="lazy"></div>
  </div></section>
  <section class="av-cta"><div class="av-in">
    <img src="img/hh-mascot.webp" alt="">
    <div><h2>อยากรู้ก่อนใครเมื่อเปิดกิจกรรมใหม่</h2><p>ทัก LINE แล้วบอกว่าน้องเรียนชั้นไหน สนใจเรื่องอะไร ทีมจะแจ้งเมื่อมีกิจกรรมที่เหมาะ</p></div>
    <a href="https://page.line.me/jkm4247u?openQrModal=true" target="_blank" rel="noopener">รับแจ้งเตือนทาง LINE</a>
  </div></section>
</div>

'''
s=s[:a]+ACTV+s[b:]
JS=r'''  /* v69: activity page */
  (function(){var G=$('#avG'),F=$('#avF');if(!G||!F)return;
    var IMG={'IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','AI for Business':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'};
    var TC={'ค่าย':'#E8891C','เวิร์กชอป':'#1C74D9','แข่งขัน':'#D6336C','โชว์ผลงาน':'#7048E8','โครงการ':'#1E8E5A'};
    var GN={'ค่าย':'ได้ผลงานกลับไปภายในไม่กี่วัน','เวิร์กชอป':'ได้ลองทักษะใหม่ในวันเดียว','แข่งขัน':'ได้ลงแข่งจริง มีเรื่องเล่าใส่พอร์ต','โชว์ผลงาน':'ได้นำเสนอผลงานต่อคนจริง','โครงการ':'ได้ผลงานส่งเวทีระดับประเทศ'};
    var L=ACT.filter(function(a){return !a[4]});$('#avCount').textContent=L.length;
    var types=['ทั้งหมด'];L.forEach(function(a){if(types.indexOf(a[3])<0)types.push(a[3])});
    F.innerHTML=types.map(function(t,i){var n=t==='ทั้งหมด'?L.length:L.filter(function(a){return a[3]===t}).length;return '<button type="button" data-t="'+t+'" aria-pressed="'+(i?'false':'true')+'">'+t+' <span>'+n+'</span></button>'}).join('');
    function card(a){var im=IMG[a[1]],c=TC[a[3]]||'#1C74D9';
      return '<article class="avc" style="--tc:'+c+'"><div class="avc-m">'+(im?'<img src="img/'+im+'.webp" alt="" loading="lazy">':'<div class="avc-ty"><b>'+a[1]+'</b><img src="img/hh-mascot.webp" alt=""></div>')+'</div><div class="avc-t"><p class="avc-d"><span>'+a[3]+'</span>'+a[0]+'</p><h3>'+a[1]+'</h3><p>'+a[2]+'</p><p class="avc-g">น้องได้: '+GN[a[3]]+'</p></div></article>'}
    function show(t){G.innerHTML=L.filter(function(a){return t==='ทั้งหมด'||a[3]===t}).map(card).join('')}
    F.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;F.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});show(b.dataset.t)});show('ทั้งหมด');
    function cd(){var ms=new Date('2026-11-14T09:00:00+07:00')-new Date(),el=$('#avnCd');if(!el)return;if(ms<=0){el.hidden=true;$('#avnTag').textContent='จัดไปแล้ว';return}
      var d=Math.floor(ms/864e5),h=Math.floor(ms%864e5/36e5),m=Math.floor(ms%36e5/6e4),b=el.querySelectorAll('b');b[0].textContent=d;b[1].textContent=h;b[2].textContent=m}
    cd();setInterval(cd,30000)})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
CSS=r'''
/* ===== v69 ===== */
/* hero: Hamster Hub's own look, text left, the brand hamsters right */
.zq-top{display:grid!important;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);column-gap:clamp(24px,4vw,64px);align-items:center;text-align:left!important;max-width:1240px!important;width:100%!important;margin:0 auto!important;padding:0 16px;box-sizing:border-box}
.zq-top>*{grid-column:1}
.zq-lead{display:flex;align-items:center;gap:10px;margin:0 0 18px;font:700 clamp(.95rem,1.3vw,1.08rem) var(--display);color:#0D2E63}
.zq-lead img{width:34px;height:34px;border-radius:50%}
.zq-q{text-align:left!important;margin-left:0!important}
.zq-h{text-align:left!important;justify-content:flex-start!important;margin-left:0!important;margin-right:0!important}
.zq-sw{margin-left:0!important;margin-right:0!important;max-width:640px!important;width:100%!important}
.zq-pop{justify-content:flex-start!important;text-align:left!important;margin-left:0!important}
.zq-ptn{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-top:28px}
.zq-ptn span{font:600 .82rem var(--display);color:#6A7891}
.zq-ptn img{height:30px;width:auto;filter:grayscale(1);opacity:.7;transition:filter .3s,opacity .3s}
.zq-ptn img:hover{filter:none;opacity:1}
.zq-brand{grid-column:2!important;grid-row:1/span 7;position:relative;justify-self:center;width:min(100%,460px);aspect-ratio:1}
.zq-brand img{position:relative;width:100%;height:100%;object-fit:contain;filter:drop-shadow(0 30px 40px rgba(13,46,99,.25));animation:hhBob 6s ease-in-out infinite;transition:transform .5s cubic-bezier(.3,1.6,.5,1)}
.zb-ring{position:absolute;inset:6%;border-radius:50%;border:2px dashed rgba(28,116,217,.25);animation:hhSpin 40s linear infinite}
.zq-brand:hover img{transform:scale(1.04) rotate(-3deg)}
@keyframes hhBob{0%,100%{translate:0 0}50%{translate:0 -10px}}
@keyframes hhSpin{to{transform:rotate(360deg)}}
.zq.ask .zq-brand,.zq.ask .zq-lead,.zq.ask .zq-ptn{opacity:0;pointer-events:none;transition:opacity .3s}
.zq-sw .zq-res{left:0!important;right:-45%!important}
@media (max-width:1000px){.zq-top{grid-template-columns:minmax(0,1fr)}.zq-brand{grid-column:1!important;grid-row:auto;width:180px;order:-1;justify-self:start;margin-bottom:8px}.zb-ring{display:none}.zq-sw .zq-res{right:0!important}}
@media (max-width:700px){.zq-brand{width:120px}.zq-ptn img{height:24px}}
@media (prefers-reduced-motion:reduce){.zq-brand img,.zb-ring{animation:none}}
/* home rows: startup leads with three real products */
.oc-biz{display:grid;grid-template-columns:1.4fr 1fr;grid-template-rows:1fr 1fr;gap:6px}.oc-biz img:first-child{grid-row:span 2}.oc-biz img{min-height:0}
.oc-big .oc-t h3{font-size:clamp(1.8rem,3.2vw,2.7rem)}
/* about: one lead card, two under it */
.ab-do2{padding:clamp(70px,8vw,120px) 0}
.ab-do2 .sec-h{margin-bottom:32px}
.ad-big{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:0;border-radius:28px;overflow:hidden;background:#0D2E63;color:#fff;text-decoration:none;box-shadow:0 30px 60px -36px rgba(13,46,99,.7);transition:transform .25s}
.ad-big:hover{transform:translateY(-2px)}
.ad-im{display:grid;grid-template-rows:1fr 1fr;gap:4px;min-height:420px;background:#081B3F}.ad-im img{width:100%;height:100%;object-fit:cover;display:block;min-height:0}
.ad-tx{display:flex;flex-direction:column;gap:12px;justify-content:center;padding:clamp(28px,4vw,52px)}
.ad-tx small{font:700 .95rem var(--display);color:#FFD866}
.ad-tx b{font:800 clamp(2rem,3.6vw,3rem)/1.1 var(--display)}
.ad-tx>span{color:#D7E4FA;line-height:1.7;font-size:1.05rem}
.ad-tx .oc-st li{background:rgba(255,255,255,.1);color:#fff}.ad-tx .oc-st li::before{background:#FFD866;color:#0D2E63}
.ad-two{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px}
.ad-s{display:flex;flex-direction:column;gap:8px;border-radius:24px;background:#F3F6FB;padding:18px 18px 22px;text-decoration:none;color:inherit;transition:transform .2s,box-shadow .2s}
.ad-s:hover{transform:translateY(-2px);box-shadow:inset 0 0 0 1px #CFDDF1}
.ad-si{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;border-radius:16px;overflow:hidden;aspect-ratio:16/7;margin-bottom:8px}.ad-si.one{grid-template-columns:1fr}.ad-si img{width:100%;height:100%;object-fit:cover;object-position:50% 25%;min-height:0}
.ad-s b{font:800 1.5rem var(--display);color:#0D2E63}.ad-s>span{color:#2B3A55;line-height:1.6}.ad-s em{font-style:normal;font:700 .95rem var(--display);color:#1C5FC8;margin-top:4px}
.ab-use{padding:clamp(70px,8vw,120px) 0;background:#F6F8FC}
.ab-use-s{color:#4A5874;font-size:1.08rem;margin:-8px 0 0}
.us{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(24px,4vw,56px);align-items:center;margin-top:clamp(40px,5vw,64px)}
.us.rv2 .us-m{order:2}
.us-m{border-radius:24px;overflow:hidden;aspect-ratio:16/10;background:#0E1B3D;box-shadow:0 30px 60px -40px rgba(13,46,99,.6)}.us-m img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s}.us-m:hover img{transform:scale(1.025)}
.us-t h3{font:800 clamp(1.8rem,3vw,2.4rem) var(--display);color:#0D2E63;margin:0}.us-t>p{color:#4A5874;margin:4px 0 18px;font-size:1.05rem}
.us dl{margin:0;display:grid;gap:10px}.us dl div{display:grid;grid-template-columns:96px 1fr;gap:12px;align-items:baseline;padding:12px 16px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px #E3E9F3}
.us dt{font:700 .9rem var(--display);color:#6A7891}.us dd{margin:0;color:#0D2E63;font-weight:600;line-height:1.5}.us dd.ok{color:#137A43;font-weight:800}
@media (max-width:900px){.ad-big,.ad-two,.us{grid-template-columns:minmax(0,1fr)}.ad-im{min-height:260px}.us.rv2 .us-m{order:0}}
/* activity page */
[data-view="activity"]{background:#fff}
.av-in{max-width:1240px;margin:0 auto;padding:0 16px}
.av-h{padding:clamp(70px,8vw,110px) 0 28px}
.av-h h1{font:800 clamp(2.8rem,6vw,4.6rem)/1 var(--display);color:#0D2E63;margin:0}
.av-h p{color:#2B3A55;font-size:clamp(1.05rem,1.4vw,1.2rem);line-height:1.7;max-width:640px;margin:16px 0 0}
.avn{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);border-radius:28px;overflow:hidden;background:#0D2E63;color:#fff;box-shadow:0 30px 60px -36px rgba(13,46,99,.7)}
.avn-m{position:relative;min-height:380px;background:#1C5FC8}.avn-m img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.avn-tag{position:absolute;left:18px;top:18px;background:#FFD866;color:#5A3B00;font:800 .88rem var(--display);padding:7px 13px;border-radius:999px}
.avn-t{display:flex;flex-direction:column;gap:10px;justify-content:center;padding:clamp(26px,3.5vw,46px)}
.avn-d{color:#9FC4FF;font:700 .95rem var(--display);margin:0}
.avn-t h2{font:800 clamp(1.8rem,3vw,2.5rem)/1.15 var(--display);margin:0}
.avn-t>p{margin:0;color:#D7E4FA;line-height:1.6}
.avn-g b{display:inline-block;margin-right:8px;color:#FFD866}
.avn-cd{display:flex;gap:10px;margin-top:6px}.avn-cd div{min-width:78px;text-align:center;background:rgba(255,255,255,.08);border-radius:14px;padding:10px 8px}
.avn-cd b{display:block;font:800 1.9rem/1 var(--display)}.avn-cd span{font-size:.8rem;color:#BFD3F3}
.avn-b{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.avn-b a{font:800 .98rem var(--display);padding:12px 20px;border-radius:12px;text-decoration:none;transition:transform .15s}
.avn-b .b1{background:#fff;color:#0D2E63}.avn-b .b2{background:#06C755;color:#fff}.avn-b a:hover{transform:translateY(-2px)}
.av-all{padding:clamp(70px,8vw,110px) 0 20px}
.av-top{display:flex;flex-wrap:wrap;gap:18px;align-items:flex-end;justify-content:space-between}
.av-top h2,.av-ph h2{font:800 clamp(1.8rem,3.4vw,2.6rem)/1.15 var(--display);color:#0D2E63;margin:0}
.av-f{display:flex;flex-wrap:wrap;gap:8px}
.av-f button{border:0;cursor:pointer;font:700 .92rem var(--display);padding:9px 14px;border-radius:12px;background:#F1F4F9;color:#0D2E63;transition:background .2s}
.av-f button span{color:#6A7891;font-weight:600;margin-left:2px}
.av-f button:hover{background:#E3E9F3}
.av-f button[aria-pressed="true"]{background:#0D2E63;color:#fff}.av-f button[aria-pressed="true"] span{color:#9FC4FF}
.av-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px 20px;margin-top:28px}
.avc{display:flex;flex-direction:column;border-radius:22px;overflow:hidden;background:#fff;box-shadow:inset 0 0 0 1px #E6ECF5;transition:transform .2s,box-shadow .2s}
.avc:hover{transform:translateY(-3px);box-shadow:inset 0 0 0 1px #CFDDF1,0 20px 40px -28px rgba(13,46,99,.5)}
.avc-m{aspect-ratio:16/9;overflow:hidden;background:#0D2E63}.avc-m>img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}.avc:hover .avc-m>img{transform:scale(1.03)}
.avc-ty{position:relative;height:100%;display:flex;align-items:flex-end;padding:18px 20px;background:var(--tc);overflow:hidden}
.avc-ty b{position:relative;z-index:1;font:800 clamp(1.25rem,2vw,1.6rem)/1.15 var(--display);color:#fff;max-width:70%}
.avc-ty img{position:absolute;right:-30px;top:-20px;width:62%;opacity:.95;transform:rotate(8deg)}
.avc-t{padding:16px 18px 20px;display:flex;flex-direction:column;gap:6px;flex:1}
.avc-d{display:flex;align-items:center;gap:8px;margin:0;font:600 .85rem var(--display);color:#6A7891}
.avc-d span{color:#fff;background:var(--tc);padding:3px 9px;border-radius:999px;font-size:.78rem;font-weight:700}
.avc-t h3{font:800 1.15rem/1.3 var(--display);color:#0D2E63;margin:2px 0 0}
.avc-t>p{margin:0;color:#2B3A55;font-size:.94rem;line-height:1.55}
.avc-t .avc-g{margin-top:auto;padding-top:8px;color:#137A43;font-weight:700;font-size:.88rem}
.av-ph{padding:clamp(70px,8vw,110px) 0 0}
.av-pg{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:220px 220px;gap:8px;margin-top:24px;border-radius:24px;overflow:hidden}
.av-pg img{width:100%;height:100%;object-fit:cover;display:block}.av-pg img:first-child{grid-row:span 2}
.av-cta{padding:clamp(70px,8vw,110px) 0}
.av-cta .av-in{display:flex;align-items:center;gap:28px;background:#FFF4D1;border-radius:28px;padding:28px 36px}
.av-cta img{width:110px;flex:none}
.av-cta h2{font:800 clamp(1.4rem,2.4vw,1.9rem) var(--display);color:#0D2E63;margin:0}.av-cta p{margin:6px 0 0;color:#4A3A10}
.av-cta a{margin-left:auto;flex:none;background:#06C755;color:#fff;font:800 1rem var(--display);padding:14px 22px;border-radius:12px;text-decoration:none;transition:transform .15s}.av-cta a:hover{transform:translateY(-2px)}
@media (max-width:1000px){.av-g{grid-template-columns:repeat(2,minmax(0,1fr))}.avn{grid-template-columns:minmax(0,1fr)}.avn-m{min-height:240px}}
@media (max-width:640px){.av-g{grid-template-columns:minmax(0,1fr)}.av-pg{grid-template-columns:1fr 1fr;grid-template-rows:200px 140px 140px}.av-pg img:first-child{grid-column:span 2;grid-row:auto}.av-pg img:nth-child(5){display:none}.av-cta .av-in{flex-direction:column;align-items:flex-start;padding:24px}.av-cta a{margin-left:0}.avn-cd div{min-width:64px}}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v69.html','w').write(s)
print('v69 ok')
