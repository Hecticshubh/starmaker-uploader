# 🚀 Termux + Termux:X11 Setup

This guide explains how to set up the StarMaker Upload Automation project on Android using Termux, Termux:X11, Chromium, and Selenium.

> 💡 Follow the steps in order. Complete the Termux environment setup first, then configure the project files and run the automation.

---

## 📋 Setup Flow

```text
Download Termux
      ↓
Update Termux
      ↓
Download Termux:X11
      ↓
Install Python
      ↓
Install Git
      ↓
Install Project Requirements
      ↓
Install X11 Repository
      ↓
Install Termux:X11 Package
      ↓
Install Chromium
      ↓
Install ChromeDriver
      ↓
Install Openbox
      ↓
Start Termux:X11
      ↓
Start Openbox
      ↓
Test Chromium
      ↓
Configure Project
      ↓
Run Automation
```

---

# 📱 1. Install Termux

Download Termux from the official F-Droid page.

🔗 https://f-droid.org/packages/com.termux/

> ⚠️ Use the official Termux distribution. Avoid random APK websites.

Install Termux on your Android device.

---

# 🖥️ 2. Install Termux:X11

Termux:X11 is required to provide the graphical display needed to run Chromium.

Download the latest Termux:X11 release from the official GitHub repository:

🔗 https://github.com/termux/termux-x11/releases

Install the Termux:X11 APK on your Android device.

> 💡 You need both:
>
> `Termux`
>
> and
>
> `Termux:X11`

---

# 🔄 3. Update Termux

Open Termux and run:

```bash
pkg update
pkg upgrade
```

If Termux asks for confirmation, type:

```text
y
```

and press Enter.

---

# 🐍 4. Install Python

Install Python:

```bash
pkg install python
```

Check the installation:

```bash
python --version
```

You should see the installed Python version.

---

# 📦 5. Install Git

Git is useful for downloading and managing the project from GitHub.

Install Git:

```bash
pkg install git
```

Check the installation:

```bash
git --version
```

---

# 📥 6. Get the Project

Download or clone the project into Termux.

For example:

```bash
git clone https://github.com/Hecticshubh/starmaker-uploader.git
```

Then enter the project directory:

```bash
cd starmaker-uploader
```

# 🧰 7. Install Python Requirements

From inside the project directory, run:

```bash
python -m pip install -r requirements.txt
```

This installs the Python packages required by the project.

The project uses:

```text
Python
Pytest
Selenium
```

---

# 🖥️ 8. Install X11 Repository

Enable the Termux X11 repository:

```bash
pkg install x11-repo
```

---

# 📺 9. Install Termux:X11 Package

Install the Termux:X11 package:

```bash
pkg install termux-x11-nightly
```

---

# 🌐 10. Install Chromium

Install Chromium:

```bash
pkg install chromium
```

Check the Chromium command:

```bash
which chromium-browser
```

The project configuration expects the Chromium executable at:

```text
/data/data/com.termux/files/usr/bin/chromium-browser
```

---

# 🚗 11. Install ChromeDriver

Install ChromeDriver:

```bash
pkg install chromedriver
```

Check the installation:

```bash
which chromedriver
```

---

# 🪟 12. Install Openbox

Openbox is used as a lightweight window manager for the Termux:X11 environment.

Install it with:

```bash
pkg install openbox
```

Check the installation:

```bash
which openbox
```

---

# 🖥️ 13. Start Termux:X11

First open the Termux:X11 application on your Android device.

Then return to the Termux terminal and run:

```bash
termux-x11 :0 &
```

Set the display:

```bash
export DISPLAY=:0
```

You can verify the display variable:

```bash
echo $DISPLAY
```

It should show:

```text
:0
```

---

# 🪟 14. Start Openbox

Start Openbox with:

```bash
openbox &
```

Termux:X11 should now provide the graphical environment required by Chromium.

---

# 🌐 15. Test Chromium

Run:

```bash
chromium-browser
```

Chromium should open inside the Termux:X11 environment.

> ⚠️ If Chromium does not open, check the troubleshooting section below before continuing.

---

# ⚙️ 16. Configure the Project

The repository contains separate Selenium configuration files for different platforms.

For Android / Termux, use:

```text
conftest_termux.py
```

Rename it to:

```text
conftest.py
```

## Important

Before running the project, make sure there is only one active `conftest.py` file.

For the Termux setup, the project should look like:

```text
starmaker-uploader/
├── test_upload.py
├── conftest.py
├── conftest_desktop.py
├── requirements.txt
├── .gitignore
├── README.md
└── SETUP.md
```

Here:

```text
conftest.py
```

is the active Termux configuration.

```text
conftest_desktop.py
```

is the separate desktop configuration.

> 💡 Do not delete `conftest_desktop.py`.
>
> Keep it in the project as the alternate desktop configuration.
>
> Only `conftest.py` is automatically loaded by Pytest.

### If `conftest.py` Already Exists

If the project folder already contains:

```text
conftest.py
```

replace that file with the Termux configuration.

The final active configuration must be:

```text
conftest.py
```

Do not keep two different files named `conftest.py`.

---

# 📂 17. Move to the Project Directory

Make sure you are inside the project folder:

```bash
cd starmaker-uploader
```

Check the files:

```bash
ls
```

You should see files similar to:

```text
test_upload.py
conftest.py
conftest_desktop.py
requirements.txt
README.md
SETUP.md
```

---

