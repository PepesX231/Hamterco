import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build30.py').read())
# HoF: straight podium row, framed image, single spotlight
s=re.sub(r'<a class="h5f-c" href="#works" data-pane="hof" style="--i:(-?\d)"><img src="(img/work-[a-z-]+\.webp)" alt="" loading="lazy">',
         lambda m:'<a class="h5f-c%s" href="#works" data-pane="hof"><span class="h5f-im"><img src="%s" alt="" loading="lazy"></span>'%(' mid' if m.group(1)=='0' else '',m.group(2)),s)
assert s.count('h5f-im')==5
s=re.sub(r'<span class="h5f-ry">.*?</span>','<span class="h5f-sp"></span>',s,count=1)
css=r'''
/* ===== v31 ===== */
.h5f-sp{position:absolute;left:50%;top:-6%;width:170%;height:115%;transform:translateX(-50%);transform-origin:50% 0;
  background:repeating-conic-gradient(from 166deg at 50% 0%,rgba(255,224,150,.20) 0deg 3deg,transparent 3deg 7deg);
  -webkit-mask:radial-gradient(60% 85% at 50% 0%,#000 20%,transparent 75%) ,linear-gradient(90deg,transparent 22%,#000 40%,#000 60%,transparent 78%);-webkit-mask-composite:source-in;
  mask:radial-gradient(60% 85% at 50% 0%,#000 20%,transparent 75%) intersect,linear-gradient(90deg,transparent 22%,#000 40%,#000 60%,transparent 78%);
  filter:blur(3px);animation:h5Sway 9s ease-in-out infinite alternate}
.h5f-fx::before{content:"";position:absolute;left:50%;top:-30%;width:900px;height:600px;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(255,214,120,.35),transparent);filter:blur(10px)}
@keyframes h5Sway{from{transform:translateX(-50%) rotate(-4deg)}to{transform:translateX(-50%) rotate(4deg)}}
.h5f-r{align-items:flex-end}
.h5f-c{transform:none!important;flex:1;max-width:210px}
.h5f-c.mid{max-width:260px}
.h5f-c::before{display:none}
.h5f-im{position:relative;display:block;border-radius:16px;overflow:hidden;padding:2px;background:linear-gradient(140deg,#FFF1C2,#B8862A 35%,#FFE39A 55%,#8A5A00 80%,#FFF1C2);
  box-shadow:0 0 30px -6px rgba(255,200,90,.55),0 30px 50px -24px rgba(0,0,0,.95);transition:transform .35s cubic-bezier(.3,1.4,.5,1),box-shadow .35s}
.h5f-im img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:50% 20%;border-radius:14px;box-shadow:none!important;transform:scale(1.12);transform-origin:50% 0}
.h5f-im::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 35%,rgba(255,250,225,.45) 50%,transparent 65%) -200% 0/250% 100% no-repeat;animation:h5Sheen 5s ease-in-out infinite}
.h5f-c:nth-child(2) .h5f-im::after{animation-delay:1s}.h5f-c:nth-child(3) .h5f-im::after{animation-delay:.4s}.h5f-c:nth-child(4) .h5f-im::after{animation-delay:1.6s}.h5f-c:nth-child(5) .h5f-im::after{animation-delay:2.2s}
@keyframes h5Sheen{0%,55%{background-position:-200% 0}100%{background-position:200% 0}}
.h5f-c.mid .h5f-im{box-shadow:0 0 60px -4px rgba(255,205,100,.75),0 30px 50px -24px rgba(0,0,0,.95)}
.h5f-c:hover .h5f-im{transform:translateY(-10px);box-shadow:0 0 60px 0 rgba(255,205,100,.8),0 30px 50px -24px rgba(0,0,0,.95)}
.h5f-c b{margin-top:14px}
@media (max-width:700px){.h5f-c.mid{max-width:none}}
@media (prefers-reduced-motion:reduce){.h5f-sp,.h5f-im::after{animation:none}}
/* seniors: white */
.mc-in{background:#fff!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v31.html','w').write(s)
print('v31 ok')
s=s.replace('.mc-in{background:#fff!important}','.mc-in{background:#fff!important}\n.h5f-c em{position:absolute;top:12px;left:12px;margin:0;z-index:2;box-shadow:0 4px 12px rgba(0,0,0,.4)}.h5f-im{padding:3px}',1)
open('/home/claude/hamsterhub-home/v31.html','w').write(s)
s=s.replace('.h5f-im{padding:3px}','.h5f-im{padding:3px}.mc-u button b{color:#1C74D9}.mc-u button[aria-pressed="true"] b{color:#FFC531}',1)
open('/home/claude/hamsterhub-home/v31.html','w').write(s)
