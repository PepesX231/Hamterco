"use client";

import { useEffect, useRef, useState } from "react";
import { motion } from "motion/react";
import { OLD_SITE } from "@/lib/site";
import { useMedia, useOnScreen, usePageLoaded } from "@/lib/hooks";
import { useExamples } from "@/lib/useExamples";
import { gather } from "@/lib/cardMotion";
import { TypedWish } from "./TypedWish";
import { HandNote } from "./HandDrawn";
import { WorkCards } from "./WorkCards";

// Answers still come from the current site's search, which knows every course, event and price.
const ask = (q: string) => {
  if (q.trim()) window.location.href = `${OLD_SITE}?q=${encodeURIComponent(q.trim())}#home`;
};

export function Hero() {
  const section = useRef<HTMLElement>(null);
  const cards = useRef<HTMLDivElement>(null);
  const bar = useRef<HTMLLabelElement>(null);
  const anims = useRef<Animation[]>([]);
  const onScreen = useOnScreen(section);
  const loaded = usePageLoaded();
  const desktop = useMedia("(min-width: 1100px)");
  const phone = useMedia("(max-width: 600px)");
  const { text: placeholder, current } = useExamples(phone);
  const [focused, setFocused] = useState(false);
  const [q, setQ] = useState("");

  // cards gather round (desktop) or into (phones) the bar while the visitor searches, and go back the same way
  useEffect(() => {
    if (!cards.current || !bar.current || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const list = anims.current;
    if (focused) {
      if (list.length && list[0].playbackRate < 0) { list.forEach((a) => (a.playbackRate = 1)); return; }
      if (!list.length) anims.current = gather(cards.current, bar.current, desktop);
    } else if (list.length) {
      let left = list.length;
      list.forEach((a) => {
        a.playbackRate = -1.15;
        if (a.playState === "finished") a.play();
        a.finished.then(() => { if (--left === 0 && anims.current === list && list[0].playbackRate < 0) { list.forEach((x) => x.cancel()); anims.current = []; } });
      });
    }
  }, [focused, desktop]);

  return (
    <section ref={section} aria-label="ค้นหาคอร์สและกิจกรรม" className="hero">
      <WorkCards ref={cards} play={loaded && onScreen && !focused} />

      <div className="hero-top">
        <p className="font-display text-[clamp(18px,1.5vw,22px)] font-semibold text-ink/75">น้องอยาก...</p>
        <TypedWish paused={focused} />
        <p className="hero-who">
          {["สร้างผลงานจริง", "ใช้ยื่นมหาลัย", "ต่อยอดสตาร์ทอัพ", "คว้ารางวัลระดับประเทศ"].map((t, i) => (
            <span key={t}>{i ? " " : ""}<span>{t}</span></span>
          ))}
        </p>

        <form
          role="search"
          className="hero-form"
          onSubmit={(e) => {
            e.preventDefault();
            ask(q || current.current);
          }}
        >
          <motion.label
            ref={bar}
            className="search-bar"
            animate={focused ? { y: -3, scale: 1.012 } : { y: 0, scale: 1 }}
            transition={{ type: "spring", stiffness: 380, damping: 26 }}
            data-on={focused || undefined}
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden>
              <circle cx="11" cy="11" r="7" />
              <path d="M20 20l-3.5-3.5" strokeLinecap="round" />
            </svg>
            <span className="sr-only">ถามเรื่องคอร์ส ค่าย พอร์ต หรือมหาลัย</span>
            <input
              value={q}
              onChange={(e) => setQ(e.target.value)}
              onFocus={() => setFocused(true)}
              onBlur={() => setTimeout(() => setFocused(false), 120)}
              placeholder={placeholder}
              enterKeyHint="search"
            />
            <button type="submit">ค้นหา</button>
          </motion.label>
          {/* the arrow starts under the magnifier, the first thing on the bar */}
          <HandNote hidden={focused} />
        </form>
      </div>
    </section>
  );
}
