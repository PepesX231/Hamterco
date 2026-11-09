D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build24.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
EXT='href="'+PX+'" target="_blank" rel="noopener"'
# ---- remove the Port Express detail page; details live on the Port Express website ----
i=s.index('<div data-view="portex"');j=s.index('<!-- ================= ACTIVITY',i);s=s[:i]+s[j:]
rep("onclick=\"if(!event.target.closest('a'))location.hash='portex'\"","onclick=\"if(!event.target.closest('a'))window.open('"+PX+"','_blank','noopener')\"")
rep('<a class="pb2" href="#portex">ดูรายละเอียด</a>','<a class="pb2" '+EXT+'>ดูรายละเอียดคอร์ส</a>')
rep('<a class="ctb-f" href="#portex"','<a class="ctb-f" '+EXT)
rep('<a class="b1" href="#portex">ดูรายละเอียดคอร์ส</a><a class="b2" href="'+PX+'" target="_blank" rel="noopener">เว็บ Port Express</a>','<a class="b1" '+EXT+'>ดูรายละเอียดและสมัครเรียน</a>')
s=s.replace('<a href="#portex">Port Express</a>','<a '+EXT+'>Port Express</a>')
s=s.replace('href="#portex"',EXT)
# ---- Hall of Fame: a sacred hall, title in the middle, the kids' games on the stage ----
i=s.index('    <section class="tile hf3"');j=s.index('    </section>',i)+len('    </section>')
W=[('stressstrike','StressStrike','@วิน','ชนะเลิศ OBEC Roboplayground'),('phi-krahang','ผีกระหัง','@นนท์',''),('eugation-strike','Eugation Strike','@ไผ่',''),('slash-speed','SLASH//SPEED','@ดินสอ',''),
   ('midnight-at-roadside','Midnight at Roadside','@Windy',''),('hot-hot-hot','Hot Hot Hot','@โอม',''),('apocalypis-building','Apocalypis Building','@ฟาร์',''),('escape-rolling','Escape Rolling','@เป๊ป','')]
thumbs=''.join('<button type="button" class="hz-t" data-k="%d" aria-label="%s"><img src="img/work-%s.webp" alt="" loading="lazy"></button>'%(k,w[1],w[0]) for k,w in enumerate(W))
s=s[:i]+'''    <section class="tile hz" id="hz" aria-label="Hall of Fame ผลงานเด่นของน้องๆ ปี 2569">
      <span class="hz-dust" aria-hidden="true"></span>
      <p class="hz-k">ผลงานเด่นของน้องๆ ปี 2569</p>
      <h3 class="hz-t1">HALL OF FAME</h3>
      <p class="hz-s">เกมทุกเกมในห้องนี้ น้องๆ เขียนโปรแกรมสร้างเองกับมือ</p>
      <div class="hz-stage">
        <figure class="hz-f"><img id="hzImg" src="img/work-stressstrike.webp" alt=""><span class="hz-sh" aria-hidden="true"></span></figure>
        <div class="hz-cap" aria-live="polite"><b id="hzN">StressStrike</b><span id="hzBy">เกมที่น้อง @วิน สร้างเอง</span><em id="hzAw">ชนะเลิศ OBEC Roboplayground</em></div>
      </div>
      <div class="hz-row">'''+thumbs+'''</div>
      <a class="hz-go" href="#works" data-pane="hof">ดูผลงานทั้งหมด</a>
    </section>'''+s[j:]
