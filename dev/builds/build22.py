D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build21.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
# 1) hero: no repeated text, pixel buttons, full width dark band
i=s.index('    <div class="ov-bar2">');j=s.index('</div></div>',i)+12
s=s[:i]+'''    <div class="ov-bar3"><a class="pb1" href="'''+PX+'''" target="_blank" rel="noopener">▶ สมัครเรียน</a><a class="pb2" href="#portex">ดูรายละเอียดคอร์ส</a></div>'''+s[j:]
# 2) news: drop separate heading, label lives inside the tile
i=s.index('<div class="nw-h">');j=s.index('</div>',i)+6;s=s[:i]+s[j:]
rep('<p class="t-k"><span class="nw-new">ข่าวใหม่</span></p>','<p class="t-k"><span class="nw-new">ข่าวสาร · อัปเดตล่าสุด</span></p>')
css=r'''
/* ===== v22 ===== */
.ov{padding:0!important;background:#1A1460 url(img/px-sky.webp) 50% 50%/cover!important;image-rendering:pixelated}
.ov a.ov-c{width:100%!important;max-width:none;height:min(calc(100svh - 150px),56.25vw);aspect-ratio:auto!important}
.ov-c video{object-fit:contain!important}
.ov .ov-c{background:transparent!important}
.ov-bar3{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;padding:22px 16px 26px;background:#140F3A;box-shadow:0 -6px 0 #5B3FD6}
.ov-bar3 a{display:inline-flex;align-items:center;min-height:54px;padding:0 30px 5px;font:800 1.1rem var(--display);text-decoration:none;transition:transform .1s steps(2);
  clip-path:polygon(0 6px,6px 6px,6px 0,calc(100% - 6px) 0,calc(100% - 6px) 6px,100% 6px,100% calc(100% - 6px),calc(100% - 6px) calc(100% - 6px),calc(100% - 6px) 100%,6px 100%,6px calc(100% - 6px),0 calc(100% - 6px))}
.ov-bar3 a:hover{transform:translateY(4px)}
.pb1{background:#FFD24A;color:#0B0720;box-shadow:inset 0 -6px 0 #C28A00}
.pb2{background:#5BC0FF;color:#06123A;box-shadow:inset 0 -6px 0 #1D5FB8}
.hp-grid{padding-top:12px!important}
/* hall of fame row: fit, never cut */
.hf-row{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr));max-width:1100px;margin-left:auto!important;margin-right:auto!important;padding:0 8px}
.hf-row figure{width:auto!important}
@media (max-width:700px){.hf-row{grid-template-columns:repeat(3,minmax(0,1fr))}.ov a.ov-c{height:56.25vw}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v22.html','w').write(s)
print('v22 ok',len(s))
