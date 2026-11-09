import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build34.py').read())
n=[0]
def add(m):
    art=m.group(0);link=re.search(r'data-link="([^"]+)"',art).group(1)
    k=art.index('<div class="tk-rail">');p=art.rfind('</div>',0,k)
    n[0]+=1
    return art[:p]+'<a class="tk-more" href="'+link+'" target="_blank" rel="noopener">ดูรายละเอียดผลงาน <b>→</b></a>\n      '+art[p:]
s=re.sub(r'<article class="tk-item tk-work[^>]*data-link="[^"]+".*?</article>',add,s,flags=re.S)
print('works',n[0])
css=r'''
/* ===== v35 ===== */
.tk-more{display:inline-flex;align-items:center;gap:8px;margin-top:14px;min-height:46px;padding:0 22px;background:#fff;color:#0B0B0B;font:700 1rem var(--display);text-decoration:none;pointer-events:auto;position:relative;z-index:3;transition:transform .15s,background .2s}
.tk-more b{transition:transform .2s}.tk-more:hover{background:var(--yel)}.tk-more:hover b{transform:translateX(4px)}
.yt-side{display:flex;flex-direction:column}
.yt-side .wkz{margin-top:auto;flex:none;width:100%}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v35.html','w').write(s)
print('v35 ok')
s=s.replace('.yt-side .wkz{margin-top:auto;flex:none;width:100%}','.yt-side .wkz{margin-top:auto;flex:none;width:100%}\n.tk-work .tk-hint{display:none!important}\n@media(max-width:900px){.yt-side .wkz{display:none}}',1)
open('/home/claude/hamsterhub-home/v35.html','w').write(s)
s=s.replace('<span class="ph-r"></span><span class="ph-r r2"></span>','')
assert 'class="ph-r' not in s
s=s.replace('/* ---------- footer ---------- */','.pt .ph-c img{box-shadow:none!important}\n/* ---------- footer ---------- */',1)
open('/home/claude/hamsterhub-home/v35.html','w').write(s)
