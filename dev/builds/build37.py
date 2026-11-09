import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build36.py').read())
# 1) transitions: full show only the first time a page is opened, then fast
rep("var first=true;function route(){var v=(location.hash||'#home').slice(1);if(views.indexOf(v)<0)v='home';\n    if(first||reduce){first=false;show();return}",
    "var first=true,seenV={};function route(){var v=(location.hash||'#home').slice(1);if(views.indexOf(v)<0)v='home';\n    if(first||reduce){first=false;seenV[v]=1;show();return}\n    if(seenV[v]){clearTimeout(ptT);pt.className='pt';pt.innerHTML='';show();var vq=document.querySelector('[data-view].on');if(vq){vq.classList.remove('fast-in');void vq.offsetWidth;vq.classList.add('fast-in')}return}seenV[v]=1;")
# 3) scrollytelling: what 2 months of Port Express gives
ST=[('work-phi-krahang','ขั้นที่ 1','เรียนสร้างเกมด้วย Unity','เริ่มจากพื้นฐาน ไม่เคยเขียนโค้ดมาก่อนก็เรียนได้ เรียนสด จันทร์ พุธ ศุกร์'),
    ('work-eugation-strike','ขั้นที่ 2','ทำเกมของตัวเองจนเล่นได้จริง','น้องคิดไอเดียเอง ลงมือทำเอง ได้ผลงานที่เป็นของตัวเอง ไม่ใช่งานลอกตามตัวอย่าง'),
    ('photo-class','ขั้นที่ 3','อาจารย์มหาวิทยาลัยช่วยตรวจงาน','รู้ว่าผลงานต้องปรับตรงไหน ก่อนส่งให้กรรมการดูจริง'),
    ('folio','ขั้นที่ 4','ทำแฟ้มพอร์ตและสไลด์เล่าผลงาน','จัดผลงานลงพอร์ต พร้อมสไลด์ที่เล่าว่าน้องทำอะไร และได้เรียนรู้อะไร'),
    ('photo-desk','ขั้นที่ 5','ซ้อมตอบคำถามกรรมการ','ซ้อมสัมภาษณ์กับพี่ๆ จนเล่าผลงานของตัวเองได้ลื่นไหล'),
    ('dek69-13','ขั้นที่ 6','ยื่นรอบ Portfolio','รุ่นพี่ DEK69 ที่เรียนกับเรา ติดมหาวิทยาลัยแล้ว 48 คน')]
imgs=''.join('<img class="sy-i%s" src="img/%s.webp" alt="" loading="lazy" data-k="%d">'%(' on' if k==0 else '',a[0],k) for k,a in enumerate(ST))
steps=''.join('<li class="sy-s%s" data-k="%d"><small>%s</small><h3>%s</h3><p>%s</p></li>'%(' on' if k==0 else '',k,a[1],a[2],a[3]) for k,a in enumerate(ST))
SY='''<section class="sy" aria-label="2 เดือนใน Port Express น้องได้อะไรบ้าง">
      <div class="sy-hd"><p class="sy-k">Port Express · เรียน 2 เดือน</p><h2>2 เดือนนี้ น้องได้อะไรบ้าง</h2><p>เลื่อนลงเพื่อดูทีละขั้น ตั้งแต่วันแรกจนถึงวันยื่นพอร์ต</p></div>
      <div class="sy-g"><div class="sy-v"><div class="sy-f">'''+imgs+'''<span class="sy-n"><b id="syN">1</b>/'''+str(len(ST))+'''</span></div></div><ol class="sy-l">'''+steps+'''</ol></div>
    </section>
    '''
