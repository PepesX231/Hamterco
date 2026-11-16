(function(){function go(){[].forEach.call(document.querySelectorAll('.fx-row .fx-s'),function(a){if(a.querySelector('.zc-st'))return;var rc=a.querySelector('.rc.rc-s');if(!rc)return;
  /* the "แนะนำ" pill becomes an honest status: these two only take LINE sign-ups for the next round */
  rc.classList.add('zc-st');rc.textContent='รอเปิดรอบถัดไป'})}
  if(document.readyState==='complete')go();else addEventListener('load',go);setTimeout(go,1500)})();