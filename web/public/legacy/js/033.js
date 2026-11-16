
(function(){
  /* infinite CSS animations that are off screen are paused (sections far above/below the viewport) */
  function sweep(){var vh=innerHeight;document.getAnimations().forEach(function(a){var e=a.effect&&a.effect.target;if(!e||!e.getBoundingClientRect)return;
    var t=a.effect.getTiming&&a.effect.getTiming();if(!t||t.iterations!==Infinity)return;if(e.closest&&e.closest('.nav'))return;
    var r=e.getBoundingClientRect(),on=r.width>0&&r.bottom>-200&&r.top<vh+200;
    if(!on&&a.playState==='running'){a.pause();a.__pf=1}else if(on&&a.__pf&&a.playState==='paused'){a.play();a.__pf=0}})}
  var q=0;function k(){if(!q)q=setTimeout(function(){q=0;sweep()},250)}
  addEventListener('scroll',k,{passive:true});addEventListener('hashchange',function(){setTimeout(sweep,300)});addEventListener('resize',k);
  if(document.readyState==='complete')setTimeout(sweep,800);else addEventListener('load',function(){setTimeout(sweep,800)});
  setInterval(sweep,3000);
})();
