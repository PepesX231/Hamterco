// Pictures and clips are shared with the old site, so they are read from the repo's img/ folder instead of being copied.
export const img = (name: string) => `/Hamterco/img/${name}`;
export const OLD_SITE = "/Hamterco/slime.html";
export const LINE_URL = "https://page.line.me/jkm4247u?openQrModal=true";
export const LOGIN_URL = "https://www.hamsterhub.co/login";

export const NAV = [
  { label: "คอร์ส", href: `${OLD_SITE}#courses` },
  { label: "กิจกรรม", href: `${OLD_SITE}#activity` },
  { label: "ผลงาน", href: `${OLD_SITE}#works` },
  { label: "เกี่ยวกับเรา", href: `${OLD_SITE}#about` },
] as const;

// The headline types "น้องอยาก… <wish>". Same list as the current site.
export const WISHES = [
  "ยื่นพอร์ตเข้ามหาลัย",
  "เข้าวิศวะคอม",
  "สร้างเกมของตัวเอง",
  "ทำแอปของตัวเอง",
  "ติด CEDT จุฬาฯ",
  "สร้างสตาร์ทอัพ",
  "เขียนโปรแกรมเป็น",
  "ทำเว็บของตัวเอง",
];

// Example questions, typed one by one inside the search bar.
export const EXAMPLES = ["อยากเข้าวิศวะคอม", "ม.6 ยังไม่มีพอร์ต", "อยากทำเกมของตัวเอง", "Hamster Hub คืออะไร", "ค่าเรียนเท่าไหร่"];

// Real works around the headline. Every line comes from the site's own text.
// desk: [x %, y %, width px at 1440, tilt]. phone: [offset from own side %, bottom %, width %, tilt] or null (hidden on phones).
export type WorkCard = {
  side: "l" | "r";
  img: string;
  ratio: number; // height / width of the picture
  name: string;
  line: string;
  clip?: string;
  face?: [number, number]; // where the face sits in the picture, for the small square avatar
  desk: [number, number, number, number];
  phone: [number, number, number, number] | null;
};

export const CARDS: WorkCard[] = [
  { side: "l", img: "w-revoice.webp", ratio: 3 / 4, name: "น้องไอดิน", line: "REVOICE · ชนะ NSC 2025", face: [28, 30], desk: [1, 9, 232, -3], phone: [-9, 3, 44, 5] },
  { side: "l", img: "dek69-6.webp", ratio: 5 / 4, name: "น้องต้นกล้า", line: "ติดจุฬาฯ รอบ Portfolio", face: [74, 50], desk: [11, 37, 166, 3], phone: [-4, 0, 27, -6] },
  { side: "l", img: "work-stressstrike.webp", ratio: 9 / 16, name: "StressStrike", line: "ชนะเลิศ OBEC Roboplayground", clip: "hole-stressstrike.mp4", desk: [1.5, 67, 224, -2], phone: null },
  { side: "r", img: "w-hmap.webp", ratio: 10 / 16, name: "PHC Map", line: "สตาร์ทอัพ · ใช้สอนเด็กกว่า 1,000 คน", desk: [83, 9, 232, 3], phone: null },
  { side: "r", img: "dek69-1.webp", ratio: 5 / 4, name: "น้องปลื้ม", line: "ติดสถิติประยุกต์ฯ สจล.", face: [68, 46], desk: [78.5, 35, 166, -3], phone: [-3, 0, 27, 6] },
  { side: "r", img: "work-slash-speed.webp", ratio: 9 / 16, name: "SLASH//SPEED", line: "เข้ารอบ Final TGS", clip: "hole-slash-speed2.mp4", desk: [83.5, 67, 224, 2], phone: [-9, 5, 44, -5] },
];
