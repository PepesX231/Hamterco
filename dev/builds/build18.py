D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build17.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
# ---------- HERO: a pixel-art clip that tells the whole course ----------
i=s.index('  <section class="hc">');j=s.index('  <section class="hp-grid">',i)
s=s[:i]+'''  <section class="hc"><div class="pc" id="pc" data-s="0" role="region" aria-label="Port Express คอร์สพาน้อง ม.6 ทำพอร์ตยื่นมหาลัย เรียนทำเกมกับพี่ๆ 2 เดือน ได้ผลงานจริงใส่แฟ้มพอร์ต รุ่นพี่ติดมหาลัยแล้ว 48 คน เริ่ม 9 พ.ย. 2569 ราคา 5,990 บาท">
    <span class="pc-sky" aria-hidden="true"></span><span class="pc-tw" aria-hidden="true"></span>
    <span class="pc-ln" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>
    <p class="pc-mini" aria-hidden="true">PORT EXPRESS</p>
    <div class="ps s0 on"><p class="pc-big">PORT<br>EXPRESS</p><p class="pc-h">คอร์สพาน้อง ม.6<br>ทำพอร์ตยื่นมหาลัย</p></div>
    <div class="ps s1"><p class="pc-k">ขั้นที่ 1</p><p class="pc-h">เรียนทำเกม<br>กับพี่ๆ 2 เดือน</p><p class="pc-s">จันทร์ พุธ ศุกร์ · ไม่เคยทำมาก่อนก็เริ่มได้</p>
      <div class="pc-v gm"><img src="img/work-phi-krahang.webp" alt=""><img src="img/work-stressstrike.webp" alt=""><img src="img/work-midnight-at-roadside.webp" alt=""></div></div>
    <div class="ps s2"><p class="pc-k">ขั้นที่ 2</p><p class="pc-h">ได้ผลงานจริง<br>ใส่แฟ้มพอร์ต</p><p class="pc-s">พร้อมสไลด์เล่าผลงาน และซ้อมสัมภาษณ์กับอาจารย์มหาลัย</p>
      <div class="pc-v fdx"><span class="tb">PORTFOLIO</span><i></i><i></i><i></i><em>READY!</em></div></div>
    <div class="ps s3"><p class="pc-k">ขั้นที่ 3</p><p class="pc-h">ยื่นรอบ Portfolio<br>รุ่นพี่ติดมหาลัยแล้ว 48 คน</p><p class="pc-s">สจล. · จุฬาฯ · มหิดล · เกษตรศาสตร์</p>
      <div class="pc-v pst"><img src="img/dek69-13.webp" alt=""><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""><img src="img/dek69-11.webp" alt=""></div></div>
    <div class="ps s4"><p class="pc-k">รุ่นใหม่</p><p class="pc-h">เริ่ม 9 พ.ย. 2569</p><p class="pc-pr"><b>5,990 บาท</b> <s>ปกติ 9,990</s></p><p class="pc-s">เรียน 2 เดือน · จันทร์ พุธ ศุกร์</p></div>
    <img class="pc-ham" src="img/px-astro.webp" alt="">
    <div class="pc-bar">
      <div class="pc-pip" role="tablist" aria-label="เลือกฉาก"><button type="button" aria-label="ฉาก 1"></button><button type="button" aria-label="ฉาก 2"></button><button type="button" aria-label="ฉาก 3"></button><button type="button" aria-label="ฉาก 4"></button><button type="button" aria-label="ฉาก 5"></button></div>
      <p class="pc-p"><b>5,990 บาท</b> · เริ่ม 9 พ.ย.</p>
      <div class="pc-b"><a class="a1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="a2" href="#portex">ดูรายละเอียด</a></div>
    </div>
  </div></section>

'''+s[j:]
rep("  /* router */",r'''  /* hero clip: scenes advance like a video */
  (function(){var pc=document.getElementById('pc');if(!pc)return;var sc=pc.querySelectorAll('.ps'),pp=pc.querySelectorAll('.pc-pip button'),i=0,t=0,D=4200;
    function go(k){i=(k+sc.length)%sc.length;pc.dataset.s=i;sc.forEach(function(e,n){e.classList.toggle('on',n===i)});pp.forEach(function(b,n){b.classList.toggle('on',n===i);b.classList.remove('run');if(n===i){void b.offsetWidth;b.classList.add('run')}});clearTimeout(t);t=setTimeout(function(){go(i+1)},D)}
    pp.forEach(function(b,n){b.addEventListener('click',function(){go(n)})});
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){pc.classList.add('still')}
    go(0)})();
  /* router */''')
