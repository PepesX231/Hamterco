SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build66.py').read())
rep('<h2 id="ocH">น้องที่นี่ไปได้ไกลกว่าการติดมหาลัย</h2><p>เราสอนให้น้องสร้างของจริง ที่มีคนใช้ ขายได้ และชนะรางวัล การยื่นพอร์ตเป็นแค่หนึ่งในทางที่น้องเลือกได้</p>',
    '<h2 id="ocH">เราไม่ได้สอนแค่ทำพอร์ต<br>เราสอนให้น้องสร้างของจริง</h2><p>น้องที่นี่ทำแอปที่ช่วยคนได้ เกมที่มีคนเล่นจริง ผลงานที่ขายได้ และพอร์ตที่พาติดมหาลัย</p>')
CSS=r'''
/* v67: side course cards - landscape picture, text centred */
.fx-s{grid-template-columns:minmax(0,42%) minmax(0,1fr)!important;align-items:center!important;padding:18px!important}
.fx-si{aspect-ratio:4/3;align-self:center;height:auto}
.fx-si img{object-position:50% 22%!important}
.fx-sb{justify-content:center}
.fx-pr{margin-top:6px!important;padding-top:6px!important}
.oc-hd{max-width:900px}
@media (max-width:560px){.fx-s{grid-template-columns:minmax(0,1fr)!important}.fx-si{aspect-ratio:16/9}}
/* video column must never grow past its column */
.fx-media{aspect-ratio:auto!important;min-width:0;min-height:340px;height:100%}
@media (max-width:980px){.fx-media{aspect-ratio:16/9!important;min-height:0;height:auto}}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
s=s.replace('REVOICE แอปฝึกพูด ที่น้องไอดินสร้างเองใน 4 เดือน','REVOICE แอปฝึกพูด ที่<span class="nw">น้องไอดิน</span>สร้างเองใน 4 เดือน').replace('จนมีผลงานชิ้นแรกเป็นของตัวเอง</span>','จนมีผลงานชิ้นแรกเป็น<span class="nw">ของตัวเอง</span></span>').replace('.oc-hd{max-width:900px}','.oc-hd{max-width:900px}\n.nw{white-space:nowrap}')
open('/home/claude/hamsterhub-home/v67.html','w').write(s)
print('v67 ok')
