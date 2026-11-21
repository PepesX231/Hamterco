import { APPLY_STEPS, LINK, PACKAGES, PRICE_NOTE, baht, route } from "@/lib/routes";
import { LINE_URL } from "@/lib/site";

export function Compare() {
  return (
    <div className="st-compare" role="region" aria-label="เปรียบเทียบแพ็กเกจ" tabIndex={0}>
      <table>
        <thead>
          <tr><th scope="col"><span className="sr-only">หัวข้อ</span></th>{PACKAGES.map((p) => <th key={p.id} scope="col">{p.name}</th>)}</tr>
        </thead>
        <tbody>
          <tr><th scope="row">ชิ้นงานที่ได้</th>{PACKAGES.map((p) => <td key={p.id}>{p.makes}</td>)}</tr>
          <tr><th scope="row">เหมาะกับ</th>{PACKAGES.map((p) => <td key={p.id}>{p.forWho}</td>)}</tr>
          <tr><th scope="row">Route ที่รวม</th>{PACKAGES.map((p) => <td key={p.id}>{p.routes.map((r) => route(r).name).join(", ")}</td>)}</tr>
          <tr><th scope="row">ราคา</th>{PACKAGES.map((p) => <td key={p.id}><b>{baht(p.price)}</b> <span className="st-tag">{PRICE_NOTE}</span></td>)}</tr>
          <tr><th scope="row"><span className="sr-only">ไปต่อ</span></th>{PACKAGES.map((p) => <td key={p.id}><a className="st-link" href={LINK.pkg(p.id)}>ดูแพ็กเกจ</a></td>)}</tr>
        </tbody>
      </table>
    </div>
  );
}

// Answers say only what is known today; anything the team has not confirmed points to LINE.
export const FAQ: [string, string][] = [
  ["Route กับแพ็กเกจต่างกันยังไง", "Route คือทักษะหนึ่งเรื่อง เลือกเรียนแยกได้ทีละเส้น ส่วนแพ็กเกจรวม 3 Route ที่ต่อกันจนได้ชิ้นงานหนึ่งชิ้นตามเป้าหมาย เช่น เว็บไว้ใส่พอร์ต หรือโปรเจกต์ส่งแข่ง"],
  ["ราคาที่เห็นเป็นราคาจริงไหม", "ตอนนี้ราคาของ Route และแพ็กเกจเป็นราคาตัวอย่าง ราคาจริงและรอบที่เปิดเช็กได้ใน LINE ก่อนสมัคร"],
  ["ต้องมีพื้นฐานก่อนไหม", "แพ็กเกจโปรแกรมชิ้นแรกตั้งใจไว้สำหรับคนที่ยังไม่เคยทำโปรเจกต์ ส่วนพื้นฐานของแต่ละ Route ทีมกำลังสรุป ถ้าไม่แน่ใจ ทัก LINE ให้ทีมช่วยเลือกได้"],
  ["เรียนที่ไหน กี่ครั้ง", "รายละเอียดเวลาและสถานที่ของแต่ละ Route ทีมกำลังสรุป ทัก LINE เพื่อถามรอบที่เปิดอยู่"],
  ["Port Express และ Project Build Skill เป็นแพ็กเกจไหม", "ไม่ใช่ ทั้งสองเป็นโปรแกรมเต็มที่มีเงื่อนไขของตัวเอง Port Express เรียน 2 เดือน ราคา 5,990 บาท ส่วน Project Build Skill เป็นโปรแกรม 12 เดือน ราคา 19,990 บาท"],
];

export function FaqAndSteps({ title = "ก่อนสมัคร." }: { title?: string }) {
  return (
    <section className="st-block" aria-label="คำถามที่พบบ่อยและขั้นตอนสมัคร">
      <h2 className="st-title" style={{ marginBottom: 28 }}><i>{title}</i> <span style={{ color: "var(--st-sub)" }}>เรื่องที่คนถามบ่อย</span></h2>
      <div className="st-split">
        <div className="st-faq">
          {FAQ.map(([q, a]) => (
            <details key={q}><summary>{q}</summary><p>{a}</p></details>
          ))}
        </div>
        <div>
          <h3 className="st-shelf-t" style={{ fontSize: 22, marginBottom: 4 }}>สมัครยังไง</h3>
          <ol className="st-steps">
            {APPLY_STEPS.map(([b, s]) => <li key={b}><b>{b}</b><span>{s}</span></li>)}
          </ol>
          <a className="st-btn st-btn-line" href={LINE_URL} target="_blank" rel="noopener" style={{ marginTop: 22 }}>ทัก LINE ถามรอบที่เปิด</a>
        </div>
      </div>
    </section>
  );
}
