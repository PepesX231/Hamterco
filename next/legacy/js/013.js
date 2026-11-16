
(function(){
  if(!window.Hamblob)return;var H=Hamblob,rm=matchMedia('(prefers-reduced-motion: reduce)').matches,all=[];
  /* card: element to hang on; at: 0..1 across its width; w: hamster width (px, desktop) */
  function cling(card,at,w,mood){if(!card||card.dataset.cl)return;card.dataset.cl='1';
    /* sticky cards move on their own, so the hamster lives inside them; the clip box ends exactly on the card edge */
    var inside=getComputedStyle(card).position==='sticky',host=inside?card:(card.offsetParent||card.parentElement),wrap=null;
    if(inside){card.classList.add('cl-in-card');wrap=document.createElement('span');wrap.className='cl-w';wrap.setAttribute('aria-hidden','true')}
    else{host.classList.add('cl-host');card.classList.add('cl-card')}
    var b=H.make({fur:'cream',shape:'loaf',mood:mood||'calm',size:w});b.classList.add('cl-b');b.style.width='';
    var p=[0,1].map(function(){var e=document.createElement('i');e.className='cl-p';e.setAttribute('aria-hidden','true');return e});
    if(wrap){wrap.appendChild(b);host.appendChild(wrap)}else host.appendChild(b);p.forEach(function(e){host.appendChild(e)});
    var o={card:card,host:host,b:b,p:p,at:at,w:w,wrap:wrap};all.push(o);
    card.addEventListener('pointerenter',function(){cls(o,'cl-up',1);if(!rm)H.squish(b)});
    card.addEventListener('pointerleave',function(){cls(o,'cl-up',0)});
    place(o);
    if('IntersectionObserver' in window&&!rm)new IntersectionObserver(function(es,ob){if(!es[0].isIntersecting)return;ob.disconnect();setTimeout(function(){place(o);cls(o,'cl-in',1)},750)},{threshold:.35}).observe(card);
    else cls(o,'cl-in',1)}
  function cls(o,c,v){[o.b].concat(o.p).forEach(function(e){e.classList.toggle(c,!!v)})}
  function place(o){var c=o.card;if(!c.offsetWidth)return;
    var w=Math.round(o.w*(innerWidth<640?.78:1)),h=w*190/220,
        /* position of the card's top edge inside the host (ignores the reveal transform, which ends at 0) */
        x0=o.wrap?0:c.offsetLeft,y0=o.wrap?0:c.offsetTop,cx=x0+c.offsetWidth*o.at,
        top=y0-h*.69;                      /* chin rests on the edge: eyes and mouth stay above it */
    if(o.wrap){o.wrap.style.cssText='left:'+(cx-w/2)+'px;top:'+top+'px;width:'+w+'px;height:'+(h*.69)+'px';o.b.style.cssText='width:'+w+'px'}
    else o.b.style.cssText='width:'+w+'px;left:'+(cx-w/2)+'px;top:'+top+'px';
    var pw=w*.24,ph=w*.17;
    o.p[0].style.cssText='width:'+pw+'px;height:'+ph+'px;left:'+(cx-w*.27-pw/2)+'px;top:'+(y0-ph*.45)+'px';
    o.p[1].style.cssText='width:'+pw+'px;height:'+ph+'px;left:'+(cx+w*.27-pw/2)+'px;top:'+(y0-ph*.45)+'px'}
  function placeAll(){all.forEach(place)}
  function build(){
    var afo=document.querySelector('[data-view="home"] .t-afo');if(afo)cling(afo,.8,96,'happy');
    var row=document.querySelector('[data-view="home"] .fx-row');
    if(row)[].forEach.call(row.querySelectorAll('.fx-s'),function(c,i){cling(c,.8,i?60:66,i?'happy':'calm')});
    placeAll()}
  function go(){build();setTimeout(placeAll,600);setTimeout(placeAll,1800)}
  if(document.readyState==='complete')go();else addEventListener('load',go);
  addEventListener('resize',placeAll);
  if(window.ResizeObserver)new ResizeObserver(placeAll).observe(document.body);
  addEventListener('hashchange',function(){setTimeout(placeAll,120)});
})();
