from yt_dlp import YoutubeDL

def download_video(url, quality):
    opts = get_opts(quality)
    try:
        with YoutubeDL(opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            print(f"[✔] Downloaded: {filename}")
            return filename
    except Exception as e:
        print(f"[!] Download failed: {e}")
        return None

def download_playlist(url, quality):
    opts = get_opts(quality)
    opts['noplaylist'] = False
    try:
        with YoutubeDL(opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"[!] Playlist download failed: {e}")

def get_opts(quality):
    format_map = {
        "low": "bestvideo[height<=360]+bestaudio/best",
        "medium": "bestvideo[height<=720]+bestaudio/best",
        "high": "bestvideo[height<=1080]+bestaudio/best",
        "very high": "bestvideo+bestaudio/best"
    }
    return {
        'format': format_map.get(quality, "bestvideo[height<=360]+bestaudio/best"),
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  # Try to merge to mp4 always
        'quiet': False,
        'allow_unplayable_formats': True,   # accept more types
        'ignoreerrors': True,               # don't break on individual failures
        'retries': 10,
        'concurrent_fragment_downloads': 5
    }

def input_links():
    print("Enter the links of the videos (type 'STOP' to finish):")
    links = []
    while True:
        link = input()
        if link.lower() == "stop":
            break
        links.append(link)
    return links
