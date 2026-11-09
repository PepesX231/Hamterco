SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build62.py').read())
PX='https://www.hamsterhub.co/portex-site/index.html'
LINE='https://page.line.me/jkm4247u?openQrModal=true'

# ---------- featured (recommended) block ----------
def av(ids):
    return ''.join('<img src="img/dek69-%d.webp" alt="" loading="lazy">'%i for i in ids)
FT_GRID='''<div class="ft-g">
    <a class="ft-main" href="'''+PX+'''" target="_blank" rel="noopener">
      <span class="ft-media"><video src="img/portex-hero.mp4" poster="img/portex-poster.webp" muted loop playsinline preload="none" aria-hidden="true"></video><span class="ft-live">เปิดรับสมัคร</span></span>
      <span class="ft-body">
        <small>สำหรับน้อง ม.6 ที่ยังไม่มีผลงาน</small>
        <b class="ft-t">Port Express</b>
        <span class="ft-d">จบคอร์ส น้องมีแฟ้มพอร์ตพร้อมยื่นรอบ Portfolio ผลงานในแฟ้มคือเกมที่น้องเขียนโปรแกรมสร้างเองด้วย Unity</span>
        <span class="ft-f"><span><b>2 เดือน</b>เรียนจันทร์ พุธ ศุกร์</span><span><b>9 พ.ย. 2569</b>วันเริ่มเรียน</span><span><b>5,990 บาท</b>ค่าเรียนทั้งคอร์ส</span></span>
        <span class="ft-cta">ดูรายละเอียดคอร์ส</span>
      </span>
    </a>
    <div class="ft-side">
      <a class="ft-s" href="'''+LINE+'''" target="_blank" rel="noopener">
        <small>สำหรับน้องที่ยังไม่เคยเขียนโปรแกรม</small><b>Hamstarter</b>
        <p>เริ่มจากศูนย์ จนมีผลงานชิ้นแรกเป็นของตัวเอง</p>
        <span class="ft-pr"><span class="ft-av">'''+av([1])+'''</span>น้องปลื้มจากคอร์สนี้ ติดสถิติประยุกต์ฯ สจล.</span>
        <span class="ft-sb">รับแจ้งเตือนรอบถัดไป</span>
      </a>
      <a class="ft-s" href="'''+LINE+'''" target="_blank" rel="noopener">
        <small>สำหรับน้องที่อยากมีรางวัลระดับประเทศในพอร์ต</small><b>National Project</b>
        <p>ทำโปรเจกต์ส่งเวทีระดับประเทศ เช่น NSC (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย)</p>
        <span class="ft-pr"><span class="ft-av">'''+av([3,6,16])+'''</span>รุ่นพี่ 5 คนจากคอร์สนี้ ติดวิศวะคอมฯ CEDT และวิทย์คอมฯ</span>
        <span class="ft-sb">รับแจ้งเตือนรอบถัดไป</span>
      </a>
    </div>
  </div>'''
FT='''<section class="ft"><div class="ft-in">
  <div class="ft-hd"><h2>คอร์สที่เราแนะนำ</h2><p>คอร์สหลักของ Hamster Hub เลือกตามสิ่งที่น้องอยากได้</p></div>
  '''+FT_GRID+'''
</div></section>
'''
# ---------- story: statement + chapters ----------
WH='''<section class="wh"><div class="wh-in"><p class="wh-t" id="whT">ปี 2569 รุ่นพี่ <strong>48 คน</strong> ที่ทำผลงานกับเรา ยื่นพอร์ตแล้วติด <strong>สจล. มหิดล จุฬาฯ และเกษตรศาสตร์</strong> เส้นทางของพวกเขาเริ่มแบบนี้</p></div></section>
'''
posters=[3,6,13,10,16,4]
CH='''<section class="ch" id="ch" aria-label="เส้นทางของรุ่นพี่">
  <div class="ch-pin">
    <div class="ch-txt">
      <div class="ch-hd"><h2>จากวันแรก ถึงวันที่ติดมหาลัย</h2></div>
      <div class="ch-bar" aria-hidden="true"><i></i></div>
      <div class="ch-list">
        <div class="ch-w" style="order:1"><span class="ch-n">วันแรก</span><h3>ไม่ต้องเก่งมาก่อน ก็เริ่มได้</h3><p>น้องได้เจอเพื่อนที่ชอบเรื่องเดียวกัน มีพี่ๆ คอยดูแลใกล้ชิด และเริ่มจากพื้นฐานเทคโนโลยีที่ต้องใช้จริง</p></div>
        <div class="ch-w" style="order:3"><span class="ch-n">ระหว่างเรียน</span><h3>สร้างผลงานของตัวเองทั้งชิ้น</h3><p>น้องเขียนโปรแกรมสร้างเกม เว็บ หรืออุปกรณ์ IoT เอง ตั้งแต่ไอเดียจนใช้งานได้ คลิปนี้คือเกมที่น้องๆ ทำในปี 2569</p></div>
        <div class="ch-w" style="order:5"><span class="ch-n">เอาออกไปใช้จริง</span><h3>ส่งแข่ง และให้คนใช้จริง</h3><p>12 ผลงานเข้ารอบชิงชนะเลิศ NSC (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย) ในคลิป ไอดินเล่าว่าเขามาถึงตรงนี้ได้ยังไง</p><button type="button" class="ch-snd" data-v="2">เปิดเสียงคลิปไอดิน</button></div>
        <div class="ch-w" style="order:7"><span class="ch-n">วันยื่นพอร์ต</span><h3>ยื่นพอร์ต แล้วติดมหาลัย</h3><p>พี่ๆ ช่วยแนะนำการยื่นรอบ Portfolio จนรุ่นพี่ได้เรียนวิศวะคอมฯ CEDT และวิทย์คอมฯ ในมหาลัยที่อยากเข้า</p><a class="ch-lk" href="#works" data-pane="sen">ดูรุ่นพี่ทั้งหมด</a></div>
      </div>
    </div>
    <div class="ch-stage">
      <figure class="ch-m" style="order:0"><div class="ch-col"><img src="img/photo-class.webp" alt="น้องๆ ในห้องเรียน Hamster Hub" loading="lazy"><img src="img/photo-camp.webp" alt="น้องๆ ในค่าย" loading="lazy"><img src="img/photo-desk.webp" alt="น้องๆ ทำงานที่โต๊ะคอม" loading="lazy"><img src="img/team-group.webp" alt="รูปรวมน้องๆ และทีม" loading="lazy"></div></figure>
      <figure class="ch-m" style="order:2"><video src="img/reel.mp4" poster="img/reel-poster.webp" muted loop playsinline preload="none" aria-label="คลิปเกมที่น้องๆ ทำ"></video></figure>
      <figure class="ch-m ch-sq" style="order:4"><video src="img/story-nsc.mp4" poster="img/story-nsc.webp" muted loop playsinline preload="none" aria-label="คลิปไอดิน ผู้ชนะ NSC 2025"></video></figure>
      <figure class="ch-m" style="order:6"><div class="ch-wall">'''+''.join('<img src="img/dek69-%d.webp" alt="" loading="lazy">'%i for i in posters)+'''</div></figure>
    </div>
  </div>
</section>
'''
# ---------- reorder home ----------
i=s.index('<section class="hp-grid nw2">');j=s.index('<section class="zc2 dk">')
news=s[i:j];s=s[:i]+s[j:]
i=s.index('<section class="zb">');j=s.index('<div class="wkz wkz-rift" id="wkRift">')
s=s[:i]+WH+CH+'\n  '+s[j:]
rep('<section class="zc2 dk">',FT+'  <section class="zc2 dk">')
rep('<h2>คอร์สเรียน</h2><p>ทุกคอร์สจบแล้วน้องได้ผลงานจริงของตัวเอง','<h2>คอร์สทั้งหมด</h2><p>ทุกคอร์สจบแล้วน้องได้ผลงานจริงของตัวเอง')
k=s.index('<section class="end">');s=s[:k]+news+'\n  '+s[k:]
# courses page: the featured block first
rep('<div class="zq-g ctg" id="zqC2"></div>','<div class="ft ft-c">'+FT_GRID+'</div><h2 class="ct-all">คอร์สทั้งหมด</h2><div class="zq-g ctg" id="zqC2"></div>')

