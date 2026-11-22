import type { Metadata } from "next";
import { LegacyRuntime } from "@/components/LegacyRuntime";
import { RouteCard } from "@/components/store/Cards";
import { GoalSearch } from "@/components/store/GoalSearch";
import { FaqAndSteps } from "@/components/store/Info";
import { PackageShelf } from "@/components/store/PackageShelf";
import { Shelf } from "@/components/store/Shelf";
import { DISCIPLINES, LINK, art, routesIn } from "@/lib/routes";

export const metadata: Metadata = { title: "Hams Route | Hamster Hub", description: "เลือกแพ็กเกจตามผลงานที่น้องอยากมี หรือฝึกทีละทักษะ" };

// Laid out as the Hams Route wireframe: title, mascot, the question; packages by goal; then each kind of Route.
export default function Page() {
  return (
    <main className="st">
      <div className="st-wrap">
        <header className="st-head">
          <h1 className="st-display">Hams Route</h1>
          <img className="st-mascot" src={art("logo.webp")} alt="" />
          <p>อยากลองทำชิ้นแรก หรือมีงานไว้ยื่นพอร์ต?</p>
        </header>
        <GoalSearch onlyWhenAsked />

        <PackageShelf />

        {DISCIPLINES.map((d) => (
          <div key={d.id} className="st-kind"><Shelf label={d.name} title={d.name} sub={d.line} more={<a className="st-link" href={LINK.disc(d.id)}>ดูทั้งหมด</a>}>
            {routesIn(d.id).map((r) => <RouteCard key={r.id} r={r} />)}
          </Shelf></div>
        ))}
        <FaqAndSteps />
      </div>
      <LegacyRuntime view="shell" />
    </main>
  );
}
