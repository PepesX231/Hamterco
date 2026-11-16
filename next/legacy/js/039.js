
(function(){
  function quiet(e){var t=e.target;if(!t||!t.closest)return;var zq=t.closest('[data-view="home"] .zq');if(!zq)return;
    if(t.closest('form,input,button,a,label,select,textarea,.zq-ch,.zq-pop,#zqRes,#zqSug,[role="button"]'))return;
    e.stopImmediatePropagation();if(e.type==='click')e.preventDefault()}
  ['pointerdown','mousedown','click','touchstart','dblclick'].forEach(function(k){window.addEventListener(k,quiet,{capture:true,passive:k!=='click'})});
  function go(){var h=document.querySelector('.zq-h');if(h){h.removeAttribute('title');h.setAttribute('data-f','kanit');h.removeAttribute('tabindex');h.removeAttribute('role')}}
  if(document.readyState==='complete')go();else addEventListener('load',go);
})();
