"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "motion/react";
import { LINE_URL, LOGIN_URL, NAV, ROUTE, img } from "@/lib/site";

export function Header({ tone = "clear", active }: { tone?: "clear" | "solid" | "dark"; active?: string }) {
  const [open, setOpen] = useState(false);
  // over the home hero the bar is clear; once the page scrolls it becomes solid
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    if (tone !== "clear") return;
    const on = () => setScrolled(scrollY > 40);
    on();
    addEventListener("scroll", on, { passive: true });
    return () => removeEventListener("scroll", on);
  }, [tone]);
  const look = tone === "clear" && scrolled ? "solid" : tone;

  return (
    <header className={`nx-head nx-head-${look} fixed inset-x-0 top-0 z-[60]`}>
      <div className="mx-auto flex h-[60px] max-w-[1120px] items-center gap-3 px-4">
        <a href={ROUTE.home} className="mr-auto flex items-center gap-2 font-display text-[16px] font-bold">
          <img src={img("logo.webp")} alt="" width={30} height={30} />
          Hamster Hub
        </a>

        <nav aria-label="เมนูหลัก" className="hidden bg-[#fff6e8]/40 px-2 md:flex">
          {NAV.map((n) => (
            <a key={n.label} href={n.href} aria-current={active === n.label ? "page" : undefined} className="px-4 py-2 text-[15px] transition-colors hover:bg-white/60 aria-[current=page]:bg-white aria-[current=page]:font-semibold">
              {n.label}
            </a>
          ))}
        </nav>

        <a href={LINE_URL} target="_blank" rel="noopener" className="bg-line px-4 py-2 text-[15px] font-semibold text-ink">
          ทัก LINE
        </a>
        <a href={LOGIN_URL} target="_blank" rel="noopener" className="hidden bg-ink px-5 py-2 text-[15px] font-semibold text-white md:inline-block">
          เข้าสู่ระบบ
        </a>

        <button
          type="button"
          className="grid size-10 place-items-center md:hidden"
          aria-expanded={open}
          aria-controls="drawer"
          aria-label={open ? "ปิดเมนู" : "เปิดเมนู"}
          onClick={() => setOpen((o) => !o)}
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round">
            {open ? <path d="M6 6l12 12M18 6L6 18" /> : <path d="M4 8h16M4 16h16" />}
          </svg>
        </button>
      </div>

      <AnimatePresence>
        {open && (
          <motion.nav
            id="drawer"
            aria-label="เมนู"
            initial={{ opacity: 0, y: -8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.18 }}
            className="mx-4 flex flex-col bg-cream p-2 text-[17px] md:hidden"
          >
            {NAV.map((n) => (
              <a key={n.label} href={n.href} className="px-4 py-3">
                {n.label}
              </a>
            ))}
            <a href={LOGIN_URL} target="_blank" rel="noopener" className="px-4 py-3">
              เข้าสู่ระบบ
            </a>
          </motion.nav>
        )}
      </AnimatePresence>
    </header>
  );
}
