import re
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build54.py').read())
# remove activity deck
s=re.sub(r'<section class="dq" aria-label="ไทม์ไลน์กิจกรรม">.*?</section>\n    ','',s,count=1,flags=re.S)
assert 'id="dqSt"' not in s
# transition: no subtitle
s=s.replace('<small>Game · Web · IoT</small>','')
css=r'''
/* ===== v55 ===== */
/* login: the light drifts along the pill and breathes */
.login{background-size:100% 100%,100% 100%!important;animation:lgDrift 5s ease-in-out infinite}
@keyframes lgDrift{0%,100%{--ox:92%}50%{--ox:18%}}
@property --ox{syntax:"<percentage>";inherits:true;initial-value:92%}
.lg-orb{animation:lgOrb 5s ease-in-out infinite}
@keyframes lgOrb{0%,100%{right:-6px;opacity:.85}50%{right:calc(100% - 22px);opacity:.55}}
.login::before{animation:lgTw2 2.6s ease-in-out infinite alternate!important}
@keyframes lgTw2{from{opacity:.35}to{opacity:.9}}
.lg-t{animation:lgGlow 5s ease-in-out infinite}
@keyframes lgGlow{0%,100%{text-shadow:0 0 6px rgba(150,200,255,.25)}50%{text-shadow:0 0 12px rgba(170,215,255,.6)}}
.login:hover{animation-play-state:paused}
.login:hover .lg-orb,.login:hover .lg-t{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.login,.lg-orb,.lg-t,.login::before{animation:none!important}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v55.html','w').write(s)
print('v55 ok')
