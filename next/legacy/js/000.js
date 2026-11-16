
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $=function(s){return document.querySelector(s)},$$=function(s){return Array.prototype.slice.call(document.querySelectorAll(s))};
  var W=[['stressstrike','StressStrike'],['beyond-the-board','Beyond the Board'],['eugation-strike','Eugation Strike'],['slash-speed','SLASH//SPEED'],['micro-immersive-sim','Micro Immersive Sim'],['phi-krahang','ผีกระหัง'],['midnight-at-roadside','Midnight at Roadside'],['hot-hot-hot','Hot Hot Hot'],['apocalypis-building','Apocalypis Building'],['escape-rolling','Escape Rolling']];
  var UN={k:'สจล.',m:'มหิดล',c:'จุฬาฯ',u:'เกษตรศาสตร์'},UC={k:'#E8742A',m:'#3F5FD0',c:'#D9558C',u:'#2E9E6B'};
  var G=[[1,'น้องปลื้ม','k','สถิติประยุกต์ฯ','Hamstarter'],[2,'น้องมินนี่','k','เทคโนโลยีสิ่งแวดล้อม','Project For Port69'],[3,'น้องดา','k','วิศวะคอมฯ และวิทย์คอมฯ','National Project'],[4,'น้องเบสท์','k','วิทยาการคอมพิวเตอร์','Business Project'],[5,'น้องแมนยู','k','วิทยาการคอมพิวเตอร์','National Project'],[6,'น้องต้นกล้า','c','CEDT','National Project'],[7,'น้องไอซ์','c','CEDT','Project Express'],[8,'น้องเฟิร์ส','c','CEDT','Port70'],[9,'พี่มิคกี้','c','CEDT','National Project'],[10,'พี่จุ๊บ','c','CEDT','Project Express'],[11,'น้องจุนกิ','u','วิทยาการคอมพิวเตอร์','Business Project'],[12,'น้องปิงย่า','u','วิทยาการคอมพิวเตอร์ ศรีราชา','Project Express'],[13,'น้องอาร์ม','m','วิศวกรรมคอมพิวเตอร์','Business Project'],[14,'น้องมิก','m','วิศวกรรมคอมพิวเตอร์','Python Pro Pack'],[15,'น้องเช','m','วิศวกรรมคอมพิวเตอร์','Project Express 2'],[16,'น้องปิ่นโต','m','วิศวกรรมคอมพิวเตอร์','National Project'],[17,'น้องไอซ์','m','วิศวกรรมคอมพิวเตอร์','Port70']];
  var link=function(w){return 'https://www.hamsterhub.co/go/hall-of-fame/'+w[0]};
  var AW={"stressstrike": "ชนะเลิศ OBEC Roboplayground"},VID=["stressstrike", "eugation-strike", "slash-speed", "apocalypis-building", "escape-rolling"],ACT=[["14 พ.ย. 2569", "All for One University รอบชิงชนะเลิศ", "รอบออนไซต์ที่ IoTE สจล.", "แข่งขัน", 1], ["7 พ.ย. 2569", "IoTE KMITL 2026 Showcase (Hallow Open House)", "โชว์ผลงานออนไลน์ ไลฟ์ YouTube เข้าร่วมฟรี", "โชว์ผลงาน", 0], ["ต.ค. 2569", "All for One University รอบออนไลน์", "แข่งสร้างผลงานเทค 4 วันด้วย AI", "แข่งขัน", 0], ["14–16 ส.ค.", "SciGame Lab Camp", "ค่ายสร้างเกมวิทยาศาสตร์", "ค่าย", 0], ["31 มี.ค. – 31 ก.ค.", "NSC Software Project 2026", "ทำโปรเจกต์ส่งการแข่งขันซอฟต์แวร์ระดับประเทศ", "โครงการ", 0], ["20 มิ.ย.", "AI for Business", "เวิร์กชอปใช้ AI ในธุรกิจ", "เวิร์กชอป", 0], ["19–21 มิ.ย.", "AI Camp Season 2", "สร้างเกมหรือเว็บด้วย AI ใน 3 วัน สาย Unity / Roblox / Web App", "ค่าย", 0], ["10–12 มิ.ย.", "Game Pee Camp", "ค่ายสร้างเกมสยองขวัญ", "ค่าย", 0], ["1–29 มิ.ย.", "StarLight", "โครงการพัฒนาผลงานตลอดเดือน", "โครงการ", 0], ["8–13 พ.ค.", "Intelligence Camp EP-2", "ค่ายพัฒนาทักษะ", "ค่าย", 0], ["24–27 เม.ย.", "GameJam X ปีที่ 5", "แข่งสร้างเกมในเวลาจำกัด", "แข่งขัน", 0], ["20–22 มี.ค.", "Dek-70 Camp", "ค่ายเตรียมพอร์ตสำหรับ DEK70", "ค่าย", 0], ["13–15 มี.ค.", "Intelligence Camp", "ค่ายพัฒนาทักษะ", "ค่าย", 0], ["27 ก.พ. – 6 มี.ค.", "Python x Hunter Camp", "ค่ายเขียน Python", "ค่าย", 0], ["30 ม.ค. – 1 ก.พ.", "Dek70 Camp", "ค่ายเตรียมพอร์ตสำหรับ DEK70", "ค่าย", 0], ["23–25 ม.ค.", "Tech Booster for Teens", "เวิร์กชอปเทคโนโลยีสำหรับวัยรุ่น", "เวิร์กชอป", 0], ["12–16 ม.ค.", "Python Adventure Camp", "ค่ายเขียน Python แบบผจญภัย", "ค่าย", 0], ["10–11 ม.ค.", "Kid Day", "กิจกรรมวันเด็ก", "เวิร์กชอป", 0]];
  var NK={stressstrike:['วิน',''],'beyond-the-board':['กัปตัน',''],'eugation-strike':['ไผ่',''],'slash-speed':['ดินสอ',''],'micro-immersive-sim':['เพชร',''],'phi-krahang':['นนท์',''],'midnight-at-roadside':['Windy',''],'hot-hot-hot':['โอม',''],'apocalypis-building':['ฟาร์',''],'escape-rolling':['เป๊ป','']};
  var LINE='https://page.line.me/jkm4247u?openQrModal=true';
  function card(w,i,cls){var n=NK[w[0]],v=VID.indexOf(w[0])>-1,a=AW[w[0]];
    return '<button type="button" class="'+cls+'" data-i="'+i+'" data-vid="'+(v?1:0)+'" data-aw="'+(a?1:0)+'"><span class="th"><img src="/Hamterco/img/work-'+w[0]+'.webp" alt="" loading="lazy">'+(v?'<span class="badge pl">▶ มีคลิป</span>':'')+'</span><span class="by"><span class="av">'+n[0].charAt(0)+'</span><span><b>'+w[1]+'</b><span>น้อง'+n[0]+'</span>'+(a?'<span class="aw">'+a+'</span>':'<span>ผลงานปี 2569</span>')+'</span></span></button>'}
  /* home: hall of fame grid (6) */
  var hg=$('#hgrid');if(hg&&0)hg.innerHTML=W.slice(0,6).map(function(w,i){return card(w,i,'hw rv')}).join('').replace(/class="badge pl"/g,'class="pl"');
  /* works: grid */
  $('#vgrid').innerHTML=W.map(function(w,i){return card(w,i,'vc')}).join('');
  $$('#hofChips button').forEach(function(b){b.addEventListener('click',function(){$$('#hofChips button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});var f=b.dataset.f;$$('#vgrid .vc').forEach(function(c){c.hidden=!(f==='all'||(f==='vid'&&c.dataset.vid==='1')||(f==='aw'&&c.dataset.aw==='1'))})})});
  /* seniors */
  var mix=[5,0,12,10,2,6,13,11,3,7,14,1,8,15,4,9,16];
  function sfig(g){return '<figure data-u="'+g[2]+'"><img src="/Hamterco/img/dek69-'+g[0]+'.webp" alt="'+g[1]+'" loading="lazy"><figcaption><b>'+g[1]+'</b><span>'+g[3]+' · '+UN[g[2]]+'<br>คอร์ส '+g[4]+'</span></figcaption></figure>'}
  if($('#srow'))$('#srow').innerHTML=mix.map(function(i){return sfig(G[i])}).join('');
  $('#sgrid').innerHTML=G.map(sfig).join('');
  $('#senChips').innerHTML='<button type="button" data-u="all" aria-pressed="true">ทั้งหมด 17</button>'+['k','m','c','u'].map(function(k){return '<button type="button" data-u="'+k+'" aria-pressed="false">'+UN[k]+' '+G.filter(function(g){return g[2]===k}).length+'</button>'}).join('');
  function ufilter(btns,figs){btns.forEach(function(b){b.addEventListener('click',function(){btns.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});figs().forEach(function(f){f.hidden=!(b.dataset.u==='all'||f.dataset.u===b.dataset.u)})})})}
  ufilter($$('#senChips button'),function(){return $$('#sgrid figure')});
  
  /* courses list */
  var C=[['Port70','คอร์สทำพอร์ตสำหรับน้อง DEK70'],['Project Express','ทำโปรเจกต์ให้เสร็จไวเพื่อยื่นพอร์ต'],['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ'],['Business Project','ทำโปรเจกต์ที่ต่อยอดเป็นธุรกิจ'],['Python Pro Pack','เรียนเขียนโปรแกรมด้วย Python'],['Hamstarter','คอร์สเริ่มต้นสำหรับคนที่ยังไม่มีผลงาน']];
  var CB=['','','','','',''],MO=['70','EXPRESS','NSC','฿','&gt;&gt;&gt; run()','START'];
  if($('#crows'))$('#crows').innerHTML=C.map(function(c,ci){var al=G.filter(function(x){return x[4]===c[0]}),us=al.map(function(x){return UN[x[2]]}).filter(function(v,k,a){return a.indexOf(v)===k});
    var im=al.slice(0,3).map(function(x,k){return '<img src="/Hamterco/img/dek69-'+x[0]+'.webp" alt="" loading="lazy" style="--k:'+(k-(Math.min(al.length,3)-1)/2)+'">'}).join('');
    return '<div class="cc"><div class="cc-m th'+ci+'"><i class="mo" aria-hidden="true">'+MO[ci]+'</i>'+im+'<span class="cc-st">รอบถัดไป</span></div><div class="cc-b"><b>'+c[0]+'</b><p>'+c[1]+'</p>'+(al.length?'<p class="al">รุ่นพี่ '+al.length+' คนจากคอร์สนี้ติด '+us.join(' ')+'</p>':'')+'<a href="'+LINE+'" target="_blank" rel="noopener">รับแจ้งเตือนรอบถัดไป</a></div></div>'}).join('');

  /* home: find (search + tabs + cards) */
  (function(){var G2=$('#zqG');if(!G2)return;var PX='https://www.hamsterhub.co/portex-site/index.html';
    var CRS=[['Port Express','คอร์สทำพอร์ตยื่นมหาลัย 2 เดือน สร้างเกมด้วย Unity','เริ่มเรียนแล้ว 9 พ.ย. 2569','5,990 บาท','/Hamterco/img/portex-poster.webp',PX,'พอร์ต มหาลัย ยื่น ม.6 dek69 dek70 เกม unity สัมภาษณ์ กรรมการ วิศวะ คอม'],
      ['Port70','คอร์สทำพอร์ตสำหรับน้อง DEK70','รอบถัดไป','','','','พอร์ต มหาลัย ม.5 dek70'],['Project Express','ทำโปรเจกต์ให้เสร็จไวเพื่อยื่นพอร์ต','รอบถัดไป','','','','พอร์ต โปรเจกต์ มหาลัย'],
      ['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ','รอบถัดไป','','','','แข่งขัน nsc ระดับประเทศ โปรเจกต์'],['Business Project','ทำโปรเจกต์ที่ต่อยอดเป็นธุรกิจ','รอบถัดไป','','','','ธุรกิจ สตาร์ทอัพ ขาย'],
      ['Python Pro Pack','เรียนเขียนโปรแกรมด้วย Python','รอบถัดไป','','','','python เขียนโปรแกรม โค้ด'],['Hamstarter','คอร์สเริ่มต้นสำหรับคนที่ยังไม่มีผลงาน','รอบถัดไป','','','','เริ่มต้น มือใหม่ ไม่เคย เกม']];
    var DIMG={'ค่าย':'photo-camp','เวิร์กชอป':'photo-class','แข่งขัน':'k-gamejam','โชว์ผลงาน':'s-showcase1','โครงการ':'photo-group'},
      AI2={'All for One University รอบชิงชนะเลิศ':'k-afo-logo','IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'};
    var IT=CRS.map(function(c){var g=G.filter(function(x){return x[4]===c[0]})[0];return {k:'course',t:c[0],d:c[1],st:c[2],pr:c[3],img:c[4]||(g?'/Hamterco/img/dek69-'+g[0]+'.webp':'/Hamterco/img/photo-class.webp'),url:c[5]||LINE,open:!!c[5],tags:c[6]}});
    ACT.forEach(function(a){IT.push({k:a[3],t:a[1],d:a[2],st:a[4]?'กำลังจะมา '+a[0]:'จบแล้ว '+a[0],pr:'',img:'/Hamterco/img/'+(AI2[a[1]]||DIMG[a[3]])+'.webp',url:a[4]?'https://www.hamsterhub.co/allforone':LINE,open:!!a[4],tags:a[3]+' '+a[2]})});
    var POP=['Port Express','All for One University รอบชิงชนะเลิศ','Hamstarter','AI Camp Season 2','GameJam X ปีที่ 5','Port70','Python Pro Pack','NSC Software Project 2026'];
    var SYN={'มหาลัย':'พอร์ต','มหาวิทยาลัย':'พอร์ต','tcas':'พอร์ต','portfolio':'พอร์ต','วิศวะ':'พอร์ต','คอม':'พอร์ต','สัมภาษณ์':'พอร์ต','game':'เกม','roblox':'เกม','unity':'เกม','เอไอ':'ai','โค้ด':'python','เขียนโปรแกรม':'python','แข่ง':'แข่งขัน','jam':'แข่งขัน','เว็บ':'web','web':'เว็บ'};
    function lab(x){return x.k==='course'?'คอร์สเรียน':'กิจกรรม: '+x.k}
    function cardH(x){var bell='<svg viewBox="0 0 24 24"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z M10 20a2 2 0 0 0 4 0" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/></svg>',arr='<svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      cal='<svg viewBox="0 0 24 24"><rect x="4" y="5.5" width="16" height="14" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',tag='<svg viewBox="0 0 24 24"><path d="M4 12.5V5h7.5l8.5 8.5-7.5 7.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="8.5" cy="9" r="1.4" fill="currentColor"/></svg>';
      var lab=x.k==='course'?'คอร์สเรียน':x.k;
      return '<a class="qv'+(x.open?' on':'')+'" href="'+x.url+'" target="_blank" rel="noopener" aria-label="'+x.t+'"><span class="qv-im"><img src="'+x.img+'" alt="" loading="lazy">'+(x.open?'<span class="qv-live">เปิดรับ</span>':'')+(['Port Express','Hamstarter','National Project'].indexOf(x.t)>-1?'<span class="qv-rc"><svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z\" fill=\"currentColor\"/></svg>แนะนำ</span>':'')+'</span><span class="qv-row"><span class="qv-tx"><b>'+x.t+'</b><span class="qv-d">'+x.d+'</span></span><span class="qv-btn" title="'+(x.open?'ดูรายละเอียด':'รับแจ้งเตือน')+'">'+(x.open?arr:bell)+'</span></span><span class="qv-meta"><span>'+cal+x.st+'</span><span>'+tag+(x.pr?'<em>'+x.pr+'</em>':lab)+'</span></span></a>'}
    function render(list,msg){$('#zqR').innerHTML=msg||'';G2.innerHTML=list.length?list.map(cardH).join(''):'<div class="zq-e"><b>ยังไม่เจอคำตอบตรงๆ สำหรับคำนี้</b><p>ลองพิมพ์แบบนี้ หรือบอกทีมว่าน้องอยากได้อะไร</p><p class="zq-e-q"><button type="button" data-q="อยากเข้าวิศวะคอม">อยากเข้าวิศวะคอม</button><button type="button" data-q="อยากทำเกมของตัวเอง">อยากทำเกมของตัวเอง</button><button type="button" data-q="เริ่มจากศูนย์ได้ไหม">เริ่มจากศูนย์ได้ไหม</button></p><a href="'+LINE+'" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div>'}
    function tab(t){$$('.zq-t button').forEach(function(b){b.setAttribute('aria-selected',String(b.dataset.t===t))});
      var L=t==='pop'?POP.map(function(n){return IT.filter(function(x){return x.t===n})[0]}).filter(Boolean):IT.filter(function(x){return x.k===t});render(L)}

    /* v63: answers by intent - what the kid typed, which course helps and why */
    var UNF={k:'สจล. (พระจอมเกล้าลาดกระบัง)',m:'มหิดล',c:'จุฬาฯ',u:'เกษตรศาสตร์'},UNN={k:24,m:9,c:8,u:7};
    var UN0=(typeof UN!=='undefined')?UN:{k:'สจล.',m:'มหิดล',c:'จุฬาฯ',u:'เกษตรศาสตร์'};
    function gf(f){return G.filter(f)}
    var INT=[
     {re:/สจล|ลาดกระบัง|kmitl|พระจอมเกล้า/,u:'k'},{re:/จุฬา|chula|(^|[^a-z])cu([^a-z]|$)/,u:'c'},{re:/มหิดล|mahidol/,u:'m'},{re:/เกษตร|kasetsart|(^|[^a-z])ku([^a-z]|$)/,u:'u'},
     {re:/แพทย์|หมอ|เภสัช|พยาบาล|ทันต|สัตวแพทย์|(^|[^a-z])med|กายภาพ|สาธารณสุข|เทคนิคการแพทย์/,h:'อยากเข้าแพทย์ หรือคณะสายสุขภาพ',
      a:'Hamster Hub สอนสายเทคโนโลยี เราไม่มีคอร์สติวสอบแพทย์ แต่ถ้าน้องอยากมีผลงานที่ไม่เหมือนใครในพอร์ต เช่น แอปหรืออุปกรณ์ที่ช่วยเรื่องสุขภาพ ทีมช่วยน้องสร้างได้',
      f:['ตัวอย่างผลงานจริง: StressStrike เกมที่เล่นด้วยการบีบอุปกรณ์วัดแรงมือ ชนะเลิศ OBEC Roboplayground'],pk:'ถ้าอยากมีผลงานเทคในพอร์ต',
      p:[['Project Express','มีไอเดียเรื่องสุขภาพแล้ว ทีมช่วยทำให้เสร็จทันยื่นพอร์ต'],['National Project','ทำโปรเจกต์ส่งเวทีระดับประเทศ ได้ทั้งผลงานและรางวัลใส่พอร์ต']],r:['อยากทำเว็บหรือแอป','Hamster Hub คืออะไร']},
     {re:/วิศว|วิดวะ|engineer|cedt|วิศวกรรม/,h:'อยากเข้าวิศวะคอมฯ หรือ CEDT',
      a:'พอร์ตสายนี้จะโดดเด่นมาก ถ้ามีผลงานที่น้องเขียนโปรแกรมเองทั้งชิ้น และเล่าได้ว่าทำยังไง คอร์สข้างล่างช่วยให้น้องมีผลงานแบบนั้น รุ่นพี่ 11 คนข้างล่างติดวิศวะคอมฯ หรือ CEDT แล้ว',
      p:[['Port Express','ม.6 ที่ยังไม่มีผลงาน: 2 เดือน น้องได้เกมที่เขียนโค้ดเองด้วย Unity (ภาษา C#) พร้อมแฟ้มพอร์ตยื่นรอบ Portfolio'],['Project Express','มีไอเดียแล้วแต่ทำไม่เสร็จ: ทีมช่วยทำให้เสร็จทันยื่น พี่จุ๊บกับน้องไอซ์จากคอร์สนี้ติด CEDT จุฬาฯ'],['National Project','อยากมีผลงานแข่งระดับประเทศในพอร์ต: น้องปิ่นโตจากคอร์สนี้ติดวิศวะคอมฯ มหิดล'],['Python Pro Pack','ยังไม่เคยเขียนโค้ด: เริ่มพื้นฐานที่นี่ น้องมิกจากคอร์สนี้ติดวิศวะคอมฯ มหิดล']],
      s:function(g){return /วิศว|CEDT/.test(g[3])},r:['อยากเข้าวิทย์คอม','ม.6 ยังไม่มีพอร์ต','ค่าเรียนเท่าไหร่']},
     {re:/วิทย์คอม|วิทยาการคอม|computer|(^|[^a-z])cs([^a-z]|$)|ไอที|(^|[^a-z])it([^a-z]|$)|(^|[^a-z])ict|สารสนเทศ|ดิจิทัล|คอมพิว|คอม/,h:'อยากเข้าวิทย์คอมฯ หรือไอที',
      a:'คณะสายนี้ดูว่าน้องเขียนโปรแกรมแก้ปัญหาได้จริงไหม ผลงานที่มีคนใช้หรือเคยส่งแข่งช่วยให้พอร์ตเด่นกว่าใบเกียรติบัตร รุ่นพี่ 5 คนข้างล่างติดวิทยาการคอมพิวเตอร์แล้ว',
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
      p:[['Port Express','รอบนี้เริ่มเรียนแล้ว 9 พ.ย. 2569 ทัก LINE จองรอบถัดไป']],r:['เรียนวันไหน','Hamster Hub คืออะไร']},
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
      a:'ผลงานของน้องต่อยอดเป็นธุรกิจได้จริง เช่น Mr. City เกมเดินเที่ยวสงขลาแบบ Pokémon GO ขายให้สวนสัตว์สงขลาแล้ว',
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
      return {h:'อยากเข้า'+UNF[u],a:'ปี 2569 รุ่นพี่ Hamster Hub ติด'+UN0[u]+' รอบ Portfolio แล้ว '+UNN[u]+' คน ข้างล่างคือบางส่วน พร้อมคอร์สที่เขาเรียน',
        p:cs.slice(0,4).map(function(c){var n=S.filter(function(g){return g[4]===c}).map(function(g){return g[1]});return [c,n.join(' ')+' เรียนคอร์สนี้ แล้วติด'+UN0[u]]}),s:function(g){return g[2]===u},r:['อยากเข้าวิศวะคอม','ม.6 ยังไม่มีพอร์ต']}}

    /* v65: search that forgives - aliases, prefix while typing, typos, wrong keyboard layout, filler words */
    var KW=[
     ['สจล','ลาดกระบัง','พระจอมเกล้าลาดกระบัง','พระจอมเกล้า','kmitl','ลาดกบัง','ไอทีลาดกระบัง'],
     ['จุฬา','จุฬาฯ','จุฬาลงกรณ์','chula','chulalongkorn','cu'],
     ['มหิดล','mahidol','mu'],
     ['เกษตร','เกษตรศาสตร์','เกษตรศรีราชา','ศรีราชา','kasetsart','ku'],
     ['แพทย์','แพทย','แพท','แพด','หมอ','เภสัช','เภสัชศาสตร์','พยาบาล','ทันตะ','ทันตแพทย์','สัตวแพทย์','med','medicine','doctor','กายภาพ','สาธารณสุข','เทคนิคการแพทย์','สายสุขภาพ','สายหมอ'],
     ['วิศวะ','วิศวกรรม','วิศวกรรมศาสตร์','วิศวกร','วิศวะคอม','วิศวะคอมพิวเตอร์','วิศวกรรมคอมพิวเตอร์','วิดวะ','วิสวะ','วิศะ','วิศว','วิดสะวะ','engineer','engineering','eng','cedt','คอมเอ็น','comeng','wisawa','witsawa','visawa','wishawa'],
     ['วิทย์คอม','วิทยาการคอมพิวเตอร์','วิทยาการคอม','computerscience','compsci','cs','ไอที','it','ict','เทคโนโลยีสารสนเทศ','สารสนเทศ','คอม','คอมพิวเตอร์','computer','ดิจิทัล','datascience','software','ซอฟต์แวร์','ซอฟแวร์'],
     ['วิทยาศาสตร์','วิทย์','สถิติ','สิ่งแวดล้อม','ฟิสิกส์','เคมี','ชีวะ','ชีววิทยา','คณิต','คณิตศาสตร์','science','ข้อมูล','data'],
     ['hamsterhub','hamster','แฮมสเตอร์ฮับ','แฮมสเตอร์','แฮมเตอร์','แฮมสเตอ','แฮม','ฮับ','คืออะไร','ที่นี่','เกี่ยวกับ','เป็นใคร','ทำอะไร','บริษัท','สถาบัน','น่าเชื่อถือ','รีวิว','about'],
     ['ราคา','เท่าไหร่','เท่าไร','เท่าไห่','กี่บาท','ค่าเรียน','ค่าคอร์ส','บาท','แพง','ผ่อน','ส่วนลด','price','cost'],
     ['วันไหน','กี่โมง','ตารางเรียน','ตาราง','ออนไลน์','online','onsite','ที่ไหน','เรียนที่ไหน','เรียนยังไง','เวลาเรียน','เปิดเมื่อไหร่','สมัคร','สมัครยังไง','เริ่มเรียน','กี่วัน','register','schedule'],
     ['ผู้ปกครอง','ลูก','ลูกชาย','ลูกสาว','พ่อแม่','คุณแม่','คุณพ่อ','ผปค','parent'],
     ['ม6','ม.6','มหก','dek70','เด็ก70','เด็กหกสิบ','ปีสุดท้าย','grade12','มัธยม6'],
     ['ม4','ม5','ม.4','ม.5','dek71','dek72','มัธยม4','มัธยม5'],
     ['ม1','ม2','ม3','ม.1','ม.2','ม.3','มต้น','ม.ต้น','ประถม','ป6','ป5','ป.6'],
     ['มือใหม่','ไม่เคย','ไม่เก่ง','ไม่มีพื้นฐาน','เริ่มจากศูนย์','ศูนย์','เริ่มต้น','python','ไพธอน','ไพทอน','ไพตอน','โค้ด','โค้ดดิ้ง','เขียนโค้ด','เขียนโปรแกรม','โปรแกรมมิ่ง','โปรแกรม','programming','coding','code','beginner'],
     ['เกม','เกมส์','game','games','unity','ยูนิตี้','ยูนิตี','roblox','โรบล็อกซ์','โรบอก','godot','ทำเกม','สร้างเกม','gamedev','นักพัฒนาเกม'],
     ['เว็บ','เวป','เว็ป','เวบ','web','website','เว็บไซต์','แอป','แอพ','แอบ','app','application','แอปพลิเคชัน','frontend','react'],
     ['iot','ไอโอที','หุ่นยนต์','หุ่นยน','robot','robotic','arduino','อาดูโน่','อาดุยโน่','esp32','บอร์ด','อุปกรณ์','เซนเซอร์','เซ็นเซอร์','sensor','ไฟฟ้า','อิเล็กทรอนิกส์','embedded'],
     ['ai','เอไอ','chatgpt','gpt','แชทจีพีที','ปัญญาประดิษฐ์','machinelearning','ml','gemini','claude'],
     ['ธุรกิจ','สตาร์ทอัพ','สตาร์ตอัป','สตาทอัพ','startup','ขายของ','ขาย','หาเงิน','business','บริหาร','การตลาด','ผู้ประกอบการ','บัญชี'],
     ['แข่ง','แข่งขัน','nsc','รางวัล','ประกวด','gamejam','เกมแจม','jam','โอลิมปิก','เวที','hackathon','แฮกกาธอน','แฮคกาตอน'],
     ['ค่าย','camp','แคมป์','ปิดเทอม','เวิร์กชอป','เวิร์คช็อป','workshop','กิจกรรม','อีเวนต์','event'],
     ['พอร์ต','พอต','พอท','portfolio','port','พอร์ตโฟลิโอ','มหาลัย','มหาวิทยาลัย','มหาลัยดังๆ','tcas','ทีแคส','ยื่น','สัมภาษณ์','แฟ้ม','รอบ1','รอบพอร์ต','ติดมหาลัย','เข้ามหาลัย','uni','university']];
    var NAME=['สจล.','จุฬาฯ','มหิดล','เกษตรศาสตร์','แพทย์ / สายสุขภาพ','วิศวะคอมฯ / CEDT','วิทย์คอมฯ / ไอที','สายวิทยาศาสตร์','Hamster Hub คืออะไร','ค่าเรียน','เรียนเมื่อไหร่ / สมัคร','ผู้ปกครอง','น้อง ม.6','น้อง ม.4–5','น้อง ม.ต้น','เริ่มจากศูนย์','ทำเกม','ทำเว็บ / แอป','IoT / หุ่นยนต์','AI','ธุรกิจ / สตาร์ทอัพ','ส่งผลงานแข่ง','ค่ายและกิจกรรม','พอร์ตยื่นมหาลัย'];
    var EN="`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?",
        TH="_ๅ/-ภถุึคตจขชๆไำพะัีรนยบลฃฟหกดเ้่าสวงผปแอิืทมใฝ%+๑๒๓๔ู฿๕๖๗๘๙๐\"ฎฑธํ๊ณฯญฐ,ฅฤฆฏโฌ็๋ษศซ.()ฉฮฺ์?ฒฬฦ";
    function swapKb(t,toTh){var a=toTh?EN:TH,b=toTh?TH:EN,o='';for(var i=0;i<t.length;i++){var k=a.indexOf(t[i]);o+=k>-1?b[k]:t[i]}return o}
    function norm(t){return t.toLowerCase().replace(/[\s​"'“”‘’!?.,()\-_/]+/g,'').replace(/ๆ/g,'')}
    function strip(t){var o=t.replace(/^(อยาก(จะ)?(เข้า|เรียน|ทำ|ได้|เป็น|รู้|ติด|มี|ลอง)?|อยาก|ต้องการ|หา|เข้า|เรียน|คณะ|สาย|ขอ)+/,'').replace(/(ครับ|คับ|ค่ะ|คะ|จ้า|จ้ะ|นะ|หน่อย|ได้ไหม|ได้มั้ย|ไหม|มั้ย|มั๊ย|บ้าง)+$/,'');return o.length>=1?o:t}
    function lev(a,b){if(a===b)return 0;var m=a.length,n=b.length;if(!m)return n;if(!n)return m;var d=[],i,j;for(i=0;i<=m;i++){d[i]=[i];}for(j=0;j<=n;j++)d[0][j]=j;
      for(i=1;i<=m;i++)for(j=1;j<=n;j++){var c=a[i-1]===b[j-1]?0:1;d[i][j]=Math.min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+c);if(i>1&&j>1&&a[i-1]===b[j-2]&&a[i-2]===b[j-1])d[i][j]=Math.min(d[i][j],d[i-2][j-2]+1)}return d[m][n]}
    function score1(q,a){var L=q.length;if(!L)return 0;var short=/^[a-z0-9]{1,2}$/.test(a);
      if(q===a)return 100+a.length;
      if(short){return new RegExp('(^|[^a-z])'+a+'([^a-z]|$)').test(q)?70:0}
      if(a.length>=2&&q.indexOf(a)>-1)return 60+a.length*3;
      if(L>=2&&a.indexOf(q)===0)return 48+L*3-(a.length-L)*.4;
      if(L>=3){var tol=L>=7?2:1,d=Math.min(lev(q,a),lev(q,a.slice(0,L)));if(d<=tol)return 40+L*2-d*8}
      return 0}
    function scoreAll(q){var toks=[q];if(window.Intl&&Intl.Segmenter){var sg=new Intl.Segmenter('th',{granularity:'word'});var ts=Array.from(sg.segment(q),function(x){return x.segment}).filter(function(x){return x.length>=2});
        for(var i=0;i<ts.length;i++){toks.push(ts[i]);if(ts[i+1])toks.push(ts[i]+ts[i+1])}}
      return KW.map(function(list,i){var b=0;list.forEach(function(a){a=norm(a);toks.forEach(function(t){var v=score1(t,a)*(t===q?1:.92);if(v>b)b=v})});return {i:i,s:b}}).sort(function(x,y){return y.s-x.s})}
    function intent2(raw){var n=norm(raw),cands=[[strip(n),''],[n,'']];
      if(/[a-z;\[\]',.\/]/.test(n)&&!/[ก-๙]/.test(n)){var th=norm(swapKb(raw.replace(/\s+/g,''),true));cands.push([strip(th),th])}
      if(/[ก-๙]/.test(n)&&!/[a-z]/.test(n)){var en=norm(swapKb(raw.replace(/\s+/g,''),false));cands.push([en,en])}
      var best=null;cands.forEach(function(c,ci){if(!c[0])return;var r=scoreAll(c[0]);var pen=ci>=2?.9:1;if(!best||r[0].s*pen>best.r[0].s*best.pen)best={r:r,pen:pen,via:c[1]}});
      if(!best||best.r[0].s<34)return null;var top=best.r[0],I=INT[top.i];I=I.u?uniI(I.u):I;
      var alts=best.r.slice(1).filter(function(x){return x.s>=34&&x.s>=top.s*.8}).slice(0,3).map(function(x){return x.i});
      var shown=n.length<=3||top.s<60;return {I:I,alts:alts,via:best.via,partial:shown}}
    function intent(q){var t=q.toLowerCase();for(var i=0;i<INT.length;i++){if(INT[i].re.test(t))return INT[i].u?uniI(INT[i].u):INT[i]}return null}
    function pickH(p){var x=IT.filter(function(y){return y.t===p[0]})[0];if(!x)return '';
      var st=x.open?(x.pr?'เปิดรับแล้ว ค่าเรียน '+x.pr:'เปิดรับแล้ว'):(x.k==='course'?'รอบถัดไป กดรับแจ้งเตือนได้':x.st);
      return '<li><a class="ia-c'+(x.open?' on':'')+'" href="'+x.url+'" target="_blank" rel="noopener"><img src="'+x.img+'" alt="" loading="lazy"><span class="ia-b"><b>'+esc(x.t)+'</b><em>'+p[1]+'</em><small>'+st+'</small></span><i class="ia-go">'+(x.open?'ดูรายละเอียด':(x.k==='course'?'รับแจ้งเตือน':'ดูกิจกรรม'))+'</i></a></li>'}
    function snH(g){return '<figure class="ia-sn"><span class="ia-av"><img src="/Hamterco/img/dek69-'+g[0]+'.webp" alt="" loading="lazy"></span><figcaption><b>'+g[1]+'</b><span>'+g[3]+' '+UN0[g[2]]+'</span><small>คอร์ส '+g[4]+'</small></figcaption></figure>'}
    function ansH(I,q){var h='<div class="ia"><p class="ia-q">คำตอบสำหรับ “'+esc(q)+'”</p><h3>'+I.h+'</h3><p class="ia-a">'+I.a+'</p>';
      if(I.f)h+='<ul class="ia-f">'+I.f.map(function(f){return '<li>'+f+'</li>'}).join('')+'</ul>';
      if(I.p&&I.p.length)h+='<p class="ia-k">'+(I.pk||'คอร์สและกิจกรรมที่ช่วยได้')+'</p><ol class="ia-p">'+I.p.map(pickH).join('')+'</ol>';
      if(I.s){var S=gf(I.s);if(S.length>8)S=S.filter(function(g,i){return i%2===0}).concat(S.filter(function(g,i){return i%2})).slice(0,8);if(S.length)h+='<p class="ia-k">รุ่นพี่ที่ไปทางนี้แล้ว</p><div class="ia-s">'+S.map(snH).join('')+'</div>'}
      h+='<div class="ia-x">'+(I.r?'<span>ถามต่อ</span>'+I.r.map(function(r){return '<button type="button" data-q="'+r+'">'+r+'</button>'}).join(''):'')+(I.lk?'<a class="ia-lk" href="'+I.lk[0]+'">'+I.lk[1]+'</a>':'')+'<a class="ia-line" href="'+LINE+'" target="_blank" rel="noopener">ทัก LINE ถามทีม</a></div></div>';return h}
    function search(q){q=(q||'').trim();var R=$('#zqRes'),A=$('#zqA');if(!q){R.hidden=true;return}var nq0=norm(q),TL=nq0.length>=5?IT.filter(function(x){var t=norm(x.t);return t.indexOf(nq0)===0||nq0.indexOf(t)>-1}):[];if(TL.length){A.hidden=true;A.innerHTML='';R.hidden=false;render(TL,'ผลลัพธ์สำหรับ “'+esc(q)+'”');return}var M=intent2(q);
      if(M){var I=M.I;R.hidden=false;$('#zqR').textContent='';G2.innerHTML='';var pre='';if(M.via)pre+='<p class="ia-fix">น้องอาจลืมเปลี่ยนภาษาแป้นพิมพ์ แสดงคำตอบสำหรับ “<b>'+esc(M.via)+'</b>”</p>';if(M.alts.length)pre+='<p class="ia-alt"><span>หรือน้องหมายถึง</span>'+M.alts.map(function(i){return '<button type="button" data-q="'+esc(KW[i][0])+'">'+NAME[i]+'</button>'}).join('')+'</p>';A.innerHTML=pre+ansH(I,M.via||q);A.hidden=false;R.scrollTop=0;return}var nq=norm(q),P=[];if(nq.length<=2)KW.forEach(function(l,i){if(l.some(function(a){return norm(a).indexOf(nq)===0}))P.push(i)});if(P.length){R.hidden=false;$('#zqR').textContent='';G2.innerHTML='';A.innerHTML='<div class="ia"><p class="ia-q">น้องพิมพ์ “'+esc(q)+'”</p><h3>น้องหมายถึงเรื่องไหน</h3><p class="ia-alt ia-pick">'+P.slice(0,8).map(function(i){return '<button type="button" data-q="'+esc(KW[i][0])+'">'+NAME[i]+'</button>'}).join('')+'</p></div>';A.hidden=false;return}
      A.hidden=true;A.innerHTML='';search0(q)}
    function search0(q){q=(q||'').trim();var R=$('#zqRes');if(!q){R.hidden=true;return}R.hidden=false;var toks=q.toLowerCase().split(/\s+/),k=[];toks.forEach(function(w){k.push(w);Object.keys(SYN).forEach(function(s2){if(w.indexOf(s2)>-1)k.push(SYN[s2])})});
      var L=IT.filter(function(x){var h=(x.t+' '+x.d+' '+x.tags+' '+x.k).toLowerCase();return k.some(function(w){return w.length>1&&h.indexOf(w)>-1})});
      L.sort(function(a,b){return (b.open?2:0)+(b.k==='course'?1:0)-((a.open?2:0)+(a.k==='course'?1:0))});
      $$('.zq-t button').forEach(function(b){b.setAttribute('aria-selected','false')});render(L,'ผลลัพธ์สำหรับ “'+q.replace(/[<>&]/g,'')+'” '+L.length+' รายการ')}
    $$('.zq-t button').forEach(function(b){b.addEventListener('click',function(){$('#zqIn').value='';tab(b.dataset.t)})});
    $('#zqForm').addEventListener('submit',function(e){e.preventDefault();search($('#zqIn').value)});
    var dt;$('#zqIn').addEventListener('input',function(){clearTimeout(dt);dt=setTimeout(function(){search($('#zqIn').value)},250)});
    document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-q]');if(!b)return;e.preventDefault();$('#zqIn').value=b.dataset.q;search(b.dataset.q);});
    $('#zqC').innerHTML=IT.filter(function(x){return x.k==='course'}).map(cardH).join('');if($('#zqC2'))$('#zqC2').innerHTML=$('#zqC').innerHTML;
    $('#zqN').innerHTML=IT.filter(function(x){return x.k!=='course'}).slice(1,5).map(cardH).join('');
    var W2=['ยื่นพอร์ตเข้ามหาลัย','เข้าวิศวะคอม','สร้างเกมของตัวเอง','ทำแอปของตัวเอง','ติด CEDT จุฬาฯ','สร้างสตาร์ทอัพ','เขียนโปรแกรมเป็น','ทำเว็บของตัวเอง'],wi=0,ci=W2[0].length,del=true,el=$('#zqType');
    if(!matchMedia('(prefers-reduced-motion:reduce)').matches)(function ty(){var zz=document.querySelector('[data-view="home"] .zq');if(zz&&(zz.classList.contains('ask')||document.activeElement===document.getElementById('zqIn'))){if(ci!==W2[wi].length){ci=W2[wi].length;del=true;el.textContent=W2[wi]}setTimeout(ty,600);return}var w=W2[wi];if(del){ci--;if(ci<=0){del=false;wi=(wi+1)%W2.length}}else{ci++;if(ci>=W2[wi].length){del=true;el.textContent=W2[wi];setTimeout(ty,2200);return}}el.textContent=W2[wi].slice(0,Math.max(ci,0));setTimeout(ty,del?40:85)})();
  })();

  /* search: loading dots while matching */
  (function(){var f=$('#zqForm');if(!f)return;var btn=f.querySelector('button'),t0=btn.textContent;f.addEventListener('submit',function(){btn.classList.add('ld');btn.innerHTML='<i></i><i></i><i></i>';setTimeout(function(){btn.classList.remove('ld');btn.textContent=t0},520)})})();

  /* who-we-are: words light up as you scroll */
  (function(){var p=$('#zaSay');if(!p)return;var ws=p.textContent.split(' ');p.innerHTML=ws.map(function(w){return '<span>'+w+'</span>'}).join(' ');var S=p.querySelectorAll('span');
    function up(){var r=p.getBoundingClientRect(),h=innerHeight,t=Math.min(1,Math.max(0,(h*.85-r.top)/(h*.6)));var n=Math.round(t*S.length);S.forEach(function(x,i){x.classList.toggle('lit',i<n)})}
    addEventListener('scroll',up,{passive:true});up()})();
  /* tilt + light on cards (pointer only) */
  (function(){if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
    document.querySelectorAll('.za-c,.za-t').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
      c.style.transform='perspective(900px) rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) translateY(-4px)';c.style.setProperty('--lx',(x+.5)*100+'%');c.style.setProperty('--ly',(y+.5)*100+'%')});
      c.addEventListener('pointerleave',function(){c.style.transform=''})})})();
  /* hero: the floating games follow the mouse at different depths */
  (function(){var z=$('.zq');if(!z||!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var I=z.querySelectorAll('.zq-dc img'),D=[1.2,.6,1,1.1,.7,.9,1.4],tx=0,ty=0,cx=0,cy=0,run=false;
    z.addEventListener('pointermove',function(e){tx=e.clientX/innerWidth-.5;ty=e.clientY/innerHeight-.5;if(!run){run=true;requestAnimationFrame(loop)}});
    function loop(){cx+=(tx-cx)*.08;cy+=(ty-cy)*.08;I.forEach(function(im,i){im.style.transform='translate('+(-cx*40*D[i])+'px,'+(-cy*30*D[i])+'px)'});if(Math.abs(tx-cx)>.001||Math.abs(ty-cy)>.001)requestAnimationFrame(loop);else run=false}})();

  
  /* search hamster: 15 fps sprite (0 straight, 1 left, 2 right, 3 blink) */
  (function(){var h=$('#zqHam'),sp=$('#zqSpr'),f=$('#zqForm'),inp=$('#zqIn');if(!h||!sp)return;setTimeout(function(){h.classList.add('up')},600);
    var T=[],add=function(fr,n){for(var i=0;i<n;i++)T.push(fr)};add(0,30);add(3,2);add(0,8);add(1,14);add(0,6);add(2,14);add(0,24);add(3,2);add(0,3);add(3,2);add(0,12);
    var t=0,mode='idle',ov=-1;function draw(fr){sp.style.backgroundPosition=(fr*100/3)+'% 0'}
    setInterval(function(){if(document.hidden)return;var fr=T[t%T.length];t++;if(ov>=0&&fr!==3)fr=ov;draw(fr)},1000/15);
    f.addEventListener('pointerenter',function(){h.classList.add('watch')});f.addEventListener('pointerleave',function(){if(document.activeElement!==inp){h.classList.remove('watch');ov=-1}});
    inp.addEventListener('focus',function(){h.classList.add('watch');ov=0});inp.addEventListener('blur',function(){h.classList.remove('watch');ov=-1});
    inp.addEventListener('input',function(){ov=inp.value.length%2?1:2;h.classList.remove('nod');void h.offsetWidth;h.classList.add('nod')});
    function dive(){h.classList.remove('dive');void h.offsetWidth;h.classList.add('dive');setTimeout(function(){h.classList.remove('dive')},1100)}
    f.addEventListener('submit',dive);document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('.zq-pop [data-q]'))dive()})})();
  /* headline: every phrase gets its own type style; click to switch */
  (function(){var el=$('#zqType');if(!el)return;var h=el.closest('.zq-h'),S=['kanit','persona','got','ragnarok','elden','pencil','pencil2b','pen','cartoon','doraemon','robot','ai','glitch','hacker','curtain','computer','fan'],k=0,last=el.textContent;h.dataset.f=S[0];
    function next(){k=(k+1)%S.length;h.dataset.f=S[k];h.classList.remove('sw');void h.offsetWidth;h.classList.add('sw')}
    new MutationObserver(function(){var t=el.textContent;if(t.length<=1&&last.length>1)next();last=t}).observe(el,{childList:true,characterData:true,subtree:true});
    h.addEventListener('click',next)})();
  /* scroll cue: nudges if nobody scrolls */
  (function(){var b=$('#zqMore');if(!b)return;b.addEventListener('click',function(){var n=$('.nw2');if(n)n.scrollIntoView({behavior:'smooth'})});
    var iv=setInterval(function(){if(scrollY>40||!document.querySelector('[data-view="home"].on')){b.classList.remove('nudge');return}b.classList.remove('nudge');void b.offsetWidth;b.classList.add('nudge')},3200);
    addEventListener('scroll',function(){b.classList.toggle('gone',scrollY>80)},{passive:true})})();
  /* rails */
  document.querySelectorAll('.mr').forEach(function(m){var r=m.querySelector('.mr-r');if(!r)return;function st(d){var c=r.querySelector('.qv');r.scrollBy({left:d*((c?c.offsetWidth:300)+18),behavior:'smooth'})}
    m.querySelector('.mr-p').addEventListener('click',function(){st(-1)});m.querySelector('.mr-n').addEventListener('click',function(){st(1)})});

  /* hero objects follow the mouse */
  (function(){var z=$('.zq');if(!z||!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var I=z.querySelectorAll('.zq-ob img'),D=[1.2,.7,1.4,.9,1.1,.6],tx=0,ty=0,cx=0,cy=0,run=false;
    z.addEventListener('pointermove',function(e){tx=e.clientX/innerWidth-.5;ty=e.clientY/innerHeight-.5;if(!run){run=true;requestAnimationFrame(loop)}});
    function loop(){cx+=(tx-cx)*.07;cy+=(ty-cy)*.07;I.forEach(function(im,i){im.style.translate=(-cx*46*D[i])+'px '+(-cy*34*D[i])+'px'});if(Math.abs(tx-cx)>.001||Math.abs(ty-cy)>.001)requestAnimationFrame(loop);else run=false}})();

  /* search: suggestions on focus, staggered results on submit */
  (function(){var f=$('#zqForm'),inp=$('#zqIn'),sg=$('#zqSug'),h=$('#zqHam');if(!f||!sg)return;
    function open(){if(!inp.value)sg.hidden=false}function close(){sg.hidden=true}
    inp.addEventListener('focus',open);inp.addEventListener('input',function(){sg.hidden=!!inp.value});
    document.addEventListener('pointerdown',function(e){if(!e.target.closest('.zq-sw'))close()});
    sg.addEventListener('click',function(e){var b=e.target.closest('[data-q]');if(b)close()});
    function stagger(){$$('#zqG .qv').forEach(function(c,i){c.style.animationDelay=(i*70)+'ms';c.classList.remove('in');void c.offsetWidth;c.classList.add('in')})}
    f.addEventListener('submit',function(){close();inp.blur();f.classList.remove('go');void f.offsetWidth;f.classList.add('go');setTimeout(function(){stagger()},380)});
    document.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('[data-q]')&&e.target.closest('.zq')){f.classList.remove('go');void f.offsetWidth;f.classList.add('go');setTimeout(stagger,380)}})})();

  /* login button: light follows the cursor, burst on press */
  (function(){var b=$('.login');if(!b)return;b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.setProperty('--mx',(e.clientX-r.left)+'px');b.style.setProperty('--my',(e.clientY-r.top)+'px')});
    b.addEventListener('pointerdown',function(e){var r=b.getBoundingClientRect(),i=document.createElement('i');i.className='lg-burst';i.style.left=(e.clientX-r.left)+'px';i.style.top=(e.clientY-r.top)+'px';b.appendChild(i);setTimeout(function(){i.remove()},700)})})();
  /* rails: arrows at the screen edges, centred on the cards */
  (function(){document.querySelectorAll('.mr').forEach(function(m){var r=m.querySelector('.mr-r'),ar=m.querySelector('.mr-ar');if(!r||!ar)return;var w=document.createElement('div');w.className='mr-rw';r.parentNode.insertBefore(w,r);w.appendChild(r);w.appendChild(ar);
})})();

  /* rails: page dots */
  (function(){document.querySelectorAll('.mr-r').forEach(function(r){var d=document.createElement('div');d.className='ak-dots';(r.closest('.mr-rw')||r).after(d);
      function build(){var n=r.querySelectorAll('.qv').length;if(d.childElementCount!==n){d.innerHTML='';for(var i=0;i<n;i++){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','การ์ดที่ '+(i+1));(function(i){b.addEventListener('click',function(){var c=r.querySelectorAll('.qv')[i];r.scrollTo({left:c.offsetLeft-r.offsetLeft,behavior:'smooth'})})})(i);d.appendChild(b)}}upd()}
      function upd(){var cs=r.querySelectorAll('.qv'),a=0,best=1e9;cs.forEach(function(c,i){var x=Math.abs(c.offsetLeft-r.offsetLeft-r.scrollLeft);if(x<best){best=x;a=i}});[].forEach.call(d.children,function(b,i){b.classList.toggle('on',i===a)})}
      r.addEventListener('scroll',function(){requestAnimationFrame(upd)},{passive:true});new MutationObserver(build).observe(r,{childList:true});build()})})();
  /* search focus: the sky glow pulls in around the bar */
  (function(){var sw=$('.zq-sw'),inp=$('#zqIn');if(!sw)return;inp.addEventListener('focus',function(){sw.classList.remove('lit');void sw.offsetWidth;sw.classList.add('lit')});inp.addEventListener('blur',function(){sw.classList.remove('lit')})})();

  /* hamster eyes look at the cursor in any direction; blink; act on search */
  (function(){var h=$('#zqHam');if(!h)return;var E=h.querySelectorAll('.ze b');
    document.addEventListener('pointermove',function(e){var r=h.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height*.46,dx=e.clientX-cx,dy=e.clientY-cy,d=Math.hypot(dx,dy)||1,k=Math.min(1,d/260);
      E.forEach(function(b){b.style.transform='translate('+(dx/d*k*38).toFixed(1)+'%,'+(dy/d*k*38).toFixed(1)+'%)'})});
    var f=$('#zqForm');function act(){h.classList.remove('act');void h.offsetWidth;h.classList.add('act');setTimeout(function(){h.classList.remove('act')},1500)}
    })();
  /* hero play: click the empty sky for confetti */
  (function(){var z=$('.zq');if(!z)return;var C=['#1C74D9','#4DA3F0','#B3D8FF','#0D2E63','#fff','#7FC0FF'];
    z.addEventListener('click',function(e){if(e.target.closest('a,button,input,form,.zq-h,.zq-sug'))return;if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;
      for(var i=0;i<16;i++){var p=document.createElement('i');p.className='zq-cf';var a=Math.random()*6.283,v=60+Math.random()*120;p.style.left=e.clientX+'px';p.style.top=e.clientY+'px';p.style.background=C[i%C.length];
        p.style.setProperty('--x',(Math.cos(a)*v).toFixed(0)+'px');p.style.setProperty('--y',(Math.sin(a)*v-60).toFixed(0)+'px');p.style.setProperty('--r',(Math.random()*720-360).toFixed(0)+'deg');document.body.appendChild(p);setTimeout(function(q){return function(){q.remove()}}(p),1100)}})})();
  /* search button: magnetic + sparks */
  (function(){var b=$('.zq-go');if(!b)return;
    if(matchMedia('(hover:hover)').matches){b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.translate=((e.clientX-r.left-r.width/2)*.18)+'px '+((e.clientY-r.top-r.height/2)*.25)+'px';b.style.setProperty('--gx',(e.clientX-r.left)+'px')});b.addEventListener('pointerleave',function(){b.style.translate=''})}
    b.addEventListener('click',function(){for(var i=0;i<8;i++){var s=document.createElement('i');s.className='zq-sp';s.style.setProperty('--a',(i*45)+'deg');b.appendChild(s);setTimeout(function(q){return function(){q.remove()}}(s),600)}})})();
  /* login: light follows the cursor */
  (function(){var b=$('.login');if(!b)return;b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.setProperty('--mx',(e.clientX-r.left)+'px')})})();

  /* hamster turns its whole head toward the cursor */
  (function(){var h=$('#zqHam'),hb=h&&h.querySelector('.zq-hb');if(!hb||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var tx=0,ty=0,cx=0,cy=0,run=false;
    document.addEventListener('pointermove',function(e){var r=h.getBoundingClientRect(),dx=e.clientX-(r.left+r.width/2),dy=e.clientY-(r.top+r.height*.45),d=Math.hypot(dx,dy)||1,k=Math.min(1,d/320);tx=dx/d*k;ty=dy/d*k;if(!run){run=true;requestAnimationFrame(loop)}});
    function loop(){cx+=(tx-cx)*.12;cy+=(ty-cy)*.12;hb.style.transform='translate('+(cx*5).toFixed(2)+'px,'+(cy*3).toFixed(2)+'px) rotate('+(cx*9).toFixed(2)+'deg) rotateY('+(cx*26).toFixed(2)+'deg) rotateX('+(-cy*22).toFixed(2)+'deg)';
      if(Math.abs(tx-cx)>.002||Math.abs(ty-cy)>.002)requestAnimationFrame(loop);else run=false}})();
  /* focus: the sky gathers into the search bar */
  (function(){var z=$('.zq'),inp=$('#zqIn'),sw=$('.zq-sw');if(!z||!inp)return;
    function place(){var r=sw.getBoundingClientRect(),zr=z.getBoundingClientRect();z.style.setProperty('--fx',(r.left+r.width/2-zr.left)+'px');z.style.setProperty('--fy',(r.top+r.height/2-zr.top)+'px')}
    inp.addEventListener('focus',function(){place();z.classList.add('fx')});inp.addEventListener('blur',function(){z.classList.remove('fx')})})();
  /* site-wide feel: scroll progress, back to top, ripple on buttons */
  (function(){var bar=document.createElement('i');bar.className='sp-bar';document.body.appendChild(bar);
    var top=document.createElement('button');top.type='button';top.className='to-top';top.setAttribute('aria-label','กลับขึ้นด้านบน');top.innerHTML='<svg viewBox="0 0 24 24"><path d="M12 19V6M6 11l6-6 6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>';document.body.appendChild(top);
    top.addEventListener('click',function(){scrollTo({top:0,behavior:'smooth'})});
    function u(){var m=document.documentElement.scrollHeight-innerHeight;bar.style.transform='scaleX('+(m>0?scrollY/m:0)+')';top.classList.toggle('on',scrollY>innerHeight*1.2)}
    addEventListener('scroll',u,{passive:true});addEventListener('hashchange',function(){setTimeout(u,60)});u();
    document.addEventListener('pointerdown',function(e){var b=e.target.closest&&e.target.closest('button,.mr-btn,.lbtn,.qv-btn,.zp-c i,.fit button,.btn');if(!b||b.classList.contains('vg-c'))return;var r=b.getBoundingClientRect(),d=Math.max(r.width,r.height)*2,i=document.createElement('i');i.className='rp';i.style.width=i.style.height=d+'px';i.style.left=(e.clientX-r.left-d/2)+'px';i.style.top=(e.clientY-r.top-d/2)+'px';
      if(getComputedStyle(b).position==='static')b.style.position='relative';b.style.overflow=b.style.overflow||'hidden';b.appendChild(i);setTimeout(function(){i.remove()},600)})})();
  /* nav: sliding indicator under the current page */
  (function(){var nav=$('.nav-in');if(!nav)return;var ind=document.createElement('i');ind.className='nv-ind';nav.appendChild(ind);
    function go(){var a=nav.querySelector('a.v[aria-current="page"]');if(!a){ind.style.opacity=0;return}var r=a.getBoundingClientRect(),n=nav.getBoundingClientRect();ind.style.opacity=1;ind.style.width=(r.width-16)+'px';ind.style.transform='translateX('+(r.left-n.left+8)+'px)'}
    addEventListener('hashchange',function(){setTimeout(go,80);setTimeout(go,1300)});addEventListener('resize',go);setTimeout(go,300)})();

  /* search results open in a panel under the bar, no page jump */
  (function(){var sw=$('.zq-sw'),r=$('#zqRes');if(!sw||!r)return;sw.appendChild(r);
    var x=document.createElement('button');x.type='button';x.className='zq-x';x.setAttribute('aria-label','ปิดผลค้นหา');x.innerHTML='&times;';r.prepend(x);
    x.addEventListener('click',function(){r.hidden=true});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')r.hidden=true});
    document.addEventListener('pointerdown',function(e){if(!e.target.closest('.zq-sw')&&!e.target.closest('.zq-pop'))r.hidden=true})})();
  /* sky gathers into the bar as a soft orb (no hard edges) */
  (function(){var z=$('.zq'),sw=$('.zq-sw');if(!z||!sw)return;var o=document.createElement('i');o.className='zq-orb';o.setAttribute('aria-hidden','true');sw.prepend(o)})();
  /* login: the light follows the cursor */
  (function(){var b=$('.login');if(!b)return;b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.setProperty('--ox',((e.clientX-r.left)/r.width*100)+'%')});b.addEventListener('pointerleave',function(){b.style.removeProperty('--ox')})})();
  /* activity deck */
  (function(){var st=$('#dqSt');if(!st)return;var AI3={'All for One University รอบชิงชนะเลิศ':'k-afo','IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'},
      D={'ค่าย':'photo-camp','เวิร์กชอป':'photo-class','แข่งขัน':'k-gamejam','โชว์ผลงาน':'s-showcase1','โครงการ':'photo-group'};
    var L=ACT.slice(0,7).map(function(a){var p=a[0].split(' ');return {d:p[0],m:p[1]||'',t:a[1],x:a[2],k:a[3],up:!!a[4],img:'/Hamterco/img/'+(AI3[a[1]]||D[a[3]])+'.webp'}});
    st.innerHTML=L.map(function(c,i){return '<button type="button" class="dq-c" data-i="'+i+'"><span class="dq-chip">'+(c.up?'<b>SOON</b>':'<b>'+c.m+'</b><small>'+c.d+'</small>')+'</span><img src="'+c.img+'" alt="" loading="lazy"><span class="dq-tx"><small>'+(c.up?'กำลังจะมา '+c.d+' '+c.m:c.k+' · '+c.d+' '+c.m)+'</small><b>'+c.t+'</b><span>'+c.x+'</span></span></button>'}).join('');
    var C=[].slice.call(st.children),ord=C.map(function(_,i){return i});
    function lay(){var w=st.clientWidth,base=Math.min(400,w*.6),step=Math.min(78,(w-base)/(ord.length-1));ord.forEach(function(ci,p){var c=C[ci];c.style.width=base+'px';c.style.transform='translateX('+(p*step)+'px) translateY('+(p*7)+'px) scale('+(1-p*.035)+')';c.style.zIndex=50-p;c.classList.toggle('on',p===0);c.tabIndex=0});
      st.style.setProperty('--sw',(base+step*(ord.length-1))+'px')}
    C.forEach(function(c,ci){c.addEventListener('click',function(){var p=ord.indexOf(ci);if(p===0)return;ord=ord.slice(p).concat(ord.slice(0,p));lay()})});
    new ResizeObserver(lay).observe(st);lay()})();
  /* tilt + light on cards across the site */
  (function(){if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
    document.addEventListener('pointermove',function(e){var c=e.target.closest&&e.target.closest('.qv-im,.zb-t,.zp-c,.dq-c.on');document.querySelectorAll('.tl-on').forEach(function(x){if(x!==c){x.classList.remove('tl-on');x.style.removeProperty('--rx');x.style.removeProperty('--ry')}});if(!c)return;
      var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.classList.add('tl-on');c.style.setProperty('--rx',(-y*7)+'deg');c.style.setProperty('--ry',(x*9)+'deg');c.style.setProperty('--lx',(x+.5)*100+'%');c.style.setProperty('--ly',(y+.5)*100+'%')},{passive:true})})();

  /* Hall of Fame: aurora textures drawn once, moved by the GPU */
  (function(){var host=$('#h5Au');if(!host)return;var W=1024,H=420;
    function tex(seed,R){var c=document.createElement('canvas');c.width=W;c.height=H;var x=c.getContext('2d');x.globalCompositeOperation='lighter';
      R.forEach(function(r,k){for(var i=0;i<W;i+=2){var u=i/W,P=6.2832,yc=H*(r.y+r.a*Math.sin(u*r.f*P+seed)+.03*Math.sin(u*11*P/11*2+k+seed)),hh=H*r.h*(.6+.4*Math.sin(u*4*P/4*2+k*1.7+seed)),
          st=.5+.5*Math.sin(u*96*P/6.2832*6.2832/6.2832+k*3)*Math.sin(u*38*P/6.2832+seed),al=r.k*(.10+.22*st)*(.6+.4*Math.sin(u*2*P+k+seed));
          var g=x.createLinearGradient(0,yc-hh,0,yc+hh*.25);g.addColorStop(0,'rgba('+r.c+',0)');g.addColorStop(.75,'rgba('+r.c+','+al.toFixed(3)+')');g.addColorStop(.86,'rgba(255,255,240,'+Math.min(1,al*1.4).toFixed(3)+')');g.addColorStop(1,'rgba('+r.c+',0)');x.fillStyle=g;x.fillRect(i,yc-hh,2,hh*1.25)}});
      return c.toDataURL('image/webp',.82)}
    var A=tex(0,[{y:.30,a:.08,f:2,h:.34,c:[255,214,120],k:.9},{y:.52,a:.07,f:1,h:.3,c:[236,170,70],k:.8}]),
        B=tex(2,[{y:.42,a:.10,f:3,h:.26,c:[255,240,190],k:.75},{y:.34,a:.05,f:4,h:.16,c:[255,252,236],k:.6}]);
    var d=document.createElement('div');d.className='h5f-au2';d.setAttribute('aria-hidden','true');d.innerHTML='<i style="background-image:url('+B+'),url('+A+')"></i>';host.replaceWith(d)})();
  /* pause every Hall of Fame animation while it is off screen */
  (function(){var sec=$('.h5f');if(!sec)return;var all=[sec].concat([].slice.call(document.querySelectorAll('.rau,.rsd,#wkRift')));
    new IntersectionObserver(function(e){var off=!e[0].isIntersecting;all.forEach(function(n){n.classList.toggle('zz-off',off)})},{rootMargin:'120px'}).observe(sec)})();
  /* walker follows the rift's top edge (offsets cached) */
  (function(){var z=$('#wkRift'),sec=$('.h5f');if(!z||!sec)return;var E=[[0.0, 22], [0.027, 5], [0.086, 23], [0.135, 28], [0.19, 26], [0.22, 16], [0.259, 32], [0.281, 18], [0.342, 33], [0.365, 10], [0.392, 35], [0.44, 5], [0.494, 44], [0.543, 26], [0.568, 17], [0.592, 41], [0.637, 15], [0.698, 17], [0.743, 40], [0.788, 40], [0.828, 24], [0.886, 9], [0.938, 15], [0.99, 41], [1.0, 14]],o=null;
    function ey(f){for(var i=1;i<E.length;i++){if(f<=E[i][0]){var a=E[i-1],b=E[i],k=(f-a[0])/((b[0]-a[0])||1);return a[1]+(b[1]-a[1])*k}}return E[E.length-1][1]}
    function m(){var zr=z.getBoundingClientRect(),sr=sec.getBoundingClientRect();o={dx:zr.left-sr.left,w:sr.width,dy:sr.top-(zr.bottom-4)}}
    new ResizeObserver(m).observe(sec);addEventListener('resize',m);
    z.__g=function(lx){if(!o||!o.w)m();var f=(o.dx+lx)/o.w;return o.dy+ey(Math.max(0,Math.min(1,f)))}})();

  /* rift edge: strands drawn once per size, two variants cross-fade */
  (function(){var sec=$('.h5f'),hT=$('#rauT'),hB=$('#rauB');if(!sec||!hT)return;var ET=[[0.0, 22], [0.027, 5], [0.086, 23], [0.135, 28], [0.19, 26], [0.22, 16], [0.259, 32], [0.281, 18], [0.342, 33], [0.365, 10], [0.392, 35], [0.44, 5], [0.494, 44], [0.543, 26], [0.568, 17], [0.592, 41], [0.637, 15], [0.698, 17], [0.743, 40], [0.788, 40], [0.828, 24], [0.886, 9], [0.938, 15], [0.99, 41], [1.0, 14]],EB=[[0.0, 15], [0.033, 38], [0.075, 37], [0.109, 41], [0.138, 9], [0.166, 31], [0.19, 40], [0.229, 40], [0.268, 41], [0.311, 10], [0.356, 22], [0.412, 23], [0.463, 39], [0.498, 20], [0.529, 10], [0.59, 11], [0.643, 19], [0.686, 38], [0.717, 41], [0.745, 28], [0.777, 32], [0.801, 7], [0.863, 30], [0.91, 5], [0.942, 18], [0.964, 18], [0.989, 38], [1.0, 9]],H=96,M=50,lastW=0;
    function ey(E,f){for(var i=1;i<E.length;i++){if(f<=E[i][0]){var a=E[i-1],b=E[i],k=(f-a[0])/((b[0]-a[0])||1);return a[1]+(b[1]-a[1])*k}}return E[E.length-1][1]}
    function strip(W,E,up,ph){var c=document.createElement('canvas');c.width=W;c.height=H;var x=c.getContext('2d');x.shadowColor='rgba(255,190,70,.55)';x.shadowBlur=4;
      for(var i=0;i<W;i+=2){var f=i/W,e=ey(E,f),y0=up?(M+e):(H-M-e),n=Math.sin(f*70+ph)*Math.sin(f*23-ph*.6)+Math.sin(f*140+ph*1.7)*.35,len=Math.max(0,10+30*(.5+.5*n)),al=Math.min(1,.45+.55*(.5+.5*n));
        var g=x.createLinearGradient(0,y0,0,up?y0-len:y0+len);g.addColorStop(0,'rgba(232,160,40,'+al.toFixed(3)+')');g.addColorStop(.3,'rgba(246,196,84,'+(al*.8).toFixed(3)+')');g.addColorStop(1,'rgba(255,224,140,0)');x.fillStyle=g;x.fillRect(i,up?y0-len:y0,1.4,len)}
      return c}
    function build(){var Wc=sec.clientWidth;if(!Wc||Math.abs(Wc-lastW)<4)return;lastW=Wc;var W=Math.min(1200,Math.round(Wc/1.5));
      [[hT,ET,true],[hB,EB,false]].forEach(function(o){var host=o[0];host.innerHTML='';[0,2.4].forEach(function(ph,k){var c=strip(W,o[1],o[2],ph);c.className='rv'+k;c.style.width=Wc+'px';c.style.height=H+'px';host.appendChild(c)})})}
    var tm;new ResizeObserver(function(){clearTimeout(tm);tm=setTimeout(build,150)}).observe(sec);build()})();
  /* v62: sections off screen stop animating */
  (function(){if(!('IntersectionObserver' in window))return;var io=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('zz-off',!e.isIntersecting)})},{rootMargin:'160px'});
    document.querySelectorAll('[data-view] > section:not(.h5f), [data-view] > .zq, .hp-grid, .zc2, .zb, .zp, .mc, .end, .ptn, .au2, .ab-win, .ab-h, .ab-do, .ab-real, .ab-res, .ab-ct').forEach(function(n){if(!n.classList.contains('h5f'))io.observe(n)})})();
  /* v63: featured video plays only while on screen */
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
  /* v64: when an answer opens, the search glides up under the nav so the answer has room (no page jump) */
  (function(){var z=$('.zq'),top=$('.zq-top'),r=$('#zqRes'),sw=$('.zq-sw');if(!z||!r||!top)return;
    function upd(){var open=!r.hidden;if(open){if(z.classList.contains('ask'))return;var b=sw.getBoundingClientRect().top,d=Math.max(0,b-(innerWidth<700?84:96));if(scrollY>40)d=0;top.style.setProperty('--ask',(-d)+'px');z.classList.add('ask')}else{z.classList.remove('ask');top.style.removeProperty('--ask')}}
    new MutationObserver(upd).observe(r,{attributes:true,attributeFilter:['hidden']})})();
  /* v66: story clip opens in a player with sound, only when asked */
  (function(){var d=$('#ocDlg');if(!d)return;var v=d.querySelector('video');
    document.querySelectorAll('.oc-play').forEach(function(b){b.addEventListener('click',function(){v.src=b.dataset.v;if(d.showModal)d.showModal();else d.setAttribute('open','');v.play().catch(function(){})})});
    function shut(){v.pause();d.close?d.close():d.removeAttribute('open')}
    d.querySelector('.oc-x').addEventListener('click',shut);d.addEventListener('click',function(e){if(e.target===d)shut()});d.addEventListener('close',function(){v.pause()})})();
  /* v69: activity page */
  (function(){var G=$('#avG'),F=$('#avF');if(!G||!F)return;
    var IMG={'IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','AI for Business':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'};
    var TC={'ค่าย':'#E8891C','เวิร์กชอป':'#1C74D9','แข่งขัน':'#D6336C','โชว์ผลงาน':'#7048E8','โครงการ':'#1E8E5A'};
    var GN={'ค่าย':'ได้ผลงานกลับไปภายในไม่กี่วัน','เวิร์กชอป':'ได้ลองทักษะใหม่ในวันเดียว','แข่งขัน':'ได้ลงแข่งจริง มีเรื่องเล่าใส่พอร์ต','โชว์ผลงาน':'ได้นำเสนอผลงานต่อผู้ชมจริง','โครงการ':'ได้ผลงานส่งเวทีระดับประเทศ'};
    var L=ACT.filter(function(a){return !a[4]});$('#avCount').textContent=L.length;
    var types=['ทั้งหมด'];L.forEach(function(a){if(types.indexOf(a[3])<0)types.push(a[3])});
    F.innerHTML=types.map(function(t,i){var n=t==='ทั้งหมด'?L.length:L.filter(function(a){return a[3]===t}).length;return '<button type="button" data-t="'+t+'" aria-pressed="'+(i?'false':'true')+'">'+t+' <span>'+n+'</span></button>'}).join('');
    function card(a){var im=IMG[a[1]],c=TC[a[3]]||'#1C74D9';
      return '<article class="avc" style="--tc:'+c+'"><div class="avc-m">'+(im?'<img src="/Hamterco/img/'+im+'.webp" alt="" loading="lazy">':'<div class="avc-ty"><b>'+a[1]+'</b><img src="/Hamterco/img/hh-mascot.webp" alt=""></div>')+'</div><div class="avc-t"><p class="avc-d"><span>'+a[3]+'</span>'+a[0]+'</p><h3>'+a[1]+'</h3><p>'+a[2]+'</p><p class="avc-g">น้องได้: '+GN[a[3]]+'</p></div></article>'}
    function show(t){G.innerHTML=L.filter(function(a){return t==='ทั้งหมด'||a[3]===t}).map(card).join('')}
    F.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;F.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});show(b.dataset.t)});show('ทั้งหมด');
    function cd(){var ms=new Date('2026-11-14T09:00:00+07:00')-new Date(),el=$('#avnCd');if(!el)return;if(ms<=0){el.hidden=true;$('#avnTag').textContent='จัดไปแล้ว';return}
      var d=Math.floor(ms/864e5),h=Math.floor(ms%864e5/36e5),m=Math.floor(ms%36e5/6e4),b=el.querySelectorAll('b');b[0].textContent=d;b[1].textContent=h;b[2].textContent=m}
    cd();setInterval(cd,30000)})();
  /* v71: hero headline keeps one look; videos play only on screen */
  (function(){
    if(!('IntersectionObserver' in window))return;var rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
    var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting&&!rm)v.play().catch(function(){});else v.pause()})},{threshold:.2});
    document.querySelectorAll('.hx-bg video,.oc-biz video,.us-m video').forEach(function(v){v.removeAttribute('autoplay');io.observe(v)})})();
  /* v75: archive of all student work */
  (function(){var G=$('#arcG'),C=$('#arcChips');if(!G)return;
    var AR=[["soi-13", "SOI 13", "", "คอร์สและโปรเจกต์", "Soi 13 เป็นเกมแนว Horror ที่เราจะได้เล่นเป็นนักเรียนคนหนึ่งออกไปตามหาไอโตะ เพื่อนที่หายตัวไปใน Soi 13 เมื่อ 3 วันที่แล้ว…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/771015891760054495/2026-06-03/video-Recording-2026-06-03-094816-504306158e41b728.mp4", "Can", "top"], ["omni-piece", "Omni Piece", "Dead RAILs", "Intelligence Camp", "นี่คือเกมแอ็กชันบน Roblox ที่ผสมผสานความตื่นเต้นของการตามล่าหา", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/954286608113360927/2026-06-01/video-Omni-Piece-df01e33bdd462751.mkv", "IC2-87 CHAMP", "top"], ["khao-yai-alert", "Khao Yai Alert", "", "Intelligence Camp", "ระบบ Forest Fire Alert เป็นเว็บสำหรับแจ้งเหตุไฟป่าและเหตุฉุกเฉิน โดยใช้ GPS ระบุตำแหน่งผู้ใช้งาน…", "https://media.mediaquest.uk/profile-projects/1229104775380074537/2026-06-20/video-202605122027-ab781a01cc88d53f.mp4", "IC2-06 เซน IC2-07 ไอซ์ IC2-76 POOM", "top"], ["phun", "PHUN", "", "Intelligence Camp", "", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/1081540856525357066/2026-06-12/video-Phun-8175be45f16f4d1c.mp4", "Muftee", "middle"], ["man-in-the-forest", "Man in the forest", "", "ค่ายเกมผี", "เรื่องราวของชายคนหนึ่งที่กลับไปเยี่ยมบ้านเกิดแต่พบว่าหมู่บ้านที่เขารู้จักได้เปลี่ยนไปอย่างสิ้นเชิง เป็นเกมวิ่งหนีผี…", "https://media.mediaquest.uk/profile-projects/1522168190610968577/2026-07-06/video-1000021628-a4efee4c1fe0f7da.mp4", "โอม ยูเอส พฤกษ์ Ming", "middle"], ["big-yokai", "Big Yokai", "BigBackDoor", "คอร์สและโปรเจกต์", "เป็นเกม Action Horror ที่เราจะต้องไปกำราบวิญญาณในสถานที่ต่างๆ เพื่อไถ่ตัวลูกสาวที่ถูกมาเฟียจับไปเป็นตัวประกัน", "https://media.mediaquest.uk/profile-projects/868026277716717588/2026-07-05/video-game-Roblox-Studio-2026-04-23-17-30-53-d17cafe9d8ae79ba.mp4", "ไผ่ Jame สิน", "middle"], ["woody-jack-restaurant", "Woody-Jack Restaurant", "ฝันใหญ่ไข่เล็ก", "ค่ายเกมผี", "Woody Jack Restaurant…", "https://media.mediaquest.uk/profile-projects/858715669289893949/2026-07-05/video-camp-1d415323b5bab433.mov", "สตางค์ โฟม ไอซ์สึ", "middle"], ["bath-66e2e378", "ประสบ Bath", "Somrom dekpunya oon👽", "ค่ายเกมผี", "Concept: BlackRoom + PublicBathroom", "https://media.mediaquest.uk/profile-projects/1280174904158851082/2026-07-05/video-1000130888-08661a0132672e5a.mp4", "เปรม เดลต้า ปอน", "middle"], ["heat-thieves", "HEAT THIEVES", "", "GameJam X", "เกมที่ทำขึ้นตามหัวข้อของงาน GameJam X", "https://media.mediaquest.uk/profile-projects/1023446854475710565/2026-07-05/video-Heat_Thieves-20c45ad45b6d76e3.mov", "บอย Eve ออม Tle", "middle"], ["the-collector", "The Collector", "", "NSC 2026", "เป็นเกม The Collector ที่นำไปลงแข่ง NSC ครับ โดยอันนี้เป็นรายละเอียดต้นแบบก่อนที่จะนำไปปรับแก้นะครับ…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/767330842514817036/2026-06-01/video-2026-06-01-20-00-06-c6424c78d4c2559e.mkv", "อาร์ม Porsche", "middle"], ["a-picturesque-breakfast", "A Picturesque Breakfast", "Springroll", "NSC 2026", "", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/970873503677046825/2026-06-03/video-2026-06-03-22-12-02-866bbbd7194d5e3b.mp4", "โฟร์ ไอเดีย ชิว เอ็กซ์", "middle"], ["fractured-sanity", "Fractured Sanity", "", "ค่ายเกมผี", "เกมผีที่เราติดอยู่ในโรงพยาบาลร้าง และต้องทำภารกิจที่ได้รับเพื่อออกจากโรงพยาบาล", "https://media.mediaquest.uk/profile-projects/905762435011579904/2026-07-05/video-FRACTURED-SANITY-fc159629b865b129.mp4", "เคนตะ ภัทร ธาม ภพ", "small"], ["game-pee-naja-eiei", "Game pee naja eiei", "เป็นบ้า", "ค่ายเกมผี", "เกม Roblox ที่คุณจะได้เล่นเป็นผู้ป่วยจิตเวช", "https://media.mediaquest.uk/profile-projects/989119206714912809/2026-07-05/video-GamePee-105-GamePee-112-GamePee-31-aa52291dd2fb9ae2.mp4", "พอช ริว เตย์", "small"], ["camping-with-us", "Camping with us", "ไข่ดาวแคมป์ไซต์", "ค่ายเกมผี", "เกมผีบอกบรู๊ววว", "https://media.mediaquest.uk/profile-projects/701365172970848276/2026-07-05/video-Camping-With-Us-3a2f5afc0b345691.mp4", "โต้ Mark เฟื่อง", "small"], ["f-e-a-r", "F.E.A.R.", "ขนตูดลุก", "ค่ายเกมผี", "เป็นผลงานเกม Horror แนว Party Horror ที่เราจะต้องเอาชีวิตรอดออกมาจากโรงแรมบนเกาะปีศาจ", "https://media.mediaquest.uk/profile-projects/868026277716717588/2026-07-05/video-GamePee-67e252e5351c6811.mp4", "ไผ่ สิน รุต แอม", "small"], ["leukophobia", "Leukophobia", "Leukophobia", "ค่ายเกมผี", "เกมผีสไตล์ Psychological ที่สร้างขึ้นภายใน 3 วัน เกี่ยวกับ ILl ทหารรับจ้างที่ต้องการแก้ไขอดีตที่เสียใจ", "https://media.mediaquest.uk/profile-projects/712872989657530459/2026-07-05/video-0705-487f56202f89b0a0.mp4", "Nan ฟาร์ม เรย์อา", "small"], ["anomoly", "ห้องน้ำ Anomaly", "บ้านเจ๊นวล", "ค่ายเกมผี", "แมพนี้จะจำลองว่าเราได้ไปเข้าห้องน้ำสาธารณะ แล้วมีสิ่งแปลกๆ ที่ทำให้เราอยู่ใน loop เราต้องหาสิ่งผิดปกติในห้องน้ำให้ได้ ถ้าห…", "https://media.mediaquest.uk/profile-projects/1258040440943284286/2026-07-05/video-2026-07-05-192848-e14041dd09bce0e5.mp4", "มอส เสือ", "small"], ["melody-duel", "Melody Duel", "", "AI Camp", "เป็นเว็บไซต์สำหรับร้องเพลงคาราโอเกะทางออนไลน์ สามารถเล่นแข่งกับเพื่อนได้ว่าใครร้องเพราะกว่าด้วยโหมด Duel…", "https://media.mediaquest.uk/profile-projects/759442610460557312/2026-06-21/video-AC2-85-ad074ea2593a0b0d.mp4", "เฟท", "small"], ["together-forever", "Together Forever", "summertimerunway", "AI Camp", "เกมผีแนว Asymmetrical Horror มีผู้เล่นเป็นผี 1 คน และเป็นคน 4 คน", "https://media.mediaquest.uk/profile-projects/1161375845953323048/2026-06-21/video-play-5f2d71993c16b66a.mp4", "IC2-65 Aung-un", "small"], ["the-collectors", "The Collectors", "", "AI Camp", "เกมที่ให้บรรยากาศหลอนๆ โดยภารกิจคือเก็บของต่างๆ ในบ้านให้ได้ 5 ชิ้น แล้วนำไปส่งที่บอร์ดเพื่อกลับออกไป", "https://media.mediaquest.uk/profile-projects/549164350288691200/2026-06-22/video-AC2-45-35bb4dd666211885.mp4", "ทัพพ์", "small"], ["room-304", "ROOM 304", "", "คอร์สและโปรเจกต์", "เป็นเกม point and click ที่เราจะรับบทเป็นชายความจำเสื่อมต้องสำรวจห้องนอนเพื่อหาทางออกและค้นหาความจริงที่ซ่อนอยู่", "https://media.mediaquest.uk/profile-projects/732911022020493413/2026-06-24/video-2026-06-24-20-24-57-2010362cdea5a053.mov", "IC2-47 Bonus", "small"], ["deadsea", "Deadsea", "Deadsea", "คอร์สและโปรเจกต์", "แมพผจญภัย จัดการบอส และล่องเรือ", "https://media.mediaquest.uk/profile-projects/907567939153195038/2026-06-24/video-Screen-Recording-2026-06-24-205251-46f3b92cf79b388a.mp4", "ปุณ", "small"], ["element-royal", "Element Royal", "Scarlet", "AI Camp", "เป็นเกมแนว Battle Royale ที่เราจะเลือกธาตุมาสู้กัน มีอยู่ 2 แมพ แมพเมืองและภูเขาไฟ เมื่อเข้าไปในเกม จะมี Action ตามนี้ M1…", "https://media.mediaquest.uk/profile-projects/1504505879033020419/2026-06-21/video-Screen-Recording-2026-06-21-190831-66c67e34f9fd61f5.mp4", "เฟื่อง", "small"], ["endlessnoon", "EndlessNoon", "Deep", "GameJam X", "เกมที่ผู้เล่นจะต้องหาทางออกจากดาวดวงนี้เพราะแดดของดาวดวงนี้ร้อนเกินไป", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/903249823044612166/2026-06-03/video-EndLessNoonGameJamX-7d1ee4eae67af5db.mp4", "Tin โจม", "small"], ["micro-immersive-sim-initialize-override-protocol", "Micro Immersive SIM initialize override protocol", "มิตรภาพลาบมะม่วง", "GameJam X", "รางวัลรองชนะเลิศ GameJam X เป็นเกมแนวเนื้อเรื่อง เอาชีวิตรอด Sci-fi แบบ 3D มุมมองบุคคลที่หนึ่ง (First-person)…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/1464609178420121703/2026-06-03/video-0603-1d14be8c62bc2f6a.mp4", "เพชร เจ", "small"], ["mythnight", "MythNight", "", "NSC 2026", "เกมแนวสยองขวัญลึกลับแบบ Multiplayer ในมุมมองบุคคลที่หนึ่ง ที่เน้นบรรยากาศความน่ากลัวและการสำรวจพื้นที่มืด…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/1382608609237794836/2026-06-02/video-Recording-2026-06-02-194710-c1eaccb65699e741.mp4", "โชกุน", "small"], ["nampun", "Nampun", "YAMA5", "GameJam X", "เกมน้ำปั่น ทำใน 72 ชั่วโมง ธีม “ร้อน”", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/728153538869329960/2026-06-02/video-2026-06-02-19-25-34-c0276a217674245f.mp4", "วิน", "small"], ["ecoeats-mas", "EcoEats Mas", "95เต็มถัง", "AI Camp", "EcoEats MAS คือแพลตฟอร์มตลาดกลางซื้อขายอาหารส่วนเกินแบบเรียลไทม์เพื่อช่วยลดขยะอาหาร (Food Waste)…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/1368175056399765546/2026-06-02/video-2026-05-31-182922-637c7f564a0f0064.mp4", "ยิม Nut Chokun", "small"], ["meow-lostship", "MEOW_LOSTSHIP", "moew", "GameJam X", "", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/1053524169746296912/2026-06-01/video-meow-lost-ship-ab906059c2b0f6e4.mp4", "ไอเดีย", "small"], ["gamejam-x", "เมษาหน้าลาบ", "ไอหน้าลาบ", "คอร์สและโปรเจกต์", "เกมขายลาบที่เราได้รับบทเป็นลุงร้านลาบที่ต้องออกตะเวนไปขายลาบให้คนตามบ้าน เพราะอากาศร้อนแบบนี้ คนไม่ออกมาซื้อลาบกันหรอก", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/1023982559203446845/2026-06-01/video-video-gameplay-848031cdb02490ab.mp4", "Nainy นน Porpla", "small"], ["bewarefront", "Bewarefront", "", "คอร์สและโปรเจกต์", "เกมนี้เป็นเกม First-Person Shooter ที่ให้คุณรับบทเป็นทหาร ในช่วงสงครามโลกครั้งที่ 2…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/961916759026331658/2026-06-01/video-2026-03-02-21-05-14-a304897c93f03ff4.mp4", "สตางค์", "small"], ["endlessly", "Endlessly", "summertimerunway", "AI Camp", "เกมยังทำไม่เสร็จ กำลังพัฒนาต่อ", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/1161375845953323048/2026-06-01/video-2026-05-31-19-23-59-d487cdfafe43cf4e.mp4", "IC2-65 Aung-un IC2-67 ว่าน เปรม Leo", "small"], ["ghostly-prisoner-demo", "Ghostly Prisoner[Demo]", "solo หรือ trio ให้ทาย", "AI Camp", "เป็นเกมที่ผู้เล่นจะได้รับบทเป็นผีตัวน้อยที่ต้องการหนีออกจากคุกร้างที่ผู้คุมละเลยการดูแลในยามกลางคืน…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/759442610460557312/2026-06-01/video-Ghostly-prisoner-Demo-e66f34d6b43082f3.mp4", "เฟท ตี๋", "small"], ["woven-citadel", "Woven Citadel", "", "AI Camp", "ทำระบบ Movement และ Gameplay พื้นฐานของเกม Woven Citadel", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/736930964520829028/2026-06-01/video-2026-06-01-17-58-21-8ec3e59290f49005.mp4", "Canon พุฒิ", "small"], ["bidet-blaster", "Bidet Blaster", "", "GameJam X", "The world is burning and your butt is stuck to the toilet Use your high-pressure bidet to blast fires and propel…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/886426175445024858/2026-05-30/video-Gameplay-96dc2467be6c52f3.mp4", "โอม Boat Poot", "small"], ["beat-the-beat-on-beach", "Beat the Beat on Beach", "3B", "GameJam X", "เกมแนว Rhythm Karaoke ที่ผู้เล่นสามารถร้องเพลงกับเพื่อนๆ ได้แบบ Realtime โดยไม่ต้องเสียเงินสักบาทในการเล่นเพลง…", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/425549473930936320/2026-05-29/video-Sequence-01_2-J1R4T-f15d9829b4a4a6bb.mp4", "Pubpab", "small"], ["night-fear", "Night Fear", "NuutorDev.", "คอร์สและโปรเจกต์", "เกมผีเกมแรกของพี่โฟกัสสมัย ม.6 โคตรเท่โคตรอันตราย no AI สมองล้วนโหดจัดปลัดบอก", "https://pub-1edf364a5206483081ad6407a8739e13.r2.dev/profile-projects/563644358352568331/2026-05-25/video-100-Night-Fear-new-0e3a5e496d6b0e23.mp4", "โฟกัส", "small"]];
    var ORD=['ทั้งหมด','ค่ายเกมผี','GameJam X','AI Camp','NSC 2026','Intelligence Camp','คอร์สและโปรเจกต์'];
    C.innerHTML=ORD.map(function(t,i){var n=i?AR.filter(function(a){return a[3]===t}).length:AR.length;return '<button type="button" data-g="'+t+'" aria-pressed="'+(i?'false':'true')+'">'+t+' '+n+'</button>'}).join('');
    function card(a,i){return '<button type="button" class="ac" data-i="'+i+'"><span class="ac-m"><img src="/Hamterco/img/ar-'+a[0]+'.webp" alt="" loading="lazy"><i class="ac-pl" aria-hidden="true"></i><em>'+a[3]+'</em></span><b>'+a[1]+'</b><small>'+(a[2]?'ทีม '+a[2]:(a[6]?'โดย '+a[6]:''))+'</small></button>'}
    function show(g){G.innerHTML=AR.map(function(a,i){return (g==='ทั้งหมด'||a[3]===g)?card(a,i):''}).join('')}
    C.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;C.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});show(b.dataset.g)});show('ทั้งหมด');
    var D=$('#arcDlg'),V=D.querySelector('video');
    G.addEventListener('click',function(e){var c=e.target.closest('.ac');if(!c)return;var a=AR[+c.dataset.i];
      V.src=a[5];V.poster='/Hamterco/img/ar-'+a[0]+'.webp';D.querySelector('.arc-dt b').textContent=a[1];D.querySelector('.arc-dt p').textContent=(a[4]||'')+(a[6]?' · ผู้สร้าง: '+a[6]:'');
      D.querySelector('.arc-dt a').href='https://www.hamsterhub.co/go/projects/'+a[0];if(D.showModal)D.showModal();else D.setAttribute('open','');V.play().catch(function(){})});
    function shut(){V.pause();V.removeAttribute('src');V.load();D.close?D.close():D.removeAttribute('open')}
    D.querySelector('.oc-x').addEventListener('click',shut);D.addEventListener('click',function(e){if(e.target===D)shut()});D.addEventListener('close',function(){V.pause()});
    document.querySelectorAll('.yt-side [data-jump]').forEach(function(b){b.addEventListener('click',function(){setTimeout(function(){var t=$('#'+b.dataset.jump);if(t)scrollTo(0,t.getBoundingClientRect().top+scrollY-80)},60)})})})();
  /* activity list */
  var AIMG={'All for One University รอบชิงชนะเลิศ':'k-afo-logo','IoTE KMITL 2026 Showcase (Hallow Open House)':'k-hallow','All for One University รอบออนไลน์':'k-afo','AI Camp Season 2':'k-aicamp','Game Pee Camp':'k-ghost','GameJam X ปีที่ 5':'k-gamejam','Dek-70 Camp':'k-dek70','Dek70 Camp':'k-dek70','NSC Software Project 2026':'s-showcase2'},ACOL={'ค่าย':['#FFF1D6','#B26A00'],'เวิร์กชอป':['#E3F3FF','#1D5FB8'],'แข่งขัน':['#FFE6EE','#B23A68'],'โชว์ผลงาน':['#EEE8FF','#5B3FD6'],'โครงการ':['#E6F7EC','#1E7A4C']};
  var MAS={'ค่าย':'ev-st2','เวิร์กชอป':'ev-st3','แข่งขัน':'ev-st4','โชว์ผลงาน':'ev-st1','โครงการ':'ev-st5'},
    GAIN={'ค่าย':'ได้ผลงานกลับไปภายในไม่กี่วัน','เวิร์กชอป':'ได้ลองทักษะใหม่ในวันเดียว','แข่งขัน':'ได้ลงแข่งจริง มีเรื่องเล่าใส่พอร์ต','โชว์ผลงาน':'ได้นำเสนอผลงานต่อผู้ชมจริง','โครงการ':'ได้ผลงานส่งเวทีระดับประเทศ'};
  function alist(){var el=$('#acl');if(!el)return;el.innerHTML=ACT.filter(function(a){return !a[4]}).map(function(a){var im=AIMG[a[1]];
    return '<li class="er"'+(im?' data-pv="/Hamterco/img/'+im+'.webp"':'')+'><time>'+a[0]+'</time><span class="er-c" style="--c:'+ACOL[a[3]][1]+'">'+a[3]+'</span><div><b>'+a[1]+'</b><p>'+a[2]+'</p><em>น้องได้: '+GAIN[a[3]]+'</em></div></li>'}).join('');
    var pv=$('#erPv');el.querySelectorAll('.er').forEach(function(r){r.addEventListener('pointerenter',function(){if(!r.dataset.pv){pv.classList.remove('on');return}pv.src=r.dataset.pv;pv.classList.add('on')});r.addEventListener('pointerleave',function(){pv.classList.remove('on')})});
    el.addEventListener('pointermove',function(e){pv.style.transform='translate('+(e.clientX+28)+'px,'+(e.clientY-120)+'px) rotate(4deg)'})}
  alist();
  (function(){if(new Date()>new Date('2026-11-14T18:00:00+07:00')){var k=$('#auK');if(k)k.textContent='เพิ่งจบไป · 14 พ.ย. 2569'}})();
  /* countdowns */
  function cd(){var d=Math.ceil((new Date('2026-11-14T09:00:00+07:00')-new Date())/864e5),t=d>0?'อีก '+d+' วัน':'วันนี้';['#cdHome','#cdAct'].forEach(function(s){var e=$(s);if(e)e.textContent=t})}cd();
  /* portex seniors */
  var cs=$('#cxSen');if(cs)cs.innerHTML=[5,6,9,0,12,10,3,15].map(function(i){var g=G[i];return '<li><img src="/Hamterco/img/dek69-'+g[0]+'.webp" alt="'+g[1]+'" loading="lazy"><b>'+g[1]+'</b><span>'+g[3]+'<br>'+UN[g[2]]+'</span><em>เรียนคอร์ส '+g[4]+'</em></li>'}).join('');
  /* copy */
  document.addEventListener('click',function(e){var b=e.target.closest('[data-copy]');if(!b)return;var t=b.dataset.copy,done=function(){var o=b.firstChild.textContent;b.firstChild.textContent='คัดลอกแล้ว ';setTimeout(function(){b.firstChild.textContent=o},1600)};
    if(navigator.clipboard)navigator.clipboard.writeText(t).then(done,done);else done()});
  /* works panes */
  function pane(p){$$('.yt-side button').forEach(function(b){b.setAttribute('aria-current',String(b.dataset.pane===p))});$$('.yt-pane').forEach(function(s){s.classList.toggle('on',s.dataset.p===p)})}
  $$('.yt-side button').forEach(function(b){b.addEventListener('click',function(){pane(b.dataset.pane);scrollTo(0,0)})});
  $('#vgrid').addEventListener('click',function(e){var c=e.target.closest('.vc');if(!c)return;pane('shorts');scrollTo(0,0);var i=+c.dataset.i;setTimeout(function(){var b=document.querySelector('.tk-index-btn[data-tk-go="'+(i+1)+'"]');if(b)b.click()},80)});
  if(hg)hg.addEventListener('click',function(e){var c=e.target.closest('.hw');if(!c)return;pendingPane=['shorts',+c.dataset.i];location.hash='works'});
  var pendingPane=null;
  document.addEventListener('click',function(e){var a=e.target.closest('a[data-pane]');if(a)pendingPane=[a.dataset.pane]});
  /* reveal + count */
  function count(el){var to=+el.dataset.count;if(reduce||!to)return;var t0=null;el.textContent='0';(function f(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/1100);el.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(performance.now())}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;e.target.classList.add('in');Array.prototype.forEach.call(e.target.querySelectorAll('[data-count]'),count);io.unobserve(e.target)})},{rootMargin:'0px 0px -8% 0px'});
  function arm(){$$('[data-view].on .rv:not(.in)').forEach(function(el){io.observe(el)})}

  var inView=function(el){var r=el.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight&&!document.hidden&&document.querySelector('[data-view="home"].on')};
  /* hero: three.js 2.5D hamster hub on a giant maker desk. hamsters wander, zig-zag sprint loops,
     chase each other, sometimes crash into the edge and get knocked out; pick them up by the scruff to dangle them */
  (function(){var hx=$('#hx'),st=$('#hx3'),cv=$('#hxCanvas'),say=$('#hxSay');if(!hx||!cv)return;
    var ok=false;try{ok=!!window.THREE&&!!(cv.getContext('webgl')||cv.getContext('experimental-webgl'))}catch(e){}
    if(!ok){hx.classList.add('nogl');return}
    var T=THREE,R=new T.WebGLRenderer({canvas:cv,antialias:true,alpha:true});R.outputEncoding=T.sRGBEncoding;R.setPixelRatio(Math.min(devicePixelRatio||1,2));
    var S=new T.Scene(),C=new T.OrthographicCamera(-1,1,1,-1,-100,100),L=new T.TextureLoader(),w=1,h=1,bw=1,bh=1,bx=0,by=0,uMin=0,uMax=1,IW=1536,IH=864,V0=.865,V1=.97;
    function tex(u,cb){var t=L.load(u,function(){cb&&cb(t)});t.encoding=T.sRGBEncoding;t.anisotropy=4;return t}
    function ctex(draw){var c=document.createElement('canvas');c.width=c.height=64;draw(c.getContext('2d'));var t=new T.CanvasTexture(c);t.encoding=T.sRGBEncoding;return t}
    var shT=ctex(function(g){var r=g.createRadialGradient(32,32,2,32,32,32);r.addColorStop(0,'rgba(90,55,20,.42)');r.addColorStop(1,'rgba(90,55,20,0)');g.fillStyle=r;g.fillRect(0,0,64,64)});
    var dustT=ctex(function(g){g.lineWidth=3.5;g.strokeStyle='#7A4A22';g.fillStyle='#FFF7E6';g.beginPath();[[22,38,13],[36,30,15],[46,40,11],[30,44,11]].forEach(function(c){g.moveTo(c[0]+c[2],c[1]);g.arc(c[0],c[1],c[2],0,7)});g.stroke();g.fill();g.fillStyle='#F3DDB4';g.beginPath();g.arc(40,44,6,0,7);g.fill()});
    var starT=ctex(function(g){g.translate(32,32);g.fillStyle='#FFC93C';g.strokeStyle='#7A4A12';g.lineWidth=3;g.beginPath();for(var i=0;i<10;i++){var a=i*Math.PI/5-Math.PI/2,r=i%2?11:27;g.lineTo(Math.cos(a)*r,Math.sin(a)*r)}g.closePath();g.fill();g.stroke()});
    var sparkT=ctex(function(g){g.translate(32,32);g.fillStyle='#fff';g.strokeStyle='#7A4A22';g.lineWidth=3;g.beginPath();for(var i=0;i<8;i++){var a=i*Math.PI/4,r=i%2?5:28;g.lineTo(Math.cos(a)*r,Math.sin(a)*r)}g.closePath();g.stroke();g.fill()});
    var sweatT=ctex(function(g){g.fillStyle='#8FD3FF';g.strokeStyle='#2B5F8A';g.lineWidth=3;g.beginPath();g.moveTo(32,6);g.quadraticCurveTo(52,36,32,56);g.quadraticCurveTo(12,36,32,6);g.fill();g.stroke()});
    var foot=function(){var g=new T.PlaneGeometry(1,1);g.translate(0,.5,0);return g}(),top=function(){var g=new T.PlaneGeometry(1,1);g.translate(0,-.5,0);return g}(),flat=new T.PlaneGeometry(1,1);
    var bgT=tex('/Hamterco/img/px-bg.webp',function(){hx.classList.add('ready')});bgT.generateMipmaps=false;bgT.minFilter=T.LinearFilter;var bg=new T.Mesh(flat,new T.MeshBasicMaterial({map:bgT}));bg.position.z=-50;bg.visible=false;S.add(bg);
    var P=[];for(var i=0;i<70;i++){var pm=new T.Mesh(flat,new T.MeshBasicMaterial({map:dustT,transparent:true,depthWrite:false}));pm.visible=false;pm.renderOrder=400;S.add(pm);P.push({m:pm,life:0})}
    function puff(x,y,n,kind,spread){for(var k=0;k<n;k++){var p=null;for(var j=0;j<P.length;j++)if(P[j].life<=0){p=P[j];break}if(!p)return;
      var tx={star:starT,spark:sparkT,sweat:sweatT}[kind]||dustT;p.m.material.map=tx;p.m.material.needsUpdate=true;p.kind=kind;var fly=kind!=='dust';
      var a=fly?Math.random()*Math.PI*2:(Math.random()<.5?Math.PI:0)+(Math.random()-.5)*.9,v=(spread||1)*(fly?130+Math.random()*120:40+Math.random()*70);
      p.x=x;p.y=y;p.vx=Math.cos(a)*v;p.vy=fly?Math.abs(Math.sin(a))*v+60:20+Math.random()*30;p.r=kind==='sweat'?0:Math.random()*6;p.vr=kind==='sweat'?0:(Math.random()-.5)*8;
      p.ro=Math.round((spread&&spread.ro)||15);p.s0=(kind==='star'?.028:kind==='spark'?.02:kind==='sweat'?.018:.032)*bh*(.7+Math.random()*.6);p.max=p.life=kind==='star'?.9:kind==='dust'?.55+Math.random()*.3:.6;p.m.visible=true}}
    var defs=[['gamer',576/898,560/840,560/416,'ทำเกมด้วย Unity'],['walker',640/813,505/874,560/455,'เขียนแอปและเว็บ'],['maker',616/864,511/894,560/368,'ต่อบอร์ด IoT']],H=[];
    defs.forEach(function(d,i){var tN=tex('/Hamterco/img/n-'+d[0]+'.webp'),tD=tex('/Hamterco/img/n-'+d[0]+'-d.webp'),tK=tex('/Hamterco/img/n-'+d[0]+'-k.webp');
      var m=new T.Mesh(foot,new T.MeshBasicMaterial({map:tN,transparent:true,depthWrite:false})),md=new T.Mesh(top,new T.MeshBasicMaterial({map:tD,transparent:true,depthWrite:false}));md.visible=false;md.renderOrder=300;
      var s2=new T.Mesh(flat,new T.MeshBasicMaterial({map:shT,transparent:true,depthWrite:false}));S.add(s2);S.add(m);S.add(md);
      var st=[0,1,2].map(function(){var q=new T.Mesh(flat,new T.MeshBasicMaterial({map:starT,transparent:true,depthWrite:false}));q.visible=false;q.renderOrder=450;S.add(q);return q});
      H.push({i:i,m:m,md:md,s:s2,st:st,tN:tN,tK:tK,ar:d[1],arD:d[2],arK:d[3],line:d[4],u:.3+i*.2,d:.3+.3*(i%2),tu:.5,td:.5,face:i%2?-1:1,mode:'idle',t:.6+i*.9,ph:Math.random()*6,walk:0,
        x:0,y:0,vy:0,lift:0,ko:0,dizzy:0,ang:0,av:0,gx:0,gy:0,pgx:0,cvx:0,dust:0,path:[],sq:0,ft:0})});
    function fit(){if(st.clientWidth<2||st.clientHeight<2)return;w=st.clientWidth;h=st.clientHeight;R.setSize(w,h,false);C.left=-w/2;C.right=w/2;C.top=h/2;C.bottom=-h/2;C.updateProjectionMatrix();
      var k=Math.max(w/IW,h/IH)*1.04;bw=IW*k;bh=IH*k;bx=0;by=-h/2+bh/2-bh*.01;bg.scale.set(bw,bh,1);
      hx.style.setProperty('--floor',Math.round((1-V0)*bh)+'px');uMin=.5-(w/bw)/2+.05;uMax=.5+(w/bw)/2-.05;H.forEach(function(o){if(!isFinite(o.u))o.u=.5;if(!isFinite(o.d))o.d=.5;if(!isFinite(o.tu))o.tu=o.u;o.u=Math.min(uMax,Math.max(uMin,o.u))})}
    function wx(u){return (u-.5)*bw+bx}function wy(v){return (.5-v)*bh+by}function vOf(y){return .5-(y-by)/bh}function uOf(x){return (x-bx)/bw+.5}
    function hh0(o){return Math.min(bh*(.115+.05*o.d),w*(.25+.07*o.d))}
    function bubble(o,txt){say.textContent=txt;say.classList.remove('on');void say.offsetWidth;say.classList.add('on');say._o=o;clearTimeout(say._t);say._t=setTimeout(function(){say.classList.remove('on');say._o=null},1600)}
    function pick(cx,cy){var r=st.getBoundingClientRect(),x=cx-r.left-w/2,y=h/2-(cy-r.top),best=null;
      H.forEach(function(o){if(o.mode==='drag')return;var hh=hh0(o),ww=hh*o.ar,px=o.m.position.x,py=o.m.position.y,top=py+(o.ko>.5?hh*.62:hh);
        if(Math.abs(x-px)<(o.ko>.5?hh*.62*o.arK/2:ww*.42)&&y>py&&y<top&&(!best||o.d>best.d))best=o});return best}
    function rnd(a,b){return a+Math.random()*(b-a)}
    function choose(o){var r=Math.random();
      if(r<.09){o.mode='run';o.path=[];var n=3+Math.floor(Math.random()*4);for(var k=0;k<n;k++)o.path.push([rnd(uMin,uMax),Math.random()]);if(Math.random()<.35)o.path.push([Math.random()<.5?uMin-.05:uMax+.05,Math.random()]);next(o)}
      else if(r<.14){var other=H[(o.i+1+Math.floor(Math.random()*2))%3];if(other.mode!=='drag'&&other.ko<.1){o.mode='chase';o.tgt=other;o.t=3+Math.random()*2}else{o.mode='idle';o.t=1}}
      else if(r<.26){o.mode='play';o.t=1.3}
      else if(r<.7){o.mode='walk';o.tu=rnd(uMin,uMax);o.td=Math.random()}
      else{o.mode='idle';o.t=2+Math.random()*3}}
    function next(o){var p=o.path.shift();if(!p){o.mode='idle';o.t=.6+Math.random();return}o.tu=p[0];o.td=p[1]}
    function knock(o,side){o.mode='ko';o.side=side;o.t=0;o.dizzy=2.4;o.ko=1;o.path=[];o.walk=0;bubble(o,'โอ๊ย!')}
    var mx=0,my=0,tx=0,ty=0,last=0,run=false,rq=0,grab=null,downAt=null;
    function local(e){var r=st.getBoundingClientRect();return [e.clientX-r.left-w/2,h/2-(e.clientY-r.top)]}
    hx.addEventListener('pointermove',function(e){var r=st.getBoundingClientRect();tx=(e.clientX-r.left)/r.width-.5;ty=(e.clientY-r.top)/r.height-.5;
      if(grab){var p=local(e);grab.gx=p[0];grab.gy=p[1];if(downAt&&Math.hypot(e.clientX-downAt[0],e.clientY-downAt[1])>6)downAt.moved=true}
      else cv.style.cursor=pick(e.clientX,e.clientY)?'grab':''});
    function down(e,cx,cy){if(e.target.closest&&e.target.closest('a,button'))return false;var o=pick(cx,cy);if(!o)return false;
      grab=o;var p=local({clientX:cx,clientY:cy});o.prevMode=o.mode;o.mode='drag';o.gx=o.pgx=p[0];o.gy=p[1];o.ang=0;o.av=0;o.cvx=0;downAt=[cx,cy];downAt.moved=false;cv.style.cursor='grabbing';return true}
    hx.addEventListener('pointerdown',function(e){if(e.pointerType==='touch')return;if(down(e,e.clientX,e.clientY)){window.__hxD=Date.now();e.preventDefault();try{hx.setPointerCapture(e.pointerId)}catch(_){} }});
    hx.addEventListener('touchstart',function(e){var t=e.touches[0];if(down(e,t.clientX,t.clientY)){window.__hxD=Date.now();e.preventDefault()}},{passive:false});
    hx.addEventListener('click',function(e){if(Date.now()-(window.__hxD||0)<1500){e.preventDefault();e.stopPropagation()}},true);
    hx.addEventListener('touchmove',function(e){if(!grab)return;e.preventDefault();var t=e.touches[0],p=local(t);grab.gx=p[0];grab.gy=p[1];if(Math.hypot(t.clientX-downAt[0],t.clientY-downAt[1])>6)downAt.moved=true},{passive:false});
    function release(){if(!grab)return;var o=grab;grab=null;cv.style.cursor='';var hh=hh0(o);
      if(!downAt.moved){o.ko=0;o.dizzy=0;o.mode='hop';o.vy=1;o.y=.001;bubble(o,o.line);puff(o.x,o.m.position.y+hh*.9,6,'spark');return}
      var fx=o.gx+Math.sin(o.ang)*hh,fy=o.gy-Math.cos(o.ang)*hh,v=vOf(fy);o.ko=0;o.dizzy=0;
      o.u=Math.min(uMax,Math.max(uMin,uOf(fx)));if(v>V0)o.d=Math.max(0,Math.min(1,(v-V0)/(V1-V0)));o.lift=Math.max(0,fy-wy(V0+(V1-V0)*o.d));o.vy=0;o.mode='fall';o.side=o.cvx>0?1:-1;o.spin=o.ang}
    addEventListener('pointerup',release);addEventListener('touchend',release);addEventListener('pointercancel',release);
    function step(t){rq=0;if(!run)return;var dt=Math.min(.04,(t-(last||t))/1000);last=t;mx+=(tx-mx)*.06;my+=(ty-my)*.06;
      bg.position.set(bx-mx*14,by+my*7,-50);
      H.forEach(function(o){var hh=hh0(o),ww=hh*o.ar,fast=o.mode==='run'||o.mode==='chase';
        if(o.mode==='idle'){o.t-=dt;o.walk*=.85;if(o.t<=0)choose(o)}
        else if(o.mode==='chase'){o.t-=dt;o.tu=o.tgt.u;o.td=o.tgt.d;if(o.t<=0||o.tgt.mode==='drag'){o.mode='idle';o.t=1}}
        if(o.mode==='walk'||o.mode==='run'||o.mode==='chase'){var du=o.tu-o.u,dd=o.td-o.d,dist=Math.hypot(du*1.6,dd*.45);
          var sp=(fast?.26:.085)*dt/Math.max(dist,1e-4);o.u+=du*Math.min(1,sp);o.d+=dd*Math.min(1,sp);if(Math.abs(du)>.001)o.face=du>0?1:-1;o.walk=Math.min(fast?1.6:1,o.walk+dt*5);
          if(fast){o.dust-=dt;if(o.dust<=0){o.dust=.16;puff(o.x-o.face*ww*.55,o.m.position.y+hh*.02,1,'dust',.6);var lp=P.filter(function(q){return q.life>0&&q.kind==='dust'}).pop();if(lp)lp.ro=Math.round(o.d*100)+19}}
          if(o.u<uMin||o.u>uMax){o.u=Math.min(uMax,Math.max(uMin,o.u));if(fast){puff(o.x+o.face*ww*.4,o.m.position.y+hh*.55,7,'star');knock(o,-o.face)}else{o.mode='idle';o.t=1}}
          else if(o.mode==='chase'&&dist<.05){o.mode='play';o.t=1;if(o.tgt.mode!=='drag'&&o.tgt.ko<.1){o.tgt.mode='play';o.tgt.t=1}bubble(o,'จับได้แล้ว!')}
          else if(dist<.008){if(o.mode==='run')next(o);else if(o.mode==='walk'){o.mode='idle';o.t=.8+Math.random()*2}}}
        else if(o.mode==='play'){o.t-=dt;o.walk*=.8;if(o.y<=0&&o.vy<=0&&o.t>0){o.vy=.6;o.y=.001;puff(o.x,o.m.position.y+hh,2,'spark')}if(o.t<=0&&o.y<=0){o.mode='idle';o.t=1}}
        else if(o.mode==='ko'){o.t+=dt;o.dizzy=Math.max(0,o.dizzy-dt);if(o.dizzy<=0){o.mode='getup';o.ko=0;o.vy=.45;o.y=.001;puff(o.x,o.m.position.y,4,'dust')}}
        else if(o.mode==='getup'){if(o.y<=0&&o.vy<=0){o.mode='idle';o.t=.6}}
        else if(o.mode==='fall'){o.vy-=dt*bh*3.2;o.lift+=o.vy*dt;o.spin*=.9;if(o.lift<=0){var hard=o.vy<-bh*1.05;o.lift=0;o.sq=1;puff(o.x,o.m.position.y,hard?10:5,'dust',hard?1.4:.8);
            if(hard){puff(o.x,o.m.position.y+hh*.5,5,'star');knock(o,o.side)}else{o.mode='idle';o.t=.8;o.vy=.25;o.y=.001}}}
        else if(o.mode==='hop'){if(o.y<=0&&o.vy<=0){o.mode='idle';o.t=1}}
        if((o.y>0||o.vy>0)&&o.mode!=='fall'&&o.mode!=='drag'){o.y+=o.vy*dt*2.2;o.vy-=dt*2.6;if(o.y<=0){o.y=0;o.vy=0;o.sq=1}}
        o.sq=Math.max(0,o.sq-dt*5);o.ph+=dt*(fast?20:11)*Math.min(1,o.walk);
        var fx=wx(o.u)-mx*(26+18*o.d),floorY=wy(V0+(V1-V0)*o.d)+my*(7+5*o.d);o.x=fx;
        var drag=o.mode==='drag',ko=o.ko>.5;o.md.visible=drag;o.m.visible=!drag;
        if(drag){var ax=(o.gx-o.pgx)/Math.max(dt,1e-3);o.cvx=o.cvx*.7+ax*.3;o.pgx=o.gx;
          o.av+=(-Math.sin(o.ang)*30-o.av*3-o.cvx*.016)*dt;o.ang+=o.av*dt;o.ang=Math.max(-1.3,Math.min(1.3,o.ang));o.ft+=dt;
          var kick=Math.sin(o.ft*26)*.07,dh=hh*1.02,dw=dh*o.arD;
          o.md.position.set(o.gx,o.gy+dh*.06,3);o.md.rotation.z=o.ang+kick;o.md.scale.set(dw*(1+Math.sin(o.ft*26+1)*.04)*o.face,dh*(1+Math.abs(Math.sin(o.ft*13))*.05),1);
          o.s.position.set(o.gx,floorY,o.d-.01);o.s.scale.set(ww*.6,hh*.08,1);o.s.material.opacity=.45;o.x=o.gx;
          o.dust-=dt;if(o.dust<=0){o.dust=Math.abs(o.av)>3?.1:.5;puff(o.gx+(Math.random()-.5)*dw*.6,o.gy-dh*.15,1,Math.abs(o.av)>3?'spark':'sweat',.4)}}
        else{var lift=o.mode==='fall'?o.lift:o.y*hh*.45,bob=Math.abs(Math.sin(o.ph))*hh*.05*Math.min(1,o.walk),sq=o.sq;
          o.m.material.map=ko?o.tK:o.tN;
          if(ko){var kh=hh*.62*(1+Math.sin(t/260)*.03),kw=kh*o.arK;o.m.rotation.z=0;o.m.scale.set(kw*-o.side,kh,1);o.m.position.set(fx,floorY,o.d);
            o.s.position.set(fx,floorY+kh*.04,o.d-.01);o.s.scale.set(kw*.95,hh*.1,1)}
          else{var lean=fast?o.face*-.14:0;o.m.rotation.z=o.mode==='fall'?o.spin:lean+Math.sin(o.ph)*.06*Math.min(1,o.walk);
            o.m.scale.set(ww*o.face*(1+.1*sq),hh*(1-.12*sq-.04*Math.abs(Math.cos(o.ph))*Math.min(1,o.walk)),1);o.m.position.set(fx,floorY+lift+bob,o.d);
            o.s.position.set(fx,floorY,o.d-.01);o.s.scale.set(ww*.8*(1-Math.min(.6,lift/hh)),hh*.11,1)}
          o.m.renderOrder=Math.round(o.d*100)+20;o.s.material.opacity=1;o.s.renderOrder=10}
        var kh2=hh*.62,kw2=kh2*o.arK,headX=o.m.position.x+o.side*kw2*.27,headY=o.m.position.y+kh2*.82;
        o.st.forEach(function(q,k){q.visible=o.mode==='ko';if(!q.visible)return;var a=t/240+k*2.094;q.position.set(headX+Math.cos(a)*kw2*.17,headY+Math.sin(a)*kh2*.12,9);var s3=hh*.12*(.8+.25*Math.sin(a));q.scale.set(s3,s3,1);q.rotation.z=a*2});
        if(say._o===o){var hp=drag?[o.gx,o.gy+hh*.15]:ko?[headX,headY+hh*.1]:[o.m.position.x,o.m.position.y+hh];say.style.transform='translate('+(hp[0]+w/2+hh*.15)+'px,'+(h/2-hp[1])+'px)'}});
      P.forEach(function(p){if(p.life<=0)return;p.life-=dt;if(p.life<=0){p.m.visible=false;return}var k=1-p.life/p.max;
        p.x+=p.vx*dt;p.y+=p.vy*dt;p.vy-=(p.kind==='dust'?20:260)*dt;p.vx*=.96;p.r+=p.vr*dt;var s4=p.s0*(p.kind==='dust'?(k<.25?.4+k*2.4:1-(k-.25)*1.2):1-k*.5);
        p.m.position.set(p.x,p.y,10);p.m.renderOrder=p.kind==='dust'?(p.ro||15):400;p.m.scale.set(s4,s4,1);p.m.rotation.z=p.r;p.m.material.opacity=p.kind==='dust'?(k<.75?1:1-(k-.75)*4):1-k*k});
      R.render(S,C);rq=requestAnimationFrame(step)}
    function play(on){run=on&&!document.hidden;if(run&&!rq){last=0;rq=requestAnimationFrame(step)}}
    new ResizeObserver(function(){fit();if(!run)R.render(S,C)}).observe(st);fit();
    new IntersectionObserver(function(es){play(es[0].isIntersecting&&!reduce&&!!document.querySelector('[data-view="home"].on'))}).observe(hx);
    document.addEventListener('visibilitychange',function(){play(!document.hidden&&st.getBoundingClientRect().bottom>0)});
    if(reduce){run=true;setTimeout(function(){step(performance.now());run=false},600)}
    if(!reduce)setInterval(function(){if(!run||say._o)return;var c=H.filter(function(o){return o.mode!=='drag'&&o.mode!=='ko'&&o.mode!=='fall'});if(c.length){var o=c[Math.floor(Math.random()*c.length)];bubble(o,o.line)}},5200);
    window.__hh=H;})();

  (function(){function f(){var ms=new Date('2026-11-14T09:00:00+07:00')-new Date();if(ms<0)ms=0;var d=Math.floor(ms/864e5),h=Math.floor(ms/36e5)%24,m=Math.floor(ms/6e4)%60;
    [['#cdD',d],['#cdH',h],['#cdM',m]].forEach(function(x){var e=$(x[0]);if(e)e.textContent=x[1]})}f();setInterval(f,3e4)})();
  /* works: if nobody scrolls the feed, nudge it so it is obvious more is below */
  (function(){var feed=document.querySelector('.tk-feed');if(!feed||reduce)return;var moved=false;feed.addEventListener('scroll',function(){if(feed.scrollTop>40)moved=true},{passive:true});
    setInterval(function(){if(moved||!document.querySelector('[data-p="shorts"].on')||!document.querySelector('[data-view="works"].on'))return;feed.classList.remove('nudge');void feed.offsetWidth;feed.classList.add('nudge')},3800)})();

  /* Port Express status (starts 9 Nov 2569) */
  (function(){var n=new Date(),a=new Date('2026-11-09T00:00:00+07:00'),b=new Date('2027-01-10T00:00:00+07:00'),t=n<a?'รุ่นใหม่เริ่มเรียน 9 พ.ย. 2569':n<b?'รุ่นนี้กำลังเรียนอยู่ · เริ่ม 9 พ.ย. 2569':'ทัก LINE ถามรอบถัดไป';
    $$('.pxst').forEach(function(e){e.textContent=(e.classList.contains('blink')?'● ':'')+t})})();
  /* AFO tile: after the day it says so */
  (function(){if(new Date()>new Date('2026-11-14T18:00:00+07:00')){var t=$('#afoTag');if(t)t.textContent='เพิ่งจบไป';var c=$('#afoCd');if(c)c.style.display='none';var nv=$('#nvNext');if(nv)nv.textContent='ดูทั้งหมด'}})();

  /* showcase: Apple-style auto advance with progress bars */
  (function(){var sc=document.getElementById('sc');if(!sc)return;var sl=sc.querySelectorAll('.sl'),tb=sc.querySelectorAll('.sc-nav button'),i=0;
    function go(n){i=(n+sl.length)%sl.length;sl.forEach(function(e,k){e.classList.toggle('on',k===i);var v=e.querySelector('video');if(v){if(k===i){v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){})}else v.pause()}});
      tb.forEach(function(b,k){b.setAttribute('aria-selected',String(k===i));var bar=b.querySelector('.bar');bar.style.animation='none';void bar.offsetWidth;bar.style.animation=''})}
    tb.forEach(function(b,k){b.addEventListener('click',function(){go(k)});b.querySelector('.bar').addEventListener('animationend',function(){if(k===i)go(i+1)})});
    sc.addEventListener('pointerenter',function(){sc.classList.add('hold')});sc.addEventListener('pointerleave',function(){sc.classList.remove('hold')});go(0)})();
  /* seniors: center-focus carousel that walks by itself */
  (function(){var st=document.getElementById('mcSt');if(!st)return;var on='',L=[],a=0,tm=0,hold=false;
    function build(){L=G.filter(function(g){return !on||g[2]===on});a=0;st.innerHTML=L.map(function(g,k){return '<figure class="mc-c" data-k="'+k+'"><img src="/Hamterco/img/dek69-'+g[0]+'.webp" alt="'+g[1]+' '+UN[g[2]]+'" loading="lazy"></figure>'}).join('');
      st.querySelectorAll('.mc-c').forEach(function(c){c.addEventListener('click',function(){go(+c.dataset.k)})});lay()}
    function lay(){var n=L.length,W=st.offsetWidth||1000,gap=Math.min(240,W*.2);st.querySelectorAll('.mc-c').forEach(function(c,k){var o=k-a;if(o>n/2)o-=n;if(o<-n/2)o+=n;var ab=Math.abs(o);
      c.style.transform='translate(-50%,-50%) translateX('+(o*gap)+'px) translateY('+(ab%2?28:0)+'px) scale('+(1-Math.min(ab,4)*.12)+')';c.style.zIndex=20-ab;c.style.opacity=ab>3?0:1;c.style.filter='brightness('+(1-Math.min(ab,3)*.18)+')';c.classList.toggle('on',o===0)});
      var g=L[a];document.getElementById('mcC').innerHTML='<b>'+g[1]+'</b> · '+g[3]+' · '+UN[g[2]]+'<small>จากคอร์ส '+g[4]+'</small>'}
    function go(k){a=(k+L.length)%L.length;lay();var bg=document.getElementById('mcBg');if(bg&&L[a]){bg.style.opacity=0;setTimeout(function(){bg.src='/Hamterco/img/dek69-'+L[a][0]+'.webp';bg.style.opacity=1},250)}clearInterval(tm);tm=setInterval(function(){if(!hold&&document.querySelector('[data-view="home"].on'))go(a+1)},2800)}
    st.addEventListener('pointerenter',function(){hold=true});st.addEventListener('pointerleave',function(){hold=false});
    
    document.querySelectorAll('.mc-u button').forEach(function(b){b.addEventListener('click',function(){on=b.dataset.u;document.querySelectorAll('.mc-u button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});build();go(0)})});
    addEventListener('resize',lay);build();go(0)})();
  /* TCAS timeline: mark where we are */
  (function(){var now=new Date(),li=document.querySelectorAll('.tl li'),k=-1;li.forEach(function(e,n){if(new Date(e.dataset.d+'T00:00:00+07:00')<=now)k=n});
    li.forEach(function(e,n){e.classList.toggle('done',n<k);e.classList.toggle('here',n===k+1)})})();
  /* feed volume: the sound button also holds a volume slider */
  (function(){var tk=document.querySelector('.yt .tk');if(!tk)return;var vol=.7;
    tk.querySelectorAll('.tk-mute').forEach(function(b){var w=document.createElement('span');w.className='tk-mw';b.parentNode.insertBefore(w,b);w.appendChild(b);
      var p=document.createElement('span');p.className='tk-vp';p.innerHTML='<input type="range" min="0" max="100" value="70" aria-label="ระดับเสียง">';w.appendChild(p);
      var r=p.querySelector('input');r.addEventListener('input',function(){vol=r.value/100;tk.querySelectorAll('video').forEach(function(v){v.volume=vol});tk.querySelectorAll('.tk-vp input').forEach(function(x){x.value=r.value});
        var on=b.getAttribute('aria-pressed')==='true';if(vol>0&&!on)b.click();if(vol===0&&on)b.click()})});
    tk.querySelectorAll('video').forEach(function(v){v.volume=vol})})();
  /* hero clip: the hamster says the course in four lines */
  (function(){var b=document.querySelector('.ov-bub');if(!b)return;var L=['เรียนทำเกมกับพี่ๆ 2 เดือน','ได้ผลงานจริง ใส่แฟ้มพอร์ต','ทันยื่นรอบ Portfolio','รุ่นพี่ติดแล้ว 48 คน ตาน้องบ้าง!'],k=0,S=document.getElementById('ovS'),N=document.getElementById('ovN');
    function go(){S.textContent=L[k];N.textContent=(k+1)+'/'+L.length;b.classList.remove('pop');void b.offsetWidth;b.classList.add('pop');k=(k+1)%L.length}go();setInterval(go,3200)})();
  /* hall of fame: one work on the stage at a time */
  (function(){var z=document.getElementById('hz');if(!z)return;var W=[["stressstrike", "StressStrike", "@วิน", "ชนะเลิศ OBEC Roboplayground"], ["phi-krahang", "ผีกระหัง", "@นนท์", ""], ["eugation-strike", "Eugation Strike", "@ไผ่", ""], ["slash-speed", "SLASH//SPEED", "@ดินสอ", ""], ["midnight-at-roadside", "Midnight at Roadside", "@Windy", ""], ["hot-hot-hot", "Hot Hot Hot", "@โอม", ""], ["apocalypis-building", "Apocalypis Building", "@ฟาร์", ""], ["escape-rolling", "Escape Rolling", "@เป๊ป", ""]],a=0,tm=0,hold=false;
    var img=document.getElementById('hzImg'),N=document.getElementById('hzN'),By=document.getElementById('hzBy'),Aw=document.getElementById('hzAw'),T=z.querySelectorAll('.hz-t');
    function show(k){a=(k+W.length)%W.length;var w=W[a];z.classList.remove('sw');void z.offsetWidth;z.classList.add('sw');
      setTimeout(function(){img.src='/Hamterco/img/work-'+w[0]+'.webp';N.textContent=w[1];By.textContent='เกมที่น้อง '+w[2]+' สร้างเอง';Aw.textContent=w[3];Aw.style.display=w[3]?'':'none'},260);
      T.forEach(function(t,n){t.classList.toggle('on',n===a)});clearTimeout(tm);tm=setTimeout(tick,4200)}
    function tick(){if(hold||!document.querySelector('[data-view="home"].on')){tm=setTimeout(tick,600);return}show(a+1)}
    T.forEach(function(t){t.addEventListener('click',function(){show(+t.dataset.k)})});
    z.addEventListener('pointerenter',function(){hold=true});z.addEventListener('pointerleave',function(){hold=false});show(0)})();
  (function(){var n=document.querySelectorAll(".er").length,e=document.getElementById("axN");if(e&&n)e.textContent=n})();
  /* walking hamsters: waddle walk, grabbed pose, dizzy after a high drop */
  (function(){document.querySelectorAll('.wkz').forEach(function(z){var h=z.querySelector('.wk');if(!h)return;var base=h.getAttribute('src'),D=base.replace('.webp','-d.webp'),K=base.replace('.webp','-k.webp');
      [D,K].forEach(function(u){var i=new Image();i.src=u});
      var sh=document.createElement('i');sh.className='wk-sh';z.insertBefore(sh,h);
      var cw=z.clientWidth,hw=h.offsetWidth||60;new ResizeObserver(function(){cw=z.clientWidth;hw=h.offsetWidth||hw}).observe(z);
      var x=Math.random()*200,y=0,vy=0,dir=1,sp=.55+Math.random()*.25,drag=null,pause=0,seen=false,px=0,ang=0,av=0,ph=0,ko=0,peak=0;
      function pose(p){var u=p==='d'?D:p==='k'?K:base;if(h.getAttribute('src')!==u)h.setAttribute('src',u);h.classList.toggle('ko',p==='k')}
      var rq=0;new IntersectionObserver(function(e){seen=e[0].isIntersecting;if(seen&&!rq)rq=requestAnimationFrame(step)}).observe(z);
      function step(now){var W=cw-hw;if(seen&&W>0){var walking=false,rot=0,bob=0,sq=1;
        if(drag){var vx=x-px;av+=(-vx*1.8-ang)*.14;av*=.85;ang+=av;ang=Math.max(-40,Math.min(40,ang));rot=ang+Math.sin(now/55)*5}
        else if(y<0||vy){vy+=0.9;y+=vy;peak=Math.min(peak,y);rot=ang*=.9;if(y>=0){y=0;var hard=peak<-90;vy=vy>6?-vy*.3:0;
            if(!vy){peak=0;h.classList.remove('land');void h.offsetWidth;h.classList.add('land');if(hard){ko=110;pose('k')}else pose('n')}}}
        else if(ko>0){ko--;if(!ko){pose('n');h.classList.remove('land');void h.offsetWidth;h.classList.add('land')}}
        else if(pause>0){pause--}
        else{x+=dir*sp;walking=true;if(x<0){x=0;dir=1}if(x>W){x=W;dir=-1}if(Math.random()<.004)pause=60+Math.random()*90}
        if(walking){ph+=sp*.16;rot=Math.sin(ph)*7;bob=-Math.abs(Math.sin(ph))*7;sq=1+Math.abs(Math.cos(ph))*.05}else if(!drag&&!y&&!ko){ang=0;rot=Math.sin(now/600)*1.5}
        px=x;var gy=z.__g?z.__g(x+hw/2):0;h.style.transform='translate('+x+'px,'+(y+bob+gy)+'px) rotate('+rot+'deg) scale('+dir/sq*sq+','+(1/sq)+') scaleX(1)';
        var lift=Math.min(1,-y/160);sh.style.transform='translate('+(x+hw/2)+'px,'+(z.__g?z.__g(x+hw/2):0)+'px) translateX(-50%) scale('+(1-lift*.55)*(walking?1-Math.abs(Math.sin(ph))*.15:1)+')';sh.style.opacity=1-lift*.6}
        rq=seen?requestAnimationFrame(step):0}
      rq=requestAnimationFrame(step);
      h.addEventListener('pointerdown',function(e){e.preventDefault();var r=z.getBoundingClientRect();drag={dx:e.clientX-r.left-x,dy:e.clientY-r.top-y};ko=0;pose('d');h.classList.add('held');h.classList.remove('land');try{h.setPointerCapture(e.pointerId)}catch(_){}});
      h.addEventListener('pointermove',function(e){if(!drag)return;var r=z.getBoundingClientRect();x=Math.max(0,Math.min(z.clientWidth-h.offsetWidth,e.clientX-r.left-drag.dx));y=Math.max(-240,Math.min(0,e.clientY-r.top-drag.dy))});
      function up(){if(!drag)return;drag=null;vy=0.1;peak=y;h.classList.remove('held');if(y>-4){pose('n')}}
      h.addEventListener('pointerup',up);h.addEventListener('pointercancel',up);
    })})();
  /* works: a clear "next" guide until they scroll once */
  (function(){var tk=document.querySelector('.yt .tk'),f=tk&&tk.querySelector('.tk-feed');if(!f)return;var g=document.createElement('button');g.type='button';g.className='tk-guide';
    g.innerHTML='เลื่อนลง หรือกดตรงนี้<br>เพื่อดูผลงานถัดไป <b>↓</b>';tk.appendChild(g);g.addEventListener('click',function(){f.scrollBy({top:f.clientHeight,behavior:'smooth'})});
    f.addEventListener('scroll',function(){if(f.scrollTop>40)g.classList.add('hide')},{passive:true})})();
  /* fit finder: ask before selling */
  (function(){var f=document.getElementById('fitQ'),r=document.getElementById('fitR');if(!f)return;
    f.addEventListener('change',function(){var d=new FormData(f),g=d.get('g'),p=d.get('p'),t=d.get('t');if(!g||!p||!t)return;
      var line='<a class="fb2" href="https://page.line.me/jkm4247u?openQrModal=true" target="_blank" rel="noopener">ทัก LINE ให้ทีมแนะนำ</a>';
      if(g==='m6'&&p!=='yes'&&(t==='game'||t==='any')){r.className='fit-r ok';r.innerHTML='<p class="fr-k">เหมาะกับน้อง</p><h3>Port Express</h3><p>น้องอยู่ ม.6 และยังต้องการผลงานใส่พอร์ต คอร์สนี้พาทำเกมของตัวเองใน 2 เดือน ทันยื่นรอบ Portfolio</p><p class="fr-p"><b>5,990 บาท</b> · เริ่ม 9 พ.ย. 2569</p><div class="fr-b"><a class="fb1" href="https://www.hamsterhub.co/portex-site/index.html" target="_blank" rel="noopener">ดูรายละเอียดและสมัครเรียน</a>'+line+'</div>'}
      else if(p==='yes'){r.className='fit-r';r.innerHTML='<p class="fr-k">น้องมีผลงานแล้ว</p><h3>ลองให้ทีมดูพอร์ตก่อน</h3><p>ทีมช่วยดูว่าผลงานที่มีพร้อมยื่นแล้วหรือยัง และควรเพิ่มอะไร</p><div class="fr-b">'+line+'</div>'}
      else{r.className='fit-r';r.innerHTML='<p class="fr-k">มีคอร์สที่เหมาะกว่า</p><h3>'+(t==='app'?'สายแอปและเว็บ':t==='iot'?'สาย IoT':'คอร์สปูพื้นฐาน')+'</h3><p>'+(g==='m45'?'น้องยังมีเวลาก่อนยื่น ทำผลงานใหญ่ขึ้นได้อีก':'คอร์สสายนี้เปิดเป็นรอบ')+' ทักทีมให้แนะนำรอบที่เหมาะกับน้อง</p><div class="fr-b">'+line+'</div>'}})})();
  /* router */
  var views=['home','courses','portex','activity','works','about'],menuBtn=$('#menuBtn'),drawer=$('#drawer');
  var titles={home:'Hamster Hub',courses:'คอร์ส | Hamster Hub',portex:'Port Express | Hamster Hub',activity:'กิจกรรม | Hamster Hub',works:'ผลงาน | Hamster Hub',about:'เกี่ยวกับเรา | Hamster Hub'};
  function show(){var h=(location.hash||'#home').slice(1);if(views.indexOf(h)<0)h='home';
    $$('[data-view]').forEach(function(v){v.classList.toggle('on',v.dataset.view===h)});
    $$('.nav-in a.v').forEach(function(a){if(a.getAttribute('href')==='#'+(h==='portex'?'courses':h))a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
    document.title=titles[h];drawer.hidden=true;menuBtn.setAttribute('aria-expanded','false');window.scrollTo(0,0);
    if(h==='works'){var pp=pendingPane||['shorts'];pendingPane=null;pane(pp[0]);if(pp[1]!=null)setTimeout(function(){var b=document.querySelector('.tk-index-btn[data-tk-go="'+(pp[1]+1)+'"]');if(b)b.click()},120)}
    $$('video[autoplay]').forEach(function(v){if(v.closest('[data-view].on')){var p=v.play();if(p&&p.catch)p.catch(function(){})}else v.pause()});
    arm()}
  menuBtn.addEventListener('click',function(){var o=drawer.hidden;drawer.hidden=!o;menuBtn.setAttribute('aria-expanded',String(o))});
  var lastXY=[innerWidth/2,innerHeight/2];document.addEventListener('pointerdown',function(e){lastXY=[e.clientX,e.clientY]},true);
  var pt=document.getElementById('pt'),ptT=0;
  var PTC={courses:1,portex:1,activity:1,works:1,about:1};
  function ptBuild(v){var h='';
    if(v==='courses'){h='<span class="cv a"></span><span class="cv b"></span><b class="cv-t">คอร์ส</b>'}
    else if(v==='portex'){var c=14,r=8;for(var y=0;y<r;y++)for(var x=0;x<c;x++)h+='<i style="left:'+(x*100/c)+'%;top:'+(y*100/r)+'%;width:'+(100/c+.2)+'%;height:'+(100/r+.2)+'%;--dl:'+(Math.random()*.32).toFixed(2)+'s"></i>';h+='<b class="pt-px">LOADING...</b>'}
    else if(v==='activity'){var nx=document.getElementById('nvNext'),x0=lastXY[0],y0=lastXY[1],ST=['ev-st0','ev-st1','ev-st2','ev-st3','ev-st4','ev-st5','ev-st1','ev-st4','ev-st0','ev-st5'];h='<span class="ev-w"><span class="ev-c a" style="--x:'+x0+'px;--y:'+y0+'px"></span><span class="ev-c b" style="--x:'+x0+'px;--y:'+y0+'px"></span>';
      for(var k=0;k<6;k++){var an=k/6*6.283+.5+Math.random()*.4,d=34+Math.random()*10;h+='<img class="ev-s" src="/Hamterco/img/'+ST[k]+'.webp" alt="" style="--tx:'+(Math.cos(an)*d).toFixed(1)+'vmin;--ty:'+(Math.sin(an)*d*.8).toFixed(1)+'vmin;--rot:'+(Math.random()*40-20).toFixed(0)+'deg;--dl:'+(.3+k*.025).toFixed(3)+'s">'}
      h+='<span class="ev-t"><small>'+(nx?nx.textContent:'')+'</small><b>กิจกรรม</b></span></span>'}
    else if(v==='works'){h='<span class="t5-cu l"></span><span class="t5-cu r"></span><span class="t5-sp"></span>';for(var k=0;k<22;k++)h+='<span class="t5-d" style="left:'+(25+Math.random()*50).toFixed(1)+'%;top:'+(20+Math.random()*60).toFixed(1)+'%;--dl:'+(Math.random()*.6).toFixed(2)+'s;--s:'+(2+Math.random()*4).toFixed(1)+'px"></span>';h+='<span class="t5-fl"></span><img class="t5-tr" src="/Hamterco/img/n-win.webp" alt=""><b class="t5-hof"><small>HAMSTER HUB · CLASS OF 2026</small><span>HALL OF FAME</span></b>'}
    else if(v==='about'){h='<span class="pt-band"></span><img class="pt-run" src="/Hamterco/img/n-walker.webp" alt="">'}
    else{h='<span class="ph-p a"></span><span class="ph-p b"></span><span class="ph-p c"></span><span class="ph-c"><img src="/Hamterco/img/logo.webp" alt=""><b><span class="ph-l" style="--k:0">H</span><span class="ph-l" style="--k:1">a</span><span class="ph-l" style="--k:2">m</span><span class="ph-l" style="--k:3">s</span><span class="ph-l" style="--k:4">t</span><span class="ph-l" style="--k:5">e</span><span class="ph-l" style="--k:6">r</span><span class="ph-l" style="--k:7">&nbsp;</span><span class="ph-l" style="--k:8">H</span><span class="ph-l" style="--k:9">u</span><span class="ph-l" style="--k:10">b</span></b></span>'}
    pt.className='pt v-'+v;pt.innerHTML=h;void pt.offsetWidth;pt.classList.add('in')}
  var first=true;function route(){var v=(location.hash||'#home').slice(1);if(views.indexOf(v)<0)v='home';
    if(first||reduce){first=false;show();return}
    clearTimeout(ptT);ptBuild(v);var hold={home:1150,courses:750,portex:760,activity:850,works:1050,about:700}[v]||620;ptT=setTimeout(function(){show();var vw=document.querySelector('[data-view].on');if(vw&&PTC[v]){vw.classList.remove('pg-in');void vw.offsetWidth;vw.classList.add('pg-in')}pt.classList.add('out');ptT=setTimeout(function(){pt.className='pt';pt.innerHTML=''},1150)},hold)}
  addEventListener('hashchange',route);route();
})();