# ---------- NEWS: say it is news ----------
rep('<section class="hp-grid"><div class="wrap hg st">','<section class="hp-grid"><div class="nw-h"><span class="nw-b">ข่าวสาร</span><h2>อัปเดตล่าสุดจาก Hamster Hub</h2></div><div class="wrap hg st">')
rep('<p class="t-k" id="afoTag">ข่าวสาร · กิจกรรมถัดไป</p>','<p class="t-k"><span class="nw-new">ข่าวใหม่</span></p><p class="t-k" id="afoTag">กิจกรรมถัดไป · 14 พ.ย. 2569</p>')
# ---------- HALL OF FAME tile ----------
i=s.index('    <a class="tile t-wk rv" href="#works">');j=s.index('</a>',i)+4
FR=[('work-stressstrike','StressStrike'),('work-phi-krahang','ผีกระหัง'),('work-eugation-strike','Eugation Strike'),('work-slash-speed','SLASH//SPEED'),('work-escape-rolling','Escape Rolling')]
s=s[:i]+'''    <a class="tile hof2 rv" href="#works" data-pane="hof">
      <span class="hf-sp" aria-hidden="true"></span>
      <p class="hf-k">ผลงานเด่นของน้องๆ ปี 2569</p>
      <h3 class="hf-t">HALL OF FAME</h3>
      <div class="hf-row">'''+''.join('<figure><img src="img/%s.webp" alt="" loading="lazy"><figcaption>%s</figcaption></figure>'%f for f in FR)+'''</div>
      <span class="hf-b">ดูผลงานทั้งหมด</span>
      <img class="hf-tr" src="img/n-win.webp" alt="">
    </a>'''+s[j:]
