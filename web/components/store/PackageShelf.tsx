import { PACKAGES } from "@/lib/routes";
import { PackageCard } from "./Cards";
import { Shelf } from "./Shelf";

/** Packages by goal. */
export function PackageShelf() {
  return (
    <div id="packages">
      <Shelf label="แพ็กเกจตามเป้าหมาย" title="แพ็กเกจ" sub="ตัวเลือกเป้าหมายของน้อง">
        {PACKAGES.map((p) => <PackageCard key={p.id} p={p} />)}
      </Shelf>
    </div>
  );
}
