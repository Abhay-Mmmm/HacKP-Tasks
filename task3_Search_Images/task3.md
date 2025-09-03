
# CLIP-Based Semantic Image Search Tool

This project demonstrates semantic image search using OpenAI's CLIP model in a Jupyter notebook. Users can search for images in the `images/` folder using natural language queries, and the tool retrieves the most relevant image based on visual and textual similarity.

## Overview
The notebook loads a set of sample images, encodes them using CLIP, and allows users to input a search query (e.g., "beach", "family", "dog", "mountain"). The tool finds and displays the image most semantically similar to the query.

## Features
- **Semantic Search:** Find images using natural language queries, not just filenames.
- **CLIP Model:** Uses OpenAI's CLIP (ViT-B/32) for robust image-text matching.
- **Interactive Notebook:** Search and view results directly in Jupyter Notebook.
- **Sample Dataset:** Includes a variety of images (animals, people, sports, nature, etc.) for experimentation.

## Requirements
- Python 3.x
- Jupyter Notebook
- torch
- openai-clip
- pillow
- matplotlib

Install dependencies:
```sh
pip install torch pillow matplotlib git+https://github.com/openai/CLIP.git
```

## Setup
1. Place your images in the `images/` folder.
2. Open `model.ipynb` in Jupyter Notebook.
3. Run all cells to load the model, encode images, and perform searches.

## Usage
- Run the notebook cells to initialize the model and encode images.
- Enter a search query when prompted (e.g., "Search: beach").
- The notebook will display the most relevant image and its filename.

## Notes
- The search uses CLIP's semantic similarity, so queries can be descriptive (e.g., "a person playing football", "a mountain landscape").
- You can extend the notebook to show top-k results or batch process queries.
- For best results, use clear and descriptive queries.

## Credits
- CLIP model: [OpenAI CLIP](https://github.com/openai/CLIP)
- Sample images provided for demonstration purposes.

## License
This project is for educational and research use. Please ensure you have rights to use any additional images you add.
