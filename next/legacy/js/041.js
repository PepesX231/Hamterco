(function(){
  /* pause every large looping CSS animation while it is off screen; looks identical, frees the GPU while scrolling elsewhere */
  function go(){if(!('IntersectionObserver' in window))return;var io=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('pf-off',!e.isIntersecting)})},{rootMargin:'200px 0px'});
    [].forEach.call(document.querySelectorAll('main *'),function(el){var s=getComputedStyle(el);if(s.animationName==='none'||s.animationIterationCount.indexOf('infinite')<0)return;
      var r=el.getBoundingClientRect();if(r.width*r.height<60000)return;var host=el.closest('section')||el;io.observe(host)})}
  if(document.readyState==='complete')setTimeout(go,1500);else addEventListener('load',function(){setTimeout(go,1500)})})();