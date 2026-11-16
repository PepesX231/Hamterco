
(function(){/* the animated drip strip under the hero only plays while on screen */
  function go(){var j=document.querySelectorAll('.je');if(!('IntersectionObserver' in window))return;var io=new IntersectionObserver(function(es){es.forEach(function(e){e.target.style.visibility=e.isIntersecting?'':'hidden'})},{rootMargin:'250px 0px'});
    j.forEach(function(e){io.observe(e)})}
  if(document.readyState==='complete')go();else addEventListener('load',go)})();
