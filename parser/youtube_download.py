import os

import yt_dlp


def download_audio_flac(url, path="downloads"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'quiet': True,
        'ignoreerrors': True,
        'ffmpeg_location': r'C:\ffmpeg\bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '0',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"🎧 Скачано как FLAC: {url}")
    except Exception as e:
        print(f"❌ Пропущено (ошибка скачивания): {url}")
        print(f"   Причина: {str(e)}")
