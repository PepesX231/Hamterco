SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build73.py').read())
import re
# back to the centred search-only hero
s=re.sub(r'<p class="zq-lead">.*?</p>','',s,count=1)
i=s.index('<div class="zq-ptn">');j=s.index('<div class="zq-brand"',i);k=s.index('</div>',s.index('<img',j))+6
s=s[:i]+s[k:]
a=s.index("/* hero: Hamster Hub's own look");b=s.index("/* home rows: startup leads")
s=s[:a]+s[b:]
assert 'zq-brand' not in s and 'zq-lead' not in s
open('/home/claude/hamsterhub-home/v74.html','w').write(s)
print('v74 ok')
