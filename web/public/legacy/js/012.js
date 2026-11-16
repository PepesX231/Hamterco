
/* headline: keep only the clean, readable type styles (the neon / glitch / outline / script ones read badly) */
(function(){var h=document.querySelector('[data-view="home"] .zq-h');if(!h)return;var OK=['kanit'],k=0;
  function fix(){var f=h.dataset.f;if(f&&OK.indexOf(f)<0){k=(k+1)%OK.length;h.dataset.f=OK[k]}}
  fix();new MutationObserver(fix).observe(h,{attributes:true,attributeFilter:['data-f']})})();
