#!/usr/bin/env python3
"""Customise the freshly generated Capacitor Android project (run after `npx cap add android`).
Safe to run more than once. Makes the app portrait-only and dark, so no white bars appear."""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent / "android" / "app" / "src" / "main"
res = root / "res" / "values"

def need(cond, msg):
    if not cond:
        sys.exit("patch_android.py: " + msg)

# 1. night colour resource
(res / "colors.xml").write_text(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n'
    '    <color name="kol_night">#0A1D2B</color>\n</resources>\n', encoding="utf-8")

# 2. theme: dark window, status bar and navigation bar; dark Android 12+ splash
sp = res / "styles.xml"
s = sp.read_text(encoding="utf-8")
if "kol_night" not in s:
    s, n1 = re.subn(
        r'(<style name="AppTheme\.NoActionBar"[^>]*>.*?)(\s*</style>)',
        lambda m: m.group(1)
        + '\n        <item name="android:windowBackground">@color/kol_night</item>'
        + '\n        <item name="android:statusBarColor">@color/kol_night</item>'
        + '\n        <item name="android:navigationBarColor">@color/kol_night</item>'
        + m.group(2), s, count=1, flags=re.S)
    s, n2 = re.subn(
        r'(<style name="AppTheme\.NoActionBarLaunch"[^>]*>.*?)(\s*</style>)',
        lambda m: m.group(1) + '\n        <item name="windowSplashScreenBackground">@color/kol_night</item>' + m.group(2),
        s, count=1, flags=re.S)
    need(n1 == 1 and n2 == 1, "styles.xml did not look as expected")
    sp.write_text(s, encoding="utf-8")

# 3. launcher background colour
lb = res / "ic_launcher_background.xml"
if lb.exists():
    lb.write_text(lb.read_text(encoding="utf-8").replace("#FFFFFF", "#0A1D2B"), encoding="utf-8")

# 4. portrait only
mp = root / "AndroidManifest.xml"
m = mp.read_text(encoding="utf-8")
if "screenOrientation" not in m:
    m, n = re.subn(r'android:launchMode="singleTask"', 'android:launchMode="singleTask"\n            android:screenOrientation="portrait"', m, count=1)
    need(n == 1, "AndroidManifest.xml did not look as expected")
    mp.write_text(m, encoding="utf-8")

print("patch_android.py: ok")
