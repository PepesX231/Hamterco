SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build27.py').read())
i=s.index('  <section class="fit">');j=s.index('</div></section>',i)+len('</div></section>')
fit=s[i:j];s=s[:i]+s[j:]
fit=fit.replace('<p class="fit-k">ยังไม่แน่ใจว่าเหมาะไหม</p><h2>ตอบ 3 ข้อ ดูว่าคอร์สนี้เหมาะกับน้องไหม</h2>','<p class="fit-k">ยังไม่แน่ใจว่าเริ่มคอร์สไหนดี</p><h2>ตอบ 3 ข้อ ดูว่าคอร์สไหนเหมาะกับน้อง</h2>')
k=s.index('    <section class="ct-help">')
s=s[:k]+'    <div class="ct-fit">'+fit+'</div>\n'+s[k:]
s=s.replace('/* ---------- footer ---------- */','.ct-fit{margin:56px 0}.ct-fit .fit{padding:0}\n/* ---------- footer ---------- */',1)
open('/home/claude/hamsterhub-home/v28.html','w').write(s)
print('v28 ok',s.count('id="fitQ"'))
