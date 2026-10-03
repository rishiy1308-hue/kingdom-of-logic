#!/usr/bin/env bash
# Creates the Android project from the loose files in this folder:
# Capacitor project + dark theme + icon + the game. Needs `npm ci` first.
set -euo pipefail
cd "$(dirname "$0")"

for f in index.html icon-only.png icon-foreground.png icon-background.png splash.png splash-dark.png capacitor.config.json patch_android.py; do
  [ -f "$f" ] || { echo "ERROR: $f is missing from the repository. Upload it to the top level of the repository (not inside a folder) and run the build again."; exit 1; }
done

mkdir -p www assets
cp index.html www/index.html
cp icon-only.png icon-foreground.png icon-background.png splash.png splash-dark.png assets/

[ -d android ] || npx cap add android
python3 patch_android.py
npx capacitor-assets generate --android \
  --iconBackgroundColor '#0a1d2b' --splashBackgroundColor '#0a1d2b' --splashBackgroundColorDark '#0a1d2b'
npx cap sync android
echo "Android project ready in ./android"
