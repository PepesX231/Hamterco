SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build33.py').read())
NAME='Hamster Hub'
letters=''.join('<span class="ph-l" style="--k:%d">%s</span>'%(k,c if c!=' ' else '&nbsp;') for k,c in enumerate(NAME))
rep('''h='<span class="pt-home"></span><span class="pt-lg"><img src="img/logo.webp" alt=""><b>Hamster Hub</b></span>\'''',
    '''h='<span class="ph-p a"></span><span class="ph-p b"></span><span class="ph-p c"></span><span class="ph-c"><span class="ph-r"></span><span class="ph-r r2"></span><img src="img/logo.webp" alt=""><b>'''+letters+'''</b><small>เกม · Roblox · เว็บ · IoT</small></span>\'''')
rep("var hold={courses:750,","var hold={home:1150,courses:750,")
css=r'''
/* ===== v34 ===== */
/* Hall of Fame: square, full width */
.h5f{margin:0;border-radius:0}
.h5f-im,.h5f-im img{border-radius:0}
.h5f-c em{border-radius:0}
.h5f-go{clip-path:none}
/* home transition: panels sweep in, logo stamps, name types in */
.v-home .ph-p{position:fixed;top:-10%;bottom:-10%;left:-20%;right:-20%;transform:translateX(-120%) skewX(-14deg)}
.v-home .ph-p.a{background:#FFC531;animation:phIn .5s cubic-bezier(.7,0,.2,1) forwards}
.v-home .ph-p.b{background:#1C74D9;animation:phIn .5s cubic-bezier(.7,0,.2,1) .08s forwards}
.v-home .ph-p.c{background:#071631;animation:phIn .5s cubic-bezier(.7,0,.2,1) .16s forwards}
@keyframes phIn{to{transform:translateX(0) skewX(-14deg)}}
.v-home.out .ph-p{animation:phOut .55s cubic-bezier(.7,0,.2,1) forwards}
.v-home.out .ph-p.b{animation-delay:.06s}.v-home.out .ph-p.a{animation-delay:.12s}
@keyframes phOut{from{transform:translateX(0) skewX(-14deg)}to{transform:translateX(120%) skewX(-14deg)}}
.ph-c{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);display:grid;justify-items:center;gap:14px;color:#fff;z-index:2}
.pt .ph-c img{width:120px!important;height:120px!important;border-radius:50%;box-shadow:0 0 0 6px rgba(255,255,255,.12),0 20px 50px rgba(0,0,0,.5);transform:scale(0) rotate(-200deg);animation:phLogo .6s cubic-bezier(.2,1.5,.4,1) .4s forwards}
@keyframes phLogo{to{transform:scale(1) rotate(0)}}
.ph-r{position:absolute;left:50%;top:54px;width:108px;height:108px;margin:-54px 0 0 -54px;border-radius:50%;border:3px solid #FFC531;opacity:0;animation:phRing .8s ease-out .62s forwards}
.ph-r.r2{border-color:#4DA3F0;animation-delay:.74s}
@keyframes phRing{0%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(2.6)}}
.ph-c b{display:flex;font:900 clamp(2.2rem,5vw,3.6rem)/1 var(--display);letter-spacing:-.01em}
.ph-c b .ph-l{display:inline-block;opacity:0;transform:translateY(24px);animation:phL .38s cubic-bezier(.2,1.6,.4,1) forwards;animation-delay:calc(.5s + var(--k) * .025s)}
.ph-c b .ph-l:nth-child(n+9){color:#FFC531}
@keyframes phL{to{opacity:1;transform:none}}
.ph-c small{font:700 1rem var(--display);letter-spacing:.12em;color:#B3D8FF;opacity:0;animation:phL .4s ease-out .8s forwards;transform:translateY(10px)}
.v-home.out .ph-c{animation:phCo .35s ease-in forwards}
@keyframes phCo{to{opacity:0;transform:translate(-50%,-50%) scale(.9)}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v34.html','w').write(s)
print('v34 ok')
