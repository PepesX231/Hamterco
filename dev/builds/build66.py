SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build65.py').read())
# ---- featured: one wide card, two equal cards under it ----
def side(img,small,title,p,pr_ids,pr):
    return '''<a class="fx-s" href="'''+LINE+'''" target="_blank" rel="noopener"><span class="fx-si"><img src="'''+img+'''" alt="" loading="lazy"></span><span class="fx-sb">
          <small>'''+small+'''</small><b>'''+title+'''</b><span class="fx-sp">'''+p+'''</span>
          <span class="fx-pr"><span class="ft-av">'''+av(pr_ids)+'''</span>'''+pr+'''</span>
          <span class="fx-go">รับแจ้งเตือนรอบถัดไป</span></span></a>'''
FX='''<div class="fx">
    <a class="fx-main" href="'''+PX+'''" target="_blank" rel="noopener">
      <span class="fx-media"><video src="img/portex-hero.mp4" poster="img/portex-poster.webp" muted loop playsinline preload="none" aria-hidden="true"></video><span class="ft-live">เปิดรับสมัคร</span></span>
      <span class="fx-body">
        <small>สำหรับน้อง ม.6 ที่ยังไม่มีผลงาน</small>
        <b class="fx-t">Port Express</b>
        <span class="fx-d">จบคอร์ส น้องมีแฟ้มพอร์ตพร้อมยื่นรอบ Portfolio ผลงานในแฟ้มคือเกมที่น้องเขียนโปรแกรมสร้างเองด้วย Unity</span>
        <span class="fx-f"><span><b>2 เดือน</b>จันทร์ พุธ ศุกร์</span><span><b>9 พ.ย. 2569</b>เริ่มเรียน</span><span><b>5,990 บาท</b>ทั้งคอร์ส</span></span>
        <span class="fx-cta">ดูรายละเอียดคอร์ส</span>
      </span>
    </a>
    <div class="fx-row">
      '''+side('img/dek69-1.webp','สำหรับน้องที่ยังไม่เคยเขียนโปรแกรม','Hamstarter','เริ่มจากศูนย์ จนมีผลงานชิ้นแรกเป็นของตัวเอง',[1],'น้องปลื้มจากคอร์สนี้ ติดสถิติประยุกต์ฯ สจล.')+'''
      '''+side('img/sc-lyno.webp','สำหรับน้องที่อยากมีรางวัลระดับประเทศในพอร์ต','National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ เช่น NSC (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย)',[3,6,16],'รุ่นพี่ 5 คนจากคอร์สนี้ ติดวิศวะคอมฯ CEDT และวิทย์คอมฯ')+'''
    </div>
  </div>'''
