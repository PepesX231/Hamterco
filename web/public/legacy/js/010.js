
(function(){
  var zq=document.querySelector('[data-view="home"] .zq');if(!zq)return;
  var sw=zq.querySelector('.zq-sw'),form=zq.querySelector('#zqForm'),top=zq.querySelector('.zq-top');
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* ---------- glow ring around the search ---------- */
  var gw=document.createElement('span'),gr=document.createElement('span');gw.className='hx-gw';gr.className='hx-gr';
  if(sw&&form){sw.insertBefore(gw,sw.firstChild);sw.insertBefore(gr,sw.firstChild)}
  function ring(){if(!form)return;var l=form.offsetLeft,t=form.offsetTop,w=form.offsetWidth,h=form.offsetHeight;
    gr.style.cssText='left:'+(l-2.5)+'px;top:'+(t-2.5)+'px;width:'+(w+5)+'px;height:'+(h+5)+'px';
    gw.style.cssText='left:'+(l-6)+'px;top:'+(t-4)+'px;width:'+(w+12)+'px;height:'+(h+8)+'px'}
  ring();addEventListener('resize',ring);if(window.ResizeObserver&&form)new ResizeObserver(ring).observe(form);

  /* ---------- glyph wave field ---------- */
  var cv=document.createElement('canvas');cv.className='hx-cv';cv.setAttribute('aria-hidden','true');zq.insertBefore(cv,zq.firstChild);
  var cx=cv.getContext('2d'),G=[],atlas,cw,ch,dpr,W,H,cols,rows,mx=-1e4,my=-1e4,rip=[],box;
  var atlasW;
  /* the sea is made of real code (games, web, IoT, robots), not maths symbols */
  for(var gi=33;gi<127;gi++)G.push(String.fromCharCode(gi));
  var CODE=window.HXCODE=['function jump(){ player.vy = -12; }   if (coin.hit(player)) score += 10;',
    '<button onclick="startGame()">PLAY</button>   <h1>My First Website</h1>',
    'void Update(){ if (Input.GetKeyDown("space")) Jump(); }',
    'digitalWrite(LED, HIGH); delay(500); digitalWrite(LED, LOW);',
    'for i in range(10): print("Hello, Hamster Hub")',
    'const robot = new Robot(); robot.forward(50); robot.turn(90);',
    'while (alive) { move(); draw(); checkHit(); }',
    'let hp = 100; let level = 1; if (hp <= 0) gameOver();',
    '.card { border-radius: 16px; color: orange; }',
    'int sensor = analogRead(A0); if (sensor > 512) buzzer.on();',
    'class Player : MonoBehaviour { public float speed = 5f; }',
    'fetch("/api/score").then(r => r.json()).then(show);'],rowC=[];
  function mkRows(){rowC=[];for(var j=0;j<rows;j++){var t=CODE[(j*5)%CODE.length]+'    ',a=new Uint8Array(cols),o=(j*13)%t.length;for(var i=0;i<cols;i++)a[i]=t.charCodeAt((i+o)%t.length);rowC.push(a)}}
  function mk(col){var c=document.createElement('canvas');c.width=G.length*cw*dpr;c.height=ch*dpr;var a=c.getContext('2d');a.scale(dpr,dpr);
    a.font='600 '+(ch*.78)+'px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace';a.textAlign='center';a.textBaseline='middle';a.fillStyle=col;
    G.forEach(function(g,i){a.fillText(g,i*cw+cw/2,ch/2+1)});return c}
  function mkAtlas(){atlas=mk('#8A3A00');atlasW=mk('#E07B1E')}
  function size(){W=zq.clientWidth;H=zq.clientHeight;dpr=Math.min(devicePixelRatio||1,W<640?1:1.5);var mob=W<640;cw=mob?7:8;ch=mob?13:15;
    cv.width=W*dpr;cv.height=H*dpr;cols=Math.ceil(W/cw);rows=Math.ceil(H/ch);mkAtlas();mkRows();
    var r=zq.getBoundingClientRect(),h1=top.querySelector('.zq-h')||top,a=h1.getBoundingClientRect(),b=(form||h1).getBoundingClientRect();
    box={x:(Math.min(a.left,b.left)+Math.max(a.right,b.right))/2-r.left,y:(a.top+b.bottom)/2-r.top,rx:Math.max(a.width,b.width)*.5+(W<640?6:40),ry:(b.bottom-a.top)*.5+(W<640?24:46)}}
  /* gather: when the search is used, the glyph sea flows in and hugs the search bar (and the results panel) */
  var gat=0,inp=zq.querySelector('#zqIn'),resEl=zq.querySelector('#zqRes'),zr;
  function rr(px,py,b){var qx=Math.abs(px-b.cx)-b.hw+b.r,qy=Math.abs(py-b.cy)-b.hh+b.r;
    return Math.min(Math.max(qx,qy),0)+Math.hypot(Math.max(qx,0),Math.max(qy,0))-b.r}
  function target(){var r=zq.getBoundingClientRect(),f=form.getBoundingClientRect(),l=f.left,t=f.top,R=f.right,B=f.bottom;
    if(resEl&&!resEl.hidden&&zq.classList.contains('ask')){var q=resEl.getBoundingClientRect();if(q.height){l=Math.min(l,q.left);R=Math.max(R,q.right);B=Math.max(B,q.bottom)}}
    return{cx:(l+R)/2-r.left,cy:(t+B)/2-r.top,hw:(R-l)/2,hh:(B-t)/2,r:Math.min(30,(B-t)/2)}}
  function frame(t){if(zq.clientWidth!==W||zq.clientHeight!==H){if(!zq.clientWidth)return;size()}
    t/=1000;cx.setTransform(1,0,0,1,0,0);cx.clearRect(0,0,cv.width,cv.height);
    var n=G.length,now=performance.now();rip=rip.filter(function(p){return now-p.t<2600});
    var gt=0;/* owner: the glyph sea stays as it is while searching */gat+=(gt-gat)*(rm?1:.07);if(Math.abs(gt-gat)<.002)gat=gt;
    var S=window.HXSlime,sp=S&&typeof S.p==='number'?Math.max(0,Math.min(1,S.p)):0,rim=S&&S.rim?S.rim:0;
    var ge=gat*gat*(3-2*gat),tb=(ge>.003||sp>.003)&&form?target():null,far=Math.max(W,H)*.75,r0=10+rim*sp+(1-ge)*far,wd=16+(1-ge)*70,clr=6+rim*sp;
    var B1=W<640?.2:.36;
    /* the two bands only depend on the column: work them out once per frame */
    if(!frame.Y||frame.Y.length!==cols*4)frame.Y=new Float32Array(cols*4);var YB=frame.Y;
    for(var c0=0;c0<cols;c0++){var u0=(c0*cw+cw/2)/W;YB[c0*4]=B1+.1*Math.sin(u0*5.2+t*.55)+.035*Math.sin(u0*13-t*.9);YB[c0*4+1]=.085+.035*Math.sin(u0*3.4+t*.4);
      YB[c0*4+2]=.68+.08*Math.sin(u0*4.1-t*.45+1.7)+.03*Math.sin(u0*11+t*.7);YB[c0*4+3]=.065+.03*Math.sin(u0*2.6-t*.5+.6)}
    var lastA=-1;
    for(var j=0;j<rows;j++){var y=j*ch+ch/2,v=y/H,RC=rowC[j];if(!RC)continue;
      for(var i=0;i<cols;i++){var cc=RC[i];if(cc===32)continue;var x=i*cw+cw/2,u=x/W;
        /* two drifting bands, like a slow sea */
        var ex=(x-box.x)/box.rx,ey=(y-box.y)/box.ry,m=ex*ex+ey*ey;if(m<1&&!tb)continue;m=Math.sqrt(m);
        var y1=YB[i*4],t1=YB[i*4+1],y2=YB[i*4+2],t2=YB[i*4+3],q1=(v-y1)/t1,q2=(v-y2)/t2;if(q1*q1>9&&q2*q2>9&&!rip.length&&!tb&&((x-mx)*(x-mx)+(y-my)*(y-my))>40000)continue;
        var d=Math.exp(-Math.pow((v-y1)/t1,2))+.8*Math.exp(-Math.pow((v-y2)/t2,2));
        d*=.72+.28*Math.sin(x*.21+y*.13+t*1.6)*Math.sin(x*.05-t*.7+y*.02);
        /* pointer lifts the sea a little */
        var px=x-mx,py=y-my,pd=px*px+py*py;if(pd<40000)d+=.55*Math.exp(-pd/9000);
        /* ripples */
        for(var k=0;k<rip.length;k++){var p=rip[k],e=(now-p.t)/1000,R=e*p.v,dx=(x-p.x),dy=(y-p.y)*2.6,dd=Math.sqrt(dx*dx+dy*dy);
          d+=p.s*Math.exp(-Math.pow((dd-R)/34,2))*Math.max(0,1-e/p.life)}
        /* keep the headline and search clear */
        d*=m<1?0:m<1.5?(m-1)*2:1;
        if(tb){var sd=rr(x,y,tb);if(sd<clr)d*=sd<6?1-Math.max(ge,sp):1-sp;else{var an=Math.atan2((y-tb.cy)*1.6,x-tb.cx),
            hug=Math.exp(-Math.pow((sd-r0)/wd,2))*(.8+.35*Math.sin(an*9-t*2.4+sd*.05))+.55*Math.exp(-Math.pow((sd-r0-46)/(wd*1.6),2))*(.6+.4*Math.sin(an*5+t*1.3));
            d=d*(1-ge*.85)+hug*Math.min(1,ge*1.6)*(1-.45*sp)}}
        if(d<.2)continue;var g=cc-33;
        var al=Math.round(Math.min(.7,.1+d*.42)*20)/20;
        if(sp<.98){var A=al*(1-sp);if(A!==lastA){cx.globalAlpha=A;lastA=A}cx.drawImage(atlas,g*cw*dpr,0,cw*dpr,ch*dpr,i*cw*dpr,j*ch*dpr,cw*dpr,ch*dpr)}
        if(sp>.02){lastA=-1;cx.globalAlpha=al*sp*.9;cx.drawImage(atlasW,g*cw*dpr,0,cw*dpr,ch*dpr,i*cw*dpr,j*ch*dpr,cw*dpr,ch*dpr)}}}
    cx.globalAlpha=1}
  var run=false,last=0;
  function loop(t){if(!run)return;requestAnimationFrame(loop);if(t-last<66||document.hidden||(window.__scr&&t-window.__scr<160))return;last=t;frame(t)}
  function start(){size();cv.classList.add('on');if(rm){frame(0);return}
    new IntersectionObserver(function(es){var v=es[0].isIntersecting;if(v&&!run){run=true;requestAnimationFrame(loop)}else if(!v)run=false}).observe(zq)}
  addEventListener('resize',function(){size();if(rm)frame(0)});
  if(!rm)zq.addEventListener('pointermove',function(e){var r=zq.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top},{passive:true});
  zq.addEventListener('pointerleave',function(){mx=my=-1e4});

  /* ---------- ripples: rings on the surface that push through the glyph sea ---------- */
  function rings(x,y,sz,n){var o=window.HXSlime&&HXSlime.p>.5;for(var k=0;k<n;k++){(function(k){var r=document.createElement('i');r.className='hx-ring'+(o?' o':'');r.style.left=x+'px';r.style.top=y+'px';zq.appendChild(r);
      var s=sz*(1-k*.2);
      r.style.width=s+'px';r.style.height=(s*.3)+'px';r.style.willChange='transform,opacity';
      r.animate([{transform:'translate(-50%,-50%) scale('+(10/s).toFixed(3)+','+(4/(s*.3)).toFixed(3)+')',opacity:.95},{transform:'translate(-50%,-50%) scale(1)',opacity:0}],{duration:1800+k*220,delay:k*180,easing:'cubic-bezier(.15,.6,.3,1)',fill:'both'}).onfinish=function(){r.remove()}})(k)}
    rip.push({x:x,y:y,t:performance.now(),v:sz*.3,s:1.05,life:2.4})}
  form&&form.querySelector('.zq-go')&&form.querySelector('.zq-go').addEventListener('pointerdown',function(){if(rm)return;var r=zq.getBoundingClientRect(),b=this.getBoundingClientRect();rings(b.left+b.width/2-r.left,b.top+b.height/2-r.top,420,2)});
  /* every few seconds a ripple opens somewhere on the sea (never on the headline or search) */
  var amb=0;
  function ambient(){clearTimeout(amb);amb=setTimeout(ambient,2600+Math.random()*1800);
    if(rm||!run||document.hidden||!W||!box)return;
    for(var tries=0;tries<12;tries++){var x=W*(.06+Math.random()*.88),y=H*(.14+Math.random()*.72),ex=(x-box.x)/(box.rx+60),ey=(y-box.y)/(box.ry+50);
      if(ex*ex+ey*ey>1.2&&!(y>box.y&&Math.abs(x-W/2)<(W<640?W:300))){rings(x,y,(W<640?320:520)+Math.random()*200,0);return}}}
  /* typing: each key sends a small ripple out of the caret */
  var mc=document.createElement('canvas').getContext('2d');
  inp&&inp.addEventListener('input',function(){if(rm)return;var r=zq.getBoundingClientRect(),ir=inp.getBoundingClientRect(),cs=getComputedStyle(inp);mc.font=cs.font;
    var tw=Math.min(ir.width-8,mc.measureText(inp.value.slice(0,inp.selectionStart==null?inp.value.length:inp.selectionStart)).width);
    rip.push({x:ir.left-r.left+tw,y:ir.top-r.top+ir.height/2,t:performance.now(),v:300,s:.8,life:1.3})});
  /* results: titles decode out of the same code glyphs */
  var seg=window.Intl&&Intl.Segmenter?new Intl.Segmenter('th',{granularity:'grapheme'}):null,GL='{}<>+=-:#';
  function parts(t){return seg?Array.from(seg.segment(t),function(x){return x.segment}):Array.from(t)}
  function decode(el,delay){if(el.dataset.hxa||el.dataset.hxd===el.textContent)return;el.dataset.hxa='1';var txt=el.textContent,P=parts(txt),n=P.length,t0=0,dur=Math.min(700,260+n*22);
    el.dataset.hxd=txt;el.setAttribute('aria-label',txt);
    function step(ts){if(!t0)t0=ts;var k=Math.min(1,(ts-t0-delay)/dur);if(k<0){requestAnimationFrame(step);return}
      var shown=Math.floor(k*n),out=P.slice(0,shown).join('');
      for(var i=shown;i<n;i++)out+=P[i]===' '?' ':GL[(Math.random()*GL.length)|0];
      if(!el.isConnected){delete el.dataset.hxa;return}el.textContent=k>=1?txt:out;if(k<1)requestAnimationFrame(step);else{delete el.dataset.hxa;el.removeAttribute('aria-label')}}
    requestAnimationFrame(step)}
  if(resEl&&!rm){var dq=0;new MutationObserver(function(){clearTimeout(dq);dq=setTimeout(function(){if(resEl.hidden)return;var k=0;
      resEl.querySelectorAll('h3,h4,.zq-g b,.zq-g strong').forEach(function(el){if(el.children.length||!el.textContent.trim()||el.textContent.length>60)return;decode(el,k++*70)})},30)}).observe(resEl,{childList:true,subtree:true})}
  /* follow the slime layer: white state */
  addEventListener('hx-slime',function(e){zq.classList.toggle('hx-white',!!(e.detail&&e.detail.active))});

  function go(){start();cv.classList.add('on');ambient()}
  if(document.readyState==='complete')go();else addEventListener('load',go);
  addEventListener('hashchange',function(){if(/^#?(home)?$/.test(location.hash.replace('#','')||'home'))setTimeout(function(){size();ring()},350)});
})();
