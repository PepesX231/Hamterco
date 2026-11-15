# Hamster Hub: Next.js version (in progress)

The site is being moved from `slime.html` (built from `new.html` plus layers) to Next.js + React + TypeScript + Tailwind CSS + Motion.

- Live preview: https://pepesx231.github.io/Hamterco/next/
- Run locally: `npm install && npm run dev`, then open http://localhost:3000/Hamterco/next/. Pictures load from `/Hamterco/img/`, so serve the repo root under `/Hamterco/` to see them.
- Publish: `npm run export`. This builds a static site into `../next/`. Then commit and push to `main` and `gh-pages`.

## What has been moved

| Part | Status |
|---|---|
| Header and phone menu | Done |
| Home hero: cheese with works in the holes (clips play), typed headline, search bar, example chips, pencil arrow and note, pencil loop on phones, peeking hamsters | Done |
| Search answers | Not yet. Questions are sent to `slime.html?q=...`, which answers them (layer `99zzzzzzzzzzzzzz-q.html`) |
| Rest of the home page, courses, activity, works, about, loader | Not yet. Links go to `slime.html` |

## Where things are

- `lib/site.ts`: links, nav, headline wishes, example chips, and the list of holes (position, size, picture, clip, name)
- `components/Hero.tsx`: the hero
- `components/CheeseHoles.tsx`: the holes; pictures load after the page, clips play only while the hero is on screen and nobody is searching
- `components/HandDrawn.tsx`: pencil arrow + note (desktop), pencil loop (phones)
- `components/TypedWish.tsx`: "น้องอยาก… <wish>"
