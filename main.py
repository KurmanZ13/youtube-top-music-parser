import pandas as pd
from parser.youtube import get_top_music_videos
from parser.youtube_download import download_audio_flac

if __name__ == "__main__":
    videos = get_top_music_videos()

    data = []

    for i, video in enumerate(videos[:5], start=1):
        title = video["snippet"]["title"]
        views = video["statistics"].get("viewCount", "0")
        video_id = video["id"]
        url = f"https://www.youtube.com/watch?v={video_id}"

        print(f"{i}. {title} — {views} просмотров")
        download_audio_flac(url)

        data.append({
            "№": i,
            "Название": title,
            "Просмотры": views,
            "Ссылка": url,
            "Файл": f"{title}.flac"
        })

    df = pd.DataFrame(data)
    df.to_csv("downloads/top_music.csv", index=False, encoding="utf-8-sig")
    print("📄 Данные сохранены в top_music.csv")
