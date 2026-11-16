
(function(){
  function go(d){var st=document.getElementById('mcSt');if(!st)return;var cs=[].slice.call(st.querySelectorAll('.mc-c'));if(!cs.length)return;
    var on=st.querySelector('.mc-c.on'),k=on?+on.dataset.k:0,n=cs.length,t=st.querySelector('.mc-c[data-k="'+((k+d+n)%n)+'"]');if(t)t.click();cnt()}
  function cnt(){var st=document.getElementById('mcSt'),c=document.querySelector('.mc2-cnt');if(!st||!c)return;var n=st.querySelectorAll('.mc-c').length,on=st.querySelector('.mc-c.on');c.textContent=(on?+on.dataset.k+1:1)+' / '+n}
  function build(){var cap=document.querySelector('[data-view="home"] .mc .mc-cap');if(!cap||cap.parentNode.classList.contains('mc2-nav'))return;
    var nav=document.createElement('div');nav.className='mc2-nav';cap.parentNode.insertBefore(nav,cap);
    var ar='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>';
    var p=document.createElement('button');p.type='button';p.setAttribute('aria-label','รุ่นพี่คนก่อนหน้า');p.innerHTML=ar;
    var x=document.createElement('button');x.type='button';x.setAttribute('aria-label','รุ่นพี่คนถัดไป');x.innerHTML=ar.replace('M15 5l-7 7 7 7','M9 5l7 7-7 7');
    nav.appendChild(p);nav.appendChild(cap);nav.appendChild(x);
    var c=document.createElement('p');c.className='mc2-cnt';nav.parentNode.insertBefore(c,nav.nextSibling);
    p.addEventListener('click',function(){go(-1)});x.addEventListener('click',function(){go(1)});
    var st=document.getElementById('mcSt');if(st){new MutationObserver(cnt).observe(st,{subtree:true,attributes:true,attributeFilter:['class'],childList:true});
      st.tabIndex=0;st.setAttribute('aria-label','รุ่นพี่ที่ติดมหาลัย ใช้ลูกศรซ้ายขวาเพื่อเลื่อน');st.addEventListener('keydown',function(e){if(e.key==='ArrowLeft'){e.preventDefault();go(-1)}else if(e.key==='ArrowRight'){e.preventDefault();go(1)}})}
    cnt()}
  if(document.readyState==='complete')build();else addEventListener('load',build);
})();
