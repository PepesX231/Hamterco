import re
D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build12.py').read())
def sub_all(a,b):
    global s
    assert a in s,a[:80];s=s.replace(a,b)
sub_all('<p class="pb-a">คอร์สช่วยน้อง ม.6<br>ทำพอร์ตยื่นมหาลัย</p><p class="pb-b">ไม่เคยทำผลงานมาก่อน ก็เริ่มได้</p>',
        '<p class="pb-a">คอร์สทำพอร์ต<br>สำหรับ ม.6</p><p class="pb-b">เรียน 2 เดือน มีผลงานไปยื่นมหาลัย</p>')
i=s.find('<div class="sc s2">')
while i!=-1:
    j=s.index('<div class="sc s3">',i)
    s=s[:i]+'''<div class="sc s2"><p class="pb-h">น้องได้ผลงานเป็นเกมที่เขียนโปรแกรมเอง<br>เอาไปใส่แฟ้มพอร์ตได้เลย</p><div class="pb-gs"><figure><img src="img/work-phi-krahang.webp" alt=""></figure><figure><img src="img/work-stressstrike.webp" alt=""></figure><figure><img src="img/work-midnight-at-roadside.webp" alt=""></figure></div><p class="pb-y">ผลงานแบบนี้บอกกรรมการได้ชัดว่า</p><p class="pb-r"><span>น้องเขียนโปรแกรมเป็น</span><span>คิดงานเองได้</span><span>ทำงานจนเสร็จ</span></p><p class="pb-n">ภาพตัวอย่างจากผลงานของรุ่นพี่</p></div>
  '''+s[j:]
    i=s.find('<div class="sc s2">',i+30)
sub_all('<p class="pb-h">จบคอร์ส ได้แฟ้มพอร์ตพร้อมยื่น</p><ul class="pb-ck"><li>ผลงานเกม 3 ชิ้นในแฟ้ม</li><li>สไลด์นำเสนอผลงาน</li><li>ซ้อมสัมภาษณ์กับอาจารย์มหาลัยจริง</li></ul>',
        '<p class="pb-h">จบคอร์ส ได้แฟ้มพอร์ต<br>พร้อมยื่นมหาลัย</p><ul class="pb-ck"><li>ผลงานเกมของน้องในแฟ้ม</li><li>สไลด์เล่าผลงาน</li><li>ซ้อมสัมภาษณ์กับอาจารย์มหาลัย</li></ul>')
sub_all('<p class="pb-h">รุ่นพี่ที่ทำแบบนี้<br>ติดมหาลัยแล้ว 48 คน</p>','<p class="pb-h">รุ่นพี่ทำแบบนี้<br>ติดมหาลัยแล้ว 48 คน</p>')
css=r'''
/* v13: scene 2 reads at a glance */
.s2 .pb-h{font-size:4cqw;text-align:center;line-height:1.3}.s2 .pb-gs figure{width:21cqw}
.pb-y{font:600 2.4cqw var(--display);color:#C9CDE8;animation-delay:5.2s!important}
.pb-r{display:flex;gap:1.4cqw;margin-top:-1cqw;animation-delay:5.5s!important}.pb-r span{font:700 2.5cqw var(--display);color:#0B0720;background:#7CF29A;padding:.6cqw 1.6cqw;border-radius:99px}
.s2 .pb-n{font-size:1.6cqw;margin-top:-1cqw}.s2{gap:2cqw!important}.s2 .pb-b.c{margin-top:-.6cqw}
.pb-gs{gap:3cqw}
.pb-gs figure{width:25cqw;padding:0;background:none;box-shadow:none!important;position:relative}
.pb-gs img{aspect-ratio:16/10;border-radius:1.2cqw;box-shadow:0 0 0 .5cqw #fff,0 1.6cqw 3cqw rgba(0,0,0,.5)}
.pb-gs figcaption{position:absolute;left:50%;bottom:-1.6cqw;transform:translateX(-50%);white-space:nowrap;font:700 2cqw var(--display);color:#0B0720;background:#FFD24A;padding:.5cqw 1.4cqw;border-radius:99px}
.pb-n{font:500 1.9cqw var(--display);color:#9AA0C8;margin-top:1.6cqw}
.s2 .pb-n{animation-delay:5s}
.s3 .pb-h{font-size:4.4cqw;line-height:1.25}
.pb-ck li{font-size:3.5cqw}
'''
s=s.replace('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */',1)
for a,b in [('class="pg p1"','class="pgx q1"'),('class="pg p2"','class="pgx q2"'),('class="pg p3"','class="pgx q3"'),('.pg.p1','.pgx.q1'),('.pg.p2','.pgx.q2'),('.pg.p3','.pgx.q3'),('.pg{','.pgx{'),('.pg::','.pgx::'),(',.pg,',',.pgx,')]:
    s=s.replace(a,b)
open('/home/claude/hamsterhub-home/v13.html','w').write(s)
print('v13 ok',len(s))
