#!/bin/sh
# Serves the built site the way GitHub Pages does: http://localhost:8791/Hamterco/next/ (pictures from /Hamterco/img/).
# Run from the repo root after `cd web && npm run export`.
ROOT=$(cd "$(dirname "$0")/../.." && pwd)
SRV=${TMPDIR:-/tmp}/hh-srv
mkdir -p "$SRV/Hamterco"
ln -sfn "$ROOT/img" "$SRV/Hamterco/img"
ln -sfn "$ROOT/web/out" "$SRV/Hamterco/next"
cd "$SRV" && exec python3 -m http.server 8791
