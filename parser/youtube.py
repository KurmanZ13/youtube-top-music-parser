import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=api_key)


def get_top_music_videos():
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode="US",
        videoCategoryId="10",  # Music category
        maxResults=50
    )
    response = request.execute()
    return response["items"]
