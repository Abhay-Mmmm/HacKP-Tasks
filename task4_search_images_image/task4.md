# Task 4: Image-to-Image Search Tool

This project demonstrates an image-to-image search system using a collection of sample images and a Jupyter notebook. The tool allows you to find visually similar images from a dataset by providing a query image.

## Overview
The notebook loads all images from the `images/` folder, encodes them, and enables searching for similar images using a reference image. This is useful for visual search, image organization, and exploring relationships between images.

## How It Works
- All images in the `images/` folder are loaded and preprocessed.
- Each image is encoded into a feature vector using a deep learning model (such as CLIP or a CNN).
- To search, you provide a query image; the system computes its feature vector and compares it to all dataset images using cosine similarity.
- The most visually similar image(s) are retrieved and displayed.

## Features
- **Image-to-Image Search:** Find similar images by providing a reference image.
- **Visual Similarity:** Uses deep learning features for robust matching.
- **Interactive Notebook:** Search and view results directly in Jupyter Notebook.
- **Sample Dataset:** Includes a variety of images (animals, objects, nature, people, etc.) for experimentation.

## Requirements
- Python 3.x
- Jupyter Notebook
- torch
- pillow
- matplotlib
- (Optional) openai-clip or other deep learning library for feature extraction

Install dependencies:
```sh
pip install torch pillow matplotlib
# For CLIP-based models:
pip install git+https://github.com/openai/CLIP.git
```

## Setup
1. Place your images in the `images/` folder.
2. Open `model.ipynb` in Jupyter Notebook.
3. Run all cells to load the model, encode images, and perform searches.

## Usage
- Run the notebook cells to initialize the model and encode images.
- Provide a query image (e.g., `apple.jpg`, `car.jpg`, `family.jpg`).
- The notebook will display the most visually similar image(s) from the dataset.
- You can experiment with different query images to explore the dataset.

## Notes
- The search uses deep learning features, so results are based on visual similarity, not filenames.
- You can extend the notebook to show top-k results or batch process queries.
- For best results, use clear and high-quality images as queries.

## Credits
- Sample images provided for demonstration purposes.
- Feature extraction model: CLIP or other CNN-based models.

## License
This project is for educational and research use. Please ensure you have rights to use any additional images you add.
