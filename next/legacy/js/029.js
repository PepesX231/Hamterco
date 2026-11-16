
(function(){
  function el(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.textContent=h;return e}
  function nav(){
    var c=document.querySelector('.nav-in>a.nv-c>span');
    if(c&&!c.querySelector('.na-x')){var l=el('span','na-x na-c l','<'),r=el('span','na-x na-c r','/>');r.appendChild(el('i'));[l,r].forEach(function(x){x.setAttribute('aria-hidden','true')});c.appendChild(l);c.appendChild(r)}
    var w=document.querySelector('.nav-in>a.nv-w>span');
    if(w&&!w.querySelector('.na-x')){var t=w.textContent;w.textContent='';w.appendChild(el('span','na-w0',t));var p=el('span','na-x na-w');p.setAttribute('aria-hidden','true');p.innerHTML='<b></b>';w.appendChild(p)}
    var b=document.querySelector('.nav-in>a.nv-b>span');
    if(b&&!b.querySelector('.na-x')){var d=el('span','na-x na-b');d.setAttribute('aria-hidden','true');d.innerHTML='<svg viewBox="0 0 120 40" preserveAspectRatio="none"><path pathLength="1" d="M70 4C40 1 8 6 5 19c-3 14 40 19 72 17 30-2 42-11 38-21C111 4 86 1 56 4"/><g class="h"><ellipse cx="117" cy="5.5" rx="3.6" ry="3"/><circle cx="111.6" cy="1.2" r="1.5"/><circle cx="115.3" cy="-1.2" r="1.5"/><circle cx="119.4" cy="-1" r="1.5"/><circle cx="122.6" cy="1.6" r="1.5"/></g></svg>';b.appendChild(d)}}
  /* seniors caption */
  var last='';
  function cap(){var p=document.getElementById('mcC');if(!p)return;var box=p.parentNode,m=box.querySelector('.mc3');
    if(!m){m=el('div','mc3');m.setAttribute('aria-hidden','true');box.appendChild(m)}
    var b=p.querySelector('b'),s=p.querySelector('small');if(!b)return;
    var rest='';[].forEach.call(p.childNodes,function(n){if(n.nodeType===3)rest+=n.textContent});
    var parts=rest.split('·').map(function(x){return x.trim()}).filter(Boolean),key=p.textContent;if(key===last)return;last=key;
    function fill(){m.innerHTML='';m.appendChild(el('span','mc3-n',b.textContent));var u=el('span','mc3-u');
      if(parts[1]){u.appendChild(el('b',null,parts[1]));u.appendChild(el('i'))}if(parts[0])u.appendChild(el('span',null,parts[0]));m.appendChild(u);
      if(s)m.appendChild(el('span','mc3-c',s.textContent));}
    if(!m.firstChild||matchMedia('(prefers-reduced-motion: reduce)').matches){fill();return}
    m.classList.add('out');setTimeout(function(){fill();void m.offsetWidth;m.classList.remove('out')},220)}
  function go(){nav();cap();var p=document.getElementById('mcC');if(p&&!p.dataset.mc3){p.dataset.mc3=1;new MutationObserver(cap).observe(p,{childList:true,characterData:true,subtree:true})}}
  if(document.readyState==='complete')go();else addEventListener('load',go);
  addEventListener('hashchange',function(){setTimeout(go,150)});
})();
