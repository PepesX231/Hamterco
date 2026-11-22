import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { LegacyRuntime } from "@/components/LegacyRuntime";
import { PackageCard, RouteCard } from "@/components/store/Cards";
import { FaqAndSteps } from "@/components/store/Info";
import { BuyBar } from "@/components/store/BuyBar";
import { LINK, PACKAGES, PENDING, PRICE_NOTE, art, baht, route, sumOf } from "@/lib/routes";
import { LINE_URL } from "@/lib/site";

export const dynamicParams = false;
export function generateStaticParams() { return PACKAGES.map((p) => ({ id: p.id })); }
export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const key = (await params).id;
  const p = PACKAGES.find((x) => x.id === key);
  return { title: p ? `${p.name} | Hams Route` : "Hams Route", description: p?.line };
}

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const key = (await params).id;
  const p = PACKAGES.find((x) => x.id === key);
  if (!p) notFound();
  const others = PACKAGES.filter((x) => x.id !== p.id);
  const apart = sumOf(p);
  return (
    <main className="st">
      <section className="st-pk-hero" aria-label={p.name} style={{ background: p.bg }}>
        <img src={art(p.img)} alt="" />
        <div className="st-wrap">
          <nav className="st-crumb" aria-label="ตำแหน่ง"><a href={LINK.store}>Hams Route</a><span aria-hidden>/</span><a href={LINK.store + "#packages"}>แพ็กเกจ</a><span aria-hidden>/</span><span>{p.name}</span></nav>
          <p style={{ marginTop: 18, fontWeight: 600, color: "#f6b26b" }}>สำหรับ {p.forWho}</p>
          <h1 className="st-display" style={{ maxWidth: "11em" }}>{p.name}</h1>
          <p style={{ marginTop: 10, fontFamily: "var(--font-display)", fontWeight: 700, fontSize: "clamp(22px,2.4vw,30px)", lineHeight: 1.25 }}>{p.hook}</p>
          <p className="st-lead" style={{ maxWidth: "32em", fontSize: "clamp(18px,1.6vw,22px)", lineHeight: 1.5, color: "rgba(255,255,255,.88)", marginTop: 14 }}>{p.line}</p>
          <div className="st-buy" id="buy">
            <span className="st-amount">{baht(p.price)}</span><span className="st-tag st-tag-dark">{PRICE_NOTE}</span>
            <span style={{ flexBasis: "100%" }} />
            <a className="st-btn st-btn-line" href={LINE_URL} target="_blank" rel="noopener">ทัก LINE สมัครแพ็กเกจนี้</a>
            <a className="st-btn st-btn-light" href="#routes">ดู Route ที่รวม</a>
          </div>
        </div>
      </section>
      <div className="st-wrap">
        <section className="st-facts" aria-label="สรุปแพ็กเกจ" style={{ marginTop: 40 }}>
          <div><small>ชิ้นงานที่ได้</small><b>{p.makes}</b></div>
          <div><small>เหมาะกับ</small><b>{p.forWho}</b></div>
          <div><small>รวม</small><b>{p.routes.length} Route</b><span className="st-note">ถ้าแยกเรียน {baht(apart)}</span></div>
          <div><small>ระยะเวลา</small><b>เช็กรอบใน LINE<span className="st-pending">{PENDING}</span></b></div>
        </section>

        <section className="st-block" id="routes" aria-label="Route ในแพ็กเกจ">
          <h2 className="st-title" style={{ marginBottom: 24 }}><i>ทำอะไรบ้าง.</i> <span style={{ color: "var(--st-sub)" }}>เรียงตามลำดับที่ทำ</span></h2>
          <div className="st-path">{p.routes.map((id) => <RouteCard key={id} r={route(id)} showDisc />)}</div>
        </section>

        <section className="st-shelf" aria-label="แพ็กเกจอื่น">
          <div className="st-shelf-h"><h2 className="st-shelf-t"><i>แพ็กเกจอื่น.</i> <span>เป้าหมายต่างกัน</span></h2></div>
          <div className="st-row">{others.map((x) => <PackageCard key={x.id} p={x} />)}</div>
        </section>
        <FaqAndSteps />
      </div>
      <BuyBar name={p.name} price={`${baht(p.price)} · ${PRICE_NOTE}`} watch="buy" />
      <LegacyRuntime view="shell" />
    </main>
  );
}
