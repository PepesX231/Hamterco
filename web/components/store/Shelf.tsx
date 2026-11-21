"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";

/** A horizontal shelf: scroll, swipe, or use the two buttons. Nothing moves on its own. */
export function Shelf({ title, sub, more, children, label, top }: { title: string; sub?: string; more?: ReactNode; children: ReactNode; label: string; top?: ReactNode }) {
  const row = useRef<HTMLDivElement>(null);
  const [edge, setEdge] = useState({ start: true, end: false });
  useEffect(() => {
    const el = row.current;
    if (!el) return;
    const on = () => setEdge({ start: el.scrollLeft < 8, end: el.scrollLeft + el.clientWidth > el.scrollWidth - 8 });
    on();
    el.addEventListener("scroll", on, { passive: true });
    addEventListener("resize", on);
    return () => { el.removeEventListener("scroll", on); removeEventListener("resize", on); };
  }, []);
  const go = (dir: number) => row.current?.scrollBy({ left: dir * row.current.clientWidth * 0.8, behavior: "smooth" });
  return (
    <section className="st-shelf" aria-label={label}>
      <div className="st-shelf-h">
        <h2 className="st-shelf-t">
          <i>{title}</i>
          {sub && <span> {sub}</span>}
        </h2>
        {more}
      </div>
      {top}
      <div className="st-row" ref={row}>{children}</div>
      {!(edge.start && edge.end) && (
        <div className="st-arrows">
          <button className="st-arrow" type="button" aria-label="เลื่อนไปทางซ้าย" disabled={edge.start} onClick={() => go(-1)}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4"><path d="M15 5l-7 7 7 7" /></svg>
          </button>
          <button className="st-arrow" type="button" aria-label="เลื่อนไปทางขวา" disabled={edge.end} onClick={() => go(1)}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4"><path d="M9 5l7 7-7 7" /></svg>
          </button>
        </div>
      )}
    </section>
  );
}
