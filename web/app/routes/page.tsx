import type { Metadata } from "next";
import { LegacyRuntime } from "@/components/LegacyRuntime";
import { DisciplineIcons, PackageCard, ProgramCard, RouteCard } from "@/components/store/Cards";
import { Shelf } from "@/components/store/Shelf";
import { GoalSearch } from "@/components/store/GoalSearch";
import { Compare, FaqAndSteps } from "@/components/store/Info";
import { PackageShelf } from "@/components/store/PackageShelf";
import { DISCIPLINES, LINK, PROGRAMS, art, routesIn } from "@/lib/routes";

export const metadata: Metadata = { title: "Hams Route | Hamster Hub", description: "เลือกทักษะที่อยากมีทีละเส้น หรือเลือกแพ็กเกจตามเป้าหมาย เช่น เว็บแรกใส่พอร์ต หรือโปรเจกต์ส่งแข่ง" };

export default function Page() {
  return (
    <main className="st">
      <div className="st-wrap">
        <header className="st-head">
          <h1 className="st-display">Hams Route</h1>
          <img className="st-mascot" src={art("logo.webp")} alt="" />
          <p>อยากลองทำชิ้นแรก <span>หรือมีงานไว้ยื่นพอร์ต?</span></p>
        </header>
        <DisciplineIcons />
        <GoalSearch />

        <PackageShelf />

        <section className="st-shelf" aria-label="โปรแกรมเต็ม">
          <div className="st-shelf-h"><h2 className="st-shelf-t"><i>โปรแกรมเต็ม.</i> <span>เงื่อนไขและรอบของตัวเอง</span></h2></div>
          <div className="st-row">{PROGRAMS.map((p) => <ProgramCard key={p.id} p={p} />)}</div>
        </section>

        {DISCIPLINES.map((d) => (
          <Shelf key={d.id} label={d.name} title={`${d.name}.`} sub={d.line} more={<a className="st-link" href={LINK.disc(d.id)}>ดูหมวดนี้</a>}>
            {routesIn(d.id).map((r) => <RouteCard key={r.id} r={r} />)}
          </Shelf>
        ))}

        <section className="st-block" id="compare" aria-label="เปรียบเทียบแพ็กเกจ">
          <h2 className="st-title" style={{ marginBottom: 24 }}><i>เทียบแพ็กเกจ.</i> <span style={{ color: "var(--st-sub)" }}>ดูชิ้นงานที่ได้ก่อนเลือก</span></h2>
          <Compare />
        </section>

        <FaqAndSteps />
      </div>
      <LegacyRuntime view="shell" />
    </main>
  );
}