s=s.replace(FT_GRID,FX)
# ---- replace the scroll story with plain outcome rows ----
OUT='''<section class="oc" aria-labelledby="ocH"><div class="oc-in">
  <div class="oc-hd"><h2 id="ocH">น้องที่นี่ไปได้ไกลกว่าการติดมหาลัย</h2><p>เราสอนให้น้องสร้างของจริง ที่มีคนใช้ ขายได้ และชนะรางวัล การยื่นพอร์ตเป็นแค่หนึ่งในทางที่น้องเลือกได้</p></div>

  <article class="oc-r">
    <div class="oc-m"><img src="img/sc-revoice.webp" alt="น้องไอดิน กับแอป REVOICE ที่เขาสร้าง" loading="lazy"></div>
    <div class="oc-t"><span class="oc-k">สร้างของที่ช่วยคนได้จริง</span>
      <h3>REVOICE แอปฝึกพูด ที่น้องไอดินสร้างเองใน 4 เดือน</h3>
      <p>แอปช่วยฝึกการสื่อสาร สำหรับคนที่มีปัญหาด้านการพูด เล่นเหมือนเกม ทำด้วย Unity ผลงานนี้พาน้องไอดินชนะ NSC 2025 (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย)</p>
      <button type="button" class="oc-play" data-v="img/story-nsc.mp4"><i aria-hidden="true"></i>ดูคลิปไอดินเล่า 27 วินาที</button>
    </div>
  </article>

  <article class="oc-r rv2">
    <div class="oc-m oc-4"><img src="img/su-innovation.webp" alt="" loading="lazy"><img src="img/su-project-creation.webp" alt="" loading="lazy"><img src="img/su-advanced-development.webp" alt="" loading="lazy"><img src="img/su-toward-startup.webp" alt="" loading="lazy"></div>
    <div class="oc-t"><span class="oc-k">ขายได้จริง หาเงินได้จริง</span>
      <h3>ผลงานของน้องต่อยอดเป็นธุรกิจได้</h3>
      <p>Mr. City เกมแนะนำที่เที่ยวในสงขลา ขายให้สวนสัตว์สงขลาแล้ว น้องที่อยากไปทางนี้เรียนตั้งแต่คิดไอเดีย ทำผลงาน พัฒนาให้เก่งขึ้น จนต่อยอดเป็นสตาร์ทอัพที่มีรายได้</p>
      <ol class="oc-st"><li>คิดไอเดีย</li><li>ทำผลงาน</li><li>พัฒนาเชิงลึก</li><li>เป็นสตาร์ทอัพ</li></ol>
    </div>
  </article>

  <article class="oc-r">
    <div class="oc-m oc-3"><img src="img/sc-lyno.webp" alt="น้องดา กับเกม LYNO" loading="lazy"><img src="img/sc-timekeeper.webp" alt="พี่มิคกี้ กับเกม Time Keeper" loading="lazy"><img src="img/sc-zoo.webp" alt="พี่ไอซ์ กับเกม Z.O.O." loading="lazy"></div>
    <div class="oc-t"><span class="oc-k">ทำเกมที่มีคนเล่นจริง</span>
      <h3>เกมของน้อง มีคนเล่นแล้วกว่า 1,000 คน</h3>
      <p>PHC Map เกมสอนเขียนโปรแกรม Python ใช้สอนเด็กไปแล้วกว่า 1,000 คน ส่วน LYNO ของน้องดา, Time Keeper บน Roblox ของพี่มิคกี้ และ Z.O.O. ของพี่ไอซ์ คือเกมที่น้องสร้างเองทั้งเกม</p>
      <a class="oc-lk" href="#works">ดูเกมของน้องๆ ทั้งหมด</a>
    </div>
  </article>

  <article class="oc-r rv2">
    <div class="oc-m oc-w">'''+''.join('<img src="img/dek69-%d.webp" alt="" loading="lazy">'%i for i in [3,6,13,10,16,4])+'''</div>
    <div class="oc-t"><span class="oc-k">ติดมหาลัยด้วยผลงานของตัวเอง</span>
      <h3>ปี 2569 รุ่นพี่ติดมหาลัยรอบ Portfolio 48 คน</h3>
      <p>สจล. 24 คน มหิดล 9 คน จุฬาฯ 8 คน และเกษตรศาสตร์ 7 คน หลายคนได้เรียนวิศวะคอมฯ CEDT และวิทย์คอมฯ ด้วยผลงานที่ทำกับเรา</p>
      <a class="oc-lk" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a>
    </div>
  </article>
</div>
<dialog class="oc-dlg" id="ocDlg" aria-label="คลิปไอดิน"><video controls playsinline preload="none"></video><button type="button" class="oc-x" aria-label="ปิดคลิป">&times;</button></dialog>
</section>
'''
assert WH+CH in s
OUT=OUT.replace(' loading="lazy"','')
s=s.replace(WH+CH,OUT)
JS=r'''  /* v66: story clip opens in a player with sound, only when asked */
  (function(){var d=$('#ocDlg');if(!d)return;var v=d.querySelector('video');
    document.querySelectorAll('.oc-play').forEach(function(b){b.addEventListener('click',function(){v.src=b.dataset.v;if(d.showModal)d.showModal();else d.setAttribute('open','');v.play().catch(function(){})})});
    function shut(){v.pause();d.close?d.close():d.removeAttribute('open')}
    d.querySelector('.oc-x').addEventListener('click',shut);d.addEventListener('click',function(e){if(e.target===d)shut()});d.addEventListener('close',function(){v.pause()})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
CSS=r'''
/* ===== v66: featured layout, outcome rows ===== */
.fx{display:grid;gap:20px;margin-top:32px}
.ft-c .fx{margin-top:8px}
.fx-main{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);border-radius:28px;overflow:hidden;background:#0D2E63;color:#fff;text-decoration:none;box-shadow:0 30px 60px -36px rgba(13,46,99,.7);transition:transform .25s}
.fx-main:hover{transform:translateY(-2px)}
.fx-media{position:relative;min-height:100%;aspect-ratio:16/9;overflow:hidden;background:#1D1550 url(img/portex-poster.webp) center/cover}
.fx-media video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.22,1,.36,1)}
.fx-main:hover .fx-media video{transform:scale(1.025)}
.fx-body{display:flex;flex-direction:column;gap:12px;padding:clamp(24px,3vw,40px);justify-content:center}
.fx-body small{color:#9FC4FF;font:600 .95rem var(--display)}
.fx-t{font:800 clamp(2rem,3.4vw,3rem)/1 var(--display)}
.fx-d{color:#D7E4FA;line-height:1.65}
.fx-f{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:4px}
.fx-f>span{background:rgba(255,255,255,.08);border-radius:14px;padding:12px 14px;font-size:.84rem;color:#BFD3F3}
.fx-f b{display:block;font:800 1.08rem var(--display);color:#fff;margin-bottom:2px;white-space:nowrap}
.fx-cta{align-self:flex-start;margin-top:8px;background:#fff;color:#0D2E63;font:800 1rem var(--display);padding:13px 22px;border-radius:12px;transition:transform .2s}
.fx-main:hover .fx-cta{transform:translateY(-2px)}
.fx-row{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.fx-s{display:grid;grid-template-columns:150px minmax(0,1fr);gap:20px;align-items:stretch;border-radius:24px;background:#F3F6FB;padding:16px;text-decoration:none;color:inherit;transition:transform .2s,box-shadow .2s}
.fx-s:hover{transform:translateY(-2px);box-shadow:inset 0 0 0 1px #CFDDF1}
.fx-si{border-radius:16px;overflow:hidden;background:#D9E2EF}.fx-si img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;display:block;transition:transform .5s}
.fx-s:hover .fx-si img{transform:scale(1.03)}
.fx-sb{display:flex;flex-direction:column;gap:6px;padding:6px 6px 6px 0}
.fx-sb small{color:#1C5FC8;font:700 .85rem var(--display)}
.fx-sb>b{font:800 1.5rem var(--display);color:#0D2E63}
.fx-sp{color:#2B3A55;line-height:1.55}
.fx-pr{display:flex;align-items:center;gap:10px;margin-top:auto;padding-top:10px;font-size:.84rem;color:#4A5874;line-height:1.4}
.fx-go{align-self:flex-start;margin-top:8px;font:700 .9rem var(--display);color:#1C5FC8;background:#fff;padding:10px 14px;border-radius:10px;box-shadow:inset 0 0 0 1px #D5E1F2}
@media (max-width:980px){.fx-main{grid-template-columns:minmax(0,1fr)}.fx-row{grid-template-columns:minmax(0,1fr)}}
@media (max-width:560px){.fx-f{grid-template-columns:minmax(0,1fr)}.fx-s{grid-template-columns:96px minmax(0,1fr);gap:14px}}

.oc{background:#fff;padding:clamp(90px,10vw,150px) 16px clamp(60px,8vw,110px)}
.oc-in{max-width:1240px;margin:0 auto}
.oc-hd{max-width:760px}
.oc-hd h2{font:800 clamp(2.2rem,4.6vw,3.8rem)/1.12 var(--display);color:#0D2E63;margin:0}
.oc-hd p{color:#2B3A55;font-size:clamp(1.05rem,1.4vw,1.2rem);line-height:1.7;margin:16px 0 0}
.oc-r{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(28px,5vw,72px);align-items:center;margin-top:clamp(56px,7vw,96px)}
.oc-r.rv2 .oc-m{order:2}
.oc-m{border-radius:28px;overflow:hidden;background:#0E1B3D;aspect-ratio:4/3;box-shadow:0 30px 60px -40px rgba(13,46,99,.6)}
.oc-m img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s cubic-bezier(.22,1,.36,1)}
.oc-m:hover img{transform:scale(1.025)}
.oc-4{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:6px}
.oc-3{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:6px}.oc-3 img:first-child{grid-row:span 2}
.oc-w{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:6px}.oc-w img{object-position:50% 25%}
.oc-4 img,.oc-3 img,.oc-w img{min-height:0}
.oc-k{display:inline-block;font:700 .92rem var(--display);color:#1C5FC8;background:#EEF4FD;padding:6px 12px;border-radius:999px}
.oc-t h3{font:800 clamp(1.6rem,2.8vw,2.4rem)/1.2 var(--display);color:#0D2E63;margin:16px 0 12px}
.oc-t p{color:#2B3A55;line-height:1.75;margin:0;font-size:1.05rem;max-width:52ch}
.oc-st{list-style:none;margin:20px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:8px;counter-reset:st}
.oc-st li{counter-increment:st;display:flex;align-items:center;gap:8px;font:700 .9rem var(--display);color:#0D2E63;background:#F3F6FB;padding:8px 12px 8px 8px;border-radius:12px}
.oc-st li::before{content:counter(st);display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:#0D2E63;color:#fff;font-size:.78rem}
.oc-play,.oc-lk{display:inline-flex;align-items:center;gap:10px;margin-top:22px;border:0;cursor:pointer;font:700 1rem var(--display);padding:13px 20px;border-radius:12px;background:#0D2E63;color:#fff;text-decoration:none;transition:transform .15s,background .2s}
.oc-play:hover,.oc-lk:hover{transform:translateY(-2px);background:#163E80}.oc-play:active,.oc-lk:active{transform:scale(.97)}
.oc-play i{width:0;height:0;border-left:11px solid #fff;border-top:7px solid transparent;border-bottom:7px solid transparent}
.oc-dlg{border:0;padding:0;background:transparent;max-width:min(92vw,640px);width:100%;overflow:visible}
.oc-dlg::backdrop{background:rgba(6,14,32,.78)}
.oc-dlg video{width:100%;display:block;border-radius:20px;background:#000;aspect-ratio:1}
.oc-x{position:absolute;top:-16px;right:-16px;width:40px;height:40px;border-radius:50%;border:0;background:#fff;color:#0D2E63;font-size:1.5rem;cursor:pointer;box-shadow:0 6px 20px rgba(0,0,0,.3)}
@media (max-width:900px){.oc-r{grid-template-columns:minmax(0,1fr);gap:22px}.oc-r.rv2 .oc-m{order:0}.oc-x{top:-48px;right:0}}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v66.html','w').write(s)
print('v66 ok')
