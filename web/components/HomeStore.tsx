import { LINK, PACKAGES, ROUTES } from "@/lib/routes";
import { PackageCard, RouteCard } from "./store/Cards";
import { Shelf } from "./store/Shelf";

// Home, right after the hero. Packages lead (Apple's "ใหม่ล่าสุด" shelf), single Routes follow (its second shelf).
const SHELF = ["unity", "web", "blender", "iot", "python", "story", "app", "pitch"];

export function HomeStore() {
  return (
    <section className="hm-store" aria-label="แพ็กเกจและ Route">
      <div className="st-wrap">
        <Shelf label="แพ็กเกจตามเป้าหมาย" title="แพ็กเกจตามเป้าหมาย" sub="เลือกจากผลงานที่น้องอยากมี" more={<a className="st-link" href={LINK.store}>ดูทั้งหมด</a>}>
          {PACKAGES.map((p) => <PackageCard key={p.id} p={p} />)}
        </Shelf>
        <Shelf label="Route รายเส้น" title="Route รายเส้น" sub="ฝึกทีละทักษะ" more={<a className="st-link" href={LINK.store}>ดูทั้งหมด</a>}>
          {SHELF.map((id) => <RouteCard key={id} r={ROUTES.find((r) => r.id === id)!} showDisc />)}
        </Shelf>
      </div>
    </section>
  );
}
