#!/usr/bin/env bash
set -e
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "[SMOKE] UI Frontend SignalBet v5"
for f in README.md manifest.json src/index.html src/styles/main.css src/js/app.js data/mock-data.js; do
  if [ ! -f "$ROOT_DIR/$f" ]; then
    echo "Missing required file: $f"
    exit 1
  fi
done
echo "All required files exist."
echo "Open src/index.html in a browser to verify navigation and states."
