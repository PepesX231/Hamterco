import { understand } from "./understand";
// Hams Route: skills you can learn one at a time (Route), and sets of Routes for one goal (Package).
// Source: Hamster_Hub_Claude_Handoff/01-design/routes (Routes HTML + route-store-v2 data), 22 Nov 2026.
// Every Route and Package price here is a SAMPLE price from the design files and must be shown as such
// (PRICE_NOTE) until the team confirms it. Port Express and Project Build Skill are real programs.

export const BASE = "/Hamterco/next";
export const art = (f: string) => `${BASE}/route-art/${f}`;
export const PRICE_NOTE = "ราคาตัวอย่าง";
export const PENDING = "รอทีมยืนยัน";

export type Discipline = { id: string; name: string; line: string; tile: string; tone: string };
export type Route = { id: string; name: string; d: string; line: string; price: number; tile: string };
export type Package = {
  id: string;
  name: string;
  hook: string; // one plain line under the name: what the student walks away with
  goal: string; // goal chip it belongs to
  forWho: string;
  line: string;
  makes: string; // the piece of work you finish with
  routes: string[];
  price: number;
  img: string;
  dark: boolean; // picture is dark: text goes white
  bg: string; // the picture's own edge colour, so a wide hero can continue it
};
export type Program = { id: string; name: string; forWho: string; line: string; facts: [string, string][]; price: string; img: string; href: string; status: string };

export const DISCIPLINES: Discipline[] = [
  { id: "game", name: "Game Dev", line: "ทำเกมให้เล่นได้", tile: "A0", tone: "#F7D9C4" },
  { id: "motion", name: "3D & Animation", line: "ปั้นและขยับตัวละคร", tile: "A3", tone: "#DDE9DF" },
  { id: "web", name: "Web & App", line: "สร้างเว็บหรือแอป", tile: "A4", tone: "#E5DDF0" },
  { id: "coding", name: "Coding & IoT", line: "เขียนโค้ดและต่อวงจร", tile: "A6", tone: "#E3EBD3" },
  { id: "portfolio", name: "Portfolio", line: "เล่าโปรเจกต์ให้เห็นฝีมือ", tile: "A8", tone: "#F5E6C4" },
  { id: "venture", name: "Startup & Pitch", line: "พาไอเดียไปเจอคนใช้", tile: "B11", tone: "#F3DCE0" },
];

