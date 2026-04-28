import yt_dlp
import os
ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg.exe")
def download_youtube_audio(url):
    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': '%(title)s.%(ext)s',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0'
        },
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = input("Силка на відео: ")
    download_youtube_audio(video_url)
    print("Ok")