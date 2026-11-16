
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* header shadow once the page moves */
  function sc(){document.documentElement.classList.toggle('pl-scrolled',scrollY>8)}
  addEventListener('scroll',sc,{passive:true});sc();

  /* search suggestions: Hamblob heads instead of the 3D clip-art icons */
  function sug(){
    if(!window.Hamblob)return;
    var furs=['orange','cream','pink','mint','lilac'],moods=['happy','calm','wow','happy','calm'];
    document.querySelectorAll('.zq-sug button').forEach(function(b,i){
      if(b.querySelector('.pl-sb'))return;var im=b.querySelector('img');if(!im)return;
      im.classList.add('pl-hide');var w=document.createElement('span');w.className='pl-sb';w.setAttribute('aria-hidden','true');
      w.appendChild(Hamblob.make({fur:furs[i%5],shape:'loaf',mood:moods[i%5],size:38}));b.insertBefore(w,b.firstChild);
      b.addEventListener('pointerenter',function(){var h=w.querySelector('.hb');if(h&&Hamblob.squish)Hamblob.squish(h)});
    });
  }
  /* courses quiz walker: mirror the original walker's motion onto a Hamblob (drag/throw still work on the hidden img) */
  function walker(){
    if(!window.Hamblob)return;
    document.querySelectorAll('.wkz,.wkz-rift').forEach(function(z){
      var img=z.querySelector('img.wk');if(!img||z.querySelector('.pl-wk'))return;
      var box=document.createElement('span');box.className='pl-wk';box.setAttribute('aria-hidden','true');
      var calm=Hamblob.make({fur:'orange',shape:'loaf',mood:'happy',size:84}),wow=Hamblob.make({fur:'orange',shape:'loaf',mood:'wow',size:84}),zz=Hamblob.make({fur:'orange',shape:'loaf',mood:'sleep',size:84});
      [wow,zz].forEach(function(h){h.style.display='none'});box.appendChild(calm);box.appendChild(wow);box.appendChild(zz);z.appendChild(box);
      img.classList.add('pl-skinned');
      var last='';
      function sync(){
        var t=img.style.transform||'';
        /* the sticker faces right by default and is flipped with scale(-1,..); a blob is symmetric, so drop the flip */
        t=t.replace(/scale\((-?[\d.]+),\s*([\d.]+)\)/,function(m,a,b){return 'scale('+Math.abs(+a)+','+b+')'});
        if(t!==last){box.style.transform=t;last=t}
        var held=img.classList.contains('held'),ko=img.classList.contains('ko');
        calm.style.display=held||ko?'none':'';wow.style.display=held&&!ko?'':'none';zz.style.display=ko?'':'none';
      }
      new MutationObserver(sync).observe(img,{attributes:true,attributeFilter:['style','class','src']});sync();
      img.addEventListener('pointerdown',function(){Hamblob.squish&&Hamblob.squish(wow)});
    });
  }
  function run(){sug();walker()}
  if(document.readyState==='complete')run();else addEventListener('load',run);
  addEventListener('hashchange',function(){setTimeout(run,80);setTimeout(function(){dispatchEvent(new Event('resize'))},120)});
  /* 20-pages measures its scenes before this layer's CSS existed: re-measure once */
  addEventListener('load',function(){setTimeout(function(){dispatchEvent(new Event('resize'))},60)});
})();
