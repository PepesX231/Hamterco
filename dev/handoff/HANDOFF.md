# Hamster Hub: redesign handoff (to 16 พ.ย. 2569)

A summary for whoever continues the work. It covers what was done, how to build the site, what the owner likes and dislikes, and what is still open.

- Live preview: https://pepesx231.github.io/Hamterco/slime.html (add `?v=<number>` to skip the cache)
- Repo: https://github.com/PepesX231/Hamterco (push to both `main` and `gh-pages`)
- Owner: ชมน์ปภพ "Pesd" (GitHub PepesX231). Reply in Thai, in plain words.
- Audience: Thai ม.4–6 students (they use the site) and their parents (they pay).

---

## 1. Latest feedback (see `feedback-no-cheese.png`)

A senior on the team (watchirapongth) reviewed the hero with the cheese background:

> "ไม่เอาชีส / ไม่เกี่ยวกับ product"

**Done (16 พ.ย.):** the owner chose to keep the cheese but tie it to the product. `dev/builds/layers/99zzzzzzzzzzzz-herobg.html` draws the cheese again, and every hole is a window showing a real work: game-jam games, NSC projects (REVOICE, LYNO, Z.O.O., Timekeeper), the Mr. City app, Hamster Quest (web and Python game) and DEK69 portfolio results. The pictures load after the page has loaded, so they don't slow the first paint. Pointing at a hole shows the work's name, and clicking it goes to #works. Holes stay off the headline and search; two holes have separate phone positions so they don't sit under the example chips. (A Unity-grid version was tried in between and dropped.)

---

## 2. How the site is built (important)

- **Source:** `new.html`. **Never edit it.** All changes go in as layers.
- **Build:** `cd hamterco && python3 dev/builds/theme_slime.py new.html slime.html`
  1. It applies text replacements from `dev/builds/copy.json`. Each entry is `[old, new, count]`.
  2. It recolours the palette.
  3. It appends every file in `dev/builds/layers/*.html` in filename order. Later layers win, which is why the names carry more and more `z`.
- **Loader:** `dev/builds/parts/loader.html` is injected through a `copy.json` entry. Whenever loader.html changes, that entry must be rebuilt: its `new` value is loader.html followed by the `old` value.
- **Local preview:** `python3 -m http.server 8767`, then open http://localhost:8767/slime.html
- **Deploy:**
  ```
  git add -A && git -c user.name=PepesX231 commit -m "..."
  git push https://github.com/PepesX231/Hamterco.git main main:gh-pages
  ```
  GitHub Pages caches for about 10 minutes. When an image changes, give it a new file name so visitors get the new one.
- **Views** are hash routes: `#home` (default), `#courses`, `#activity`, `#works`, `#about`.

### Main layers (newest at the bottom)

| File | What it does |
|---|---|
| `50-hero.html` | Hero code-sea canvas (now hidden by the cheese layer) |
| `60-slurp.html` | Orange liquid that wraps the search results |
| `65-search.html` | Search answer logic: Thai keyword matching, half-typed wishes, events |
| `99z-round.html` | Home "สิ่งที่ Hamster Hub สร้าง" rows, now one short result line per work |
| `99zz-about.html` | About page: CRT/WebGL drum of works, photo ring "บรรยากาศจริง" |
| `99zzz-nav.html` | Nav pill and per-tab hover effects |
| `99zzzz-fix.html` | Event status follows the real date ("เพิ่งจบ 14 พ.ย.") |
| `99zzzzzz-search.html` | Search bar: placeholder "พิมพ์คำถามได้เลย", floating "ถามเราได้เลย" button |
| `99zzzzzzz-crew.html` | Hero: hand-drawn arrow, the note "ไม่รู้จะเริ่มตรงไหน? ลองถามดู", the hamsters peeking from the edges, results panel sizing |
| `99zzzzzzzz-courses.html` | Course cards without the template look (no "แนะนำ" pills, tilt, glare) |
| `99zzzzzzzzz-review.html` | Mobile header shows ทัก LINE, no dead countdown, courses/activity pages have no page-name banner |
| `99zzzzzzzzzz-perf.html` | Performance: no big blurs, off-screen animations paused |
| `99zzzzzzzzzzz-lists.html` | Courses page as a ruled list, poster-less events as a dated list, home "คอร์สทั้งหมด" carousel removed |
| `99zzzzzzzzzzzz-herobg.html` | Hero background: cheese, every hole shows a real work; also hides the code text |
| `99zzzzzzzzzzzzz-plain.html` | De-templated the two home sections: flat pictures, rules between rows, underlined text links instead of orange pills |

