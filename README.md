# Video Format Converter

A modern Python application for converting videos from one format to another with ease. The application features a user-friendly graphical interface built using `tkinter` and `ttkthemes`.

## Features

- Convert videos between multiple formats, including:
  - MP4
  - AVI
  - MOV
  - MKV
  - WMV
  - FLV
  - WEBM
  - GIF
- Clean and modern UI with dropdown menus for selecting input and output formats.
- File dialogs for selecting input files and saving converted videos.
- Efficient and fast video processing using `moviepy`.

## Prerequisites

Before running the application, ensure the following prerequisites are met:

- **Python 3.x**: Download from [Python Official Website](https://www.python.org/downloads/)
- **Required Libraries**:
  - `moviepy`: For video processing and format conversion.
  - `ttkthemes`: For a modern and clean user interface.
  - `tkinter`: Included with Python by default.

### Install Required Libraries

Run the following command to install the required libraries:

```bash
pip install moviepy ttkthemes
```

## How to Use

1. **Run the Application**:
   - Open a terminal or command prompt and navigate to the directory containing the Python script.
   - Run the script using:
     ```bash
     python video_converter.py
     ```

2. **Select Input Video**:
   - Use the "Select Input Video" button to browse and choose the video you want to convert.

3. **Choose Output Format**:
   - Select the desired output format from the dropdown menu.

4. **Save Converted Video**:
   - Use the "Save As" button to specify the name and location for the converted video.

5. **Convert**:
   - Click the "Convert" button to start the conversion process.
   - A success message will be displayed when the conversion is complete.

## Supported Video Formats

- MP4
- AVI
- MOV
- MKV
- WMV
- FLV
- WEBM
- GIF
- 
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MoviePy Documentation](https://zulko.github.io/moviepy/)
- [ttkthemes Documentation](https://ttkthemes.readthedocs.io/)
- Icons and design inspirations from modern UI practices.
