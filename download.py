import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from moviepy import AudioFileClip

import subprocess



class Download:
    def __init__(self, youtube_url,download_formet,download_type):
        self.youtube_url = youtube_url
        self.download_formet = download_formet
        self.download_type = download_type

    def single_download(self):

        yt = YouTube(self.youtube_url, on_progress_callback=on_progress)
        print(yt.title)

        download_folder = "download"

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)


      
        if self.download_formet == 'video':
                stream = yt.streams.get_highest_resolution()
                if stream:
                    file_path = stream.download(output_path=download_folder)
                    return [file_path]
                else:
                    return 'notFound'

        elif self.download_formet == 'audio':
            stream = yt.streams.get_audio_only()
            if stream:
                audio_path = stream.download(output_path=download_folder)
                # mp3_path = os.path.splitext(audio_path)[0] + ".mp3"

                # audio = AudioFileClip(audio_path)
                # audio.write_audiofile(mp3_path, codec='libmp3lame', bitrate='320k')


                # os.remove(audio_path)
                return [audio_path]
            else:
                return 'notFound'
    def playlist_download(self):

        yt = Playlist(self.youtube_url)

        download_folder = "download/downloaded_files"

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)


      
        if self.download_formet == 'video':
                for video in yt.videos:
                    ys = video.streams.get_highest_resolution()
                    ys.download(output_path=download_folder)

        elif self.download_formet == 'audio':
            for video in yt.videos:
                print(f"Downloading: {video.title}")

                # Download the audio file (usually in .mp4 or .m4a format)
                audio_stream = video.streams.get_audio_only()
                audio_file = audio_stream.download(output_path=download_folder)

                # Convert to MP3 using FFmpeg directly
                # mp3_filename = os.path.splitext(audio_file)[0] + ".mp3"
                # audio = AudioFileClip(audio_file)
                # audio.write_audiofile(mp3_filename, codec='libmp3lame', bitrate='320k')

                # # Remove original file after conversion
                # os.remove(audio_file)

                print(f"Saved as MP3: {audio_file}")
        
        # return download_folder
