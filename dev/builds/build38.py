import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build36.py').read())
# Plan (frontend-design skill):
#  colour: navy #0D2E63 (flat), ink #10213F, paper #FFFFFF, yellow #FFC531 (price/CTA only), gold #E2C27A (Hall of Fame only), HoF ground #1C150A
#  no grids, no gradient washes, no glows, no light rays/dust, no corner brackets, no stripe textures
#  one bold thing per section: hero = the Port Express clip; HoF = the floating games
#  copy: no '·' meta strings, no '→' on links, no tracked all-caps eyebrows
# ---- copy
rep('<p class="hq-k">Port Express · คอร์สทำพอร์ตยื่นมหาลัย สำหรับ ม.6</p>','<p class="hq-k">คอร์ส Port Express สำหรับน้อง ม.6</p>')
s=s.replace(' <b>→</b>','')
rep('เราสอนทำ <b>Game</b> · <b>Web</b> · <b>IoT</b> ให้น้องมีผลงานจริงของตัวเอง','เราสอนทำ Game, Web และ IoT ให้น้องมีผลงานจริงของตัวเอง')
rep('คอร์สทำพอร์ตยื่นมหาลัย สำหรับ ม.6 · เริ่ม 9 พ.ย. 2569 · เรียน 2 เดือน','คอร์สทำพอร์ตยื่นมหาลัย สำหรับ ม.6 เริ่ม 9 พ.ย. 2569 เรียน 2 เดือน')
rep('แบบ ค่าย · เวิร์กชอป · แข่ง · โชว์','แบบ: ค่าย เวิร์กชอป แข่งขัน และโชว์ผลงาน')
s=re.sub(r'<p class="axh-k"><span>HAMSTER HUB EVENTS</span></p>\s*','',s)
s=re.sub(r'<p class="t-k[^"]*"[^>]*>ข่าวสาร · อัปเดตล่าสุด</p>','',s)
s=s.replace('ข่าวสาร · อัปเดตล่าสุด','')
s=s.replace('DEK69 · รอบ Portfolio','DEK69 รอบ Portfolio')
s=s.replace('© 2569 Hamster Hub · ตัวเลขจาก','© 2569 Hamster Hub ตัวเลขจาก')
# ---- HoF: drop rays, dust, corners
s=re.sub(r'<div class="h5f-fx" aria-hidden="true">.*?</span></span></div>','',s,count=1,flags=re.S)
css=r'''
/* ===== v38: remove generated-looking decoration ===== */
.hq{background:#0D2E63!important}
.hq::after,.hq::before{display:none!important}
.hq-v{box-shadow:none!important}
.hq-k{color:#B3D8FF;font-weight:600}
/* Hall of Fame: flat warm ground, gold as the only accent, games float */
.h5f{background:#1C150A!important}
.h5f-fx{display:none!important}
.h5f-t{animation:none!important;background:none!important;-webkit-background-clip:border-box!important;background-clip:border-box!important;color:#E2C27A!important;letter-spacing:.02em}
.h5f-k{color:#E2C27A;letter-spacing:0}
.h5f-s{color:rgba(255,246,224,.75)}
.h5f-im{background:#E2C27A!important;padding:2px!important;box-shadow:0 24px 30px -18px rgba(0,0,0,.9)!important}
.h5f-im::after{display:none!important}
.h5f-c.mid .h5f-im,.h5f-c:hover .h5f-im{box-shadow:0 24px 30px -18px rgba(0,0,0,.9)!important}
.h5f-c::after{background:rgba(0,0,0,.45)!important;filter:blur(6px)}
.h5f-nm{background:#1C150A!important;box-shadow:inset 0 0 0 1px #E2C27A!important}
.h5f-go{background:#E2C27A!important}
/* activity header: photo under one flat tint, no stripes or light bands */
.axh{background:linear-gradient(rgba(13,46,99,.9),rgba(13,46,99,.9)),url(img/photo-group.webp) center 30%/cover!important}
.axh::before{display:none!important}
.axh::after{background:var(--yel)!important}
.axh-h{text-shadow:none!important;animation:none!important}
/* news block and other sections: no dot textures */
.t-afo,.tile.t-afo{background-image:none!important}
.t-afo::before,.t-afo::after{display:none!important}
/* no fade-up on every section */
.rv{opacity:1!important;transform:none!important;transition:none!important}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v38.html','w').write(s)
print('v38 ok')
s=s.replace('<p class="t-k"><span class="nw-new"></span></p>','')
s=s.replace('กิจกรรมถัดไป · 14 พ.ย. 2569','กิจกรรมถัดไป 14 พ.ย. 2569').replace('กำลังจะมา · 14 พ.ย. 2569','กำลังจะมา 14 พ.ย. 2569').replace("'เพิ่งจบไป · รอบชิงชนะเลิศ'","'เพิ่งจบไป'")
s=s.replace('14 พ.ย. 2569 · IoTE KMITL 2026 Showcase ที่ สจล.','14 พ.ย. 2569 ที่ IoTE สจล. (IoTE KMITL 2026 Showcase)')
s=s.replace('/* ---------- footer ---------- */','img[loading=lazy]{content-visibility:visible}\n/* ---------- footer ---------- */',1)
open('/home/claude/hamsterhub-home/v38.html','w').write(s)
css3=r'''
/* course cards: flat colour behind the senior posters, no watermark text or textures */
.cc-m{background-image:none!important}
.cc-m .mo,.cc-m::before,.cc-m::after{display:none!important}
.cc-m.th0{background:#FFB36B!important}.cc-m.th1{background:#4DA3F0!important}.cc-m.th2{background:#3A4A6B!important}
.cc-m.th3{background:#BFE3C9!important}.cc-m.th4{background:#1F2A44!important}.cc-m.th5{background:#FFE3A8!important}
/* about: no gradient wash at the top */
.ab-win,.aw,.ab-top{background:#fff!important;background-image:none!important}
'''
s=s.replace('/* ---------- footer ---------- */',css3+'\n/* ---------- footer ---------- */',1)
s=s.replace(' ›</a>','</a>')
open('/home/claude/hamsterhub-home/v38.html','w').write(s)
