"use client";

import { useEffect, useState } from "react";
import { motion } from "motion/react";

const ink = { fill: "none", stroke: "#2A221D", strokeWidth: 2.2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const };

/** Handwriting under the search bar: an arrow drawn up to the bar, then the invitation written line by line. */
export function HandNote({ hidden }: { hidden: boolean }) {
  // start writing once the loading screen has gone, so the visitor sees it being written
  const [go, setGo] = useState(false);
  useEffect(() => {
    if (!document.getElementById("hhL")) { setGo(true); return; }
    const on = () => setGo(true);
    addEventListener("hh:loaded", on);
    const t = setInterval(() => { if (!document.getElementById("hhL")) on(); }, 300);
    return () => { removeEventListener("hh:loaded", on); clearInterval(t); };
  }, []);
  if (!go) return <div aria-hidden className="nx-note" />;
  return (
    <motion.div aria-hidden className="nx-note" animate={{ opacity: hidden ? 0 : 1 }} transition={{ duration: 0.2 }}>
      <svg viewBox="0 0 230 96">
        <motion.path d="M34 66 C 12 50, 10 24, 30 4" {...ink} initial={{ pathLength: 0, opacity: 0 }} animate={{ pathLength: 1, opacity: 1 }} transition={{ duration: 0.75, delay: 0.5, ease: [0.5, 0, 0.3, 1], opacity: { duration: 0.01, delay: 0.5 } }} />
        <motion.path d="M19 12 L30 3 L35 16" {...ink} initial={{ pathLength: 0, opacity: 0 }} animate={{ pathLength: 1, opacity: 1 }} transition={{ duration: 0.3, delay: 1.25, opacity: { duration: 0.01, delay: 1.25 } }} />
      </svg>
      <p>
        <motion.span initial={{ clipPath: "inset(-30% 100% -30% 0)" }} animate={{ clipPath: "inset(-30% 0% -30% 0)" }} transition={{ duration: 1, delay: 1.55, ease: "linear" }}>
          ไม่รู้จะเริ่มตรงไหน?
        </motion.span>
        <motion.span initial={{ clipPath: "inset(-30% 100% -30% 0)" }} animate={{ clipPath: "inset(-30% 0% -30% 0)" }} transition={{ duration: 0.8, delay: 2.55, ease: "linear" }}>
          ลองพิมพ์ถามดู
        </motion.span>
      </p>
    </motion.div>
  );
}
