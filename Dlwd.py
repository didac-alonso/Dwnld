import tkinter as tk
from tkinter import filedialog, messagebox
import pytubefix
from pytubefix import Playlist, YouTube

def download():
    url = entry_url.get()
    destination_path = filedialog.askdirectory()
    
    if not url or not destination_path:
        messagebox.showerror("Error", "Please provide a URL and choose a download location.")
        return
    
    try:
        if 'playlist' in url:
            p = Playlist(url)
            messagebox.showinfo("Download", f"Downloading {p.length} songs to {destination_path}")
            for song in p.videos:
                song.streams.get_audio_only().download(output_path=destination_path, filename=f"{song.title}.mp3")
                print(f'{song.title} downloaded')
        elif 'watch' in url:
            song = YouTube(url)
            song.streams.get_audio_only().download(output_path=destination_path, filename=f"{song.title}.mp3")
            print(f'{song.title} downloaded')
        else:
            messagebox.showerror("Error", "Invalid URL. Please provide a valid YouTube playlist or video URL.")
        
        messagebox.showinfo("Download", "Download completed")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Tkinter setup
root = tk.Tk()
root.title("YouTube Downloader")

# Entry for the URL
tk.Label(root, text="YouTube URL:").pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Download button
tk.Button(root, text="Download", command=download).pack(pady=10)

root.mainloop()
