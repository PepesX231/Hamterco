
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* glossy slime: a strip under the hero, a cap on each card */
  function drip(zq){var r=parseFloat(getComputedStyle(zq).borderBottomLeftRadius)||40,m=parseFloat(getComputedStyle(zq).marginLeft)||0,
      b=document.createElement('div'),i=document.createElement('i');b.className='je';i.style.left=m+'px';i.style.right=m+'px';b.appendChild(i);zq.after(b)}
  function cap(box,small){if(!box||box.querySelector(':scope > .cap'))return;var c=document.createElement('i');c.className='cap'+(small?' s':'');c.setAttribute('aria-hidden','true');
      c.style.setProperty('--cx',-Math.round(Math.random()*300)+'px');box.insertBefore(c,box.firstChild)}

  /* the one hero hamster: tap empty space, a sunflower seed drops, the hamster comes to eat it */
  var busy=false,seeds=[],tip;
  function seedSvg(){var d=document.createElementNS('http://www.w3.org/2000/svg','svg');d.setAttribute('class','seed');d.setAttribute('viewBox','-8 -10 16 20');
    d.innerHTML='<path d="M0 -9C5 -9 7 -2 6 3C5 8 2 10 0 10C-2 10 -5 8 -6 3C-7 -2 -5 -9 0 -9Z" fill="#3A332D"/><path d="M-2 -6C-3 -1 -3 4 -1.5 8M2 -6C3 -1 3 4 1.5 8" stroke="#EDE6DA" stroke-width="1.3" fill="none" stroke-linecap="round"/>';return d}
  function feed(zq,cx,cy){
    var sw=zq.querySelector('.zq-sw'),form=zq.querySelector('.zq-s');if(!sw||!form||seeds.length>3)return;
    var r=sw.getBoundingClientRect(),sx=cx-r.left,sy=cy-r.top,tx=Math.max(40,Math.min(sw.clientWidth-40,sx)),ty=form.offsetTop-6,s=seedSvg();
    s.style.left=sx+'px';s.style.top=sy+'px';sw.appendChild(s);
    var dur=Math.max(420,Math.min(900,Math.sqrt(Math.abs(ty-sy))*42)),rot=(Math.random()<.5?-1:1)*(240+Math.random()*200);
    s.animate([{transform:'translate(0,0) rotate(0)'},{transform:'translate('+(tx-sx)+'px,'+(ty-sy)+'px) rotate('+rot+'deg)',offset:.8},{transform:'translate('+(tx-sx)+'px,'+(ty-sy-7)+'px) rotate('+(rot+20)+'deg)',offset:.9},{transform:'translate('+(tx-sx)+'px,'+(ty-sy)+'px) rotate('+(rot+30)+'deg)'}],{duration:dur,easing:'cubic-bezier(.45,0,.9,.6)',fill:'forwards'});
    seeds.push({el:s,x:tx});if(tip)tip.classList.remove('on');try{localStorage.setItem('hhFed','1')}catch(e){}
    setTimeout(next,dur+60);
  }
  function next(){
    if(busy||!seeds.length)return;var sd=seeds[0],h=document.getElementById('zqHam'),sw=h&&h.parentNode,img=h&&h.querySelector('img');if(!h)return;busy=true;
    if(!h.dataset.home)h.dataset.home=getComputedStyle(h).right;var W=h.offsetWidth,right=Math.round(sw.clientWidth-sd.x-W/2),old=h.dataset.home;
    h.style.setProperty('transition','right .55s cubic-bezier(.5,0,.3,1),transform .45s cubic-bezier(.3,1.6,.5,1)','important');
    h.style.setProperty('right',right+'px','important');h.classList.add('up','watch');
    setTimeout(function(){
      sd.el.animate([{opacity:1},{opacity:0}],{duration:160,fill:'forwards'});setTimeout(function(){sd.el.remove()},180);seeds.shift();
      if(img){img.dataset.src=img.dataset.src||img.getAttribute('src');img.src='/Hamterco/img/ham-happy.webp'}h.classList.add('chew');
      setTimeout(function(){h.classList.remove('chew');if(img)img.src=img.dataset.src;h.classList.remove('watch');busy=false;if(seeds.length)next();
        else setTimeout(function(){if(!busy&&!seeds.length){h.style.setProperty('right',old,'important')}},500)},1100);
    },600);
  }


  /* ================= drawn faces: brush strokes and wobbly ink shapes, not geometry ================= */
  var NS='http://www.w3.org/2000/svg',INK='#1D1712';
  function rnd(seed){return function(){seed=(seed*16807)%2147483647;return (seed-1)/2147483646}}
  function E(t,a,k){var e=document.createElementNS(NS,t);for(var i in a)e.setAttribute(i,a[i]);(k||[]).forEach(function(c){e.appendChild(c)});return e}
  function smooth(pts,closed){ /* catmull-rom -> bezier */
    var d='M'+pts[0][0].toFixed(1)+' '+pts[0][1].toFixed(1),n=pts.length;
    for(var i=0;i<(closed?n:n-1);i++){var p0=pts[(i-1+n)%n],p1=pts[i],p2=pts[(i+1)%n],p3=pts[(i+2)%n];
      if(!closed){p0=pts[Math.max(0,i-1)];p3=pts[Math.min(n-1,i+2)]}
      d+='C'+(p1[0]+(p2[0]-p0[0])/6).toFixed(1)+' '+(p1[1]+(p2[1]-p0[1])/6).toFixed(1)+' '+(p2[0]-(p3[0]-p1[0])/6).toFixed(1)+' '+(p2[1]-(p3[1]-p1[1])/6).toFixed(1)+' '+p2[0].toFixed(1)+' '+p2[1].toFixed(1)}
    return d+(closed?'Z':'')}
  function blob(R,cx,cy,rx,ry,amp,rot){ /* hand-drawn ellipse: radius wobbles a little, like a felt-tip pen */
    var pts=[],N=18,ph1=R()*6,ph2=R()*6,a=amp||.06,c=Math.cos(rot||0),s=Math.sin(rot||0);
    for(var i=0;i<N;i++){var t=i/N*Math.PI*2,k=1+a*Math.sin(2*t+ph1)+a*.6*Math.sin(3*t+ph2),x=Math.cos(t)*rx*k,y=Math.sin(t)*ry*k*(t>0&&t<Math.PI?1.04:1);pts.push([cx+x*c-y*s,cy+x*s+y*c])}
    return smooth(pts,true)}
  function brush(R,pts,w){ /* tapered ink stroke along a path: thin at both ends, a touch of pressure jitter */
    var P=[],i,j;for(i=0;i<pts.length-1;i++)for(j=0;j<8;j++){var t=j/8,p0=pts[i],p1=pts[i+1];P.push([p0[0]+(p1[0]-p0[0])*t,p0[1]+(p1[1]-p0[1])*t])}P.push(pts[pts.length-1]);
    /* smooth the polyline */
    for(var it=0;it<3;it++)for(i=1;i<P.length-1;i++){P[i]=[(P[i-1][0]+P[i][0]*2+P[i+1][0])/4,(P[i-1][1]+P[i][1]*2+P[i+1][1])/4]}
    var L=[],Rr=[],n=P.length;for(i=0;i<n;i++){var a=P[Math.max(0,i-1)],b=P[Math.min(n-1,i+1)],dx=b[0]-a[0],dy=b[1]-a[1],l=Math.hypot(dx,dy)||1,t=i/(n-1),
      ww=w*Math.pow(Math.sin(Math.PI*Math.min(1,t*1.15)),.55)*(.9+.2*R())*.5+.25;L.push([P[i][0]-dy/l*ww,P[i][1]+dx/l*ww]);Rr.unshift([P[i][0]+dy/l*ww,P[i][1]-dx/l*ww])}
    return smooth(L.concat(Rr),true)}
  function face(o){
    var R=rnd(o.seed||5),W=200,H=120,sv=E('svg',{'class':'dfc',viewBox:'0 0 '+W+' '+H,'aria-hidden':'true'}),g=E('g');sv.appendChild(g);
    var ex=[62,138],ey=o.ey||50,er=(o.er||13)*1.3,ink=o.ink||INK;
    /* blush: soft pad of colour + three little pen hatches */
    if(o.blush!==false)[ex[0]-28,ex[1]+28].forEach(function(x){g.appendChild(E('path',{d:blob(R,x,ey+24,15,8,.08),fill:o.blushC||'#FF8A8A',opacity:.38}));
      for(var h=0;h<3;h++)g.appendChild(E('path',{d:brush(R,[[x-7+h*6,ey+27],[x-3+h*6,ey+20]],2.2),fill:o.blushC||'#E8566B',opacity:.55}))});
    ex.forEach(function(x,i){var lid=E('g',{'class':'lid'}),pu=E('g',{'class':'pu'}),sz=(o.wink&&i)?0:1,rr=er*(o.uneven&&i?1.18:1);
      if(o.eyes==='white'){lid.appendChild(E('path',{d:blob(R,x,ey,rr*1.35,rr*1.5,.05),fill:'#fff'}));lid.appendChild(E('path',{d:brush(R,[[x-rr*1.3,ey-rr*.4],[x-rr*.6,ey-rr*1.45],[x+rr*.7,ey-rr*1.4],[x+rr*1.33,ey-rr*.2]],2.6),fill:ink}));
        pu.appendChild(E('path',{d:blob(R,x+1,ey+3,rr*.62,rr*.72,.05),fill:ink}));pu.appendChild(E('path',{d:blob(R,x+4,ey-1,rr*.2,rr*.2,.1),fill:'#fff'}))}
      else if(o.eyes==='happy'||(o.wink&&i)){lid.appendChild(E('path',{d:brush(R,[[x-rr,ey+3],[x-rr*.4,ey-rr*.7],[x+rr*.4,ey-rr*.7],[x+rr,ey+3]],5),fill:ink}))}
      else{pu.appendChild(E('path',{d:blob(R,x,ey,rr*.86,rr,.05),fill:ink}));pu.appendChild(E('path',{d:blob(R,x+rr*.32,ey-rr*.38,rr*.3,rr*.32,.12),fill:'#fff'}));pu.appendChild(E('path',{d:blob(R,x-rr*.35,ey+rr*.45,rr*.12,rr*.12,.1),fill:'#fff',opacity:.9}))}
      lid.appendChild(pu);g.appendChild(lid);
      if(o.brows)g.appendChild(E('path',{d:brush(R,[[x-12,ey-rr-12+(i?3:-3)*o.brows],[x,ey-rr-15],[x+12,ey-rr-12+(i?-3:3)*o.brows]],4.2),fill:ink}))});
    var my=ey+30;
    if(o.mouth==='w')g.appendChild(E('path',{d:brush(R,[[86,my-2],[92,my+5],[99,my],[100,my-1],[101,my],[108,my+5],[114,my-2]],4.4),fill:ink}));
    else if(o.mouth==='tongue'){g.appendChild(E('path',{d:blob(R,104,my+9,8,10,.07),fill:'#EF6F7F'}));g.appendChild(E('path',{d:brush(R,[[104,my+4],[104.5,my+13]],1.8),fill:'#B8384A'}));
      g.appendChild(E('path',{d:brush(R,[[86,my],[100,my+6],[116,my-3]],4.6),fill:ink}))}
    else if(o.mouth==='open'){g.appendChild(E('path',{d:blob(R,100,my+5,10,8,.08),fill:'#5A1E22'}));g.appendChild(E('path',{d:blob(R,100,my+9,6,3.5,.1),fill:'#EF6F7F'}))}
    else if(o.mouth==='o')g.appendChild(E('path',{d:blob(R,100,my+2,4.6,5.6,.1),fill:ink}));
    else if(o.mouth==='flat')g.appendChild(E('path',{d:brush(R,[[90,my+2],[100,my+1],[110,my+3]],4),fill:ink}));
    else g.appendChild(E('path',{d:brush(R,[[86,my-1],[94,my+5],[106,my+5],[114,my-2]],4.6),fill:ink}));
    return sv}
  function pads(home){
    home.querySelectorAll('.dfc').forEach(function(n){n.remove()});
    var mob=innerWidth<640;
    var fs=home.querySelectorAll('.fx-row .fx-s');
    if(fs[0]){var f=face({seed:3,mouth:'tongue',er:14});f.style.cssText='right:6px;bottom:2px;width:'+(mob?130:190)+'px;transform:rotate(-6deg)';fs[0].appendChild(f)}
    if(fs[1]){var f2=face({seed:8,mouth:'w',wink:true,er:13});f2.style.cssText='right:6px;bottom:4px;width:'+(mob?130:190)+'px;transform:rotate(5deg)';fs[1].appendChild(f2)}
    var zc=home.querySelector('.zc2');if(zc){var f3=face({seed:11,eyes:'white',mouth:'o',er:13,blush:false});f3.style.cssText='right:30px;top:20px;width:'+(mob?140:200)+'px;transform:rotate(-8deg);opacity:.95';zc.appendChild(f3)}
    var en=home.querySelector('.end-in');if(en){var f4=face({seed:21,mouth:'open',er:15,uneven:true});f4.style.cssText='left:50%;top:18px;width:'+(mob?180:260)+'px;margin-left:-'+(mob?90:130)+'px';en.appendChild(f4)}
    faces=[].slice.call(document.querySelectorAll('.dfc'));
  }
  var faces=[],fmx=0,fmy=0,fr=0;
  function flook(){fr=0;faces.forEach(function(f){var r=f.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;var dx=fmx-(r.left+r.width/2),dy=fmy-(r.top+r.height*.45),d=Math.hypot(dx,dy)||1,k=Math.min(1,d/260)*3.2;
    f.querySelectorAll('.pu').forEach(function(p){p.setAttribute('transform','translate('+(dx/d*k).toFixed(2)+' '+(dy/d*k*.8).toFixed(2)+')')})})}
  if(!rm){addEventListener('pointermove',function(e){fmx=e.clientX;fmy=e.clientY;if(!fr)fr=requestAnimationFrame(flook)},{passive:true});
    (function bl(){setTimeout(function(){var f=faces[Math.floor(Math.random()*faces.length)];if(f){f.classList.add('blink');setTimeout(function(){f.classList.remove('blink')},130)}bl()},1200+Math.random()*2200)})()}


  function stickers(zq){
    zq.querySelectorAll('.hstk').forEach(function(n){n.remove()});
    var L=[['co-rocket',8,14,118,-10,'m'],['co-bulb',84,10,104,12,''],['co-laptop',6,62,128,8,''],['co-pad',86,58,118,-12,'m'],['co-bot',18,84,96,6,''],['co-cap',76,84,104,-6,'']];
    var mob=innerWidth<640;if(mob)L=[['co-rocket',12,9,64,-10,'m'],['co-pad',88,9,64,10,'m']];
    L.forEach(function(c,i){var a=document.createElement('a');a.className='hstk '+c[5];a.setAttribute('aria-hidden','true');a.tabIndex=-1;
      a.style.left=c[1]+'%';a.style.top=c[2]+'%';a.style.setProperty('--w',c[3]+'px');a.style.setProperty('--r',c[4]+'deg');
      a.style.setProperty('--t',(4+i*.6)+'s');a.style.setProperty('--d','-'+(i*.9)+'s');a.style.marginLeft=-(c[3]/2)+'px';a.style.marginTop=-(c[3]/2)+'px';
      a.innerHTML='<img src="/Hamterco/img/'+c[0]+'.webp" alt="">';a.dataset.k=(.6+i%3*.35);zq.appendChild(a)});
  }
  function portex(home){
    var fm=home.querySelector('.fx-main'),fx=fm&&fm.parentNode;if(!fm)return;
    fx.querySelectorAll('.px-aura').forEach(function(n){n.remove()});
    var au=document.createElement('i');au.className='px-aura';au.style.left=(fm.offsetLeft-4)+'px';au.style.top=(fm.offsetTop+6)+'px';au.style.width=(fm.offsetWidth+8)+'px';au.style.height=(fm.offsetHeight+6)+'px';fx.insertBefore(au,fx.firstChild);
    if(!fm.querySelector('.px-shine')){var sh=document.createElement('i');sh.className='px-shine';fm.appendChild(sh);
      var rb=document.createElement('span');rb.className='px-rib';
      var med=fm.querySelector('.fx-media');if(med)for(var i=0;i<9;i++){var t=document.createElementNS('http://www.w3.org/2000/svg','svg');t.setAttribute('class','tw');t.setAttribute('viewBox','-10 -10 20 20');
        t.innerHTML='<path d="M0-10C1 -2 2 -1 10 0C2 1 1 2 0 10C-1 2-2 1-10 0C-2-1-1-2 0-10Z" fill="#FFF6C8"/>';t.style.left=(8+Math.random()*84)+'%';t.style.top=(8+Math.random()*80)+'%';
        t.style.setProperty('--s',(10+Math.random()*12)+'px');t.style.setProperty('--t',(1.8+Math.random()*2)+'s');t.style.setProperty('--d','-'+(Math.random()*3).toFixed(1)+'s');med.appendChild(t)}
      if(!rm){fm.addEventListener('pointermove',function(e){var r=fm.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
          fm.style.setProperty('--ry',((x-.5)*6).toFixed(2)+'deg');fm.style.setProperty('--rx',(-(y-.5)*6).toFixed(2)+'deg');fm.style.setProperty('--mx',(x*100)+'%');fm.style.setProperty('--my',(y*100)+'%')});
        fm.addEventListener('pointerleave',function(){fm.style.setProperty('--ry','0deg');fm.style.setProperty('--rx','0deg')})}}
  }
  var szq=null;
  if(!rm)addEventListener('pointermove',function(e){if(!szq)return;var r=szq.getBoundingClientRect();if(e.clientY>r.bottom)return;var dx=(e.clientX-r.left-r.width/2)/r.width,dy=(e.clientY-r.top-r.height/2)/r.height;
    szq.querySelectorAll('.hstk').forEach(function(a){var k=+a.dataset.k;a.style.setProperty('--px',(-dx*22*k).toFixed(1)+'px');a.style.setProperty('--py',(-dy*18*k).toFixed(1)+'px')})},{passive:true});


  var WORKS=[['omni-piece','Omni Piece'],['phun','PHUN'],['heat-thieves','HEAT THIEVES'],['the-collector','The Collector'],['a-picturesque-breakfast','A Picturesque Breakfast'],['melody-duel','Melody Duel'],['element-royal','Elemental Lava Royale'],['endlessnoon','Endless Noon'],['nampun','Nampun'],['gamejam-x','เมษาหน้าลาบ'],['beat-the-beat-on-beach','Beat the Beat'],['khao-yai-alert','Khao Yai Alert'],['ecoeats-mas','EcoEats']];
  function reel(zq){
    zq.querySelectorAll('.reel,.reel-h').forEach(function(n){n.remove()});
    var ok=WORKS;
    var box=document.createElement('div');box.className='reel';var t=document.createElement('div');t.className='reel-t';
    var html=ok.map(function(w,i){var nm=w[1];return '<a class="rc-w" href="https://www.hamsterhub.co/go/projects/'+w[0]+'" target="_blank" rel="noopener" style="--r:'+((i%2?1:-1)*(2+i%3))+'deg;--y:'+(i%3*8)+'px"><img src="/Hamterco/img/ar-'+w[0]+'.webp" alt="'+nm+'" loading="lazy"><b>'+nm+'</b></a>'}).join('');
    t.innerHTML=html+html.replace(/<a /g,'<a tabindex="-1" aria-hidden="true" ');box.appendChild(t);zq.appendChild(box);
    var h=document.createElement('p');h.className='reel-h';h.textContent='ผลงานจริงของน้องๆ Hamster Hub กดเพื่อเปิดดู';zq.appendChild(h);
  }


  /* ===== the hero IS the slime: a WebGL ripple surface, glossy, that answers the pointer ===== */
  var GG=null;
  function goo(zq){
    if(GG){GG.stop();GG=null}zq.querySelectorAll('.gl-goo,.reel,.reel-h').forEach(function(n){n.remove()});
    var cv=document.createElement('canvas');cv.className='gl-goo';cv.setAttribute('aria-hidden','true');
    var gl=cv.getContext('webgl2',{alpha:false,antialias:false,premultipliedAlpha:false});
    if(!gl||!gl.getExtension('EXT_color_buffer_float'))return;
    zq.insertBefore(cv,zq.firstChild);
    function sh(t,src){var o=gl.createShader(t);gl.shaderSource(o,src);gl.compileShader(o);if(!gl.getShaderParameter(o,gl.COMPILE_STATUS))console.warn(gl.getShaderInfoLog(o));return o}
    function prog(fs){var p=gl.createProgram();gl.attachShader(p,sh(gl.VERTEX_SHADER,'#version 300 es\nin vec2 p;out vec2 uv;void main(){uv=p*.5+.5;gl_Position=vec4(p,0,1);}'));gl.attachShader(p,sh(gl.FRAGMENT_SHADER,fs));gl.linkProgram(p);return p}
    var SIM=prog('#version 300 es\nprecision highp float;in vec2 uv;out vec4 o;uniform sampler2D s;uniform vec2 px;uniform vec4 d;uniform float asp;\n'+
      'void main(){vec4 c=texture(s,uv);float n=(texture(s,uv+vec2(px.x,0)).r+texture(s,uv-vec2(px.x,0)).r+texture(s,uv+vec2(0,px.y)).r+texture(s,uv-vec2(0,px.y)).r)*.5-c.g;n*=.986;'+
      'vec2 q=(uv-d.xy)*vec2(asp,1.);n+=d.w*smoothstep(d.z,0.,length(q));o=vec4(n,c.r,0,1);}');
    var REN=prog('#version 300 es\nprecision highp float;in vec2 uv;out vec4 o;uniform sampler2D s;uniform vec2 px;uniform vec3 base;\n'+
      'void main(){float l=texture(s,uv-vec2(px.x,0)).r,r=texture(s,uv+vec2(px.x,0)).r,b=texture(s,uv-vec2(0,px.y)).r,t=texture(s,uv+vec2(0,px.y)).r,h=texture(s,uv).r;'+
      'vec3 n=normalize(vec3((l-r)*9.,(b-t)*9.,1.));vec3 L=normalize(vec3(-.45,.55,.7));float df=dot(n,L);'+
      'float sp=pow(max(dot(reflect(-L,n),vec3(0,0,1)),0.),48.);float sp2=pow(max(dot(reflect(-L,n),vec3(0,0,1)),0.),8.);'+
      'vec3 c=base*(1.+.3*(df-.702))+vec3(1.)*sp*.85+vec3(1.,.9,.75)*sp2*.06-vec3(.12,.07,.0)*clamp(-h*2.,0.,1.);o=vec4(c,1);}');
    var buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
    function bindQuad(p){var a=gl.getAttribLocation(p,'p');gl.enableVertexAttribArray(a);gl.vertexAttribPointer(a,2,gl.FLOAT,false,0,0)}
    var W,H,SW,SH,tex=[],fb=[];
    function size(){var r=zq.getBoundingClientRect(),dp=Math.min(devicePixelRatio||1,1.5);W=Math.round(r.width*dp);H=Math.round(r.height*dp);cv.width=W;cv.height=H;
      SW=Math.max(64,Math.round(r.width/3));SH=Math.max(64,Math.round(r.height/3));
      for(var i=0;i<2;i++){if(tex[i])gl.deleteTexture(tex[i]);tex[i]=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,tex[i]);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA16F,SW,SH,0,gl.RGBA,gl.HALF_FLOAT,null);
        gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);
        if(!fb[i])fb[i]=gl.createFramebuffer();gl.bindFramebuffer(gl.FRAMEBUFFER,fb[i]);gl.framebufferTexture2D(gl.FRAMEBUFFER,gl.COLOR_ATTACHMENT0,gl.TEXTURE_2D,tex[i],0);gl.clearColor(0,0,0,1);gl.clear(gl.COLOR_BUFFER_BIT)}}
    size();
    var cur=0,drops=[],run=false,raf=0,asp=1;
    function drop(x,y,r,s){drops.push([x,y,r,s])}
    function step(){
      asp=W/H;gl.useProgram(SIM);bindQuad(SIM);gl.viewport(0,0,SW,SH);
      var u=function(n){return gl.getUniformLocation(SIM,n)};gl.uniform2f(u('px'),1/SW,1/SH);gl.uniform1f(u('asp'),asp);gl.uniform1i(u('s'),0);
      for(var k=0;k<2;k++){var d=drops.shift()||[0,0,0,0];gl.uniform4f(u('d'),d[0],d[1],d[2],d[3]);gl.activeTexture(gl.TEXTURE0);gl.bindTexture(gl.TEXTURE_2D,tex[cur]);gl.bindFramebuffer(gl.FRAMEBUFFER,fb[1-cur]);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);cur=1-cur}
      gl.useProgram(REN);bindQuad(REN);gl.bindFramebuffer(gl.FRAMEBUFFER,null);gl.viewport(0,0,W,H);
      gl.uniform2f(gl.getUniformLocation(REN,'px'),1/SW,1/SH);gl.uniform3f(gl.getUniformLocation(REN,'base'),.969,.635,.243);gl.uniform1i(gl.getUniformLocation(REN,'s'),0);
      gl.activeTexture(gl.TEXTURE0);gl.bindTexture(gl.TEXTURE_2D,tex[cur]);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);
      if(run)raf=requestAnimationFrame(step)}
    var idle=setInterval(function(){if(run&&!rm&&Math.random()<.5)drop(Math.random(),Math.random(),.012+Math.random()*.015,(Math.random()<.5?-1:1)*.22)},1600);
    var lx=null,ly=null;
    function mv(e){var r=cv.getBoundingClientRect();if(e.clientY<r.top||e.clientY>r.bottom)return;var x=(e.clientX-r.left)/r.width,y=1-(e.clientY-r.top)/r.height;
      var v=lx==null?0:Math.min(1,Math.hypot(x-lx,y-ly)*30);lx=x;ly=y;if(v>.02)drop(x,y,.02,-.5*v-.1)}
    function dn(e){var r=cv.getBoundingClientRect();drop((e.clientX-r.left)/r.width,1-(e.clientY-r.top)/r.height,.035,-2.2)}
    if(!rm){zq.addEventListener('pointermove',mv,{passive:true});zq.addEventListener('pointerdown',dn,{passive:true})}
    var io=new IntersectionObserver(function(es){var v=es[0].isIntersecting;if(v&&!run){run=true;raf=requestAnimationFrame(step)}else if(!v){run=false;cancelAnimationFrame(raf)}});io.observe(cv);
    if(rm){run=false;step()}
    GG={stop:function(){run=false;cancelAnimationFrame(raf);clearInterval(idle);io.disconnect();zq.removeEventListener('pointermove',mv);zq.removeEventListener('pointerdown',dn)}};
  }

  function build(){
    var home=document.querySelector('[data-view="home"]'),zq=home&&home.querySelector('.zq');
    if(!zq||!zq.offsetWidth)return;
    document.querySelectorAll('.je').forEach(function(n){n.remove()});drip(zq);
    pads(home);portex(home);
    var top=zq.querySelector('.zq-top');
    if(top&&!tip&&!rm){var f=0;try{f=localStorage.getItem('hhFed')}catch(e){}
      if(!f){tip=document.createElement('p');tip.className='tip';tip.textContent='แตะพื้นสีส้มเพื่อป้อนเมล็ดทานตะวันให้น้องแฮมสเตอร์';top.appendChild(tip);
        tip.style.position='relative';tip.style.marginTop='18px';setTimeout(function(){tip.classList.add('on')},2400)}}
  }
  if(!rm)document.addEventListener('pointerdown',function(e){var zq=e.target.closest&&e.target.closest('[data-view="home"] .zq');
    if(zq&&!e.target.closest('form,button,a,input,h1,.zq-res,.zq-sug,.zq-pop'))feed(zq,e.clientX,e.clientY)});
  addEventListener('hashchange',function(){setTimeout(build,450)});
  var rt,lw=innerWidth;addEventListener('resize',function(){if(innerWidth===lw)return;lw=innerWidth;clearTimeout(rt);rt=setTimeout(build,250)});
  if(document.readyState==='complete')setTimeout(build,60);else addEventListener('load',function(){setTimeout(build,60)});
})();