rep('<section class="ct-list">',SY+'<section class="ct-list">')
js=r'''
  /* courses: scrollytelling */
  (function(){var S=document.querySelectorAll('.sy-s'),I=document.querySelectorAll('.sy-i'),N=document.getElementById('syN');if(!S.length)return;
    function on(k){S.forEach(function(x){x.classList.toggle('on',+x.dataset.k===k)});I.forEach(function(x){x.classList.toggle('on',+x.dataset.k===k)});if(N)N.textContent=k+1}
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)on(+e.target.dataset.k)})},{rootMargin:'-45% 0px -45% 0px'});S.forEach(function(x){io.observe(x)})})();
  /* activity header: soft parallax on the photo stack */
  (function(){var P=document.querySelectorAll('.axh-p img');if(!P.length||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var K=[.18,-.12,.3,-.22,.08],tk=0;
    addEventListener('scroll',function(){if(tk)return;tk=requestAnimationFrame(function(){tk=0;var y=scrollY;if(y>900)return;P.forEach(function(p,i){p.style.transform='translateY('+(y*K[i]).toFixed(1)+'px)'})})},{passive:true})})();
'''
rep('/* walking hamsters: waddle walk',js+'  /* walking hamsters: waddle walk')
css=r'''
/* ===== v37 ===== */
/* quick re-entry for pages already seen */
[data-view].fast-in{animation:fastIn .28s ease-out both}
@keyframes fastIn{from{opacity:0;transform:translateY(8px)}}
/* button states: hover, pressed, keyboard focus */
.hq-b .go:active,.tk-more:active,.h5f-go:active,a.b1:active,.e1:active,.e2:active,.lbtn:active{transform:translateY(1px) scale(.97)!important;filter:brightness(.95)}
a:focus-visible,button:focus-visible{outline:3px solid #4DA3F0;outline-offset:3px}
.hq-b .go:focus-visible{outline-color:#fff}
/* scrollytelling */
.sy{margin:56px calc(50% - 50vw) 8px;padding:clamp(56px,6vw,88px) 0;color:#fff;background:radial-gradient(50% 60% at 25% 40%,rgba(77,163,240,.28),transparent 70%),linear-gradient(180deg,#071631,#0A2250)}
.sy-hd{max-width:1180px;margin:0 auto;padding:0 24px}
.sy-k{font:700 1rem var(--display);color:var(--yel)}
.sy-hd h2{font:800 clamp(2rem,4vw,3.2rem)/1.15 var(--display);margin-top:8px}
.sy-hd>p:last-child{color:#B3D8FF;margin-top:10px}
.sy-g{max-width:1180px;margin:40px auto 0;padding:0 24px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(24px,4vw,64px)}
.sy-v{position:relative}
.sy-f{position:sticky;top:calc(50vh - min(19vw,230px));aspect-ratio:4/3;overflow:hidden;box-shadow:0 0 0 1px rgba(255,255,255,.15),0 40px 70px -30px rgba(0,0,0,.8)}
.sy-i{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity .6s,transform 1.2s cubic-bezier(.2,.7,.2,1)}
.sy-i.on{opacity:1;transform:none}
.sy-n{position:absolute;right:0;bottom:0;background:var(--yel);color:#2A1E00;font:700 .95rem var(--display);padding:6px 14px}.sy-n b{font-size:1.2rem}
.sy-l{list-style:none;margin:0;padding:0}
.sy-s{min-height:62vh;display:flex;flex-direction:column;justify-content:center;opacity:.28;transition:opacity .4s;border-left:3px solid rgba(255,255,255,.15);padding-left:24px}
.sy-s.on{opacity:1;border-left-color:var(--yel)}
.sy-s:first-child{min-height:42vh;justify-content:flex-start}
.sy-s small{font:700 .9rem var(--display);color:var(--yel)}
.sy-s h3{font:800 clamp(1.5rem,2.6vw,2.2rem)/1.2 var(--display);margin-top:6px}
.sy-s p{color:#D9ECFF;font-size:1.08rem;line-height:1.6;margin-top:10px;max-width:30em}
@media (max-width:900px){.sy-g{grid-template-columns:minmax(0,1fr)}.sy-v{position:sticky;top:60px;z-index:2}.sy-f{position:relative;top:0}.sy-s{min-height:55vh}.sy-s:first-child{min-height:40vh;padding-top:20px}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v37.html','w').write(s)
print('v37 ok')
# Hugh: sort visitors first, open with their problem (storytelling, not a hard sell)
rep('<p class="hq-k">Port Express · คอร์สทำพอร์ตยื่นมหาลัย สำหรับ ม.6</p>','<p class="hq-k">ม.6 ยังไม่มีผลงานไปยื่นพอร์ต? <span>คอร์ส Port Express</span></p>')
i=s.index('<a class="hq-v"');j=s.index('</a>',i)+4
s=s[:j]+'''
  </div>
  <nav class="hq-w" aria-label="เลือกทางที่ตรงกับน้อง"><p>ไม่ใช่ ม.6? เลือกทางที่ตรงกับน้อง</p>
    <a href="#courses" data-scroll=".ct-list"><b>ม.4–5</b>อยากเริ่มเก็บผลงานไว้ก่อน</a>
    <a href="#activity"><b>ทุกชั้น</b>อยากลองค่ายและเวิร์กชอป</a>
    <a href="#courses" data-scroll=".ct-fit"><b>ยังไม่แน่ใจ</b>ตอบ 3 ข้อ ดูคอร์สที่เหมาะ</a>
  </nav><div hidden>'''+s[j:]
# the extra <div hidden> keeps the original closing </div> balanced
rep('/* courses: scrollytelling */',r'''/* links that land on a section of another page */
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-scroll]');if(!a)return;var q=a.dataset.scroll,t0=Date.now();
    (function wait(){var el=document.querySelector('[data-view].on '+q);if(el&&el.offsetParent){setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'start'})},150)}else if(Date.now()-t0<3000)setTimeout(wait,120)})()});
  /* courses: scrollytelling */''')
css2=r'''
.hq-k span{color:#fff;opacity:.6;font-weight:500;margin-left:6px}
.hq-w{max-width:1560px;width:100%;margin:clamp(28px,3vw,44px) auto 0;display:grid;grid-template-columns:auto repeat(3,minmax(0,1fr));gap:10px;align-items:stretch}
.hq-w p{align-self:center;font:700 1rem var(--display);color:#B3D8FF;padding-right:10px}
.hq-w a{display:flex;flex-direction:column;gap:2px;padding:12px 16px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12);color:#fff;text-decoration:none;font-size:.95rem;transition:background .2s,transform .15s}
.hq-w a b{font:800 1.05rem var(--display);color:var(--yel)}
.hq-w a:hover{background:rgba(255,255,255,.12)}.hq-w a:active{transform:scale(.98)}
@media (max-width:900px){.hq-w{grid-template-columns:minmax(0,1fr)}.hq-w p{padding:0}}
'''
s=s.replace('/* ---------- footer ---------- */',css2+'\n/* ---------- footer ---------- */',1)
open('/home/claude/hamsterhub-home/v37.html','w').write(s)
s=s.replace('</nav><div hidden>\n  </div>\n</section>','</nav>\n</section>',1)
assert '<div hidden>\n  </div>' not in s
open('/home/claude/hamsterhub-home/v37.html','w').write(s)
