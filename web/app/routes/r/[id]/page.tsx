import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { LegacyRuntime } from "@/components/LegacyRuntime";
import { PackageCard, RouteCard } from "@/components/store/Cards";
import { FaqAndSteps } from "@/components/store/Info";
import { BuyBar } from "@/components/store/BuyBar";
import { LINK, PENDING, PRICE_NOTE, ROUTES, baht, disc, packagesWith, routesIn, tile } from "@/lib/routes";
import { LINE_URL } from "@/lib/site";

export const dynamicParams = false;
export function generateStaticParams() { return ROUTES.map((r) => ({ id: r.id })); }
export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const key = (await params).id;
  const r = ROUTES.find((x) => x.id === key);
  return { title: r ? `${r.name} | Hams Route` : "Hams Route", description: r?.line };
}

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const key = (await params).id;
  const r = ROUTES.find((x) => x.id === key);
  if (!r) notFound();
  const d = disc(r.d);
  const inPk = packagesWith(r.id);
  const next = routesIn(r.d).filter((x) => x.id !== r.id);
  return (
    <main className="st">
      <div className="st-wrap">
        <nav className="st-crumb" aria-label="ตำแหน่ง">
          <a href={LINK.store}>Hams Route</a><span aria-hidden>/</span><a href={LINK.disc(d.id)}>{d.name}</a><span aria-hidden>/</span><span>{r.name}</span>
        </nav>
        <header className="st-hero">
          <div className="st-hero-art" style={{ background: d.tone }}><img src={tile(r.tile)} alt="" /></div>
          <div>
            <p className="st-note" style={{ fontWeight: 600 }}>Route · {d.name}</p>
            <h1 className="st-title">{r.name}</h1>
            <p className="st-lead">{r.line}</p>
            <div className="st-buy" id="buy">
              <span className="st-amount">{baht(r.price)}</span><span className="st-tag">{PRICE_NOTE}</span>
              <span style={{ flexBasis: "100%" }} />
              <a className="st-btn st-btn-line" href={LINE_URL} target="_blank" rel="noopener">ทัก LINE สมัคร Route นี้</a>
              <a className="st-btn st-btn-ghost" href={LINK.disc(d.id)}>ดู Route อื่นในหมวด</a>
            </div>
          </div>
        </header>

        <section className="st-facts" aria-label="สรุป Route">
          <div><small>จะได้ทำ</small><b>{r.line}</b></div>
          <div><small>เหมาะกับ</small><b>{inPk.length ? inPk.map((p) => p.forWho).join(" · ") : `คนที่อยาก${d.line}`}</b></div>
          <div><small>พื้นฐานที่ต้องมี</small><b>ทักถามทีมได้<span className="st-pending">{PENDING}</span></b></div>
          <div><small>ระยะเวลา</small><b>เช็กรอบใน LINE<span className="st-pending">{PENDING}</span></b></div>
        </section>

        {inPk.length > 0 && (
          <section className="st-shelf" aria-label="แพ็กเกจที่มี Route นี้">
            <div className="st-shelf-h"><h2 className="st-shelf-t"><i>อยู่ในแพ็กเกจ.</i> <span>เรียนต่อกันจนได้ชิ้นงาน</span></h2></div>
            <div className="st-row">{inPk.map((p) => <PackageCard key={p.id} p={p} />)}</div>
          </section>
        )}
        <section className="st-shelf" aria-label="Route ถัดไป">
          <div className="st-shelf-h"><h2 className="st-shelf-t"><i>ไปต่อในหมวดเดียวกัน.</i> <span>{d.name}</span></h2><a className="st-link" href={LINK.store}>กลับไปดูทั้งหมด</a></div>
          <div className="st-row">{next.map((x) => <RouteCard key={x.id} r={x} />)}</div>
        </section>
        <FaqAndSteps />
      </div>
      <BuyBar name={r.name} price={`${baht(r.price)} · ${PRICE_NOTE}`} watch="buy" />
      <LegacyRuntime view="shell" />
    </main>
  );
}
