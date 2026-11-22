import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { LegacyRuntime } from "@/components/LegacyRuntime";
import { DisciplineIcons, PackageCard, RouteCard } from "@/components/store/Cards";
import { FaqAndSteps } from "@/components/store/Info";
import { DISCIPLINES, LINK, PACKAGES, route, routesIn, tile } from "@/lib/routes";

export const dynamicParams = false;
export function generateStaticParams() { return DISCIPLINES.map((d) => ({ d: d.id })); }

export async function generateMetadata({ params }: { params: Promise<{ d: string }> }): Promise<Metadata> {
  const key = (await params).d;
  const d = DISCIPLINES.find((x) => x.id === key);
  return { title: d ? `${d.name} | Hams Route` : "Hams Route" };
}

export default async function Page({ params }: { params: Promise<{ d: string }> }) {
  const key = (await params).d;
  const d = DISCIPLINES.find((x) => x.id === key);
  if (!d) notFound();
  const pk = PACKAGES.filter((p) => p.routes.some((r) => route(r).d === d.id));
  return (
    <main className="st">
      <div className="st-wrap">
        <nav className="st-crumb" aria-label="ตำแหน่ง"><a href={LINK.store}>Hams Route</a><span aria-hidden>/</span><span>{d.name}</span></nav>
        <header className="st-hero" style={{ paddingBottom: 24 }}>
          <div>
            <h1 className="st-display">{d.name}</h1>
            <p className="st-lead">{d.line} เลือกเรียนทีละ Route หรือเลือกแพ็กเกจที่รวมไว้แล้ว</p>
          </div>
          <div className="st-hero-art" style={{ background: d.tone, maxWidth: 420, justifySelf: "end", width: "100%" }}><img src={tile(d.tile)} alt="" /></div>
        </header>
        <DisciplineIcons current={d.id} />
        <section className="st-shelf" aria-label={`Route ในหมวด ${d.name}`}>
          <div className="st-shelf-h"><h2 className="st-shelf-t"><i>Route ในหมวดนี้.</i> <span>{routesIn(d.id).length} เส้น</span></h2></div>
          <div className="st-grid">{routesIn(d.id).map((r) => <RouteCard key={r.id} r={r} />)}</div>
        </section>
        {pk.length > 0 && (
          <section className="st-shelf" aria-label="แพ็กเกจที่ใช้ Route หมวดนี้">
            <div className="st-shelf-h"><h2 className="st-shelf-t"><i>แพ็กเกจที่ใช้หมวดนี้.</i> <span>ไปให้ถึงชิ้นงาน</span></h2></div>
            <div className="st-row">{pk.map((p) => <PackageCard key={p.id} p={p} />)}</div>
          </section>
        )}
        <FaqAndSteps />
      </div>
      <LegacyRuntime view="shell" />
    </main>
  );
}
