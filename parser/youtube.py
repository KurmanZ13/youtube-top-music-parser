import os
import isodate
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env
load_dotenv()

# Get the YouTube API key
api_key = os.getenv("YOUTUBE_API_KEY")

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=api_key)


def get_top_music_videos(year: str):
    """
    Fetches top music videos for a given year by keyword search,
    filtering out shorts, lives, and overly long videos.
    """
    published_after = f"{year}-01-01T00:00:00Z"
    published_before = f"{year}-12-31T23:59:59Z"

    all_videos = []
    next_page_token = None

    for _ in range(12):  # Up to 600 videos (12 pages * 50 results)
        search_request = youtube.search().list(
            part="snippet",
            maxResults=50,
            publishedAfter=published_after,
            publishedBefore=published_before,
            type="video",
            order="viewCount",
            q="official music video",  # Keyword-based search
            pageToken=next_page_token
        )
        search_response = search_request.execute()

        video_ids = [item["id"]["videoId"] for item in search_response.get("items", [])]
        if not video_ids:
            break

        details_response = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(video_ids)
        ).execute()

        for video in details_response.get("items", []):
            if is_valid_music_video(video):
                all_videos.append(video)

        next_page_token = search_response.get("nextPageToken")
        if not next_page_token:
            break

    print(f"✔ Found {len(all_videos)} valid music videos")
    return sorted(all_videos, key=lambda x: int(x["statistics"]["viewCount"]), reverse=True)


def duration_in_seconds(iso_duration: str) -> int:
    """
    Converts ISO 8601 duration string to total seconds.
    """
    try:
        return int(isodate.parse_duration(iso_duration).total_seconds())
    except Exception:
        return 0


def is_valid_music_video(video) -> bool:
    """
    Checks if a video is a valid music clip:
    - Not a live stream
    - Not a short (under 60 seconds)
    - Not longer than 1 hour
    - Has necessary metadata (ID, title, views)
    """
    snippet = video.get("snippet", {})
    statistics = video.get("statistics", {})
    details = video.get("contentDetails", {})

    # Skip live streams
    if snippet.get("liveBroadcastContent") == "live":
        return False

    # Skip shorts (<60s) and long content (>1h)
    duration = details.get("duration", "")
    seconds = duration_in_seconds(duration)
    if seconds < 60 or seconds > 3600:
        return False

    return all([
        video.get("id"),
        snippet.get("title"),
        statistics.get("viewCount"),
    ])
