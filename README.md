# YouTube Downloader

## Introduction
The YouTube Downloader is a simple GUI application built in Python that allows users to download videos from YouTube. It utilizes the `pytube` library to interact with YouTube's API and download videos.

## Features
- Input a YouTube video URL.
- Fetch video information such as title, cover image, available resolutions, and sizes.
- Select the desired resolution to download.
- Download the selected video.

## Installation
To run the YouTube Downloader, you need Python installed on your system along with the following dependencies:
- `pytube`: Used to interact with YouTube's API and download videos.
- `PIL`: Required for image processing and display.
- `requests`: Used to fetch thumbnail images.
- `certifi`: Provides Mozilla's SSL certificates for secure connections.

You can install these dependencies using pip:
pip install pytube pillow requests certifi
or
pip install -r requirements.txt


## Usage
1. Run the program by executing the Python script.
2. Enter the URL of the YouTube video you want to download.
3. Click the "Fetch Info" button to fetch video information.
4. Once the information is loaded, select the desired resolution from the dropdown menu.
5. Click the "Download Selected" button to start the download process.
6. The download progress will be displayed, and upon completion, a success message will appear.

## Documentation
### Functions
1. `start_download()`: Fetches video information, including title, cover image, available resolutions, and sizes. Displays the fetched information in the GUI.
2. `download_selected()`: Downloads the selected video with the chosen resolution.
3. `format_size(size_in_bytes)`: Formats the size of the video file from bytes to a human-readable format.

### Widgets
1. `title_label`: Displays the title of the YouTube video.
2. `link`: Entry widget to input the YouTube video URL.
3. `fetch_button`: Button to fetch video information.
4. `cover_image_label`: Label to display the cover image of the video.
5. `resolution_combo`: Dropdown box to select the video resolution.
6. `download_selected_button`: Button to initiate the download process.

## Limitations
1. The application relies on the `pytube` library, which may be subject to changes or limitations imposed by YouTube's API.
2. The video quality options may vary depending on the availability and encoding of the video on YouTube.

## Conclusion
The YouTube Downloader provides a convenient way to download YouTube videos with customizable resolution options. It simplifies the downloading process and offers a user-friendly interface for users to interact with.


