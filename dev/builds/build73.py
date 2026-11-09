SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build71p.py').read())
# class clash: an old .oc card style was leaking into the "what we build" section
rep('<section class="oc" aria-labelledby="ocH">','<section class="hbx" aria-labelledby="ocH">')
rep('.oc{background:#fff;padding:clamp(90px,10vw,150px) 16px clamp(60px,8vw,110px)}','.hbx{background:#fff;padding:clamp(90px,10vw,150px) 16px clamp(60px,8vw,110px)}')
# rift edges: run past both screen edges so no end is ever visible
CSS=r'''
/* v73 */
.hbx .oc-m{aspect-ratio:16/10}
.h5f-cap,.h5f-rt{left:-3%!important;width:106%!important}
.rau{overflow-x:visible!important}
.rau>div{left:-3%!important;width:106%!important}
.rau canvas{width:100%!important}
.h5f,.rau,.rsd{max-width:100vw}
main{overflow-x:clip}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v73.html','w').write(s)
print('v73 ok')
