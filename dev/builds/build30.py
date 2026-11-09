import re,random
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build29.py').read())
random.seed(7)
# paths: back to the hamster characters, no square photos
P=[('dek69-8','n-grad','ไปมหาลัยกัน!'),('k-gamejam','n-win','ลุยเลย!')]
s=re.sub(r'<span class="pod"><img class="ph" src="img/dek69-8\.webp" alt="" loading="lazy"></span>','<span class="pod"><img src="img/n-grad.webp" alt="" loading="lazy"><i class="bubble">ไปมหาลัยกัน!</i></span>',s)
s=re.sub(r'<span class="pod"><img class="ph" src="img/w-revoice\.webp" alt="" loading="lazy"></span>','<span class="pod"><img src="img/n-ceo.webp" alt="" loading="lazy"><i class="bubble">ไปให้สุด!</i></span>',s)
s=re.sub(r'<span class="pod"><img class="ph" src="img/k-gamejam\.webp" alt="" loading="lazy"></span>','<span class="pod"><img src="img/n-win.webp" alt="" loading="lazy"><i class="bubble">ลุยเลย!</i></span>',s)
assert s.count('class="bubble"')==3, s.count('class="bubble"')
# HoF light rays + falling gold dust
rays=''.join('<i style="--x:%d%%;--r:%ddeg;--w:%dpx;--d:%.1fs"></i>'%(x,r,w,d) for x,r,w,d in [(18,14,120,0),(34,6,70,1.6),(50,0,180,.8),(66,-6,80,2.2),(82,-14,130,1.1)])
dust=''.join('<b style="left:%d%%;--s:%dpx;--t:%.1fs;--dl:-%.1fs"></b>'%(random.randint(2,98),random.choice([2,3,3,4,5]),random.uniform(6,12),random.uniform(0,12)) for _ in range(34))
rep('<section class="h5f" aria-label="Hall of Fame">','<section class="h5f" aria-label="Hall of Fame"><div class="h5f-fx" aria-hidden="true"><span class="h5f-ry">'+rays+'</span><span class="h5f-du">'+dust+'</span></div>')
css=r'''
/* ===== v30 ===== */
/* hero: full-width, sharp corners, bigger */
.hq{margin:0;border-radius:0;min-height:calc(100svh - 60px);display:flex;flex-direction:column;justify-content:center;position:relative;isolation:isolate;
  padding:clamp(40px,5vw,80px) clamp(20px,4vw,64px) clamp(28px,3vw,44px);
  background:radial-gradient(1px 1px at 12% 22%,rgba(255,255,255,.7),transparent),radial-gradient(1px 1px at 28% 68%,rgba(255,255,255,.5),transparent),radial-gradient(1.5px 1.5px at 44% 14%,rgba(255,255,255,.6),transparent),radial-gradient(1px 1px at 8% 84%,rgba(255,255,255,.5),transparent),radial-gradient(1.5px 1.5px at 92% 12%,rgba(255,255,255,.6),transparent),radial-gradient(1px 1px at 58% 88%,rgba(255,255,255,.45),transparent),radial-gradient(1px 1px at 36% 40%,rgba(255,255,255,.35),transparent),
  radial-gradient(55% 70% at 72% 45%,rgba(77,163,240,.38),transparent 70%),radial-gradient(70% 45% at 50% 110%,rgba(28,116,217,.55),transparent 70%),linear-gradient(180deg,#071631 0%,#0A2250 55%,#0D2E63 100%)}
.hq::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px) 0 0/100% 56px,linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px) 0 0/56px 100%;-webkit-mask:radial-gradient(70% 70% at 50% 50%,#000,transparent);mask:radial-gradient(70% 70% at 50% 50%,#000,transparent)}
.hq-in,.hq-s{max-width:1480px;width:100%}
.hq-in{grid-template-columns:minmax(0,.85fr) minmax(0,1.25fr)}
.hq-h{font-size:clamp(2.4rem,3.9vw,4rem)}
.hq-v{border-radius:0;box-shadow:0 0 0 1px rgba(255,255,255,.18),0 0 80px -10px rgba(77,163,240,.55),0 50px 80px -30px rgba(0,0,0,.8)}
.hq-s li{border-radius:0;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
.hq-s img{border-radius:0}
.hq-b .go{border-radius:0;min-height:58px;padding:0 40px}
.hq-p em{border-radius:0}
.hp-grid.hg,.hp-grid .hg{margin-top:0}
/* Hall of Fame: falling light + gold aura */
.h5f{isolation:isolate}
.h5f-fx{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden}
.h5f-ry i{position:absolute;top:-10%;left:var(--x);width:var(--w);height:120%;transform:translateX(-50%) rotate(var(--r));transform-origin:50% 0;
  background:linear-gradient(180deg,rgba(255,226,150,.55) 0%,rgba(255,206,110,.18) 45%,transparent 85%);filter:blur(14px);mix-blend-mode:screen;animation:h5Ray 5s ease-in-out var(--d) infinite alternate}
@keyframes h5Ray{0%{opacity:.35;transform:translateX(-50%) rotate(var(--r)) scaleX(.8)}100%{opacity:1;transform:translateX(-50%) rotate(calc(var(--r) + 3deg)) scaleX(1.15)}}
.h5f-du b{position:absolute;top:-10px;width:var(--s);height:var(--s);border-radius:50%;background:#FFE7A3;box-shadow:0 0 8px 2px rgba(255,210,110,.8);animation:h5Dust var(--t) linear var(--dl) infinite}
@keyframes h5Dust{0%{transform:translate(0,0);opacity:0}10%{opacity:1}90%{opacity:.8}100%{transform:translate(30px,105vh);opacity:0}}
.h5f-c{position:relative}
.h5f-c::before{content:"";position:absolute;left:-14px;right:-14px;top:-14px;aspect-ratio:4/5;width:calc(100% + 28px);border-radius:26px;z-index:-1;
  background:conic-gradient(from var(--h5a,0deg),#FFD56A,#8A5A00,#FFF1C2,#C98A10,#FFD56A);filter:blur(16px);opacity:.75;animation:h5Spin 4s linear infinite,h5Pulse 2.4s ease-in-out infinite alternate}
@property --h5a{syntax:"<angle>";inherits:false;initial-value:0deg}
@keyframes h5Spin{to{--h5a:360deg}}
@keyframes h5Pulse{from{opacity:.45}to{opacity:.95}}
.h5f-c img{box-shadow:0 0 0 2px rgba(255,225,150,.75),0 30px 50px -24px rgba(0,0,0,.9)}
.h5f-c:hover::before{opacity:1;filter:blur(22px)}
.h5f-r{position:relative;z-index:1}
@media (prefers-reduced-motion:reduce){.h5f-ry i,.h5f-du b,.h5f-c::before{animation:none}}
/* paths: characters only */
.f4.p3 .pod{background:none}
.f4.p3 .pod img{position:relative;width:100%;height:220px;object-fit:contain;aspect-ratio:auto}
/* seniors: warm graduation cream */
.mc-in{background:radial-gradient(45% 50% at 50% 58%,#FFFFFF 0%,rgba(255,255,255,0) 70%),linear-gradient(180deg,#FBF3E4 0%,#F6E7CB 100%)!important;color:#0B2550}
.mc-k{color:#B26A00}.mc h2{color:#0B2550}.mc h2 span{color:#1C74D9}
.mc-u button{color:rgba(11,37,80,.6)}.mc-u button:hover{background:rgba(11,37,80,.07)!important;color:#0B2550}
.mc-u button[aria-pressed="true"]{background:#0B2550!important;color:#fff}.mc-u button[aria-pressed="true"] b{color:#FFC531}
.mc-cap p{color:rgba(11,37,80,.8)}.mc-cap p b{color:#0B2550}.mc-cap p small{color:#B26A00}
.mc-c img{box-shadow:0 26px 40px -22px rgba(80,50,10,.55)}.mc-c.on img{box-shadow:0 0 0 3px #1C74D9,0 36px 50px -22px rgba(80,50,10,.6)}
.mc .lk{color:#1C74D9}
.mc-cap button,.mc-cap .mc-n{color:#0B2550}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v30.html','w').write(s)
print('v30 ok')
s=s.replace('.hq-in{grid-template-columns:minmax(0,.85fr) minmax(0,1.25fr)}','.hq-in{grid-template-columns:minmax(0,1fr) minmax(0,1.2fr)}.hq-h{white-space:nowrap}@media(max-width:900px){.hq-h{white-space:normal}}',1)
open('/home/claude/hamsterhub-home/v30.html','w').write(s)
s=s.replace('@media(max-width:900px){.hq-h{white-space:normal}}','@media(max-width:900px){.hq-h{white-space:normal}.hq-in{grid-template-columns:minmax(0,1fr)}.hq{min-height:0}.hq-h{font-size:2.3rem}}',1)
open('/home/claude/hamsterhub-home/v30.html','w').write(s)
