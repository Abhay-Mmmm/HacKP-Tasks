pip install segmentation-models-pytorch opencv-python

# Task 5: Face Detection and Blurring with MediaPipe

This project demonstrates automatic face detection and selective blurring of faces in images using MediaPipe and a Jupyter notebook. The tool processes images to detect faces, applies Gaussian blur to the detected regions, and saves the results for further use.

## Overview
The notebook loads images from the `images/` folder, uses MediaPipe for face detection, and saves the processed images (with blurred faces) to the `processed/` folder. This is useful for privacy protection, anonymizing faces, or preparing datasets for research.

## How It Works
- Images are loaded from the `images/` folder.
- MediaPipe's Face Detection model is used to find faces in each image.
- For every detected face, the region is blurred using Gaussian blur, and the processed image is saved in the `processed/` folder with the same filename as the original.

## Features
- **Face Detection:** Automatically detects faces in images using MediaPipe.
- **Selective Blurring:** Applies Gaussian blur only to detected face regions.
- **Batch Processing:** Processes all images in the folder automatically.
- **Jupyter Notebook:** Interactive environment for running and modifying the workflow.

## Requirements
- Python 3.x
- Jupyter Notebook
- mediapipe
- opencv-python

Install dependencies:
```sh
pip install mediapipe opencv-python
```

## Setup
1. Place your input images in the `images/` folder.
2. Open `Model.ipynb` in Jupyter Notebook.
3. Run all cells to process and blur the images.

## Usage
- Run the notebook cells to detect and blur faces in each image.
- Processed images will be saved in the `processed/` folder with the same filenames.
- You can modify the notebook to change blur strength or detection parameters.

## Notes
- The quality of face detection and blurring depends on image clarity and MediaPipe's model.
- You can extend the notebook to handle multiple faces per image or add post-processing steps.
- For best results, use clear and high-resolution images.

## Credits
- Face detection: MediaPipe by Google.
- Sample images provided for demonstration purposes.

## License
This project is for educational and research use. Please ensure you have rights to use any additional images you add.
