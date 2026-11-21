import { DISCIPLINES, LINK, PRICE_NOTE, art, baht, disc, route, tile, type Package, type Program, type Route } from "@/lib/routes";

const Plus = () => (
  <span className="st-plus" aria-hidden>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.6" strokeLinecap="square"><path d="M9 5l7 7-7 7" /></svg>
  </span>
);

/** A package: the picture is the card. Who it's for, its name, what you get, then the price. */
export function PackageCard({ p }: { p: Package }) {
  return (
    <a className="st-pk" href={LINK.pkg(p.id)} aria-label={`${p.name} ${baht(p.price)} ${PRICE_NOTE}`}>
      <img src={art(p.img)} alt="" loading="lazy" decoding="async" />
      <span className="st-pk-t">
        <small>สำหรับ {p.forWho}</small>
        <b>{p.name}</b>
        <i>
          {baht(p.price)} · รวม {p.routes.length} Route <span className="st-tag st-tag-dark">{PRICE_NOTE}</span>
        </i>
      </span>
      <Plus />
    </a>
  );
}

/** A single Route: name, price, and the clay piece that stands for what you make. */
export function RouteCard({ r, showDisc = false }: { r: Route; showDisc?: boolean }) {
  return (
    <a className="st-card" href={LINK.route(r.id)} aria-label={`${r.name} ${baht(r.price)} ${PRICE_NOTE}`}>
      {showDisc && <small>{disc(r.d).name}</small>}
      <b>{r.name}</b>
      <em>{r.line}</em>
      <span className="st-price"><b>{baht(r.price)}</b> <span className="st-tag">{PRICE_NOTE}</span></span>
      <img src={tile(r.tile)} alt="" loading="lazy" decoding="async" />
      <Plus />
    </a>
  );
}

export function ProgramCard({ p }: { p: Program }) {
  return (
    <a className="st-prog" href={p.href} target="_blank" rel="noopener">
      <img src={p.img} alt="" loading="lazy" decoding="async" />
      <div>
        <small>สำหรับ {p.forWho}</small>
        <b>{p.name}</b>
        <p>{p.line}</p>
        <dl>
          {p.facts.map(([a, b]) => (
            <div key={a}><dt>{a}</dt><dd>{b}</dd></div>
          ))}
        </dl>
        <p style={{ fontSize: 13, marginTop: 14, color: "rgba(255,255,255,.7)" }}>{p.status}</p>
      </div>
    </a>
  );
}

/** Apple Store's product icon row, with the clay pieces: one per kind of skill. */
export function DisciplineIcons({ current }: { current?: string }) {
  return (
    <nav className="st-icons" aria-label="หมวดของ Hams Route">
      {DISCIPLINES.map((d) => (
        <a key={d.id} className="st-ic" href={LINK.disc(d.id)} aria-current={current === d.id ? "page" : undefined}>
          <img src={tile(d.tile)} alt="" />
          <b>{d.name}</b>
        </a>
      ))}
    </nav>
  );
}

export const routeList = (ids: string[]) => ids.map(route);