export const ROUTES: Route[] = [
  { id: "unity", name: "Unity Basics", d: "game", line: "ทำเกม Unity ฉากแรก", price: 1390, tile: "A0" },
  { id: "game-design", name: "Game Design", d: "game", line: "ออกแบบกติกาให้คนลองเล่น", price: 1190, tile: "A1" },
  { id: "level", name: "Level Design", d: "game", line: "จัดฉากและจังหวะของด่าน", price: 1490, tile: "A10" },
  { id: "playtest", name: "Game Playtest", d: "game", line: "เก็บฟีดแบ็กจากผู้เล่น", price: 990, tile: "B0" },
  { id: "blender", name: "Blender 3D", d: "motion", line: "ปั้นโมเดลพร้อมใช้ในเกม", price: 1590, tile: "A3" },
  { id: "animation", name: "3D Animation", d: "motion", line: "ทำให้ตัวละครขยับได้", price: 1790, tile: "A2" },
  { id: "rig", name: "Character Rigging", d: "motion", line: "ตั้งโครงขยับตัวละคร", price: 1490, tile: "B1" },
  { id: "vfx", name: "Unity VFX", d: "motion", line: "ทำเอฟเฟกต์ในฉากเกม", price: 1690, tile: "B2" },
  { id: "web", name: "Web Foundations", d: "web", line: "ทำเว็บหน้าแรกให้เปิดได้", price: 1290, tile: "A4" },
  { id: "ux", name: "UX/UI Design", d: "web", line: "ออกแบบหน้าจอตามโจทย์ผู้ใช้", price: 1390, tile: "B6" },
  { id: "app", name: "App Prototype", d: "web", line: "ทำต้นแบบแอปที่กดได้", price: 1790, tile: "A5" },
  { id: "backend", name: "Backend API", d: "web", line: "เชื่อมแอปกับข้อมูล", price: 1490, tile: "B3" },
  { id: "programming", name: "Programming Basics", d: "coding", line: "เข้าใจเงื่อนไข ลูป และตัวแปร", price: 890, tile: "A7" },
  { id: "python", name: "Python Starter", d: "coding", line: "เขียนโปรแกรม Python ชิ้นแรก", price: 990, tile: "B4" },
  { id: "iot", name: "Arduino IoT", d: "coding", line: "ต่อวงจรและสั่งงานอุปกรณ์", price: 1690, tile: "A6" },
  { id: "sensor", name: "Sensor Systems", d: "coding", line: "อ่านและแสดงข้อมูลเซนเซอร์", price: 1190, tile: "B5" },
  { id: "story", name: "Portfolio Story", d: "portfolio", line: "เล่าบทบาทและผลลัพธ์ของงาน", price: 1090, tile: "A8" },
  { id: "build", name: "Project Build", d: "portfolio", line: "พาโปรเจกต์ไปถึงชิ้นงานแรก", price: 1490, tile: "B7" },
  { id: "case", name: "Case Study", d: "portfolio", line: "บันทึกโจทย์ วิธีคิด และผลลัพธ์", price: 1190, tile: "B8" },
  { id: "review", name: "Portfolio Review", d: "portfolio", line: "ทบทวนและจัดลำดับหลักฐาน", price: 990, tile: "B9" },
  { id: "problem", name: "Problem Discovery", d: "venture", line: "หาโจทย์จากคนที่เจอปัญหาจริง", price: 1290, tile: "B10" },
  { id: "validate", name: "Idea Validation", d: "venture", line: "ทดสอบไอเดียกับคนใช้", price: 1290, tile: "A11" },
  { id: "demo", name: "Product Demo", d: "venture", line: "ทำเดโมให้คนลองใช้งาน", price: 1690, tile: "A9" },
  { id: "pitch", name: "Demo & Pitch", d: "venture", line: "นำเสนอเดโมและเหตุผลเบื้องหลัง", price: 1690, tile: "B11" },
];

export const GOALS = [
  { id: "first", label: "เริ่มชิ้นแรก" },
  { id: "port", label: "เตรียมพอร์ต ม.6" },
  { id: "compete", label: "เตรียมลงแข่ง" },
  { id: "idea", label: "ทดสอบไอเดีย" },
];

export const PACKAGES: Package[] = [
  {
    id: "first-program", name: "First Build", hook: "โปรแกรมชิ้นแรกที่น้องเขียนเอง", goal: "first", forWho: "ม.5 ที่ยังไม่เคยทำโปรเจกต์",
    line: "ลองเขียนโค้ดจากพื้นฐาน แล้วทำโปรแกรม Python ชิ้นเล็กที่เปิดใช้เองได้",
    makes: "โปรแกรม Python ที่เขียนเอง", routes: ["programming", "python", "build"], price: 2390, img: "pk2-first.webp", dark: true, bg: "#160600",
  },
  {
    id: "first-web", name: "Port Ready", hook: "เว็บของน้องเอง พร้อมใส่พอร์ต", goal: "port", forWho: "ม.6 ที่ยังไม่มีผลงาน",
    line: "ทำเว็บที่เปิดใช้และเชื่อมข้อมูลได้ เก็บขั้นตอนตั้งแต่ร่างหน้าจอจนเป็นเว็บจริงไว้เล่าในพอร์ต",
    makes: "เว็บไซต์ที่เชื่อมข้อมูลได้", routes: ["ux", "web", "backend"], price: 3490, img: "pk2-web.webp", dark: true, bg: "#11011c",
  },
  {
    id: "compete", name: "Arena", hook: "พาโปรเจกต์ขึ้นเวทีแข่ง", goal: "compete", forWho: "ทีมที่เตรียมลงแข่ง",
    line: "เลือกปัญหาที่อยากแก้ ทำต้นแบบ แล้วซ้อมเดโมสำหรับวันแข่ง",
    makes: "ต้นแบบพร้อมเดโมสำหรับวันแข่ง", routes: ["problem", "app", "pitch"], price: 4290, img: "pk2-compete.webp", dark: true, bg: "#010825",
  },
  {
    id: "prototype", name: "Launch Lab", hook: "ไอเดียกลายเป็นแอปที่คนลองใช้จริง", goal: "idea", forWho: "คนที่มีไอเดียอยู่แล้ว",
    line: "ทำต้นแบบจากไอเดียของตัวเอง ให้คนลองใช้ แล้วดูว่าควรแก้ตรงไหน",
    makes: "ต้นแบบแอปที่มีคนลองใช้แล้ว", routes: ["validate", "app", "demo"], price: 3990, img: "pk2-proto.webp", dark: true, bg: "#001109",
  },
];

