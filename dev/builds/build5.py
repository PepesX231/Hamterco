import re
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build4.py').read())          # -> v4, s holds it
LINE='https://page.line.me/jkm4247u?openQrModal=true'
PX='https://www.hamsterhub.co/portex-site/index.html'
AFO='https://www.hamsterhub.co/allforone'

# ---------- a real-looking arcade cabinet: every detail lives on the machine ----------
def cab(cls):
    return '''<div class="cab '''+cls+'''">
  <div class="cab-hood"><div class="cab-sign"><span class="lamp l"></span><b>PORT EXPRESS</b><span class="lamp r"></span><small>BY HAMSTER HUB</small></div></div>
  <div class="cab-up"><div class="cab-bez"><div class="cab-scr">
    <video src="img/portex-banner.mp4" poster="img/portex-poster.webp" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video>
    <span class="cab-hud"><em class="pxst">รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</em><em>1P READY</em></span></div></div></div>
  <div class="cab-dk">
    <span class="cab-js" aria-hidden="true"><span class="ball"></span><span class="shaft"></span></span>
    <a class="cab-b red" href="#portex"><span class="cap"></span><span class="lb">ดูรายละเอียด</span></a>
    <a class="cab-b blue" href="'''+PX+'''" target="_blank" rel="noopener"><span class="cap"></span><span class="lb">เว็บ Port Express</span></a>
    <a class="cab-b green" href="'''+LINE+'''" target="_blank" rel="noopener"><span class="cap"></span><span class="lb">ทัก LINE</span></a>
  </div>
  <div class="cab-lo">
    <span class="stk s1">ม.6 ยังไม่มีพอร์ต?<b>2 เดือน · 3 เกม</b></span>
    <div class="cab-door"><span class="lcd">5,990฿</span><small>ปกติ 9,990</small><span class="slots"><span></span><span></span></span><span class="ins">INSERT COIN</span></div>
    <span class="stk s2">เรียน จ · พ · ศ<b>เริ่ม 9 พ.ย.</b></span>
  </div>
  <div class="cab-kick"></div>
</div>'''

# ---------- HOME hero: what Hamster Hub is + a showcase of what's on (hamsters stand on top of it) ----------
cut('  <section class="h-hero hp" id="hx">','  <section class="paths">','''  <section class="h-hero h5" id="hx">
    <div class="wrap h5-top">
      <p class="h5-k rv">Hamster Hub</p>
      <h1 class="rv">ผลงานจริง ขายได้จริง<br><em>ติดมหาลัยจริง</em></h1>
      <p class="h5-s rv">เราพาน้องสร้างเกม แอป และ IoT ตั้งแต่ไอเดียแรก จนเป็นผลงานที่มีคนใช้ ลงแข่ง และยื่นเข้ามหาวิทยาลัย</p>
    </div>
    <div class="sc-wrap">
      <div class="h5-stage"><div class="hx3" id="hx3" aria-hidden="true"><canvas id="hxCanvas"></canvas><div class="hx-say" id="hxSay"></div></div></div>
      <div class="sc" id="sc" aria-roledescription="carousel" aria-label="ตอนนี้ที่ Hamster Hub">
        <div class="sc-main">
          <article class="sl s-px on">
            <video src="img/portex-banner.mp4" poster="img/portex-poster.webp" muted loop playsinline preload="metadata" aria-hidden="true"></video>
            <div class="sl-c"><p class="sl-k">คอร์สทำพอร์ต ม.6 · <span class="pxst">รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569</span></p><h2>Port Express</h2><p class="sl-d">เรียน 2 เดือน ได้เกม 3 งาน พร้อมยื่นมหาลัย · 5,990 บาท</p>
              <div class="sl-b"><a class="b1" href="#portex">ดูรายละเอียด</a><a class="b2" href="'''+PX+'''" target="_blank" rel="noopener">เว็บ Port Express</a></div></div>
          </article>
          <article class="sl s-afo">
            <img class="afo-big" src="img/k-afo-logo.webp" alt="" loading="lazy"><img class="afo-ic i0" src="img/afo-ic0.webp" alt="" aria-hidden="true"><img class="afo-ic i1" src="img/afo-ic1.webp" alt="" aria-hidden="true"><img class="afo-ic i2" src="img/afo-ic2.webp" alt="" aria-hidden="true">
            <div class="sl-c"><p class="sl-k" id="afoTag">กิจกรรมถัดไป · 14 พ.ย. 2569</p><h2>All for One University<br>รอบชิงชนะเลิศ</h2><p class="sl-d">IoTE KMITL 2026 Showcase ที่ สจล. ลาดกระบัง</p>
              <div class="cd" id="afoCd" aria-label="นับถอยหลังถึงวันแข่ง"><div><b id="cdD">0</b><span>วัน</span></div><div><b id="cdH">0</b><span>ชั่วโมง</span></div><div><b id="cdM">0</b><span>นาที</span></div></div>
              <div class="sl-b"><a class="b1" href="'''+AFO+'''" target="_blank" rel="noopener">รายละเอียดงาน</a><a class="b2" href="#activity">กิจกรรมทั้งหมด</a></div></div>
          </article>
          <article class="sl s-wk">
            <video src="img/reel.mp4" poster="img/reel-poster.webp" muted loop playsinline preload="none" aria-hidden="true"></video>
            <div class="sl-c"><p class="sl-k">Hall of Fame</p><h2>ผลงานจริงของน้องๆ</h2><p class="sl-d">ทุกฉากในคลิปนี้มาจากเกมที่น้องสร้างเอง</p>
              <div class="sl-b"><a class="b1" href="#works">ดูผลงาน</a></div></div>
          </article>
          <article class="sl s-dk">
            <div class="dk-fan"><img src="img/dek69-6.webp" alt="" loading="lazy"><img src="img/dek69-1.webp" alt="" loading="lazy"><img src="img/dek69-13.webp" alt="" loading="lazy"></div>
            <div class="sl-c"><p class="sl-k">DEK69</p><h2>รุ่นพี่ติดมหาลัย<br>แล้ว 48 คน</h2><p class="sl-d">สจล. 24 · มหิดล 9 · จุฬาฯ 8 · เกษตรศาสตร์ 7</p>
              <div class="sl-b"><a class="b1" href="#works" data-pane="sen">ดูรุ่นพี่</a></div></div>
          </article>
        </div>
        <div class="sc-nav" role="tablist">
          <button type="button" role="tab" aria-selected="true"><img src="img/portex-poster.webp" alt=""><span><b>Port Express</b><small>คอร์สทำพอร์ต ม.6</small></span><em class="bar"></em></button>
          <button type="button" role="tab" aria-selected="false"><img src="img/k-afo.webp" alt=""><span><b>All for One</b><small>รอบชิง 14 พ.ย.</small></span><em class="bar"></em></button>
          <button type="button" role="tab" aria-selected="false"><img src="img/reel-poster.webp" alt=""><span><b>Hall of Fame</b><small>ผลงานน้องๆ</small></span><em class="bar"></em></button>
          <button type="button" role="tab" aria-selected="false"><img src="img/dek69-8.webp" alt=""><span><b>DEK69</b><small>ติดมหาลัย 48 คน</small></span><em class="bar"></em></button>
        </div>
      </div>
    </div>
  </section>

''')
# paths: startup wording + new pose
rep('<span class="pod"><img src="img/n-biz.webp" alt="" loading="lazy"><i class="bubble">ขายได้จริง!</i></span><span class="k">สตาร์ทอัพ</span><span class="w">สร้างธุรกิจ</span>',
    '<span class="pod"><img src="img/n-up.webp" alt="" loading="lazy"><i class="bubble">ไปให้สุด!</i></span><span class="k">ธุรกิจของตัวเอง</span><span class="w">สตาร์ทอัพ</span>')
