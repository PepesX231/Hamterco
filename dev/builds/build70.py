SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build69.py').read())
rep('<p class="zq-lead"><img src="img/hh-mascot.webp" alt="">','<p class="zq-lead">')
s=s.replace('<b>พาน้องสร้างสตาร์ทอัพ</b>','<b>พาน้องสร้าง<span class="nw">สตาร์ทอัพ</span></b>').replace('<h3>ผลงานของน้อง ขายได้และมีคนใช้จริง</h3>','<h3>ผลงานของน้อง <span class="nw">ขายได้</span>และมีคนใช้จริง</h3>')
s=s.replace("'<div class=\"avc-ty\"><b>'+a[1]+'</b><img src=\"img/hh-mascot.webp\" alt=\"\"></div>'","'<div class=\"avc-ty\"><b>'+a[1]+'</b><img src=\"img/hh-mascot.webp\" alt=\"\"></div>'")
CSS=r'''
/* v70 */
.avc-ty{background:#0D2E63!important;align-items:flex-start!important;flex-direction:column;justify-content:space-between;padding:18px 20px!important}
.avc-ty::before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:var(--tc)}
.avc-ty b{max-width:62%!important;font-size:clamp(1.2rem,1.8vw,1.5rem)!important}
.avc-ty img{right:14px!important;top:auto!important;bottom:-18px;width:38%!important;transform:rotate(-6deg)!important;opacity:1!important}
.ab-use .sec-h{text-align:center}.ab-use-s{text-align:center;margin:0 auto!important;max-width:640px}
.ad-im img{object-position:50% 20%}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v70.html','w').write(s)
print('v70 ok')
