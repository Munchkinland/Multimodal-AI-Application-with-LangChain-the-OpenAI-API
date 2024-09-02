import os
import yt_dlp as youtube_dl
from yt_dlp import DownloadError
import openai

# Configuración del API Key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def download_and_transcribe_video(youtube_url):
    output_dir = "app/static/audio/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_config = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "ffmpeg_location": "C:\\ffmpeg\\ffmpeg-2024-08-28-git-b730defd52-full_build\\bin",
        "verbose": True
    }

    try:
        with youtube_dl.YoutubeDL(ydl_config) as ydl:
            result = ydl.extract_info(youtube_url, download=True)
            audio_file = ydl.prepare_filename(result).replace('.webm', '.mp3')

        # Transcribe the audio file
        try:
            with open(audio_file, "rb") as audio:
                response = openai.Audio.transcribe("whisper-1", audio)
                transcript = response["text"]

            # Save the transcript to a file
            transcript_file_path = audio_file.replace('.mp3', '.txt')
            with open(transcript_file_path, 'w') as transcript_file:
                transcript_file.write(transcript)

            return transcript, transcript_file_path  # Return both the transcript and the path to the transcript file

        except Exception as e:
            return f"Error during transcription: {str(e)}", None

    except DownloadError as e:
        return f"Error downloading the video: {str(e)}", None
