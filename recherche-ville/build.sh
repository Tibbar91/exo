#!/usr/bin/env bash
# rapport.md -> rapport.html -> rapport.pdf
# Ne refait aucune analyse : rendu seulement. Editez rapport.md puis relancez.
set -euo pipefail
cd "$(dirname "$0")"

SRC="${1:-rapport.md}"
BASE="${SRC%.md}"

command -v python3 >/dev/null || { echo "python3 introuvable" >&2; exit 1; }

CHROME=""
for c in chromium chromium-browser google-chrome google-chrome-stable \
         /opt/pw-browsers/chromium-*/chrome-linux/chrome \
         /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell; do
  if command -v "$c" >/dev/null 2>&1; then CHROME="$c"; break; fi
  for g in $c; do [ -x "$g" ] && { CHROME="$g"; break 2; }; done
done
[ -n "$CHROME" ] || { echo "Aucun binaire Chrome/Chromium trouve" >&2; exit 1; }

echo "==> Markdown -> HTML"
python3 md2html.py "$SRC" "$BASE.html"

echo "==> HTML -> PDF ($CHROME)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
"$CHROME" --headless --disable-gpu --no-sandbox \
  --user-data-dir="$TMP" \
  --no-pdf-header-footer \
  --print-to-pdf="$BASE.pdf" \
  "file://$PWD/$BASE.html" 2>/dev/null

[ -s "$BASE.pdf" ] || { echo "PDF vide ou non genere" >&2; exit 1; }
echo "==> OK : $BASE.pdf ($(du -h "$BASE.pdf" | cut -f1))"
