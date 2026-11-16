
(function(){
  var NS='http://www.w3.org/2000/svg',INK='#1D1712',rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function R0(s){return function(){s=(s*16807)%2147483647;return (s-1)/2147483646}}
  function E(t,a){var e=document.createElementNS(NS,t);for(var i in a)e.setAttribute(i,a[i]);return e}
  function sm(p){var n=p.length,d='M'+p[0][0].toFixed(1)+' '+p[0][1].toFixed(1);for(var i=0;i<n;i++){var a=p[(i-1+n)%n],b=p[i],c=p[(i+1)%n],e=p[(i+2)%n];d+='C'+(b[0]+(c[0]-a[0])/6).toFixed(1)+' '+(b[1]+(c[1]-a[1])/6).toFixed(1)+' '+(c[0]-(e[0]-b[0])/6).toFixed(1)+' '+(c[1]-(e[1]-b[1])/6).toFixed(1)+' '+c[0].toFixed(1)+' '+c[1].toFixed(1)}return d+'Z'}
  function blob(R,cx,cy,rx,ry,a){var p=[],ph=R()*6;for(var i=0;i<16;i++){var t=i/16*Math.PI*2,k=1+(a||.05)*Math.sin(2*t+ph);p.push([cx+Math.cos(t)*rx*k,cy+Math.sin(t)*ry*k])}return sm(p)}
  function stroke(R,pts,w){var P=[],i,j;for(i=0;i<pts.length-1;i++)for(j=0;j<8;j++){var t=j/8;P.push([pts[i][0]+(pts[i+1][0]-pts[i][0])*t,pts[i][1]+(pts[i+1][1]-pts[i][1])*t])}P.push(pts[pts.length-1]);
    for(var it=0;it<3;it++)for(i=1;i<P.length-1;i++)P[i]=[(P[i-1][0]+P[i][0]*2+P[i+1][0])/4,(P[i-1][1]+P[i][1]*2+P[i+1][1])/4];
    var L=[],Rr=[],n=P.length;for(i=0;i<n;i++){var a=P[Math.max(0,i-1)],b=P[Math.min(n-1,i+1)],dx=b[0]-a[0],dy=b[1]-a[1],l=Math.hypot(dx,dy)||1,ww=w*Math.pow(Math.sin(Math.PI*Math.min(1,i/(n-1)*1.12)),.55)*.5+.25;
      L.push([P[i][0]-dy/l*ww,P[i][1]+dx/l*ww]);Rr.unshift([P[i][0]+dy/l*ww,P[i][1]-dx/l*ww])}return sm(L.concat(Rr))}
  function face(o){var R=R0(o.seed),sv=E('svg',{'class':'lf',viewBox:'0 0 200 120','aria-hidden':'true'}),ey=50,er=17,ex=[62,138],c=o.ink||INK;
    if(o.blush!==false)[34,166].forEach(function(x){sv.appendChild(E('path',{d:blob(R,x,ey+26,15,8),fill:'#FF7F9F',opacity:.4}));for(var h=0;h<3;h++)sv.appendChild(E('path',{d:stroke(R,[[x-7+h*6,ey+29],[x-3+h*6,ey+22]],2.2),fill:'#E8566B',opacity:.55}))});
    ex.forEach(function(x,i){var lid=E('g',{'class':'lid'}),pu=E('g',{'class':'pu'});
      if(o.happy)lid.appendChild(E('path',{d:stroke(R,[[x-er,ey+4],[x-er*.45,ey-er*.6],[x+er*.45,ey-er*.6],[x+er,ey+4]],6),fill:c}));
      else if(o.wink&&i)lid.appendChild(E('path',{d:stroke(R,[[x-er,ey+3],[x-er*.4,ey-er*.7],[x+er*.4,ey-er*.7],[x+er,ey+3]],5),fill:c}));
      else{pu.appendChild(E('path',{d:blob(R,x,ey,er*.86,er),fill:c}));pu.appendChild(E('path',{d:blob(R,x+er*.32,ey-er*.38,er*.3,er*.32,.1),fill:o.hi||'#fff'}));pu.appendChild(E('path',{d:blob(R,x-er*.35,ey+er*.45,er*.12,er*.12),fill:o.hi||'#fff'}))}
      lid.appendChild(pu);sv.appendChild(lid)});
    var my=ey+32;
    if(o.mouth==='grin'){sv.appendChild(E('path',{d:'M84 '+(my-2)+'Q100 '+(my+2)+' 116 '+(my-2)+'Q114 '+(my+16)+' 100 '+(my+17)+'Q86 '+(my+16)+' 84 '+(my-2)+'Z',fill:'#5A1E22'}));sv.appendChild(E('path',{d:blob(R,100,my+11,7,3.5),fill:'#EF6F7F'}));sv.appendChild(E('path',{d:'M88 '+(my-.5)+'Q100 '+(my+3)+' 112 '+(my-.5)+'V'+(my+3)+'Q100 '+(my+6)+' 88 '+(my+3)+'Z',fill:'#fff'}))}
    else if(o.mouth==='open'){sv.appendChild(E('path',{d:blob(R,100,my+5,11,9,.08),fill:'#5A1E22'}));sv.appendChild(E('path',{d:blob(R,100,my+9,6.5,3.6),fill:'#EF6F7F'}))}
    else if(o.mouth==='o2'){sv.appendChild(E('path',{d:blob(R,100,my+4,7,8,.08),fill:'#5A1E22'}));sv.appendChild(E('path',{d:blob(R,100,my+8,4,2.4),fill:'#EF6F7F'}))}
    else if(o.mouth==='tongue'){sv.appendChild(E('path',{d:blob(R,104,my+9,8,10,.07),fill:'#EF6F7F'}));sv.appendChild(E('path',{d:stroke(R,[[86,my],[100,my+6],[116,my-3]],4.6),fill:c}))}
    else sv.appendChild(E('path',{d:stroke(R,[[86,my-2],[92,my+5],[99,my],[100,my-1],[101,my],[108,my+5],[114,my-2]],4.4),fill:c}));
    return sv}

  /* props per row, drawn in the same soft style: [0] startup explorer, [1] REVOICE singer, [2] gamer */
  function prop(k){var R=R0(40+k),sv=E('svg',{'class':'lfa',viewBox:'0 0 200 200','aria-hidden':'true'});
    function A(d,f,x){var a={d:d,fill:f};for(var i in x)a[i]=x[i];sv.appendChild(E('path',a))}
    /* hamster ears + cream muzzle + buck teeth on every pad */
    var fur=['#D9741A','#E0558C','#26A386'][k];
    [[52,40,-1],[148,40,1]].forEach(function(e){A(blob(R,e[0],e[1],24,22,.05),fur);A(blob(R,e[0],e[1]+2,12,11,.06),'#FFB3C8')});
    A(blob(R,100,128,34,22,.05),'#FFF3E3',{opacity:.9});A('M94 132h12v9q-6 3-12 0z','#fff',{stroke:'#1D1712','stroke-width':1.6});A('M100 132v9','none',{stroke:'#1D1712','stroke-width':1.2});
    if(k===0){ /* startup: rocket taking off + coin (it sells for real) */
      A('M170 150C168 120 178 98 190 88C202 98 210 120 208 150Z','#fff',{stroke:'#1D1712','stroke-width':3});A(blob(R,189,120,7,7),'#6FC3FF',{stroke:'#1D1712','stroke-width':2});
      A('M170 140l-10 16 12-4zM208 140l10 16-12-4z','#FF5A5A',{stroke:'#1D1712','stroke-width':2});A('M178 152q11 24 22 0','#FFB23E');
      A(blob(R,22,160,16,16,.03),'#FFD24A',{stroke:'#1D1712','stroke-width':2.5});A('M18 152h8M16 160h12M18 168h8','none',{stroke:'#B8860B','stroke-width':2.4,'stroke-linecap':'round'})}
    else if(k===1){ /* national winner: gold medal on a ribbon + sparkle */
      A('M76 150l-10 40 18-8 10 14 8-44zM124 150l10 40-18-8-10 14-8-44z','#6FC3FF',{stroke:'#1D1712','stroke-width':2});
      A(blob(R,100,178,20,20,.03),'#FFD24A',{stroke:'#1D1712','stroke-width':3});A('M100 166l4 8 9 1-7 6 2 9-8-5-8 5 2-9-7-6 9-1z','#fff');
      A('M168 30h6v10h10v6h-10v10h-6v-10h-10v-6h10z','#FFD24A')}
    else{ /* game that people play: controller held below + pixel star */
      A(blob(R,100,178,58,22,.04),'#2A211B');A(blob(R,58,182,18,18),'#2A211B');A(blob(R,142,182,18,18),'#2A211B');
      A('M66 172h8v-8h8v8h8v8h-8v8h-8v-8h-8z','#fff',{opacity:.9});
      A(blob(R,128,172,5,5),'#FF5A7A');A(blob(R,142,180,5,5),'#5FD3B4');A(blob(R,114,180,5,5),'#FFD24A');A(blob(R,128,188,5,5),'#6FC3FF');
      A('M164 26h8v8h8v8h-8v8h-8v-8h-8v-8h8z','#FFD24A')}
    return sv}
  var faces=[];
  function mascot(){var zq=document.querySelector('[data-view="home"] .zq');if(!zq||zq.querySelector('.lm'))return;
    var a=document.createElement('a');a.className='lm';a.setAttribute('aria-hidden','true');a.tabIndex=-1;a.innerHTML='<img src="/Hamterco/img/hh-mascot.webp" alt="" width="290" height="290">';
    a.addEventListener('pointerdown',function(e){e.stopPropagation();a.classList.remove('tap');void a.offsetWidth;a.classList.add('tap')});zq.appendChild(a)}


  var SN=[[1,'น้องปลื้ม','สจล.',5,13,118,-6],[6,'น้องต้นกล้า','จุฬาฯ',13,48,104,5],[13,'น้องอาร์ม','มหิดล',4,76,112,-3],
          [3,'น้องดา','สจล.',95,14,112,6],[8,'น้องเฟิร์ส','จุฬาฯ',86,46,106,-5],[16,'น้องปิ่นโต','มหิดล',95,76,114,4]];
  function seniors(){var zq=document.querySelector('[data-view="home"] .zq');if(!zq||zq.querySelector('.sn'))return;
    SN.forEach(function(c){var a=document.createElement('a');a.className='sn';a.href='#works';
      a.style.cssText='left:'+c[3]+'%;top:'+c[4]+'%;--w:'+c[5]+'px;--r:'+c[6]+'deg;margin-left:-'+(c[5]/2)+'px';
      a.innerHTML='<i><span><img src="/Hamterco/img/dek69-'+c[0]+'.webp" alt="'+c[1]+' ติด '+c[2]+'" loading="lazy"></span></i><b>'+c[1]+'</b><em>ติด '+c[2]+'</em>';zq.appendChild(a)});
    var p=document.createElement('p');p.className='sn-cap';p.textContent='รุ่นพี่ปี 2569 ติดมหาลัยด้วยผลงานที่ทำกับเรา';zq.appendChild(p)}
  function build(){
    document.querySelectorAll('.lf,.lfp').forEach(function(n){n.remove()});faces=[];
    var home=document.querySelector('[data-view="home"]');if(!home)return;var mob=innerWidth<640;
    var en=home.querySelector('.end-in');if(en){var f=face({seed:21,mouth:'open'});f.style.cssText='left:50%;top:'+(mob?14:22)+'px;width:'+(mob?170:250)+'px;margin-left:-'+(mob?85:125)+'px';en.appendChild(f)}
    /* "what we build": a face peeks from behind each picture, different mood per row */
    var M=[{seed:3,mouth:'w',happy:true},{seed:8,mouth:'w'},{seed:13,mouth:'w'}];
    faces=[].slice.call(document.querySelectorAll('.lf'));
  }
  var mx=0,my=0,raf=0;
  function look(){raf=0;faces.forEach(function(f){var r=f.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;var dx=mx-(r.left+r.width/2),dy=my-(r.top+r.height*.45),d=Math.hypot(dx,dy)||1,k=Math.min(1,d/260)*3.4;
    f.querySelectorAll('.pu').forEach(function(p){p.setAttribute('transform','translate('+(dx/d*k).toFixed(2)+' '+(dy/d*k*.8).toFixed(2)+')')})})}
  if(!rm){addEventListener('pointermove',function(e){mx=e.clientX;my=e.clientY;if(!raf)raf=requestAnimationFrame(look)},{passive:true});
    (function bl(){setTimeout(function(){var f=faces[Math.floor(Math.random()*faces.length)];if(f){f.classList.add('blink');setTimeout(function(){f.classList.remove('blink')},130)}bl()},1300+Math.random()*2000)})()}
  addEventListener('hashchange',function(){setTimeout(build,500)});var lw=innerWidth,t;addEventListener('resize',function(){if(innerWidth===lw)return;lw=innerWidth;clearTimeout(t);t=setTimeout(build,300)});
  if(document.readyState==='complete')setTimeout(build,400);else addEventListener('load',function(){setTimeout(build,400)});
})();
