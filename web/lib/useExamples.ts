"use client";

import { useEffect, useRef, useState } from "react";
import { EXAMPLES } from "./site";

const seg = (t: string) =>
  typeof Intl !== "undefined" && "Segmenter" in Intl
    ? Array.from(new Intl.Segmenter("th", { granularity: "grapheme" }).segment(t), (s) => s.segment)
    : [...t];
const wait = (ms: number) => new Promise((r) => setTimeout(r, ms));

/** The bar's placeholder: an invitation, then example questions typed one by one. Returns the text and the example showing. */
export function useExamples(phone: boolean) {
  const [text, setText] = useState("");
  const current = useRef("");
  useEffect(() => {
    let alive = true;
    const invite = phone ? "อยากรู้อะไร ถามได้เลย" : "อยากรู้อะไร พิมพ์ถามได้เลย เรามีคำตอบ";
    const pre = phone ? "" : "ลองพิมพ์ “";
    const post = phone ? "" : "”";
    const type = async (full: string, from = 0) => {
      const g = seg(full);
      for (let i = from; i <= g.length && alive; i++) { setText(g.slice(0, i).join("")); await wait(70); }
    };
    const erase = async (full: string, to = 0) => {
      const g = seg(full);
      for (let i = g.length; i >= to && alive; i--) { setText(g.slice(0, i).join("")); await wait(32); }
    };
    (async () => {
      setText(invite);
      await wait(3200);
      let k = 0, last = invite;
      while (alive) {
        const ex = EXAMPLES[k++ % EXAMPLES.length];
        const full = pre + ex + post;
        await erase(last);
        await type(full);
        current.current = ex;
        await wait(2300);
        current.current = "";
        last = full;
        if (k % EXAMPLES.length === 0) { await erase(last); await type(invite); last = invite; await wait(2800); }
      }
    })();
    return () => { alive = false; };
  }, [phone]);
  return { text, current };
}
