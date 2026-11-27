# Hamster Hub website: handoff (27 พ.ย. 2569)

For the next person or Claude taking over. Read all of it before changing anything. The owner is strict about look and copy, and many ideas have already been tried and rejected (section 8).

## 1. The project in one minute

- **Client:** Hamster Hub (hamsterhub.co). It teaches high-school students (ม.ปลาย) to build games, web apps, IoT and startups. The students' work gets them into university (TCAS portfolio round), wins national competitions and is sold or used for real.
- **Audience:** students choose, parents pay. Parents need to trust the site at a glance.
- **Owner:** Pesd (ชมน์ปภพ), GitHub `PepesX231`. He relays comments from พี่ฮิว and พี่เก่ง. **Always reply to him in Thai, in plain words.** He writes in blunt, casual Thai with typos, sometimes typed on the wrong keyboard layout (English letters that are really Thai). He often sends screenshots numbered "รูป 1, รูป 2…" and the order of the images is the numbering.
- **Who continues the code:** his friends, in **Next.js**. All new work happens in `web/` (Next.js). `slime.html`, `new.html` and `index.html` are frozen older versions.

## 2. Links

| What | Where |
|---|---|
| Repo | https://github.com/PepesX231/Hamterco (`main` and `gh-pages` are kept identical) |
| **Current site (Next.js)** | https://pepesx231.github.io/Hamterco/next/ |
| Hams Route store | https://pepesx231.github.io/Hamterco/next/routes/ |
| Older single-file versions (frozen) | `/Hamterco/slime.html`, `/Hamterco/new.html`, `/Hamterco/` (index.html) |
| Team sheet of projects and awards | https://docs.google.com/spreadsheets/d/1eB-6lrVTdXQ8LRwiYjp0x6J8E1jpndy6d-hYZWgSvL0/edit?gid=0 |
| Real production site (the client's) | https://www.hamsterhub.co/ |
| LINE | https://page.line.me/jkm4247u?openQrModal=true |

## 3. Run, build, test and publish

```sh
cd web
npm install
npm run dev            # http://localhost:3000/Hamterco/next/ (pictures come from /Hamterco/img/, see serve.sh)
npm run export         # rebuilds the legacy bundle, builds the static site into web/out, copies it to ../next/
```

Test the built site the way GitHub Pages serves it:

```sh
dev/tests/serve.sh     # http://localhost:8791/Hamterco/next/  (needs `npm run export` first)
cd dev/tests
node flow.js           # main user flow at 1440 and 390, prints "errors: none" when clean (needs playwright)
node shots.js "routes/|1440|r" "|390|home"    # full-page screenshots: path|width|name
node gen.js && node harness.js                # 5,814 generated search questions; prints the share left unanswered
node txt.js http://localhost:8791/Hamterco/next/   # counts visible text (the owner wants less text than apple.com/th)
python3 tile.py in.png out.png 2200           # tiles a tall screenshot into one image
```

Publish (GitHub Pages takes 1–5 minutes):

```sh
git add -A && git commit -m "..." && git push origin main main:gh-pages
```

Always check at **1440 and 390 px wide**. Nothing may cause sideways scrolling (`html{overflow-x:clip}`).

## 4. How the app is built

Next.js 16 (App Router, static export), React 19, TypeScript, Tailwind 4, Motion 12. `basePath` is `/Hamterco/next`, with `trailingSlash`.

It is a **hybrid**. Parts already rewritten are React. Everything else is the original page (markup, CSS and scripts), run inside the app by `components/LegacyRuntime.tsx`.

- `dev/builds/legacy_next.py` rebuilds the original page from `new.html` plus the layer files in `dev/builds/layers/`, skipping the layers React now replaces. It splits the result into `web/public/legacy/` (`body.html`, `legacy.css`, `js/NNN.js`, `manifest.json`).
- **Content edits to legacy sections are made in `legacy_next.py`** as string replacements on the body or the scripts. For example, the pictures and clips in "สิ่งที่ Hamster Hub สร้าง", renamed links, shorter button text and the Hams Route rename are all there. Do not edit `web/public/legacy/` by hand; it is regenerated on every export.
- `LegacyRuntime` loads all legacy scripts in parallel and moves the old header and the page-wipe element to the top. `view="home" | "works" | …` picks the legacy view. `view="shell"` keeps only the header, footer and loader (used by the React-only Hams Route pages). The `hide` prop hides legacy parts that React has replaced.
- Page transitions use the original wipe (`window.HH_pt`, key `hh-pt` in sessionStorage). The loader (`lib/loader.ts`) is skipped when arriving through a transition.

### CSS gotcha (important)

The order is `@layer theme, base, legacy, components, utilities`. Legacy CSS often uses `!important`. An `!important` rule in a **lower** layer beats one in a higher layer, so to override a legacy `!important`, put your rule inside `@layer theme { … !important }` in `app/globals.css`. Several blocks there already do this (look for `@layer theme`).

### File map (web/)

| File | What it does |
|---|---|
| `app/page.tsx` | Home: `<Hero/>`, `<HomeStore/>`, then the legacy home sections |
| `app/routes/…` | Hams Route: store page, kind pages `[d]`, Route detail `r/[id]`, Package detail `p/[id]` |
| `app/works/page.tsx` | Works page (legacy); `SheetWorks` adds the full awards list to its Hall of Fame tab |
| `app/courses/` | Redirects to `/routes/` |
| `app/globals.css` | Global and legacy overrides (search bar, follow bar, sections, Hall of Fame tab, text cuts) |
| `app/store.css` | Hams Route look: shelves, cards, package blocks, header, arrows |
| `components/Hero.tsx` | Hero: work cards, "น้องอยาก…", search bar, answers (`solveQuery`), `RouteMatches`, `FollowBar` (the search bar that appears at the bottom of the screen after the big one scrolls away) |
| `components/HomeStore.tsx` | Home shelves: Packages, then 6 Routes |
| `components/store/*` | `Shelf` (row plus arrows), `Cards` (Package, Route, Program), `PackageShelf`, `GoalSearch`, `Info` (FAQ and steps), `BuyBar` |
| `components/SheetWorks.tsx` | Puts the awards list from `lib/works.ts` into the Hall of Fame tab |
| `components/LegacyRuntime.tsx` | Runs the legacy page (see above) |
| `lib/routes.ts` | All Hams Route data: 6 kinds, 24 Routes, 4 Packages, 2 programs, goal search `findForGoal` |
| `lib/understand.ts` | Reads search questions in any form: typos, slang, no spaces, wrong keyboard layout, tone marks |
| `lib/works.ts` | Awards from the team sheet (22 พ.ย.) |
| `lib/site.ts` | Hero work cards, wishes, example questions, nav links |
| `public/route-art/` | `t-<route id>.webp` (Route art), `pk2-*.webp` (Package art) |

Pictures and videos for the whole site live in the repo-root `img/` and are served as `/Hamterco/img/…`.

### The search

1. The original engine (legacy layer `65-search.html`) answers first.
2. If it gives up (unknown, foreign, shape and similar), `understand()` names the topic and the engine is asked again with a standard question. If the topic is something only Hams Route covers (3D, the 12-month programme), the card says so and the matching Routes show under it.
3. Keyboard mash such as "ฟหก" gets "แป้นพิมพ์อาจเป็นอีกภาษาอยู่".

To add words, extend `INTENTS` in `lib/understand.ts`, then run `harness.js`. The last run left 0.4% unanswered, mostly mixed Thai and English strings.

## 5. What the site looks like now

**Home, in order:**
1. **Hero.** Work cards gather around the search bar. "น้องอยาก…" has a typed wish. The search answers appear under the bar.
2. **Shelves.** "**แพ็กเกจ** ตัวเลือกเป้าหมายของน้อง" (4 Packages), then "**Route** ฝึกทีละทักษะ" (6 Routes).
3. **สิ่งที่ Hamster Hub สร้าง:**
   - PHC Map clip, a Mr. City block (play button opening its Facebook clip) and a Hamster Quest app screen
   - REVOICE
   - three real game clips: SLASH//SPEED, Apocalypis Building (depa 2026 winner) and Eugation Strike, cut from `img/reel.mp4`
4. Hall of Fame (dark, gold), seniors who got into university, activities, closing section and footer.

**Hams Route (`/routes/`):**
- Apple Store–style header: name on the left, mascot in the middle, question on the right.
- Packages, then one shelf per kind.
- Content starts about 2.8vw from the left edge, like Apple.
- Arrows always show at the right edge (faded when there is nothing to scroll).
- Route cards are 284 × 430: white card, picture inside with space around it, name and price, then the arrow.
- Package detail pages have the picture, a buy bar, FAQ and apply steps.

**Package names:**

| Package | Line | Sample price |
|---|---|---|
| First Build | โค้ดชิ้นแรกของน้อง | ฿2,390 |
| Port Ready | เว็บพร้อมใส่พอร์ต | ฿3,490 |
| Arena | โปรเจกต์ขึ้นเวทีแข่ง | ฿4,290 |
| Launch Lab | ไอเดียสู่แอปจริง | ฿3,990 |

**Programs:**
- Port Express: 2 months, ฿5,990
- Project Build Skill: 12 months, ฿19,990

## 6. Facts (never invent numbers)

- **Prices are SAMPLES.** All Route and Package prices are samples from the design files and are labelled "ราคาตัวอย่าง". Prerequisites, durations and the real apply link are still "รอทีมยืนยัน".
- **University results:** 48 seniors in DEK69 got in through the portfolio round (สจล. 24, มหิดล 9, จุฬาฯ 8, เกษตรฯ 7).
- **Mr. City:**
  - A game for touring Songkhla, sold to สวนสัตว์สงขลา (the Songkhla zoo).
  - **There is no real picture of it.** The two files that looked like Mr. City are really Hamster Quest's town, and `g-mrcity.webp` is a generated picture.
  - The site shows an orange block with a play button that links to the Facebook clip.
- **PHC Map:** used to teach more than 1,000 children. The site uses the `w-hmap.mp4` clip for it.
- **Hamster Quest:** a learning site that plays like a game.
- **Apocalypis Building:** by น้องฟาร์. The owner confirmed it is the depa 2026 winner ("สร้างตึก", prize 200,000 บาท).
- **Awards:** the full list is in `lib/works.ts`, copied from the sheet. Names are kept as written there.
- **Generated pictures** (not student work):
  - Route art (`t-*.webp`, flat poster style the owner asked for)
  - Package art (`pk2-*.webp`)
  - Never generate pictures that pretend to be students' games or screenshots.

## 7. Rules the owner has set

- Square, sharp corners everywhere (except true circles), with an Apple feel. He compares against apple.com/th and apple.com/th/store constantly.
- No "AI slop":
  - no decorative gradients
  - no template grids of identical cards
  - no pill buttons
  - no decorative lines or rules ("ขีดๆ")
- **No hard cut edges ("ขอบตัด")** between sections or under rows. Shadows must fade out (rows have bottom padding for this).
- **Less text than Apple.** The home page now has 720 visible characters; apple.com/th has 724. Run `txt.js` after adding copy. Remove the small explanatory lines under headings.
- **Real pictures and clips over generated ones.** When something has a clip, play it automatically: muted, looping, `playsinline`.
- Copy follows the `thai-plain-copy` rules: outcome first, numbers with units, no slogans, buttons that say what happens.
- In new copy, do not use "ดูทั้งหมด", and say "Hams Route" instead of "คอร์ส" (some old legacy text still says คอร์ส).
- When he says "กลับเป็นแบบเดิม", restore exactly what was there before.
- Motion is 60fps and purposeful. Nothing moves on its own without a reason.
- Do not invent facts. If unsure, ask him and say clearly what is a sample.

## 8. Tried and rejected (do not bring back)

**Earlier versions:**
- dark cinematic hero with background video
- left-aligned hero with a big mascot
- scroll-driven storytelling
- the line "เราไม่ได้สอนแค่ทำพอร์ต"
- an orange theme
- grid backgrounds and gradient washes
- watercolor and visionOS-style UI
- hamsters built from CSS circles
- the cheese drip under the search bar (the legacy `.je`, now hidden globally)

**Hams Route era (22–23 พ.ย.):**
- goal chips and the compare table
- the full programs section
- clay-toy Route art
- package names in Thai ("โปรแกรมชิ้นแรก"…)
- the sheet's "ใช้งานจริง ขายได้" shelf on the home page (the awards list belongs only in Hall of Fame)
- poster images with student photos in "สิ่งที่ Hamster Hub สร้าง"
- generated device mockups for Mr. City, PHC Map and Hamster Quest
- the search bar that followed at the top of the screen (now at the bottom)
- Route cards so big that they run off the edge

## 9. Open items

1. **Mr. City:** a real screenshot or clip (Facebook cannot be fetched from here).
2. **Clips of LYNO, Time Keeper and Z.O.O.:** they were replaced by games that have clips. The owner can send files.
3. **Names to confirm:** PHC Map or Hamster Map? RE//SLASH (sheet) or SLASH//SPEED (Hall of Fame)?
4. **Dune by น้องแทน:** what "10k" in the sheet means.
5. **MIT 2025 (ขนมปัง):** the project has no name in the sheet.
6. **From the team:** real prices, prerequisites, durations and the apply link for Routes and Packages.
7. **Rewrite remaining legacy sections as React components,** one at a time, then drop them from `legacy_next.py`. This is the long-term goal so the friends inherit a clean Next.js app.
8. **Hams Route kind pages:** these can now be reached only from the breadcrumb on a Route page, because the "ดูทั้งหมด" links were removed at the owner's request.
