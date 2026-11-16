# Hamster Hub: Next.js version (in progress)

The site is being moved from `slime.html` (built from `new.html` plus layers) to Next.js + React + TypeScript + Tailwind CSS + Motion.

- Live preview: https://pepesx231.github.io/Hamterco/next/
- Run locally: `npm install && npm run dev`, then open http://localhost:3000/Hamterco/next/. Pictures load from `/Hamterco/img/`, so serve the repo root under `/Hamterco/` to see them.
- Publish: `npm run export`. This builds a static site into `../next/`. Then commit and push to `main` and `gh-pages`.

## What has been moved

| Part | Status |
|---|---|
| Header and phone menu | Done (square buttons) |
| Home hero: work cards round the headline (Fastwork layout on phones), typed headline, short who-we-are line, example questions typed in the bar, running orange light on the bar, handwriting "ไม่รู้จะเริ่มตรงไหน? ลองพิมพ์ถามดู", cards dock round the bar (desktop) or are pulled into it (phones) while searching | Done |
| คอร์สที่เราแนะนำ (Port Express + Hamstarter + National Project) | Done |
| Search answers | Not yet. Questions go to `slime.html?q=...` |
| Rest of home, courses, activity, works, about, loader | Not yet. Links go to `slime.html` |

## Where things are

- `lib/site.ts`: links, nav, headline wishes, example chips, and the example questions, and the work cards (picture, name, result line, desktop and phone spots)
- `components/Hero.tsx`: the hero
- `components/WorkCards.tsx`: the work cards; `lib/cardMotion.ts`: their search motion
- `components/Courses.tsx`: คอร์สที่เราแนะนำ
- `lib/useExamples.ts`: the typed example questions in the bar
- `components/HandDrawn.tsx`: the handwriting under the bar
- `components/TypedWish.tsx`: "น้องอยาก… <wish>"
