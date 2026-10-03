# Kingdom of Logic: Android app

GitHub builds this into an Android app (`.apk`) for you, for free. The game works offline and saves progress on the phone.

All files here sit at the top level on purpose, so you can upload them with a normal file picker. No folders are needed.

## Steps (on a computer)

### 1. Upload the files
1. Open your repository, click **Add file**, then **Upload files**.
2. Open this unzipped folder, select **all the files** (Ctrl+A or Cmd+A) and drag them into the page. Wait until all of them are listed.
3. Click **Commit changes**.

### 2. Start the build (this moves one file)
1. In the repository, click **build-apk.yml** to open it, then click the **pencil** icon (Edit).
2. Click the file name box at the top. Click at the very start of the name, and type `.github/workflows/` so it reads `.github/workflows/build-apk.yml`.
3. Click **Commit changes**, then **Commit changes** again.

The build starts by itself. Do this step last, after all the other files are uploaded.

### 3. Wait for the green tick
Open the **Actions** tab. A run called **Build Android APK** takes about 5 to 10 minutes. If it never starts, click **Build Android APK** on the left, then **Run workflow**.

### 4. Install on the phone
1. On the phone, open `github.com/YOUR-NAME/kingdom-of-logic/releases/tag/latest`.
2. Tap **KingdomOfLogic.apk** to download it.
3. Open the downloaded file. Allow "install from this source" if asked, then tap **Install**.
4. If Play Protect warns you, tap **More details**, then **Install anyway**. The warning appears because the app is not from the Play Store.

The APK is also in the Actions run under *Artifacts* (inside a .zip).

## If the build shows a red cross
Open the run, open the red step, and copy the last 30 lines of its log. A message that starts with `ERROR:` names a file that did not upload: add it at the top level of the repository and press **Run workflow**.