---

## 3. What the owner wants

- **Look:** no "AI slop". That means:
  - no generic stickers, confetti, gradients used as decoration, or blob mascots
  - no identical rounded card grids, no pattern or big-number placeholder thumbnails
  - no rotated sideways faces
- **No cut edges ("ขอบตัด")** and no layout jumps. Anything peeking from an edge must sit flush with it.
- **Never invent facts** about the school. Use what is already on the page, or ask.
- **Keep the existing layouts** unless asked to change them.
- **Off-limits:** Hall of Fame (`.h5f`) is not to be touched, and the AFO banner stays blue.
- **Hamsters:**
  - style: clean sticker with big eyes, no whiskers or fur lines ("ไม่เอาขน"), cute rather than scary
  - hands: round mitten paws without fingers
- **Motion:**
  - smooth, 60fps
  - nothing bouncing around on its own ("ไม่ต้องเด้งไปเด้งมา")
  - things move in response to the visitor
- **Copy:**
  - short and plain
  - invites without pushing (prefers something like "ไม่รู้จะเริ่มตรงไหน? ลองถามดู" over an exclamation-mark command)
  - covers more than courses: คอร์ส ค่าย พอร์ต มหาลัย
- **Reverts:** the owner often asks to undo. When he says "กลับเป็นแบบเดิม", restore exactly the previous state.
- **Mobile matters:** test at 390px wide every time.

---

## 4. Current state of each part

- **Home hero:**
  - The headline types "น้องอยาก… <wish>".
  - The search bar has the placeholder "พิมพ์คำถามได้เลย" and example chips below it.
  - Desktop: on the left, a hand-drawn arrow is drawn toward the bar, then the note is written above the curve. There is no hamster or pencil on the left (the owner removed them).
  - Mobile: a pencil-loop drawing around the bar.
  - On the right edge, a grey hamster peeks down from the top and a peach hamster peeks round the side.
  - The background is cheese; every hole shows a real work (games, startup app, NSC, portfolios).
- **Search results:** the panel is centred under the bar. The hero grows so the panel is never cut off, and its background turns the page's cream colour while the panel is open.
- **"คอร์สที่เราแนะนำ":**
  - Port Express is the big card.
  - Hamstarter and National Project show "รอเปิดรอบถัดไป".
  - The two smaller cards are now flat (no box, shadow or pill buttons), split by a rule. An earlier rework into slim rows was reverted at the owner's request.
- **"สิ่งที่ Hamster Hub สร้าง":** three rows with less text, now flat: pictures without shadows, a rule above each row, plain text links.
- **Activity page:** events with a poster are picture cards, the rest are a dated list. The All for One banner is marked as finished.
- **About page:** a WebGL works drum (next screen rises from below, no dark rim) and a photo ring (fixed so it no longer shows black).
- **Loader:** a walking hamster sprite. When loading finishes it says "โหลดเสร็จแล้ว!", ends on the both-paws-up frame, and is centred.

---

## 5. Open items: facts only the owner can give

1. **Port Express next round:** the page now says "เริ่มเรียนแล้ว 9 พ.ย." and asks people to message LINE about the next round. When is it, and what does it cost?
2. **Information parents can't find:**
   - online or on site (where)
   - class times
   - who teaches
   - how to pay, and whether instalments are possible
   - whether there is a certificate

   Search currently answers these with "ยังตอบไม่ได้".
3. **Students' full legal names:** removed from the page and its source (PDPA). Cards now show "น้อง<nickname>" only. Put names back only if consent is confirmed.
4. **LINE ID is @smart-school, not Hamster Hub:** should it be labelled "LINE ทางการของ Hamster Hub"?

## 6. Design work still to do

- Get owner/team sign-off on the cheese-with-works background and the flatter course/works sections.
- **Optional:**
  - two activity cards share a poster

## 7. Testing

- Playwright and Chromium are available. Wait for `#hhL` (the loader) to disappear before taking screenshots.
- Check at 1440×900, 1920×900 and 390×844 (mobile).
- Check the console for errors.
- Throttle the CPU to check smoothness. The last measurement after the performance work was about 60fps when scrolling, on both desktop and mobile.
