# 🎵 StarMaker Upload Automation

A Selenium + Pytest based automation project for uploading songs to **StarMaker** from Android using **Termux, Termux:X11, and Chromium**.

The project handles the main upload flow from login through song details, lyrics entry, lyric synchronization, and confirmation.

---

## 🧩 Choose Your Platform

This project provides separate Selenium browser configurations for Android/Termux and desktop platforms.

«💡 **Choose the configuration that matches your device before running the project.**»

### 📱 Android / Termux

**Environment:**

`Android + Termux + Termux:X11 + Chromium`

**Configuration:**

`conftest_termux.py`

Rename it to:

`conftest.py`

Then continue with the **Termux + Termux:X11 Setup** in [SETUP.md](SETUP.md).

---

### 💻 Windows / Linux / macOS

**Environment:**

`Windows / Linux / macOS + Chrome/Chromium`

**Configuration:**

`conftest_desktop.py`

Rename it to:

`conftest.py`

Then install the required Python packages and run the project.

«⚠️ **Important: Only the configuration file for your platform should be named `conftest.py` before running the project.**»

---

## ✨ Features

- 🎵 Upload an audio track
- 🖼️ Upload cover artwork
- 📝 Enter song title and artist name
- 🌐 Select the song language
- 📜 Enter multi-line lyrics
- 🎶 Synchronize lyrics line by line
- 🤖 Automate Chromium with Selenium
- 🧪 Run the workflow with Pytest
- 🖥️ Use Chromium through Termux:X11 on Android
- 👤 Use a fresh browser profile by default, with an optional saved-profile setup

---

## 🔄 Workflow

```text
Start
  ↓
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

## 🛠️ Project Environment

### 📱 Android / Termux

```text
Android
   ↓
Termux
   ↓
Python + Pytest + Selenium
   ↓
Termux:X11
   ↓
Chromium + ChromeDriver
   ↓
StarMaker
```

### 💻 Windows / Linux / macOS

```text
Windows / Linux / macOS
   ↓
Python + Pytest + Selenium
   ↓
Chrome / Chromium
   ↓
Selenium WebDriver Management
   ↓
StarMaker
```

---

## 🧰 Technologies Used

| Component | Purpose |
|---|---|
| Termux | Main command-line environment |
| Termux:X11 | Graphical X11 display |
| Python | Runs the automation code |
| Pytest | Executes the project test |
| Selenium | Controls the web browser |
| Chromium | Web browser used on Termux |
| Chrome / Chromium | Web browser used on desktop platforms |
| ChromeDriver | Connects Selenium to Chromium |
| Selenium WebDriver Management | Handles WebDriver management on supported desktop platforms |
| Openbox | Lightweight X11 window manager |

---

## 📁 Project Structure

```text
starmaker-uploader/
│
├── test_upload.py
├── conftest_termux.py
├── conftest_desktop.py
├── requirements.txt
├── .gitignore
├── README.md
└── SETUP.md
```

> 💡 The repository does not include an active `conftest.py`.
> Choose the configuration for your platform and rename it to `conftest.py` before running the project.

### `test_upload.py`

Contains the main StarMaker automation workflow and collects the song information, file paths, language, and lyrics required for the upload.

### `conftest_termux.py`

Contains the Selenium and Pytest configuration required for running the project on Android through Termux, Termux:X11, and Chromium.

### `conftest_desktop.py`

Contains the Selenium and Pytest configuration for running the project on Windows, Linux, and macOS with Chrome or Chromium.

### `conftest.py`

The selected platform configuration must be renamed to `conftest.py` before running the project.

### `requirements.txt`

Lists the Python packages required by the project.

### `SETUP.md`

Contains the complete Termux + Termux:X11 installation and setup instructions.

### `.gitignore`

Defines files and folders that should not be committed to the repository.

---

## 📝 Lyrics Input

The project supports multi-line lyrics. During execution, enter the lyrics line by line and type:

```text
End
```

on a separate line when finished.

A minimum of **4 lyric lines** is required.

---

## 👤 Browser Profile

The default configuration creates a temporary Chromium profile for each session. The temporary profile is removed when the browser session ends.

A persistent profile can be enabled in `conftest.py` by using the provided `--user-data-dir` configuration instead of the temporary profile.

---

## ▶️ Run

After completing the environment setup described in `SETUP.md`, run the project from its directory with:

```bash
pytest -s
```

The `-s` option keeps the project's prompts and status messages visible in the terminal.

---

## 🔐 Security

The script asks for the StarMaker email and password at runtime. Do not hard-code real credentials or commit sensitive information to a public GitHub repository.

Review local file paths and other personal configuration before publishing the repository.

---

## 📚 Setup Guide

For installation and environment configuration, see:

**[SETUP.md](SETUP.md)**
