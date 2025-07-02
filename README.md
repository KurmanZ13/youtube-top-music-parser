# 🎵 YouTube Top Music Parser

A simple Python project to get the top 50 most-viewed music videos on YouTube and download their audio in FLAC format. Results are saved to a CSV file.

## Features

- Fetch top 50 trending music videos from YouTube (category: Music)
- Show video title, views, and link
- Download audio as `.flac`
- Save info to `top_music.csv`

## Installation

1. Clone the repo:

```bash
git clone git@github.com:KurmanZ13/youtube-top-music-parser.git
cd youtube-top-music-parser
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install FFmpeg and add it to your system PATH.

# **API Setup**

1. Get a YouTube Data API key from Google Cloud Console
2. Create a .env file in the project root:
```ini
YOUTUBE_API_KEY=your_api_key_here
```

# Usage
```bash
python main.py
```