from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_to_mp3(filename):
    try:
        clip = VideoFileClip(filename)
        clip.audio.write_audiofile(filename.rsplit('.', 1)[0] + ".mp3")
        print(f"[✔] Converted '{filename}' to MP3.")
    except Exception as e:
        print(f"[!] Conversion failed for {filename}: {e}")
    finally:
        if 'clip' in locals():
            clip.close()
