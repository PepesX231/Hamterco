SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build64.py').read())
KW=r'''
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
'''
rep("    function intent(q){",KW+"    function intent(q){")
# use the forgiving matcher in search
rep("var I=intent(q);\n      if(I){R.hidden=false;$('#zqR').textContent='';G2.innerHTML='';A.innerHTML=ansH(I,q);A.hidden=false;R.scrollTop=0;return}",
    "var nq0=norm(q),TL=nq0.length>=5?IT.filter(function(x){var t=norm(x.t);return t.indexOf(nq0)===0||nq0.indexOf(t)>-1}):[];if(TL.length){A.hidden=true;A.innerHTML='';R.hidden=false;render(TL,'ผลลัพธ์สำหรับ “'+esc(q)+'”');return}"
    "var M=intent2(q);\n      if(M){var I=M.I;R.hidden=false;$('#zqR').textContent='';G2.innerHTML='';var pre='';"
    "if(M.via)pre+='<p class=\"ia-fix\">น้องอาจลืมเปลี่ยนภาษาแป้นพิมพ์ แสดงคำตอบสำหรับ “<b>'+esc(M.via)+'</b>”</p>';"
    "if(M.alts.length)pre+='<p class=\"ia-alt\"><span>หรือน้องหมายถึง</span>'+M.alts.map(function(i){return '<button type=\"button\" data-q=\"'+esc(KW[i][0])+'\">'+NAME[i]+'</button>'}).join('')+'</p>';"
    "A.innerHTML=pre+ansH(I,M.via||q);A.hidden=false;R.scrollTop=0;return}"
    "var nq=norm(q),P=[];if(nq.length<=2)KW.forEach(function(l,i){if(l.some(function(a){return norm(a).indexOf(nq)===0}))P.push(i)});"
    "if(P.length){R.hidden=false;$('#zqR').textContent='';G2.innerHTML='';A.innerHTML='<div class=\"ia\"><p class=\"ia-q\">น้องพิมพ์ “'+esc(q)+'”</p><h3>น้องหมายถึงเรื่องไหน</h3><p class=\"ia-alt ia-pick\">'+P.slice(0,8).map(function(i){return '<button type=\"button\" data-q=\"'+esc(KW[i][0])+'\">'+NAME[i]+'</button>'}).join('')+'</p></div>';A.hidden=false;return}")
CSS=r'''
/* v65 */
.ia-fix{margin:0 44px 10px 0;font-size:.88rem;color:#8A5A00;background:#FFF6DD;padding:8px 12px;border-radius:10px}
.ia-alt{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 44px 14px 0}
.ia-alt span{font:600 .85rem var(--display);color:#6A7891}
.ia-alt button{border:0;background:#EEF4FD;color:#1C5FC8;font:700 .86rem var(--display);padding:7px 12px;border-radius:10px;cursor:pointer;transition:background .2s}
.ia-alt button:hover{background:#DCE8FA}
.ia-pick{margin-top:14px!important}.ia-pick button{font-size:.95rem;padding:10px 14px}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v65.html','w').write(s)
print('v65 ok')