i=s.index('  /* hall of fame: timed cards, the next work opens into the background */');j=s.index('  /* walking hamsters',i)
s=s[:i]+'''  /* hall of fame: one work on the stage at a time */
  (function(){var z=document.getElementById('hz');if(!z)return;var W='''+repr([list(w) for w in W]).replace("'",'"')+''',a=0,tm=0,hold=false;
    var img=document.getElementById('hzImg'),N=document.getElementById('hzN'),By=document.getElementById('hzBy'),Aw=document.getElementById('hzAw'),T=z.querySelectorAll('.hz-t');
    function show(k){a=(k+W.length)%W.length;var w=W[a];z.classList.remove('sw');void z.offsetWidth;z.classList.add('sw');
      setTimeout(function(){img.src='img/work-'+w[0]+'.webp';N.textContent=w[1];By.textContent='เกมที่น้อง '+w[2]+' สร้างเอง';Aw.textContent=w[3];Aw.style.display=w[3]?'':'none'},260);
      T.forEach(function(t,n){t.classList.toggle('on',n===a)});clearTimeout(tm);tm=setTimeout(tick,4200)}
    function tick(){if(hold||!document.querySelector('[data-view="home"].on')){tm=setTimeout(tick,600);return}show(a+1)}
    T.forEach(function(t){t.addEventListener('click',function(){show(+t.dataset.k)})});
    z.addEventListener('pointerenter',function(){hold=true});z.addEventListener('pointerleave',function(){hold=false});show(0)})();
'''+s[j:]
css=r'''
/* ===== v25: Hall of Fame as a sacred hall ===== */
.hg.st .tile.hz{display:block!important;position:relative;overflow:hidden;text-align:center;padding:clamp(48px,6vw,80px) 20px clamp(40px,5vw,64px)!important;min-height:0!important;color:#fff;
  background:#070503 url(img/hof-hall.webp) 50% 30%/cover}
.hz::before{content:"";position:absolute;inset:0;background:radial-gradient(45% 55% at 50% 45%,rgba(7,5,3,.15),rgba(7,5,3,.75) 80%),linear-gradient(rgba(7,5,3,.35),transparent 30%,transparent 70%,rgba(7,5,3,.9));pointer-events:none}
.hz>*{position:relative;z-index:1}
.hz .hz-k{color:#FFE6A0!important;opacity:1!important}.hz .hz-s{color:#FFF6D6!important;opacity:1!important;text-shadow:0 2px 8px #000}
.hz-dust{position:absolute!important;inset:0;background-image:radial-gradient(#FFE6A0 1px,transparent 1.6px),radial-gradient(#FFF6D6 .8px,transparent 1.4px);background-size:120px 160px,80px 110px;background-position:10px 0,40px 60px;opacity:.35;animation:dust 14s linear infinite;pointer-events:none}
@keyframes dust{to{background-position:10px -320px,40px -160px}}
.hz-k{font:700 1.05rem var(--display);color:#FFE6A0;letter-spacing:.04em}
.hz-t1{font:900 clamp(3.2rem,9.5vw,8.6rem)/1 var(--display)!important;letter-spacing:.04em;margin-top:10px!important;
  background:linear-gradient(100deg,#E8C877 0%,#FFF1C2 22%,#FFFFFF 32%,#F6DF9A 48%,#FFF1C2 66%,#E8C877 100%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;
  animation:hfS 6s linear infinite;filter:drop-shadow(0 6px 0 #3A2806) drop-shadow(0 0 40px rgba(255,200,90,.35))}
@keyframes hfS{from{background-position:120% 0}to{background-position:-130% 0}}
.hz-s{font:600 clamp(1rem,1.6vw,1.2rem) var(--display);color:rgba(255,246,214,.9);margin-top:12px}
.hz-stage{margin:clamp(28px,4vw,44px) auto 0;max-width:820px}
.hz-f{position:relative;margin:0 auto;width:min(100%,720px);padding:14px;background:linear-gradient(135deg,#FFF1C2,#B8862A 25%,#F6DF9A 50%,#8A6A1E 75%,#E8C877);
  box-shadow:0 0 0 3px #2A1C04,0 0 60px rgba(255,200,90,.35),0 40px 60px -20px rgba(0,0,0,.9)}
.hz-f::before{content:"";position:absolute;inset:6px;border:2px solid rgba(58,40,6,.6);pointer-events:none}
.hz-f img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;border:4px solid #1A1206;transition:opacity .25s,filter .25s}
.hz.sw .hz-f img{animation:hzIn .9s cubic-bezier(.2,.8,.2,1)}
@keyframes hzIn{0%{opacity:1}28%{opacity:0;filter:brightness(2)}30%{opacity:0;transform:scale(1.03)}100%{opacity:1;transform:none;filter:none}}
.hz-sh{position:absolute;inset:14px;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.28) 45%,transparent 60%);background-size:250% 100%;animation:shine 4.2s linear infinite;pointer-events:none}
@keyframes shine{from{background-position:120% 0}to{background-position:-120% 0}}
.hz-cap{display:grid;justify-items:center;gap:6px;margin-top:22px}
.hz-cap b{font:800 clamp(1.6rem,3vw,2.4rem) var(--display);color:#fff}
.hz-cap span{color:rgba(255,246,214,.85);font-weight:600}
.hz-cap em{font-style:normal;font:700 .95rem var(--display);color:#1A1206;background:linear-gradient(90deg,#E8C877,#FFF1C2);padding:4px 14px;border-radius:999px}
.hz.sw .hz-cap{animation:tcIn .7s .25s both}
.hz-row{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:28px}
.hz-t{width:clamp(64px,7vw,96px);padding:3px;border:0;background:#5A4210;cursor:pointer;opacity:.6;transition:opacity .2s,transform .2s,background .2s}
.hz-t img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover}
.hz-t:hover{opacity:1;transform:translateY(-3px)}
.hz-t.on{opacity:1;background:linear-gradient(135deg,#FFF1C2,#C9A04A);transform:translateY(-4px)}
.hz-go{display:inline-block;margin-top:30px;font:700 1.05rem var(--display);color:#1A1206;background:linear-gradient(90deg,#E8C877,#FFF1C2,#E8C877);padding:13px 30px;border-radius:999px;text-decoration:none}
.hz-go:hover{filter:brightness(1.08)}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v25.html','w').write(s)
print('v25 ok',len(s),s.count('#portex'))
