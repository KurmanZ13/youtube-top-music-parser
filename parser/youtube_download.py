import yt_dlp


def download_audio_flac(url, path="downloads"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'quiet': True,
        'ffmpeg_location': r"C:\ffmpeg\bin",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '0',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"🎧 Скачано как FLAC: {url}")

