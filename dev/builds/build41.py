import re,random
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build40.py').read())
random.seed(11)
# --- Hall of Fame: bring the effects back (spotlight rays, gold dust, corner frame, sheen, gold title)
i=s.index('/* Hall of Fame: flat warm ground, gold as the only accent, games float */');j=s.index('.h5f-go{background:#E2C27A!important}',i)+len('.h5f-go{background:#E2C27A!important}')
s=s[:i]+s[j:]
dust=''.join('<b style="left:%d%%;--s:%dpx;--t:%.1fs;--dl:-%.1fs"></b>'%(random.randint(2,98),random.choice([2,3,3,4]),random.uniform(7,13),random.uniform(0,12)) for _ in range(28))
rep('<section class="h5f" aria-label="Hall of Fame">','<section class="h5f" aria-label="Hall of Fame"><div class="h5f-fx" aria-hidden="true"><span class="h5f-sp"></span><span class="h5f-du">'+dust+'</span></div>')
# --- search hero: full screen, decorated with the kids' real games floating at the edges
G=[('stressstrike','l1'),('phi-krahang','l2'),('slash-speed','l3'),('eugation-strike','r1'),('escape-rolling','r2'),('hot-hot-hot','r3')]
deco='<div class="zq-dc" aria-hidden="true">'+''.join('<img class="%s" src="img/work-%s.webp" alt="">'%(c,w) for w,c in G)+'<img class="zq-hm" src="img/n-gamer.webp" alt=""></div>'
rep('<section class="zq" aria-label="ค้นหาคอร์สและกิจกรรม">','<section class="zq" aria-label="ค้นหาคอร์สและกิจกรรม">'+deco)
css=r'''
/* ===== v41 ===== */
/* search hero fills the first screen */
.zq{position:relative;overflow:hidden;isolation:isolate;min-height:calc(100svh - 60px);display:flex;flex-direction:column;justify-content:center;
  background:#EAF1FB}
.zq-top{position:relative;z-index:2}
.zq-res{position:relative;z-index:2}
.zq-dc{position:absolute;inset:0;z-index:0;pointer-events:none}
.zq-dc img:not(.zq-hm){position:absolute;width:clamp(150px,15vw,230px);aspect-ratio:4/3;object-fit:cover;border:6px solid #fff;border-radius:14px;box-shadow:0 22px 40px -18px rgba(13,46,99,.45);animation:zqF 7s ease-in-out infinite}
.zq-dc .l1{left:4%;top:12%;rotate:-8deg}
.zq-dc .l2{left:9%;top:44%;rotate:5deg;animation-delay:-2s}
.zq-dc .l3{left:3%;bottom:8%;rotate:-4deg;animation-delay:-4s}
.zq-dc .r1{right:5%;top:10%;rotate:7deg;animation-delay:-1s}
.zq-dc .r2{right:10%;top:42%;rotate:-6deg;animation-delay:-3s}
.zq-dc .r3{right:4%;bottom:9%;rotate:4deg;animation-delay:-5s}
.zq-dc .zq-hm{position:absolute;right:calc(10% + 150px);bottom:6%;width:110px;rotate:6deg}
@keyframes zqF{0%,100%{translate:0 0}50%{translate:0 -12px}}
@media (max-width:1100px){.zq-dc .l2,.zq-dc .r2,.zq-dc .zq-hm{display:none}.zq-dc img:not(.zq-hm){width:130px;opacity:.55}}
@media (max-width:700px){.zq-dc{display:none}.zq{min-height:calc(100svh - 60px)}}
@media (prefers-reduced-motion:reduce){.zq-dc img{animation:none}}
/* news: one aligned column, heading clearly first */
.nw2{background:#fff}
.nw2-h{max-width:1240px!important;margin:0 auto 24px!important;padding:0 24px!important;font:800 clamp(2.4rem,4.6vw,3.6rem)/1.1 var(--display)!important;color:#0D2E63;display:flex;align-items:center;gap:14px}
.nw2-h::before{content:"";width:14px;height:14px;border-radius:50%;background:#E5484D;box-shadow:0 0 0 6px rgba(229,72,77,.18);animation:nwP 1.6s ease-in-out infinite}
@keyframes nwP{50%{box-shadow:0 0 0 12px rgba(229,72,77,0)}}
.nw2 .wrap.hg,.nw2 .hg{max-width:1240px!important;margin:0 auto!important;padding:0 24px!important;width:auto!important}
.nw2 .tile.t-afo{border-radius:28px!important;margin:0!important}
.nw2-l{max-width:1240px!important;padding:0 24px!important}
.nw2-l h3{font-size:1.6rem!important}
/* courses band: soft colour with the kids' faces, no textures */
.zc2{background:#F2F5FA}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v41.html','w').write(s)
print('v41 ok')
