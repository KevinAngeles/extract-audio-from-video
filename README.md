# Video to Audio Extractor

A simple command-line tool to extract audio from video files and save them as MP3 using FFmpeg.

## Supported Input Formats

This tool works with any video format supported by FFmpeg, including but not limited to:
- AVI
- MP4
- MKV
- MOV
- WMV
- FLV
- And many more...

## Requirements

- Python 3.6 or higher
- FFmpeg installed on your system

### Installing FFmpeg

**Windows:**
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Add FFmpeg to your system PATH

**Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

## Usage

1. Run the script:
   ```bash
   python video_to_mp3_extractor.py
   ```

2. Follow the on-screen prompts to:
   - Enter the path to your video file
   - Choose between:
     - Extracting the full video as MP3
     - Extracting a specific portion by entering start and end times
   - Choose an output filename (optional)

3. The extracted MP3 will be saved in the same directory as the script.

## Features

- Extract full video audio or specific portions with millisecond accuracy
- Simple command-line interface
- No external Python dependencies required
- Works with any video format supported by FFmpeg

## Notes

- The extracted audio will be saved in MP3 format with the best quality settings.
- If you encounter any issues, make sure FFmpeg is properly installed and added to your system PATH.
- This software is provided "as is" without any warranties. The author is not responsible for any damages or issues that may arise from its use.

## Author
- Kevin Angeles [https://www.kevinangeles.com](https://www.kevinangeles.com)

## License
- MIT License