// Full programs: real, with their own terms. Facts only from the site and the briefs.
export const PROGRAMS: Program[] = [
  {
    id: "port-express", name: "Port Express", forWho: "ม.6 ที่ยังไม่มีผลงาน", line: "เรียนสร้างเกมของตัวเองด้วย Unity จบคอร์สได้เกมที่ทำเองไว้ใส่พอร์ต",
    facts: [["2 เดือน", "จันทร์ พุธ ศุกร์"], ["5,990 บาท", "ทั้งคอร์ส"]], price: "฿5,990", img: "/Hamterco/img/portex-poster.webp",
    href: "https://www.hamsterhub.co/portex-site/index.html", status: "รอบนี้เริ่มเรียนแล้ว 9 พ.ย. 2569",
  },
  {
    id: "build-skill", name: "Project Build Skill", forWho: "เด็ก ม.ปลาย", line: "โปรแกรม 12 เดือน ทำโปรเจกต์หลักหนึ่งชิ้น พร้อมฝึกทำงานจริงและนำเสนอ เตรียมผลงานไว้ยื่นพอร์ตหรือลงแข่ง",
    facts: [["12 เดือน", "โปรเจกต์หลัก 1 ชิ้น"], ["19,990 บาท", "ทั้งโปรแกรม"]], price: "฿19,990", img: `${BASE}/route-art/pk-iot.webp`,
    href: "https://pepesx231.github.io/Buildskill/", status: "ดูรายละเอียดเต็มที่หน้าโปรแกรม",
  },
];

export const disc = (id: string) => DISCIPLINES.find((d) => d.id === id)!;
export const route = (id: string) => ROUTES.find((r) => r.id === id)!;
export const pkg = (id: string) => PACKAGES.find((p) => p.id === id)!;
export const baht = (n: number) => "฿" + n.toLocaleString("en-US");
export const routesIn = (d: string) => ROUTES.filter((r) => r.d === d);
export const packagesWith = (rid: string) => PACKAGES.filter((p) => p.routes.includes(rid));
export const tile = (t: string) => art(t + ".webp");
export const sumOf = (p: Package) => p.routes.reduce((s, r) => s + route(r).price, 0);

export const LINK = {
  store: `${BASE}/routes/`,
  disc: (d: string) => `${BASE}/routes/${d}/`,
  route: (r: string) => `${BASE}/routes/r/${r}/`,
  pkg: (p: string) => `${BASE}/routes/p/${p}/`,
};

// ---------- search: type a goal, get Routes and Packages ----------
// Each topic: words that point to it, and what it shows.
const TOPICS: { words: string[]; d?: string[]; r?: string[]; p?: string[] }[] = [
  { words: ["เกม", "game", "unity", "ยูนิตี้", "ด่าน", "level"], d: ["game"], p: [] },
  { words: ["3d", "สามมิติ", "blender", "เบลนเดอร์", "โมเดล", "แอนิเมชัน", "animation", "อนิเมชัน", "ตัวละคร", "vfx", "เอฟเฟกต์"], d: ["motion"] },
  { words: ["เว็บ", "web", "เว็บไซต์", "website", "หน้าเว็บ"], d: ["web"], p: ["first-web"], r: ["web", "ux", "backend"] },
  { words: ["แอป", "app", "แอพ", "ui", "ux", "ออกแบบหน้าจอ"], r: ["app", "ux"], p: ["prototype"] },
  { words: ["iot", "arduino", "อาดูโน่", "วงจร", "เซนเซอร์", "sensor", "หุ่นยนต์", "robot"], r: ["iot", "sensor"] },
  { words: ["python", "ไพทอน", "โค้ด", "code", "coding", "เขียนโปรแกรม", "โปรแกรม", "programming"], r: ["programming", "python"], p: ["first-program"] },
  { words: ["พอร์ต", "portfolio", "port", "ยื่น", "tcas", "มหาลัย", "มหาวิทยาลัย", "ม.6", "dek"], d: ["portfolio"], p: ["first-web", "first-program"] },
  { words: ["แข่ง", "nsc", "ประกวด", "ส่งแข่ง", "รางวัล", "เวที", "compete"], p: ["compete"], r: ["problem", "pitch"] },
  { words: ["ไอเดีย", "สตาร์ทอัพ", "startup", "ธุรกิจ", "pitch", "นำเสนอ", "เดโม", "demo", "คนใช้"], d: ["venture"], p: ["prototype"] },
  { words: ["เริ่ม", "ศูนย์", "พื้นฐาน", "ไม่เคย", "มือใหม่", "ชิ้นแรก", "ม.5", "ม.4"], p: ["first-program"], r: ["programming", "unity", "web"] },
];

