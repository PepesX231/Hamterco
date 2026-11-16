# Hamster Hub: Next.js version (in progress)

The site is being moved from `slime.html` (built from `new.html` plus layers) to Next.js + React + TypeScript + Tailwind CSS + Motion.

- Live preview: https://pepesx231.github.io/Hamterco/next/
- Run locally: `npm install && npm run dev`, then open http://localhost:3000/Hamterco/next/. Pictures load from `/Hamterco/img/`, so serve the repo root under `/Hamterco/` to see them.
- Publish: `npm run export`. This builds a static site into `../next/`. Then commit and push to `main` and `gh-pages`.

## What is in the app

Every page is now a Next.js route: `/` (home), `/courses/`, `/activity/`, `/works/`, `/about/`.

| Part | How |
|---|---|
| Home hero, คอร์สที่เราแนะนำ, loading screen | React components (`components/`, `lib/loader.ts`) |
| Header and page transitions | The original header (tab animations, "เพิ่งจบ 14 พ.ย." roll) and its page wipe; views switch in place like the original, and the address bar follows the route. `components/Header.tsx` is a React version not used yet |
| Search answers | The original search engine runs in the page; `Hero.tsx` sends the question to it and shows its answer panel under the bar |
| Everything else (rest of home, courses, activity, works, about, footer) | `components/LegacyRuntime.tsx` runs the original markup, styles and scripts, built by `python3 ../dev/builds/legacy_next.py` into `public/legacy/`. Parts already rewritten in React are hidden there with `hide`. Next step: rewrite these one section at a time as components, then remove them from the legacy bundle |

`npm run export` rebuilds the legacy bundle, builds the app and copies it to `../next/` for GitHub Pages.

## Where things are

- `lib/site.ts`: links, nav, headline wishes, example chips, and the example questions, and the work cards (picture, name, result line, desktop and phone spots)
- `components/Hero.tsx`: the hero
- `components/WorkCards.tsx`: the work cards; `lib/cardMotion.ts`: their search motion
- `components/Courses.tsx`: คอร์สที่เราแนะนำ
- `lib/useExamples.ts`: the typed example questions in the bar
- `components/HandDrawn.tsx`: the handwriting under the bar
- `components/TypedWish.tsx`: "น้องอยาก… <wish>"