rep('<img class="do-i" src="img/n-biz.webp"','<img class="do-i" src="img/n-up.webp"')

# seniors: dark 3D ring
cut('  <section class="sx">','  <section class="ptn">','''  <section class="cy">
    <p class="cy-bg" aria-hidden="true">CONGRATULATIONS</p>
    <div class="wrap cy-h">
      <div><p class="cy-k rv">DEK69</p><h2 class="rv">รุ่นพี่ 48 คน<br>ไปถึงคณะที่ใช่แล้ว</h2></div>
      <div class="cy-u rv" role="group" aria-label="ดูตามมหาวิทยาลัย">
        <button type="button" data-u="k" style="--c:#FF8A3D" aria-pressed="false"><b>24</b>สจล.</button>
        <button type="button" data-u="m" style="--c:#7D9BFF" aria-pressed="false"><b>9</b>มหิดล</button>
        <button type="button" data-u="c" style="--c:#FF7EB6" aria-pressed="false"><b>8</b>จุฬาฯ</button>
        <button type="button" data-u="u" style="--c:#4FD69C" aria-pressed="false"><b>7</b>เกษตรศาสตร์</button>
      </div>
    </div>
    <div class="cy-st" aria-label="โปสเตอร์รุ่นพี่ DEK69"><div class="cy-r" id="cyR"></div></div>
    <div class="wrap cy-f"><p>ชี้ค้างเพื่อหยุด · แตะมหาวิทยาลัยเพื่อดูเฉพาะที่นั่น</p><a href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด ›</a></div>
  </section>

''')

# ---------- COURSES: the banner IS the cabinet ----------
cut('    <div class="ct-px">','    <section class="ct-list">','''    <div class="ct-cab">'''+cab('c-big')+'''<span class="ct-floor" aria-hidden="true"></span></div>
''')
# ---------- PORT EXPRESS hero uses the same machine ----------
s=re.sub(r'<a class="arc px-arc".*?</a></span></a>|<a class="arc px-arc".*?<span class="arc-ft"></span></a>',lambda m:cab('c-px'),s,count=1,flags=re.S)
assert 'class="arc ' not in s

# ---------- ACTIVITY: an explicit "coming up" ----------
rep('    <a class="ac-next" ','''    <div class="ac-sh" style="margin-top:8px"><h2>กำลังจะมา</h2><p>รอบชิงชนะเลิศออนไซต์ ต่อจากรอบออนไลน์ Hallow Open House เมื่อ 7 พ.ย.</p></div>
    <div class="ac-up"><a class="ac-next" ''')
rep('<h2>All for One University รอบชิงชนะเลิศ</h2>','<h2>All for One University รอบชิงชนะเลิศ</h2><p class="sub2">IoTE KMITL 2026 Showcase · สำหรับทีมที่ผ่านการคัดเลือก</p>')
i=s.index('<a class="ac-next" ');j=s.index('</a>',i)+4
s=s[:j]+'''<div class="ac-soon"><img src="img/n-peek.webp" alt="" loading="lazy"><b>กิจกรรมถัดไป<br>กำลังจะประกาศ</b><p>ค่ายและการแข่งขันรอบใหม่ ประกาศทาง LINE ก่อนที่อื่น</p><a class="btn btn-line" href="'''+LINE+'''" target="_blank" rel="noopener">รับแจ้งเตือนทาง LINE</a></div></div>'''+s[j:]

