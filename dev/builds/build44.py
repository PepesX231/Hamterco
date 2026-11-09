SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build43.py').read())
# ---------- new "who we are" section
i=s.index('<section class="zh">');j=s.index('</section>',i)+10
SAY='Hamster Hub สอนน้อง ม.ปลาย ทำเกม เว็บ และ IoT จนมีผลงานจริงของตัวเอง แล้วพาผลงานนั้นไปยื่นมหาลัย ลงแข่ง และใช้งานได้จริง'
s=s[:i]+'''<section class="za">
    <div class="za-in">
      <p class="za-say" id="zaSay">'''+SAY+'''</p>
      <div class="za-b">
        <figure class="za-t t1"><img src="img/photo-group.webp" alt="น้องๆ และทีม Hamster Hub" loading="lazy"><figcaption><b>48 คน</b>รุ่นพี่ DEK69 ติดมหาลัยรอบ Portfolio</figcaption></figure>
        <figure class="za-t t2"><img src="img/work-stressstrike.webp" alt="เกม StressStrike" loading="lazy"><figcaption><b>ชนะเลิศ</b>OBEC Roboplayground ด้วยเกม StressStrike</figcaption></figure>
        <figure class="za-t t3"><img src="img/s-showcase1.webp" alt="งานโชว์ผลงานของน้องๆ" loading="lazy"><figcaption><b>12 ผลงาน</b>เข้ารอบชิงชนะเลิศ NSC</figcaption></figure>
        <figure class="za-t t4"><img src="img/photo-class.webp" alt="บรรยากาศในห้องเรียน" loading="lazy"><figcaption><b>17 กิจกรรม</b>ค่าย เวิร์กชอป และงานแข่งในปี 2569</figcaption></figure>
      </div>
      <h3 class="za-h">เริ่มจากสิ่งที่น้องอยากได้</h3>
      <div class="za-w">
        <a class="za-c" href="#" data-q="ยื่นพอร์ต"><img src="img/dek69-13.webp" alt="" loading="lazy"><span><small>สำหรับน้องที่อยาก</small><b>ติดมหาลัย</b><em>ทำผลงานจริงเข้าแฟ้มพอร์ต ซ้อมตอบคำถามกรรมการ</em><i>ดูคอร์สทำพอร์ต</i></span></a>
        <a class="za-c" href="#" data-q="สร้างเกม"><img src="img/work-phi-krahang.webp" alt="" loading="lazy"><span><small>สำหรับน้องที่อยาก</small><b>มีผลงานของตัวเอง</b><em>เริ่มจากศูนย์ได้ สร้างเกมหรือเว็บที่เล่นได้จริง แล้วเอาไปลงแข่ง</em><i>ดูคอร์สและค่ายสร้างเกม</i></span></a>
        <a class="za-c" href="https://page.line.me/jkm4247u?openQrModal=true" target="_blank" rel="noopener"><img src="img/photo-desk.webp" alt="" loading="lazy"><span><small>สำหรับ</small><b>ผู้ปกครอง</b><em>ถามรายละเอียดคอร์ส ราคา และวันเรียนกับทีมได้โดยตรง</em><i>ทัก LINE ถามทีม</i></span></a>
      </div>
    </div>
  </section>'''+s[j:]
