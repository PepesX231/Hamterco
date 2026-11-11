# Hamster Hub website redesign: handoff

This is a summary for whoever (person or AI) continues this work. It covers what exists, where it lives, how to change it safely, and what the client has said yes and no to.

## 1. The project

- **Client:** Hamster Hub (hamsterhub.co). The company teaches high-school students to build games, web apps and IoT, and the students' work is used for university admission (TCAS portfolio round), startups and national competitions.
- **Who the site is for (stated by the owner):**
  1. Students who want to get into university. Sell them the portfolio course.
  2. Students who want to make their own things. Sell them game-making skill.
  3. Parents. They pay, so the site has to earn their trust. Sell them hope.
- **What makes Hamster Hub different (stated):** it does not only get kids into university. Its students build startups, products that are sold (Mr. City), games and web apps with real users, and award-winning projects. Do NOT frame this by putting down "portfolio" ("we don't just do portfolios" was rejected). Just say what Hamster Hub builds.
- **Language:** all copy is Thai. Write it plainly so a parent understands at a glance: the outcome first, a number with its unit, and an explanation for any jargon. A skill called `thai-plain-copy` holds these rules.
- **Feedback comes from:** the owner (Pesd, GitHub PepesX231) relays comments from พี่ฮิว (reviewer) and พี่เก่ง. The owner writes in blunt casual Thai, so reply in Thai.

## 2. Where things are

| What | Where |
|---|---|
| Repo | https://github.com/PepesX231/Hamterco (branches `main` and `gh-pages`, kept identical) |
| **Preview page (work in progress)** | `new.html` → https://pepesx231.github.io/Hamterco/new.html |
| Live page | `index.html` (an older approved version, v38). **Do not replace it until the owner explicitly says to promote the preview.** |
| Images and videos | `img/` |
| Build scripts (history) | `dev/builds/build*.py` (build39 to build74 are the recent ones) |
| Latest built source | `dev/v74-source.html` (same body as new.html, without the old `<head>` wrapper) |
| Perf test scripts | `dev/perf*.js` (Playwright) |

`new.html` is **one self-contained file**: a single-page app with hash routes `#home`, `#courses`, `#activity`, `#works` and `#about`. All CSS and JS are inline, and the data arrays are inline too:
- `CRS`: courses
- `ACT`: activities
- `G`: seniors and their admission results
- `IT`: the search index
- `INT`: search intents
- `KW`: search aliases

### How to edit (recommended)

Edit `new.html` directly. The python build chain lives in `dev/builds/`. Each `buildN.py` `exec`s the previous one and patches the HTML with string replacement. It points at absolute paths from the old sandbox, so it will **not** run as-is. Keep it as history and reference only.

To publish the preview:
```
git add new.html img/...
git commit -m "..."
git push origin main main:gh-pages
```
GitHub Pages takes about 1 to 5 minutes, and sometimes needs an extra empty commit before it picks up the change.

### Gotchas that have bitten before

- **Class name clashes.** The file has lots of old short class names (`.oc`, `.fd`, `.gk`, `.hd`, `.v`, `.b2`). New sections must use unique prefixes. In v73, the "what Hamster Hub builds" section was named `.oc`, picked up an old card style and turned into a big white box. It is now `.hbx`.
- **Performance.** The owner said the site was unusably laggy, even on an RTX 5060. Three optimisation passes (v60 to v62) took the Hall of Fame section from 2–3 fps to about 29 fps with the CPU throttled 6x. Keep these rules:
  - no canvas redraw every frame
  - no animated `clip-path`
  - no `backdrop-filter` on large or fixed elements
  - animations pause when off-screen (the `.zz-off` class, set by IntersectionObserver)
  - videos play only while visible
- **Mobile.** Always check at 390px wide. `main` has `overflow-x:clip`, so nothing may cause horizontal scroll.

## 3. Current home page order (v74)

1. **Search hero (centred), the main feature.**
   - Headline "น้องอยาก…" with a typing word in a sticker style. Clicking it cycles through many font styles.
   - A hamster peeks out behind the search bar.
   - Suggestion chips under the bar.
   - Searching opens an answer panel under the bar, without the page jumping.
