(function(){function go(){var top=document.querySelector('[data-view="home"] .nw2 .nw2-h'),l=document.querySelector('[data-view="home"] .mr-l h3');
  /* self-review: one "กิจกรรมล่าสุด" heading above the banner; the card list under it is the earlier events */
  if(top&&top.textContent.trim()!=='กิจกรรมล่าสุด')top.textContent='กิจกรรมล่าสุด';
  if(l&&l.textContent.trim()==='กิจกรรมล่าสุด')l.textContent='งานที่ผ่านมา'}
  if(document.readyState==='complete')go();else addEventListener('load',go);setTimeout(go,6500);setTimeout(go,12000)})();