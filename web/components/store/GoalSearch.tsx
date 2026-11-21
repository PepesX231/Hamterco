"use client";

import { useEffect, useMemo, useState } from "react";
import { GOAL_EXAMPLES, findForGoal } from "@/lib/routes";
import { LINE_URL } from "@/lib/site";
import { PackageCard, ProgramCard, RouteCard } from "./Cards";

/** Ask from your goal ("อยากทำเกมไว้ยื่นพอร์ต") and see the Packages and Routes that lead there. */
export function GoalSearch() {
  const [q, setQ] = useState("");
  // ?q= from Home or a shared link
  useEffect(() => {
    const v = new URLSearchParams(location.search).get("q");
    if (v) setQ(v);
  }, []);
  const found = useMemo(() => findForGoal(q), [q]);
  const asked = q.trim().length > 0;
  return (
    <div className="st-search">
      <form role="search" onSubmit={(e) => e.preventDefault()}>
        <label className="st-field">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden><circle cx="11" cy="11" r="7" /><path d="M20 20l-3.5-3.5" /></svg>
          <span className="sr-only">บอกเป้าหมายของน้อง</span>
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="บอกเป้าหมาย เช่น อยากทำเกมไว้ยื่นพอร์ต" enterKeyHint="search" />
          {asked && <button type="button" className="st-btn st-btn-ghost" style={{ minHeight: 40, padding: "0 14px" }} onClick={() => setQ("")}>ล้าง</button>}
        </label>
      </form>
      {!asked && (
        <div className="st-ex" aria-label="ตัวอย่างเป้าหมาย">
          {GOAL_EXAMPLES.map((x) => <button key={x} type="button" onClick={() => setQ(x)}>{x}</button>)}
        </div>
      )}
      {asked && (
        <div className="st-found" aria-live="polite">
          {found.understood ? (
            <>
              {found.programs.length > 0 && (
                <>
                  <h3>โปรแกรมเต็มที่ตรงเป้าหมายนี้</h3>
                  <div className="st-row" style={{ paddingBottom: 18 }}>{found.programs.map((p) => <ProgramCard key={p.id} p={p} />)}</div>
                </>
              )}
              {found.packages.length > 0 && (
                <>
                  <h3>แพ็กเกจที่พาไปถึงเป้าหมายนี้ ({found.packages.length})</h3>
                  <div className="st-row" style={{ paddingBottom: 18 }}>{found.packages.map((p) => <PackageCard key={p.id} p={p} />)}</div>
                </>
              )}
              {found.routes.length > 0 && (
                <>
                  <h3>Route ที่เกี่ยวข้อง ({found.routes.length})</h3>
                  <div className="st-row" style={{ paddingBottom: 18 }}>{found.routes.map((r) => <RouteCard key={r.id} r={r} showDisc />)}</div>
                </>
              )}
            </>
          ) : (
            <p className="st-found-none">
              ยังไม่มี Route ที่ตรงกับ “{q.trim()}” ลองพิมพ์สิ่งที่อยากทำ เช่น เกม เว็บ แอป หรือ IoT หรือ{" "}
              <a className="st-link" href={LINE_URL} target="_blank" rel="noopener">ทัก LINE ให้ทีมช่วยเลือก</a>
            </p>
          )}
        </div>
      )}
    </div>
  );
}
