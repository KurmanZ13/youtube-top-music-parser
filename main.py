import os
import csv
from parser.youtube import get_top_music_videos
from parser.youtube_download import download_audio_flac


def main():
    year = input("Enter a year: ").strip()
    folder_path = os.path.join("downloads", year)
    os.makedirs(folder_path, exist_ok=True)

    print(f"🔎 Fetching top music videos for {year}...")
    videos = get_top_music_videos(year)

    if not videos:
        print("❌ No valid music videos found.")
        return

    # Limit to top 5 by view count
    videos = videos[:5]

    csv_path = os.path.join(folder_path, "top_music.csv")
    with open(csv_path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Views", "YouTube URL"])

        for i, video in enumerate(videos, start=1):
            title = video["snippet"]["title"]
            views = video["statistics"].get("viewCount", "0")
            video_id = video["id"]
            url = f"https://www.youtube.com/watch?v={video_id}"

            print(f"{i}. {title} — {int(views):,} views")
            try:
                download_audio_flac(url, path=folder_path)
            except Exception as e:
                print(f"⚠️ Failed to download: {e}")
                continue

            writer.writerow([title, views, url])
            print(f"🎧 Saved as FLAC: {url}")

    print("\n✅ Finished downloading top music of", year)


if __name__ == "__main__":
    main()
