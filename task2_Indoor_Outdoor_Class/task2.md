# Indoor/Outdoor Scene Classification Tool

A Python-based tool for classifying images as indoor or outdoor scenes using a pretrained AlexNet model (Places365). It also predicts the most probable scene category for each image.

## Overview
This project uses deep learning and the Places365 dataset to automatically classify images. It is useful for scene understanding, image organization, and computer vision research.

## Features
- **Indoor/Outdoor Classification:** Uses IO mapping from Places365 to label images as indoor or outdoor.
- **Scene Category Prediction:** Identifies the most likely scene category (e.g., kitchen, park, etc.) for each image.
- **Pretrained Model:** Utilizes AlexNet trained on Places365 for robust predictions.
- **Easy to Use:** Simple function call for single image classification.

## Requirements
- Python 3.x
- PyTorch
- Torchvision
- NumPy
- PIL (Pillow)
- Places365 model weights and mapping files:
  - `alexnet_places365.pth.tar` (download from Places365 website)
  - `IO_places365.txt` (indoor/outdoor mapping)
  - `categories_places365.txt` (scene categories)

Install dependencies:
```sh
pip install torch torchvision numpy pillow
```

## Setup
1. Download the Places365 model weights and mapping files and place them in your project directory.
2. Update the image path in the notebook or script to point to your test image.

## Usage
- Open the notebook `Model.ipynb`.
- Run the cells to import packages, load mappings, and initialize the model.
- Use the `classify_scene_single(img_path)` function to classify your image.
- Example:
  ```python
  img_path = 'trial/outdoor_1.jpg'
  scene, confidence, io_label = classify_scene_single(img_path)
  print(f"Prediction: {scene}")
  print(f"Confidence: {confidence:.2f}%")
  print(f"Indoor/Outdoor: {io_label}")
  ```

## Notes
- The tool supports any image compatible with PIL.
- You can test with sample images like `indoor_1.jpg`, `indoor_2.jpg`, `outdoor_1.jpg`, and `outdoor_2.jpg`.
- For batch processing, extend the function to loop over multiple images.

## Credits
- Model and dataset: [Places365](http://places2.csail.mit.edu/)
- Pretrained AlexNet: [PyTorch Hub](https://pytorch.org/hub/)

## License
This project is for educational and research purposes. See Places365 and PyTorch for respective licenses.
