import { LINK, PACKAGES, PRICE_NOTE, ROUTES, art, baht, pkg } from "@/lib/routes";
import { RouteCard } from "./store/Cards";
import { Shelf } from "./store/Shelf";

// Home, right after the hero: from "what do you want" to "here is how to get there".
// One package leads (the most asked-for goal), two sit beside it, then single Routes on a shelf.
const LEAD = "first-web";
const SIDE = ["first-program", "compete"];
const SHELF = ["unity", "web", "blender", "iot", "python", "story", "app", "pitch"];

export function HomeStore() {
  const lead = pkg(LEAD);
  return (
    <section className="hm-store" aria-label="เลือกแพ็กเกจตามเป้าหมาย">
      <div className="st-wrap">
        <div className="st-shelf-h" style={{ marginBottom: 22 }}>
          <h2 className="st-title"><i>เลือกแพ็กเกจตามเป้าหมาย.</i> <span style={{ color: "var(--st-sub)" }}>ทำจนได้ชิ้นงานจริง</span></h2>
          <a className="st-link" href={LINK.store + "#packages"}>ดูทุกแพ็กเกจ</a>
        </div>

        <a className="hm-feature" href={LINK.pkg(lead.id)}>
          <figure><img src={art(lead.img)} alt="" loading="lazy" decoding="async" /></figure>
          <div>
            <small>สำหรับ {lead.forWho}</small>
            <b>{lead.name}</b>
            <p>{lead.line}</p>
            <span className="st-price"><b>{baht(lead.price)}</b> · รวม {lead.routes.length} Route <span className="st-tag st-tag-dark">{PRICE_NOTE}</span></span>
            <span className="st-btn st-btn-light" style={{ marginTop: 22, alignSelf: "flex-start" }}>ดูแพ็กเกจ</span>
          </div>
        </a>
        <div className="hm-two">
          {SIDE.map((id) => {
            const p = pkg(id);
            return (
              <a key={id} className="hm-small" href={LINK.pkg(id)}>
                <img src={art(p.img)} alt="" loading="lazy" decoding="async" />
                <div>
                  <small>สำหรับ {p.forWho}</small>
                  <b>{p.name}</b>
                  <p>{p.line}</p>
                  <span className="st-price"><b>{baht(p.price)}</b> · รวม {p.routes.length} Route <span className="st-tag">{PRICE_NOTE}</span></span>
                </div>
              </a>
            );
          })}
        </div>

        <Shelf label="Route รายเส้น" title="Route รายเส้น." sub="เลือกฝึกทีละทักษะ" more={<a className="st-link" href={LINK.store}>ดู Hams Route ทั้งหมด</a>}>
          {SHELF.map((id) => <RouteCard key={id} r={ROUTES.find((r) => r.id === id)!} showDisc />)}
        </Shelf>
        <p className="st-note" style={{ marginTop: -6 }}>ราคาของ Route และแพ็กเกจเป็นราคาตัวอย่าง ราคาจริงและรอบที่เปิดเช็กใน LINE · มีทั้งหมด {PACKAGES.length} แพ็กเกจ {ROUTES.length} Route</p>
      </div>
    </section>
  );
}
