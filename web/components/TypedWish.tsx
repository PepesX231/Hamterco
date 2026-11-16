"use client";

import { useEffect, useMemo, useState } from "react";
import { WISHES } from "@/lib/site";

// Split by grapheme so Thai vowels and tone marks are never typed on their own.
const split = (t: string) =>
  typeof Intl !== "undefined" && "Segmenter" in Intl
    ? [...new Intl.Segmenter("th", { granularity: "grapheme" }).segment(t)].map((s) => s.segment)
    : [...t];

/** "น้องอยาก… <wish>": types one wish, holds it, deletes it, moves on. Pauses while the visitor is searching. */
export function TypedWish({ paused }: { paused: boolean }) {
  const parts = useMemo(() => WISHES.map(split), []);
  const [wi, setWi] = useState(0);
  const [n, setN] = useState(parts[0].length);
  const [deleting, setDeleting] = useState(false);

  useEffect(() => {
    if (paused) return;
    const full = parts[wi].length;
    let delay = deleting ? 38 : 75;
    if (!deleting && n === full) delay = 1900;
    if (deleting && n === 0) delay = 260;
    const t = setTimeout(() => {
      if (!deleting && n === full) setDeleting(true);
      else if (deleting && n === 0) {
        setDeleting(false);
        setWi((w) => (w + 1) % parts.length);
      } else setN((c) => c + (deleting ? -1 : 1));
    }, delay);
    return () => clearTimeout(t);
  }, [paused, wi, n, deleting, parts]);

  return (
    <h1 className="font-headline text-[clamp(34px,4.9vw,72px)] font-black leading-[1.3] tracking-[-0.02em] text-[#1d1611]">
      <span className="sr-only">{WISHES.join(", ")}</span>
      <span aria-hidden>{(paused ? parts[wi] : parts[wi].slice(0, n)).join("")}</span>
      <i aria-hidden className="ml-1 inline-block h-[0.9em] w-[3px] translate-y-[0.12em] animate-[blink_1s_steps(1)_infinite] bg-[#c8631b]" />
    </h1>
  );
}
