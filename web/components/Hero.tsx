"use client";

import { useEffect, useRef, useState } from "react";
import { motion } from "motion/react";
import { useMedia, useOnScreen, usePageLoaded } from "@/lib/hooks";
import { useExamples } from "@/lib/useExamples";
import { gather } from "@/lib/cardMotion";
import { TypedWish } from "./TypedWish";
import { HandNote } from "./HandDrawn";
import { WorkCards } from "./WorkCards";

// Answers come from the original search engine, which runs in the legacy part of the page (LegacyRuntime) and
// knows every course, event and price. Its answer panel is moved under this bar, inside wrappers its styles expect.
function ask(q: string, slot: HTMLElement | null, onOpen: () => void) {
  q = q.trim();
  const legacyIn = document.querySelector<HTMLInputElement>(".lg-box #zqIn");
  const legacyForm = document.querySelector<HTMLFormElement>(".lg-box #zqForm");
  const res = document.getElementById("zqRes");
  if (!q || !legacyIn || !legacyForm || !res || !slot) return;
  if (!slot.firstChild) {
    const view = document.createElement("div");
    view.setAttribute("data-view", "home");
    view.className = "on";
    const zq = document.createElement("section");
    zq.className = "zq ask sl-on hx-white";
    ["background", "padding", "margin", "min-height", "border-radius", "box-shadow", "overflow"].forEach((p) => zq.style.setProperty(p, p === "min-height" ? "0" : p === "overflow" ? "visible" : p === "background" ? "none" : "0", "important"));
    zq.style.setProperty("display", "block", "important");
    zq.appendChild(res);
    view.appendChild(zq);
    slot.appendChild(view);
  }
  legacyIn.value = q;
  legacyIn.dispatchEvent(new Event("input", { bubbles: true }));
  legacyForm.requestSubmit();
  onOpen();
}

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
  const [answering, setAnswering] = useState(false);
  const slot = useRef<HTMLDivElement>(null);
  // the panel's own close button hides it; follow that
  useEffect(() => {
    if (!answering) return;
    const res = document.getElementById("zqRes");
    if (!res) return;
    const mo = new MutationObserver(() => { if (res.hidden) setAnswering(false); });
    mo.observe(res, { attributes: true, attributeFilter: ["hidden"] });
    return () => mo.disconnect();
  }, [answering]);
  const gathered = focused || answering;

  // cards gather round (desktop) or into (phones) the bar while the visitor searches, and go back the same way
  useEffect(() => {
    if (!cards.current || !bar.current || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const list = anims.current;
    if (gathered) {
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
  }, [gathered, desktop]);

  return (
    <section ref={section} aria-label="ค้นหาคอร์สและกิจกรรม" className="nx-hero">
      <WorkCards ref={cards} play={loaded && onScreen && !gathered} answering={answering} />

      <div className="nx-hero-top">
        <p className="font-display text-[clamp(18px,1.5vw,22px)] font-semibold text-ink/75">น้องอยาก...</p>
        <TypedWish paused={focused} />
        <p className="nx-hero-who">
          {["สร้างผลงานจริง", "ใช้ยื่นมหาลัย", "ต่อยอดสตาร์ทอัพ", "คว้ารางวัลระดับประเทศ"].map((t, i) => (
            <span key={t}>{i ? " " : ""}<span>{t}</span></span>
          ))}
        </p>

        <form
          role="search"
          className="nx-hero-form"
          onSubmit={(e) => {
            e.preventDefault();
            ask(q || current.current, slot.current, () => setAnswering(true));
          }}
        >
          <motion.label
            ref={bar}
            className="nx-bar"
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
          <HandNote hidden={gathered} />
        </form>
        <div ref={slot} className="nx-answer" />
      </div>
    </section>
  );
}
