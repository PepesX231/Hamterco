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

export const CHIPS = ["อยากเข้าวิศวะคอม", "ม.6 ยังไม่มีพอร์ต", "อยากทำเกมของตัวเอง", "Hamster Hub คืออะไร", "ค่าเรียนเท่าไหร่"];

// Holes in the cheese. Each one is a window onto a real work made here.
// x, y: percent of the hero. size: px at a 1440px-wide screen. phone: hidden on phones, or its own spot there.
export type Hole = {
  x: number;
  y: number;
  size: number;
  img: string;
  name: string;
  clip?: string;
  phone?: false | [number, number];
};

export const HOLES: Hole[] = [
  { x: 10, y: 25, size: 210, img: "work-stressstrike.webp", clip: "hole-stressstrike.mp4", name: "StressStrike", phone: [9, 19] },
  { x: 9, y: 80, size: 200, img: "sc-revoice.webp", name: "REVOICE", phone: [8, 93] },
  { x: 89, y: 28, size: 200, img: "w-hmap.webp", clip: "hole-hmap.mp4", name: "Hamster Map", phone: [92, 25] },
  { x: 87, y: 83, size: 180, img: "work-slash-speed.webp", clip: "hole-slash-speed2.mp4", name: "SLASH//SPEED", phone: [62, 77] },
  { x: 3, y: 56, size: 100, img: "dek69-1.webp", name: "พอร์ต DEK69", phone: [8, 76] },
  { x: 72, y: 22, size: 104, img: "work-midnight-at-roadside.webp", name: "Midnight at Roadside", phone: false },
  { x: 73, y: 90, size: 90, img: "work-hot-hot-hot.webp", name: "Hot Hot Hot", phone: false },
  { x: 24, y: 13, size: 64, img: "sc-lyno.webp", name: "LYNO", phone: false },
  { x: 44, y: 12, size: 56, img: "dek69-5.webp", name: "พอร์ต DEK69", phone: false },
  { x: 62, y: 12, size: 56, img: "sc-timekeeper.webp", name: "Time Keeper", phone: false },
  { x: 76, y: 10, size: 64, img: "sc-zoo.webp", name: "Z.O.O.", phone: false },
  { x: 83, y: 64, size: 64, img: "w-quest-town.webp", name: "Hamster Quest", phone: false },
  { x: 25, y: 84, size: 70, img: "dek69-2.webp", name: "พอร์ต DEK69", phone: false },
  { x: 58, y: 90, size: 56, img: "work-escape-rolling.webp", name: "Escape Rolling", phone: false },
];
