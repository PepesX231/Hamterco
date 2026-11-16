
/* typing details: Esc closes the answer (second Esc leaves the field); whitespace-only never searches */
(function(){var inp=document.getElementById('zqIn'),res=document.getElementById('zqRes');if(!inp||!res)return;
  inp.addEventListener('keydown',function(e){if(e.key!=='Escape'||e.isComposing)return;
    if(!res.hidden){e.preventDefault();inp.value='';inp.dispatchEvent(new Event('input',{bubbles:true}));res.hidden=true}else inp.blur()});
  inp.addEventListener('input',function(){if(!inp.value.trim()&&!res.hidden)res.hidden=true});
  document.getElementById('zqForm').addEventListener('submit',function(e){if(!inp.value.trim()){e.preventDefault();e.stopImmediatePropagation();inp.value='';inp.focus()}},true);
})();
