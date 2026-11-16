
(function(){
  function put(){[].forEach.call(document.querySelectorAll('.fx-main .fx-media'),function(m){if(m.querySelector('.ow-rec'))return;var live=m.querySelector('.ft-live');
    var t=document.createElement('span');t.className='ow-rec';t.textContent='คอร์สแนะนำ';m.appendChild(t);
    function pos(){var l=live?live.offsetLeft+live.offsetWidth+8:16;t.style.left=l+'px';if(live)t.style.top=live.offsetTop+'px'}
    pos();if(window.ResizeObserver&&live)new ResizeObserver(pos).observe(live)})}
  if(document.readyState==='complete')put();else addEventListener('load',put);
})();
