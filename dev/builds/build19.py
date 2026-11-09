D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build18.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
i=s.index('  <section class="hc"><div class="pc" id="pc"');j=s.index('  <section class="hp-grid">',i)
s=s[:i]+'''  <section class="ov"><div class="ov-c" id="ovc">
    <video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="auto" aria-hidden="true"></video>
    <h1 class="ov-t">คอร์สพาน้อง ม.6<br>ทำพอร์ตยื่นมหาลัย</h1>
    <div class="ov-bub" aria-live="polite"><span class="ov-n" id="ovN">1/4</span><p id="ovS">เรียนทำเกมกับพี่ๆ 2 เดือน</p></div>
    <div class="ov-bar"><p class="ov-p"><b>5,990 บาท</b> <s>9,990</s><span>เริ่ม 9 พ.ย. 2569 · เรียน จ พ ศ</span></p>
      <div class="ov-b"><a class="a1" href="'''+PX+'''" target="_blank" rel="noopener">สมัครเรียน</a><a class="a2" href="#portex">ดูรายละเอียด</a></div></div>
  </div>
  <ol class="ov-m"><li>เรียนทำเกมกับพี่ๆ 2 เดือน</li><li>ได้ผลงานจริงใส่แฟ้มพอร์ต</li><li>ยื่นรอบ Portfolio · รุ่นพี่ติดมหาลัยแล้ว 48 คน</li></ol>
  </section>

'''+s[j:]
i=s.index('  /* hero clip: scenes advance like a video */');j=s.index('  /* router */',i)
s=s[:i]+r'''  /* hero clip: the hamster says the course in four lines */
  (function(){var b=document.querySelector('.ov-bub');if(!b)return;var L=['เรียนทำเกมกับพี่ๆ 2 เดือน','ได้ผลงานจริง ใส่แฟ้มพอร์ต','ยื่นรอบ Portfolio ติดมหาลัย!','รุ่นพี่ติดแล้ว 48 คน ตาน้องบ้าง!'],k=0,S=document.getElementById('ovS'),N=document.getElementById('ovN');
    function go(){S.textContent=L[k];N.textContent=(k+1)+'/'+L.length;b.classList.remove('pop');void b.offsetWidth;b.classList.add('pop');k=(k+1)%L.length}go();setInterval(go,3200)})();
'''+s[j:]
css=r'''
/* ===== v19: the original clip, with the info placed inside it ===== */
.ov{padding:12px 12px 0;background:#fff}
.ov-c{position:relative;width:min(100%,calc((100svh - 84px) * 16 / 9));margin:0 auto;aspect-ratio:16/9;overflow:hidden;container-type:inline-size;background:#1A1460}
.ov-c video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ov-t{position:absolute;left:4.3%;top:63.5%;margin:0;font:800 2.6cqw/1.25 var(--display);color:#fff;text-shadow:.25cqw .25cqw 0 #2A1A6E,0 0 1.2cqw rgba(20,10,60,.6);background:linear-gradient(90deg,rgba(26,20,96,.92),rgba(26,20,96,.6));padding:.6cqw 1.4cqw .7cqw .9cqw;width:max-content;min-width:36cqw}
.ov-bub{position:absolute;left:47%;top:7%;max-width:30cqw;background:#fff;color:#1A1460;padding:1.1cqw 1.6cqw 1.2cqw;font:800 2.2cqw/1.3 var(--display);
  box-shadow:0 -.4cqw 0 #1A1460,0 .4cqw 0 #1A1460,-.4cqw 0 0 #1A1460,.4cqw 0 0 #1A1460,.4cqw .8cqw 0 #E0337E;transform-origin:70% 120%}
.ov-bub::after{content:"";position:absolute;left:62%;bottom:-2.2cqw;width:2cqw;height:2cqw;background:#fff;clip-path:polygon(0 0,100% 0,30% 100%);filter:drop-shadow(.4cqw 0 0 #1A1460)}
.ov-bub p{margin:0}
.ov-n{display:block;font:400 .9cqw var(--pixel);color:#E0337E;margin-bottom:.5cqw}
.ov-bub.pop{animation:bub .45s cubic-bezier(.2,1.6,.4,1)}
@keyframes bub{from{transform:scale(.6);opacity:0}}
.ov-bar{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:space-between;gap:2cqw;padding:2cqw 4cqw 2.2cqw;background:linear-gradient(transparent,rgba(16,10,60,.85) 45%)}
.ov-p{color:#E8EAF8;font:600 1.5cqw var(--display)}.ov-p b{font:800 3.2cqw var(--display);color:#FFD24A}.ov-p s{color:#B7BCE0;margin-left:.6cqw}.ov-p span{display:block;margin-top:.2cqw}
.ov-b{display:flex;gap:1cqw}
.ov-b a{display:inline-flex;align-items:center;min-height:max(44px,3.6cqw);padding:0 max(20px,2cqw);border-radius:999px;font:700 max(15px,1.4cqw) var(--display);text-decoration:none;transition:transform .15s,background .2s}
.ov-b a:hover{transform:translateY(-2px)}
.ov-m{display:none}
@media (max-width:700px){.ov-t{font-size:4cqw}.ov-bub{font-size:3.4cqw;max-width:44cqw;left:40%;top:4%}.ov-n{font-size:1.8cqw}
  .ov-bar{position:static;flex-direction:column;align-items:stretch;background:#1A1460;padding:16px}.ov-c{aspect-ratio:auto}.ov-c video{position:relative;aspect-ratio:16/9;height:auto}
  .ov-p{font-size:.9rem;text-align:center}.ov-p b{font-size:1.6rem}.ov-b{justify-content:center;margin-top:10px}
  .ov-t{top:calc((100vw - 24px) * 9 / 16 * .6)}
  .ov-m{display:grid;gap:8px;list-style:none;margin:0;padding:16px 16px 0;counter-reset:s}.ov-m li{counter-increment:s;font:700 1rem var(--display);display:flex;gap:10px;align-items:center}
  .ov-m li::before{content:counter(s);display:grid;place-items:center;flex:none;width:26px;height:26px;border-radius:50%;background:#7CF29A;font-size:.85rem}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v19.html','w').write(s)
print('v19 ok',len(s))
