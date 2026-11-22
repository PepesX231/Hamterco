// What Hamster Hub students built and won. Source: the team's sheet (Google Sheet "Hamster Hub", tab 1), 22 Nov 2026.
// Copied as written there; only spelling of names was kept. Rows with no link stay without one.

export type Win = { rank: string; name: string; by: string; href?: string };
export type Stage = { stage: string; full?: string; wins: Win[] };

const FB26 = "https://www.facebook.com/100000550526763/videos/oa.1802609267598780/";
const FB25 = "https://www.facebook.com/100000550526763/videos/oa.1528925231792269/";

export const WINS: Stage[] = [
  { stage: "depa 2026", wins: [{ rank: "ชนะ 200,000 บาท", name: "Apocalypis Building", by: "ฟาร์", href: "https://www.youtube.com/watch?v=dKM2loG0bMA" }] },
  { stage: "OBEC Robotics Playground", wins: [{ rank: "ชนะเลิศ", name: "ต่อยมวย", by: "วิน" }] },
  { stage: "GGJ 2026", full: "Global Game Jam", wins: [{ rank: "อันดับ 1", name: "Windy", by: "วินดี้" }] },
  { stage: "MIT 2025", wins: [{ rank: "อันดับ 1", name: "", by: "ขนมปัง" }] },
  { stage: "NSC 2026 เกม", full: "การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย", wins: [
    { rank: "อันดับ 2", name: "Karma", by: "มาริโอ้", href: FB26 + "2972173776459512" },
    { rank: "อันดับ 4", name: "หมากรุก", by: "กัปตัน", href: FB26 + "1283098503824184" },
    { rank: "อันดับ 4", name: "ทีมมหาลัย", by: "เจได", href: FB26 + "1427537582730365" },
    { rank: "รอบชิง", name: "Co-op Roblox", by: "ปัน", href: FB26 + "1771986460470849" },
    { rank: "รอบชิง", name: "ตาบอด", by: "ธันวา", href: FB26 + "2830786583956742" },
    { rank: "รอบชิง", name: "ผีอวกาศ", by: "เพชร", href: FB26 + "1620010033053522" },
    { rank: "รอบชิง", name: "เสือสมิง", by: "เฟรม", href: FB26 + "1413063067429632" },
    { rank: "รอบชิง", name: "กระหัง", by: "นน", href: FB26 + "2304725113676720" },
  ] },
  { stage: "NSC 2026 การศึกษา", wins: [
    { rank: "อันดับ 4", name: "สมการ", by: "วิน", href: FB26 + "28097120909948436" },
    { rank: "รอบชิง", name: "RTS ฟิสิกส์", by: "จิน", href: FB26 + "4726064581050042" },
    { rank: "รอบชิง", name: "ผ่าศพ", by: "แอนดิว", href: FB26 + "1127574426441259" },
    { rank: "รอบชิง", name: "ปลูกผัก", by: "วินดี้" },
  ] },
  { stage: "TGGS 2026", wins: [
    { rank: "Top 12", name: "RE//SLASH", by: "ดินสอ", href: "https://www.instagram.com/p/DevgB-uHUoU/" },
    { rank: "Top 12", name: "Don't Talk, I Need Coffee", by: "สตางค์", href: "https://stangshinez.itch.io/dont-talk-i-need-coffee" },
    { rank: "Top 20", name: "TLAMAN", by: "ลาเต้", href: "https://tomyummama.itch.io/tlaman" },
  ] },
  { stage: "NSC 2025 แอป", wins: [{ rank: "อันดับ 1", name: "REVOICE", by: "ไอดิน", href: FB25 + "1754855858728388" }] },
  { stage: "NSC 2025 เกม", wins: [
    { rank: "อันดับ 2", name: "Noas", by: "ไอซ์", href: FB25 + "1485088192630896" },
    { rank: "อันดับ 3", name: "Time Keeper", by: "มิคกี้", href: FB25 + "1108706890674978" },
    { rank: "อันดับ 4", name: "Plant Create World", by: "พลอย", href: FB25 + "1128696488701788" },
    { rank: "อันดับ 4", name: "Z.O.O", by: "ใบข้าว", href: FB25 + "1464192271292821" },
    { rank: "รอบชิง", name: "ทีมมหาลัย", by: "อัญ", href: FB25 + "774454108465678" },
    { rank: "รอบชิง", name: "แซลมอน", by: "นิน", href: FB25 + "983650750517128" },
    { rank: "รอบชิง", name: "Glass Whisper", by: "เมเม", href: FB25 + "751550477583698" },
    { rank: "รอบชิง", name: "Shadow Maze", by: "ซัน", href: FB25 + "803451712235299" },
    { rank: "รอบชิง", name: "หยดน้ำ", by: "ทีม 3D", href: FB25 + "2266727817119965" },
  ] },
  { stage: "GGJ 2025", wins: [{ rank: "อันดับ 2", name: "เรียน 1 เดือน", by: "เบทส์", href: "https://www.facebook.com/reel/966426822132133" }] },
  { stage: "TGF 2025", wins: [{ rank: "รอบชิง", name: "Veggie Grow", by: "เป๊ป", href: "https://youtu.be/Q49xwuCOzEI" }] },
  { stage: "NSC 2024 เกม", wins: [
    { rank: "อันดับ 2", name: "Whisker Odyssey", by: "บีม", href: "https://www.facebook.com/reel/1537303340552554" },
    { rank: "อันดับ 3", name: "Veggie Dash", by: "แมค" },
    { rank: "รอบชิง", name: "อโยธยา", by: "ขนมปัง", href: "https://www.facebook.com/reel/482698241392113" },
  ] },
  { stage: "NSC 2023", wins: [{ rank: "อันดับ 2", name: "ยางลบ", by: "แป้ง", href: "https://www.facebook.com/reel/455891749905328" }] },
];

export const winCount = WINS.reduce((n, s) => n + s.wins.length, 0);
export const topCount = WINS.reduce((n, s) => n + s.wins.filter((w) => w.rank !== "รอบชิง" && !w.rank.startsWith("Top")).length, 0);