# ---------- NAV: courses = many art styles, not only games ----------
i=s.index('.nav-in>a.nv-c::after{');j=s.index('.nav-in>a.nv-a>.roll{')
s=s[:i]+'''.nav-in>a.nv-c::after{display:none}
.nav-in>a.nv-c[aria-current="page"]::after{display:block}
.nav-in>a.nv-c:hover>span{animation:styl 1.6s steps(1) infinite}
@keyframes styl{0%{color:#5B3FD6;text-shadow:2px 2px 0 #FFD24A;transform:none;background:none}
 25%{color:#fff;background:#E60012;transform:skewX(-12deg) rotate(-4deg);box-shadow:3px 3px 0 #0B0B0F;text-shadow:none;padding:0 6px}
 50%{color:#fff;-webkit-text-stroke:.6px #0B1640;text-shadow:1px 1px 0 #1068DC,2px 2px 0 #1068DC,3px 3px 0 #0B1640;transform:translateY(-2px);background:none}
 75%{color:#3FB950;background:#0D1117;font-family:ui-monospace,Menlo,monospace;padding:0 6px;transform:none;text-shadow:none}}
'''+s[j:]

# ---------- page transitions ----------
i=s.index('  function ptBuild(v){');j=s.index('  var first=true;function route()')
s=s[:i]+r'''  function ptBuild(v){var h='';
    if(v==='courses'||v==='portex'){var C=['#5B3FD6','#E60012','#1068DC','#0D1117','#FFB81C','#2E9E6B','#FF8A3D','#0B1640'],c=innerWidth<700?4:7,r=innerWidth<700?7:4;
      for(var y=0;y<r;y++)for(var x=0;x<c;x++){var k=(x+y)%C.length;h+='<span class="t5-t" style="left:'+(x*100/c)+'%;top:'+(y*100/r)+'%;width:'+(100/c+.3)+'%;height:'+(100/r+.3)+'%;--c:'+C[(k*3+y)%C.length]+';--dl:'+((x+y)*.035).toFixed(3)+'s"></span>'}
      h+='<b class="t5-cl"><small>COURSES</small>คอร์ส</b>'}
    else if(v==='activity'){h='<span class="t5-bg l"></span><span class="t5-bg r"></span><div class="t5-tk"><div class="tl"><small>HAMSTER HUB · EVENTS</small><b>กิจกรรม</b><em id="t5d">ถัดไป 14 พ.ย.</em></div><div class="tr"><small>ADMIT</small><b>ONE</b></div></div>';var nx=document.getElementById('nvNext');if(nx)h=h.replace('ถัดไป 14 พ.ย.',nx.textContent)}
    else if(v==='works'){h='<span class="t5-cu l"></span><span class="t5-cu r"></span><span class="t5-sp"></span>';for(var k=0;k<22;k++)h+='<span class="t5-d" style="left:'+(25+Math.random()*50).toFixed(1)+'%;top:'+(20+Math.random()*60).toFixed(1)+'%;--dl:'+(Math.random()*.6).toFixed(2)+'s;--s:'+(2+Math.random()*4).toFixed(1)+'px"></span>';h+='<b class="t5-hof"><small>HAMSTER HUB · CLASS OF 2026</small><span>HALL OF FAME</span></b>'}
    else if(v==='about'){h='<span class="pt-band"></span><img class="pt-run" src="img/n-walker.webp" alt="">'}
    else{h='<span class="pt-home"></span><img class="pt-peek" src="img/n-peek.webp" alt="">'}
    pt.className='pt v-'+v;pt.innerHTML=h;void pt.offsetWidth;pt.classList.add('in')}
'''+s[j:]
rep("var hold=v==='activity'?700:620;","var hold={works:1050,activity:900,courses:760,portex:760}[v]||620;")
rep("ptT=setTimeout(function(){pt.className='pt';pt.innerHTML=''},1000)","ptT=setTimeout(function(){pt.className='pt';pt.innerHTML=''},1150)")

