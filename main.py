import yt_dlp
import os
import uuid
from downloader import download_audio


def download_audio(url):
    filename = f"temp/{uuid.uuid4()}.%(ext)s"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")

    return file_path