"use client";

import { useEffect, useState } from "react";
import { createPortal } from "react-dom";
import { WINS, winCount } from "@/lib/works";

// The team's sheet of awards, placed at the end of the Hall of Fame tab on the works page once it exists.
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
  const wins = useSlot('.lg-box .yt-pane[data-p="hof"] .yt-pad', null, "sw-wins");
  return wins ? createPortal(<Wins />, wins) : null;
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
