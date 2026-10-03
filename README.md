# Kingdom of Logic: Android app

This folder turns the Kingdom of Logic game into an Android app (`.apk`).
GitHub builds the app for you, for free. You do not need Android Studio or a programmer's computer.

The game works fully offline. Fonts are built in. Progress is saved on the phone.

## Get the APK on your phone

You need a free GitHub account (github.com/signup) and about 10 minutes. The first build takes about 5 to 10 minutes.

### 1. Make a repository
1. Sign in to GitHub. Tap **+** (top right), then **New repository**.
2. Name it `kingdom-of-logic`. Choose **Public** (this makes the download link easy to open on a phone). Tap **Create repository**.

### 2. Upload this folder
1. Unzip `kingdom-of-logic-android.zip` on your computer.
2. On the new repository page, click **uploading an existing file**.
3. Open the unzipped folder and drag **everything inside it** into the browser: the `www`, `assets`, `tools` and `.github` folders and all the loose files.
   - If you cannot see the `.github` folder, it is hidden. On Mac press Cmd + Shift + . in Finder. On Windows it shows normally.
   - If `.github` still won't upload, do step 3 instead of dragging it.
4. Click **Commit changes**.

### 3. Only if `.github` did not upload
1. On the repository page click **Add file**, then **Create new file**.
2. In the name box type exactly `.github/workflows/build-apk.yml` (typing each `/` makes a folder).
3. Open `build-apk.yml` from the unzipped folder, copy all of it, paste it into the big box, and click **Commit changes**.

### 4. Let GitHub build it
1. Click the **Actions** tab. A run called **Build Android APK** starts by itself. (If it asks, click **I understand my workflows, go ahead and enable them**.)
2. Wait for the green tick. If it never started, click **Build Android APK** on the left, then **Run workflow**.

### 5. Download it on the phone
1. On the phone, open the repository in the browser (or the GitHub app) and tap **Releases** on the right side of the page. If you can't see it, open `github.com/YOUR-NAME/kingdom-of-logic/releases/tag/latest`.
2. Tap **KingdomOfLogic.apk** to download it.
3. Open the downloaded file. Android will ask permission to install apps from this source. Tap **Settings**, switch on **Allow from this source**, go back, and tap **Install**.
4. Tap **Open**. The crystal icon is also on your home screen.

If you only have a computer, download the file from the **Actions** run page (under *Artifacts*, it comes inside a `.zip`) and send it to the phone by cable, Drive or email.

### If something goes wrong
- **"Blocked by Play Protect" or "unknown app":** tap **More details**, then **Install anyway**. This warning appears because the app is not from the Play Store.
- **"App not installed":** an older copy signed differently may exist. Uninstall it, then install again.
- **Red cross in Actions:** open the run, open the red step, and copy the last 30 lines of its log to whoever is helping you. The app files themselves were tested, but the Android build step runs for the first time on GitHub.
- **No Releases section:** the last workflow step failed or the repository is private. Use the Artifacts download on the run page instead.

## Update the game later
Replace `www/index.html` with the new game file (with fonts built in, see below) and commit it. GitHub builds a new APK. Install it over the old one and progress is kept.

## For developers
- `www/index.html` is the whole game. Regenerate it from the standalone HTML with `npm i --no-save @fontsource/baloo-2 @fontsource/nunito` then `python3 tools/make_www.py kingdom-of-logic-standalone.html .`
- `tools/android-back.js` is added to that page: the Android Back button steps out of a screen (and a second Back on the home screen leaves the app).
- `assets/*.png` come from `python3 tools/make_icons.py` (needs Playwright with Chromium).
- Local build: needs Node 22, JDK 21 and the Android SDK (platform 36). Run `npm ci`, `npm run android:prepare`, `npm run android:apk`. The APK is `android/app/build/outputs/apk/debug/app-debug.apk`.
- App id `com.kingdomoflogic.game`. This is a debug-signed build for sideloading. A Play Store release needs your own signing key and `./gradlew bundleRelease`.
