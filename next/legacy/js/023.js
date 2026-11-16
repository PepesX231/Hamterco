
(function(){
  var MAP={'hamstarter':'cb-hamstarter','port70':'cb-port70','project express':'cb-pexp','national project':'cb-national','business project':'cb-business','python pro pack':'cb-python'};
  function key(t){return (t||'').toLowerCase().replace(/\s+/g,' ').trim()}
  function run(){
    /* seniors captions: name + faculty on separate lines */
    [].forEach.call(document.querySelectorAll('.sn2-c figcaption'),function(fc){if(fc.dataset.ok)return;fc.dataset.ok=1});
    /* the two secondary course cards on home and courses: portrait banners instead of a congratulation poster */
    [].forEach.call(document.querySelectorAll('.fx-row .fx-s'),function(c){var b=c.querySelector('.fx-sb>b');var k=key(b&&b.textContent);var im=c.querySelector('.fx-si img');
      if(!im||im.dataset.ow)return;if(k==='hamstarter'){im.src='/Hamterco/img/cbp-hamstarter.webp';im.dataset.ow=1}else if(k==='national project'){im.src='/Hamterco/img/cbp-national.webp';im.dataset.ow=1}});
    /* course rail type covers: the course banner on top */
    [].forEach.call(document.querySelectorAll('.rv-cv'),function(cv){if(cv.parentNode.querySelector('.ow-bn'))return;var b=cv.querySelector('b');var f=MAP[key(b&&b.textContent)];if(!f)return;
      var i=document.createElement('img');i.className='ow-bn';i.src='/Hamterco/img/'+f+'.webp';i.alt='';i.loading='lazy';cv.parentNode.appendChild(i)});
  }
  var n=0;(function t(){run();if(++n<20)setTimeout(t,400)})();
  addEventListener('hashchange',function(){setTimeout(run,300)});
})();