# 📱 18. Allow Storage Access

To access files stored on your Android device, run:

```bash
termux-setup-storage
```

Android will ask for storage permission.

Allow the permission.

After that, Termux will provide access to shared storage through:

```text
~/storage/shared/
```

For example:

```text
~/storage/shared/Music/
```

or:

```text
~/storage/shared/Pictures/
```

---

# 🎵 19. Check Your File Paths

The automation asks for:

```text
Audio file path
Image file path
```

Example:

```text
/storage/emulated/0/Music/song.mp3
```

Example:

```text
/storage/emulated/0/Pictures/cover.jpg
```

You can also use the Termux shared-storage path:

```text
~/storage/shared/Music/song.mp3
```

and:

```text
~/storage/shared/Pictures/cover.jpg
```

> 💡 Make sure the file paths point to real files before running the automation.

---

# ▶️ 20. Run the Project

From the project directory, run:

```bash
pytest -s
```

The `-s` option keeps the project's input prompts and status messages visible in the terminal.

---

# 👤 21. Enter StarMaker Login Details

When the program starts, it will ask for:

```text
Enter email:
Enter password:
```

Enter your StarMaker account details.

> 🔐 Never place your real password directly inside the source code.

---

# 🎵 22. Enter Song Information

The program will ask for:

```text
Enter audio file path:
Enter image file path:
Enter title:
Enter artist name:
Enter language:
```

Enter the correct information for the song.

---

# 📜 23. Enter Lyrics

The program will display a lyrics section.

Paste or type the lyrics line by line.

Example:

```text
First lyric line
Second lyric line
Third lyric line
Fourth lyric line
Fifth lyric line
```

When you finish entering the lyrics, type:

```text
End
```

on a separate line.

Example:

```text
First lyric line
Second lyric line
Third lyric line
Fourth lyric line
End
```

> 💡 A minimum of 4 lyric lines is required.

Blank lyric lines are also supported.

---

# 🔄 24. Upload Workflow

After the required information is entered, the automation performs the upload workflow:

```text
Open StarMaker
      ↓
Login
      ↓
Open Upload Tracks
      ↓
Upload Audio
      ↓
Add Song Details
      ↓
Upload Cover Image
      ↓
Select Language
      ↓
Enter Lyrics
      ↓
Synchronize Lyrics
      ↓
Confirm
      ↓
Complete
```

---

# 🧪 25. Verify Pytest

You can verify that Pytest is installed with:

```bash
pytest --version
```

You can verify Selenium with:

```bash
python -c "import selenium; print(selenium.__version__)"
```

---

# 🛠️ Troubleshooting

## Chromium Does Not Start

Check Chromium:

```bash
which chromium-browser
```

Make sure the result points to:

```text
/data/data/com.termux/files/usr/bin/chromium-browser
```

Also make sure Termux:X11 is running.

Then set:

```bash
export DISPLAY=:0
```

and try again:

```bash
chromium-browser
```

---

## Termux:X11 Does Not Display Chromium

Make sure Termux:X11 is open on the Android device.

Then run:

```bash
termux-x11 :0 &
export DISPLAY=:0
openbox &
```

Try Chromium again:

```bash
chromium-browser
```

---

## ChromeDriver Problem

Check ChromeDriver:

```bash
which chromedriver
```

Then check the version:

```bash
chromedriver --version
```

Also check Chromium:

```bash
chromium-browser --version
```

The browser and driver should be compatible.

---

## Pytest Does Not Find the Test

Make sure the test file keeps the name:

```text
test_upload.py
```

Pytest automatically discovers files matching its test naming conventions.

Run:

```bash
pytest -s
```

---

## `conftest.py` Configuration Problem

Make sure the Termux configuration has been renamed:

```text
conftest_termux.py
        ↓
   rename to
        ↓
conftest.py
```

The desktop file can remain:

```text
conftest_desktop.py
```

Do not rename the desktop file to another `conftest.py`.

The project should have only one active file named:

```text
conftest.py
```

---

# 🔐 Security

The script asks for the StarMaker email and password at runtime.

Do not:

```text
hard-code your password
```

Do not commit real login credentials to GitHub.

Before publishing your repository, also check:

```text
file paths
personal information
cookies
session data
browser profiles
.env files
passwords
API keys
```

---

# ✅ Setup Complete

Your Android environment is now ready for the StarMaker Upload Automation project.

The important final structure is:

```text
starmaker-uploader/
├── test_upload.py
├── conftest.py
├── conftest_desktop.py
├── requirements.txt
├── .gitignore
├── README.md
└── SETUP.md
```

For Android / Termux:

```text
conftest_termux.py
        ↓
     rename
        ↓
conftest.py
```

Keep:

```text
conftest_desktop.py
```

as a separate file.

Only:

```text
conftest.py
```

is used as the active Pytest configuration.

Then run:

```bash
pytest -s
```

---

# 🔗 Official Resources

### Termux

https://f-droid.org/packages/com.termux/

### Termux:X11

https://github.com/termux/termux-x11/releases

### Termux:X11 GitHub Repository

https://github.com/termux/termux-x11

### Selenium

https://www.selenium.dev/

### Pytest

https://pytest.org/

### Chromium

https://www.chromium.org/

---

# 🎉 Ready to Use

Your Termux + Termux:X11 environment is ready.

Start Termux:X11, start the required X11 environment, enter the project directory, and run:

```bash
pytest -s
```