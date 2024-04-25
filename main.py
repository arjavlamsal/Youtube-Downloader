import tkinter
import customtkinter
from pytube import YouTube, exceptions
import ssl
import certifi
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import requests  # Import the requests module for fetching the thumbnail image

# Set the default SSL context to use certifi certificates
ssl._create_default_https_context = ssl._create_unverified_context

def start_download():
    try:
        # Get the YouTube URL from the input box
        yt_link = link.get().strip()
        if not yt_link:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        # Create a YouTube object
        yt_object = YouTube(yt_link)

        # Extract video title
        video_title = yt_object.title
        title_label.configure(text=f"Video Title: {video_title}")

        # Load and display video cover image
        cover_image_url = yt_object.thumbnail_url
        cover_image = Image.open(requests.get(cover_image_url, stream=True).raw)
        cover_image.thumbnail((500, 500))
        cover_image = ImageTk.PhotoImage(cover_image)
        cover_image_label.configure(image=cover_image)
        cover_image_label.image = cover_image  # Keep a reference

        # Get available streams
        streams = yt_object.streams.filter(progressive=True, file_extension='mp4').all()

        if not streams:
            messagebox.showerror("Error", "No suitable streams found for download.")
            return

        # Create a list of available streams with resolution and size information
        stream_info = [f"{stream.resolution} ({format_size(stream.filesize)})" for stream in streams]

        # Update the dropdown box with available streams and sizes
        resolution_combo.configure(values=["Choose Video Resolution"] + stream_info)  # Set default value

        # Display available streams and sizes
        for i, stream in enumerate(streams):
            print(f"{i+1}. Resolution: {stream.resolution}, Size: {format_size(stream.filesize)}")

    except exceptions.RegexMatchError:
        messagebox.showerror("Error", "Invalid YouTube URL.")
    except exceptions.VideoUnavailable:
        messagebox.showerror("Error", "Video is unavailable.")
    except Exception as e:
        messagebox.showerror("Error", f"Download Failed: {e}")

def download_selected():
    try:
        # Get the selected stream from the dropdown box
        selected_stream_info = resolution_combo.get()
        selected_resolution = selected_stream_info.split(' (')[0]

        # Get the YouTube URL from the input box
        yt_link = link.get().strip()
        if not yt_link:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        # Create a YouTube object
        yt_object = YouTube(yt_link)

        # Get the selected stream based on the resolution
        selected_stream = yt_object.streams.filter(progressive=True, resolution=selected_resolution, file_extension='mp4').first()

        # Download the selected stream
        selected_stream.download()
        messagebox.showinfo("Success", "Download Complete!")

    except exceptions.RegexMatchError:
        messagebox.showerror("Error", "Invalid YouTube URL.")
    except exceptions.VideoUnavailable:
        messagebox.showerror("Error", "Video is unavailable.")
    except Exception as e:
        messagebox.showerror("Error", f"Download Failed: {e}")

def format_size(size_in_bytes):
    # Convert size from bytes to appropriate unit (KB, MB, GB)
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"
    elif size_in_bytes < 1024 ** 2:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024 ** 3:
        return f"{size_in_bytes / (1024 ** 2):.2f} MB"
    else:
        return f"{size_in_bytes / (1024 ** 3):.2f} GB"

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.title("YouTube Downloader")

# Adding UI elements
title_label = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title_label.pack(padx=10, pady=5)

# Link input box
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=5)

# Download button
fetch_button = customtkinter.CTkButton(app, text="Fetch Info", command=start_download)
fetch_button.pack(padx=10, pady=5)

# Video title display
title_label = customtkinter.CTkLabel(app, text="")
title_label.pack(padx=10, pady=5)

# Cover image display
cover_image_label = tkinter.Label(app)
cover_image_label.pack(padx=10, pady=5)

# Dropdown box for resolutions and sizes
resolution_combo = ttk.Combobox(app, width=50)
resolution_combo.pack(padx=10, pady=5)
resolution_combo.set("Choose Video Resolution")  # Set default value

# Download selected button
download_selected_button = customtkinter.CTkButton(app, text="Download Selected", command=download_selected)
download_selected_button.pack(padx=10, pady=5)

app.mainloop()