# ---------- search: chips + suggestions ----------
i=s.index('<p class="zq-pop">');j=s.index('</p>',i)+4
s=s[:i]+'<p class="zq-pop"><span>ลองพิมพ์</span><button type="button" data-q="อยากเข้าวิศวะคอม">อยากเข้าวิศวะคอม</button><button type="button" data-q="ม.6 ยังไม่มีพอร์ต">ม.6 ยังไม่มีพอร์ต</button><button type="button" data-q="อยากทำเกมของตัวเอง">อยากทำเกมของตัวเอง</button><button type="button" data-q="Hamster Hub คืออะไร">Hamster Hub คืออะไร</button><button type="button" data-q="ค่าเรียนเท่าไหร่">ค่าเรียนเท่าไหร่</button></p>'+s[j:]
i=s.index('<div class="zq-sug" id="zqSug" hidden>');j=s.index('</div>',i)+6
SUG=[('อยากเข้าวิศวะคอม','i3-cap','ดูคอร์สที่รุ่นพี่วิศวะคอมฯ เรียน'),('อยากเข้าแพทย์','i3-cap','เราช่วยเรื่องไหนได้บ้าง'),('อยากทำเกมของตัวเอง','i3-pad','คอร์สและค่ายสร้างเกม'),('ไม่เคยเขียนโปรแกรมเลย','i3-rocket','เริ่มจากศูนย์ได้ไหม'),('ผู้ปกครอง ลูกจะได้อะไร','i3-bot','สิ่งที่ลูกได้จากที่นี่')]
s=s[:i]+'<div class="zq-sug" id="zqSug" hidden><p>น้องพิมพ์แบบนี้ได้เลย</p>'+''.join('<button type="button" data-q="%s"><img src="img/%s.webp" alt="">%s<small>%s</small></button>'%(q,im,q,d) for q,im,d in SUG)+'</div>'+s[j:]
rep('<p class="zq-r" id="zqR" aria-live="polite"></p>','<p class="zq-r" id="zqR" aria-live="polite"></p><div class="ia-w" id="zqA" hidden></div>')
rep("input id=\"zqIn\" type=\"search\" placeholder=\"พิมพ์สิ่งที่น้องอยากทำ เช่น อยากติดวิศวะคอม หรือ อยากทำเกม\"","input id=\"zqIn\" type=\"search\" placeholder=\"พิมพ์สิ่งที่น้องอยากได้ เช่น อยากเข้าวิศวะคอม\"")

