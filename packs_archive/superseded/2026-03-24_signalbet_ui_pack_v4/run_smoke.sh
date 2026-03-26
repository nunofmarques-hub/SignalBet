#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
ENTRY="$ROOT/src/index.html"
if [ ! -f "$ENTRY" ]; then
  echo "[FAIL] index.html não encontrado em src/"
  exit 1
fi
if [ ! -f "$ROOT/manifest.json" ]; then
  echo "[FAIL] manifest.json não encontrado"
  exit 1
fi
if [ ! -f "$ROOT/data/mock-data.js" ]; then
  echo "[FAIL] mock-data.js não encontrado"
  exit 1
fi
echo "[OK] Estrutura base encontrada"
echo "[OK] Entry point: $ENTRY"
echo "[OK] Pack pronto para abrir no browser"
