"use client";

import { motion } from "motion/react";

const pencil = { stroke: "#2a221d", strokeWidth: 2.2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const, fill: "none" };

/** Desktop: a pencil arrow is drawn toward the search bar, then the note is written above its curve. */
export function ArrowNote({ hidden }: { hidden: boolean }) {
  return (
    <motion.div
      aria-hidden
      animate={{ opacity: hidden ? 0 : 1 }}
      transition={{ duration: 0.25 }}
      className="pointer-events-none absolute right-[calc(100%+12px)] top-[-96px] hidden w-[300px] min-[1180px]:block"
    >
      <svg viewBox="0 0 300 150" className="w-full overflow-visible">
        <defs>
          <filter id="rough">
            <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="3" />
            <feDisplacementMap in="SourceGraphic" scale="1.6" />
          </filter>
        </defs>
        <g filter="url(#rough)">
          <motion.path
            d="M14 18 C 40 70, 90 128, 270 128"
            {...pencil}
            initial={{ pathLength: 0 }}
            animate={{ pathLength: 1 }}
            transition={{ duration: 0.9, delay: 0.6, ease: [0.5, 0, 0.3, 1] }}
          />
          <motion.path
            d="M256 118 L272 128 L256 137"
            {...pencil}
            initial={{ pathLength: 0 }}
            animate={{ pathLength: 1 }}
            transition={{ duration: 0.25, delay: 1.5 }}
          />
        </g>
      </svg>
      <motion.p
        className="absolute left-[78px] top-[18px] -rotate-[4deg] font-hand text-[21.6px] font-bold leading-[1.35] text-[#2a221d]"
        initial={{ clipPath: "inset(0 100% 0 0)" }}
        animate={{ clipPath: "inset(0 0% 0 0)" }}
        transition={{ duration: 1.1, delay: 1.8, ease: "linear" }}
      >
        ไม่รู้จะเริ่มตรงไหน?
        <br />
        ลองถามดู
      </motion.p>
    </motion.div>
  );
}

/** Phones: a pencil loop is drawn around the search bar instead, since there is no room beside it. */
export function PencilLoop({ hidden }: { hidden: boolean }) {
  return (
    <motion.svg
      aria-hidden
      viewBox="0 0 400 100"
      preserveAspectRatio="none"
      className="pointer-events-none absolute -inset-x-4 -inset-y-3 h-[calc(100%+24px)] w-[calc(100%+32px)] overflow-visible min-[1180px]:hidden"
      animate={{ opacity: hidden ? 0 : 1 }}
    >
      <motion.path
        d="M200 6 C 330 4, 396 22, 396 50 C 396 80, 320 95, 200 95 C 80 95, 4 80, 4 50 C 4 22, 70 6, 190 8 C 250 9, 300 12, 330 16"
        {...pencil}
        strokeWidth={1.6}
        vectorEffect="non-scaling-stroke"
        initial={{ pathLength: 0 }}
        animate={{ pathLength: 1 }}
        transition={{ duration: 1.2, delay: 0.7, ease: [0.5, 0, 0.3, 1] }}
      />
    </motion.svg>
  );
}