# ---------- intent engine ----------
INT=r'''
    /* v63: answers by intent - what the kid typed, which course helps and why */
    var UNF={k:'สจล. (พระจอมเกล้าลาดกระบัง)',m:'มหิดล',c:'จุฬาฯ',u:'เกษตรศาสตร์'},UNN={k:24,m:9,c:8,u:7};
    var UN0=(typeof UN!=='undefined')?UN:{k:'สจล.',m:'มหิดล',c:'จุฬาฯ',u:'เกษตรศาสตร์'};
    function gf(f){return G.filter(f)}
    var INT=[
     {re:/สจล|ลาดกระบัง|kmitl|พระจอมเกล้า/,u:'k'},{re:/จุฬา|chula|(^|[^a-z])cu([^a-z]|$)/,u:'c'},{re:/มหิดล|mahidol/,u:'m'},{re:/เกษตร|kasetsart|(^|[^a-z])ku([^a-z]|$)/,u:'u'},
     {re:/แพทย์|หมอ|เภสัช|พยาบาล|ทันต|สัตวแพทย์|(^|[^a-z])med|กายภาพ|สาธารณสุข|เทคนิคการแพทย์/,h:'อยากเข้าแพทย์ หรือคณะสายสุขภาพ',
      a:'Hamster Hub สอนสายเทคโนโลยี เราไม่มีคอร์สติวสอบแพทย์ แต่ถ้าน้องอยากมีผลงานที่ไม่เหมือนใครในพอร์ต เช่น แอปหรืออุปกรณ์ที่ช่วยเรื่องสุขภาพ ทีมช่วยน้องสร้างได้',
      f:['ตัวอย่างผลงานจริง: StressStrike เกมที่เล่นด้วยการบีบอุปกรณ์วัดแรงมือ ชนะเลิศ OBEC Roboplayground'],pk:'ถ้าอยากมีผลงานเทคในพอร์ต',
      p:[['Project Express','มีไอเดียเรื่องสุขภาพแล้ว ทีมช่วยทำให้เสร็จทันยื่นพอร์ต'],['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ ได้ทั้งผลงานและรางวัลใส่พอร์ต']],r:['อยากทำ IoT','Hamster Hub คืออะไร']},
     {re:/วิศว|วิดวะ|engineer|cedt|วิศวกรรม/,h:'อยากเข้าวิศวะคอมฯ หรือ CEDT',
      a:'พอร์ตสายนี้จะแข็งแรงขึ้นมาก ถ้ามีผลงานที่น้องเขียนโปรแกรมเองทั้งชิ้น และเล่าได้ว่าทำยังไง คอร์สข้างล่างพาน้องไปถึงตรงนั้น รุ่นพี่ 11 คนข้างล่างติดวิศวะคอมฯ หรือ CEDT แล้ว',
      p:[['Port Express','ม.6 ที่ยังไม่มีผลงาน: 2 เดือน น้องได้เกมที่เขียนโค้ดเองด้วย Unity (ภาษา C#) พร้อมแฟ้มพอร์ตยื่นรอบ Portfolio'],['Project Express','มีไอเดียแล้วแต่ทำไม่เสร็จ: ทีมช่วยทำให้เสร็จทันยื่น พี่จุ๊บกับน้องไอซ์จากคอร์สนี้ติด CEDT จุฬาฯ'],['National Project','อยากมีผลงานแข่งระดับประเทศในพอร์ต: น้องปิ่นโตจากคอร์สนี้ติดวิศวะคอมฯ มหิดล'],['Python Pro Pack','ยังไม่เคยเขียนโค้ด: เริ่มพื้นฐานที่นี่ น้องมิกจากคอร์สนี้ติดวิศวะคอมฯ มหิดล']],
      s:function(g){return /วิศว|CEDT/.test(g[3])},r:['อยากเข้าวิทย์คอม','ม.6 ยังไม่มีพอร์ต','ค่าเรียนเท่าไหร่']},
     {re:/วิทย์คอม|วิทยาการคอม|computer|(^|[^a-z])cs([^a-z]|$)|ไอที|(^|[^a-z])it([^a-z]|$)|(^|[^a-z])ict|สารสนเทศ|ดิจิทัล|คอมพิว|คอม/,h:'อยากเข้าวิทย์คอมฯ หรือไอที',
      a:'สายนี้ดูว่าน้องใช้โปรแกรมแก้ปัญหาได้จริงไหม ผลงานที่มีคนใช้ หรือเคยส่งแข่ง ช่วยให้พอร์ตเด่นกว่าใบเกียรติบัตร รุ่นพี่ 5 คนข้างล่างติดวิทยาการคอมพิวเตอร์แล้ว',
      p:[['Business Project','อยากทำแอปหรือเกมที่มีคนใช้จริง: น้องเบสท์และน้องจุนกิจากคอร์สนี้ติดวิทย์คอมฯ'],['National Project','ส่งผลงานแข่งระดับประเทศ: น้องแมนยูจากคอร์สนี้ติดวิทย์คอมฯ สจล.'],['Project Express','มีไอเดียแล้ว ทำให้เสร็จทันยื่น: น้องปิงย่าจากคอร์สนี้ติดวิทย์คอมฯ เกษตรฯ ศรีราชา'],['Python Pro Pack','ยังไม่เคยเขียนโค้ด เริ่มพื้นฐานที่นี่']],
      s:function(g){return /วิทยาการ|วิทย์คอม/.test(g[3])},r:['อยากเข้าวิศวะคอม','อยากทำเว็บหรือแอป']},
     {re:/สถิติ|สิ่งแวดล้อม|วิทยาศาสตร์|วิทย์|science|ฟิสิกส์|เคมี|ชีวะ|คณิต|ข้อมูล|data/,h:'อยากเข้าคณะสายวิทยาศาสตร์',
      a:'ผลงานเทคช่วยพอร์ตสายวิทย์ได้เหมือนกัน เช่น โปรแกรมเก็บและวิเคราะห์ข้อมูล หรือเกมสอนวิทยาศาสตร์ รุ่นพี่ข้างล่างติดสถิติประยุกต์ และเทคโนโลยีสิ่งแวดล้อม',
      p:[['Hamstarter','ยังไม่มีผลงานเลย: น้องปลื้มจากคอร์สนี้ติดสถิติประยุกต์ฯ สจล.'],['Project Express','มีไอเดียแล้ว ทีมช่วยทำให้เสร็จทันยื่น'],['SciGame Lab Camp','ค่ายสร้างเกมวิทยาศาสตร์ ลองก่อนว่าชอบไหม']],
      s:function(g){return /สถิติ|สิ่งแวดล้อม/.test(g[3])},r:['เริ่มจากศูนย์ได้ไหม']},
     {re:/hamster|แฮมสเตอร์|แฮม|คืออะไร|ที่นี่|เกี่ยวกับ|เป็นใคร|ทำอะไร|บริษัท|สถาบัน|น่าเชื่อ/,h:'Hamster Hub คืออะไร',
      a:'Hamster Hub สอนน้องมัธยมสร้างเกม เว็บ และ IoT จนมีผลงานจริงของตัวเอง ไว้ยื่นพอร์ตเข้ามหาลัย ส่งแข่ง หรือต่อยอดเป็นธุรกิจ ไม่ต้องเก่งมาก่อนก็เริ่มได้',
      f:['ปี 2569 รุ่นพี่ติดมหาลัยรอบ Portfolio แล้ว 48 คน','12 ผลงานของน้องเข้ารอบชิงชนะเลิศ NSC (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย)','จัดกิจกรรมร่วมกับคณะเทคโนโลยีสารสนเทศ สจล., IoTE สจล. และ EDUverse'],
      p:[['Port Express','คอร์สหลักที่เปิดรับตอนนี้ สำหรับน้อง ม.6'],['Hamstarter','สำหรับน้องที่ยังไม่มีผลงาน']],lk:['#about','อ่านเรื่องของเรา'],r:['ค่าเรียนเท่าไหร่','ผู้ปกครอง ลูกจะได้อะไร']},
     {re:/ราคา|เท่าไ|กี่บาท|ค่าเรียน|ค่าคอร์ส|บาท|แพง|ผ่อน|ส่วนลด/,h:'ค่าเรียน',
      a:'Port Express คอร์ส 2 เดือน ค่าเรียน 5,990 บาท ส่วนคอร์สอื่นยังไม่เปิดรอบ ราคาจะแจ้งตอนเปิดรับ กดรับแจ้งเตือน หรือทัก LINE ถามทีมได้',
      p:[['Port Express','เปิดรับแล้ว เริ่มเรียน 9 พ.ย. 2569']],r:['เรียนวันไหน','Hamster Hub คืออะไร']},
     {re:/วันไหน|กี่โมง|ตาราง|ออนไลน์|online|onsite|ที่ไหน|เรียนยังไง|เวลาเรียน|เปิดเมื่อ|สมัคร|เริ่มเรียน|กี่วัน|นานไหม/,h:'เรียนเมื่อไหร่ สมัครยังไง',
      a:'Port Express เรียนจันทร์ พุธ ศุกร์ นาน 2 เดือน เริ่ม 9 พ.ย. 2569 สมัครได้ที่หน้าคอร์ส ส่วนสถานที่และเวลาเรียน ถามทีมทาง LINE ได้เลย',
      p:[['Port Express','ดูรายละเอียดและสมัครที่หน้าคอร์ส']],r:['ค่าเรียนเท่าไหร่']},
     {re:/ผู้ปกครอง|ลูก|พ่อ|แม่|ผปค/,h:'ลูกจะได้อะไรจาก Hamster Hub',
      a:'ลูกได้ผลงานจริงที่ทำเอง ไว้ยื่นพอร์ตเข้ามหาลัย ได้เพื่อนที่ชอบเรื่องเดียวกัน และมีพี่ๆ คอยดูแลใกล้ชิด ปี 2569 รุ่นพี่ติดมหาลัยรอบ Portfolio แล้ว 48 คน',
      p:[['Port Express','ถ้าลูกอยู่ ม.6 และยังไม่มีผลงาน'],['Hamstarter','ถ้าลูกยังไม่เคยเขียนโปรแกรม']],s:function(g){return true},r:['ค่าเรียนเท่าไหร่','เรียนวันไหน']},
     {re:/ม\.?\s?6|(^|[^0-9])ม6|dek\s?70|เด็ก\s?70|ปีสุดท้าย/,h:'น้อง ม.6 (DEK70)',
      a:'เวลาเหลือไม่มาก เลือกคอร์สที่จบแล้วมีแฟ้มพอร์ตพร้อมยื่นรอบ Portfolio ได้เลย',
      p:[['Port Express','2 เดือน ได้เกมที่ทำเองพร้อมแฟ้มพอร์ต เปิดรับแล้ว'],['Port70','คอร์สทำพอร์ตสำหรับ DEK70 รอบถัดไป'],['Project Express','มีไอเดียแล้ว ทีมช่วยทำให้เสร็จทันยื่น']],r:['อยากเข้าวิศวะคอม','ค่าเรียนเท่าไหร่']},
     {re:/ม\.?\s?[45]|(^|[^0-9])ม[45]|dek\s?7[12]/,h:'น้อง ม.4–5',
      a:'มีเวลาพอสร้างผลงานดีๆ และลองส่งแข่งก่อนถึงวันยื่นพอร์ต',
      p:[['National Project','ส่งผลงานแข่งระดับประเทศ ได้รางวัลใส่พอร์ต'],['Hamstarter','ยังไม่มีผลงาน เริ่มที่นี่'],['Python Pro Pack','ปูพื้นเขียนโปรแกรม'],['AI Camp Season 2','ค่าย 3 วัน สร้างเกมหรือเว็บด้วย AI']]},
     {re:/ม\.?\s?[123]|ม\.?ต้น|ประถม|ป\.?\s?[456]/,h:'น้อง ม.ต้น',
      a:'เริ่มจากค่ายสั้นๆ หรือคอร์สพื้นฐาน ให้น้องรู้ก่อนว่าชอบสายไหน',
      p:[['Hamstarter','คอร์สเริ่มต้นสำหรับคนที่ยังไม่มีผลงาน'],['Python Pro Pack','เรียนเขียนโปรแกรมด้วย Python'],['Python Adventure Camp','ค่ายเขียน Python แบบผจญภัย']]},
     {re:/มือใหม่|ไม่เคย|ไม่เก่ง|ไม่มีพื้น|ศูนย์|เริ่มต้น|python|ไพธอน|โค้ด|เขียนโปรแกรม|coding|code/,h:'เริ่มจากศูนย์ได้ไหม',
      a:'ได้ น้องไม่ต้องเก่งมาก่อน คอร์สเริ่มต้นพาน้องเขียนโปรแกรมจนมีผลงานชิ้นแรกของตัวเอง',
      p:[['Hamstarter','สำหรับน้องที่ยังไม่มีผลงาน น้องปลื้มจากคอร์สนี้ติดสถิติประยุกต์ฯ สจล.'],['Python Pro Pack','เรียนเขียนโปรแกรมด้วย Python น้องมิกจากคอร์สนี้ติดวิศวะคอมฯ มหิดล'],['Python Adventure Camp','ค่ายเขียน Python แบบผจญภัย']],r:['อยากทำเกมของตัวเอง']},
     {re:/เกม|game|unity|roblox|godot/,h:'อยากทำเกมของตัวเอง',
      a:'ที่นี่น้องเขียนโปรแกรมสร้างเกมเอง ตั้งแต่ไอเดียจนเล่นได้จริง ปีนี้มีเกมของน้องๆ 10 เกมใน Hall of Fame และเกม PHC Map มีคนเล่นแล้วกว่า 1,000 คน',
      p:[['Port Express','ม.6: ได้เกมที่ทำเองด้วย Unity พร้อมแฟ้มพอร์ต'],['Hamstarter','ยังไม่เคยทำเกม เริ่มที่นี่'],['GameJam X ปีที่ 5','แข่งสร้างเกมในเวลาจำกัด'],['AI Camp Season 2','ค่าย 3 วัน สาย Unity หรือ Roblox']],lk:['#works','ดูเกมที่น้องๆ ทำ'],r:['ม.6 ยังไม่มีพอร์ต']},
     {re:/เว็บ|web|แอป|แอพ|(^|[^a-z])app|เว็บไซต์|website/,h:'อยากทำเว็บหรือแอป',
      a:'น้องสร้างเว็บหรือแอปที่ใช้งานได้จริง เช่น Hamster Quest เว็บเรียนที่เล่นเหมือนเกม ซึ่งกำลังเตรียมใช้กับมหาวิทยาลัย',
      p:[['AI Camp Season 2','ค่าย 3 วัน มีสาย Web App'],['Business Project','ทำแอปที่ต่อยอดเป็นธุรกิจ'],['Python Pro Pack','ปูพื้นเขียนโปรแกรม']]},
     {re:/iot|ไอโอที|หุ่นยนต์|robot|arduino|esp|บอร์ด|อุปกรณ์|เซนเซอร์|sensor|ไฟฟ้า/,h:'อยากทำ IoT หรือหุ่นยนต์',
      a:'น้องสร้างอุปกรณ์ที่ทำงานร่วมกับโปรแกรมได้จริง เช่น StressStrike เกมที่เล่นด้วยการบีบอุปกรณ์วัดแรงมือ ชนะเลิศ OBEC Roboplayground',
      p:[['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ'],['Project Express','มีไอเดียแล้ว ทีมช่วยทำให้เสร็จ'],['IoTE KMITL 2026 Showcase (Hallow Open House)','ดูผลงาน IoT ของจริง']]},
     {re:/(^|[^a-z])ai([^a-z]|$)|เอไอ|chatgpt|gpt|ปัญญาประดิษฐ์|machine/,h:'อยากใช้ AI สร้างผลงาน',
      a:'น้องใช้ AI ช่วยสร้างเกม เว็บ และโปรเจกต์ธุรกิจได้ภายในไม่กี่วัน',
      p:[['AI Camp Season 2','สร้างเกมหรือเว็บด้วย AI ใน 3 วัน'],['All for One University รอบชิงชนะเลิศ','แข่งสร้างผลงานเทค 4 วันด้วย AI'],['AI for Business','เวิร์กชอปใช้ AI ในธุรกิจ']]},
     {re:/ธุรกิจ|สตาร์ทอัพ|startup|ขาย|หาเงิน|business|บริหาร|การตลาด|ผู้ประกอบการ/,h:'อยากทำสตาร์ทอัพหรือธุรกิจ',
      a:'ผลงานของน้องต่อยอดเป็นธุรกิจได้จริง เช่น Mr. City เกมแนะนำที่เที่ยวในสงขลา ขายให้สวนสัตว์สงขลาแล้ว',
      p:[['Business Project','ทำโปรเจกต์ที่ต่อยอดเป็นธุรกิจ'],['AI for Business','เวิร์กชอปใช้ AI ในธุรกิจ']],s:function(g){return g[4]==='Business Project'}},
     {re:/แข่ง|nsc|รางวัล|ประกวด|jam|โอลิมปิก|เวที/,h:'อยากส่งผลงานแข่ง',
      a:'12 ผลงานของน้องเข้ารอบชิงชนะเลิศ NSC (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย) รางวัลจากเวทีแบบนี้ใส่พอร์ตได้เลย',
      p:[['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ'],['All for One University รอบชิงชนะเลิศ','รอบชิงวันที่ 14 พ.ย. 2569 ที่ IoTE สจล.'],['NSC Software Project 2026','ทำโปรเจกต์ส่ง NSC'],['GameJam X ปีที่ 5','แข่งสร้างเกมในเวลาจำกัด']],s:function(g){return g[4]==='National Project'}},
     {re:/ค่าย|camp|ปิดเทอม|เวิร์กชอป|workshop|กิจกรรม|อีเวนต์|event/,h:'ค่ายและกิจกรรม',
      a:'ค่ายและเวิร์กชอปช่วงสั้นๆ ให้น้องลองทำผลงานจริงก่อนเรียนคอร์สยาว',
      p:[['All for One University รอบชิงชนะเลิศ','กิจกรรมถัดไป 14 พ.ย. 2569'],['AI Camp Season 2','สร้างเกมหรือเว็บด้วย AI ใน 3 วัน'],['Game Pee Camp','ค่ายสร้างเกมสยองขวัญ'],['Dek70 Camp','ค่ายเตรียมพอร์ตสำหรับ DEK70']],lk:['#activity','ดูกิจกรรมทั้งหมด']},
     {re:/พอร์ต|port|มหาลัย|มหาวิทยาลัย|tcas|ยื่น|สัมภาษณ์|แฟ้ม|รอบ\s?1|ติด/,h:'อยากมีพอร์ตยื่นมหาลัย',
      a:'พอร์ตที่ดีมีผลงานที่น้องทำเอง และเล่าได้ว่าทำยังไง ปี 2569 รุ่นพี่ Hamster Hub ติดมหาลัยรอบ Portfolio แล้ว 48 คน',
      p:[['Port Express','ม.6 ที่ยังไม่มีผลงาน: 2 เดือนได้เกมที่ทำเองพร้อมแฟ้มพอร์ต'],['Port70','คอร์สทำพอร์ตสำหรับ DEK70 รอบถัดไป'],['Project Express','มีไอเดียแล้ว ทีมช่วยทำให้เสร็จทันยื่น']],s:function(g){return true},r:['อยากเข้าวิศวะคอม','อยากเข้าวิทย์คอม']}
    ];
    function esc(t){return String(t).replace(/[<>&"]/g,function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]})}
    function uniI(u){var S=gf(function(g){return g[2]===u}),cs=[];S.forEach(function(g){if(cs.indexOf(g[4])<0&&IT.some(function(x){return x.t===g[4]}))cs.push(g[4])});
      return {h:'อยากเข้า'+UNF[u],a:'ปี 2569 รุ่นพี่ Hamster Hub ติด'+UN0[u]+'รอบ Portfolio แล้ว '+UNN[u]+' คน ข้างล่างคือบางส่วน พร้อมคอร์สที่เขาเรียน',
        p:cs.slice(0,4).map(function(c){var n=S.filter(function(g){return g[4]===c}).map(function(g){return g[1]});return [c,n.join(' ')+' เรียนคอร์สนี้ แล้วติด'+UN0[u]]}),s:function(g){return g[2]===u},r:['อยากเข้าวิศวะคอม','ม.6 ยังไม่มีพอร์ต']}}
    function intent(q){var t=q.toLowerCase();for(var i=0;i<INT.length;i++){if(INT[i].re.test(t))return INT[i].u?uniI(INT[i].u):INT[i]}return null}
    function pickH(p){var x=IT.filter(function(y){return y.t===p[0]})[0];if(!x)return '';
      var st=x.open?(x.pr?'เปิดรับแล้ว ค่าเรียน '+x.pr:'เปิดรับแล้ว'):(x.k==='course'?'รอบถัดไป กดรับแจ้งเตือนได้':x.st);
      return '<li><a class="ia-c'+(x.open?' on':'')+'" href="'+x.url+'" target="_blank" rel="noopener"><img src="'+x.img+'" alt="" loading="lazy"><span class="ia-b"><b>'+esc(x.t)+'</b><em>'+p[1]+'</em><small>'+st+'</small></span><i class="ia-go">'+(x.open?'ดูรายละเอียด':(x.k==='course'?'รับแจ้งเตือน':'ดูกิจกรรม'))+'</i></a></li>'}
    function snH(g){return '<figure class="ia-sn"><span class="ia-av"><img src="img/dek69-'+g[0]+'.webp" alt="" loading="lazy"></span><figcaption><b>'+g[1]+'</b><span>'+g[3]+' '+UN0[g[2]]+'</span><small>คอร์ส '+g[4]+'</small></figcaption></figure>'}
    function ansH(I,q){var h='<div class="ia"><p class="ia-q">คำตอบสำหรับ “'+esc(q)+'”</p><h3>'+I.h+'</h3><p class="ia-a">'+I.a+'</p>';
      if(I.f)h+='<ul class="ia-f">'+I.f.map(function(f){return '<li>'+f+'</li>'}).join('')+'</ul>';
      if(I.p&&I.p.length)h+='<p class="ia-k">'+(I.pk||'คอร์สและกิจกรรมที่ช่วยได้')+'</p><ol class="ia-p">'+I.p.map(pickH).join('')+'</ol>';
      if(I.s){var S=gf(I.s);if(S.length>8)S=S.filter(function(g,i){return i%2===0}).concat(S.filter(function(g,i){return i%2})).slice(0,8);if(S.length)h+='<p class="ia-k">รุ่นพี่ที่ไปทางนี้แล้ว</p><div class="ia-s">'+S.map(snH).join('')+'</div>'}
      h+='<div class="ia-x">'+(I.r?'<span>ถามต่อ</span>'+I.r.map(function(r){return '<button type="button" data-q="'+r+'">'+r+'</button>'}).join(''):'')+(I.lk?'<a class="ia-lk" href="'+I.lk[0]+'">'+I.lk[1]+'</a>':'')+'<a class="ia-line" href="'+LINE+'" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div></div>';return h}
    function search(q){q=(q||'').trim();var R=$('#zqRes'),A=$('#zqA');if(!q){R.hidden=true;return}var I=intent(q);
      if(I){R.hidden=false;$('#zqR').textContent='';G2.innerHTML='';A.innerHTML=ansH(I,q);A.hidden=false;R.scrollTop=0;return}
      A.hidden=true;A.innerHTML='';search0(q)}
'''
rep("    function search(q){q=(q||'').trim();var R=$('#zqRes');if(!q){R.hidden=true;return}R.hidden=false;var toks",INT+"    function search0(q){q=(q||'').trim();var R=$('#zqRes');if(!q){R.hidden=true;return}R.hidden=false;var toks")
rep("'<div class=\"zq-e\"><b>ยังไม่มีคอร์สหรือกิจกรรมที่ตรงกับคำนี้</b><p>บอกทีมได้ว่าน้องอยากทำอะไร ทีมช่วยแนะนำให้</p><a href=\"'+LINE+'\" target=\"_blank\" rel=\"noopener\">ทัก LINE ถามทีม</a></div>'",
    "'<div class=\"zq-e\"><b>ยังไม่เจอคำตอบตรงๆ สำหรับคำนี้</b><p>ลองพิมพ์แบบนี้ หรือบอกทีมว่าน้องอยากได้อะไร</p><p class=\"zq-e-q\"><button type=\"button\" data-q=\"อยากเข้าวิศวะคอม\">อยากเข้าวิศวะคอม</button><button type=\"button\" data-q=\"อยากทำเกมของตัวเอง\">อยากทำเกมของตัวเอง</button><button type=\"button\" data-q=\"เริ่มจากศูนย์ได้ไหม\">เริ่มจากศูนย์ได้ไหม</button></p><a href=\"'+LINE+'\" target=\"_blank\" rel=\"noopener\">ทัก LINE ถามทีม</a></div>'")
