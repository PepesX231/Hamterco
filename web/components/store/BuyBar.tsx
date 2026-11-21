"use client";

import { useEffect, useState } from "react";
import { LINE_URL } from "@/lib/site";

/** Shows once the hero's buy button has scrolled out of view, so the action stays in reach while reading. */
export function BuyBar({ name, price, watch }: { name: string; price: string; watch: string }) {
  const [on, setOn] = useState(false);
  useEffect(() => {
    const el = document.getElementById(watch);
    if (!el) return;
    const io = new IntersectionObserver(([e]) => setOn(!e.isIntersecting && e.boundingClientRect.top < 0));
    io.observe(el);
    return () => io.disconnect();
  }, [watch]);
  return (
    <div className="st-bar" data-on={on || undefined} aria-hidden={!on}>
      <div className="st-wrap">
        <b>{name}</b>
        <span>{price}</span>
        <a className="st-btn st-btn-line" href={LINE_URL} target="_blank" rel="noopener" tabIndex={on ? 0 : -1}>ทัก LINE สมัคร</a>
      </div>
    </div>
  );
}
