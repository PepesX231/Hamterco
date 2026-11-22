import { PACKAGES } from "@/lib/routes";
import { PackageCard } from "./Cards";
import { Shelf } from "./Shelf";

/** Packages by goal. */
export function PackageShelf() {
  return (
    <div id="packages">
      <Shelf label="แพ็กเกจตามเป้าหมาย" title="แพ็กเกจตามเป้าหมาย" sub="เลือกจากผลงานที่น้องอยากมี">
        {PACKAGES.map((p) => <PackageCard key={p.id} p={p} />)}
      </Shelf>
    </div>
  );
}
