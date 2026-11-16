
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches,NS='http://www.w3.org/2000/svg',uid=0;
  function E(t,a,k){var e=document.createElementNS(NS,t);for(var i in a)e.setAttribute(i,a[i]);(k||[]).forEach(function(c){e.appendChild(c)});return e}
  function H(t,c,css){var e=document.createElement(t);if(c)e.className=c;if(css)e.style.cssText=css;return e}
  function grad(id,stops,lin){var g=E(lin?'linearGradient':'radialGradient',lin?{id:id,x1:'0',y1:'0',x2:lin[0],y2:lin[1]}:{id:id,cx:'34%',cy:'26%',r:'80%'});
    stops.forEach(function(s){g.appendChild(E('stop',{offset:s[0],'stop-color':s[1],'stop-opacity':s[2]==null?1:s[2]}))});return g}
  function blob(o){if(!window.Hamblob)return H('span');var w=Hamblob.make(o);w.classList.add('pz-hb');w.addEventListener('pointerdown',function(){Hamblob.squish(w)});return w}
  function at(e,css){e.style.cssText+=';'+css}
  function parts(w){var s=w.querySelector('svg');return {svg:s,defs:s.querySelector('defs'),body:s.querySelector('.hb-b')}}

  /* ---------- props drawn in the same soft-gradient style ---------- */
  function cap(w,top){var p=parts(w),id='pzc'+(++uid);
    p.defs.appendChild(grad(id+'a',[['0','#5E4D41'],['.55','#2A211B'],['1','#120D0A']]));
    p.defs.appendChild(grad(id+'t',[['0','#FFD08A'],['.5','#F7A23E'],['1','#D9741A']]));
    var g=E('g',{transform:'rotate(-8 100 '+top+')'}),T=top;
    g.appendChild(E('path',{d:'M66 '+(T+2)+' Q100 '+(T-8)+' 134 '+(T+2)+' L131 '+(T+22)+' Q100 '+(T+31)+' 69 '+(T+22)+' Z',fill:'url(#'+id+'a)'}));
    g.appendChild(E('path',{d:'M100 '+(T-24)+' Q104 '+(T-24)+' 110 '+(T-22)+' L166 '+(T-5)+' Q173 '+(T-2)+' 166 '+(T+1)+' L108 '+(T+17)+' Q100 '+(T+19)+' 92 '+(T+17)+' L34 '+(T+1)+' Q27 '+(T-2)+' 34 '+(T-5)+' L90 '+(T-22)+' Q96 '+(T-24)+' 100 '+(T-24)+' Z',fill:'url(#'+id+'a)'}));
    g.appendChild(E('path',{d:'M52 '+(T-6)+' L98 '+(T-20)+' L124 '+(T-13),stroke:'rgba(255,255,255,.3)','stroke-width':4,'stroke-linecap':'round','stroke-linejoin':'round',fill:'none'}));
    g.appendChild(E('path',{d:'M100 '+(T-3)+' Q138 '+(T-3)+' 150 '+(T+3)+' Q156 '+(T+14)+' 154 '+(T+30),stroke:'#F7A23E','stroke-width':3.2,fill:'none','stroke-linecap':'round'}));
    g.appendChild(E('ellipse',{cx:100,cy:T-3,rx:7,ry:4,fill:'url(#'+id+'t)'}));
    var ts=E('g',{'class':'pz-tassel'});ts.appendChild(E('path',{d:'M148 '+(T+27)+' Q154 '+(T+22)+' 160 '+(T+27)+' L162 '+(T+46)+' Q154 '+(T+52)+' 146 '+(T+46)+' Z',fill:'url(#'+id+'t)'}));g.appendChild(ts);
    p.body.appendChild(g)}
  function laptop(w){var p=parts(w),id='pzl'+(++uid);
    p.defs.appendChild(grad(id+'a',[['0','#FFFFFF'],['1','#E6D6C1']],['0','1']));
    p.defs.appendChild(grad(id+'b',[['0','#F4E9DA'],['1','#C9B293']],['0','1']));
    p.defs.appendChild(E('radialGradient',{id:id+'g',cx:'50%',cy:'100%',r:'60%'},[E('stop',{offset:'0','stop-color':'#A9E0FF','stop-opacity':'.85'}),E('stop',{offset:'1','stop-color':'#A9E0FF','stop-opacity':'0'})]));
    p.defs.appendChild(grad(id+'o',[['0','#FFD08A'],['1','#F7A23E']]));
    var g=E('g');
    g.appendChild(E('ellipse',{cx:100,cy:104,rx:78,ry:30,fill:'url(#'+id+'g)'}));
    g.appendChild(E('path',{d:'M50 112 Q50 104 58 104 L142 104 Q150 104 150 112 L156 156 L44 156 Z',fill:'url(#'+id+'a)'}));
    g.appendChild(E('path',{d:'M60 109 L140 109',stroke:'rgba(255,255,255,.95)','stroke-width':3,'stroke-linecap':'round'}));
    g.appendChild(E('ellipse',{cx:100,cy:131,rx:11,ry:10,fill:'url(#'+id+'o)'}));
    g.appendChild(E('ellipse',{cx:96.5,cy:127.5,rx:3.6,ry:2.6,fill:'#fff',opacity:.7}));
    g.appendChild(E('path',{d:'M24 156 Q24 152 29 152 L171 152 Q176 152 176 156 L174 163 Q173 167 167 167 L33 167 Q27 167 26 163 Z',fill:'url(#'+id+'b)'}));
    g.appendChild(E('path',{d:'M86 152 L114 152 L112 155 L88 155 Z',fill:'rgba(120,90,60,.35)'}));
    p.svg.appendChild(g)}
  function badge(w,col){var p=parts(w),id='pzb'+(++uid);
    p.defs.appendChild(grad(id+'a',[['0','#FFFFFF'],['1','#F1E6D8']],['0','1']));
    var g=E('g');
    g.appendChild(E('path',{d:'M80 118 Q90 134 100 140 Q110 134 120 118',stroke:col,'stroke-width':4,fill:'none','stroke-linecap':'round'}));
    g.appendChild(E('path',{d:'M86 140 Q86 136 90 136 L110 136 Q114 136 114 140 L114 156 Q114 160 110 160 L90 160 Q86 160 86 156 Z',fill:'url(#'+id+'a)'}));
    g.appendChild(E('path',{d:'M86 141 Q86 136 90 136 L110 136 Q114 136 114 141 L114 143 L86 143 Z',fill:col}));
    g.appendChild(E('path',{d:'M91 149 L109 149 M91 154 L103 154',stroke:'rgba(29,23,18,.22)','stroke-width':2.2,'stroke-linecap':'round'}));
    p.body.appendChild(g)}
  function coins(w){var p=parts(w),id='pzk'+(++uid);
    p.defs.appendChild(grad(id+'a',[['0','#FFE7A3'],['.5','#FFC53D'],['1','#D98A0F']],['1','0']));
    p.defs.appendChild(grad(id+'t',[['0','#FFF3C4'],['1','#FFC94D']]));
    var g=E('g');
    [[168,160],[168,150],[170,140],[167,130]].forEach(function(c,i){
      g.appendChild(E('path',{d:'M'+(c[0]-20)+' '+(c[1]-4)+' L'+(c[0]-20)+' '+(c[1]+3)+' Q'+c[0]+' '+(c[1]+11)+' '+(c[0]+20)+' '+(c[1]+3)+' L'+(c[0]+20)+' '+(c[1]-4)+' Z',fill:'url(#'+id+'a)'}));
      g.appendChild(E('ellipse',{cx:c[0],cy:c[1]-4,rx:20,ry:6.5,fill:'url(#'+id+'t)'}));
      if(i===3){g.appendChild(E('ellipse',{cx:c[0],cy:c[1]-4,rx:12,ry:3.6,fill:'none',stroke:'#E3A21C','stroke-width':1.6}))}});
    g.appendChild(E('path',{d:'M188 108 C189 114 190 115 196 116 C190 117 189 118 188 124 C187 118 186 117 180 116 C186 115 187 114 188 108Z',fill:'#FFF6C8'}));
    p.svg.appendChild(g)}

  /* ---------- the goo pad ---------- */
  function drips(W,spots){
    var svg=E('svg',{'class':'pz-drip',width:W,height:60,viewBox:'0 0 '+W+' 60','aria-hidden':'true'}),id='pzd'+(++uid);
    svg.appendChild(E('defs',{},[grad(id,[['0','#F29736'],['1','#E8862A']],['0','1'])]));
    var L=spots;
    L.forEach(function(d,i){var x=W*d[0],l=d[1],w=d[2],a=x-w/2,b=x+w/2;
      var g=E('g',{'class':'dr',style:'--t:'+(4.5+i*.7)+'s;--d:-'+(i*1.3)+'s'});
      g.appendChild(E('path',{d:'M'+(a-13)+' 0 C'+(a-3)+' 0 '+(a+1)+' '+(l*.3)+' '+(a+2)+' '+(l*.62)+' C'+(a+3)+' '+(l+w*.42)+' '+(b-3)+' '+(l+w*.42)+' '+(b-2)+' '+(l*.62)+' C'+(b-1)+' '+(l*.3)+' '+(b+3)+' 0 '+(b+13)+' 0 Z',fill:'url(#'+id+')'}));
      g.appendChild(E('ellipse',{cx:a+w*.32,cy:l*.62+w*.08,rx:w*.11,ry:w*.2,fill:'#fff',opacity:.55}));
      svg.appendChild(g)});
    return svg}
  function pad(view,bottomFn,spots){
    var p=view.querySelector(':scope>.pz-pad');
    if(!p){p=H('div','pz-pad');p.setAttribute('aria-hidden','true');var inn=H('div','pz-pad-in');
      [[8,20,26,'40px','-18px',16],[46,-30,34,'-50px','24px',19],[74,40,22,'30px','-26px',13]].forEach(function(b,i){var s=H('i','pz-bub','left:'+b[0]+'%;top:'+b[1]+'%;width:'+b[2]+'vw;height:'+b[2]+'vw;--dx:'+b[3]+';--dy:'+b[4]+';--t:'+b[5]+'s;--d:-'+(i*4)+'s');inn.appendChild(s)});
      p.appendChild(inn);view.insertBefore(p,view.firstChild)}
    var vt=view.getBoundingClientRect().top,h=Math.round(bottomFn()-vt-12);
    if(h>40)p.style.setProperty('--pz-h',h+'px');
    var W=Math.round(p.offsetWidth);
    if(W&&p._w!==W){p._w=W;var o=p.querySelector('.pz-drip');if(o)o.remove();if(spots&&spots.length)p.appendChild(drips(W,spots))}
    return p}

  /* ---------- scenes ---------- */
  function sceneCourses(host){
    if(host.querySelector('.pz-scene'))return;var s=H('div','pz-scene pz-c-scene');s.setAttribute('aria-hidden','true');
    var gr=blob({fur:'cream',shape:'tall',mood:'happy',size:158});at(gr,'left:8px;bottom:0');cap(gr,14);s.appendChild(gr);
    var lp=blob({fur:'orange',shape:'loaf',mood:'calm',size:200});at(lp,'right:0;bottom:-2px');laptop(lp);s.appendChild(lp);
    var pk=blob({fur:'pink',shape:'loaf',mood:'wow',size:88});at(pk,'left:142px;bottom:-4px');s.appendChild(pk);
    host.appendChild(s)}
  function sceneActivity(host){
    if(host.querySelector('.pz-scene'))return;var s=H('div','pz-scene pz-a-scene');s.setAttribute('aria-hidden','true');
    [['70px','-14deg','6deg'],['250px','10deg','-8deg']].forEach(function(b){var e=H('i','pz-beam','left:'+b[0]+';--r0:'+b[1]+';--r1:'+b[2]);s.appendChild(e)});
    var C=[['#FFC7DA','#FF8DB4'],['#D9CCFF','#9B82FF'],['#CDEBFF','#6FC3FF'],['#C9F5E6','#5FD3B4'],['#FFFFFF','#FFEBD0']];
    [[30,70,-30],[96,40,20],[160,58,60],[214,30,-10],[282,50,35],[350,74,-50],[60,112,15],[330,108,70],[206,90,-40],[392,36,10]].forEach(function(c,i){
      var k=C[i%C.length],e=H('i','pz-cf','left:'+c[0]+'px;top:'+c[1]+'px;--r:'+c[2]+'deg;--c1:'+k[0]+';--c2:'+k[1]+';--w:'+(12+i%3*3)+'px;--t:'+(4+i%4)+'s;--d:-'+(i*.7)+'s');s.appendChild(e)});
    var a=blob({fur:'sky',shape:'loaf',mood:'happy',size:150});at(a,'left:6px;bottom:0');badge(a,'#2F8FE0');s.appendChild(a);
    var c=blob({fur:'cream',shape:'loaf',mood:'happy',size:142});at(c,'right:0;bottom:0');badge(c,'#E0558C');s.appendChild(c);
    var b=blob({fur:'orange',shape:'tall',mood:'wow',size:176});at(b,'left:124px;bottom:10px');badge(b,'#1D1712');s.appendChild(b);
    host.appendChild(s)}
  function family(bento){
    if(bento.querySelector('.pz-fam'))return;var f=H('div','pz-fam');f.setAttribute('aria-hidden','true');
    var bb=blob({fur:'mint',shape:'puddle',mood:'sleep',size:70});at(bb,'left:0;bottom:-6px');f.appendChild(bb);
    var mom=blob({fur:'cream',shape:'loaf',mood:'calm',size:122});at(mom,'left:52px;bottom:0');f.appendChild(mom);
    var dad=blob({fur:'orange',shape:'tall',mood:'happy',size:140});at(dad,'right:0;bottom:2px');f.appendChild(dad);
    var kid=blob({fur:'pink',shape:'loaf',mood:'happy',size:76});at(kid,'left:150px;bottom:-8px');f.appendChild(kid);
    bento.appendChild(f)}

  /* ---------- Port Express on the courses page: same aura/tilt/twinkle language as home ---------- */
  function portex(view){
    var fm=view.querySelector('.fx-main'),fx=fm&&fm.parentNode;if(!fm||!fm.offsetWidth)return;
    var au=fx.querySelector(':scope>.px-aura');if(!au){au=H('i','px-aura');fx.insertBefore(au,fx.firstChild)}
    au.style.left=(fm.offsetLeft-4)+'px';au.style.top=(fm.offsetTop+6)+'px';au.style.width=(fm.offsetWidth+8)+'px';au.style.height=(fm.offsetHeight+6)+'px';
    var pk=fx.querySelector(':scope>.pz-peek');
    if(!pk){pk=blob({fur:'orange',shape:'loaf',mood:'wow',size:110});pk.classList.add('pz-peek');pk.setAttribute('aria-hidden','true');fm.after(pk)}
    var mob=innerWidth<640;pk.style.width=(mob?78:110)+'px';
    pk.style.left=(fm.offsetLeft+fm.offsetWidth-(mob?110:190))+'px';pk.style.top=(fm.offsetTop-(mob?46:68))+'px';
    if(fm._pz)return;fm._pz=1;
    var sh=H('i','px-shine');fm.appendChild(sh);if(!fm.querySelector('.pxe-ring'))fm.appendChild(H('i','pxe-ring'));
    var med=fm.querySelector('.fx-media');if(med&&!med.querySelector('.tw'))for(var i=0;i<9;i++){var t=E('svg',{'class':'tw',viewBox:'-10 -10 20 20','aria-hidden':'true'});
      t.appendChild(E('path',{d:'M0-10C1 -2 2 -1 10 0C2 1 1 2 0 10C-1 2-2 1-10 0C-2-1-1-2 0-10Z',fill:'#FFF6C8'}));
      t.style.left=(8+Math.random()*84)+'%';t.style.top=(8+Math.random()*80)+'%';t.style.setProperty('--s',(10+Math.random()*12)+'px');t.style.setProperty('--t',(1.8+Math.random()*2)+'s');t.style.setProperty('--d','-'+(Math.random()*3).toFixed(1)+'s');med.appendChild(t)}
    if(!rm){fm.addEventListener('pointermove',function(e){var r=fm.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
        fm.style.setProperty('--ry',((x-.5)*6).toFixed(2)+'deg');fm.style.setProperty('--rx',(-(y-.5)*6).toFixed(2)+'deg');fm.style.setProperty('--mx',(x*100)+'%');fm.style.setProperty('--my',(y*100)+'%')});
      fm.addEventListener('pointerenter',function(){pk.classList.add('up');Hamblob.squish(pk)});
      fm.addEventListener('pointerleave',function(){pk.classList.remove('up');fm.style.setProperty('--ry','0deg');fm.style.setProperty('--rx','0deg')})}
  }

  /* ---------- activity cards ---------- */
  var TY={'ค่าย':['orange','#FFE9CC','#FFC98A','#FFD7A3'],'เวิร์กชอป':['sky','#E4F4FF','#AEDDFF','#CDEBFF'],'แข่งขัน':['pink','#FFE7F0','#FFB7D0','#FFD3E3'],'โชว์ผลงาน':['lilac','#EEE8FF','#C9BBFF','#DDD3FF'],'โครงการ':['mint','#E2FAF2','#A6E9D4','#C9F5E6']};
  function decoCards(G){
    G.querySelectorAll('.avc').forEach(function(c,i){if(c._pz)return;c._pz=1;
      var t=c.querySelector('.avc-d span'),k=TY[t&&t.textContent.trim()]||TY['ค่าย'];
      c.style.setProperty('--pz-chip',k[3]);c.style.setProperty('--pz-l',k[1]);c.style.setProperty('--pz-bg',k[2]);
      var ty=c.querySelector('.avc-ty');
      if(ty&&!ty.querySelector('.hb')){var moods=['happy','calm','wow'],sh=['loaf','tall','loaf'];var FC=['orange','mint','sky','pink','lilac','cream'];var h=blob({fur:FC[i%6],shape:sh[i%3],mood:moods[i%3]});h.setAttribute('aria-hidden','true');ty.appendChild(h);
        c.addEventListener('pointerenter',function(){Hamblob.squish(h)})}
    })}
  function popIn(G){if(rm||!G.animate)return;[].slice.call(G.children).forEach(function(c,i){c.animate([{opacity:0,transform:'translateY(18px) scale(.97)'},{opacity:1,transform:'none'}],{duration:520,delay:Math.min(i,8)*45,easing:'cubic-bezier(.2,.9,.25,1)',fill:'backwards'})})}
  function countUp(el){if(rm||el._pz)return;el._pz=1;var n=parseInt(el.textContent,10);if(!n)return;
    var io=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;io.disconnect();var t0=performance.now(),d=900;
      (function f(t){var k=Math.min(1,(t-t0)/d),e=1-Math.pow(1-k,3);el.textContent=Math.round(n*e);if(k<1)requestAnimationFrame(f);else el.textContent=n})(t0)},{threshold:.6});io.observe(el)}

  /* ---------- scroll reveals + press feel come from the shared 15-motion system ---------- */
  function mo(v,list,press){if(!window.Motion)return;list.forEach(function(x){v.querySelectorAll(x[0]).forEach(function(n){n.classList.add('mo-'+x[1])})});
    if(press)v.querySelectorAll(press).forEach(function(n){n.classList.add('mo-press')});Motion.scan(v)}
  /* ---------- one entrance per page: the header hamblobs drop in and land with a squash ---------- */
  function land(sc){if(rm||!sc||!sc.animate)return;sc.querySelectorAll('.hb').forEach(function(h,i){
    h.animate([{transform:'translateY(-70px) scale(.88,1.14)',opacity:0,easing:'cubic-bezier(.55,0,.95,.5)'},{opacity:1,offset:.15},{transform:'translateY(0) scale(.92,1.1)',offset:.55},
      {transform:'scale(1.16,.84)',offset:.68},{transform:'translateY(-8px) scale(.97,1.03)',offset:.84},{transform:'none'}],{duration:950,delay:250+i*130,fill:'backwards'})})}
  var landed={};addEventListener('hashchange',function(){landed={}});

  /* ---------- small screens: the scene sits beside the page title, never over the text ---------- */
  function place(sc,h1){if(!sc||!h1)return;if(innerWidth>900){sc.style.removeProperty('--pz-top');return}
    var k=parseFloat(getComputedStyle(sc).getPropertyValue('--pz-s'))||.5;sc.style.setProperty('--pz-top',Math.round(h1.offsetTop+h1.offsetHeight-250*k-2)+'px')}

  /* ---------- per view ---------- */
  function courses(v){
    var hd=v.querySelector('.ct-h');if(!hd)return;hd.style.position='relative';
    pad(v,function(){return hd.getBoundingClientRect().bottom-28},innerWidth<=640?[[.72,12,20],[.84,20,24]]:[[.64,12,22],[.74,22,28],[.86,10,20],[.93,18,24]]);
    sceneCourses(hd);place(hd.querySelector('.pz-scene'),hd.querySelector('h1'));
    portex(v);
    mo(v,[['.ft-hd','rise'],['.fx-main','goo'],['.fx-row','kids'],['.ct-all','rise'],['.ctg','kids'],['.fit-in','goo']],'.fx-cta,.fx-go,.fit-q label,.ct-help .btn');
    if(!landed.c){landed.c=1;land(hd.querySelector('.pz-scene'))}
  }
  function activity(v){
    var hd=v.querySelector('.av-h'),nx=v.querySelector('.avn');if(!hd)return;var hin=hd.querySelector('.av-in');hin.style.position='relative';
    pad(v,function(){if(!nx)return hd.getBoundingClientRect().bottom;var r=nx.getBoundingClientRect();if(innerWidth<=900)return r.top-14;return r.top+Math.min(220,r.height*.42)},innerWidth<=900?[[.7,14,22],[.82,22,26]]:null);
    sceneActivity(hin);place(hin.querySelector('.pz-scene'),hin.querySelector('h1'));
    var G=v.querySelector('#avG');if(G){decoCards(G);if(!G._pzo){G._pzo=new MutationObserver(function(){decoCards(G);popIn(G)});G._pzo.observe(G,{childList:true})}}
    var cnt=v.querySelector('#avCount');if(cnt)countUp(cnt);
    mo(v,[['.av-top','rise'],['#avG','kids'],['.av-ph h2','rise'],['.av-pg','kids'],['.av-cta .av-in','goo']],'.av-f button,.avn-b a,.av-cta a');
    if(!landed.a){landed.a=1;land(hin.querySelector('.pz-scene'))}
  }
  function about(v){
    var aw=v.querySelector('.ab-win'),fg=aw&&aw.querySelector('.aw-g figure');if(!aw)return;
    pad(v,function(){if(!fg)return aw.getBoundingClientRect().bottom;var r=fg.getBoundingClientRect();return r.top+r.height*.5});
    var np=aw.querySelector('figure.nopic');
    if(np&&!np.querySelector('.pz-sold')){var s=H('div','pz-sold');s.setAttribute('aria-hidden','true');var h=blob({fur:'orange',shape:'loaf',mood:'happy'});coins(h);s.appendChild(h);np.insertBefore(s,np.firstChild);
      np.addEventListener('pointerenter',function(){Hamblob.squish(h)})}
    var be=v.querySelector('.ab-bento');if(be)family(be);
    var big=v.querySelector('.ad-big');
    if(big&&big.offsetWidth){var wr=big.parentNode,gl=wr.querySelector(':scope>.pz-glow');if(!gl){gl=H('i','pz-glow');gl.setAttribute('aria-hidden','true');wr.insertBefore(gl,big)}
      gl.style.left=(big.offsetLeft+10)+'px';gl.style.top=(big.offsetTop+16)+'px';gl.style.width=(big.offsetWidth-20)+'px';gl.style.height=(big.offsetHeight-10)+'px';
      var pc=wr.querySelector(':scope>.pz-perch');if(!pc){pc=blob({fur:'orange',shape:'loaf',mood:'wow'});pc.classList.add('pz-perch');pc.setAttribute('aria-hidden','true');wr.insertBefore(pc,big);
        big.addEventListener('pointerenter',function(){pc.classList.add('up');Hamblob.squish(pc)});big.addEventListener('pointerleave',function(){pc.classList.remove('up')})}
      var pw=innerWidth<640?84:120;pc.style.width=pw+'px';pc.style.left=(big.offsetLeft+big.offsetWidth-pw-(innerWidth<640?18:40))+'px';pc.style.top=(big.offsetTop-pw*.62)+'px'}
    mo(v,[['.aw-g','kids'],['.ab-do2 .sec-h','rise'],['.ad-big','goo'],['.ad-two','kids'],['.ab-use .sec-h','rise'],['.ab-use .us','goo'],['.ab-res img','goo']],'.ab-ct .btn,.ab-ct .cprow');
    if(!landed.b){landed.b=1;var fm=v.querySelector('.pz-fam');if(fm&&fm.getBoundingClientRect().top<innerHeight)land(fm)}
  }
  function build(){
    var c=document.querySelector('[data-view="courses"].on'),a=document.querySelector('[data-view="activity"].on'),b=document.querySelector('[data-view="about"].on');
    if(c&&c.offsetWidth)courses(c);if(a&&a.offsetWidth)activity(a);if(b&&b.offsetWidth)about(b);
  }
  /* keep pads/aura sized as images load and the layout settles */
  var bt=0;function soon(ms){clearTimeout(bt);bt=setTimeout(build,ms||80)}
  if('ResizeObserver' in window){var ro=new ResizeObserver(function(){soon(60)});
    ['courses','activity','about'].forEach(function(k){var v=document.querySelector('[data-view="'+k+'"]');if(v)ro.observe(v)})}
  addEventListener('hashchange',function(){setTimeout(build,40);soon(500)});
  addEventListener('resize',function(){soon(150)});
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){soon(30)});
  if(document.readyState==='complete')setTimeout(build,30);else addEventListener('load',function(){setTimeout(build,30)});
  setTimeout(build,0);
})();
