
(function(){
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
  var raf=window.requestAnimationFrame||function(f){return setTimeout(f,16)};

  /* ---------- 1. search panel fades ---------- */
  var res=$('#zqRes');
  if(res){
    var q=0;
    var edge=function(){q=0;var more=res.scrollHeight-res.clientHeight>4,b=more&&res.scrollTop+res.clientHeight<res.scrollHeight-6,t=more&&res.scrollTop>6;
      if(res.classList.contains('rv-fb')!==b)res.classList.toggle('rv-fb',b);if(res.classList.contains('rv-ft')!==t)res.classList.toggle('rv-ft',t)};
    var later=function(){if(!q)q=raf(edge)};
    res.addEventListener('scroll',later,{passive:true});
    new MutationObserver(later).observe(res,{childList:true,subtree:true});
    if(window.ResizeObserver)new ResizeObserver(later).observe(res);
    var z=$('[data-view="home"] .zq');if(z)new MutationObserver(function(){setTimeout(later,60);setTimeout(later,500)}).observe(z,{attributes:true,attributeFilter:['class']});
  }

  /* ---------- 2 + 4. focus: reveal anything hidden, pick ring colour from the surface ---------- */
  function rgb(c){var m=c&&c.match(/[\d.]+/g);return m?{r:+m[0],g:+m[1],b:+m[2],a:m[3]==null?1:+m[3]}:null}
  function dark(el){var n=el;while(n&&n.nodeType===1){var s=getComputedStyle(n),c=rgb(s.backgroundColor);
      if(s.backgroundImage&&s.backgroundImage!=='none'&&/gradient/.test(s.backgroundImage)){var g=rgb(s.backgroundImage);if(g)c=g}
      if(c&&c.a>.5){return (.2126*c.r+.7152*c.g+.0722*c.b)<110}n=n.parentElement}
    return false}
  document.addEventListener('focusin',function(e){var t=e.target;if(!t||!t.closest)return;
    for(var n=t;n&&n!==document.body;n=n.parentElement){var c=n.classList;if(!c)continue;
      if((c.contains('mo-goo')||c.contains('mo-rise')||c.contains('mo-kids'))&&!c.contains('mo-in')){c.add('mo-in');c.add('mo-done')}
      if(c.contains('rv')&&!c.contains('in'))c.add('in')}
    var d=dark(t.parentElement||t);if(t.classList.contains('rv-on-dk')!==d)t.classList.toggle('rv-on-dk',d)},true);

  /* ---------- 5. LINE green buttons: ink text ---------- */
  function line(){$$('a,button').forEach(function(e){if(e.classList.contains('rv-ln'))return;var c=rgb(getComputedStyle(e).backgroundColor);
    if(c&&c.a>.9&&c.g>150&&c.r<90&&c.b<140)e.classList.add('rv-ln')})}

  /* ---------- 7. course covers ---------- */
  function f1(n){return Math.round(n*10)/10}
  function rng(seed){var s=seed>>>0||1;return function(){s^=s<<13;s>>>=0;s^=s>>>17;s^=s<<5;s>>>=0;return s/4294967296}}
  function hash(str){var h=2166136261;for(var i=0;i<str.length;i++){h^=str.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
  var PAT={
    grid:function(r){var o='',ox=r()*18,oy=r()*18;for(var x=ox;x<320;x+=18)o+='<path d="M'+f1(x)+' 0V240"/>';for(var y=oy;y<240;y+=18)o+='<path d="M0 '+f1(y)+'H320"/>';
      var ax=ox+18*(9+Math.floor(r()*4)),ay=oy+18*2,R=72;return o+'<path class="a" d="M'+f1(ax)+' '+f1(ay+R)+'A'+R+' '+R+' 0 0 0 '+f1(ax+R)+' '+f1(ay)+'"/>'},
    speed:function(r){var o='';for(var k=0;k<16;k++){var y=k*15+r()*6,x0=120+r()*90,len=60+r()*140;o+='<path'+(k===5?' class="a"':'')+' d="M'+f1(x0)+' '+f1(y)+'h'+f1(len)+'"/>'}return o},
    orbit:function(r){var cx=250+r()*40,cy=20+r()*30,o='<g transform="rotate(-18 '+f1(cx)+' '+f1(cy)+')">';for(var k=0;k<6;k++){var rx=40+k*42;o+='<ellipse cx="'+f1(cx)+'" cy="'+f1(cy)+'" rx="'+rx+'" ry="'+f1(rx*.5)+'"'+(k===2?' class="a"':'')+'/>'}return o+'</g>'},
    steps:function(r){var o='',x=150,y=210;for(var k=0;k<6;k++){var w=26,h=18+r()*8;o+='<path'+(k===5?' class="a"':'')+' d="M'+f1(x)+' '+f1(y)+'v'+f1(-h)+'h'+w+'"/>';x+=w;y-=h}
      for(var j=0;j<8;j++)o+='<path d="M0 '+(30+j*26)+'H320"/>';return o},
    dots:function(r){var o='',cx=250+r()*30,cy=40+r()*30;for(var y=8;y<240;y+=13)for(var x=8;x<320;x+=13){var d=Math.hypot(x-cx,y-cy),rr=Math.max(0,3.2-d/62);if(rr>.45)o+='<circle class="d" cx="'+x+'" cy="'+y+'" r="'+f1(rr)+'"/>'}return o},
    contour:function(r){var cx=240+r()*40,cy=60+r()*30,o='';for(var k=0;k<9;k++){var rx=14+k*22,ry=rx*.66;o+='<ellipse cx="'+f1(cx)+'" cy="'+f1(cy)+'" rx="'+rx+'" ry="'+f1(ry)+'" transform="rotate('+f1(-12+k*2.4)+' '+f1(cx)+' '+f1(cy)+')"'+(k===3?' class="a"':'')+'/>'}return o}
  };
  /* tagline: a few words taken from the card's own line */
  var COURSE={
    'Port70':['ink','grid','คอร์สทำพอร์ต DEK70'],
    'Project Express':['orange','speed','ทำโปรเจกต์ให้เสร็จไว'],
    'National Project':['sky','orbit','ส่งเวทีระดับประเทศ'],
    'Business Project':['mint','steps','ต่อยอดเป็นธุรกิจ'],
    'Python Pro Pack':['lilac','dots','เรียนเขียน Python'],
    'Hamstarter':['sand','contour','คอร์สเริ่มต้น']
  },CYC=[['pink','contour'],['sky','dots'],['mint','grid'],['lilac','orbit']];
  function covers(){var k=0;
    $$('.qv').forEach(function(q){var im=q.querySelector('.qv-im'),img=im&&im.querySelector('img');if(!img||im.classList.contains('rv-has'))return;
      if(!/dek69-/.test(img.getAttribute('src')||''))return;
      var nm=(q.querySelector('.qv-tx b')||{}).textContent||'',d=(q.querySelector('.qv-d')||{}).textContent||'';nm=nm.trim();
      var c=COURSE[nm]||(function(){var x=CYC[k++%CYC.length];return [x[0],x[1],d.trim().split(/\s+/).slice(0,3).join(' ')]})();
      var cv=document.createElement('span');cv.className='rv-cv c-'+c[0];cv.setAttribute('aria-hidden','true');
      cv.innerHTML='<svg viewBox="0 0 320 240" preserveAspectRatio="xMidYMid slice">'+PAT[c[1]](rng(hash(nm)))+'</svg><b></b><span></span>';
      cv.querySelector('b').textContent=nm;cv.querySelector('span').textContent=c[2];
      im.insertBefore(cv,im.firstChild);im.classList.add('rv-has')})}

  /* ---------- 10. about: the card with no picture ---------- */
  function about(){var f=$('.aw-g figure.nopic');if(!f||f.querySelector('.rv-ph'))return;
    var ph=document.createElement('span');ph.className='rv-ph';ph.setAttribute('aria-hidden','true');
    var o='';for(var x=-20;x<340;x+=34)o+='<path d="M'+x+' 0L'+(x+60)+' 240"/>';for(var y=10;y<240;y+=30)o+='<path d="M0 '+y+'L320 '+(y-26)+'"/>';
    o+='<path class="a" d="M30 190C90 170 110 120 160 110S250 70 290 40"/><circle class="d" cx="290" cy="40" r="6"/><circle class="d" cx="30" cy="190" r="4"/>';
    ph.innerHTML='<svg viewBox="0 0 320 240" preserveAspectRatio="xMidYMid slice">'+o+'</svg><small>เกมเดินเที่ยวสงขลา</small><b>Mr. City</b>';
    var pz=f.querySelector('.pz-sold');if(pz)pz.remove();
    f.classList.remove('nopic');f.insertBefore(ph,f.firstChild)}

  /* ---------- 12. highlighter on the first heading of each page only ---------- */
  function heads(){$$('[data-view]').forEach(function(v){
    $$('.ft-hd h2,.mr-l h2,.mr-l h3,.oc-hd h2,.nw2-h,.ct-h h1',v).forEach(function(h,i){var off=i>0;if(h.classList.contains('rv-nohl')!==off)h.classList.toggle('rv-nohl',off)})})}

  function all(){line();covers();about();heads()}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',all);else all();
  addEventListener('load',function(){all();setTimeout(all,800)});
  addEventListener('hashchange',function(){setTimeout(all,300);setTimeout(all,1200)});
  /* rails and search results are built by script: watch only their lists */
  ['#zqC','#zqN','#zqRes'].forEach(function(s){var el=$(s);if(!el)return;var p=0;new MutationObserver(function(){if(p)return;p=raf(function(){p=0;line();covers()})}).observe(el,{childList:true,subtree:true})});
  $$('[data-view="courses"] .mr-r,[data-view="courses"] .ctg').forEach(function(el){var p=0;new MutationObserver(function(){if(p)return;p=raf(function(){p=0;covers()})}).observe(el,{childList:true})});
})();
