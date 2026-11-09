SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build67.py').read())
STAR='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z" fill="currentColor"/></svg>'
# badges on the featured cards
s=s.replace('<span class="ft-live">เปิดรับสมัคร</span></span>\n      <span class="fx-body">','<span class="ft-live">เปิดรับสมัคร</span></span>\n      <span class="fx-body"><span class="rc">'+STAR+'คอร์สแนะนำอันดับ 1</span>')
s=s.replace('<span class="fx-sb">\n          <small>','<span class="fx-sb">\n          <span class="rc rc-s">'+STAR+'คอร์สแนะนำ</span><small>')
# courses page: say clearly these are recommended
rep('<div class="ft ft-c">','<div class="ft ft-c"><div class="ft-hd ct-rc"><h2>'+STAR.replace('aria-hidden="true"','class="ct-star" aria-hidden="true"')+'คอร์สที่เราแนะนำ</h2><p>3 คอร์สหลักของ Hamster Hub ถ้ายังไม่รู้จะเริ่มคอร์สไหน เริ่มจากตรงนี้</p></div>')
# the same star on these courses inside every course grid and rail
rep("(x.open?'<span class=\"qv-live\">เปิดรับ</span>':'')+'</span>","(x.open?'<span class=\"qv-live\">เปิดรับ</span>':'')+(['Port Express','Hamstarter','National Project'].indexOf(x.t)>-1?'<span class=\"qv-rc\">"+STAR.replace('"','\\"')+"แนะนำ</span>':'')+'</span>")
CSS=r'''
/* v68: recommended badges */
.rc{display:inline-flex;align-items:center;gap:6px;align-self:flex-start;font:800 .85rem var(--display);color:#5A3B00;background:linear-gradient(180deg,#FFD866,#FFC02E);padding:6px 12px 6px 9px;border-radius:999px;box-shadow:0 6px 16px -8px rgba(200,140,0,.8)}
.rc svg{width:15px;height:15px}
.rc-s{font-size:.78rem;padding:4px 10px 4px 7px;margin-bottom:2px}.rc-s svg{width:13px;height:13px}
.ft.ft-c{padding:0!important;background:none}.ct-rc{margin:0 0 20px}.ct-rc h2{display:flex;align-items:center;gap:12px;font:800 clamp(1.8rem,3.4vw,2.6rem)/1.15 var(--display);color:#0D2E63;margin:0}
.ct-star{width:.9em;height:.9em;color:#FFB800;flex:none}
.ct-rc p{color:#4A5874;margin:8px 0 0}
.qv-im{position:relative}
.qv-rc{position:absolute;right:10px;top:10px;display:inline-flex;align-items:center;gap:4px;font:800 .75rem var(--display);color:#5A3B00;background:linear-gradient(180deg,#FFD866,#FFC02E);padding:4px 9px 4px 6px;border-radius:999px;box-shadow:0 4px 12px -6px rgba(0,0,0,.4)}
.qv-rc svg{width:12px;height:12px}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v68.html','w').write(s)
print('v68 ok', s.count('class="rc'), s.count('qv-rc'))
