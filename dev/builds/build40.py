import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build39.py').read())
# order: 1 ask/search  2 news  3 courses  then who we are, HoF, seniors
i=s.index('<div class="zq-p">');j=s.index('</div>\n  </section>',i)
s=s[:i]+'<div class="zq-res" id="zqRes" hidden><p class="zq-r" id="zqR" aria-live="polite"></p><div class="zq-g" id="zqG"></div></div>'+s[j+6:]
# lift news out and put it right after the search
i=s.index('<section class="hp-grid nw2">');j=s.index('</section>',i)+10;NEWS=s[i:j];s=s[:i]+s[j:]
NEWS=NEWS.replace('<h2 class="nw2-h">ข่าวและกิจกรรมล่าสุด</h2>','<h2 class="nw2-h">ข่าวสาร</h2>')
NEWS=NEWS[:-10]+'<div class="nw2-l"><h3>กิจกรรมล่าสุด</h3><div class="zq-g" id="zqN"></div><a class="nw2-all" href="#activity">ดูกิจกรรมทั้งหมด</a></div></section>'
CRS='''<section class="zc2"><div class="zc2-in"><h2>คอร์สเรียน</h2><p>คอร์สที่เปิดรับตอนนี้ และคอร์สที่กดรับแจ้งเตือนรอบใหม่ได้</p><div class="zq-g" id="zqC"></div></div></section>'''
i=s.index('<section class="zh">');s=s[:i]+NEWS+'\n  '+CRS+'\n  '+s[i:]
# JS: results only while searching; fill news + courses
rep("function search(q){q=(q||'').trim();if(!q){tab('pop');return}","function search(q){q=(q||'').trim();var R=$('#zqRes');if(!q){R.hidden=true;return}R.hidden=false;")
rep("    tab('pop');\n","    $('#zqC').innerHTML=IT.filter(function(x){return x.k==='course'}).map(cardH).join('');\n    $('#zqN').innerHTML=IT.filter(function(x){return x.k!=='course'}).slice(1,5).map(cardH).join('');\n")
rep("$('#zqIn').value=b.dataset.q;search(b.dataset.q);$('.zq').scrollIntoView({behavior:'smooth'})","$('#zqIn').value=b.dataset.q;search(b.dataset.q);$('.zq').scrollIntoView({behavior:'smooth'})")
css=r'''
/* ===== v40 ===== */
.zq-res{max-width:1240px;margin:32px auto 0;background:#fff;border-radius:28px;padding:20px clamp(16px,2.4vw,32px) 28px;box-shadow:0 20px 50px -30px rgba(13,46,99,.35)}
.zq-res .zq-r{margin:0}
.zq-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:16px}
.nw2{background:#fff;padding:clamp(56px,6vw,88px) 0 clamp(40px,4vw,64px)!important}
.nw2-h{font-size:clamp(2rem,3.6vw,2.8rem)!important}
.nw2-l{max-width:1240px;margin:36px auto 0;padding:0 24px}
.nw2-l h3{font:800 1.4rem var(--display);color:#0D2E63}
.nw2-all{display:inline-block;margin-top:18px;font:700 1rem var(--display);color:#1C74D9;text-decoration:none}
.zc2{background:#F2F5FA;padding:clamp(56px,6vw,88px) 0}
.zc2-in{max-width:1240px;margin:0 auto;padding:0 24px}
.zc2 h2{font:800 clamp(2rem,3.6vw,2.8rem) var(--display);color:#0D2E63}.zc2-in>p{color:#4A5874;margin-top:8px}
@media (max-width:1000px){.zq-g{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:700px){.zq-g{grid-template-columns:minmax(0,1fr)}}
'''
s=s.replace('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */',1)
open('/home/claude/hamsterhub-home/v40.html','w').write(s)
print('v40 ok')
