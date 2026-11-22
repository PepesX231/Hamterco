import { PACKAGES } from "@/lib/routes";
import { PackageCard } from "./Cards";
import { Shelf } from "./Shelf";

/** Packages by goal. */
export function PackageShelf() {
  return (
    <div id="packages">
      <Shelf label="แพ็กเกจตามเป้าหมาย" title="จบแพ็กเกจ น้องมีผลงานจริงติดมือ" sub="เลือกตามเป้าหมายของน้อง">
        {PACKAGES.map((p) => <PackageCard key={p.id} p={p} />)}
      </Shelf>
    </div>
  );
}