css=r'''
/* ===== v18: hero pixel clip ===== */
.pc{position:relative;overflow:hidden;container-type:inline-size;aspect-ratio:16/8;min-height:520px;max-height:calc(100svh - 84px);width:100%;color:#fff;background:#120A3A;font-family:var(--display)}
.pc-sky{position:absolute;inset:-4%;background:url(img/px-sky.webp) 50% 50%/cover;image-rendering:pixelated;animation:sky 40s ease-in-out infinite alternate}
@keyframes sky{to{transform:translate(-2%,1%) scale(1.04)}}
.pc-tw{position:absolute;inset:0;background-image:radial-gradient(#fff 1.2px,transparent 1.8px),radial-gradient(#9FE7FF 1.2px,transparent 1.8px);background-size:11cqw 11cqw,17cqw 17cqw;background-position:2cqw 3cqw,8cqw 9cqw;animation:tw 2.4s steps(2) infinite;opacity:.6}
@keyframes tw{50%{opacity:.15}}
.pc-ln i{position:absolute;right:-20%;height:.35cqw;width:14cqw;background:linear-gradient(90deg,transparent,#9FE7FF);animation:ln 1.6s linear infinite;opacity:.7}
.pc-ln i:nth-child(1){top:30%;animation-delay:-.2s}.pc-ln i:nth-child(2){top:44%;animation-delay:-.9s;width:9cqw}.pc-ln i:nth-child(3){top:58%;animation-delay:-.5s}.pc-ln i:nth-child(4){top:70%;animation-delay:-1.3s;width:11cqw}.pc-ln i:nth-child(5){top:20%;animation-delay:-1.1s;width:7cqw}
@keyframes ln{from{transform:translateX(0)}to{transform:translateX(-140cqw)}}
.pc-mini{position:absolute;left:4cqw;top:3.2cqw;z-index:3;font:400 1.3cqw var(--pixel);color:#FFD24A;text-shadow:.2cqw .2cqw 0 #E0337E;opacity:0;transition:opacity .5s}
.pc:not([data-s="0"]) .pc-mini{opacity:1}
.ps{position:absolute;left:4cqw;top:0;bottom:9cqw;width:46cqw;z-index:3;display:flex;flex-direction:column;justify-content:center;pointer-events:none}
.ps>*{opacity:0;transform:translateY(2.4cqw);transition:opacity .5s,transform .6s cubic-bezier(.2,.8,.2,1)}
.ps.on>*{opacity:1;transform:none}
.ps.on>*:nth-child(2){transition-delay:.12s}.ps.on>*:nth-child(3){transition-delay:.24s}.ps.on>*:nth-child(4){transition-delay:.36s}
.pc-big{font:400 7.4cqw/1.08 var(--pixel);color:#FFD24A;text-shadow:.6cqw .6cqw 0 #E0337E,0 0 3cqw rgba(255,210,74,.35)}
.pc-h{font:800 4.2cqw/1.2 var(--display);letter-spacing:-.02em;text-shadow:0 .3cqw 1.4cqw rgba(0,0,0,.45)}
.s0 .pc-h{font-size:3.4cqw;margin-top:2cqw}
.pc-k{display:inline-block;align-self:flex-start;font:700 1.4cqw var(--display);color:#0B0720;background:#7CF29A;padding:.4cqw 1.2cqw;border-radius:99px;margin-bottom:1.6cqw}
.pc-s{font:600 1.6cqw/1.45 var(--display);color:#D9DCF3;margin-top:1.4cqw}
.pc-pr{margin-top:1.4cqw}.pc-pr b{font:800 5cqw var(--display);color:#FFD24A}.pc-pr s{font-size:1.8cqw;color:#9AA0C8;margin-left:1cqw}
.pc-v{position:absolute;left:52cqw;top:50%;transform:translateY(-50%)}
.ps.on .pc-v{transform:translateY(-50%)}
.gm{width:34cqw;height:24cqw}
.gm img{position:absolute;width:20cqw;aspect-ratio:16/10;object-fit:cover;border:.5cqw solid #fff;box-shadow:.7cqw .7cqw 0 #E0337E;transition:transform .9s cubic-bezier(.2,1.2,.4,1)}
.gm img:nth-child(1){left:0;top:12cqw;transform:translateX(40cqw) rotate(-6deg)}.gm img:nth-child(2){left:7cqw;top:6cqw;transform:translateX(40cqw) rotate(3deg)}.gm img:nth-child(3){left:14cqw;top:0;transform:translateX(40cqw) rotate(-2deg)}
.s1.on .gm img:nth-child(1){transform:rotate(-6deg);transition-delay:.2s}.s1.on .gm img:nth-child(2){transform:rotate(3deg);transition-delay:.35s}.s1.on .gm img:nth-child(3){transform:rotate(-2deg);transition-delay:.5s}
.fdx{left:58cqw;width:20cqw;height:22cqw}
.fdx::before{content:"";position:absolute;inset:2.4cqw 0 0;background:#FFB81C;box-shadow:inset 0 -1cqw 0 #C28A00,.7cqw .7cqw 0 #E0337E}
.fdx .tb{position:absolute;left:0;top:0;height:2.6cqw;padding:0 1.4cqw;background:#FFB81C;font:400 1.1cqw/2.8cqw var(--pixel);color:#5A3A00}
.fdx i{position:absolute;left:2cqw;right:2cqw;height:4.4cqw;background:#fff;opacity:0;transform:translateY(-6cqw);transition:all .5s cubic-bezier(.2,1.4,.4,1)}
.fdx i:nth-of-type(1){top:5cqw}.fdx i:nth-of-type(2){top:10.6cqw}.fdx i:nth-of-type(3){top:16.2cqw}
.s2.on .fdx i{opacity:1;transform:none}.s2.on .fdx i:nth-of-type(1){transition-delay:.3s}.s2.on .fdx i:nth-of-type(2){transition-delay:.55s}.s2.on .fdx i:nth-of-type(3){transition-delay:.8s}
.fdx i::before{content:"";position:absolute;left:.7cqw;top:.7cqw;bottom:.7cqw;width:5cqw;background:#5B3FD6}.fdx i:nth-of-type(2)::before{background:#1068DC}.fdx i:nth-of-type(3)::before{background:#2E9E6B}
.fdx i::after{content:"";position:absolute;left:6.6cqw;right:1.2cqw;top:1.2cqw;height:.7cqw;background:#E3DAC4;box-shadow:0 1.3cqw 0 #E3DAC4}
.fdx em{position:absolute;right:-4cqw;bottom:1.4cqw;font:400 1.8cqw var(--pixel);font-style:normal;color:#E0337E;border:.45cqw solid #E0337E;background:#fff;padding:.6cqw .9cqw;opacity:0;transform:rotate(-12deg) scale(2.4);transition:all .4s cubic-bezier(.2,1.6,.4,1) 1.2s}
.s2.on .fdx em{opacity:1;transform:rotate(-12deg)}
.pst{width:36cqw;height:22cqw}
.pst img{position:absolute;top:2cqw;width:12cqw;aspect-ratio:4/5;object-fit:cover;border:.45cqw solid #fff;box-shadow:.6cqw .6cqw 0 #E0337E;opacity:0;transition:all .6s cubic-bezier(.2,1.3,.4,1)}
.pst img:nth-child(1){left:0;transform:rotate(-12deg) translateY(6cqw)}.pst img:nth-child(2){left:8cqw;top:0;transform:rotate(-4deg) translateY(6cqw)}.pst img:nth-child(3){left:16cqw;top:0;transform:rotate(4deg) translateY(6cqw)}.pst img:nth-child(4){left:24cqw;transform:rotate(12deg) translateY(6cqw)}
.s3.on .pst img{opacity:1}.s3.on .pst img:nth-child(1){transform:rotate(-12deg);transition-delay:.2s}.s3.on .pst img:nth-child(2){transform:rotate(-4deg);transition-delay:.32s}.s3.on .pst img:nth-child(3){transform:rotate(4deg);transition-delay:.44s}.s3.on .pst img:nth-child(4){transform:rotate(12deg);transition-delay:.56s}
.pc-ham{position:absolute;z-index:2;width:30cqw;right:6cqw;top:12%;filter:drop-shadow(0 1.4cqw 1.4cqw rgba(0,0,0,.35));transition:all 1.1s cubic-bezier(.5,0,.2,1);animation:bob 2.6s ease-in-out infinite}
@keyframes bob{50%{translate:0 -1.6cqw}}
.pc:not([data-s="0"]):not([data-s="4"]) .pc-ham{width:15cqw;right:2cqw;top:4%}
.pc[data-s="4"] .pc-ham{right:12cqw;top:16%;width:28cqw}
.pc-bar{position:absolute;left:0;right:0;bottom:0;z-index:4;display:flex;align-items:center;gap:2cqw;padding:1.6cqw 4cqw;background:linear-gradient(transparent,rgba(8,6,30,.85))}
.pc-pip{display:flex;gap:.8cqw;margin-right:auto}
.pc-pip button{position:relative;width:4cqw;min-width:28px;height:6px;border:0;padding:0;background:rgba(255,255,255,.28);cursor:pointer;overflow:hidden}
.pc-pip button.on::after{content:"";position:absolute;inset:0;background:#FFD24A;transform-origin:left;transform:scaleX(0)}
.pc-pip button.run::after{animation:pip 4.2s linear forwards}
@keyframes pip{to{transform:scaleX(1)}}
.pc-p{font:600 clamp(.9rem,1.3cqw,1.1rem) var(--display);color:#D9DCF3}.pc-p b{color:#FFD24A}
.pc-b{display:flex;gap:10px}
.pc-b a{display:inline-flex;align-items:center;min-height:48px;padding:0 24px;border-radius:999px;font:700 1rem var(--display);text-decoration:none;transition:transform .15s,background .2s}
.pc-b a:hover{transform:translateY(-2px)}
.pc.still .ps,.pc.still .ps>*{transition:none}
@container (max-width:700px){
  .ps{left:5cqw;right:5cqw;width:auto;top:24cqw;bottom:auto;justify-content:flex-start}
  .pc-big{font-size:12cqw}.pc-h{font-size:7.4cqw}.s0 .pc-h{font-size:6.6cqw}.pc-k{font-size:3.4cqw}.pc-s{font-size:3.6cqw}.pc-pr b{font-size:9cqw}.pc-pr s{font-size:3.6cqw}
  .pc-mini{font-size:3cqw}
  .pc-v{left:50%;top:auto;bottom:-70cqw;transform:translateX(-50%)!important}
  .gm{width:66cqw;height:46cqw}.gm img{width:40cqw}.gm img:nth-child(2){left:13cqw;top:10cqw}.gm img:nth-child(1){top:22cqw}.gm img:nth-child(3){left:26cqw}
  .fdx{width:40cqw;height:44cqw;left:50%;bottom:-74cqw}
  .pst{width:76cqw;height:44cqw}.pst img{width:24cqw}.pst img:nth-child(2){left:16cqw}.pst img:nth-child(3){left:32cqw}.pst img:nth-child(4){left:48cqw}
  .pc-ham,.pc[data-s="4"] .pc-ham{width:56cqw;right:20cqw;top:auto;bottom:34cqw}
  .pc:not([data-s="0"]):not([data-s="4"]) .pc-ham{width:30cqw;right:4cqw;top:auto;bottom:40cqw}
  .pc-bar{flex-wrap:wrap;justify-content:center;padding:4cqw}.pc-pip{width:100%;justify-content:center;margin:0 0 1cqw}.pc-pip button{width:10cqw}
}
@media (max-width:700px){.pc{aspect-ratio:auto;height:max(680px,calc(100svh - 84px));max-height:none}}
/* NEWS heading */
.nw-h{max-width:1120px;margin:0 auto;padding:clamp(48px,6vw,80px) var(--gl) 20px}
.nw-b{display:inline-block;font:800 .95rem var(--display);color:#fff;background:#E0337E;padding:5px 14px;border-radius:999px}
.nw-h h2{font:800 clamp(2rem,4vw,3rem)/1.15 var(--display);letter-spacing:-.02em;margin-top:10px}
.nw-new{display:inline-block;color:#0B1640;background:#FFD24A;padding:3px 12px;border-radius:999px;font-weight:800;animation:kp2 1.6s ease-in-out infinite}
@keyframes kp2{50%{box-shadow:0 0 0 6px rgba(255,210,74,.3)}}
/* HALL OF FAME tile */
.hg.st .tile.hof2{display:block!important;text-align:center;background:radial-gradient(60% 70% at 50% 0%,#3A2A08 0%,#0B0906 70%);color:#fff;min-height:clamp(560px,48vw,680px)!important;overflow:hidden}
.hf-sp{position:absolute;left:50%;top:-10%;width:70%;height:90%;transform:translateX(-50%);background:conic-gradient(from 160deg at 50% 0,transparent 0,rgba(255,226,150,.22) 14deg,rgba(255,226,150,.22) 26deg,transparent 40deg);pointer-events:none}
.hf-k{position:relative;font:700 1.05rem var(--display);color:#E8C877}
.hf-t{position:relative;font:900 clamp(3.4rem,10vw,8.4rem)/1 var(--display)!important;letter-spacing:.02em;margin-top:10px!important;background:linear-gradient(100deg,#8A6A1E 0%,#F6DF9A 25%,#FFF6D6 35%,#C9A04A 50%,#F6DF9A 70%,#8A6A1E 100%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:hfS 5s linear infinite;filter:drop-shadow(0 8px 30px rgba(255,200,90,.3))}
@keyframes hfS{from{background-position:120% 0}to{background-position:-130% 0}}
.hf-row{position:relative;display:flex;justify-content:center;gap:clamp(10px,1.6vw,22px);margin-top:clamp(28px,4vw,48px);flex-wrap:wrap}
.hf-row figure{margin:0;width:clamp(150px,15vw,210px);padding:8px 8px 0;background:linear-gradient(145deg,#F6DF9A,#8A6A1E 50%,#E8C877);box-shadow:0 20px 40px -18px rgba(0,0,0,.8);transition:transform .35s cubic-bezier(.3,1.5,.5,1)}
.hf-row figure:nth-child(odd){transform:translateY(14px)}
.hof2:hover .hf-row figure{transform:translateY(-6px)}
.hf-row img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border:3px solid #1A1206}
.hf-row figcaption{font:700 .85rem var(--display);color:#2A1C04;padding:6px 0 7px}
.hf-b{position:relative;display:inline-block;margin-top:clamp(28px,4vw,40px);font:700 1.05rem var(--display);color:#1A1206;background:linear-gradient(90deg,#E8C877,#FFF1C2,#E8C877);padding:13px 28px;border-radius:999px}
.hf-tr{position:absolute;right:clamp(10px,4vw,60px);bottom:-8px;width:clamp(90px,10vw,140px)}
@media (max-width:700px){.hf-row figure:nth-child(n+4){display:none}.hf-row figure{width:28vw}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v18.html','w').write(s)
print('v18 ok',len(s))
