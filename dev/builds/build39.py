import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build38.py').read())
def sec(start):
    i=s.index(start);j=s.index('</section>',i)+10;return i,j
# pull out the news tile section, drop hero + paths
i,j=sec('<section class="hp-grid">');NEWS=s[i:j];s=s[:i]+s[j:]
i,j=sec('<section class="hq">');s=s[:i]+'@@FIND@@'+s[j:]
i=s.index('<section class="paths">');j=s.index('</div></section>',i)+16;s=s[:i]+s[j:]
FIND='''<section class="zq" aria-label="ค้นหาคอร์สและกิจกรรม">
    <div class="zq-top">
      <p class="zq-q">น้องอยาก...</p>
      <h1 class="zq-h"><span id="zqType">ยื่นพอร์ตเข้ามหาลัย</span><i class="zq-cur" aria-hidden="true"></i></h1>
      <form class="zq-s" id="zqForm" role="search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="M20 20l-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        <input id="zqIn" type="search" placeholder="พิมพ์สิ่งที่น้องอยากทำ เช่น อยากติดวิศวะคอม หรือ อยากทำเกม" aria-label="ค้นหาคอร์สและกิจกรรม" autocomplete="off"><button type="submit">ค้นหา</button></form>
      <p class="zq-pop"><span>คนค้นหาบ่อย</span><button type="button" data-q="ยื่นพอร์ต">ยื่นพอร์ต</button><button type="button" data-q="สร้างเกม">สร้างเกม</button><button type="button" data-q="AI">AI</button><button type="button" data-q="Python">Python</button><button type="button" data-q="ค่าย">ค่าย</button><button type="button" data-q="แข่งขัน">แข่งขัน</button></p>
    </div>
    <div class="zq-p">
      <div class="zq-t" role="tablist" aria-label="หมวด">
        <button type="button" role="tab" data-t="pop" aria-selected="true"><img src="img/ev-st0.webp" alt="">ยอดนิยม</button>
        <button type="button" role="tab" data-t="course" aria-selected="false"><img src="img/n-grad.webp" alt="">คอร์สเรียน</button>
        <button type="button" role="tab" data-t="ค่าย" aria-selected="false"><img src="img/ev-st2.webp" alt="">ค่าย</button>
        <button type="button" role="tab" data-t="เวิร์กชอป" aria-selected="false"><img src="img/ev-st3.webp" alt="">เวิร์กชอป</button>
        <button type="button" role="tab" data-t="แข่งขัน" aria-selected="false"><img src="img/ev-st4.webp" alt="">แข่งขันและ Game Jam</button>
        <button type="button" role="tab" data-t="โชว์ผลงาน" aria-selected="false"><img src="img/ev-st1.webp" alt="">โชว์ผลงาน</button>
        <button type="button" role="tab" data-t="โครงการ" aria-selected="false"><img src="img/ev-st5.webp" alt="">โครงการ</button>
      </div>
      <p class="zq-r" id="zqR" aria-live="polite"></p>
      <div class="zq-g" id="zqG"></div>
    </div>
  </section>
  <section class="zh"><div class="zh-in">
    <h2>Hamster Hub คือที่สอนเด็กสร้างผลงานจริง</h2>
    <p class="zh-l">เราสอนทำเกม เว็บ และ IoT ให้น้อง ม.ปลาย มีทั้งคอร์สยาว ค่ายสั้น และงานแข่งขัน จบแล้วน้องมีผลงานของตัวเองไว้ยื่นมหาลัยหรือต่อยอดได้</p>
    <ul class="zh-n"><li><b>48 คน</b>รุ่นพี่ DEK69 ติดมหาลัยรอบ Portfolio</li><li><b>ชนะเลิศ</b>OBEC Roboplayground ด้วยเกม StressStrike</li><li><b>12 ผลงาน</b>เข้ารอบชิงชนะเลิศ NSC</li></ul>
    <div class="zh-a">
      <div><h3>น้องที่อยากติดมหาลัย</h3><p>ทำผลงานจริงเข้าแฟ้มพอร์ต ซ้อมเล่าผลงานและตอบคำถามกรรมการ</p><a href="#" data-q="ยื่นพอร์ต">ดูคอร์สทำพอร์ต</a></div>
      <div><h3>น้องที่อยากมีผลงานของตัวเอง</h3><p>เริ่มจากศูนย์ได้ สร้างเกมหรือเว็บที่เล่นได้จริง แล้วเอาไปลงแข่ง</p><a href="#" data-q="สร้างเกม">ดูคอร์สและค่ายสร้างเกม</a></div>
      <div><h3>ผู้ปกครอง</h3><p>เห็นผลงานของลูกได้จริงทุกชิ้น ถามรายละเอียดคอร์ส ราคา และวันเรียนกับทีมได้ทาง LINE</p><a href="https://page.line.me/jkm4247u?openQrModal=true" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div>
    </div>
  </div></section>
  '''
