SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build60.py').read())
# white jagged caps instead of clip-path
capT='<svg class="h5f-cap t" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polygon points="0,0 '+tp+' 1000,0"/></svg>'
capB='<svg class="h5f-cap b" viewBox="0 0 1000 48" preserveAspectRatio="none" aria-hidden="true"><polygon points="0,48 '+bp+' 1000,48"/></svg>'
rep('<svg class="h5f-rt t"',capT+capB+'<svg class="h5f-rt t"')
# one merged aurora layer
rep("d.innerHTML='<i style=\"background-image:url('+A+')\"></i><i style=\"background-image:url('+B+')\"></i>';","d.innerHTML='<i style=\"background-image:url('+B+'),url('+A+')\"></i>';")
css=r'''
/* ===== v61: performance pass 2 ===== */
.h5f{clip-path:none!important}
.h5f-cap{position:absolute;left:0;width:100%;height:48px;z-index:3;pointer-events:none;fill:#fff}
.h5f-cap.t{top:-1px}.h5f-cap.b{bottom:-1px}
.h5f-au2{contain:strict}
.h5f-au2 i{background-size:50% 100%,50% 100%!important}
.nav{background:rgba(255,255,255,.96)!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important}
.h5f-du b{box-shadow:none!important;background:radial-gradient(circle,#FFF1C2 0 35%,rgba(255,210,110,.6) 50%,transparent 70%)!important;width:calc(var(--s) * 3)!important;height:calc(var(--s) * 3)!important}
.h5f-du b:nth-child(2n){display:none}
.wk{will-change:transform}
.wkz-rift .wk{filter:none!important}
.h5f-c,.h5f-c::after{will-change:transform}
.h5f{contain:paint}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v61.html','w').write(s)
print('v61 ok')
