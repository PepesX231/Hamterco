
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function el(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e}
  var W=[
    {n:'Mr. City',img:'',draw:1,w:'เกมเดินเที่ยวสงขลา แบบเดียวกับ Pokémon GO',d:[['ใครใช้','สวนสัตว์สงขลา'],['ใช้ยังไง','นักท่องเที่ยวเดินไปตามที่เที่ยวจริงในสงขลา แล้วเล่นเกมที่จุดนั้น'],['ผลลัพธ์','ขายได้แล้ว',1]]},
    {n:'PHC Map',img:'/Hamterco/img/w-hmap.webp',w:'เกมสอนเขียนโปรแกรม Python',d:[['ใครใช้','เด็กที่เริ่มเรียนเขียนโปรแกรม'],['ใช้ยังไง','เล่นผ่านด่านบนแผนที่ แต่ละด่านคือบทเรียน Python'],['ผลลัพธ์','ใช้สอนเด็กไปแล้วกว่า 1,000 คน',1]]},
    {n:'Hamster Quest',img:'/Hamterco/img/w-quest-town.webp',w:'เว็บเรียนที่เล่นเหมือนเกม',d:[['ใครใช้','น้องที่เรียนกับ Hamster Hub และมหาวิทยาลัยที่กำลังเตรียมนำไปใช้'],['ใช้ยังไง','ทำภารกิจ เก็บรางวัล และเรียนทีละขั้นเหมือนเล่นเกม'],['ผลลัพธ์','กำลังเตรียมใช้กับมหาวิทยาลัย',1]]},
    {n:'REVOICE',img:'/Hamterco/img/w-revoice.webp',w:'แอปฝึกพูดแบบเล่นเกม ของน้องไอดิน',d:[['ใครใช้','คนที่มีปัญหาด้านการพูด'],['ทำยังไง','น้องไอดินเขียนเองด้วย Unity ใน 4 เดือน'],['ผลลัพธ์','ชนะ NSC 2025',1]]},
    {n:'StressStrike',img:'/Hamterco/img/work-stressstrike.webp',w:'เกมที่น้องทำเองทั้งเกม',d:[['ผลลัพธ์','ชนะเลิศ OBEC Roboplayground',1]]}];
  var pad=function(i){return (i<9?'0':'')+(i+1)};

  function build(view){
    var tv=el('div','tv');tv.setAttribute('data-tv','1');
    /* intro */
    var it=el('section','tv-in');
    it.innerHTML='<div class="tv-fly" aria-hidden="true"></div><div class="tv-in-b"><h1 class="tv-glow"><span>เราพาน้องมัธยม</span><span>สร้างผลงาน</span><span>ที่มีคนใช้จริง</span></h1>'+
      '<p>ขายได้จริง ชนะเวทีระดับประเทศ และพาน้องเข้ามหาลัยที่ตั้งใจไว้ เราสอน พาสร้าง และพาลงเวทีจริง ตั้งแต่เกม เว็บ จนถึงแอป</p></div><div class="tv-fx"></div>';
    tv.appendChild(it);
    /* works */
    var ws=el('section','tv-w');ws.id='about-real';ws.style.height=(W.length*85+100)+'svh';
    var stk=el('div','tv-st');
    stk.innerHTML='<canvas class="tv-gl" aria-hidden="true"></canvas>'+
      '<div class="tv-ls"><h2>ผลงานที่มีคนใช้จริง</h2><p class="tv-m">เลือกดูทีละชิ้น หรือเลื่อนลง</p><ol>'+W.map(function(w,i){return '<li><button type="button" data-i="'+i+'">['+pad(i)+'] '+w.n+'</button><span class="ds">'+w.w+'<br><b>'+w.d[w.d.length-1][1]+'</b></span></li>'}).join('')+'</ol>'+
      '<div class="tv-fb">'+W.map(function(w){return '<div><img src="'+w.img+'" alt="'+w.n+'" loading="lazy"><b>'+w.n+'</b><span>'+w.w+'</span></div>'}).join('')+'</div></div>'+
      '<div class="tv-if" aria-live="polite"></div>'+
      '<div class="tv-ct tv-m"><span class="k">01</span><i><b></b></i><span>'+pad(W.length-1)+'</span></div><div class="tv-fx"></div>';
    ws.appendChild(stk);tv.appendChild(ws);
    /* numbers */
    var kn=el('section','tv-kn');
    var F=[['48 คน','รุ่นพี่ DEK69 ติดมหาลัยรอบ Portfolio','/Hamterco/img/dek69-8.webp'],['12 ผลงาน','เข้ารอบชิงชนะเลิศ NSC การแข่งขันเขียนโปรแกรมระดับประเทศ','/Hamterco/img/w-revoice.webp'],
           ['ชนะเลิศ','OBEC Roboplayground ด้วยเกม StressStrike','/Hamterco/img/work-stressstrike.webp'],['ขายได้จริง','เกม Mr. City ขายให้สวนสัตว์สงขลา','CITY'],['1,000+ คน','เด็กที่เรียนเขียน Python ผ่านเกม PHC Map','/Hamterco/img/w-hmap.webp']];
    kn.innerHTML='<h2>ผลงานของน้องๆ ปีที่ผ่านมา</h2><ul class="tv-kl">'+F.map(function(f){return '<li><span class="big" data-bg="'+f[2]+'">'+f[0]+'</span><img class="ph" data-src="'+f[2]+'" alt="" loading="lazy"><span class="cp">'+f[1]+'</span></li>'}).join('')+'</ul>';
    tv.appendChild(kn);
    /* channels */
    var ch=el('section','tv-ch');
    var C=[['01','/Hamterco/img/w-quest-town.webp','พาน้องสร้างสตาร์ทอัพ','เปลี่ยนไอเดียของน้องให้เป็นสินค้าจริง ทำกับเพื่อนๆ จนเป็นสตาร์ทอัพที่มีรายได้','#about-real','ดูผลงานที่มีคนใช้จริง'],
           ['02','/Hamterco/img/dek69-6.webp','พาเข้ามหาวิทยาลัย','คอร์สทำพอร์ต และซ้อมนำเสนอกับอาจารย์มหาวิทยาลัย ปี 2569 รุ่นพี่ติดรอบ Portfolio 48 คน','#works','ดูรุ่นพี่ที่ติดแล้ว'],
           ['03','/Hamterco/img/sc-revoice.webp','พาลงเวทีจริง','ค่าย Game Jam และการแข่งขันร่วมกับ สจล. ปีนี้ 12 ผลงานเข้ารอบชิง NSC','#activity','ดูกิจกรรม']];
    ch.innerHTML='<div class="tv-ch-in"><h2>เราทำ 3 อย่าง</h2><div class="tv-ch-g">'+C.map(function(c){return '<a class="tv-set" href="'+c[4]+'"><img src="'+c[1]+'" alt="" loading="lazy"><span class="tx"><h3>'+c[2]+'</h3><p>'+c[3]+'</p><em>'+c[5]+'</em></span></a>'}).join('')+'</div></div>';
    tv.appendChild(ch);
    /* photo wall */
    var rg=el('section','tv-rg'),P=[['team-group','ทีม Hamster Hub'],['photo-class','ในห้องเรียน'],['photo-group','ค่าย'],['photo-desk','ช่วงทำผลงาน'],['s-showcase1','วันโชว์ผลงาน'],['photo-camp','ค่าย Game Jam']];
    rg.innerHTML='<div class="tv-rg-h"><h2>บรรยากาศจริงในห้องเรียนและค่าย</h2><p>ลากเพื่อหมุนดู</p></div><div class="tv-rg-s"><div class="tv-rg-r">'+P.concat(P).map(function(p){return '<figure><img src="/Hamterco/img/'+p[0]+'.webp" alt="'+p[1]+'" decoding="async"><figcaption>'+p[1]+'</figcaption></figure>'}).join('')+'</div></div>';
    tv.appendChild(rg);
    var gr=el('div','tv-grain');gr.setAttribute('aria-hidden','true');tv.appendChild(gr);
    view.insertBefore(tv,view.firstChild);
    var old=view.querySelector('.ab-use#about-real');if(old)old.id='about-real-old';
    return tv}

  /* ---------- WebGL drum of curved CRT screens ---------- */
  var VS='attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  var FS=['precision highp float;uniform vec2 R;uniform float T,P,G,K;uniform sampler2D A,B,C;uniform vec3 AS;uniform float N;',
  'float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}',
  'vec3 tx(sampler2D s,vec2 uv,float asp,float ca,float sa){vec2 c=uv-.5;float k=.06;c*=1.+k*dot(c,c);uv=c+.5;',
  ' vec2 q=uv;if(asp>sa){q.x=(q.x-.5)*sa/asp+.5;}else{q.y=(q.y-.5)*asp/sa+.5;}',
  ' vec2 o=vec2(ca,0.);return vec3(texture2D(s,q+o).r,texture2D(s,q).g,texture2D(s,q-o).b);}',
  'float box(vec2 p,vec2 b,float r){vec2 d=abs(p)-b+r;return length(max(d,0.))+min(max(d.x,d.y),0.)-r;}',
  'void main(){vec2 fc=gl_FragCoord.xy;vec2 uv=(fc-.5*R)/R.y;float mob=step(R.x/R.y,1.);uv.x-=mix(.2,0.,mob);uv.y+=mix(0.,.2,mob);float ra=mix(-.2,-.1,mob);uv=mat2(cos(ra),sin(ra),-sin(ra),cos(ra))*uv;',
  ' float D=6.3,Rd=2.2;vec3 d=normalize(vec3(uv.x,uv.y,-1.55));',
  ' float gy=(h(vec2(floor(fc.y/5.),floor(T*24.)))-.5)*G*.025;d.x+=gy;',
  ' vec2 q=vec2(0.,D),dq=d.yz;float a=dot(dq,dq),b=2.*dot(q,dq),c=dot(q,q)-Rd*Rd,dis=b*b-4.*a*c;',
  ' vec3 col=vec3(.07,.055,.045);',
  ' if(dis>0.){float t=(-b-sqrt(dis))/(2.*a);vec3 hp=d*t;float th=-atan(hp.y,hp.z+D);float S=mix(.86,.46,mob),H=mix(.7,.34,mob);float an=th+P*S;',
  '  float k=floor(an/S+.5);float v=.5-(an-k*S)/H;float Wd=mix(2.3,1.1,mob);float u=hp.x/Wd+.5;float sa=Wd/(Rd*H);',
  '  float lit=.35+.65*cos(th*1.6);',
  '  if(k>=0.&&k<N){vec2 sp=vec2(u-.5,v-.5)*vec2(sa,1.);float bd=box(sp,vec2(sa*.5,.5),.06);',
  '   if(bd<0.){float ca=.0015+.002*length(sp)+G*.003;vec3 s;vec2 tu=vec2(u,1.-v);',
  '    if(k==K-1.)s=tx(A,tu,AS.x,ca,sa);else if(k==K)s=tx(B,tu,AS.y,ca,sa);else if(k==K+1.)s=tx(C,tu,AS.z,ca,sa);else s=vec3(.1);',
  '    float vg=smoothstep(-.0,-.12,bd);s*=mix(.55,1.,vg);s*=.95+.05*sin(fc.y*2.1);',
  '    s+=vec3(1.,.7,.4)*.05*(1.-vg);col=s*lit;}',
  '   else if(bd<.035){col=mix(vec3(.16,.12,.09),vec3(.07,.055,.045),bd/.035)*lit;}}}',
  ' vec3 bg=vec3(.0706,.0549,.0431);float sc=step(.0001,distance(col,vec3(.07,.055,.045)));float vgn=1.-.55*dot(uv*.7,uv*.7);col=mix(bg,(col+(h(fc)-.5)*.05)*vgn,sc);float ef=smoothstep(0.,.14*R.y,fc.y)*smoothstep(0.,.14*R.y,R.y-fc.y);col=mix(bg,col,ef);gl_FragColor=vec4(col,1.);}'].join('\n');
  /* Mr. City has no screenshot: draw its map card (same look the old page used) */
  function city(){var c=document.createElement('canvas');c.width=1280;c.height=760;var x=c.getContext('2d');
    x.fillStyle='#1F6249';x.fillRect(0,0,1280,760);x.strokeStyle='rgba(255,255,255,.09)';x.lineWidth=2;
    x.save();x.translate(640,380);x.rotate(-.18);for(var i=-1200;i<1200;i+=80){x.beginPath();x.moveTo(i,-900);x.lineTo(i,900);x.stroke();x.beginPath();x.moveTo(-1200,i);x.lineTo(1200,i);x.stroke()}x.restore();
    x.strokeStyle='rgba(255,246,232,.35)';x.lineWidth=10;x.setLineDash([2,22]);x.lineCap='round';x.beginPath();x.moveTo(300,330);x.bezierCurveTo(480,180,640,420,760,300);x.bezierCurveTo(860,200,980,260,1010,230);x.stroke();x.setLineDash([]);
    function pin(px,py,col){x.fillStyle=col;x.beginPath();x.arc(px,py,30,Math.PI,0);x.lineTo(px,py+52);x.closePath();x.fill();x.fillStyle='#1F6249';x.beginPath();x.arc(px,py,12,0,7);x.fill()}
    pin(300,300,'#F7C948');pin(760,270,'#FFF6E8');pin(1010,200,'#F7C948');
    x.fillStyle='#FFF6E8';x.font='800 120px Anuphan, sans-serif';x.fillText('Mr. City',200,610);x.font='600 44px Anuphan, sans-serif';x.globalAlpha=.8;x.fillText('สงขลา',206,680);
    return c}
  function drum(ws){
    var cv=ws.querySelector('.tv-gl'),gl=cv.getContext('webgl',{antialias:false,premultipliedAlpha:false});
    if(!gl){ws.closest('.tv').classList.add('tv-nogl');return null}
    function sh(t,s){var o=gl.createShader(t);gl.shaderSource(o,s);gl.compileShader(o);if(!gl.getShaderParameter(o,gl.COMPILE_STATUS)){console.warn(gl.getShaderInfoLog(o));return null}return o}
    var pr=gl.createProgram(),v=sh(gl.VERTEX_SHADER,VS),f=sh(gl.FRAGMENT_SHADER,FS);if(!v||!f){ws.closest('.tv').classList.add('tv-nogl');return null}
    gl.attachShader(pr,v);gl.attachShader(pr,f);gl.linkProgram(pr);gl.useProgram(pr);
    var bf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,bf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),gl.STATIC_DRAW);
    var lp=gl.getAttribLocation(pr,'p');gl.enableVertexAttribArray(lp);gl.vertexAttribPointer(lp,2,gl.FLOAT,false,0,0);
    var U={};['R','T','P','G','K','A','B','C','AS','N'].forEach(function(n){U[n]=gl.getUniformLocation(pr,n)});
    gl.uniform1i(U.A,0);gl.uniform1i(U.B,1);gl.uniform1i(U.C,2);gl.uniform1f(U.N,W.length);
    var tex=[],asp=[],blank=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,blank);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,1,1,0,gl.RGBA,gl.UNSIGNED_BYTE,new Uint8Array([20,16,12,255]));
    W.forEach(function(w,i){tex[i]=blank;asp[i]=1.42;var im=w.draw?city():new Image();im.onload=function(){var t=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,t);
      gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,im);['TEXTURE_WRAP_S','TEXTURE_WRAP_T'].forEach(function(k){gl.texParameteri(gl.TEXTURE_2D,gl[k],gl.CLAMP_TO_EDGE)});
      gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);tex[i]=t;asp[i]=im.width/im.height;dirty=1;if(ws.__kick)ws.__kick()};if(w.draw)im.onload();else im.src=w.img});
    var dirty=1;
    return {dirty:function(){return dirty},draw:function(t,p,g){dirty=0;var dpr=1,w=cv.clientWidth,h=cv.clientHeight;if(!w)return;
        if(cv.width!==Math.round(w*dpr)){cv.width=Math.round(w*dpr);cv.height=Math.round(h*dpr)}gl.viewport(0,0,cv.width,cv.height);
        var k=Math.round(p);[k-1,k,k+1].forEach(function(j,s){gl.activeTexture(gl.TEXTURE0+s);gl.bindTexture(gl.TEXTURE_2D,tex[j]||blank)});
        gl.uniform3f(U.AS,asp[k-1]||1.42,asp[k]||1.42,asp[k+1]||1.42);gl.uniform2f(U.R,cv.width,cv.height);gl.uniform1f(U.T,t);gl.uniform1f(U.P,p);gl.uniform1f(U.G,g);gl.uniform1f(U.K,k);
        gl.drawArrays(gl.TRIANGLES,0,3)}}}

  /* ---------- static noise for channel sets and the page grain ---------- */
  function noise(cv,s){var w=cv.width=s,h=cv.height=Math.round(s*.75),cx=cv.getContext('2d'),im=cx.createImageData(w,h);
    return function(){var d=im.data;for(var i=0;i<d.length;i+=4){var v=Math.random()*255|0;d[i]=d[i+1]=d[i+2]=v;d[i+3]=255}cx.putImageData(im,0,0)}}

  function run(tv){
    var view=tv.parentNode,ws=tv.querySelector('.tv-w'),ifo=ws.querySelector('.tv-if'),lis=[].slice.call(ws.querySelectorAll('.tv-ls li')),bar=ws.querySelector('.tv-ct b'),kk=ws.querySelector('.tv-ct .k');
    var dr=drum(ws),tgt=0,cur=0,shown=-1,g=0,raf=0,vis=false;
    function info(i){var w=W[i];ifo.innerHTML='<p class="n tv-glow">'+w.n+'</p><p class="w">'+w.w+'</p><dl>'+w.d.map(function(r){return '<dt>'+r[0]+'</dt><dd'+(r[2]?' class="r"':'')+'>'+r[1]+'</dd>'}).join('')+'</dl>';
      ifo.classList.remove('sw');void ifo.offsetWidth;ifo.classList.add('sw');lis.forEach(function(l,j){l.classList.toggle('on',j===i)});kk.textContent=pad(i)}
    function prog(){var r=ws.getBoundingClientRect(),sp=ws.offsetHeight-innerHeight;return Math.max(0,Math.min(W.length-1,(-r.top)/Math.max(1,sp)*(W.length-1)))}
    function frame(t){raf=0;if(!vis||!view.offsetParent)return;tgt=prog();cur+=(tgt-cur)*(rm?1:.12);if(Math.abs(tgt-cur)<.0005)cur=tgt;
      var k=Math.round(cur);if(k!==shown){shown=k;info(k);g=rm?0:1}g*=.9;
      bar.style.transform='scaleX('+(cur/(W.length-1))+')';
      var mv=tgt!==cur||g>.01||(dr&&dr.dirty());if(dr&&mv)dr.draw(t/1000,cur,g);if(!mv){raf=0;return}raf=requestAnimationFrame(frame)}
    function kick(){if(!raf&&vis)raf=requestAnimationFrame(frame)}ws.__kick=kick;
    new IntersectionObserver(function(es){vis=es[0].isIntersecting;kick()}).observe(ws);
    addEventListener('scroll',kick,{passive:true});addEventListener('resize',kick);
    lis.forEach(function(l,i){l.querySelector('button').addEventListener('click',function(){var top=ws.getBoundingClientRect().top+scrollY,sp=ws.offsetHeight-innerHeight;scrollTo({top:top+sp*i/(W.length-1)+2,behavior:rm?'auto':'smooth'})})});
    info(0);
    /* power-on when the page opens */
    function on(){if(!view.offsetParent)return;view.classList.add('tv-live');if(rm)return;tv.classList.remove('tv-on');void tv.offsetWidth;tv.classList.add('tv-on')}
    addEventListener('hashchange',function(){setTimeout(on,30)});on();
    /* intro: works fly toward the viewer */
    var fly=tv.querySelector('.tv-fly'),FI=['w-hmap','w-quest-town','w-revoice','work-stressstrike','sc-lyno','sc-timekeeper','sc-zoo','work-slash-speed','work-hot-hot-hot','work-escape-rolling','w-quest-app','work-midnight-at-roadside','work-beyond-the-board','s-showcase2'],
        cards=FI.map(function(n,i){var c=el('i');c.style.backgroundImage='url(/Hamterco/img/'+n+'.webp)';fly.appendChild(c);
          var a=i*2.399,r=.55+((i*37)%10)/10*.55;return {e:c,x:Math.cos(a)*r,y:Math.sin(a)*r*.62,z:-(i/FI.length)*2600}}),
        fv=false,fr=0,mx=0,my=0,last=0;
    function flyF(t){fr=0;if(!fv||!view.offsetParent)return;var dt=Math.min(50,t-(last||t));last=t;var W=fly.clientWidth,H=fly.clientHeight;
      cards.forEach(function(c){if(!rm)c.z+=dt*.09;if(c.z>500)c.z-=2600;var o=c.z<-2200?(c.z+2600)/400:c.z>250?Math.max(0,(500-c.z)/250):1;
        c.e.style.opacity=o.toFixed(3);c.e.style.transform='translate3d('+(c.x*W*.62-mx*40).toFixed(1)+'px,'+(c.y*H*.7-my*30).toFixed(1)+'px,'+c.z.toFixed(1)+'px) rotateY('+(-c.x*16).toFixed(1)+'deg)'});
      fr=requestAnimationFrame(flyF)}
    new IntersectionObserver(function(es){fv=es[0].isIntersecting;last=0;if(fv&&!fr)fr=requestAnimationFrame(flyF)}).observe(fly);
    tv.querySelector('.tv-in').addEventListener('pointermove',function(e){mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5},{passive:true});
    /* numbers: photo fill + reveal */
    var cityURL=null;tv.querySelectorAll('.tv-kl li').forEach(function(li){var b=li.querySelector('.big'),p=li.querySelector('.ph'),src=b.dataset.bg;
      if(src==='CITY'){cityURL=cityURL||city().toDataURL('image/jpeg',.85);src=cityURL}p.src=src});
    var kio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');kio.unobserve(e.target)}})},{threshold:.25});
    tv.querySelectorAll('.tv-kl li').forEach(function(l){kio.observe(l)});
    /* picture cards lean toward the pointer */
    if(!rm&&matchMedia('(hover:hover)').matches)tv.querySelectorAll('.tv-set').forEach(function(s){
      s.addEventListener('pointermove',function(e){var r=s.getBoundingClientRect(),u=(e.clientX-r.left)/r.width-.5,v=(e.clientY-r.top)/r.height-.5;s.style.transform='rotateY('+(u*10).toFixed(2)+'deg) rotateX('+(-v*8).toFixed(2)+'deg) translateY(-6px)'});
      s.addEventListener('pointerleave',function(){s.style.transform=''})});
    /* curved photo wall: spins slowly, drag to turn */
    var st=tv.querySelector('.tv-rg-s'),ring=st.querySelector('.tv-rg-r'),figs=[].slice.call(ring.children),N=figs.length,step=360/N,rot=0,vel=0,down=false,px=0,rv=false,rr=0,Rr=0,Zr=0;
    function lay(){var w=st.clientWidth,Wp=Math.min(520,w*(w<640?.66:.4)),Hp=Wp*.68;Rr=Wp/(2*Math.tan(Math.PI/N))*1.06;Zr=Rr-Math.max(120,Rr*.16);
      figs.forEach(function(f,i){f.style.width=Wp+'px';f.style.height=Hp+'px';f.style.left=-Wp/2+'px';f.style.top=-Hp/2+'px'})}
    var lw=0;
    /* the About view can be built while hidden (width 0): re-measure the photos as soon as it has a real width */
    function ringF(){rr=0;if(!rv||!view.offsetParent)return;if(st.clientWidth&&st.clientWidth!==lw){lw=st.clientWidth;lay()}if(!down){if(!rm)rot-=.035;rot+=vel;vel*=.94}
      ring.style.transform='translateZ('+Zr.toFixed(1)+'px) rotateY('+rot.toFixed(2)+'deg)';
      figs.forEach(function(f,i){var a=i*step,d=((rot-a)%360+540)%360-180,v=Math.abs(d)<78;f.style.visibility=v?'visible':'hidden';
        if(v){f.style.transform='rotateY('+(-a)+'deg) translateZ('+(-Rr).toFixed(1)+'px)'}});
      rr=requestAnimationFrame(ringF)}
    lay();addEventListener('resize',lay);
    /* place every photo once up front, so the ring is never an empty black box while waiting for its first frame */
    figs.forEach(function(f,i){var a=i*step,d=((rot-a)%360+540)%360-180;f.style.visibility=Math.abs(d)<78?'visible':'hidden';f.style.transform='rotateY('+(-a)+'deg) translateZ('+(-Rr).toFixed(1)+'px)'});
    ring.style.transform='translateZ('+Zr.toFixed(1)+'px) rotateY(0deg)';
    /* the loop could stop for good if it ran once while the About view was still hidden; any later scroll or view change restarts it */
    function kickR(){if(rv&&!rr)rr=requestAnimationFrame(ringF)}
    new IntersectionObserver(function(es){rv=es[0].isIntersecting;kickR()},{rootMargin:'300px 0px'}).observe(st);
    addEventListener('scroll',kickR,{passive:true});addEventListener('hashchange',function(){setTimeout(function(){lay();kickR()},60)});
    st.addEventListener('pointerdown',function(e){down=true;px=e.clientX;vel=0;st.classList.add('drag')});
    addEventListener('pointermove',function(e){if(!down)return;var dx=e.clientX-px;px=e.clientX;rot-=dx*.09;vel=-dx*.09});
    addEventListener('pointerup',function(){down=false;st.classList.remove('drag')});
    /* grain */
    var gc=document.createElement('canvas'),gp=noise(gc,220);gp();tv.querySelector('.tv-grain').style.backgroundImage='url('+gc.toDataURL()+')';
  }

  function go(){var v=document.querySelector('[data-view="about"]');if(!v||v.querySelector('.tv'))return;run(build(v))}
  if(document.readyState==='complete')go();else addEventListener('load',go);
})();
