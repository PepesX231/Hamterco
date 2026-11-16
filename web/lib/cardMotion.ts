// Search focus motion for the work cards (plain Web Animations so it can be reversed mid-flight).
// Desktop: each card flies to its own spot round the bar and stays tucked a little behind its edge.
// Phones: each card is pulled into the nearest point of the bar's edge.

type Box = { left: number; right: number; top: number; bottom: number; width: number; height: number };

const nearestEdge = (cx: number, cy: number, r: Box) => {
  const inY = cy > r.top && cy < r.bottom;
  const d: [number, "l" | "r" | "t" | "b"][] = [
    [Math.abs(cx - r.left) * (inY ? 1 : 3), "l"], [Math.abs(cx - r.right) * (inY ? 1 : 3), "r"],
    [Math.abs(cy - r.top), "t"], [Math.abs(cy - r.bottom), "b"],
  ];
  const e = d.sort((a, b) => a[0] - b[0])[0][1];
  const clampY = Math.max(r.top + 8, Math.min(r.bottom - 8, cy));
  if (e === "l") return { x: r.left, y: clampY, e };
  if (e === "r") return { x: r.right, y: clampY, e };
  return { x: Math.max(r.left + 12, Math.min(r.right - 12, cx)), y: e === "t" ? r.top : r.bottom, e };
};

export function gather(wrap: HTMLElement, bar: HTMLElement, desktop: boolean): Animation[] {
  const R = bar.getBoundingClientRect();
  const fr: Box = { left: R.left, right: R.right, top: R.top - 3, bottom: R.bottom - 3, width: R.width, height: R.height };
  const cards = [...wrap.querySelectorAll<HTMLElement>(".hc")].filter((c) => {
    const r = c.getBoundingClientRect();
    return r.width && getComputedStyle(c).display !== "none" && r.bottom > 0 && r.top < innerHeight;
  });
  const out: Animation[] = [];
  const start = (c: HTMLElement) => { const t = getComputedStyle(c).transform; return t === "none" ? "rotate(0deg)" : t; };

  if (desktop) {
    const slots = { l: [["t", 0.06], ["l", 0.5], ["b", 0.12]], r: [["t", 0.94], ["r", 0.5], ["b", 0.88]] } as const;
    (["l", "r"] as const).forEach((side) => {
      cards.filter((c) => c.dataset.side === side)
        .sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)
        .forEach((c, i) => {
          const [edge, f] = slots[side][Math.min(i, 2)];
          const r = c.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height / 2;
          const S = Math.min(0.42, 120 / c.offsetWidth), ws = c.offsetWidth * S, hs = c.offsetHeight * S;
          const tilt = (side === "l" ? -1 : 1) * (4 + i * 2);
          let tx = 0, ty = 0;
          if (edge === "t") { tx = fr.left + fr.width * f; ty = fr.top - hs / 2 + hs * 0.22; }
          else if (edge === "b") { tx = fr.left + fr.width * f; ty = fr.bottom + hs / 2 - hs * 0.22; }
          else if (edge === "l") { tx = fr.left - ws / 2 + ws * 0.22; ty = fr.top + fr.height / 2; }
          else { tx = fr.right + ws / 2 - ws * 0.22; ty = fr.top + fr.height / 2; }
          const dx = tx - cx, dy = ty - cy;
          out.push(c.animate([
            { transform: start(c), filter: "blur(0)" },
            { transform: `translate(${-dx * 0.04}px,${-dy * 0.04}px) rotate(0deg) scale(1.04)`, filter: "blur(0)", offset: 0.16 },
            { transform: `translate(${dx * 0.6}px,${dy * 0.6}px) rotate(${tilt * 0.5}deg) scale(${S + 0.25})`, filter: "blur(1.2px)", offset: 0.5 },
            { transform: `translate(${dx * 1.04}px,${dy * 1.04}px) rotate(${tilt * 1.3}deg) scale(${S * 0.94})`, filter: "blur(0)", offset: 0.8 },
            { transform: `translate(${dx}px,${dy}px) rotate(${tilt}deg) scale(${S})`, filter: "blur(0)" },
          ], { duration: 640, delay: (side === "l" ? i * 2 : i * 2 + 1) * 45, easing: "cubic-bezier(.55,0,.25,1)", fill: "both" }));
        });
    });
    return out;
  }

  cards.sort((a, b) => Math.abs(a.getBoundingClientRect().top - fr.top) - Math.abs(b.getBoundingClientRect().top - fr.top))
    .forEach((c, i) => {
      const r = c.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height / 2;
      const p = nearestEdge(cx, cy, fr), dx = p.x - cx, dy = p.y - cy, v = p.e === "l" || p.e === "r";
      out.push(c.animate([
        { transform: start(c), opacity: 1 },
        { transform: `translate(${dx * 0.55}px,${dy * 0.55}px) rotate(0deg) scale(.62)`, opacity: 1, offset: 0.55 },
        { transform: `translate(${dx * 0.96}px,${dy * 0.96}px) rotate(0deg) scale(${v ? ".1,.32" : ".42,.1"})`, opacity: 1, offset: 0.9 },
        { transform: `translate(${dx}px,${dy}px) rotate(0deg) scale(${v ? "0,.2" : ".3,0"})`, opacity: 0 },
      ], { duration: 560, delay: i * 55, easing: "cubic-bezier(.7,0,.25,1)", fill: "both" }));
    });
  return out;
}
