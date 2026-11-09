SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build41.py').read())
JS=r'''
  /* search: loading dots while matching */
  (function(){var f=$('#zqForm');if(!f)return;var btn=f.querySelector('button'),t0=btn.textContent;f.addEventListener('submit',function(){btn.classList.add('ld');btn.innerHTML='<i></i><i></i><i></i>';setTimeout(function(){btn.classList.remove('ld');btn.textContent=t0},520)})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v43 ===== */
/* Hall of Fame: same look, without the diagonal grid */
.h5f{background:radial-gradient(40% 50% at 50% 0%,rgba(255,206,110,.16),transparent 70%),linear-gradient(#100B05,#070503)!important}
/* small touches */
.zq-s button.ld{display:inline-flex;gap:5px;align-items:center;justify-content:center;min-width:86px}
.zq-s button.ld i{width:7px;height:7px;border-radius:50%;background:#fff;animation:ldB .6s ease-in-out infinite alternate}
.zq-s button.ld i:nth-child(2){animation-delay:.15s}.zq-s button.ld i:nth-child(3){animation-delay:.3s}
@keyframes ldB{from{opacity:.3;transform:translateY(2px)}to{opacity:1;transform:translateY(-2px)}}
.zk-i img{transition:transform .5s cubic-bezier(.2,.8,.2,1)}.zk:hover .zk-i img{transform:scale(1.05)}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v43.html','w').write(s)
print('v43 ok')
