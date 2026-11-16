
(function(){
  'use strict';
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
  var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var LINE='https://page.line.me/jkm4247u?openQrModal=true';
  var LOGO='<svg class="cl2-li" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill-rule="evenodd" d="M19.365 9.863c.349 0 .63.285.63.631 0 .345-.281.63-.63.63H17.61v1.125h1.755c.349 0 .63.283.63.63 0 .344-.281.629-.63.629h-2.386c-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63h2.386c.346 0 .627.285.627.63 0 .349-.281.63-.63.63H17.61v1.125h1.755zm-3.855 3.016c0 .27-.174.51-.432.596-.064.021-.133.031-.199.031-.211 0-.391-.09-.51-.25l-2.443-3.317v2.94c0 .344-.279.629-.631.629-.346 0-.626-.285-.626-.629V8.108c0-.27.173-.51.43-.595.06-.023.136-.033.194-.033.195 0 .375.104.495.254l2.462 3.33V8.108c0-.345.282-.63.63-.63.345 0 .63.285.63.63v4.771zm-5.741 0c0 .344-.282.629-.631.629-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63.346 0 .628.285.628.63v4.771zm-2.466.629H4.917c-.345 0-.63-.285-.63-.629V8.108c0-.345.285-.63.63-.63.348 0 .63.285.63.63v4.141h1.756c.348 0 .629.283.629.63 0 .344-.282.629-.629.629M24 10.314C24 4.943 18.615.572 12 .572S0 4.943 0 10.314c0 4.811 4.27 8.842 10.035 9.608.391.082.923.258 1.058.59.12.301.079.766.038 1.08l-.164 1.02c-.045.301-.24 1.186 1.049.645 1.291-.539 6.916-4.078 9.436-6.975C23.176 14.393 24 12.458 24 10.314"/></svg>';
  var ARW={l:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
           r:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'};
  var raf=window.requestAnimationFrame||function(f){return setTimeout(f,16)};
  function onView(){var v=$('[data-view].on');return v?v.dataset.view:'home'}
  function txt(el){return el?el.textContent.replace(/\s+/g,' ').trim():''}

  /* ---------- 1. home courses: one quiet "next round" line under Port Express ---------- */
  function nextLine(){var fx=$('[data-view="home"] .ft .fx');if(!fx||$('.cl2-next',fx))return;
    /* names come from the page's own course list (the cards that are not open yet) */
    var names=$$('#zqC .qv:not(.on) .qv-tx b').map(txt).filter(function(n,i,a){return n&&a.indexOf(n)===i});
    if(!names.length)return;
    var d=document.createElement('div');d.className='cl2-next';
    d.innerHTML='<div class="cl2-next-t"><b>คอร์สที่จะเปิดรอบถัดไป</b><p></p></div><div class="cl2-next-a"><a class="cl2-bell" href="'+LINE+'" target="_blank" rel="noopener">'+LOGO+'แจ้งเตือนเมื่อเปิด</a><a class="cl2-all" href="#courses">ดูคอร์สทั้งหมด</a></div>';
    $('p',d).textContent=names.length>1?names.slice(0,-1).join(', ')+' และ '+names[names.length-1]:names[0];
    fx.appendChild(d)}

  /* ---------- 3. flat fills for the few gradient chips built in page code ---------- */
  function flat(){
    $$('[data-view="about"] small,[data-view="about"] li,[data-view="works"] button,[data-view="activity"] h2 span,[data-view="activity"] h1 span').forEach(function(e){
      if(e.classList.contains('cl2-flat')||e.closest('.h5f,.t-afo,.yt-side'))return;var bi=getComputedStyle(e).backgroundImage;
      if(bi&&/linear-gradient|radial-gradient/.test(bi)&&!/url\(/.test(bi)){e.classList.add('cl2-flat');e.style.setProperty('background','#F7A23E','important')}})}

  /* ---------- 7. rails ---------- */
  var RAILS=[];
  function stops(r){var cs=[].slice.call(r.children).filter(function(c){return !c.hidden&&c.offsetWidth&&getComputedStyle(c).display!=='none'});
    var max=r.scrollWidth-r.clientWidth;if(!cs.length||max<=4)return [];
    var pl=parseFloat(getComputedStyle(r).scrollPaddingLeft)||0,rl=r.getBoundingClientRect().left,out=[];
    cs.forEach(function(c){var x=Math.round(c.getBoundingClientRect().left-rl+r.scrollLeft-pl);x=Math.max(0,Math.min(max,x));if(!out.length||x-out[out.length-1]>4)out.push(x)});
    if(max-out[out.length-1]>4)out.push(max);return out}
  function Rail(r,dotsHost,opt){var o={r:r,s:[],d:document.createElement('div'),opt:opt||{}};o.d.className='cl2-dots';o.d.setAttribute('role','group');o.d.setAttribute('aria-label','เลื่อนดูการ์ด');
    dotsHost(o.d);r.classList.add(o.opt.own?'cl2-own':'cl2-r');
    function go(x){r.scrollTo({left:x,behavior:RM?'auto':'smooth'})}
    o.go=go;
    o.bleed=function(){if(!o.opt.bleed||!r.offsetParent)return;var p=r.parentElement,pr=p.getBoundingClientRect(),W=document.documentElement.clientWidth;
      var l=Math.max(0,Math.round(pr.left)),rt=Math.max(0,Math.round(W-pr.right));
      /* cards line up with the section heading; the scroll area reaches the screen edges */
      var hd=r.closest('.mr'),hh=hd&&hd.querySelector('.mr-l h2,.mr-l h3'),c0=hh?Math.round(hh.getBoundingClientRect().left):l;
      var col=hh&&hh.offsetWidth?c0:l+4;col=Math.max(12,col);
      var S=function(k,v){r.style.setProperty(k,v,'important')};S('margin-left',-l+'px');S('margin-right',-rt+'px');S('padding-left',col+'px');S('padding-right',col+'px');S('scroll-padding-left',col+'px');S('scroll-padding-right',col+'px');
      r.style.setProperty('--cl2-f',Math.max(28,Math.min(72,l+24))+'px')};
    o.build=function(){o.bleed();o.s=stops(r);var n=o.s.length;
      if(o.d.childElementCount!==n){o.d.innerHTML='';for(var i=0;i<n;i++){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','ไปหน้าที่ '+(i+1)+' จาก '+n);
          (function(i){b.addEventListener('click',function(){go(o.s[i])})})(i);o.d.appendChild(b)}}
      o.d.hidden=n<2;o.upd()};
    o.upd=function(){var x=r.scrollLeft,max=r.scrollWidth-r.clientWidth,a=0,best=1e9;o.s.forEach(function(s,i){var d=Math.abs(s-x);if(d<best){best=d;a=i}});
      [].forEach.call(o.d.children,function(b,i){var on=i===a;if(b.classList.contains('on')!==on)b.classList.toggle('on',on);if(on)b.setAttribute('aria-current','true');else b.removeAttribute('aria-current')});
      var fl=x>4,fr=x<max-4;if(r.classList.contains('cl2-fl')!==fl)r.classList.toggle('cl2-fl',fl);if(r.classList.contains('cl2-fr')!==fr)r.classList.toggle('cl2-fr',fr);
      if(o.opt.onUpd)o.opt.onUpd(x,max)};
    var q=0;r.addEventListener('scroll',function(){if(!q)q=raf(function(){q=0;o.upd()})},{passive:true});
    new MutationObserver(function(){raf(o.build)}).observe(r,{childList:true});
    if(window.ResizeObserver)new ResizeObserver(function(){raf(o.build)}).observe(r);
    RAILS.push(o);o.build();return o}
  function rails(){
    $$('.mr-r').forEach(function(r){if(r.dataset.cl2)return;r.dataset.cl2='1';
      var old=r.closest('.mr-rw');old=old&&old.nextElementSibling&&old.nextElementSibling.classList.contains('ak-dots')?old.nextElementSibling:null;
      if(old)old.classList.add('cl2-off');
      Rail(r,function(d){var host=old||r.closest('.mr-rw')||r;host.parentNode.insertBefore(d,host.nextSibling)},{bleed:!!r.closest('.mr-rw')})});
    /* the course grid on phones scrolls sideways too */
    $$('#zqC2').forEach(function(r){if(r.dataset.cl2)return;var s=getComputedStyle(r);if(s.overflowX!=='auto'&&s.overflowX!=='scroll')return;r.dataset.cl2='1';
      Rail(r,function(d){r.parentNode.insertBefore(d,r.nextSibling)},{})})}
  function relayout(){RAILS.forEach(function(o){o.build()})}

  /* ---------- 8. home activity cards open their activity ---------- */
  var pend=null;
  function actCards(){$$('#zqN .qv').forEach(function(a){if(a.dataset.cl2t)return;var t=txt($('.qv-tx b',a));if(!t)return;
      a.dataset.cl2t=t;a.setAttribute('href','#activity');a.removeAttribute('target');a.removeAttribute('rel');a.setAttribute('aria-label',t+' ดูรายละเอียดกิจกรรม');
      var b=$('.qv-btn',a);if(b){b.title='ดูกิจกรรม';b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'}})}
  function findAct(t){var hit=null;$$('[data-view="activity"] .avc').some(function(c){if(txt($('h3',c))===t){hit=c;return true}});return hit}
  function land(){if(!pend)return;var p=pend,t0=Date.now();
    (function wait(){if(pend!==p)return;var v=$('[data-view="'+p.view+'"].on');
      if(!v){if(Date.now()-t0<4000)setTimeout(wait,80);else pend=null;return}
      var el=p.id?document.getElementById(p.id):findAct(p.title);pend=null;if(!el)return;
      setTimeout(function(){var y=el.getBoundingClientRect().top+scrollY-(p.title?Math.max(80,(innerHeight-el.offsetHeight)/2):76);
        window.scrollTo({top:Math.max(0,y),behavior:RM?'auto':'smooth'});
        if(p.title){el.classList.remove('cl2-hl');void el.offsetWidth;el.classList.add('cl2-hl');setTimeout(function(){el.classList.remove('cl2-hl')},2000)}},120)})()}
  /* ---------- 6. in-page links land on their section, not on a page top ---------- */
  var VIEWS=['home','courses','portex','activity','works','about'];
  document.addEventListener('click',function(e){if(e.defaultPrevented||e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    var a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a)return;var h=a.getAttribute('href').slice(1);
    var act=a.dataset.cl2t,id=null;
    if(act){e.preventDefault();pend={view:'activity',title:act};if(onView()==='activity')land();else location.hash='#activity';return}
    if(h==='about'&&(a.closest('.oc-big')||a.classList.contains('oc-lk')))id='about-real';
    else if(h&&VIEWS.indexOf(h)<0){var t=document.getElementById(h);if(t&&t.closest('[data-view]'))id=h}
    if(!id)return;var tv=document.getElementById(id),v=tv&&tv.closest('[data-view]');if(!v)return;
    e.preventDefault();pend={view:v.dataset.view,id:id};
    if(onView()===v.dataset.view)land();else location.hash='#'+v.dataset.view},true);
  addEventListener('hashchange',function(){if(pend)land()});

  /* ---------- 9. LINE mark ---------- */
  function lineMark(root){$$('a.rv-ln,button.rv-ln',root).forEach(function(a){if(a.querySelector('.cl2-li'))return;a.insertAdjacentHTML('afterbegin',LOGO);a.classList.add('cl2-hasli')})}

  /* ---------- 11. seniors: universities line + flat row ---------- */
  function seniors(){var mc=$('[data-view="home"] .mc');if(!mc||$('.cl2-sen',mc))return;
    var src=$$('#sgrid figure');if(!src.length)return;
    /* universities and counts read from the page's own filter buttons */
    var parts=$$('.mc-u button',mc).filter(function(b){return b.dataset.u}).map(function(b){var n=txt($('b',b)),u=txt(b).replace(n,'').trim();return u+' '+n+' คน'});
    var h2=$('h2',mc),tot=h2?txt($('span',h2)):'';
    if(parts.length){var p=document.createElement('p');p.className='cl2-uni';
      p.textContent='ติด '+(parts.length>1?parts.slice(0,-1).join(' ')+' และ'+parts[parts.length-1]:parts[0]);
      var u=$('.mc-u',mc);u.parentNode.insertBefore(p,u)}
    var w=document.createElement('div');w.className='cl2-sen';
    w.innerHTML='<div class="cl2-sr" aria-label="รุ่นพี่ที่ลงโปสเตอร์แล้ว"></div><div class="cl2-ctl"><button type="button" class="cl2-arw" data-d="-1" aria-label="เลื่อนไปทางซ้าย">'+ARW.l+'</button><button type="button" class="cl2-arw" data-d="1" aria-label="เลื่อนไปทางขวา">'+ARW.r+'</button></div>';
    var sr=$('.cl2-sr',w);
    src.forEach(function(f){var c=document.createElement('figure');c.dataset.u=f.dataset.u||'';var im=$('img',f),cap=$('figcaption',f);
      var i2=document.createElement('img');i2.src=im.getAttribute('src');i2.alt=im.alt||'';i2.loading='lazy';i2.decoding='async';c.appendChild(i2);
      if(cap){var fc=document.createElement('figcaption');fc.innerHTML=cap.innerHTML.replace(/<br\s*\/?>/gi,' ').replace(/ · /g,' ');c.appendChild(fc)}
      sr.appendChild(c)});
    var st=$('#mcSt',mc);(st||$('.mc-cap',mc)).parentNode.insertBefore(w,st||$('.mc-cap',mc));
    var ctl=$('.cl2-ctl',w),A=$$('.cl2-arw',w);
    var o=Rail(sr,function(d){ctl.insertBefore(d,A[1])},{own:1,onUpd:function(x,max){A[0].disabled=x<=4;A[1].disabled=x>=max-4}});
    A.forEach(function(b){b.addEventListener('click',function(){var d=+b.dataset.d,x=sr.scrollLeft,t=null;
      o.s.forEach(function(s){if(d>0&&s>x+4&&t==null)t=s;if(d<0&&s<x-4)t=s});if(t!=null)o.go(t)})});
    $$('.mc-u button',mc).forEach(function(b){b.addEventListener('click',function(){var k=b.dataset.u||'';
      $$('figure',sr).forEach(function(f){f.hidden=!!k&&f.dataset.u!==k});sr.scrollLeft=0;raf(o.build)})})}

  /* ---------- 12. the pink activity type goes warm ---------- */
  function warm(){$$('[data-view="activity"] .avc').forEach(function(c){var v=(c.style.getPropertyValue('--pz-chip')||'').trim().toUpperCase();if(v!=='#FFD3E3')return;
    c.style.setProperty('--pz-chip','#F1E2CF');c.style.setProperty('--pz-l','#FBF3E8');c.style.setProperty('--pz-bg','#F2DFC6');c.style.setProperty('--tc','#A8551A')})}

  /* ---------- 4. search answers: no IoT / robot chips on the home search ---------- */
  function noIot(){var res=$('#zqRes');if(!res)return;
    $$('button,[data-q]',res).forEach(function(b){if(b.hidden)return;var t=txt(b);if(/IoT|หุ่นยนต์/.test(t)&&!/IoT|หุ่นยนต์|iot|robot/i.test(($('#zqIn')||{}).value||''))b.hidden=true});
    var w=document.createTreeWalker(res,NodeFilter.SHOW_TEXT,null),n;while((n=w.nextNode())){if(n.nodeValue.indexOf('เกม เว็บ และ IoT')>-1)n.nodeValue=n.nodeValue.replace(/เกม เว็บ และ IoT/g,'เกม เว็บ และแอป')}}

  /* ---------- 14. closing panel: signed by the team ---------- */
  function sign(){var p=$('[data-view="home"] .end-in > p');if(!p||$('.cl2-sig',p))return;var s=document.createElement('span');s.className='cl2-sig';s.textContent='ทีม Hamster Hub';p.appendChild(s)}

  function all(){flat();rails();actCards();lineMark();warm()}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',all);else all();
  addEventListener('load',function(){all();setTimeout(all,700)});
  addEventListener('resize',function(){raf(relayout)});
  addEventListener('hashchange',function(){setTimeout(function(){all();relayout()},250);setTimeout(function(){all();relayout()},1300)});
  /* script-built lists: watch only them, act only when something is missing (no loops) */
  ['#zqN','#zqRes'].forEach(function(s){var el=$(s);if(!el)return;var p=0;
    new MutationObserver(function(){if(p)return;p=raf(function(){p=0;if(s==='#zqN')actCards();if(s==='#zqRes'){lineMark(el);noIot()}})}).observe(el,{childList:true,subtree:true})});
})();
