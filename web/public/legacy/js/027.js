
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function q(s){return document.querySelector(s)}
  function el(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.textContent=h;return e}

  /* ---- "สิ่งที่ Hamster Hub สร้าง": credits for each work, the matching picture lights up on hover ---- */
  /* one short result line per work; the long descriptions were too much to read */
  var ROWS=[
    {items:[{n:'Mr. City',w:'',r:'ขายให้สวนสัตว์สงขลาแล้ว',m:[1]},
            {n:'PHC Map',w:'',r:'เด็กใช้เรียนแล้วกว่า 1,000 คน',m:[0]},
            {n:'Hamster Quest',w:'',r:'กำลังจะใช้ในมหาวิทยาลัย',m:[2]}]},
    {h3:'แอปฝึกพูดที่น้องไอดินทำเอง',one:1,
     items:[{n:'REVOICE',w:'',r:'ชนะ NSC 2025 ระดับประเทศ'}]},
    {items:[{n:'SLASH//SPEED',w:'',r:'เกมของน้องดินสอ',m:[0]},
            {n:'Apocalypis Building',w:'',r:'เกมของน้องฟาร์',m:[1]},
            {n:'Eugation Strike',w:'',r:'เกมของน้องไผ่',m:[2]}]}];
  function credits(){[].forEach.call(document.querySelectorAll('section .oc-in>.oc-r'),function(r,i){var d=ROWS[i],t=r.querySelector('.oc-t');if(!d||!t||t.querySelector('.ocl'))return;
    var m=r.querySelector('.oc-m'),h=t.querySelector('h3');if(d.h3&&h)h.textContent=d.h3;
    var ul=el('ul','ocl'+(d.one?' one':''));
    d.items.forEach(function(it){var li=el('li'),sp=el('span',null,it.w);li.appendChild(el('b',null,it.n));sp.appendChild(el('i',null,it.r));li.appendChild(sp);ul.appendChild(li);
      if(it.m&&m){li.addEventListener('pointerenter',function(){m.classList.add('ocl-on');[].forEach.call(m.children,function(c,k){c.classList.toggle('ocl-hi',it.m.indexOf(k)>=0)})});
        li.addEventListener('pointerleave',function(){m.classList.remove('ocl-on')})}});
    var p=t.querySelector('p');t.insertBefore(ul,p?p.nextSibling:null);
    if(d.note){var n=el('p','ocl-n',d.note);n.style.display='block';t.insertBefore(n,ul.nextSibling)}})}

  /* ---- seniors fan: spaced to both edges, turned toward the middle, draggable ---- */
  var busy=false;
  function fan(){var st=document.getElementById('mcSt');if(!st||!st.offsetWidth)return;
    var cs=[].slice.call(st.querySelectorAll('.mc-c'));if(!cs.length)return;
    var on=st.querySelector('.mc-c.on'),a=Math.max(0,cs.indexOf(on)),n=cs.length,
        W=(st.closest('.mc-in')||st).getBoundingClientRect().width,cw=cs[0].offsetWidth,mob=innerWidth<640,
        sc=function(d){return Math.max(.68,1-d*(mob?.12:.085))},pos=[0];
    for(var d=1;d<=Math.floor(n/2)+1;d++)pos[d]=pos[d-1]+cw*(sc(d-1)+sc(d))/2*(mob?.62:.74);
    var half=W/2,m=1;while(m<pos.length-1&&pos[m]<half*.86)m++;var f=pos[m]>=half*.86?Math.min(1.2,Math.max(.86,half/pos[m])):1;pos=pos.map(function(p){return p*f});
    cs.forEach(function(c,k){var o=k-a;if(o>n/2)o-=n;if(o<-n/2)o+=n;var ab=Math.abs(o),s=sc(ab),x=(o<0?-1:1)*pos[ab],
        vis=Math.abs(x)-cw*s/2<W/2+4,prev=c.dataset.fo===undefined?o:+c.dataset.fo,ry=ab?(o<0?1:-1)*Math.min(16+ab*4,32):0;
      if(Math.abs(prev-o)>1||(prev*o<0&&ab>1)){c.style.transition='none';c.dataset.jump='1'}
      c.dataset.fo=o;
      c.style.transform='translate(-50%,-50%) translateX('+x.toFixed(1)+'px) translateY('+Math.min(ab*ab*5,40)+'px) scale('+s.toFixed(3)+')';
      c.style.zIndex=40-ab;c.style.opacity=vis?1:0;c.style.filter=ab?'brightness('+Math.max(.62,1-ab*.09).toFixed(2)+') saturate('+Math.max(.7,1-ab*.06).toFixed(2)+')':'none';
      if(!ab){}else{var im=c.querySelector('img');if(im)im.style.transform=''}});
    requestAnimationFrame(function(){cs.forEach(function(c){if(c.dataset.jump){c.offsetWidth;c.style.transition='';delete c.dataset.jump}})})}
  function queue(){if(busy)return;busy=true;Promise.resolve().then(function(){busy=false;fan()})}
  function step(st,d){var cs=[].slice.call(st.querySelectorAll('.mc-c')),on=st.querySelector('.mc-c.on'),a=Math.max(0,cs.indexOf(on)),t=cs[(a+d+cs.length)%cs.length];if(t)t.click()}
  function watch(){var st=document.getElementById('mcSt');if(!st||st.dataset.fan)return;st.dataset.fan='1';
    /* the page re-lays on every step; we only listen to class/children and only write style, so no loop */
    new MutationObserver(queue).observe(st,{subtree:true,childList:true,attributes:true,attributeFilter:['class']});fan();
    /* drag / swipe through the seniors */
    var down=false,x0=0,moved=0,supp=false;
    st.addEventListener('pointerdown',function(e){if(e.button)return;down=true;x0=e.clientX;moved=0;supp=false});
    addEventListener('pointermove',function(e){if(!down)return;var dx=e.clientX-x0,stp=Math.max(46,(st.querySelector('.mc-c')||st).offsetWidth*.32);
      if(Math.abs(dx)>8&&!st.classList.contains('drag'))st.classList.add('drag');
      if(Math.abs(dx)>=stp){step(st,dx<0?1:-1);x0=e.clientX;moved++;supp=true}});
    addEventListener('pointerup',function(){if(!down)return;down=false;st.classList.remove('drag');if(moved)supp=true});
    addEventListener('pointercancel',function(){down=false;st.classList.remove('drag')});
    st.addEventListener('click',function(e){if(supp&&e.isTrusted){e.stopPropagation();e.preventDefault();supp=false}},true);
    st.addEventListener('dragstart',function(e){e.preventDefault()});
  }

  /* ---- nav: every link rolls to a hint of its page ---- */
  var HINT={};
  function nav(){var nx=document.getElementById('nvNext');if(nx&&nx.textContent.indexOf('ถัดไป')===0)nx.textContent=nx.textContent;
    Object.keys(HINT).forEach(function(k){var a=document.querySelector('.nav-in>a.'+k);if(!a||a.querySelector('.roll'))return;var sp=a.querySelector('span');if(!sp)return;
      var r=el('span','roll'),one=el('span',null,sp.textContent),two=el('span','nx',HINT[k]);two.setAttribute('aria-hidden','true');r.appendChild(one);r.appendChild(two);a.replaceChild(r,sp)})}

  function go(){credits();watch();nav();addEventListener('resize',fan);addEventListener('hashchange',function(){setTimeout(function(){credits();watch();fan()},150)})}
  if(document.readyState==='complete')go();else addEventListener('load',go);
})();