# ---------- hero JS: hamsters stand on top of the showcase ----------
rep("IW=1536,IH=864,V0=.79,V1=.965","IW=1536,IH=864,V0=.935,V1=.965")
rep("hx.style.setProperty('--floor',Math.round((1-V0)*bh)+'px');","hx.style.setProperty('--feet',Math.round((1-(V0+V1)/2)*bh)+'px');")
# remove v4 seniors gallery JS (markup gone)
i=s.index('  /* seniors: an always-moving gallery */');j=s.index('  /* router */',i);s=s[:i]+s[j:]
extra=r'''
  /* showcase: Apple-style auto advance with progress bars */
  (function(){var sc=document.getElementById('sc');if(!sc)return;var sl=sc.querySelectorAll('.sl'),tb=sc.querySelectorAll('.sc-nav button'),i=0;
    function go(n){i=(n+sl.length)%sl.length;sl.forEach(function(e,k){e.classList.toggle('on',k===i);var v=e.querySelector('video');if(v){if(k===i){v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){})}else v.pause()}});
      tb.forEach(function(b,k){b.setAttribute('aria-selected',String(k===i));var bar=b.querySelector('.bar');bar.style.animation='none';void bar.offsetWidth;bar.style.animation=''})}
    tb.forEach(function(b,k){b.addEventListener('click',function(){go(k)});b.querySelector('.bar').addEventListener('animationend',function(){if(k===i)go(i+1)})});
    sc.addEventListener('pointerenter',function(){sc.classList.add('hold')});sc.addEventListener('pointerleave',function(){sc.classList.remove('hold')});go(0)})();
  /* seniors: a slowly turning 3D ring of posters */
  (function(){var R=document.getElementById('cyR');if(!R)return;var on=null,t=0;
    function card(g){return '<figure class="cy-c"><img src="img/dek69-'+g[0]+'.webp" alt="'+g[1]+' '+UN[g[2]]+'" loading="lazy"><figcaption><b>'+g[1]+'</b><span style="--c:'+UC[g[2]]+'">'+UN[g[2]]+'</span></figcaption></figure>'}
    function build(){var L=G.filter(function(g){return !on||g[2]===on}),a=L.slice();while(a.length<12)a=a.concat(L);
      R.innerHTML=a.map(card).join('');var cs=R.querySelectorAll('.cy-c'),w=innerWidth<=600?174:258,n=cs.length,rad=Math.round(w/2/Math.tan(Math.PI/n));
      cs.forEach(function(c,k){c.style.transform='rotateY('+(k*360/n)+'deg) translateZ('+rad+'px)'});R.style.setProperty('--R',rad+'px');R.style.setProperty('--d',(n*3)+'s');R.style.animation='none';void R.offsetWidth;R.style.animation=''}
    build();addEventListener('resize',function(){clearTimeout(t);t=setTimeout(build,250)});
    document.querySelectorAll('.cy-u button').forEach(function(b){b.addEventListener('click',function(){on=on===b.dataset.u?null:b.dataset.u;document.querySelectorAll('.cy-u button').forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.u===on))});build()})})})();
'''
rep("  /* router */",extra+"  /* router */")

