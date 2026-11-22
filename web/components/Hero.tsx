"use client";

import { useEffect, useRef, useState } from "react";
import { motion } from "motion/react";
import { useMedia, useOnScreen, usePageLoaded } from "@/lib/hooks";
import { useExamples } from "@/lib/useExamples";
import { gather } from "@/lib/cardMotion";
import { TypedWish } from "./TypedWish";
import { HandNote } from "./HandDrawn";
import { WorkCards } from "./WorkCards";
import { LINK, baht, findForGoal, tile, art } from "@/lib/routes";
import { understand } from "@/lib/understand";

// Answers come from the original search engine, which runs in the legacy part of the page (LegacyRuntime) and
// knows every course, event and price. Its answer panel is moved under this bar, inside wrappers its styles expect.
// When it cannot read a question, lib/understand names the topic and the engine is asked again in its own words.
function runLegacy(q: string) {
  const legacyIn = document.querySelector<HTMLInputElement>(".lg-box #zqIn");
  const legacyForm = document.querySelector<HTMLFormElement>(".lg-box #zqForm");
  const res = document.getElementById("zqRes");
  if (!legacyIn || !legacyForm || !res) return null;
  legacyIn.value = q;
  legacyIn.dispatchEvent(new Event("input", { bubbles: true }));
  legacyForm.requestSubmit();
  return (res.querySelector<HTMLElement>(".sx-card")?.dataset.sx) || "answer";
}

const GAVE_UP = new Set(["unknown", "foreign", "shape", "want", "num"]);

/** Answers q in the legacy panel. Returns the words to match Hams Route with, and what happened (for tests). */
export function solveQuery(raw: string): { match: string; kind: string } {
  const res = document.getElementById("zqRes");
  let kind = runLegacy(raw);
  if (!kind || !res) return { match: raw, kind: "none" };
  if (!GAVE_UP.has(kind)) return { match: raw, kind };
  const r = understand(raw);
  const it = r.intent;
  if (it?.ask) {
    kind = runLegacy(it.ask) || kind;
    // keep what the visitor typed in the "answer for" line
    const echo = res.querySelector(".ia-q bdi");
    if (echo) echo.textContent = raw.length > 56 ? raw.slice(0, 55) + "…" : raw;
    return { match: [it.routes, r.text].filter(Boolean).join(" "), kind: "re:" + it.id + ":" + kind };
  }
  const card = res.querySelector<HTMLElement>(".sx-card");
  const h = card?.querySelector("h3"), a = card?.querySelector(".ia-a");
  if (it && h && a) {
    // things only Hams Route teaches (3D, the 12-month programme): the Routes show right under this card
    h.textContent = "เรื่องนี้เรียนได้ใน Hams Route";
    a.textContent = "Route ที่ตรงกับคำถามอยู่ข้างล่าง กดดูชิ้นงานที่จะได้ทำและราคาได้เลย";
    card!.querySelectorAll(".ia-k, .sx-ch").forEach((x) => x.remove());
    return { match: [it.routes, r.text].filter(Boolean).join(" "), kind: "route:" + it.id };
  }
  if (kind === "unknown" && h && a) {
    h.textContent = r.mash ? "แป้นพิมพ์อาจเป็นอีกภาษาอยู่" : "ยังไม่เข้าใจคำนี้";
    a.textContent = r.mash
      ? "ลองสลับภาษาแป้นพิมพ์แล้วพิมพ์ใหม่ หรือเลือกเรื่องที่ใกล้ที่สุดข้างล่าง"
      : "ลองพิมพ์สิ่งที่น้องอยากทำ เช่น อยากทำเกม หรือค่าเรียนเท่าไหร่ หรือเลือกเรื่องที่ใกล้ที่สุดข้างล่าง";
  }
  return { match: raw, kind };
}

function ask(q: string, slot: HTMLElement | null, onOpen: () => void) {
  q = q.trim();
  const res = document.getElementById("zqRes");
  if (!q || !res || !slot) return q;
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
  const out = solveQuery(q);
  onOpen();
  return out.match;
}