export type Found = { routes: Route[]; packages: Package[]; programs: Program[]; disciplines: Discipline[]; understood: boolean };

// full programs answer some goals better than any package: Port Express is a Unity game for the portfolio
const PROGRAM_WORDS: Record<string, string[]> = { "port-express": ["เกม", "game", "unity", "ยูนิตี้", "พอร์ต", "portfolio", "ม.6", "ยื่น"], "build-skill": ["12 เดือน", "ทั้งปี", "build skill", "โปรเจกต์หลัก", "ระยะยาว"] };

export function findForGoal(q: string): Found {
  const first = matchGoal(q);
  if (first.understood || !q.trim()) return first;
  // typos, slang, no spaces, wrong keyboard layout: name the topic first, then match again
  const r = understand(q);
  return r.intent ? matchGoal([r.intent.routes, ...r.others.map((o) => o.routes), r.text].filter(Boolean).join(" ")) : first;
}

function matchGoal(q: string): Found {
  const t = q.toLowerCase().replace(/\s+/g, " ").trim();
  const r = new Set<string>(), p = new Set<string>(), d = new Set<string>();
  if (t) {
    for (const x of ROUTES) if (t.includes(x.name.toLowerCase()) || x.name.toLowerCase().includes(t)) r.add(x.id);
    for (const x of PACKAGES) if (t.includes(x.name.toLowerCase()) || x.name.toLowerCase().includes(t)) p.add(x.id);
    for (const tp of TOPICS) {
      if (!tp.words.some((w) => t.includes(w))) continue;
      tp.d?.forEach((id) => { d.add(id); routesIn(id).forEach((x) => r.add(x.id)); });
      tp.r?.forEach((id) => r.add(id));
      tp.p?.forEach((id) => p.add(id));
    }
    for (const id of d) PACKAGES.forEach((x) => { if (x.routes.some((rr) => route(rr).d === id)) p.add(x.id); });
  }
  const pg = t ? PROGRAMS.filter((x) => { const w = PROGRAM_WORDS[x.id] || []; const hits = w.filter((k) => t.includes(k)).length; return x.id === "port-express" ? hits >= 2 || t.includes("port express") : hits >= 1; }) : [];
  return {
    programs: pg,
    routes: ROUTES.filter((x) => r.has(x.id)),
    packages: PACKAGES.filter((x) => p.has(x.id)),
    disciplines: DISCIPLINES.filter((x) => d.has(x.id)),
    understood: r.size + p.size + pg.length > 0,
  };
}

export const GOAL_EXAMPLES = ["อยากทำเกมไว้ยื่นพอร์ต", "ม.6 ยังไม่มีผลงาน", "อยากทำเว็บ", "เตรียมลงแข่ง NSC", "อยากเริ่มเขียนโค้ด", "มีไอเดียแอปอยู่แล้ว"];

// What every page can say about applying. The steps are how it works today (LINE); the team should confirm.
export const APPLY_STEPS = [
  ["เลือก Route หรือแพ็กเกจ", "ดูชิ้นงานที่จะได้ทำ เวลา และราคา"],
  ["ทัก LINE บอกชื่อที่เลือก", "ทีมตอบรอบที่เปิด ราคาจริง และเวลาเรียน"],
  ["ยืนยันรอบที่จะเรียน", "ทีมแจ้งวันเริ่มและวิธีชำระเงิน"],
] as const;
