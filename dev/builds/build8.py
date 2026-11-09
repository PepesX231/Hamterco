D='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(D+'v2parts/build7.py').read())
i=s.index('        <div class="pf rv"');j=s.index('      <div class="ar-m">',i)
s=s[:i]+'''        <div class="ql rv" aria-label="สิ่งที่น้องจะได้">
          <p class="ql-h"><span>QUEST</span> เข้ารอบ Portfolio</p>
          <ul>
            <li><span class="pk"></span><b>เกม 3 งาน เข้าแฟ้มพอร์ต</b></li>
            <li><span class="pk"></span><b>แฟ้มพอร์ต + Pitch Deck พร้อมยื่น</b></li>
            <li><span class="pk"></span><b>ซ้อมนำเสนอและสัมภาษณ์กับอาจารย์มหาลัย</b></li>
          </ul>
          <div class="ql-xp"><span class="xl">LV.3</span><span class="xb"><span></span></span><span class="xr">READY</span></div>
          <div class="ql-ft"><span class="av"><img src="img/dek69-6.webp" alt=""><img src="img/dek69-1.webp" alt=""><img src="img/dek69-13.webp" alt=""><img src="img/dek69-11.webp" alt=""></span><p><b>รุ่นพี่ DEK69 ยื่นรอบพอร์ตติดแล้ว 48 คน</b><br>สจล. · จุฬาฯ CEDT · มหิดล · เกษตรศาสตร์</p></div>
        </div>
      </div>
'''+s[j:]
css=r'''
/* v8: everything pixel */
.ar-tc,.ar-k{border-radius:0!important;clip-path:polygon(0 4px,4px 4px,4px 0,calc(100% - 4px) 0,calc(100% - 4px) 4px,100% 4px,100% calc(100% - 4px),calc(100% - 4px) calc(100% - 4px),calc(100% - 4px) 100%,4px 100%,4px calc(100% - 4px),0 calc(100% - 4px));box-shadow:none!important}
.ar-tc{background:#FFD24A;box-shadow:inset 0 -4px 0 #C28A00!important;padding:7px 14px 9px!important}
.ar-k{background:#14372A!important;box-shadow:inset 0 -4px 0 #0B2219!important;padding:7px 14px 9px!important}
.ql{margin-top:26px;max-width:520px}
.ql-h{font:700 1.15rem var(--display);color:#fff;display:flex;align-items:center;gap:10px}
.ql-h span{font:400 .62rem var(--pixel);color:#0B0720;background:#7CF29A;padding:6px 8px 7px;box-shadow:inset 0 -3px 0 #2E9E6B}
.ql ul{list-style:none;padding:0;margin:14px 0 0;display:grid;gap:10px}
.ql li{display:flex;align-items:center;gap:12px;font-size:1.02rem}
.ql li b{font-weight:600;color:#E8EAF8}
.pk{position:relative;flex:none;width:20px;height:20px;background:#0B0720;box-shadow:0 0 0 3px #7CF29A}
.pk::after{content:"";position:absolute;left:3px;top:3px;width:4px;height:4px;background:#7CF29A;box-shadow:4px 4px 0 #7CF29A,8px 0 0 #7CF29A,12px -4px 0 #7CF29A,-0px 0 0 #7CF29A;opacity:0;animation:pkIn .01s steps(1) forwards}
.pk::after{left:2px;top:8px;width:3px;height:3px;box-shadow:3px 3px 0 #7CF29A,6px 3px 0 #7CF29A,6px 0 0 #7CF29A,9px 0 0 #7CF29A,9px -3px 0 #7CF29A,12px -3px 0 #7CF29A,12px -6px 0 #7CF29A}
.ql li:nth-child(1) .pk::after{animation-delay:.7s}.ql li:nth-child(2) .pk::after{animation-delay:1.1s}.ql li:nth-child(3) .pk::after{animation-delay:1.5s}
@keyframes pkIn{to{opacity:1}}
.ql-xp{display:flex;align-items:center;gap:10px;margin-top:16px;font:400 .55rem var(--pixel)}
.xl{color:#FFD24A}.xr{color:#7CF29A;animation:bl 1s steps(1) 1.9s infinite}
.xb{flex:1;max-width:300px;height:14px;background:#0B0720;box-shadow:0 0 0 3px #3A3290;padding:3px}
.xb span{display:block;height:100%;width:0;background:repeating-linear-gradient(90deg,#FFD24A 0 10px,#C28A00 10px 12px);animation:xp 1.4s steps(12) .5s forwards}
@keyframes xp{to{width:100%}}
.ql-ft{display:flex;align-items:center;gap:12px;margin-top:18px}
.ql-ft p{font-size:.84rem;color:#9AA0C8;line-height:1.45}.ql-ft b{color:#fff;font-size:.92rem}
.ql .av img{border-radius:0;border:3px solid #0B0720;box-shadow:0 0 0 2px #3A3290;margin-left:-6px;width:32px;height:32px}
.ql .av img:first-child{margin-left:0}
/* cabinet controls: pixel */
.cab-b .cap{border-radius:0;box-shadow:none!important;
  clip-path:polygon(30% 0,70% 0,70% 8%,84% 8%,84% 16%,92% 16%,92% 30%,100% 30%,100% 70%,92% 70%,92% 84%,84% 84%,84% 92%,70% 92%,70% 100%,30% 100%,30% 92%,16% 92%,16% 84%,8% 84%,8% 70%,0 70%,0 30%,8% 30%,8% 16%,16% 16%,16% 8%,30% 8%);
  background:linear-gradient(var(--h),var(--h)) 26% 22%/22% 16% no-repeat,linear-gradient(transparent 68%,var(--s) 68%),var(--c);transition:transform .1s steps(2)}
.cab-b:hover .cap{transform:translateY(.25em)}
.cab-b .lb{border-radius:0;font:700 .74em var(--display);clip-path:polygon(0 3px,3px 3px,3px 0,calc(100% - 3px) 0,calc(100% - 3px) 3px,100% 3px,100% calc(100% - 3px),calc(100% - 3px) calc(100% - 3px),calc(100% - 3px) 100%,3px 100%,3px calc(100% - 3px),0 calc(100% - 3px));box-shadow:inset 0 -3px 0 #07051A}
.cab-js .ball{border-radius:0;box-shadow:none;clip-path:polygon(30% 0,70% 0,70% 10%,90% 10%,90% 30%,100% 30%,100% 70%,90% 70%,90% 90%,70% 90%,70% 100%,30% 100%,30% 90%,10% 90%,10% 70%,0 70%,0 30%,10% 30%,10% 10%,30% 10%);background:linear-gradient(#FFB3C0,#FFB3C0) 28% 24%/22% 18% no-repeat,linear-gradient(transparent 66%,#9E1230 66%),#FF3B5C}
.cab-js .shaft{background:#3A3A3A;box-shadow:inset .15em 0 0 #6A6A6A}
.cab-js::after{border-radius:0;background:#0B0820;height:.8em;clip-path:polygon(10% 0,90% 0,100% 50%,90% 100%,10% 100%,0 50%)}
.cab-sign,.cab-bez{border-radius:0;clip-path:polygon(0 .5em,.5em .5em,.5em 0,calc(100% - .5em) 0,calc(100% - .5em) .5em,100% .5em,100% calc(100% - .5em),calc(100% - .5em) calc(100% - .5em),calc(100% - .5em) 100%,.5em 100%,.5em calc(100% - .5em),0 calc(100% - .5em))}
.cab-scr{border-radius:.3em}
.stk{border-radius:0;clip-path:polygon(0 3px,3px 3px,3px 0,calc(100% - 3px) 0,calc(100% - 3px) 3px,100% 3px,100% calc(100% - 3px),calc(100% - 3px) calc(100% - 3px),calc(100% - 3px) 100%,3px 100%,3px calc(100% - 3px),0 calc(100% - 3px));box-shadow:none}
.cab-door{border-radius:0}
.lamp{border-radius:0}
@media (max-width:900px){.ql{margin-left:auto;margin-right:auto;text-align:left}.ql-h{justify-content:center}}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v8.html','w').write(s)
print('v8 ok',len(s))
