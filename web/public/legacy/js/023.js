
(function(){
  /* countdown: drop the "days" box when it reads 0 */
  var d=document.getElementById('cdD');
  function z(){if(!d)return;var box=d.parentElement,zero=d.textContent.trim()==='0';if(box.classList.contains('cp-zero')!==zero)box.classList.toggle('cp-zero',zero)}
  if(d){z();new MutationObserver(z).observe(d,{childList:true,characterData:true,subtree:true})}
  /* closing wall: fill the slot the dashed tile used with nothing (grid of 8 reads fine as 4+4 / 3+3+2) */
})();
