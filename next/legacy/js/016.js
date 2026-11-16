
(function(){
  /* 2. wrap highlighted section titles in an inline span (text only; icons stay outside) */
  var SEL='.ft-hd h2,.mr-l h2,.mr-l h3,.oc-hd h2,.nw2-h,.ct-h h1';
  function hl(){
    document.querySelectorAll(SEL).forEach(function(h){
      if(h.closest('.zq')||h.querySelector('.qa-hl'))return;
      var nodes=[].filter.call(h.childNodes,function(n){return n.nodeType===3?n.textContent.trim():!(n instanceof SVGElement)&&n.tagName!=='IMG'});
      if(!nodes.length)return;
      var s=document.createElement('span');s.className='qa-hl';
      h.insertBefore(s,nodes[0]);nodes.forEach(function(n){s.appendChild(n)});
      h.classList.add('qa-hl-on');
    });
  }
  /* 5. quiz progress in the empty result box */
  function quiz(){
    var f=document.getElementById('fitQ'),r=document.getElementById('fitR');if(!f||!r||f.dataset.qa)return;f.dataset.qa='1';
    function draw(){
      var d=new FormData(f),n=['g','p','t'].filter(function(k){return d.get(k)}).length;
      if(n===3)return;            /* the page's own script writes the result */
      var box=r.querySelector('.qa-fp');
      if(!box){r.className='fit-r';r.innerHTML='<div class="qa-fp"><b>ตอบแล้ว <span>0</span> จาก 3 ข้อ</b><div class="qa-fp-bar" aria-hidden="true"><i></i><i></i><i></i></div><p>ตอบครบแล้วคอร์สที่เหมาะกับน้องจะขึ้นตรงนี้</p></div>';box=r.querySelector('.qa-fp')}
      box.querySelector('span').textContent=n;
      var k=['g','p','t'];box.querySelectorAll('.qa-fp-bar i').forEach(function(i,x){i.classList.toggle('on',!!d.get(k[x]))});
    }
    f.addEventListener('change',draw);draw();
  }
  function run(){hl();quiz()}
  if(document.readyState==='loading')addEventListener('DOMContentLoaded',run);else run();
  addEventListener('load',run);
  addEventListener('hashchange',function(){setTimeout(run,60)});
})();