# the hero typing words follow the new intents
rep("var W2=['ยื่นพอร์ตเข้ามหาลัย','สร้างเกมของตัวเอง','ทำหุ่นยนต์ IoT','เรียน AI','สร้างสตาร์ทอัพ','เขียน Python','ลงแข่ง Game Jam','ทำเว็บของตัวเอง']","var W2=['ยื่นพอร์ตเข้ามหาลัย','เข้าวิศวะคอม','สร้างเกมของตัวเอง','ทำหุ่นยนต์ IoT','ติด CEDT จุฬาฯ','สร้างสตาร์ทอัพ','เขียนโปรแกรมเป็น','ทำเว็บของตัวเอง']")

JS=r'''  /* v63: featured video plays only while on screen */
  (function(){if(!('IntersectionObserver' in window))return;var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting&&!matchMedia('(prefers-reduced-motion:reduce)').matches){v.play().catch(function(){})}else v.pause()})},{threshold:.35});
    document.querySelectorAll('.ft-media video').forEach(function(v){io.observe(v)})})();
  /* v63: statement words fill in as it crosses the screen */
  (function(){var p=$('#whT');if(!p)return;var seg=window.Intl&&Intl.Segmenter?new Intl.Segmenter('th',{granularity:'word'}):null;
    function wrap(node){[].slice.call(node.childNodes).forEach(function(n){if(n.nodeType===3){var f=document.createDocumentFragment(),parts=seg?Array.from(seg.segment(n.textContent),function(x){return x.segment}):n.textContent.split(/(\s+)/);
      parts.forEach(function(t){if(/^\s+$/.test(t)||!t){f.appendChild(document.createTextNode(t));return}var sp=document.createElement('span');sp.className='w';sp.textContent=t;f.appendChild(sp)});n.replaceWith(f)}else if(n.nodeType===1)wrap(n)})}
    p.setAttribute('aria-label',p.textContent);wrap(p);var W=p.querySelectorAll('.w'),last=-1,raf=0;
    if(matchMedia('(prefers-reduced-motion:reduce)').matches){W.forEach(function(w){w.classList.add('on')});return}
    function draw(){raf=0;var r=p.getBoundingClientRect(),vh=innerHeight,st=vh*.82,en=vh*.42,t=Math.min(1,Math.max(0,(st-r.top)/Math.max(1,(st-en)+r.height))),k=Math.round(t*W.length);if(k===last)return;last=k;for(var i=0;i<W.length;i++)W[i].classList.toggle('on',i<k)}
    function req(){if(!raf)raf=requestAnimationFrame(draw)}
    new IntersectionObserver(function(e){if(e[0].isIntersecting){addEventListener('scroll',req,{passive:true});req()}else removeEventListener('scroll',req)},{rootMargin:'20% 0px'}).observe(p)})();
  /* v63: chapters - the photo of each step uncovers the last as you scroll; still and stacked on small screens */
  (function(){var s=$('#ch');if(!s)return;var ms=[].slice.call(s.querySelectorAll('.ch-m')),ws=[].slice.call(s.querySelectorAll('.ch-w')),bar=s.querySelector('.ch-bar i'),n=ms.length,cur=-1,raf=0,near=false,live=false,rm=matchMedia('(prefers-reduced-motion:reduce)');
    function fits(){return innerWidth>900&&innerHeight>=560&&!rm.matches}
    function vids(k){ms.forEach(function(m,i){var v=m.querySelector('video');if(!v)return;if(near&&(k<0||i===k)&&!rm.matches)v.play().catch(function(){});else v.pause()})}
    function draw(){raf=0;if(!live)return;var r=s.getBoundingClientRect(),p=Math.min(1,Math.max(0,-r.top/Math.max(1,r.height-innerHeight))),seg=1/n,k=0;
      ms.forEach(function(m,i){var u=i===0?1:Math.min(1,Math.max(0,(p-(i-.3)*seg)/(.45*seg))),e=1-Math.pow(1-u,3);m.style.setProperty('--c',((1-e)*100).toFixed(2)+'%');m.style.setProperty('--z',(1.06-.06*e).toFixed(4));if(u>=.5)k=i});
      if(bar)bar.style.transform='scaleY('+(.08+p*.92).toFixed(3)+')';
      if(k!==cur){cur=k;ws.forEach(function(w,i){w.classList.toggle('on',i===k)});vids(k)}}
    function req(){if(!raf)raf=requestAnimationFrame(draw)}
    function sync(){live=fits();s.classList.toggle('live',live);cur=-1;if(!live){ws.forEach(function(w){w.classList.add('on')});ms.forEach(function(m){m.style.removeProperty('--c');m.style.removeProperty('--z')});vids(-1)}else req()}
    new IntersectionObserver(function(e){near=e[0].isIntersecting;if(near){addEventListener('scroll',req,{passive:true});req()}else removeEventListener('scroll',req);if(!live)vids(-1);else{cur=-1;req()}},{rootMargin:'10% 0px'}).observe(s);
    var t;addEventListener('resize',function(){clearTimeout(t);t=setTimeout(sync,150)});sync();
    s.querySelectorAll('.ch-snd').forEach(function(b){b.addEventListener('click',function(){var v=ms[+b.dataset.v].querySelector('video');v.muted=!v.muted;if(!v.muted){v.currentTime=0;v.play().catch(function(){})}b.textContent=v.muted?'เปิดเสียงคลิปไอดิน':'ปิดเสียง'})})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')

CSS=r'''
/* ===== v63: answers, featured courses, story ===== */
.zq-sw .zq-res{max-height:min(640px,70vh)!important}
.ia-w[hidden]{display:none}
.ia{padding:2px 2px 0}
.ia-q{font:600 .85rem var(--display);color:#6A7891;margin:0 44px 6px 0}
.ia h3{font:800 clamp(1.3rem,2.2vw,1.65rem)/1.25 var(--display);color:#0D2E63;margin:0}
.ia-a{color:#2B3A55;margin:8px 0 0;max-width:64ch;line-height:1.65}
.ia-f{margin:12px 0 0;padding:0;list-style:none;display:grid;gap:6px;color:#2B3A55;font-size:.93rem}
.ia-f li{position:relative;padding-left:18px;line-height:1.55}.ia-f li::before{content:"";position:absolute;left:4px;top:.6em;width:6px;height:6px;border-radius:50%;background:#1C74D9}
.ia-k{font:700 .92rem var(--display);color:#0D2E63;margin:20px 0 10px}
.ia-p{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.ia-c{display:grid;grid-template-columns:104px minmax(0,1fr) auto;gap:14px;align-items:center;padding:10px 14px 10px 10px;border-radius:16px;background:#fff;box-shadow:inset 0 0 0 1px #E1E8F2;text-decoration:none;color:inherit;transition:transform .2s,box-shadow .2s}
.ia-c:hover{transform:translateY(-2px);box-shadow:inset 0 0 0 1px #B7CBEA,0 10px 24px -16px rgba(13,46,99,.5)}
.ia-c img{width:104px;height:68px;object-fit:cover;border-radius:10px;display:block}
.ia-b{display:grid;gap:3px;min-width:0}
.ia-b b{font:800 1.04rem var(--display);color:#0D2E63}
.ia-b em{font-style:normal;color:#2B3A55;font-size:.92rem;line-height:1.5}
.ia-b small{color:#6A7891;font-size:.8rem}.ia-c.on .ia-b small{color:#137A43;font-weight:700}
.ia-go{font:700 .85rem var(--display);font-style:normal;padding:9px 14px;border-radius:10px;background:#EEF4FD;color:#1C5FC8;white-space:nowrap;transition:background .2s}
.ia-c.on .ia-go{background:#1C74D9;color:#fff}.ia-c:hover .ia-go{background:#DCE8FA}.ia-c.on:hover .ia-go{background:#155FB5}
.ia-s{display:flex;gap:10px;overflow-x:auto;padding:2px 2px 8px;scrollbar-width:thin}
.ia-sn{flex:0 0 auto;display:flex;gap:10px;align-items:center;margin:0;padding:8px 14px 8px 8px;border-radius:14px;background:#F3F6FB;width:240px}
.ia-av{width:50px;height:50px;border-radius:50%;overflow:hidden;flex:none;background:#D9E2EF}
.ia-av img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;transform:scale(1.9);transform-origin:50% 42%}
.ia-sn figcaption{display:grid;gap:1px;min-width:0}.ia-sn b{font:700 .92rem var(--display);color:#0D2E63}.ia-sn span{font-size:.8rem;color:#2B3A55;line-height:1.35}.ia-sn small{color:#6A7891;font-size:.75rem}
.ia-x{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:18px;padding-top:14px;border-top:1px solid #E6ECF5}
.ia-x>span{font:600 .85rem var(--display);color:#6A7891;margin-right:2px}
.ia-x button,.zq-e-q button{border:0;background:#EEF2F8;color:#0D2E63;font:600 .86rem var(--display);padding:8px 12px;border-radius:10px;cursor:pointer;transition:background .2s}
.ia-x button:hover,.zq-e-q button:hover{background:#DCE4F0}
.ia-lk{font:700 .88rem var(--display);color:#1C5FC8;text-decoration:none;padding:8px 10px}.ia-lk:hover{text-decoration:underline}
.ia-line{margin-left:auto;background:#06C755;color:#fff;font:700 .9rem var(--display);padding:9px 16px;border-radius:10px;text-decoration:none;transition:transform .15s}
.ia-line:hover{transform:translateY(-1px)}.ia-line:active,.ia-go:active{transform:scale(.97)}
.zq-e-q{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:0 0 16px!important}
@media (max-width:700px){.ia-c{grid-template-columns:76px minmax(0,1fr);padding:8px}.ia-c img{width:76px;height:56px}.ia-go{display:none}.ia-line{margin-left:0}.ia-sn{width:210px}}

.ft{background:#fff;padding:clamp(72px,8vw,120px) 16px clamp(28px,3vw,44px)}
.ft-in{max-width:1240px;margin:0 auto}
.ft-hd h2{font:800 clamp(2.2rem,4.4vw,3.6rem)/1.1 var(--display);color:#0D2E63;margin:0}
.ft-hd p{color:#4A5874;margin:10px 0 0;font-size:1.05rem}
.ft-g{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,1fr);gap:20px;margin-top:32px}
.ft-c .ft-g{margin-top:8px}
.ft-main{display:grid;grid-template-rows:auto 1fr;border-radius:28px;overflow:hidden;background:#0D2E63;color:#fff;text-decoration:none;box-shadow:0 30px 60px -36px rgba(13,46,99,.7);transition:transform .25s}
.ft-main:hover{transform:translateY(-2px)}
.ft-media{position:relative;aspect-ratio:16/9;overflow:hidden;background:#1D1550 url(img/portex-poster.webp) center/cover}
.ft-media video{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s cubic-bezier(.22,1,.36,1)}
.ft-main:hover .ft-media video{transform:scale(1.025)}
.ft-live{position:absolute;left:16px;top:16px;display:flex;align-items:center;gap:7px;background:#fff;color:#137A43;font:700 .85rem var(--display);padding:7px 13px;border-radius:999px}
.ft-live::before{content:"";width:8px;height:8px;border-radius:50%;background:#1DB45A}
.ft-body{display:grid;gap:10px;padding:24px 28px 28px;align-content:start}
.ft-body small{color:#9FC4FF;font:600 .95rem var(--display)}
.ft-t{font:800 clamp(2rem,3.4vw,2.8rem)/1 var(--display)}
.ft-d{color:#D7E4FA;line-height:1.6;max-width:58ch}
.ft-f{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:6px}
.ft-f>span{background:rgba(255,255,255,.08);border-radius:14px;padding:12px 14px;font-size:.85rem;color:#BFD3F3}
.ft-f b{display:block;font:800 1.15rem var(--display);color:#fff;margin-bottom:2px}
.ft-cta{justify-self:start;margin-top:8px;background:#fff;color:#0D2E63;font:800 1rem var(--display);padding:13px 22px;border-radius:12px;transition:transform .2s}
.ft-main:hover .ft-cta{transform:translateY(-2px)}.ft-main:active .ft-cta{transform:scale(.97)}
.ft-side{display:grid;gap:20px}
.ft-s{display:grid;gap:8px;align-content:start;border-radius:24px;background:#F3F6FB;padding:24px;text-decoration:none;color:inherit;transition:transform .2s,box-shadow .2s}
.ft-s:hover{transform:translateY(-2px);box-shadow:inset 0 0 0 1px #CFDDF1}
.ft-s small{color:#1C5FC8;font:700 .88rem var(--display)}
.ft-s>b{font:800 1.6rem var(--display);color:#0D2E63}
.ft-s p{margin:0;color:#2B3A55;line-height:1.55}
.ft-pr{display:flex;align-items:center;gap:10px;margin-top:6px;font-size:.86rem;color:#4A5874;line-height:1.4}
.ft-av{display:flex;flex:none}.ft-av img{width:34px;height:34px;border-radius:50%;object-fit:cover;object-position:50% 30%;border:2px solid #F3F6FB;margin-left:-8px;background:#D9E2EF}.ft-av img:first-child{margin-left:0}
.ft-sb{justify-self:start;margin-top:6px;font:700 .9rem var(--display);color:#1C5FC8;background:#fff;padding:10px 14px;border-radius:10px;box-shadow:inset 0 0 0 1px #D5E1F2}
.ct-all{font:800 clamp(1.6rem,3vw,2.2rem) var(--display);color:#0D2E63;margin:56px 0 20px}
@media (max-width:900px){.ft-g{grid-template-columns:minmax(0,1fr)}}
@media (max-width:560px){.ft-f{grid-template-columns:minmax(0,1fr)}.ft-body{padding:20px}}

.wh{background:#fff;padding:clamp(110px,15vw,220px) 16px clamp(80px,10vw,140px)}
.wh-in{max-width:1100px;margin:0 auto}
.wh-t{font:800 clamp(1.9rem,4.4vw,3.8rem)/1.25 var(--display);color:#0D2E63;margin:0;text-wrap:pretty}
.wh-t strong{font-weight:inherit}
.wh-t .w{color:#CAD4E3;transition:color .18s ease}
.wh-t .w.on{color:#0D2E63}.wh-t strong .w.on{color:#1C74D9}
@media (prefers-reduced-motion:reduce){.wh-t .w{color:#0D2E63}.wh-t strong .w{color:#1C74D9}}

.ch{background:#fff;padding:0 16px clamp(80px,9vw,140px)}
.ch-pin{max-width:1240px;margin:0 auto;display:flex;flex-direction:column;gap:20px}
.ch-txt,.ch-list,.ch-stage{display:contents}
.ch-hd{order:-1}.ch-hd h2{font:800 clamp(2rem,4vw,3.2rem)/1.15 var(--display);color:#0D2E63;margin:0 0 8px}
.ch-bar{display:none}
.ch-n{display:inline-block;font:700 .9rem var(--display);color:#1C5FC8;background:#EEF4FD;padding:5px 11px;border-radius:999px}
.ch-w h3{font:800 clamp(1.5rem,2.6vw,2.2rem)/1.2 var(--display);color:#0D2E63;margin:12px 0 8px}
.ch-w p{color:#2B3A55;line-height:1.7;margin:0;max-width:46ch;font-size:1.05rem}
.ch-w{margin-bottom:28px}
.ch-snd,.ch-lk{display:inline-block;margin-top:16px;border:0;cursor:pointer;font:700 .95rem var(--display);padding:11px 18px;border-radius:12px;background:#0D2E63;color:#fff;text-decoration:none;transition:transform .15s}
.ch-snd:hover,.ch-lk:hover{transform:translateY(-1px)}.ch-snd:active,.ch-lk:active{transform:scale(.97)}
.ch-m{margin:0;border-radius:22px;overflow:hidden;background:#0B0F1A;aspect-ratio:16/10;position:relative}
.ch-m>video{width:100%;height:100%;object-fit:cover;display:block}
.ch-sq>video{object-fit:contain;background:#000}
.ch-col{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:6px;width:100%;height:100%}
.ch-col img,.ch-wall img{width:100%;height:100%;object-fit:cover;display:block;min-height:0}
.ch-wall{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:6px;width:100%;height:100%}
.ch-wall img{object-position:50% 30%}
/* live: pinned, words on the left, the step's picture on the right */
.ch.live{height:440vh;padding:0 16px}
.ch.live .ch-pin{position:sticky;top:60px;height:calc(100vh - 60px);display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.35fr);gap:clamp(32px,4vw,64px);align-items:center}
.ch.live .ch-txt{display:grid;grid-template-columns:4px minmax(0,1fr);grid-template-rows:auto auto;column-gap:22px;row-gap:28px;align-content:center}
.ch.live .ch-hd{grid-column:1/-1}
.ch.live .ch-bar{display:block;grid-row:2;width:4px;border-radius:4px;background:#E3E9F2;overflow:hidden;align-self:stretch}
.ch.live .ch-bar i{display:block;width:100%;height:100%;background:#1C74D9;transform-origin:50% 0;transform:scaleY(.08)}
.ch.live .ch-list{display:grid;grid-row:2}
.ch.live .ch-w{grid-area:1/1;margin:0;opacity:0;transform:translateY(10px);pointer-events:none;transition:opacity .22s ease,transform .22s ease}
.ch.live .ch-w.on{opacity:1;transform:none;pointer-events:auto;transition:opacity .42s cubic-bezier(.22,1,.36,1) .06s,transform .52s cubic-bezier(.22,1,.36,1) .06s}
.ch.live .ch-stage{display:block;position:relative;height:min(70vh,640px);border-radius:28px;overflow:hidden;background:#0B0F1A;box-shadow:0 40px 80px -50px rgba(13,46,99,.7)}
.ch.live .ch-m{position:absolute;inset:0;border-radius:0;aspect-ratio:auto;clip-path:inset(var(--c,0%) 0 0 0)}
.ch.live .ch-m:first-child{clip-path:none}
.ch.live .ch-m>*{transform:scale(var(--z,1));transform-origin:50% 100%}
@media (max-width:900px){.ch-m{aspect-ratio:4/3}.ch-sq{aspect-ratio:1}}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v63.html','w').write(s)
print('v63 ok')
