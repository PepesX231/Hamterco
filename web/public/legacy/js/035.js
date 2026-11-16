
(function(){/* the two "hof" items (Hall of Fame / all works) share one pane: light only the one that was pressed, and follow the scroll */
  function go(){var side=document.querySelector('.yt-side');if(!side||side.dataset.one)return;side.dataset.one=1;
    var hb=[].slice.call(side.querySelectorAll('button[data-pane="hof"]')),arc=document.getElementById('arc'),lock=0;
    function mark(i){hb.forEach(function(b,k){b.setAttribute('aria-current',String(k===i))})}
    side.addEventListener('click',function(e){var b=e.target.closest('button[data-pane]');if(!b)return;
      side.querySelectorAll('button[data-pane]').forEach(function(x){if(x!==b)x.setAttribute('aria-current','false')});
      setTimeout(function(){side.querySelectorAll('button[data-pane]').forEach(function(x){x.setAttribute('aria-current',String(x===b))});
        if(b.dataset.jump&&arc){lock=Date.now();arc.scrollIntoView({behavior:'smooth',block:'start'})}},0)});
    addEventListener('scroll',function(){if(!arc||!hb.length||Date.now()-lock<900)return;var on=hb[0].getAttribute('aria-current')==='true'||hb[1]&&hb[1].getAttribute('aria-current')==='true';if(!on)return;
      mark(arc.getBoundingClientRect().top<innerHeight*.4?1:0)},{passive:true});
    side.querySelectorAll('button[data-pane]').forEach(function(x){x.style.removeProperty('background');x.classList.remove('cl2-flat')})}
  if(document.readyState==='complete')go();else addEventListener('load',go);addEventListener('hashchange',function(){setTimeout(go,200)});
})();
