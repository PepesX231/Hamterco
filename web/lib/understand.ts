// Reads what a visitor typed in the home search, however they typed it (Thai, English, romanised Thai, slang,
// typos, no spaces, the wrong keyboard layout), and names the topic. The legacy search engine answers first;
// when it gives up, the home bar asks it again with the canonical question below (see Hero.ask).

export type Intent = {
  id: string;
  ask: string | null; // canonical question the legacy engine answers well; null = answered by Hams Route matches
  routes?: string; // words handed to findForGoal so the right Routes show under the answer
  words: string[];
};

// Order = priority when a message names several topics: concrete things to build first, then money and time,
// then who the student is.
export const INTENTS: Intent[] = [
  { id: "express", ask: "Port Express", routes: "เกม พอร์ต", words: ["portexpress", "พอร์ตเอ็กซ์เพรส", "พอทเอ็กเพรส", "พอร์ตเอกเพรส", "express", "เอ็กซ์เพรส", "เอ็กเพรส"] },
  { id: "build", ask: null, routes: "build skill", words: ["projectbuild", "buildskill", "บิลด์สกิล", "บิ้วสกิล", "บิวสกิล", "12เดือน", "สิบสองเดือน", "ทั้งปี", "1ปี", "หนึ่งปี", "ระยะยาว", "โปรเจกต์หลัก", "yearlong", "12months", "oneyear"] },
  { id: "motion", ask: null, routes: "3d animation", words: ["3d", "3มิติ", "สามมิติ", "blender", "เบลนเดอร์", "เบลนเดอ", "เบรนเดอร์", "บลันเดอร์", "โมเดล3d", "ปั้นโมเดล", "ปั้นตัวละคร", "แอนิเมชัน", "แอนิเมชั่น", "อนิเมชัน", "อนิเมชั่น", "อะนิเมชัน", "แอนิเมท", "อนิเมท", "animation", "animate", "anime", "อนิเมะ", "การ์ตูน", "cartoon", "ตัวละคร", "character", "rig", "ริก", "ริ๊ก", "vfx", "เอฟเฟกต์", "เอฟเฟค", "เอฟเฟ็กต์", "effect", "maya", "มายา", "zbrush", "sculpt", "โมชัน", "โมชั่น", "motion"] },
  { id: "game", ask: "อยากทำเกม", routes: "เกม", words: ["เกม", "เกมส์", "เกมม์", "เกมมิ่ง", "gem", "game", "games", "gaming", "gamedev", "unity", "ยูนิตี้", "ยูนิตี", "ยูนิตตี้", "roblox", "โรบล็อกซ์", "โรบล็อก", "โรบอก", "โรบล๊อก", "godot", "โกดอท", "minecraft", "มายคราฟ", "มายคราฟต์", "unreal", "อันเรียล", "ด่าน", "เลเวล", "level", "เพลย์เทส", "playtest", "steam", "สตีม", "itch.io", "itchio", "เกมเมอร์", "gamer", "สตรีมเมอร์", "ทำเกม", "สร้างเกม", "ออกแบบเกม", "เขียนเกม"] },
  { id: "ai", ask: "อยากใช้ AI สร้างผลงาน", routes: "โค้ด", words: ["ai", "เอไอ", "เอ.ไอ", "ปัญญาประดิษฐ์", "chatgpt", "แชทจีพีที", "แชตจีพีที", "gpt", "gemini", "เจมินี", "claude", "คลอด", "machinelearning", "แมชชีนเลิร์นนิง", "deeplearning", "ml", "llm", "prompt", "พรอมต์", "พร้อมท์", "หุ่นยนต์คุย", "chatbot", "แชทบอท"] },
  { id: "iot", ask: "อยากทำ IoT หรือหุ่นยนต์", routes: "iot", words: ["iot", "ไอโอที", "ไอโอที", "arduino", "อาดูโน่", "อาดูโน", "อาร์ดูโน่", "หุ่นยนต์", "หุ่นยน", "หุ่นยนตร์", "robot", "robotic", "โรบอท", "โรบอต", "วงจร", "circuit", "เซนเซอร์", "เซ็นเซอร์", "เซนเซอ", "sensor", "บอร์ด", "board", "esp32", "esp8266", "microbit", "ไมโครบิต", "ไมโครบิท", "raspberry", "ราสเบอร์รี่", "ไฟฟ้า", "อิเล็ก", "อิเล็กทรอนิกส์", "electronic", "smarthome", "สมาร์ทโฮม", "โดรน", "drone", "ฮาร์ดแวร์", "hardware", "ต่อวงจร", "บัดกรี"] },
  { id: "web", ask: "อยากทำเว็บหรือแอป", routes: "เว็บ แอป", words: ["เว็บ", "เวบ", "เว็ป", "เวป", "เว็บไซต์", "เว็บไซท์", "เวปไซต์", "เว็ปไซต์", "web", "website", "webapp", "html", "css", "javascript", "js", "react", "nextjs", "node", "frontend", "backend", "ฟรอนต์เอนด์", "แบ็กเอนด์", "แบคเอนด์", "fullstack", "ฟูลสแตก", "api", "database", "ฐานข้อมูล", "หน้าเว็บ", "ร้านค้าออนไลน์", "แอป", "แอพ", "แอฟ", "แอ๊ป", "app", "apps", "application", "แอปพลิเคชัน", "แอพพลิเคชั่น", "แอปมือถือ", "แอพมือถือ", "mobileapp", "flutter", "ฟลัตเตอร์", "ios", "android", "แอนดรอยด์", "ui", "ux", "uxui", "uiux", "figma", "ฟิกมา", "ออกแบบหน้าจอ", "ออกแบบแอป", "prototype", "โปรโตไทป์", "ต้นแบบ"] },
  { id: "compete", ask: "อยากส่งผลงานแข่ง", routes: "แข่ง", words: ["แข่ง", "แข่งขัน", "ลงแข่ง", "ส่งแข่ง", "ประกวด", "รางวัล", "เวที", "nsc", "เอ็นเอสซี", "depa", "ดีป้า", "tggs", "ทีจีจีเอส", "hackathon", "แฮกกาธอน", "แฮคกาธอน", "แฮกกะธอน", "gamejam", "เกมแจม", "ggj", "olympiad", "โอลิมปิก", "สอวน", "competition", "contest", "compete", "award", "แชมป์", "champion", "ชนะเลิศ", "เหรียญ", "ytsf", "บอร์ดเกม"] },
  { id: "camp", ask: "ค่ายและกิจกรรม", words: ["ค่าย", "แคมป์", "แคมป", "camp", "workshop", "เวิร์กชอป", "เวิร์คช็อป", "เวิร์คชอป", "ปิดเทอม", "ซัมเมอร์", "summer", "กิจกรรม", "อีเวนต์", "อีเว้นท์", "event", "allforone", "ออลฟอร์วัน", "openhouse", "โอเพนเฮาส์", "วันเดียวจบ", "ทดลองทำ"] },
  { id: "biz", ask: "อยากทำธุรกิจหรือสตาร์ทอัพ", routes: "ไอเดีย สตาร์ทอัพ", words: ["ธุรกิจ", "ธุระกิจ", "สตาร์ทอัพ", "สตาร์ตอัป", "สตาทอัพ", "สตาร์ทอัป", "startup", "startups", "business", "บิสซิเนส", "หาเงิน", "ทำเงิน", "รวย", "เศรษฐี", "rich", "รายได้", "ขายของ", "ขายได้", "makemoney", "money", "ผู้ประกอบการ", "entrepreneur", "เจ้าของกิจการ", "pitch", "พิช", "พิทช์", "นำเสนอ", "นักลงทุน", "investor", "ระดมทุน", "ไอเดีย", "idea", "ลูกค้า", "คนใช้จริง", "validate", "mvp"] },
  { id: "works", ask: "ดูผลงาน", words: ["ผลงานน้อง", "ผลงานนักเรียน", "ผลงานเด็ก", "ผลงานรุ่นพี่", "ตัวอย่างผลงาน", "ตัวอย่างงาน", "ดูผลงาน", "ขอดูผลงาน", "เกมที่น้อง", "เกมของน้อง", "halloffame", "ฮอลล์ออฟเฟม", "ฮอลออฟเฟม", "showcase", "portfolioexample", "ผลงานที่ผ่านมา", "เคยทำอะไร", "ทำอะไรมาบ้าง", "ใครเคยได้รางวัล", "ศิษย์เก่า", "alumni", "mrcity", "hamsterquest", "hamstermap", "phcmap", "karma", "revoice"] },
  { id: "price", ask: "ค่าเรียนเท่าไหร่", words: ["ราคา", "ราคาเท่าไหร่", "ค่าเรียน", "ค่าคอร์ส", "ค่าคอส", "ค่าเทอม", "ค่าสมัคร", "ค่าใช้จ่าย", "เท่าไหร่", "เท่าไร", "เท่าไห่", "เท่าหร่", "เท่าไหน", "เท่าใด", "เท่าไหล่", "กี่บาท", "กี่ตัง", "กี่ตังค์", "ตังค์", "แพง", "แพงไหม", "ถูกไหม", "ผ่อน", "ผ่อนได้", "แบ่งจ่าย", "จ่ายเป็นงวด", "ส่วนลด", "ลดราคา", "โปรไหม", "โปรมั้ย", "โปรป่าว", "โปรปะ", "โปรลด", "โปรพิเศษ", "early bird", "earlybird", "โปรโมชั่น", "โปรโมชัน", "คูปอง", "ฟรี", "ไม่เสียเงิน", "จ่าย", "ชำระ", "โอนเงิน", "บาท", "price", "prices", "pricing", "cost", "costs", "fee", "fees", "tuition", "howmuch", "discount", "promo", "installment", "free", "baht", "raka", "kharian", "thaorai", "taorai", "เรทราคา", "งบ", "budget", "ทุน", "scholarship", "ทุนการศึกษา"] },
  { id: "apply", ask: "เรียนวันไหน สมัครยังไง", words: ["สมัคร", "สมัก", "ลงทะเบียน", "ลงชื่อ", "จองที่", "จองรอบ", "จอง", "เข้าร่วม", "register", "registration", "signup", "apply", "enroll", "enrol", "booking", "book", "samak", "รับสมัคร", "ปิดรับ", "เปิดรับ", "รับกี่คน", "ที่นั่ง", "เต็มยัง", "ยังว่าง"] },
  { id: "when", ask: "เรียนวันไหน สมัครยังไง", words: ["วันไหน", "วันอะไร", "กี่โมง", "ตาราง", "ตารางเรียน", "เวลาเรียน", "เรียนกี่วัน", "เรียนกี่ครั้ง", "เรียนกี่ชั่วโมง", "กี่ชั่วโมง", "กี่เดือน", "กี่สัปดาห์", "กี่อาทิตย์", "นานไหม", "นานแค่ไหน", "ระยะเวลา", "ใช้เวลา", "เปิดรอบ", "รอบหน้า", "รอบถัดไป", "รอบใหม่", "เปิดเมื่อไหร่", "เริ่มเมื่อไหร่", "เริ่มเรียน", "เริ่มวันไหน", "จบเมื่อไหร่", "เมื่อไหร่", "เมื่อไร", "ตอนไหน", "เสาร์อาทิตย์", "เสาร์", "อาทิตย์", "วันหยุด", "ตอนเย็น", "หลังเลิกเรียน", "ช่วงไหน", "ที่ไหน", "ที่อยู่", "สถานที่", "อยู่ตรงไหน", "อยู่แถวไหน", "แผนที่", "ไปยังไง", "เดินทาง", "bts", "mrt", "ออนไลน์", "online", "ออนไซต์", "onsite", "zoom", "ซูม", "เรียนที่บ้าน", "สาขา", "schedule", "timetable", "when", "where", "location", "duration", "howlong"] },
  { id: "contact", ask: "ติดต่อทีม", words: ["ติดต่อ", "ติดต่อยังไง", "line", "ไลน์", "ไลน", "แอดไลน์", "เบอร์", "เบอร์โทร", "โทร", "โทรศัพท์", "เพจ", "facebook", "เฟส", "เฟซบุ๊ก", "เฟสบุ๊ค", "ig", "ไอจี", "instagram", "อินสตา", "tiktok", "ติ๊กต๊อก", "youtube", "ยูทูป", "อีเมล", "อีเมล์", "email", "แอดมิน", "admin", "คุยกับคน", "คุยกับทีม", "คุยกับพี่", "ถามทีม", "contact", "ทดลองเรียน", "เรียนฟรีก่อน", "ลองเรียน", "trial", "ใบประกาศ", "ใบเซอร์", "เซอร์", "certificate", "คืนเงิน", "refund", "ยกเลิก", "เลื่อนเรียน", "ขาดเรียน", "เรียนชดเชย", "ต้องมีคอม", "ต้องมีโน้ตบุ๊ก", "โน้ตบุ๊ก", "โน๊ตบุ๊ค", "notebook", "laptop", "แล็ปท็อป", "ipad", "ไอแพด", "แมค", "mac", "สเปค", "spec", "ห้องละกี่คน", "กี่คนต่อห้อง", "เรียนกี่คน", "ครูกี่คน", "ตัวต่อตัว", "เรียนเดี่ยว", "private"] },
  { id: "about", ask: "Hamster Hub คืออะไร", words: ["hamsterhub", "hamster", "hamter", "แฮมสเตอร์", "แฮมเตอร์", "แฮมสเตอ", "แฮมสเต้อ", "แฮมสเตอร์ฮับ", "แฮม", "ฮับ", "hub", "คืออะไร", "ที่นี่คือ", "ที่นี่สอน", "สอนอะไร", "สอนอะไรบ้าง", "มีอะไรบ้าง", "มีคอร์สอะไร", "คอร์สอะไร", "คอร์ส", "คอส", "course", "courses", "class", "คลาส", "หลักสูตร", "เรียนอะไร", "เกี่ยวกับ", "เป็นใคร", "น่าเชื่อถือ", "เชื่อถือได้", "โกง", "scam", "รีวิว", "review", "ครู", "อาจารย์", "ผู้สอน", "ใครสอน", "พี่ๆที่สอน", "mentor", "เมนเทอร์", "โค้ช", "coach", "about", "สถาบัน", "บริษัท", "route", "routes", "เรท", "แพ็กเกจ", "แพคเกจ", "แพ็คเกจ", "package"] },
  { id: "eng", ask: "อยากเข้าวิศวะคอม", words: ["วิศวะ", "วิศว", "วิดวะ", "วิสวะ", "วิศวกร", "วิศวกรรม", "คอมเอ็น", "cedt", "ซีอีดีที", "engineering", "engineer", "cpe", "comeng", "wissawa", "witsawa"] },
  { id: "cs", ask: "อยากเข้าวิทย์คอม", words: ["วิทย์คอม", "วิทยาการคอม", "วิทยาการคอมพิวเตอร์", "ไอที", "ict", "cs", "computerscience", "compsci", "datascience", "ดาต้าไซแอนซ์", "ซอฟต์แวร์", "ซอฟแวร์", "software", "โปรแกรมเมอร์", "programmer", "developer", "ดีเวลอปเปอร์", "dev", "คอมพิวเตอร์", "คอมพิว", "computer", "คอม"] },
  { id: "med", ask: "อยากเข้าแพทย์", words: ["หมอ", "แพทย์", "แพทย", "เภสัช", "พยาบาล", "ทันตะ", "ทันตแพทย์", "สัตวแพทย์", "medical", "medicine", "doctor"] },
  { id: "uni", ask: "อยากมีพอร์ตยื่นมหาลัย", words: ["จุฬา", "จุฬาฯ", "chula", "มหิดล", "mahidol", "เกษตร", "kasetsart", "สจล", "ลาดกระบัง", "พระจอม", "kmitl", "บางมด", "kmutt", "ธรรมศาสตร์", "thammasat", "เชียงใหม่", "ขอนแก่น", "ศิลปากร", "ศรีนครินทร์", "มศว", "ม.เกษตร", "สงขลานครินทร์"] },
  { id: "code", ask: "เริ่มจากศูนย์ได้ไหม", routes: "โค้ด", words: ["โค้ด", "โค๊ด", "โค้ดดิ้ง", "โค๊ดดิ้ง", "code", "coding", "coder", "เขียนโค้ด", "เขียนโปรแกรม", "เขียนโปรแกม", "โปรแกรมมิ่ง", "โปรแกรมมิง", "programming", "program", "โปรแกรม", "โปรแกม", "python", "ไพทอน", "ไพธอน", "ไพท่อน", "ไพตอน", "java", "จาวา", "javascript", "c++", "c#", "ซีชาร์ป", "ภาษาซี", "scratch", "สแครช", "algorithm", "อัลกอริทึม", "logic", "ตรรกะ", "loop", "ลูป"] },
  { id: "beginner", ask: "เริ่มจากศูนย์ได้ไหม", routes: "เริ่ม", words: ["มือใหม่", "มือใหม", "ไม่เคย", "ไม่เคยเรียน", "ไม่เคยเขียน", "ไม่มีพื้นฐาน", "ไม่มีพื้น", "ไม่มีความรู้", "ไม่รู้อะไรเลย", "ไม่เป็นเลย", "เริ่มจากศูนย์", "เริ่มศูนย์", "ศูนย์", "จาก0", "เริ่มจาก0", "เริ่มต้น", "พื้นฐาน", "เบื้องต้น", "ไม่เก่ง", "เรียนไม่เก่ง", "ไม่ฉลาด", "โง่", "หัวช้า", "ตามไม่ทัน", "ตามทัน", "ยากไหม", "ยากมั้ย", "ยากป่าว", "ยากรึเปล่า", "ง่ายไหม", "เรียนรู้เรื่อง", "เริ่มยังไง", "เริ่มตรงไหน", "เริ่มจากไหน", "เริ่มอะไรก่อน", "ควรเริ่ม", "ชิ้นแรก", "beginner", "beginners", "newbie", "noob", "fromzero", "fromscratch", "basic", "basics", "starter", "noexperience"] },
  { id: "port", ask: "อยากมีพอร์ตยื่นมหาลัย", routes: "พอร์ต", words: ["พอร์ต", "พอต", "พอท", "พอร์ท", "พอร์ตโฟลิโอ", "พอร์ตฟอลิโอ", "portfolio", "portfolios", "port", "tcas", "ทีแคส", "tcas70", "dek70", "dek71", "ยื่นพอร์ต", "ยื่นมหาลัย", "ยื่น", "มหาลัย", "มหาวิทยาลัย", "มหาลัยไหน", "มหาลัยดี", "ม.ลัย", "university", "uni", "college", "admission", "ติดมหา", "ติดมหาลัย", "เข้ามหา", "เข้ามหาลัย", "รอบ1", "รอบพอร์ต", "รอบแฟ้ม", "แฟ้ม", "แฟ้มสะสมผลงาน", "สัมภาษณ์", "interview", "คณะ", "faculty", "ผลงาน", "ผลงานใส่พอร์ต", "ไม่มีผลงาน", "มีผลงาน"] },
  { id: "m6", ask: "น้อง ม.6", routes: "พอร์ต", words: ["ม6", "ม.6", "มหก", "ม.หก", "มัธยม6", "มัธยมหก", "grade12", "m6", "dek70", "เด็ก70", "ปีสุดท้าย", "ใกล้ยื่น", "เหลือเวลาน้อย", "ไม่ทันแล้ว", "ทันไหม"] },
  { id: "m45", ask: "น้อง ม.4–5", words: ["ม4", "ม5", "ม.4", "ม.5", "มสี่", "มห้า", "ม.สี่", "ม.ห้า", "มัธยม4", "มัธยม5", "grade10", "grade11", "m4", "m5", "เด็ก71", "เด็ก72", "ม.ปลาย", "มปลาย", "มัธยมปลาย"] },
  { id: "m13", ask: "น้อง ม.ต้น", words: ["ม1", "ม2", "ม3", "ม.1", "ม.2", "ม.3", "ม.ต้น", "มต้น", "มัธยมต้น", "ประถม", "ป6", "ป5", "ป4", "ป.6", "ป.5", "ป.4", "เด็กเล็ก", "กี่ขวบ", "อายุเท่าไหร่", "อายุกี่ปี", "อายุ", "เด็กประถม", "juniorhigh", "middleschool", "primary"] },
  { id: "parent", ask: "ผู้ปกครอง ลูกจะได้อะไร", words: ["ผู้ปกครอง", "ผปค", "ผู้ปก", "ลูก", "ลูกชาย", "ลูกสาว", "หลาน", "พ่อแม่", "คุณแม่", "คุณพ่อ", "แม่", "พ่อ", "parent", "parents", "myson", "mydaughter", "mykid", "mychild", "ได้อะไร", "คุ้มไหม", "คุ้มมั้ย", "คุ้มค่า", "ดีไหม", "ดีมั้ย", "ดียังไง", "ช่วยอะไร", "ประโยชน์"] },
];