JS=r'''
  /* who-we-are: words light up as you scroll */
  (function(){var p=$('#zaSay');if(!p)return;var ws=p.textContent.split(' ');p.innerHTML=ws.map(function(w){return '<span>'+w+'</span>'}).join(' ');var S=p.querySelectorAll('span');
    function up(){var r=p.getBoundingClientRect(),h=innerHeight,t=Math.min(1,Math.max(0,(h*.85-r.top)/(h*.6)));var n=Math.round(t*S.length);S.forEach(function(x,i){x.classList.toggle('lit',i<n)})}
    addEventListener('scroll',up,{passive:true});up()})();
  /* tilt + light on cards (pointer only) */
  (function(){if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
    document.querySelectorAll('.za-c,.za-t').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
      c.style.transform='perspective(900px) rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) translateY(-4px)';c.style.setProperty('--lx',(x+.5)*100+'%');c.style.setProperty('--ly',(y+.5)*100+'%')});
      c.addEventListener('pointerleave',function(){c.style.transform=''})})})();
  /* hero: the floating games follow the mouse at different depths */
  (function(){var z=$('.zq');if(!z||!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var I=z.querySelectorAll('.zq-dc img'),D=[1.2,.6,1,1.1,.7,.9,1.4],tx=0,ty=0,cx=0,cy=0,run=false;
    z.addEventListener('pointermove',function(e){tx=e.clientX/innerWidth-.5;ty=e.clientY/innerHeight-.5;if(!run){run=true;requestAnimationFrame(loop)}});
    function loop(){cx+=(tx-cx)*.08;cy+=(ty-cy)*.08;I.forEach(function(im,i){im.style.transform='translate('+(-cx*40*D[i])+'px,'+(-cy*30*D[i])+'px)'});if(Math.abs(tx-cx)>.001||Math.abs(ty-cy)>.001)requestAnimationFrame(loop);else run=false}})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v44 ===== */
/* no blinking dot */
.nw2-h::before{display:none!important}
/* cards without boxes: photo carries the card, text sits on the page */
.zk{border:0!important;background:none!important;border-radius:0!important;overflow:visible!important;box-shadow:none!important}
.zk:hover{transform:none!important;box-shadow:none!important}
.zk-i{border-radius:22px;overflow:hidden;box-shadow:0 18px 30px -22px rgba(13,46,99,.55);transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s}
.zk:hover .zk-i{transform:translateY(-4px);box-shadow:0 26px 40px -22px rgba(13,46,99,.6)}
.zk-b{padding:14px 4px 0!important}
.zk-a{color:#1C74D9}
.zk.on .zk-a{align-self:flex-start;padding:9px 18px!important;border-radius:999px!important}
.zq-res{background:none!important;box-shadow:none!important;padding:0 8px!important}
@media (max-width:700px){.zk-i{width:120px;border-radius:16px}.zk-b{padding:2px 0 0 14px!important}}
/* who we are */
.za{background:#fff;padding:clamp(80px,9vw,140px) 16px}
.za-in{max-width:1240px;margin:0 auto}
.za-say{font:800 clamp(1.9rem,4vw,3.4rem)/1.3 var(--display);letter-spacing:-.015em;max-width:24em;color:#0D2E63}
.za-say span{opacity:.16;transition:opacity .35s}.za-say span.lit{opacity:1}
.za-b{display:grid;grid-template-columns:1.4fr 1fr 1fr;grid-template-rows:260px 260px;gap:16px;margin-top:clamp(48px,6vw,80px)}
.za-t{position:relative;margin:0;border-radius:28px;overflow:hidden;transition:transform .25s ease-out;transform-style:preserve-3d}
.za-t.t1{grid-row:1/3}.za-t.t4{grid-column:2/4}
.za-t img{width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.za-t:hover img{transform:scale(1.05)}
.za-t::after,.za-c::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(400px circle at var(--lx,50%) var(--ly,50%),rgba(255,255,255,.18),transparent 60%);opacity:0;transition:opacity .3s}
.za-t:hover::after,.za-c:hover::after{opacity:1}
.za-t figcaption{position:absolute;left:0;right:0;bottom:0;padding:60px 24px 22px;color:rgba(255,255,255,.9);background:linear-gradient(transparent,rgba(5,18,40,.92) 60%);font-size:.98rem}
.za-t figcaption b{display:block;font:800 clamp(2rem,3.4vw,2.8rem)/1 var(--display);color:#fff;margin-bottom:6px}
.za-h{font:800 clamp(1.6rem,2.8vw,2.2rem) var(--display);color:#0D2E63;margin-top:clamp(64px,7vw,104px)}
.za-w{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:24px}
.za-c{position:relative;display:block;aspect-ratio:3/4;border-radius:28px;overflow:hidden;text-decoration:none;color:#fff;transition:transform .25s ease-out;box-shadow:0 30px 50px -30px rgba(13,46,99,.6)}
.za-c img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.za-c:hover img{transform:scale(1.06)}
.za-c>span{position:absolute;left:0;right:0;bottom:0;display:flex;flex-direction:column;gap:4px;padding:90px 26px 26px;background:linear-gradient(transparent,rgba(5,18,40,.9) 55%)}
.za-c small{font-size:.92rem;color:rgba(255,255,255,.75)}
.za-c b{font:800 clamp(1.6rem,2.4vw,2.1rem)/1.15 var(--display)}
.za-c em{font-style:normal;color:rgba(255,255,255,.85);line-height:1.5;margin-top:4px}
.za-c i{font-style:normal;align-self:flex-start;margin-top:14px;padding:10px 18px;border-radius:999px;background:rgba(255,255,255,.16);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);box-shadow:inset 0 0 0 1px rgba(255,255,255,.3);font:700 .95rem var(--display);transition:background .2s,color .2s}
.za-c:hover i{background:#fff;color:#0D2E63}
@media (max-width:900px){.za-b{grid-template-columns:1fr 1fr;grid-template-rows:auto}.za-t{aspect-ratio:4/3}.za-t.t1{grid-row:auto;grid-column:1/3}.za-t.t4{grid-column:1/3}.za-w{grid-template-columns:minmax(0,1fr)}.za-c{aspect-ratio:4/3}}
@media (max-width:560px){.za-b{grid-template-columns:minmax(0,1fr)}.za-t.t1,.za-t.t4{grid-column:auto}}
/* hero: glass search and a softer stage */
.zq{background:radial-gradient(60% 50% at 50% 45%,#fff,rgba(255,255,255,0) 70%),#E4EDFA}
.zq-dc img{will-change:transform;transition:none}
.zq-s{background:rgba(255,255,255,.75)!important;-webkit-backdrop-filter:blur(20px) saturate(160%);backdrop-filter:blur(20px) saturate(160%)}
.zq-h{background:linear-gradient(180deg,#123B7A,#0D2E63);-webkit-background-clip:text;background-clip:text;color:transparent!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v44.html','w').write(s)
print('v44 ok')
