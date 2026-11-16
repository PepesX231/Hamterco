
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches,html=document.documentElement,io=null;
  /* gooey edge for the mask: black on top, soft drips hanging down (generated once, seeded) */
  (function(){var W=560,H=120,s=7,R=function(){s=(s*16807)%2147483647;return (s-1)/2147483646},d='M0 0H'+W+'V36',x=W;
    while(x>0){var w=34+R()*60,l=R()<.45?40+R()*72:8+R()*14,c=x-w/2,bw=6+R()*7;x-=w;if(x<0)x=0;
      d+='C'+(x+w*.75).toFixed(1)+' 36 '+(c+bw*1.6).toFixed(1)+' 38 '+(c+bw).toFixed(1)+' '+(36+l*.5).toFixed(1)+
         'C'+(c+bw).toFixed(1)+' '+(36+l).toFixed(1)+' '+(c-bw).toFixed(1)+' '+(36+l).toFixed(1)+' '+(c-bw).toFixed(1)+' '+(36+l*.5).toFixed(1)+
         'C'+(c-bw*1.6).toFixed(1)+' 38 '+(x+w*.25).toFixed(1)+' 36 '+x.toFixed(1)+' 36'}
    d+='Z';var svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="none"><path d="'+d+'"/></svg>';
    html.style.setProperty('--mo-edge','url("data:image/svg+xml,'+encodeURIComponent(svg)+'")')})();

  var ok=!rm&&'IntersectionObserver' in window&&CSS.supports&&CSS.supports('(-webkit-mask:none) or (mask:none)');
  function reveal(el){if(!el||el.classList.contains('mo-in'))return;
    if(el.classList.contains('mo-goo')){var h=el.offsetHeight||400;el.style.setProperty('--mo-d',Math.round(Math.max(750,Math.min(1400,500+h*.9)))+'ms')}
    el.classList.add('mo-in');if(io)io.unobserve(el);
    var t=(parseFloat(getComputedStyle(el).getPropertyValue('--mo-d'))||1000)+(+el.dataset.moDelay||0)+(el.classList.contains('mo-kids')?el.children.length*70:0)+150;
    setTimeout(function(){el.classList.add('mo-done')},t)}
  function prep(el){if(el.dataset.moSeen)return;el.dataset.moSeen=1;
    if(el.dataset.moDelay)el.style.setProperty('--mo-w',(+el.dataset.moDelay)+'ms');
    if(el.classList.contains('mo-kids'))[].forEach.call(el.children,function(c,i){c.style.setProperty('--mo-i',Math.min(i,10))});
    if(!io){reveal(el);return}
    var r=el.getBoundingClientRect();if(r.width&&r.top<innerHeight*.92&&r.bottom>0){requestAnimationFrame(function(){reveal(el)});return}
    io.observe(el)}
  function scan(root){(root||document).querySelectorAll('.mo-goo,.mo-rise,.mo-kids').forEach(prep)}
  if(ok){html.classList.add('mo-js');
    io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)reveal(e.target)})},{rootMargin:'0px 0px -10% 0px'})}

  /* press / lift */
  document.addEventListener('pointerup',function(e){var b=e.target.closest&&e.target.closest('.mo-press');if(!b||rm)return;b.classList.remove('mo-boing');void b.offsetWidth;b.classList.add('mo-boing');
    setTimeout(function(){b.classList.remove('mo-boing')},600)},{passive:true});
  function tag(sel,kind,root){(root||document).querySelectorAll(sel).forEach(function(n){n.classList.add('mo-'+kind)});if(kind!=='press'&&kind!=='lift')scan(root)}

  /* smooth scroll */
  function scrollTo(t){var y=typeof t==='number'?t:(t.getBoundingClientRect().top+scrollY-70);window.scrollTo({top:Math.max(0,y),behavior:rm?'auto':'smooth'})}

  /* scroll cue */
  function cue(parent,o){o=o||{};if(!parent||parent.querySelector(':scope > .mo-cue'))return null;
    var b=document.createElement('button');b.type='button';b.className='mo-cue'+(o.dark?' dark':'');b.setAttribute('aria-label',o.label||'เลื่อนลงดูต่อ');
    b.innerHTML='<svg viewBox="0 0 30 46" aria-hidden="true"><defs><radialGradient id="mocg" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#FFE7C4"/><stop offset=".45" stop-color="#F7A23E"/><stop offset="1" stop-color="#C9650F"/></radialGradient></defs>'+
      '<rect x="1" y="1" width="28" height="44" rx="14" fill="rgba(255,252,247,.94)" stroke="rgba(29,23,18,.14)" stroke-width="1.5"/>'+
      '<path class="mo-cd" d="M7 5.5C11 3.5 19 3.5 23 5.5C21 8 18 9 17 12.5C16.4 14.5 13.6 14.5 13 12.5C12 9 9 8 7 5.5Z" fill="url(#mocg)"/>'+
      '<g class="mo-cf"><path d="M15 15C17.2 17.6 18.4 19.6 18.4 21.4C18.4 23.4 16.9 24.8 15 24.8C13.1 24.8 11.6 23.4 11.6 21.4C11.6 19.6 12.8 17.6 15 15Z" fill="url(#mocg)"/><circle cx="13.8" cy="20.8" r="1" fill="#fff" opacity=".85"/></g>'+
      '<path d="M10 39.5Q15 41.5 20 39.5" stroke="rgba(247,162,62,.5)" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg><span>'+(o.label||'เลื่อนลงดูต่อ')+'</span>';
    b.addEventListener('click',function(){var t=typeof o.target==='function'?o.target():o.target;if(t)scrollTo(t);else scrollTo(parent.getBoundingClientRect().bottom+scrollY-60)});
    parent.appendChild(b);
    function chk(){if(scrollY>40){b.classList.add('gone');removeEventListener('scroll',chk)}}
    addEventListener('scroll',chk,{passive:true});chk();return b}

  /* slime progress bar */
  (function(){var bar=document.createElement('div');bar.className='mo-bar';bar.setAttribute('aria-hidden','true');
    bar.innerHTML='<i class="mo-bar-f"><b class="mo-bar-h"><i class="mo-bar-d"></i></b></i>';document.body.appendChild(bar);
    var f=bar.firstChild,d=bar.querySelector('.mo-bar-d'),ly=scrollY,lt=performance.now(),v=0,raf=0,sp=0;
    function u(){raf=0;var m=html.scrollHeight-innerHeight,p=m>0?Math.min(1,Math.max(0,scrollY/m)):0;f.style.transform='translateX('+((p-1)*100).toFixed(3)+'%)';bar.classList.toggle('on',p>.004);
      if(!rm){var t=performance.now(),dt=Math.max(16,t-lt),vv=Math.abs(scrollY-ly)/dt;ly=scrollY;lt=t;v+=(Math.min(2.2,vv*.9)-v)*.35;d.style.setProperty('--v',(.4+v).toFixed(3));
        if(v>.02&&!sp){sp=1;requestAnimationFrame(function k(){v*=.86;d.style.setProperty('--v',(.4+v).toFixed(3));if(v>.02)requestAnimationFrame(k);else sp=0})}}}
    function q(){if(!raf)raf=requestAnimationFrame(u)}
    addEventListener('scroll',q,{passive:true});addEventListener('resize',q);addEventListener('hashchange',function(){setTimeout(q,80);setTimeout(q,900)});u()})();

  window.Motion={scan:scan,reveal:reveal,cue:cue,tag:tag,scrollTo:scrollTo,reduced:rm};
  scan();
  addEventListener('load',function(){scan()});
  addEventListener('hashchange',function(){setTimeout(scan,500)});
})();
