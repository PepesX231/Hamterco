"use client";

import { useEffect, useState, type RefObject } from "react";

export function useMedia(query: string) {
  const [match, setMatch] = useState(false);
  useEffect(() => {
    const m = window.matchMedia(query);
    const on = () => setMatch(m.matches);
    on();
    m.addEventListener("change", on);
    return () => m.removeEventListener("change", on);
  }, [query]);
  return match;
}

/** True once the page has finished loading, so decorative pictures don't compete with the first paint. */
export function usePageLoaded(delay = 300) {
  const [loaded, setLoaded] = useState(false);
  useEffect(() => {
    let t: number | undefined;
    const go = () => (t = window.setTimeout(() => setLoaded(true), delay));
    if (document.readyState === "complete") go();
    else window.addEventListener("load", go, { once: true });
    return () => {
      window.removeEventListener("load", go);
      if (t) clearTimeout(t);
    };
  }, [delay]);
  return loaded;
}

export function useOnScreen(ref: RefObject<Element | null>) {
  const [on, setOn] = useState(true);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const io = new IntersectionObserver(([e]) => setOn(e.isIntersecting));
    io.observe(el);
    return () => io.disconnect();
  }, [ref]);
  return on;
}
