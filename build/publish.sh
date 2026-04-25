#!/usr/bin/env bash
# publish.sh — build NewMathAnalysis and push docs/ → hydrays.github.io
#
# Usage:
#   bash build/publish.sh              # commit message = "publish: update"
#   bash build/publish.sh "my message" # custom commit message
#
# Env:
#   HYDRAYS_IO  path to local hydrays.github.io checkout
#               (default: ~/Code/books/hydrays.github.io)

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${HYDRAYS_IO:-$HOME/Code/books/hydrays.github.io}"
MSG="${1:-publish: update}"

if [ ! -d "$TARGET/.git" ]; then
  echo "error: $TARGET is not a git repo" >&2
  exit 1
fi

echo "==> building"
python3 "$ROOT/build/build.py"

echo "==> syncing docs/ → $TARGET"
rsync -a --delete \
  --exclude='.git' --exclude='.gitignore' \
  "$ROOT/docs/" "$TARGET/"

cd "$TARGET"
if [ -z "$(git status --porcelain)" ]; then
  echo "==> nothing to publish"
  exit 0
fi

echo "==> committing and pushing"
git add -A
git commit -m "$MSG"
git push
echo "==> done"
