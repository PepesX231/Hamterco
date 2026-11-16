"use client";

import { useEffect, useRef } from "react";

/**
 * Runs the parts of the old page that are not yet React components (see dev/builds/legacy_next.py).
 * It loads the old styles, puts the old markup in, opens the old page on `view`, then runs the old scripts one by one.
 * Hash links between views ("#works") become Next.js routes. Each part moved to React is hidden here via `hide`.
 */
const BASE = "/Hamterco/next";
const ROUTES: Record<string, string> = { home: "/", courses: "/courses/", activity: "/activity/", works: "/works/", about: "/about/" };

let started = false;

export function LegacyRuntime({ view, hide = [] }: { view: keyof typeof ROUTES; hide?: string[] }) {
  const box = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (started || !box.current) return;
    started = true;
    const el = box.current;
    let cancelled = false;

    // the old scripts wait for these events; the page has already loaded, so fire them straight away
    const patch = (target: Document | Window) => {
      const orig = target.addEventListener.bind(target);
      (target as Window).addEventListener = ((type: string, fn: EventListenerOrEventListenerObject, opts?: boolean | AddEventListenerOptions) => {
        if (type === "DOMContentLoaded" || (type === "load" && target === window)) {
          setTimeout(() => (typeof fn === "function" ? fn.call(target, new Event(type)) : fn.handleEvent(new Event(type))), 0);
          return;
        }
        return orig(type, fn, opts);
      }) as typeof window.addEventListener;
    };

    const load = (tag: "link" | "script", url: string) =>
      new Promise<void>((done) => {
        const n = document.createElement(tag);
        if (tag === "link") { (n as HTMLLinkElement).rel = "stylesheet"; (n as HTMLLinkElement).href = url; }
        else { (n as HTMLScriptElement).src = url; (n as HTMLScriptElement).async = false; }
        n.onload = n.onerror = () => done();
        document.head.appendChild(n);
      });

    (async () => {
      const manifest: { fonts: string[]; scripts: string[] } = await (await fetch(`${BASE}/legacy/manifest.json`)).json();
      manifest.fonts.forEach((f) => load("link", f));
      await new Promise<void>((done) => {
        const st = document.createElement("style");
        st.textContent = `@import url("${BASE}/legacy/legacy.css") layer(legacy);`;
        st.onload = st.onerror = () => done();
        document.head.appendChild(st);
        setTimeout(done, 4000);
      });
      const html = await (await fetch(`${BASE}/legacy/body.html`)).text();
      if (cancelled) return;
      history.replaceState(history.state, "", location.pathname + location.search + "#" + view);
      el.innerHTML = html;
      const nav = el.querySelector("header.nav");
      if (nav) document.body.insertBefore(nav, document.body.firstChild);
      const pt = el.querySelector("#pt");
      if (pt) document.body.insertBefore(pt, nav ? nav.nextSibling : document.body.firstChild);
      const home = el.querySelector('[data-view="home"]');
      const mark = () => { document.documentElement.dataset.nxView = home && home.classList.contains("on") ? "home" : "other"; };
      if (home) new MutationObserver(mark).observe(home, { attributes: true, attributeFilter: ["class", "hidden", "style"] });
      patch(document);
      patch(window);
      for (const s of manifest.scripts) await load("script", s.startsWith("http") ? s : `${BASE}/legacy/${s}`);
      el.dataset.ready = "1";
      if (home) setTimeout(() => { const m = () => { document.documentElement.dataset.nxView = home.classList.contains("on") ? "home" : "other"; }; m(); }, 0);
    })();

    // Moving between views works as on the original site: the old header and its page transition swap views in place.
    // Only the home view lives in React, so "#home" from another page loads the home route.
    const onClick = (e: MouseEvent) => {
      const a = (e.target as Element).closest?.("a[href^='#']") as HTMLAnchorElement | null;
      if (!a) return;
      const v = a.getAttribute("href")!.slice(1).split(/[?&]/)[0];
      if (v === "home" && view !== "home") {
        e.preventDefault();
        e.stopImmediatePropagation();
        location.href = BASE + "/";
      }
    };
    document.addEventListener("click", onClick, true);
    // keep the address bar on the route of the view that is showing, so a reload opens the same page
    const onHash = () => {
      const v = location.hash.slice(1).split(/[?&]/)[0];
      if (ROUTES[v]) history.replaceState(history.state, "", BASE + ROUTES[v] + location.search + location.hash);
    };
    addEventListener("hashchange", onHash);
    return () => { cancelled = true; document.removeEventListener("click", onClick, true); removeEventListener("hashchange", onHash); };
  }, [view]);

  return (
    <>
      <style>{`.lg-box #hhL{display:none!important}html[data-nx-view=other] .nx-home{display:none!important}${hide.map((h) => `.lg-box ${h}{display:none!important}`).join("")}`}</style>
      <div ref={box} className="lg-box" />
    </>
  );
}
