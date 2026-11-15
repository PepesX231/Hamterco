"use client";

import { useRef, useState } from "react";
import { motion } from "motion/react";
import { CHIPS, OLD_SITE, img } from "@/lib/site";
import { useOnScreen } from "@/lib/hooks";
import { CheeseHoles } from "./CheeseHoles";
import { TypedWish } from "./TypedWish";
import { ArrowNote, PencilLoop } from "./HandDrawn";

// Answers still come from the current site's search, which already knows every course, event and price.
const ask = (q: string) => {
  if (q.trim()) window.location.href = `${OLD_SITE}?q=${encodeURIComponent(q.trim())}#home`;
};

export function Hero() {
  const ref = useRef<HTMLElement>(null);
  const onScreen = useOnScreen(ref);
  const [focused, setFocused] = useState(false);
  const [q, setQ] = useState("");
  const searching = focused || q.length > 0;

  return (
    <section
      ref={ref}
      aria-label="ค้นหาคอร์สและกิจกรรม"
      className="relative flex min-h-[max(640px,min(100svh,900px))] flex-col items-center justify-center px-4 pb-24 pt-28 transition-colors duration-300"
      style={{
        background: searching ? "#FFFAF3" : "radial-gradient(120% 90% at 30% 10%, #FFC46B 0, #F6AE55 45%, #EE9C45 100%)",
      }}
    >
      <CheeseHoles hidden={searching} onScreen={onScreen} />
      <Crew hidden={searching} />

      <div className="relative z-10 flex w-full max-w-[860px] flex-col items-center text-center">
        <p className="font-display text-[clamp(18px,1.5vw,22px)] font-semibold text-ink/75">น้องอยาก...</p>
        <TypedWish paused={searching} />

        <form
          role="search"
          className="relative mt-7 w-full max-w-[760px]"
          onSubmit={(e) => {
            e.preventDefault();
            ask(q);
          }}
        >
          <ArrowNote hidden={searching} />
          <PencilLoop hidden={searching} />
          <label className="relative flex h-[72px] items-center gap-3 rounded-full bg-[#fffdf8]/95 pl-6 pr-2 shadow-[inset_0_1px_0_rgba(255,255,255,.9),inset_0_-8px_18px_-12px_rgba(207,109,23,.25),0_18px_40px_-18px_rgba(110,45,0,.45)]">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden>
              <circle cx="11" cy="11" r="7" />
              <path d="M20 20l-3.5-3.5" strokeLinecap="round" />
            </svg>
            <span className="sr-only">ถามเรื่องคอร์ส ค่าย พอร์ต หรือมหาลัย</span>
            <input
              value={q}
              onChange={(e) => setQ(e.target.value)}
              onFocus={() => setFocused(true)}
              onBlur={() => setFocused(false)}
              placeholder="พิมพ์คำถามได้เลย"
              className="min-w-0 flex-1 bg-transparent text-[18px] font-medium outline-none placeholder:text-ink/45"
            />
            <button type="submit" className="h-14 shrink-0 rounded-full bg-ink px-7 font-display text-[17px] font-bold text-white">
              ค้นหา
            </button>
          </label>
        </form>

        <div className="mt-4 flex w-[min(100%,860px)] flex-wrap items-center justify-center gap-2">
          <span className="text-[15px] text-ink/60">ลองพิมพ์</span>
          {CHIPS.map((c) => (
            <button
              key={c}
              type="button"
              onClick={() => ask(c)}
              className="rounded-[10px] bg-white/60 px-3 py-1.5 font-display text-[15px] font-medium text-[#3a2a1e] transition-colors hover:bg-white/90"
            >
              {c}
            </button>
          ))}
        </div>
      </div>

      <Drip />
    </section>
  );
}

/** Two hamsters peek in from the right edge. They sit flush with the edge and step back while the visitor searches. */
function Crew({ hidden }: { hidden: boolean }) {
  return (
    <motion.div aria-hidden className="pointer-events-none absolute inset-0 z-20 overflow-hidden" animate={{ opacity: hidden ? 0 : 1 }}>
      <img src={img("crew27-hang.webp")} alt="" className="absolute right-[0.4%] top-0 hidden w-[clamp(90px,10.6vw,153px)] md:block" />
      <img src={img("crew27-peek.webp")} alt="" className="absolute right-[-2.2%] top-[70%] w-[clamp(84px,9.5vw,137px)] md:top-[47%]" />
    </motion.div>
  );
}

/** The cheese melts over the edge into the page below. */
function Drip() {
  return (
    <svg aria-hidden viewBox="0 0 1440 70" preserveAspectRatio="none" className="absolute inset-x-0 top-full z-10 h-[clamp(36px,4.8vw,70px)] w-full">
      <path
        fill="#EE9C45"
        d="M0 0H1440V14C1410 14 1404 52 1388 52C1372 52 1372 18 1330 16C1270 14 1262 30 1240 30C1218 30 1214 16 1160 16C1110 16 1104 62 1086 62C1068 62 1066 18 1010 16C930 13 902 26 860 26C820 26 812 15 760 15C716 15 712 46 696 46C680 46 680 16 630 15C560 14 540 30 500 30C470 30 466 15 410 15C360 15 354 58 336 58C318 58 316 18 268 16C210 14 196 30 160 30C130 30 124 16 90 15C60 14 54 40 40 40C26 40 24 14 0 14Z"
      />
    </svg>
  );
}