2. **คอร์สที่เราแนะนำ (recommended courses).**
   - A wide Port Express card: video, 2 เดือน, starts 9 พ.ย. 2569, 5,990 บาท.
   - Below it, two equal cards: Hamstarter and National Project.
   - Gold "★ คอร์สแนะนำ" badges.
3. **คอร์สทั้งหมด (all courses):** a horizontal rail. Recommended courses carry a "★ แนะนำ" badge.
4. **สิ่งที่ Hamster Hub สร้าง (what Hamster Hub builds):** alternating image and text rows.
   1. Startup, the biggest row: Mr. City, PHC Map / Hamster Map clip, Hamster Quest.
   2. University: 48 seniors.
   3. National win: REVOICE / NSC, with a "watch clip" dialog.
   4. Games.
5. **Hall of Fame:** the "golden rift", a dark section with jagged gold edges, aurora and a walking hamster. The owner approved this look (v59), so don't redesign it. Its edges now run past both screen sides.
6. Seniors who got into university, partners, then news and recent activities at the bottom.

### The search (a key feature; the reviewer pushed hard on it)

- **Intent answers.** The search maps what the student typed to an intent and shows:
  - a short answer
  - the courses that help, each with one line on how
  - seniors who took that path, with photo, faculty and course
  - follow-up questions, and a LINE button
- **About 24 intents:** วิศวะคอม/CEDT, วิทย์คอม/IT, แพทย์, สายวิทย์, each of 4 universities, "Hamster Hub คืออะไร", price, schedule, parents, ม.6 / ม.4–5 / ม.ต้น, beginners, game, web, IoT, AI, startup, competition, camp, portfolio.
- **Medicine is answered honestly.** There is no med-prep course; the answer offers health-tech projects for the portfolio instead.
- **Forgiving matching** (`intent2()`, `KW` aliases), modelled on Algolia:
  - prefix while typing ("วิศ" works)
  - typo tolerance (Damerau-Levenshtein)
  - many aliases and misspellings per intent
  - stripping filler words ("อยากเข้า…", "…ครับ")
  - Thai/English wrong-keyboard-layout fix (`;bL;t` → วิศวะ, shown with a yellow notice)
  - "หรือน้องหมายถึง" (did you mean) for ambiguous input, and a chooser for 1–2 character input
- **Exact course names** ("python pro") show that course card directly.
- **To add words:** extend the `KW` lists, and keep `NAME` in the same order as `KW`/`INT`.

## 4. Other pages

- **#courses:** the "★ คอร์สที่เราแนะนำ" block on top (same as home), then all courses.
- **#activity (rebuilt in v69; the old one was rejected outright):**
  - a big next-event card for All for One University รอบชิงชนะเลิศ, 14 พ.ย. 2569, at IoTE สจล., with a live countdown
  - "ปี 2569 เราจัดไปแล้ว 17 งาน" with type filter buttons and cards (date, description, what the kid gets)
  - events with no poster get a navy card with the mascot
  - a real-photo gallery, and a LINE CTA
- **#about:**
  - **"เราทำอะไร":** startup is the big lead card, with university and competitions smaller underneath. The reviewer wants startup to stand out most.
  - **"ผลงานของน้องที่มีคนใช้จริง":** one product per row, each answering ใครใช้ / ใช้ยังไง / ผลลัพธ์, for Mr. City, PHC Map and Hamster Quest.
- **#works:** works gallery and seniors list (older, mostly untouched lately).

## 5. Facts used (do not invent numbers)

**Seniors and results**
- DEK69 seniors admitted in the portfolio round: **48 คน**. By university: สจล. 24, มหิดล 9, จุฬาฯ 8, เกษตรศาสตร์ 7. The owner chose to show 48, not "100+".
- **12** projects reached the NSC finals (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย).
- The per-faculty senior counts in search answers (for example "11 คนติดวิศวะคอมฯ/CEDT") are counted from the 17 senior posters in `G`. The real totals are probably higher.

**Courses and events**
- **Port Express:** 2 months, Mon/Wed/Fri, starts 9 พ.ย. 2569, 5,990 บาท, link https://www.hamsterhub.co/portex-site/index.html. It is the only course currently open.
- **All for One University final:** 14 พ.ย. 2569 at IoTE สจล.
- **Partners:** คณะเทคโนโลยีสารสนเทศ สจล., IoTE สจล., EDUverse.
- **LINE:** https://page.line.me/jkm4247u?openQrModal=true

