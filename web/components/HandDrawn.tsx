"use client";

import { motion } from "motion/react";

const ink = { fill: "none", stroke: "#2A221D", strokeWidth: 2.2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const };

/** Handwriting under the search bar: an arrow drawn up to the bar, then the invitation written line by line. */
export function HandNote({ hidden }: { hidden: boolean }) {
  return (
    <motion.div aria-hidden className="hand-note" animate={{ opacity: hidden ? 0 : 1 }} transition={{ duration: 0.2 }}>
      <svg viewBox="0 0 230 96">
        <motion.path d="M34 66 C 12 50, 10 24, 30 4" {...ink} initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.75, delay: 1.2, ease: [0.5, 0, 0.3, 1] }} />
        <motion.path d="M19 12 L30 3 L35 16" {...ink} initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.3, delay: 1.95 }} />
      </svg>
      <p>
        <motion.span initial={{ clipPath: "inset(-30% 100% -30% 0)" }} animate={{ clipPath: "inset(-30% 0% -30% 0)" }} transition={{ duration: 1, delay: 2.25, ease: "linear" }}>
          ไม่รู้จะเริ่มตรงไหน?
        </motion.span>
        <motion.span initial={{ clipPath: "inset(-30% 100% -30% 0)" }} animate={{ clipPath: "inset(-30% 0% -30% 0)" }} transition={{ duration: 0.8, delay: 3.25, ease: "linear" }}>
          ลองพิมพ์ถามดู
        </motion.span>
      </p>
    </motion.div>
  );
}