s=s.replace('@@FIND@@',FIND)
# news after seniors
i=s.index('<section class="end">');s=s[:i]+NEWS.replace('<section class="hp-grid">','<section class="hp-grid nw2"><h2 class="nw2-h">ข่าวและกิจกรรมล่าสุด</h2>')+'\n  '+s[i:]
JS=r'''
  /* home: find (search + tabs + cards) */
  (function(){var G2=$('#zqG');if(!G2)return;var PX='https://www.hamsterhub.co/portex-site/index.html';
    var CRS=[['Port Express','คอร์สทำพอร์ตยื่นมหาลัย 2 เดือน สร้างเกมด้วย Unity','เปิดรับ เริ่ม 9 พ.ย. 2569','5,990 บาท','img/portex-poster.webp',PX,'พอร์ต มหาลัย ยื่น ม.6 dek69 dek70 เกม unity สัมภาษณ์ กรรมการ วิศวะ คอม'],
      ['Port70','คอร์สทำพอร์ตสำหรับน้อง DEK70','รอบถัดไป','','','','พอร์ต มหาลัย ม.5 dek70'],['Project Express','ทำโปรเจกต์ให้เสร็จไวเพื่อยื่นพอร์ต','รอบถัดไป','','','','พอร์ต โปรเจกต์ มหาลัย'],
      ['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ','รอบถัดไป','','','','แข่งขัน nsc ระดับประเทศ โปรเจกต์'],['Business Project','ทำโปรเจกต์ที่ต่อยอดเป็นธุรกิจ','รอบถัดไป','','','','ธุรกิจ สตาร์ทอัพ ขาย'],
      ['Python Pro Pack','เรียนเขียนโปรแกรมด้วย Python','รอบถัดไป','','','','python เขียนโปรแกรม โค้ด'],['Hamstarter','คอร์สเริ่มต้นสำหรับคนที่ยังไม่มีผลงาน','รอบถัดไป','','','','เริ่มต้น มือใหม่ ไม่เคย เกม']];
    var DIMG={'ค่าย':'photo-camp','เวิร์กชอป':'photo-class','แข่งขัน':'k-gamejam','โชว์ผลงาน':'s-showcase1','โครงการ':'photo-group'},
      AI2={'All for One University รอบชิงชนะเลิศ':'k-afo','IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'};
    var IT=CRS.map(function(c){var g=G.filter(function(x){return x[4]===c[0]})[0];return {k:'course',t:c[0],d:c[1],st:c[2],pr:c[3],img:c[4]||(g?'img/dek69-'+g[0]+'.webp':'img/photo-class.webp'),url:c[5]||LINE,open:!!c[5],tags:c[6]}});
    ACT.forEach(function(a){IT.push({k:a[3],t:a[1],d:a[2],st:a[4]?'กำลังจะมา '+a[0]:'จบแล้ว '+a[0],pr:'',img:'img/'+(AI2[a[1]]||DIMG[a[3]])+'.webp',url:a[4]?'https://www.hamsterhub.co/allforone':LINE,open:!!a[4],tags:a[3]+' '+a[2]})});
    var POP=['Port Express','All for One University รอบชิงชนะเลิศ','Hamstarter','AI Camp Season 2','GameJam X ปีที่ 5','Port70','Python Pro Pack','NSC Software Project 2026'];
    var SYN={'มหาลัย':'พอร์ต','มหาวิทยาลัย':'พอร์ต','tcas':'พอร์ต','portfolio':'พอร์ต','วิศวะ':'พอร์ต','คอม':'พอร์ต','สัมภาษณ์':'พอร์ต','game':'เกม','roblox':'เกม','unity':'เกม','เอไอ':'ai','โค้ด':'python','เขียนโปรแกรม':'python','แข่ง':'แข่งขัน','jam':'แข่งขัน','เว็บ':'web','web':'เว็บ'};
    function lab(x){return x.k==='course'?'คอร์สเรียน':'กิจกรรม: '+x.k}
    function cardH(x){var cta=x.k==='course'?(x.open?'ดูรายละเอียดและสมัคร':'รับแจ้งเตือนรอบใหม่'):(x.open?'ดูรายละเอียดงาน':'รับแจ้งเตือนงานหน้า');
      return '<a class="zk'+(x.open?' on':'')+'" href="'+x.url+'" target="_blank" rel="noopener"><span class="zk-i"><img src="'+x.img+'" alt="" loading="lazy"></span><span class="zk-b"><span class="zk-k'+(x.k==='course'?' c':'')+'">'+lab(x)+'</span><b>'+x.t+'</b><span class="zk-d">'+x.d+'</span><span class="zk-s">'+x.st+(x.pr?'<em>'+x.pr+'</em>':'')+'</span><span class="zk-a">'+cta+'</span></span></a>'}
    function render(list,msg){$('#zqR').innerHTML=msg||'';G2.innerHTML=list.length?list.map(cardH).join(''):'<div class="zq-e"><b>ยังไม่มีคอร์สหรือกิจกรรมที่ตรงกับคำนี้</b><p>บอกทีมได้ว่าน้องอยากทำอะไร ทีมช่วยแนะนำให้</p><a href="'+LINE+'" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div>'}
    function tab(t){$$('.zq-t button').forEach(function(b){b.setAttribute('aria-selected',String(b.dataset.t===t))});
      var L=t==='pop'?POP.map(function(n){return IT.filter(function(x){return x.t===n})[0]}).filter(Boolean):IT.filter(function(x){return x.k===t});render(L)}
    function search(q){q=(q||'').trim();if(!q){tab('pop');return}var toks=q.toLowerCase().split(/\s+/),k=[];toks.forEach(function(w){k.push(w);Object.keys(SYN).forEach(function(s2){if(w.indexOf(s2)>-1)k.push(SYN[s2])})});
      var L=IT.filter(function(x){var h=(x.t+' '+x.d+' '+x.tags+' '+x.k).toLowerCase();return k.some(function(w){return w.length>1&&h.indexOf(w)>-1})});
      L.sort(function(a,b){return (b.open?2:0)+(b.k==='course'?1:0)-((a.open?2:0)+(a.k==='course'?1:0))});
      $$('.zq-t button').forEach(function(b){b.setAttribute('aria-selected','false')});render(L,'ผลลัพธ์สำหรับ “'+q.replace(/[<>&]/g,'')+'” '+L.length+' รายการ')}
    $$('.zq-t button').forEach(function(b){b.addEventListener('click',function(){$('#zqIn').value='';tab(b.dataset.t)})});
    $('#zqForm').addEventListener('submit',function(e){e.preventDefault();search($('#zqIn').value)});
    var dt;$('#zqIn').addEventListener('input',function(){clearTimeout(dt);dt=setTimeout(function(){search($('#zqIn').value)},250)});
    document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-q]');if(!b)return;e.preventDefault();$('#zqIn').value=b.dataset.q;search(b.dataset.q);$('.zq').scrollIntoView({behavior:'smooth'})});
    tab('pop');
    var W2=['ยื่นพอร์ตเข้ามหาลัย','สร้างเกมของตัวเอง','เรียน AI','เขียน Python','ลงแข่ง Game Jam'],wi=0,ci=W2[0].length,del=true,el=$('#zqType');
    if(!matchMedia('(prefers-reduced-motion:reduce)').matches)(function ty(){var w=W2[wi];if(del){ci--;if(ci<=0){del=false;wi=(wi+1)%W2.length}}else{ci++;if(ci>=W2[wi].length){del=true;el.textContent=W2[wi];setTimeout(ty,2200);return}}el.textContent=W2[wi].slice(0,Math.max(ci,0));setTimeout(ty,del?40:85)})();
  })();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v39: find-first home ===== */
.nav{background:rgba(255,255,255,.72)!important;-webkit-backdrop-filter:saturate(180%) blur(20px);backdrop-filter:saturate(180%) blur(20px)}
.zq{background:#F2F5FA;padding:clamp(48px,6vw,88px) 16px clamp(40px,5vw,72px)}
.zq-top{text-align:center;max-width:820px;margin:0 auto}
.zq-q{font:600 1.35rem var(--display);color:#4A5874}
.zq-h{font:800 clamp(2.4rem,5.4vw,4.4rem)/1.15 var(--display);color:#0D2E63;letter-spacing:-.02em;margin-top:6px;min-height:1.2em}
.zq-cur{display:inline-block;width:3px;height:.9em;background:#1C74D9;margin-left:6px;vertical-align:-.08em;animation:zqB 1s steps(1) infinite}
@keyframes zqB{50%{opacity:0}}
.zq-s{display:flex;align-items:center;gap:10px;margin:28px auto 0;max-width:720px;background:#fff;border-radius:999px;padding:8px 8px 8px 22px;box-shadow:0 1px 0 rgba(13,46,99,.06),0 12px 32px -12px rgba(13,46,99,.25);border:1px solid #DCE4F0}
.zq-s:focus-within{border-color:#1C74D9;box-shadow:0 0 0 4px rgba(28,116,217,.15),0 12px 32px -12px rgba(13,46,99,.25)}
.zq-s svg{width:22px;height:22px;color:#6B7A94;flex:none}
.zq-s input{flex:1;min-width:0;border:0;outline:0;font:500 1.05rem var(--body);color:#10213F;background:none;padding:10px 0}
.zq-s button{border:0;border-radius:999px;background:#1C74D9;color:#fff;font:700 1rem var(--display);padding:12px 24px;cursor:pointer}
.zq-s button:hover{background:#155FB5}
.zq-pop{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:8px;margin-top:18px;font-size:.92rem;color:#6B7A94}
.zq-pop span{margin-right:4px}
.zq-pop button{border:1px solid #DCE4F0;background:#fff;border-radius:999px;padding:6px 14px;font:600 .92rem var(--display);color:#0D2E63;cursor:pointer}
.zq-pop button:hover{border-color:#1C74D9;color:#1C74D9}
.zq-p{max-width:1240px;margin:clamp(36px,4vw,56px) auto 0;background:#fff;border-radius:28px;padding:24px clamp(16px,2.4vw,32px) 32px;box-shadow:0 20px 50px -30px rgba(13,46,99,.35)}
.zq-t{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;border-bottom:1px solid #E6ECF4;padding-bottom:2px}
.zq-t::-webkit-scrollbar{display:none}
.zq-t button{flex:1 0 auto;min-width:112px;display:flex;flex-direction:column;align-items:center;gap:8px;border:0;background:none;cursor:pointer;padding:6px 10px 14px;font:600 .95rem var(--display);color:#4A5874;border-bottom:3px solid transparent;margin-bottom:-3px;transition:color .2s}
.zq-t img{width:64px;height:64px;object-fit:contain;transition:transform .25s cubic-bezier(.3,1.5,.5,1)}
.zq-t button:hover img{transform:translateY(-4px)}
.zq-t button[aria-selected="true"]{color:#0D2E63;border-bottom-color:#1C74D9}
.zq-r{margin:18px 2px 0;color:#4A5874;font-weight:600;min-height:1px}
.zq-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:16px}
.zk{display:flex;flex-direction:column;border-radius:18px;overflow:hidden;background:#fff;border:1px solid #E6ECF4;text-decoration:none;color:#10213F;transition:transform .2s,box-shadow .2s}
.zk:hover{transform:translateY(-3px);box-shadow:0 18px 30px -18px rgba(13,46,99,.45)}
.zk-i{display:block;aspect-ratio:16/10;background:#EEF3FA;overflow:hidden}.zk-i img{width:100%;height:100%;object-fit:cover}
.zk-b{display:flex;flex-direction:column;gap:4px;padding:14px 16px 16px;flex:1}
.zk-k{align-self:flex-start;font:700 .78rem var(--display);color:#5B3FD6;background:#EEE8FF;padding:3px 10px;border-radius:999px}
.zk-k.c{color:#155FB5;background:#E3F0FF}
.zk-b b{font:700 1.08rem/1.3 var(--display);margin-top:4px}
.zk-d{font-size:.9rem;color:#4A5874;line-height:1.45}
.zk-s{margin-top:auto;padding-top:8px;font-size:.85rem;color:#6B7A94;display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.zk.on .zk-s{color:#16803C;font-weight:600}
.zk-s em{font-style:normal;font:800 1.15rem var(--display);color:#0D2E63}
.zk-a{margin-top:10px;font:700 .92rem var(--display);color:#1C74D9}
.zk.on .zk-a{background:#FFC531;color:#2A1E00;text-align:center;padding:9px;border-radius:12px}
.zq-e{grid-column:1/-1;text-align:center;padding:40px 16px}.zq-e p{color:#4A5874;margin:6px 0 16px}
.zq-e a{display:inline-block;background:#06C755;color:#fff;font:700 1rem var(--display);padding:12px 22px;border-radius:999px;text-decoration:none}
.zh{padding:clamp(64px,7vw,104px) 16px;background:#fff}
.zh-in{max-width:1080px;margin:0 auto}
.zh h2{font:800 clamp(2rem,4vw,3.2rem)/1.15 var(--display);color:#0D2E63;max-width:16em}
.zh-l{font-size:1.15rem;line-height:1.65;color:#4A5874;margin-top:16px;max-width:40em}
.zh-n{list-style:none;padding:0;margin:40px 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;border-top:1px solid #E6ECF4;padding-top:28px}
.zh-n li{color:#4A5874;font-size:.98rem}.zh-n b{display:block;font:800 clamp(1.8rem,3vw,2.4rem)/1.1 var(--display);color:#1C74D9;margin-bottom:6px}
.zh-a{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:48px}
.zh-a>div{background:#F2F5FA;border-radius:20px;padding:24px}
.zh-a h3{font:700 1.2rem var(--display);color:#0D2E63}.zh-a p{color:#4A5874;margin:8px 0 14px;line-height:1.55}
.zh-a a{font:700 1rem var(--display);color:#1C74D9;text-decoration:none}.zh-a a:hover{text-decoration:underline}
.nw2{padding-top:56px!important}.nw2-h{max-width:1240px;margin:0 auto 20px;padding:0 24px;font:800 clamp(1.8rem,3vw,2.4rem) var(--display);color:#0D2E63}
@media (max-width:1000px){.zq-g{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:700px){.zq-g,.zh-n,.zh-a{grid-template-columns:minmax(0,1fr)}.zq-s button{padding:10px 16px}.zq-t img{width:52px;height:52px}.zq-t button{min-width:92px;font-size:.85rem}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v39.html','w').write(s)
print('v39 ok')
s=s.replace("'All for One University รอบชิงชนะเลิศ':'k-afo','IoTE","'All for One University รอบชิงชนะเลิศ':'k-afo-logo','IoTE",1)
s=s.replace('/* ---------- footer ---------- */',r'''.zk-i img[src*="afo-logo"]{object-fit:contain;padding:12px;background:#1C74D9}
@media (max-width:700px){.zk{flex-direction:row}.zk-i{width:112px;flex:none;aspect-ratio:auto}.zk-b{padding:12px 14px}.zk-d{display:none}.zk-b b{font-size:1rem}.zk.on .zk-a{padding:7px}}
/* ---------- footer ---------- */''',1)
open('/home/claude/hamsterhub-home/v39.html','w').write(s)
