
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function el(tag,cls,html){var e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e}

  /* ---------- 1. startup stage ---------- */
  function stage(){
    var big=document.querySelector('.hbx .oc-r.oc-big');if(!big||big.getAttribute('data-ar'))return;big.setAttribute('data-ar','1');
    var m=big.querySelector('.oc-m'),ol=big.querySelector('.oc-st'),t=big.querySelector('.oc-t');
    if(m){[['c1','PHC Map เกมสอนเขียน Python'],['c2','Hamster Quest'],['c3','หน้าเควสต์']].forEach(function(c){var s=el('span','ar-cap '+c[0]);s.textContent=c[1];s.setAttribute('aria-hidden','true');m.appendChild(s)})}
    if(ol&&t){
      /* one plain line under each step: what the student does there */
      var SX=['น้องคิดว่าจะทำอะไร ให้ใครใช้','น้องลงมือเขียนโปรแกรมเอง','ให้คนจริงลองใช้ แล้วน้องแก้ให้ดีขึ้น','มีคนซื้อหรือใช้ผลงานของน้องจริง'];
      [].forEach.call(ol.querySelectorAll('li'),function(li,i){if(SX[i]&&!li.querySelector('.ar-sx')){var x=el('span','ar-sx');x.textContent=SX[i];li.appendChild(x)}});
      var led=el('ul','ar-led',
        '<li class="ar-led-h">ผลงานของน้องที่มีคนใช้จริงแล้ว</li>'+
        '<li><small>Mr. City</small><b>สวนสัตว์สงขลา</b><span>ซื้อไปใช้แล้ว</span></li>'+
        '<li><small>PHC Map</small><b>1,000+ คน</b><span>เรียนเขียน Python จากเกมนี้แล้ว</span></li>'+
        '<li><small>Hamster Quest</small><b>มหาวิทยาลัย</b><span>กำลังเตรียมนำไปใช้</span></li>');
      ol.parentNode.insertBefore(led,ol.nextSibling);
      /* the climbing path */
      var NS='http://www.w3.org/2000/svg',svg=document.createElementNS(NS,'svg');svg.setAttribute('class','ar-path');svg.setAttribute('aria-hidden','true');
      var pb=document.createElementNS(NS,'path'),pf=document.createElementNS(NS,'path');pb.setAttribute('class','b');pf.setAttribute('class','f');pf.setAttribute('pathLength','1');
      svg.appendChild(pb);svg.appendChild(pf);ol.insertBefore(svg,ol.firstChild);
      var lastD='';
      function draw(){
        var lis=ol.querySelectorAll('li');if(lis.length<2||!ol.clientWidth)return;
        var d='',prev=null;
        [].forEach.call(lis,function(li){var x=li.offsetLeft+17,y=li.offsetTop+17;
          if(!prev)d='M'+x+' '+y;else{var h=(x-prev.x)*.5;d+=' C'+(prev.x+h)+' '+prev.y+' '+(x-h)+' '+y+' '+x+' '+y}prev={x:x,y:y}});
        if(d!==lastD){lastD=d;pb.setAttribute('d',d);pf.setAttribute('d',d)}
      }
      draw();
      if('ResizeObserver' in window)new ResizeObserver(draw).observe(ol);else addEventListener('resize',draw);
      if(document.fonts&&document.fonts.ready)document.fonts.ready.then(draw);
    }
    /* no reveal: the steps and the ledger are always readable */
  }

  /* ---------- 2a. rank lockup ---------- */
  function rank(){
    [].forEach.call(document.querySelectorAll('.fx-main .rc:not(.ar-rk)'),function(rc){
      [].slice.call(rc.childNodes).forEach(function(n){if(n.nodeType===3)rc.removeChild(n)});
      rc.setAttribute('role','img');rc.setAttribute('aria-label','คอร์สแนะนำอันดับ 1');
      rc.appendChild(el('span','ar-rk-t','คอร์สแนะนำ<br>อันดับ'));rc.appendChild(el('span','ar-rk-n','1'));
      rc.classList.add('ar-rk');
    });
  }

  /* ---------- 2c. closing wall ---------- */
  var COVERS=['ar-melody-duel','work-phi-krahang','ar-heat-thieves','ar-a-picturesque-breakfast','ar-the-collector','ar-nampun','work-eugation-strike','ar-night-fear','ar-gamejam-x','ar-bidet-blaster','ar-woven-citadel',
    'work-stressstrike','ar-ecoeats-mas','work-midnight-at-roadside','ar-endlessly','ar-ghostly-prisoner-demo','work-hot-hot-hot','ar-together-forever'];
  function wall(){
    var host=document.querySelector('[data-view="home"] .end-in');if(!host||host.querySelector('.ar-wall'))return;
    var w=el('div','ar-wall');w.setAttribute('role','group');w.setAttribute('aria-label','เกมที่น้องๆ สร้าง กดเพื่อดูผลงาน');
    var tiles=[],shown=[];
    for(var i=0;i<12;i++){var t=el('a','ar-tile','<img class="on" alt="" loading="lazy" decoding="async" src="/Hamterco/img/'+COVERS[i]+'.webp"><img alt="" decoding="async">');
      t.href='#works';t.setAttribute('data-pane','hof');t.setAttribute('data-cover',COVERS[i]);label(t,COVERS[i]);w.appendChild(t);tiles.push(t);shown.push(COVERS[i])}
    /* a cover opens that game in the works page: Hall of Fame games play in the feed, the others open their clip */
    w.addEventListener('click',function(e){var t=e.target.closest('.ar-tile');if(!t)return;var c=t.getAttribute('data-cover');
      setTimeout(function open(){var v=document.querySelector('[data-view="works"]');if(!v||!v.offsetParent)return;
        var im=document.querySelector('#vgrid img[src$="'+c+'.webp"],#arcG img[src$="'+c+'.webp"]'),b=im&&im.closest('.vc,.ac');
        if(b){b.scrollIntoView({block:'center'});b.click()}},700)});
    function label(t,c){var im=document.querySelector('#vgrid img[src$="'+c+'.webp"],#arcG img[src$="'+c+'.webp"]'),card=im&&im.closest('.vc,.ac'),nm=card&&card.querySelector('b,h3');
      t.setAttribute('aria-label','ดูผลงาน '+(nm?nm.textContent.trim():'ของน้อง'))}
    var mine=el('div','ar-mine','<svg aria-hidden="true"><rect x="1" y="1" rx="9" ry="9" style="width:calc(100% - 2px);height:calc(100% - 2px)"/></svg><span>ที่ว่างนี้<br>รอผลงานของน้อง</span>');
    host.appendChild(w);
    if(rm)return;
    var timer=0,last=-1;
    function swap(){
      var vis=tiles.filter(function(t){return t.offsetParent!==null});if(!vis.length)return;
      var k;do{k=Math.floor(Math.random()*vis.length)}while(vis.length>1&&k===last);last=k;
      var t=vis[k],ti=tiles.indexOf(t),free=COVERS.filter(function(c){return shown.indexOf(c)<0});if(!free.length)return;
      var next=free[Math.floor(Math.random()*free.length)],im=t.querySelectorAll('img'),a=im[0].classList.contains('on')?im[0]:im[1],b=a===im[0]?im[1]:im[0];
      b.onload=function(){b.onload=null;b.classList.add('on');a.classList.remove('on');shown[ti]=next;t.setAttribute('data-cover',next);label(t,next)};
      b.src='/Hamterco/img/'+next+'.webp';
    }
    new IntersectionObserver(function(es){var on=es[0].isIntersecting;
      if(on&&!timer){timer=setInterval(function(){if(!document.hidden)swap()},2600);w.classList.add('run')}
      else if(!on&&timer){clearInterval(timer);timer=0;w.classList.remove('run')}
    },{threshold:.2}).observe(w);
  }

  /* ---------- 2d. activity posters ---------- */
  function rng(seed){var s=seed>>>0||1;return function(){s^=s<<13;s>>>=0;s^=s>>>17;s^=s<<5;s>>>=0;return s/4294967296}}
  function hash(str){var h=2166136261;for(var i=0;i<str.length;i++){h^=str.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
  function f1(n){return Math.round(n*10)/10}
  function contours(r){   /* camp: terrain lines around a peak */
    var cx=70+r()*70,cy=50+r()*40,p1=r()*6.28,p2=r()*6.28,a=.1+r()*.08,b=.05+r()*.05,o='';
    for(var k=0;k<9;k++){var R=10+k*20+k*k*.9,pts=[];
      for(var i=0;i<36;i++){var th=i/36*6.2832,rr=R*(1+a*Math.sin(3*th+p1+k*.22)+b*Math.sin(5*th+p2-k*.3));pts.push([cx+rr*Math.cos(th)*1.25,cy+rr*Math.sin(th)*.82])}
      var d='';for(i=0;i<pts.length;i++){var q=pts[i],n=pts[(i+1)%pts.length],mx=(q[0]+n[0])/2,my=(q[1]+n[1])/2;d+=(i?' Q'+f1(q[0])+' '+f1(q[1])+' ':'M'+f1((pts[pts.length-1][0]+q[0])/2)+' '+f1((pts[pts.length-1][1]+q[1])/2)+' Q'+f1(q[0])+' '+f1(q[1])+' ')+f1(mx)+' '+f1(my)}
      o+='<path d="'+d+'Z"/>'}
    return o+'<path class="a" d="M'+f1(cx-4)+' '+f1(cy)+'h8M'+f1(cx)+' '+f1(cy-4)+'v8"/>';
  }
  function drafting(r){   /* workshop: drafting grid with construction lines */
    var o='',ox=r()*20,oy=r()*20;
    for(var x=ox;x<320;x+=20)o+='<path d="M'+f1(x)+' 0V180"/>';
    for(var y=oy;y<180;y+=20)o+='<path d="M0 '+f1(y)+'H320"/>';
    var ax=ox+20*(2+Math.floor(r()*3)),ay=oy+20*(1+Math.floor(r()*2)),R=60+Math.floor(r()*3)*20;
    o+='<path class="a" d="M'+f1(ax)+' '+f1(ay+R)+'A'+R+' '+R+' 0 0 0 '+f1(ax+R)+' '+f1(ay)+'"/>';
    o+='<path class="a" d="M'+f1(ax)+' '+f1(ay)+'L'+f1(ax+R*.707)+' '+f1(ay+R*.707)+'"/>';
    o+='<path class="a" d="M'+f1(ax-5)+' '+f1(ay)+'h10M'+f1(ax)+' '+f1(ay-5)+'v10"/>';
    return o;
  }
  function orbits(r){   /* project: long arcs of one orbit system */
    var cx=40+r()*60,cy=-30+r()*40,rot=-22+r()*12,o='<g transform="rotate('+f1(rot)+' '+f1(cx)+' '+f1(cy)+')">';
    for(var k=0;k<6;k++){var rx=70+k*52,ry=rx*.52;o+='<ellipse cx="'+f1(cx)+'" cy="'+f1(cy)+'" rx="'+rx+'" ry="'+f1(ry)+'"/>';
      if(k===1||k===3||k===4){var th=.5+r()*1.4;o+='<circle class="d" r="'+(k===3?4.2:2.8)+'" cx="'+f1(cx+rx*Math.cos(th))+'" cy="'+f1(cy+ry*Math.sin(th))+'"/>'}}
    return o+'</g>';
  }
  function ridges(r){   /* camp: hills one behind another */
    var o='';for(var k=0;k<7;k++){var y0=40+k*20,ph=r()*6.28,amp=8+r()*10,d='M0 '+f1(y0);
      for(var x=0;x<=320;x+=16)d+=' L'+x+' '+f1(y0+amp*Math.sin(x/(38+k*4)+ph)+.4*amp*Math.sin(x/13+ph*2));o+='<path'+(k===3?' class="a"':'')+' d="'+d+'"/>'}
    return o;
  }
  function sundots(r){   /* camp: a halftone sun */
    var cx=200+r()*80,cy=40+r()*40,o='';
    for(var y=8;y<180;y+=14)for(var x=8;x<320;x+=14){var dd=Math.hypot(x-cx,y-cy),rr=Math.max(0,3.4-dd/60);if(rr>.5)o+='<circle class="dl" cx="'+x+'" cy="'+y+'" r="'+f1(rr)+'"/>'}
    return o+'<circle class="a" cx="'+f1(cx)+'" cy="'+f1(cy)+'" r="'+f1(26+r()*10)+'"/>';
  }
  var PAL={camp:['sand','mint','sky','lilac','pink'],work:['ink','navy'],proj:['orange','peach']},
      PAT={camp:[contours,ridges,sundots],work:[drafting,sundots],proj:[orbits,ridges]};
  function posters(root){
    var n={camp:0,work:0,proj:0};
    [].forEach.call((root||document).querySelectorAll('[data-view="activity"] .avc-ty:not(.ar-po)'),function(ty){
      var card=ty.closest('.avc'),b=ty.querySelector('b');if(!card||!b)return;
      var dEl=card.querySelector('.avc-d'),sp=dEl&&dEl.querySelector('span'),kind=sp?sp.textContent:'',date=dEl?dEl.textContent.replace(kind,'').trim():'';
      var type=/เวิร์ก/.test(kind)?'work':/โครงการ|โชว์|แข่ง/.test(kind)?'proj':'camp',i=n[type]++;
      var r=rng(hash(b.textContent+date)),g=PAT[type][i%PAT[type].length](r),pal=PAL[type][i%PAL[type].length];
      var day=(date.match(/\d+/)||[''])[0],mon=(date.match(/[ก-๙]+\.[ก-๙]+\./)||[''])[0];
      var svg='<svg class="ar-po-g" viewBox="0 0 320 180" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'+g+'</svg>';
      ty.insertAdjacentHTML('afterbegin',svg);
      if(day)ty.insertAdjacentHTML('beforeend','<span class="ar-po-d" aria-hidden="true"><i>'+day+'</i><u>'+mon+'</u></span>');
      ty.classList.add('ar-po','t-'+type,'p-'+pal);
    });
    /* "น้องได้" lines: a line shared by many cards says nothing, keep it only on the first card */
    var gs=[].slice.call(document.querySelectorAll('[data-view="activity"] .avc .avc-g')),cnt={},seen={};
    gs.forEach(function(g){var k=g.textContent.trim();cnt[k]=(cnt[k]||0)+1});
    gs.forEach(function(g){var k=g.textContent.trim();var hide=cnt[k]>3&&seen[k];seen[k]=1;if(g.hidden!==!!hide)g.hidden=!!hide});
  }

  function go(){
    rank();posters();
    var act=document.querySelector('[data-view="activity"]');
    if(act&&'MutationObserver' in window){var q=0;new MutationObserver(function(){if(q)return;q=requestAnimationFrame(function(){q=0;if(act.querySelector('.avc-ty:not(.ar-po)'))posters()})}).observe(act,{childList:true,subtree:true})}
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go();
  addEventListener('load',function(){rank();posters()});
})();
