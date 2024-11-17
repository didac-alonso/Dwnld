import pytubefix
from pytubefix import Playlist, Youtube
import argparse

parser = argparse.ArgumentParser(description='Download Path and Playlist URL')

parser.add_argument('--path', type=str, help='Path to save the playlist')
parser.add_argument('--url', type=str, help='URL of the playlist')

args = parser.parse_args()

destination_path = args.path
url = args.url

if 'playlist' in url:
    p = Playlist(url)
    print(f'Downloading {p.length} songs to {destination_path}')

    for song in p.videos:
        print(f'Downloading {song.title}')
        song.streams.get_audio_only().download(output_path=destination_path, filename=f"{song.title}.mp3")
        print(f'{song.title} downloaded')
elif 'watch' in url:
    song = Youtube(url)
    print(f'Downloading {song.title}')
    song.streams.get_audio_only().download(output_path=destination_path, filename=f"{song.title}.mp3")
    print(f'{song.title} downloaded')
else:
    print("Invalid URL. Please provide a valid YouTube playlist or video URL.")
    

print('Download completed')