"use client";

import { useEffect, useRef, useState, type CSSProperties } from "react";
import { motion } from "motion/react";
import { HOLES, OLD_SITE, img, type Hole } from "@/lib/site";
import { useMedia, usePageLoaded } from "@/lib/hooks";

type Props = { hidden: boolean; onScreen: boolean };

/** The cheese holes. Each is a window onto a real work; works with a clip play it while the hero is on screen. */
export function CheeseHoles({ hidden, onScreen }: Props) {
  const phone = useMedia("(max-width: 700px)");
  const loaded = usePageLoaded();

  return (
    <motion.div
      aria-label="ผลงานของน้องๆ"
      className="absolute inset-0 z-0 overflow-hidden"
      animate={{ opacity: hidden ? 0 : 1 }}
      transition={{ duration: 0.3 }}
      style={{ pointerEvents: hidden ? "none" : undefined }}
    >
      {HOLES.map((h, i) => {
        if (phone && h.phone === false) return null;
        const [x, y] = phone && h.phone ? h.phone : [h.x, h.y];
        return <HoleView key={i} hole={h} x={x} y={y} loaded={loaded} play={loaded && onScreen && !hidden} />;
      })}
    </motion.div>
  );
}

function HoleView({ hole, x, y, loaded, play }: { hole: Hole; x: number; y: number; loaded: boolean; play: boolean }) {
  const video = useRef<HTMLVideoElement>(null);
  const [ready, setReady] = useState(false);
  const s = `clamp(${hole.size * 0.55}px, ${(hole.size / 14.4).toFixed(3)}vw, ${hole.size * 1.25}px)`;
  // The name sits under the hole; near a screen edge it hugs the inner side so it is never cut off.
  const align = x < 15 ? "left-[20%]" : x > 85 ? "right-[20%]" : "left-1/2 -translate-x-1/2";

  useEffect(() => {
    const v = video.current;
    if (!v) return;
    if (play) v.play().catch(() => {});
    else v.pause();
  }, [play]);

  return (
    <div
      className="group absolute -translate-x-1/2 -translate-y-1/2"
      style={{ left: `${x}%`, top: `${y}%`, width: s, height: `calc(${s} * .9)`, "--s": s } as CSSProperties}
    >
      <a href={`${OLD_SITE}#works`} aria-label={hole.name} className="hole relative block size-full overflow-hidden focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-crust">
        {loaded && (
          <motion.img
            src={img(hole.img)}
            alt=""
            className="absolute inset-0 size-full rounded-full object-cover"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6 }}
          />
        )}
        {loaded && hole.clip && (
          <motion.video
            ref={video}
            src={img(hole.clip)}
            muted
            loop
            playsInline
            preload="none"
            aria-hidden
            onPlaying={() => setReady(true)}
            className="absolute inset-0 size-full rounded-full object-cover"
            initial={{ opacity: 0 }}
            animate={{ opacity: ready ? 1 : 0 }}
            transition={{ duration: 0.5 }}
          />
        )}
        <span className="hole-ring absolute inset-0" />
      </a>
      <span
        className={`pointer-events-none absolute top-full mt-1 whitespace-nowrap text-[13px] font-semibold text-crust opacity-0 transition-[opacity,margin] duration-200 group-hover:mt-2 group-hover:opacity-100 group-focus-within:opacity-100 [@media(hover:none)]:hidden ${align}`}
      >
        {hole.name}
      </span>
    </div>
  );
}
