
# Image Metadata Extraction Tool

A Python command-line tool to extract and display all embedded metadata from an image file using ExifTool by Phil Harvey.

## Overview

This tool is useful for digital forensics, photography analysis, or simply inspecting image properties. It extracts a wide variety of metadata tags and prints them in a clean, readable key-value format.

## Features

- **Comprehensive Metadata Extraction:** Uses ExifTool, the industry standard, to extract all available metadata.
- **Clean Output:** Prints metadata in an easy-to-read key: value format.
- **Error Handling:** Alerts the user in case of parsing issues or missing metadata.
- **Graceful Fallback:** Notifies the user if no metadata is found.

## Requirements

- Python 3.x
- ExifTool Executable (Download the correct version for your OS from the [ExifTool Official Site](https://exiftool.org/))
- Python Libraries:
	- `pyexiftool` (Python wrapper for ExifTool)
	- `opencv-python` & `pytesseract` (used for OCR attempts, see below)

Install dependencies:

```sh
pip install pyexiftool opencv-python pytesseract
```

## Setup

1. Install dependencies (Python packages + ExifTool executable).
2. Configure the script: Open `Metadata.py` and update the paths:

```python
# --- CONFIG ---
exiftool_path = r"C:\path\to\your\exiftool.exe"
image_path = r"C:\path\to\your\image.jpg"
```

## Usage

Open a terminal or command prompt, navigate to the folder containing `Metadata.py`, and run:

```sh
python Metadata.py
```

The script will print all available metadata for the image to the console.

## OCR Attempt (Why It Wasn't Included)

During development, OpenCV (`cv2`) and Tesseract (`pytesseract`) were imported to extract visible text from images. However, this feature was abandoned because the extracted words and text were often inconsistent, unreliable, and did not make sense in context. The current version focuses solely on robust metadata extraction.