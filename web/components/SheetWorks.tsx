"use client";

import { useEffect, useState } from "react";
import { createPortal } from "react-dom";
import { MADE, WINS, winCount } from "@/lib/works";

// The team's sheet of projects and awards, placed inside two legacy sections once they exist:
// the made-and-used shelf at the end of "สิ่งที่ Hamster Hub สร้าง", the full awards list inside Hall of Fame.
function useSlot(host: string, before: string | null, cls: string) {
  const [el, setEl] = useState<HTMLElement | null>(null);
  useEffect(() => {
    let made: HTMLElement | null = null, t = 0;
    const tryMount = () => {
      const h = document.querySelector<HTMLElement>(host);
      if (!h) { t = window.setTimeout(tryMount, 200); return; }
      made = document.createElement("div");
      made.className = cls;
      const ref = before ? h.querySelector(before) : null;
      if (ref) ref.parentNode!.insertBefore(made, ref); else h.appendChild(made);
      setEl(made);
    };
    tryMount();
    return () => { clearTimeout(t); made?.remove(); };
  }, [host, before, cls]);
  return el;
}

export function SheetWorks() {
  const made = useSlot(".lg-box section.hbx .oc-in", null, "sw-made");
  const wins = useSlot(".lg-box section.h5f", ".h5f-go", "sw-wins");
  return (
    <>
      {made && createPortal(<Made />, made)}
      {wins && createPortal(<Wins />, wins)}
    </>
  );
}

function Made() {
  return (
    <div className="sw-m">
      <h3>ใช้งานจริง ขายได้ และเปิดให้คนเล่นแล้ว</h3>
      <ul className="sw-row">
        {MADE.map((m) => {
          const body = (
            <>
              <span className="sw-im" data-plain={m.img ? undefined : ""}>
                {m.img ? <img src={m.img} alt="" loading="lazy" decoding="async" /> : <b>{m.name}</b>}
              </span>
              <small>{m.tag}</small>
              <b>{m.name}</b>
              <span>{m.what} · น้อง{m.by}</span>
            </>
          );
          return <li key={m.name}>{m.href ? <a href={m.href} target="_blank" rel="noopener">{body}</a> : <div>{body}</div>}</li>;
        })}
      </ul>
    </div>
  );
}

function Wins() {
  return (
    <div className="sw-w">
      <h3>รางวัลทั้งหมดของน้องๆ <span>{winCount} ผลงาน จากเวทีระดับประเทศและนานาชาติ</span></h3>
      <div className="sw-g">
        {WINS.map((s) => (
          <section key={s.stage} aria-label={s.stage}>
            <h4>{s.stage}{s.full && <small>{s.full}</small>}</h4>
            <ul>
              {s.wins.map((w, i) => {
                const row = (<><em data-top={w.rank === "รอบชิง" || w.rank.startsWith("Top") ? undefined : ""}>{w.rank}</em><b>{w.name || "ผลงาน"}<span>น้อง{w.by}</span></b></>);
                return <li key={i}>{w.href ? <a href={w.href} target="_blank" rel="noopener" aria-label={`${w.name} น้อง${w.by} ${w.rank} เปิดคลิป`}>{row}<i aria-hidden>ดู</i></a> : <div>{row}</div>}</li>;
              })}
            </ul>
          </section>
        ))}
      </div>
    </div>
  );
}
