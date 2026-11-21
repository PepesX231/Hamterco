"use client";

import { useState } from "react";
import { GOALS, PACKAGES } from "@/lib/routes";
import { PackageCard } from "./Cards";
import { Shelf } from "./Shelf";

/** Packages by goal, with the goal chips from the design: pick one to bring its package to the front. */
export function PackageShelf() {
  const [goal, setGoal] = useState<string | null>(null);
  const list = goal ? [...PACKAGES].sort((a, b) => Number(b.goal === goal) - Number(a.goal === goal)) : PACKAGES;
  return (
    <div id="packages">
      <Shelf
        label="แพ็กเกจตามเป้าหมาย"
        title="แพ็กเกจตามเป้าหมาย."
        sub="3 Route ต่อกันจนได้ชิ้นงาน"
        more={<a className="st-link" href="#compare">เปรียบเทียบ</a>}
        top={
          <div className="st-chips" role="group" aria-label="เลือกเป้าหมาย">
            {GOALS.map((g) => (
              <button key={g.id} type="button" aria-pressed={goal === g.id} onClick={() => setGoal(goal === g.id ? null : g.id)}>{g.label}</button>
            ))}
          </div>
        }
      >
        {list.map((p) => <PackageCard key={p.id} p={p} />)}
      </Shelf>
    </div>
  );
}