// ---------- text helpers ----------
const EN = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?";
const TH = "_ๅ/-ภถุึคตจขชๆไำพะัีรนยบลฃฟหกดเ้่าสวงผปแอิืทมใฝ%+๑๒๓๔ู฿๕๖๗๘๙๐\"ฎฑธํ๊ณฯญฐ,ฅฤฆฏโฌ็๋ษศซ.()ฉฮฺ์?ฒฬฦ";
export function swapKb(t: string, toThai: boolean) {
  const a = toThai ? EN : TH, b = toThai ? TH : EN;
  let o = "";
  for (const ch of t) { const k = toThai && /[0-9]/.test(ch) ? -1 : a.indexOf(ch); o += k > -1 ? b[k] : ch; }
  return o;
}
const THDIGIT = "๐๑๒๓๔๕๖๗๘๙";
export function norm(raw: string) {
  let s = String(raw || "").slice(0, 300);
  try { s = s.normalize("NFC"); } catch {}
  s = s.replace(/[！-～]/g, (c) => String.fromCharCode(c.charCodeAt(0) - 0xfee0));
  s = s.replace(/[๐-๙]/g, (c) => String(THDIGIT.indexOf(c)));
  s = s.toLowerCase().replace(/เเ/g, "แ").replace(/ํา/g, "ำ").replace(/([่-๋])([ัิ-ู])/g, "$2$1");
  s = s.replace(/([ัิ-ู็-์])\1+/g, "$1").replace(/(.)\1{2,}/g, "$1"); // อยากกกก > อยาก
  return s.replace(/\s+/g, " ").trim();
}
// one comparable form: no spaces or punctuation, no tone marks (people mistype them most)
const flat = (s: string) => s.replace(/[\s"'“”‘’!?.,()\-_/ๆ~^*:;]+/g, "").replace(/[่-๋์็]/g, "");
function lev(a: string, b: string) {
  if (a === b) return 0;
  const m = a.length, n = b.length;
  if (!m || !n) return m || n;
  let pp: number[] = [], prev = Array.from({ length: n + 1 }, (_, j) => j);
  for (let i = 1; i <= m; i++) {
    const cur = [i];
    for (let j = 1; j <= n; j++) {
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) cur[j] = Math.min(cur[j], pp[j - 2] + 1);
    }
    pp = prev; prev = cur;
  }
  return prev[n];
}

type Key = { w: string; i: number; short: boolean };
let KEYS: Key[] | null = null;
function keys() {
  if (KEYS) return KEYS;
  KEYS = [];
  INTENTS.forEach((it, i) => it.words.forEach((w) => {
    const f = flat(norm(w));
    if (f) KEYS!.push({ w: f, i, short: /^[a-z0-9]{1,3}$/.test(f) });
  }));
  return KEYS;
}

function hit(text: string, fuzzy: boolean) {
  const f = flat(text);
  // whole Latin words, also when typed letter by letter ("a i") or glued to Thai ("vfxครับ", "ai555")
  const latinWords = new Set([...text.split(/[^a-z0-9+#]+/), ...(f.match(/[a-z0-9+#]+/g) || []), ...(f.match(/[a-z+#]+/g) || [])].filter(Boolean));
  const found = new Map<number, number>(); // intent index -> best keyword length
  for (const k of keys()) {
    // short Latin keywords (ai, it, ui, js, m6) only count as whole words, so "said" is not "ai"
    const ok = k.short ? latinWords.has(k.w) : f.includes(k.w);
    if (ok) found.set(k.i, Math.max(found.get(k.i) || 0, k.w.length));
  }
  if (!found.size && fuzzy) {
    // nearly-spelled keywords: one slip for 4–6 letters, two for longer words
    for (const k of keys()) {
      const L = k.w.length;
      if (L < 4) continue;
      const tol = L >= 7 ? 2 : 1;
      for (let len = L - tol; len <= L + tol; len++) {
        if (len < 3 || len > f.length) continue;
        let best = 99;
        for (let s = 0; s + len <= f.length && best > tol; s++) best = Math.min(best, lev(f.slice(s, s + len), k.w));
        if (best <= tol) { found.set(k.i, Math.max(found.get(k.i) || 0, L * 10 - best * 25)); break; }
      }
    }
  }
  return found;
}

export type Reading = { intent: Intent | null; others: Intent[]; text: string; swapped: boolean; mash: boolean };

const thaiShare = (s: string) => (s.match(/[ก-๛]/g) || []).length / Math.max(1, s.replace(/\s/g, "").length);
// Thai letters with no vowel, tone or final pattern at all usually come from typing English on a Thai keyboard
const looksMashedThai = (s: string) => /^[ก-ฮ\s]{2,}$/.test(s) && !/[ะ-ฺเ-ๅ็-์]/.test(s) && /^[a-z\s]+$/.test(swapKb(s, false));

export function understand(raw: string): Reading {
  const n = norm(raw);
  const tries: [string, boolean][] = [[n, false]];
  const th = thaiShare(n);
  if (th < 0.3 && /[a-z;'\[\],.]/.test(n)) tries.push([norm(swapKb(raw, true)), true]); // Thai typed on an English layout
  if (th > 0.5) tries.push([norm(swapKb(raw, false)), true]); // English typed on a Thai layout
  for (const fuzzy of [false, true]) {
    for (const [t, swapped] of tries) {
      const found = hit(t, fuzzy);
      if (!found.size) continue;
      // exact words: the list order decides; near-spellings: the closest, longest word decides
      const order = [...found.keys()].sort((a, b) => (fuzzy ? found.get(b)! - found.get(a)! : 0) || a - b);
      return { intent: INTENTS[order[0]], others: order.slice(1).map((i) => INTENTS[i]), text: t, swapped, mash: false };
    }
  }
  return { intent: null, others: [], text: n, swapped: false, mash: looksMashedThai(n) };
}