# ---------- CSS ----------
css=r'''
/* ===== v5 ===== */
/* arcade cabinet (sized in em, so one font-size scales it) */
.cab{position:relative;width:30em;margin:0 auto;font-size:16px;filter:drop-shadow(0 2.4em 2em rgba(10,6,40,.35))}
.cab-hood{position:relative;height:6em;background:linear-gradient(#2B2075,#1B1446);border-radius:1.4em 1.4em .3em .3em;padding:.6em;box-shadow:inset 0 .3em 0 rgba(255,255,255,.12),inset .35em 0 0 #FF3EA5,inset -.35em 0 0 #39E0FF}
.cab-sign{position:relative;height:100%;border-radius:.8em;background:radial-gradient(120% 140% at 50% 0%,#5A2BD0 0%,#24105E 55%,#120838 100%);display:grid;place-items:center;align-content:center;overflow:hidden;box-shadow:inset 0 0 0 .22em #0B0820,inset 0 0 1.6em rgba(255,62,165,.45)}
.cab-sign::before{content:"";position:absolute;inset:0;background:repeating-conic-gradient(from 0deg at 50% 120%,rgba(255,255,255,.07) 0 6deg,transparent 6deg 14deg)}
.cab-sign b{position:relative;font:400 1.5em var(--pixel);color:#FFD24A;text-shadow:0 0 .4em rgba(255,210,74,.8),.12em .12em 0 #E0337E}
.cab-sign small{position:relative;font:400 .5em var(--pixel);color:#9FE7FF;letter-spacing:.2em;margin-top:.5em}
.lamp{position:absolute;top:50%;width:.6em;height:.6em;border-radius:50%;margin-top:-.3em;background:#FF4D6D;box-shadow:0 0 .8em #FF4D6D;animation:bl .9s steps(1) infinite}.lamp.l{left:1em}.lamp.r{right:1em;background:#39E0FF;box-shadow:0 0 .8em #39E0FF;animation-delay:.45s}
.cab-up{position:relative;background:#1B1446;padding:1em 1.5em 1.3em;box-shadow:inset .35em 0 0 #FF3EA5,inset -.35em 0 0 #39E0FF}
.cab-up::before,.cab-up::after{content:"";position:absolute;top:0;bottom:0;width:1.2em;background:repeating-linear-gradient(160deg,#120C36 0 .7em,#1A1250 .7em 1.4em)}
.cab-up::before{left:.35em}.cab-up::after{right:.35em}
.cab-bez{position:relative;z-index:1;background:#07051A;border-radius:1em;padding:.9em;box-shadow:inset 0 0 0 .25em #2D2470,0 .3em 0 #0B0820}
.cab-scr{position:relative;border-radius:1.5em/1.2em;overflow:hidden;background:#05061E;box-shadow:0 0 1.4em rgba(57,224,255,.25)}
.cab-scr video{display:block;width:100%;aspect-ratio:16/10;object-fit:cover}
.cab-scr::before{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 2px,transparent 2px 4px);box-shadow:inset 0 0 2.4em rgba(0,0,0,.75)}
.cab-scr::after{content:"";position:absolute;inset:0;z-index:2;pointer-events:none;background:linear-gradient(125deg,rgba(255,255,255,.2) 0 14%,transparent 30%)}
.cab-hud{position:absolute;left:0;right:0;bottom:0;z-index:3;display:flex;justify-content:space-between;gap:1em;padding:.5em .9em;background:linear-gradient(transparent,rgba(5,6,30,.85))}
.cab-hud em{font-style:normal;font:600 .72em var(--display);color:#7CF29A;text-shadow:0 0 .5em rgba(124,242,154,.6)}
.cab-hud em:last-child{font:400 .5em var(--pixel);color:#FFD24A;align-self:center;animation:bl 1.2s steps(1) infinite}
.cab-dk{position:relative;z-index:2;margin:0 -1.6em;padding:1.2em 2.2em 1em;display:flex;align-items:flex-start;justify-content:space-between;gap:.8em;background:linear-gradient(#4636B8,#2E2388);clip-path:polygon(3.5% 0,96.5% 0,100% 100%,0 100%);box-shadow:inset 0 .3em 0 rgba(255,255,255,.18)}
.cab-dk::after{content:"";position:absolute;left:0;right:0;bottom:0;height:.6em;background:#1B1446}
.cab-js{position:relative;width:3.4em;height:4.2em;flex:none}
.cab-js .shaft{position:absolute;left:50%;bottom:.6em;width:.5em;height:2.6em;margin-left:-.25em;background:linear-gradient(90deg,#222,#666,#222);transform-origin:50% 100%;transition:transform .2s}
.cab-js .ball{position:absolute;left:50%;top:0;z-index:1;width:2.2em;height:2.2em;margin-left:-1.1em;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FF9AA8,#E0203C 45%,#8A0E22);box-shadow:0 .3em .5em rgba(0,0,0,.4);transition:transform .2s}
.cab-js::after{content:"";position:absolute;left:50%;bottom:0;width:3em;height:1.2em;margin-left:-1.5em;border-radius:50%;background:radial-gradient(#111 40%,#2A2A2A)}
.cab:hover .cab-js .shaft,.cab:hover .cab-js .ball{transform:rotate(-14deg) translateX(-.3em)}
.cab-b{display:flex;flex-direction:column;align-items:center;gap:.5em;text-decoration:none;flex:1;min-width:0}
.cab-b .cap{width:3.2em;height:3.2em;border-radius:50%;background:radial-gradient(circle at 35% 30%,var(--h),var(--c) 50%,var(--s));box-shadow:0 .45em 0 var(--s),0 .55em .6em rgba(0,0,0,.45),0 0 0 .25em #15103F;transition:transform .12s,box-shadow .12s}
.cab-b:hover .cap{transform:translateY(.25em);box-shadow:0 .2em 0 var(--s),0 .25em .4em rgba(0,0,0,.45),0 0 0 .25em #15103F,0 0 1.4em var(--c)}
.cab-b .lb{font:700 .78em/1.25 var(--display);color:#fff;text-align:center;background:#15103F;padding:.35em .7em;border-radius:.4em;white-space:nowrap}
.cab-b:hover .lb{background:var(--c);color:#0B0820}
.cab-b.red{--c:#FF3B5C;--h:#FFB3C0;--s:#9E1230}.cab-b.blue{--c:#39B6FF;--h:#C6ECFF;--s:#14629A}.cab-b.green{--c:#3FDC7E;--h:#C8FFD9;--s:#1B7F43}
.cab-lo{position:relative;margin:0 .5em;padding:1.4em 1.2em 1.6em;display:flex;align-items:center;justify-content:center;gap:1em;background:#1B1446 repeating-linear-gradient(115deg,transparent 0 1.6em,rgba(255,62,165,.08) 1.6em 2.2em);box-shadow:inset .35em 0 0 #FF3EA5,inset -.35em 0 0 #39E0FF}
.cab-door{display:grid;justify-items:center;gap:.35em;padding:.9em 1.3em;background:#0E0A2A;border-radius:.5em;box-shadow:inset 0 0 0 .22em #3A3290}
.lcd{font:400 1.25em var(--pixel);color:#FFD24A;background:#1A0E05;padding:.35em .5em;box-shadow:inset 0 0 0 .15em #4A3210;text-shadow:0 0 .4em rgba(255,210,74,.7)}
.cab-door small{font:600 .7em var(--display);color:#8A90B8;text-decoration:line-through}
.slots{display:flex;gap:.8em}.slots span{width:.45em;height:1.5em;background:#2B0710;border-radius:.2em;box-shadow:0 0 0 .2em #4D1020,0 0 .9em #FF3B5C}
.ins{font:400 .48em var(--pixel);color:#FF7A90;animation:bl 1s steps(1) infinite}
.stk{flex:1;font:600 .74em/1.35 var(--display);color:#0B0820;background:#FFD24A;padding:.6em .7em;border-radius:.3em;transform:rotate(-4deg);box-shadow:.2em .2em 0 #0B0820;text-align:center}
.stk b{display:block;font-weight:800}.stk.s2{background:#9FE7FF;transform:rotate(3deg)}
.cab-kick{height:1.6em;margin:0 .5em;background:#0B0820;border-radius:0 0 .5em .5em}
.c-big{font-size:clamp(11.5px,2.5vw,17px)}
.c-px{font-size:clamp(10px,1.25vw,15px)}
.ct-cab{position:relative;padding:20px 0 60px}
.ct-floor{position:absolute;left:50%;bottom:34px;width:min(720px,90%);height:60px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(91,63,214,.35),transparent);z-index:-1}
/* home hero */
.h5{padding:clamp(56px,7vw,92px) 0 0;background:radial-gradient(70% 50% at 50% 0%,#FFF4DC 0%,#fff 70%);overflow:hidden;--feet:30px}
.h5-top{text-align:center}
.h5-k{font:700 1rem var(--display);color:#B26A00}
.h5 h1{font:700 clamp(2.6rem,6.4vw,5.2rem)/1.08 var(--display);letter-spacing:-.025em;margin-top:10px}
.h5 h1 em{font-style:normal;background:linear-gradient(90deg,#FF8A3D,#E0337E 60%,#5B3FD6);-webkit-background-clip:text;background-clip:text;color:transparent}
.h5-s{color:var(--mute);font-size:clamp(1rem,1.5vw,1.2rem);max-width:640px;margin:16px auto 0;line-height:1.65}
.sc-wrap{position:relative;max-width:1240px;margin:clamp(110px,14vw,190px) auto 0;padding:0 var(--gl)}
.h5-stage{position:absolute;left:0;right:0;bottom:calc(100% - var(--feet));height:clamp(170px,20vw,260px);pointer-events:none;z-index:4}
.h5 .hx3{position:absolute;inset:0;background:none;border-radius:0;height:auto}
.sc-main{position:relative;height:clamp(420px,46vw,560px);border-radius:28px;overflow:hidden;background:#0B0B0F;box-shadow:0 40px 80px -40px rgba(11,22,64,.45)}
.sl{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .7s,visibility .7s;color:#fff}
.sl.on{opacity:1;visibility:visible}
.sl>video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.s-px>video{left:auto;width:62%;object-position:88% 50%;-webkit-mask:linear-gradient(90deg,transparent,#000 30%);mask:linear-gradient(90deg,transparent,#000 30%)}
.s-px{background:#0A0B2E}
.sl::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,6,20,.82) 0%,rgba(5,6,20,.45) 45%,transparent 75%)}
.sl-c{position:absolute;left:clamp(24px,5vw,64px);bottom:clamp(28px,5vw,60px);right:24px;z-index:2;max-width:560px}
.sl.on .sl-c>*{animation:slUp .7s cubic-bezier(.2,.8,.2,1) both}
.sl.on .sl-c>*:nth-child(2){animation-delay:.06s}.sl.on .sl-c>*:nth-child(3){animation-delay:.12s}.sl.on .sl-c>*:nth-child(4){animation-delay:.18s}.sl.on .sl-c>*:nth-child(5){animation-delay:.24s}
@keyframes slUp{from{opacity:0;transform:translateY(18px)}}
.sl-k{font:600 .95rem var(--display);color:#FFD24A}
.sl h2{font:700 clamp(2rem,4.4vw,3.6rem)/1.08 var(--display);margin-top:8px;letter-spacing:-.02em}
.sl-d{color:rgba(255,255,255,.85);margin-top:10px;font-size:1.05rem}
.sl-b{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px}
.sl-b a{display:inline-flex;align-items:center;min-height:46px;padding:0 22px;border-radius:999px;font:600 1rem var(--display);text-decoration:none}
.sl-b .b1{background:#fff;color:#0B1640}.sl-b .b1:hover{background:#FFD24A}
.sl-b .b2{color:#fff;background:rgba(255,255,255,.14);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}.sl-b .b2:hover{background:rgba(255,255,255,.26)}
.s-afo{background:#1068DC radial-gradient(rgba(255,255,255,.14) 1.5px,transparent 1.5px) 0 0/22px 22px}
.s-afo::after{background:linear-gradient(90deg,rgba(8,30,90,.75),transparent 60%)}
.afo-big{position:absolute;right:6%;top:50%;width:min(44%,520px);transform:translateY(-50%) rotate(-4deg);filter:drop-shadow(4px 0 0 #fff) drop-shadow(-4px 0 0 #fff) drop-shadow(0 4px 0 #fff) drop-shadow(0 -4px 0 #fff) drop-shadow(0 20px 30px rgba(0,0,0,.3));z-index:1}
.s-afo .afo-ic{z-index:1}
.s-afo .afo-ic.i0{right:4%;top:12%;left:auto}.s-afo .afo-ic.i1{right:38%;bottom:10%;left:auto;top:auto}.s-afo .afo-ic.i2{right:8%;bottom:14%;left:auto;top:auto}
.s-afo .cd{margin-top:16px}
.s-dk{background:radial-gradient(80% 90% at 75% 50%,#3B1E8C,#0B0B1E)}
.dk-fan{position:absolute;right:8%;top:50%;width:min(46%,520px);height:80%;transform:translateY(-50%);z-index:1}
.dk-fan img{position:absolute;top:8%;width:44%;aspect-ratio:4/5;object-fit:cover;border-radius:16px;box-shadow:0 30px 50px -20px rgba(0,0,0,.7)}
.dk-fan img:nth-child(1){left:0;transform:rotate(-10deg)}.dk-fan img:nth-child(2){left:28%;top:2%;z-index:1}.dk-fan img:nth-child(3){right:0;transform:rotate(10deg)}
.sc-nav{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:14px}
.sc-nav button{position:relative;display:flex;align-items:center;gap:12px;padding:10px;border:0;border-radius:18px;background:#F5F5F7;cursor:pointer;text-align:left;overflow:hidden;transition:background .2s,transform .2s}
.sc-nav button:hover{transform:translateY(-2px)}
.sc-nav button[aria-selected="true"]{background:#fff;box-shadow:0 0 0 1px #E3E3E8,0 14px 30px -18px rgba(0,0,0,.3)}
.sc-nav img{width:64px;height:48px;object-fit:cover;border-radius:10px;flex:none}
.sc-nav span{display:grid;min-width:0}.sc-nav b{font:700 .98rem var(--display);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.sc-nav small{color:var(--mute);font-size:.85rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sc-nav .bar{position:absolute;left:0;bottom:0;height:3px;width:100%;background:#1D1D1F;transform:scaleX(0);transform-origin:left}
.sc-nav button[aria-selected="true"] .bar{animation:scBar 6.5s linear forwards}
.sc.hold .bar{animation-play-state:paused!important}
@keyframes scBar{to{transform:scaleX(1)}}
/* seniors ring */
.cy{position:relative;padding:clamp(80px,10vw,120px) 0 clamp(60px,8vw,90px);background:radial-gradient(60% 55% at 50% 58%,#3A1D8C 0%,#14093A 45%,#07070D 80%);color:#fff;overflow:hidden}
.cy-bg{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);font:800 clamp(4rem,13vw,12rem)/1 var(--display);letter-spacing:.02em;color:transparent;-webkit-text-stroke:1.5px rgba(186,160,255,.22);white-space:nowrap;pointer-events:none}
.cy-h{position:relative;display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}
.cy-k{font:400 .8rem var(--pixel);color:#FFD24A;letter-spacing:.12em}
.cy h2{font:700 clamp(2.2rem,4.4vw,3.4rem)/1.12 var(--display);margin-top:10px}
.cy-u{display:flex;gap:10px;flex-wrap:wrap}
.cy-u button{display:inline-flex;align-items:baseline;gap:8px;padding:10px 16px;border-radius:999px;border:0;cursor:pointer;color:#fff;font:600 .95rem var(--display);background:rgba(255,255,255,.08);box-shadow:inset 0 0 0 1px rgba(255,255,255,.16);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);transition:background .2s}
.cy-u b{font:700 1.4rem var(--display);color:var(--c)}
.cy-u button:hover{background:rgba(255,255,255,.16)}
.cy-u button[aria-pressed="true"]{background:var(--c);color:#0B0B14}.cy-u button[aria-pressed="true"] b{color:#0B0B14}
.cy-st{position:relative;height:clamp(380px,40vw,470px);margin-top:36px;perspective:1600px;perspective-origin:50% 40%}
.cy-r{position:absolute;left:50%;top:6%;width:0;height:0;transform-style:preserve-3d;animation:cyR var(--d,50s) linear infinite}
.cy-st:hover .cy-r{animation-play-state:paused}
@keyframes cyR{from{transform:translateZ(calc(var(--R) * -1)) rotateX(-4deg) rotateY(0)}to{transform:translateZ(calc(var(--R) * -1)) rotateX(-4deg) rotateY(-360deg)}}
.cy-c{position:absolute;left:-115px;top:0;width:230px;margin:0;backface-visibility:hidden;-webkit-backface-visibility:hidden}
.cy-c img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:18px;box-shadow:0 0 0 1px rgba(255,255,255,.14),0 30px 50px -24px rgba(0,0,0,.8)}
.cy-c figcaption{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:10px}
.cy-c b{font:700 1rem var(--display)}.cy-c span{font:600 .78rem var(--display);color:#fff;background:var(--c);padding:2px 10px;border-radius:999px}
.cy-f{position:relative;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.cy-f p{color:rgba(255,255,255,.55);font-size:.9rem}.cy-f a{color:#BBA8FF;font-weight:600;text-decoration:none}
/* activity: coming up */
.ac-up{display:grid;grid-template-columns:minmax(0,2.2fr) minmax(0,1fr);gap:16px;margin-top:20px}
.ac-up .ac-next{margin:0}
.sub2{color:#9FC2FF!important;margin-top:4px!important}
.ac-soon{display:flex;flex-direction:column;align-items:flex-start;gap:8px;padding:28px;border-radius:24px;background:#F5F5F7}
.ac-soon img{width:110px}.ac-soon b{font:700 1.4rem/1.3 var(--display)}.ac-soon p{color:var(--mute)}.ac-soon .btn{margin-top:auto}
/* transitions v5 */
.t5-t{position:absolute;background:var(--c);transform:perspective(600px) rotateY(90deg);animation:t5in .38s cubic-bezier(.3,.7,.3,1) var(--dl) forwards}
.pt.out .t5-t{transform:none;animation:t5out .34s cubic-bezier(.6,0,.8,.4) var(--dl) forwards}
@keyframes t5in{to{transform:perspective(600px) rotateY(0)}}@keyframes t5out{to{transform:perspective(600px) rotateY(-90deg)}}
.t5-cl{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) scale(.8);display:grid;justify-items:center;gap:8px;font:800 clamp(3rem,9vw,6.5rem)/1 var(--display);color:#fff;text-shadow:0 10px 30px rgba(0,0,0,.35);opacity:0;animation:t5pop .45s .38s cubic-bezier(.3,1.6,.5,1) forwards}
.t5-cl small{font:400 .8rem var(--pixel);letter-spacing:.2em;color:#FFD24A}
@keyframes t5pop{to{opacity:1;transform:translate(-50%,-50%) scale(1)}}
.pt.out .t5-cl{animation:fadeOut .2s forwards;opacity:1;transform:translate(-50%,-50%)}
.t5-bg{position:absolute;top:0;bottom:0;width:50.5%;background:#0B1640;transform:translateY(-100%);animation:t5drop .4s cubic-bezier(.7,0,.2,1) forwards}
.t5-bg.l{left:0}.t5-bg.r{right:0;animation-delay:.05s}
@keyframes t5drop{to{transform:none}}
.pt.out .t5-bg{transform:none;animation:none;transition:transform .6s cubic-bezier(.7,0,.2,1) .15s}
.pt.out .t5-bg.l{transform:translateX(-100%)}.pt.out .t5-bg.r{transform:translateX(100%)}
.t5-tk{position:absolute;left:50%;top:50%;display:flex;width:min(640px,86vw);height:min(240px,40vw);transform:translate(-50%,-160%) rotate(-8deg);animation:t5tk .55s .2s cubic-bezier(.3,1.4,.5,1) forwards}
@keyframes t5tk{to{transform:translate(-50%,-50%) rotate(-3deg)}}
.t5-tk>div{position:relative;background:#FFB81C;color:#0B1640;display:grid;align-content:center;padding:0 6%;transition:transform .55s cubic-bezier(.6,0,.4,1),opacity .55s}
.t5-tk .tl{flex:3;border-radius:18px 0 0 18px;-webkit-mask:radial-gradient(circle at 100% 0,transparent 16px,#000 17px) top/100% 51% no-repeat,radial-gradient(circle at 100% 100%,transparent 16px,#000 17px) bottom/100% 51% no-repeat;mask:radial-gradient(circle at 100% 0,transparent 16px,#000 17px) top/100% 51% no-repeat,radial-gradient(circle at 100% 100%,transparent 16px,#000 17px) bottom/100% 51% no-repeat}
.t5-tk .tr{flex:1;border-radius:0 18px 18px 0;background:#FF4D6D;color:#fff;text-align:center;border-left:4px dashed #0B1640}
.t5-tk small{font:400 clamp(.45rem,1.2vw,.7rem) var(--pixel);letter-spacing:.12em}
.t5-tk b{font:800 clamp(2.4rem,7vw,4.6rem)/1.05 var(--display)}
.t5-tk .tr b{font:400 clamp(1rem,3vw,1.8rem) var(--pixel);margin-top:8px}
.t5-tk em{font-style:normal;font:700 clamp(1rem,2.4vw,1.4rem) var(--display);color:#B0306A}
.pt.out .t5-tk{animation:none;transform:translate(-50%,-50%) rotate(-3deg)}
.pt.out .t5-tk .tl{transform:translate(-40%,30%) rotate(-14deg);opacity:0}
.pt.out .t5-tk .tr{transform:translate(60%,-20%) rotate(22deg);opacity:0}
.t5-cu{position:absolute;top:0;bottom:0;width:50.5%;background:repeating-linear-gradient(90deg,#4A0710 0,#8E1422 3.2%,#C8243A 4.6%,#8E1422 6%,#4A0710 8%);box-shadow:inset 0 -60px 80px -20px rgba(0,0,0,.6);transition:transform .55s cubic-bezier(.7,0,.2,1)}
.t5-cu.l{left:0;transform:translateX(-100%)}.t5-cu.r{right:0;transform:translateX(100%)}
.pt.in .t5-cu{transform:none}
.pt.out .t5-cu{transition-duration:.9s;transition-delay:.05s}.pt.out .t5-cu.l{transform:translateX(-100%)}.pt.out .t5-cu.r{transform:translateX(100%)}
.t5-sp{position:absolute;left:50%;top:-10%;width:min(900px,120vw);height:110%;transform:translateX(-50%);background:radial-gradient(50% 60% at 50% 72%,rgba(255,236,180,.55),transparent 70%),conic-gradient(from 160deg at 50% 0,transparent 0deg,rgba(255,236,180,.28) 12deg,rgba(255,236,180,.28) 28deg,transparent 40deg);opacity:0;animation:fadeIn .4s .35s forwards;mix-blend-mode:screen}
.pt.out .t5-sp{animation:fadeOut .25s forwards;opacity:1}
.t5-d{position:absolute;width:var(--s);height:var(--s);border-radius:50%;background:#FFE6A0;box-shadow:0 0 8px #FFD24A;opacity:0;animation:t5d 1.2s var(--dl) ease-out forwards}
@keyframes t5d{30%{opacity:1}to{opacity:0;transform:translateY(-60px)}}
.t5-hof{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:grid;justify-items:center;gap:14px;opacity:0;animation:t5h .7s .38s cubic-bezier(.2,.8,.2,1) forwards;text-align:center}
.t5-hof small{font:400 clamp(.5rem,1.2vw,.72rem) var(--pixel);letter-spacing:.3em;color:#E8C877}
.t5-hof span{font:800 clamp(2.8rem,9vw,7.4rem)/1 var(--display);letter-spacing:.04em;white-space:nowrap;background:linear-gradient(100deg,#8A6A1E 0%,#F6DF9A 25%,#FFF6D6 35%,#C9A04A 50%,#F6DF9A 70%,#8A6A1E 100%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:t5shine 1.4s .4s linear forwards;filter:drop-shadow(0 6px 24px rgba(255,200,90,.35))}
@keyframes t5h{from{opacity:0;transform:translate(-50%,-40%) scale(.92);filter:blur(8px)}to{opacity:1;transform:translate(-50%,-50%);filter:none}}
@keyframes t5shine{from{background-position:120% 0}to{background-position:-60% 0}}
.pt.out .t5-hof{animation:fadeOut .3s forwards;opacity:1}
@media (max-width:1000px){.ac-up{grid-template-columns:minmax(0,1fr)}.sc-nav{grid-template-columns:repeat(2,minmax(0,1fr))}.afo-big,.dk-fan{opacity:.35;right:-6%;width:70%}}
@media (max-width:600px){.sl::after{background:linear-gradient(0deg,rgba(5,6,20,.9) 0%,rgba(5,6,20,.4) 60%,transparent)}.sl-c{left:20px;right:20px;bottom:24px}.sc-nav img{width:48px;height:40px}.sc-nav small{display:none}
  .cy-c{left:-80px;width:160px}.cy-st{perspective:1000px}.stk{display:none}.cab-b .lb{font-size:.7em;padding:.3em .45em}.afo-big{top:28%;right:50%;transform:translate(50%,-50%) rotate(-4deg);opacity:1;width:72%}.s-afo .afo-ic{display:none}.dk-fan{top:30%;opacity:1;right:10%;width:80%;height:55%}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v5.html','w').write(s)
print('v5 ok',len(s))
