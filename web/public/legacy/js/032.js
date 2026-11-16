
(function(){
  /* the event status follows the real date written on the page, so nothing says "upcoming" with a 0:00 counter */
  var TM=['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.'];
  function status(){var d=document.querySelector('.avn .avn-d');if(!d)return;var m=d.textContent.match(/(\d{1,2})\s*(\S+?\.)\s*(\d{4})/);if(!m)return;
    var ev=new Date(+m[3]-543,TM.indexOf(m[2]),+m[1]),now=new Date();now.setHours(0,0,0,0);var dd=Math.round((ev-now)/864e5);if(dd>0)return;
    var tag=document.getElementById('avnTag'),cd=document.getElementById('avnCd'),nx=document.getElementById('nvNext'),hd=[].filter.call(document.querySelectorAll('.nw2-h'),function(h){return /กำลังจะมา/.test(h.textContent)});
    if(dd===0){if(tag&&tag.textContent!=='วันนี้')tag.textContent='วันนี้';
      if(cd){cd.hidden=true;if(!document.querySelector('.avn-now')){var p=document.createElement('p');p.className='avn-now';p.textContent='งานจัดวันนี้';cd.parentNode.insertBefore(p,cd)}}
      if(nx&&nx.textContent!=='วันนี้ '+m[1]+' '+m[2])nx.textContent='วันนี้ '+m[1]+' '+m[2];
      hd.forEach(function(h){h.textContent='กิจกรรมวันนี้'})}
    else{if(cd)cd.hidden=true;/* the nav hint says what actually happened, not a vague "see all" */if(nx&&nx.textContent!=='เพิ่งจบ '+m[1]+' '+m[2])nx.textContent='เพิ่งจบ '+m[1]+' '+m[2];hd.forEach(function(h){h.textContent='กิจกรรมล่าสุด'})}}
  function go(){status();setInterval(status,5000)}
  if(document.readyState==='complete')go();else addEventListener('load',go);
})();
