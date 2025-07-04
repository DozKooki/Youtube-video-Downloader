


# DozKooki YouTube Downloader & Converter (yt-dlp Edition)

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Latest-green)
![MoviePy](https://img.shields.io/badge/MoviePy-Working-orange)
![License](https://img.shields.io/badge/license-MIT-purple)
![Maintained](https://img.shields.io/badge/status-maintained-brightgreen)

---

🚀 **DozKooki YouTube Downloader & Converter v0.3**

A powerful multi-purpose YouTube downloader and converter built with Python.  
Features a user-friendly command-line interface, support for playlists, quality selection, and seamless MP3 conversion — all powered by `yt-dlp` to handle even the latest YouTube streaming changes (including SABR).

---

## 📌 Features

- ✅ **Manual Video Downloader**
- ✅ **Playlist Downloader**
- ✅ **Automatic MP3 Conversion**
- ✅ **Quality Selection:** low (360p), medium (720p), high (1080p), very high (4K)
- ✅ **Handles SABR & adaptive streams with merging**
- ✅ **Merge video & audio automatically into MP4**
- ✅ **Gracefully skips broken links or unavailable formats**

---

## 🛠 Requirements

- Python `3.9+` (Tested up to `3.13`)
- `yt-dlp`
- `moviepy`
- `imageio-ffmpeg`

## 📥 Installation

You can set up this downloader on your local machine in two easy ways:

---

### 🚀 Clone with Git (Recommended)

```bash
git clone https://github.com/DozKooki/Youtube-video-Downloader
cd Youtube-video-Downloader
````

---

### 📦 Or download as ZIP

1. Click the green `Code` button on this repository.
2. Select `Download ZIP`.
3. Extract it to a folder (e.g. `Youtube-video-Downloader`).

---

### 🛠 Install Python dependencies

Make sure you are inside the project directory:

```bash
cd Youtube-video-Downloader
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

---

✅ Now you’re ready to run:

```bash
python main.py
```

Or on Windows:

```
RUN-DOWNLOADER.bat
```



## 💻 Menu Options

```text
(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3
```

* **Manual video:**

  * Enter multiple YouTube links (type `STOP` when done)
  * Choose quality (360p/720p/1080p/4K)

* **Playlist:**

  * Enter the playlist URL
  * Downloads all videos in selected quality

* **Convert to MP3:**

  * Downloads videos at low (360p) quality
  * Extracts audio and saves `.mp3`

---

## ⚙️ Quality Options

| Quality Option | Internally selects format                |
| -------------- | ---------------------------------------- |
| `low`          | `bestvideo[height<=360]+bestaudio/best`  |
| `medium`       | `bestvideo[height<=720]+bestaudio/best`  |
| `high`         | `bestvideo[height<=1080]+bestaudio/best` |
| `very high`    | `bestvideo+bestaudio/best`               |

Automatically merges video + audio into final `.mp4`.

---

## 🚀 .BAT File

Included:

```
RUN-DOWNLOADER.bat
```

Just double-click on Windows to launch your Python downloader with no terminal typing.

---

## 🧰 Troubleshooting

* **Signature extraction failed / SABR**
  YouTube is switching to SABR segment streaming. This downloader uses advanced `yt-dlp` merging to fetch fragmented streams.
  ✅ It retries and merges automatically.
  ✅ If some videos still fail, re-run or try different quality.

* **MoviePy conversion errors**
  Ensure `ffmpeg` is bundled. `imageio-ffmpeg` from pip handles it for you.

* **Permission denied on Windows**
  Run terminal or `.bat` file as Administrator.

---

## 📚 Contributing

✅ Fork & clone this repo
✅ Submit pull requests for new features, like:

* GUI with Tkinter / PyQt
* Batch download from text files
* Telegram bot or Discord bot wrapper

---

## 📝 License

MIT — free to modify & distribute.
Project by **DozKooki**.

---

## 💖 Made with ❤️ by DozKooki

Enjoy your supercharged YouTube Downloader & Converter 🚀

```