if (typeof window !== "undefined") (window as unknown as { __hhSolve: typeof solveQuery }).__hhSolve = solveQuery;

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
  const [askedQ, setAskedQ] = useState("");
  const [matchQ, setMatchQ] = useState("");
  const slot = useRef<HTMLDivElement>(null);
  const formRef = useRef<HTMLFormElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const [follow, setFollow] = useState(false);
  // once the big bar scrolls away, a small one follows at the top of the screen
  useEffect(() => {
    const f = formRef.current;
    if (!f) return;
    const io = new IntersectionObserver(([e]) => setFollow(!e.isIntersecting && e.boundingClientRect.top < 0), { rootMargin: "-60px 0px 0px 0px" });
    io.observe(f);
    return () => io.disconnect();
  }, []);
  const askFromTop = (v: string) => {
    v = v.trim();
    if (!v) return;
    setQ(v);
    const m = ask(v, slot.current, () => setAnswering(true));
    setAskedQ(v); setMatchQ(m);
    const top = (formRef.current?.getBoundingClientRect().top || 0) + scrollY - 90;
    scrollTo({ top, behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  };
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

        <form
          ref={formRef}
          role="search"
          className="nx-hero-form"
          onSubmit={(e) => {
            e.preventDefault();
            { const v = q || current.current; const m = ask(v, slot.current, () => setAnswering(true)); setAskedQ(v); setMatchQ(m); }
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
              ref={inputRef}
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
        {answering && <RouteMatches q={askedQ} match={matchQ} />}
      </div>
      <FollowBar show={follow} placeholder={placeholder} onAsk={askFromTop} />
    </section>
  );
}

/** The search bar that follows the visitor down the home page. Asking scrolls back up to the answer. */
function FollowBar({ show, placeholder, onAsk }: { show: boolean; placeholder: string; onAsk: (v: string) => void }) {
  const [v, setV] = useState("");
  return (
    <form
      role="search"
      className="nx-follow"
      data-show={show || undefined}
      aria-hidden={!show}
      onSubmit={(e) => { e.preventDefault(); onAsk(v); setV(""); (document.activeElement as HTMLElement | null)?.blur(); }}
    >
      <label>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden><circle cx="11" cy="11" r="7" /><path d="M20 20l-3.5-3.5" strokeLinecap="round" /></svg>
        <span className="sr-only">ถามเรื่องคอร์ส ค่าย พอร์ต หรือมหาลัย</span>
        <input value={v} onChange={(e) => setV(e.target.value)} placeholder={placeholder} enterKeyHint="search" tabIndex={show ? 0 : -1} />
        <button type="submit" tabIndex={show ? 0 : -1}>ค้นหา</button>
      </label>
    </form>
  );
}

/** Above the answer: the Hams Route packages and Routes that match the question, if any. */
function RouteMatches({ q, match }: { q: string; match: string }) {
  const f = findForGoal(match || q);
  if (!f.understood) return null;
  const items = [
    ...f.programs.map((p) => ({ k: "g" + p.id, href: p.href, img: p.img, name: p.name, sub: `โปรแกรมเต็ม · ${p.price}` })),
    ...f.packages.map((p) => ({ k: "p" + p.id, href: LINK.pkg(p.id), img: art(p.img), name: p.name, sub: `แพ็กเกจ · ${baht(p.price)}` })),
    ...f.routes.slice(0, 6).map((r) => ({ k: "r" + r.id, href: LINK.route(r.id), img: tile(r.tile), name: r.name, sub: `Route · ${baht(r.price)}` })),
  ].slice(0, 6);
  return (
    <div className="hm-found nx-found">
      <h3>Hams Route ที่ตรงกับ “{q}”</h3>
      <ul>{items.map((i) => <li key={i.k}><a href={i.href}><img src={i.img} alt="" /><span><b>{i.name}</b><span>{i.sub}{i.k[0] === "g" ? "" : " · ราคาตัวอย่าง"}</span></span></a></li>)}</ul>
    </div>
  );
}
