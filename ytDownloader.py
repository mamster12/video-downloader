import os
import sys
from yt_dlp import YoutubeDL

def download_video(url):
    output_dir = r"/tyDownloads"  # Update this path

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    ydl_opts = {
        'format': '(bestvideo[height<=1080][ext=mp4]/bestvideo)+bestaudio/best',
        'merge_output_format': 'mp4',
        'writeautomaticsub': True,
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'ass/srt/best/vtt',
        'embedsubtitles': True,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_video.py <YouTube_URL>")
        sys.exit(1)

    youtube_url = "links.txt"

with open(youtube_url) as links:
    for link in links:
        download_video(link)