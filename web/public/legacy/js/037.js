
(function(){
  addEventListener('scroll',function(){window.__scr=performance.now()},{passive:true});
  function go(){var form=document.getElementById('zqForm'),inp=document.getElementById('zqIn'),go=form&&form.querySelector('.zq-go'),typ=document.getElementById('zqType');if(!form||form.dataset.pull)return;form.dataset.pull=1;
    ['a','b'].forEach(function(c){var h=document.createElement('i');h.className='zq-halo '+c;h.setAttribute('aria-hidden','true');form.insertBefore(h,form.firstChild)});
    /* the empty bar shows the headline's wish as a question; ค้นหา on an empty bar asks it */
    var cur='',tm=0;
    function setQ(){var w=(typ&&typ.textContent||'').trim();if(!w||w===cur)return;cur=w;/* the placeholder is fixed text now: no fade-out/in each time the headline changes */if(inp.getAttribute('placeholder')!=='พิมพ์คำถามได้เลย')inp.setAttribute('placeholder','พิมพ์คำถามได้เลย')}
    if(typ){new MutationObserver(function(){/* while the headline swaps words the bar keeps its prefix instead of flashing back to the default text */if(!inp.value){if(window.__zqStop)window.__zqStop();if(inp.getAttribute('placeholder')!=='พิมพ์คำถามได้เลย')inp.setAttribute('placeholder','พิมพ์คำถามได้เลย')}clearTimeout(tm);tm=setTimeout(function(){var w=(typ.textContent||'').trim();if(w===cur){cur='';setQ()}else setQ()},450)}).observe(typ,{childList:true,characterData:true,subtree:true});setQ()}
    form.addEventListener('submit',function(){if(!inp.value.trim()&&cur){inp.value='อยาก'+cur;inp.dispatchEvent(new Event('input',{bubbles:true}))}},true);
    go&&go.addEventListener('pointerdown',function(){if(!inp.value.trim()&&cur){inp.value='อยาก'+cur;inp.dispatchEvent(new Event('input',{bubbles:true}))}});
    var used=function(){form.classList.add('used')};inp.addEventListener('focus',used);form.addEventListener('submit',used);
    /* bottom pill */
    var fab=document.createElement('button');fab.type='button';fab.className='zq-fab';
    fab.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M20 20l-4-4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>ถามเราได้เลย<small>คอร์ส ค่าย พอร์ต มหาลัย ถามได้หมด</small>';
    document.body.appendChild(fab);
    var zq=document.querySelector('[data-view="home"] .zq'),past=false,near=false;
    function upd(){var home=!location.hash||/^#(home)?$/.test(location.hash);fab.classList.toggle('on',home&&past&&!near&&!document.body.classList.contains('zq-open'))}
    if(zq)new IntersectionObserver(function(es){past=!es[0].isIntersecting&&es[0].boundingClientRect.top<0;upd()}).observe(zq);
    /* hide it over the closing call-to-action and the footer, so it never sits on top of other buttons or text */
    var nearSet=new Set(),foot=document.querySelector('footer'),cta=[].filter.call(document.querySelectorAll('[data-view="home"] section'),function(x){return /สร้างอนาคต|ทัก LINE/.test((x.querySelector('h2')||{}).textContent||'')});
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)nearSet.add(e.target);else nearSet.delete(e.target)});near=nearSet.size>0;upd()});
    if(foot)io.observe(foot);cta.forEach(function(x){io.observe(x)});
    addEventListener('hashchange',upd);
    fab.addEventListener('click',function(){var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;scrollTo({top:0,behavior:rm?'auto':'smooth'});
      var t0=Date.now();(function w(){if(scrollY<10||Date.now()-t0>1200){inp.focus({preventScroll:true})}else requestAnimationFrame(w)})()})}
  if(document.readyState==='complete')go();else addEventListener('load',go);
})();
