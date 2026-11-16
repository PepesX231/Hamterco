"use client";

import { forwardRef, useEffect, useRef, useState, type CSSProperties } from "react";
import { CARDS, ROUTE, img } from "@/lib/site";

/** Real works around the headline. On phones only the cards with a phone spot show, picture only. */
export const WorkCards = forwardRef<HTMLDivElement, { play: boolean; answering?: boolean }>(function WorkCards({ play, answering }, ref) {
  return (
    <div ref={ref} aria-label="ผลงานจริงของน้องๆ" className="nx-cards" data-answering={answering || undefined}>
      {(["l", "r"] as const).map((side) => (
        <div key={side} className={`nx-col nx-${side}`}>
          {CARDS.map((c, i) => (c.side === side ? <Card key={i} c={c} i={i} play={play} /> : null))}
        </div>
      ))}
    </div>
  );
});

function Card({ c, i, play }: { c: (typeof CARDS)[number]; i: number; play: boolean }) {
  const v = useRef<HTMLVideoElement>(null);
  const [on, setOn] = useState(false);
  useEffect(() => {
    const el = v.current;
    if (!el) return;
    if (play) el.play().catch(() => {});
    else el.pause();
  }, [play]);
  const [x, y, w, r] = c.desk;
  const style = {
    "--x": `${x}%`, "--y": `${y}%`, "--w": `clamp(${Math.round(w * 0.8)}px, ${(w / 14.4).toFixed(2)}vw, ${Math.round(w * 1.2)}px)`, "--r": `${r}deg`,
    "--i": i % 3,
    ...(c.phone ? { "--mo": `${c.phone[0]}%`, "--mb": `${c.phone[1]}%`, "--mw": `${c.phone[2]}%`, "--mwx": `${Math.round(c.phone[2] * 6.6)}px`, "--mr": `${c.phone[3]}deg` } : {}),
  } as CSSProperties;
  return (
    <a href={ROUTE.works} className={`nx-card${c.phone ? (c.phone[2] < 35 ? " nx-bk" : "") : " nx-off"}`} style={style} data-side={c.side}>
      <span className="nx-m" style={{ paddingTop: `${c.ratio * 100}%` }}>
        <img src={img(c.img)} alt="" loading="lazy" decoding="async" />
        {c.clip && (
          <video ref={v} src={img(c.clip)} muted loop playsInline preload="none" aria-hidden disablePictureInPicture
            onPlaying={() => setOn(true)} style={{ opacity: on ? 1 : 0 }} />
        )}
      </span>
      {c.face && <span className="nx-av" aria-hidden style={{ backgroundImage: `url(${img(c.img)})`, backgroundPosition: `${c.face[0]}% ${c.face[1]}%` }} />}
      <b>{c.name}</b>
      <em>{c.line}</em>
    </a>
  );
}