**Products**
- **Mr. City:** a game for touring Songkhla, **like Pokémon GO** (walk to real places), sold to สวนสัตว์สงขลา (Songkhla Zoo). **No real image yet.** The about page uses a placeholder green map-pin card.
- **PHC Map:** a Python teaching game, used to teach more than 1,000 kids. The site uses the "Hamster Map" clip from hamsterhub.co for it; this is assumed to be the same game and the owner hasn't confirmed.
- **Hamster Quest:** a learning website that plays like a game, being prepared for use with a university. Its images are the pixel town with the grey hamster (`w-quest-town.webp`) and the dark quests UI (`w-quest-app.webp`). These were once wrongly labelled as Mr. City.
- **REVOICE:** a speech-practice app by น้องไอดิน, built in 4 months, won NSC 2025. Clip: `img/story-nsc.mp4`.
- **StressStrike:** won OBEC Roboplayground. It is an award winner, NOT a "real users" product.

## 6. Client likes and dislikes (very important)

### Approved or liked
- Blue/white theme.
- Search-first home page, centred (Fastwork-inspired UX).
- The hamster peeking behind the search bar, with whiskers.
- The Hall of Fame golden rift (v59 look) with aurora light coming out of the edge.
- Real photos and real student work.
- Recommended courses big and clearly badged.

### Rejected (don't bring these back)
- **Home hero:**
  - the dark cinematic hero with background video (v71/72)
  - the left-aligned hero with the big mascot circle (v69)
- **Story sections:**
  - scroll-driven storytelling: text that darkens word by word, and pinned chapters that change only as you scroll. Parents don't realise they have to scroll.
  - the line "เราไม่ได้สอนแค่ทำพอร์ต" (it reads as a dig at portfolios)
  - a v37 scrollytelling version
- **Look and style:**
  - an orange theme
  - grid backgrounds, gradient washes and "AI slop" generated illustrations
  - watercolor art and visionOS-style UI
  - holy waves and swords on the rift edge, a dashed edge line, blurry aurora
  - an "explosion/boom" headline font
- **Layout and pieces:**
  - four equal cards in a row with weak images
  - three equal "what we do" cards (one must lead)
  - an activity deck
  - the old activity page
  - two duplicate sections ("ผลงานของน้องไปไกลกว่าแฟ้มพอร์ต" and "เลือกเส้นทางของน้อง") with AI images
- **Hamster behaviour:**
  - the hamster hopping or spinning on search (dive only)
  - eyes-only tracking (the whole head turns)

### Standing direction from the reviewer
- Make the site feel like **Hamster Hub**, not Fastwork. The reviewer has said this several times, and two attempts (v69, v71) were rejected. Expect to show options before committing.
- Give people a reason to keep scrolling, with good storytelling and cool techniques, while staying easy for parents.
- Polish the details everywhere.

## 7. Open items and next steps

1. **Home "feels like Hamster Hub":** still unsolved. Both bold attempts were rejected and the owner asked to keep the centred search hero. Suggested next step: keep the hero layout and bring in brand identity through smaller elements (mascot trio, real student faces, brand colours from hamsterhub.co), and show the owner 2–3 small mockups first.
2. **Real Mr. City image or clip:** ask the owner.
3. **Confirm** that the "Hamster Map" clip is PHC Map.
4. **Posters for activities without one:** SciGame Lab, StarLight, Intelligence Camp, Python camps.
5. **Higher-resolution real activity photos:** the current ones are about 500px.
6. **Promote `new.html` to `index.html`:** only when the owner says so.

## 8. Useful sources

- Current production site: https://www.hamsterhub.co/. It has a dark theme, intro video `/hh-home/videos/development/hamster.webm`, startup stage images `/hh-home/images/startup/*.webp`, and About slides `AboutDT1..9.webp` with real student work.
- Design skills read for this work:
  - anthropics/skills `frontend-design`: an anti-slop checklist
  - Leonxlnx `taste-skill`
  - greensock `gsap-skills`
  - coreyhaines31 `marketingskills` (cro, marketing-council)
  - StoryBrand (Grunt Test)

