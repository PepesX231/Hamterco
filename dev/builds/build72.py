SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build71.py').read())
JS=r'''  /* v72: nav turns dark while the dark hero is under it */
  (function(){var n=$('.nav'),z=$('.zq');if(!n||!z)return;function on(v){n.classList.toggle('nav-dk',v)}
    new IntersectionObserver(function(e){on(e[0].isIntersecting&&!!document.querySelector('[data-view="home"].on'))},{rootMargin:'-60px 0px -100% 0px'}).observe(z);
    function chk(){var r=z.getBoundingClientRect();on(r.bottom>70&&r.top<80&&!!document.querySelector('[data-view="home"].on'))}
    addEventListener('hashchange',function(){setTimeout(chk,60)});addEventListener('scroll',chk,{passive:true});setTimeout(chk,100);setTimeout(chk,800)})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
CSS=r'''
/* v72 */
.nav{transition:background .3s,border-color .3s}
.nav.nav-dk{background:rgba(5,7,13,.92)!important;border-color:rgba(255,255,255,.08)!important}
.nav.nav-dk .brand,.nav.nav-dk .v,.nav.nav-dk .menu{color:#fff!important}
.nav.nav-dk .v span{color:#E5ECF8!important}
.hx-pf b{white-space:nowrap}
@media (max-width:700px){.zq-more{display:none!important}.hx-pf li{display:grid;grid-template-columns:118px 1fr;gap:10px}}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v72.html','w').write(s)
print('v72 ok')
