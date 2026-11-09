import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build35.py').read())
rep('<h1 class="hq-h">เรียน 2 เดือน<br><span>มีผลงานจริงไปยื่นพอร์ต</span></h1>','<h1 class="hq-h">เรียน 2 เดือน<br><span>มีผลงานจริงไปยื่นพอร์ต</span><br><em>ตอบคำถามกรรมการได้ลื่นไหล</em></h1>')
s=re.sub(r'\s*<ol class="hq-s">.*?</ol>','',s,count=1,flags=re.S)
n=len(re.findall(r'<span class="pf">[^<]*</span>',s));s=re.sub(r'<span class="pf">[^<]*</span>','',s);print('pf',n)
css=r'''
/* ===== v36 ===== */
.hq-h em{display:inline-block;font-style:normal;color:#fff;font-size:.62em;font-weight:700;margin-top:10px;letter-spacing:-.01em}
@media(max-width:900px){.hq-in{grid-template-columns:minmax(0,1fr)!important}.hq-v{order:-1}.hq-h{white-space:normal!important;font-size:2.2rem!important}.hq{min-height:0}}
.hq-in{margin-top:auto;margin-bottom:auto}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v36.html','w').write(s)
print('v36 ok')
rep('เราสอนทำ <b>เกม</b> · <b>Roblox</b> · <b>เว็บ</b> · <b>IoT</b> ให้น้องมีผลงานจริงของตัวเอง','เราสอนทำ <b>Game</b> · <b>Web</b> · <b>IoT</b> ให้น้องมีผลงานจริงของตัวเอง')
rep('<small>เกม · Roblox · เว็บ · IoT</small>','<small>Game · Web · IoT</small>')
open('/home/claude/hamsterhub-home/v36.html','w').write(s)
