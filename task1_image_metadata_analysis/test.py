import json
import exiftool
import os

# Absolute path to your exiftool.exe
exiftool_path = r"C:\Users\Abhay\OneDrive\Desktop\HacKP-Tasks\task1_image_metadata_analysis\exiftool.exe"
image_path = os.path.join("dataset", "2.jpg")

with exiftool.ExifTool(exiftool_path) as et:
    metadata_json = et.execute("-json", image_path)

    # If it's bytes, decode. If it's str, keep it.
    if isinstance(metadata_json, bytes):
        metadata_json = metadata_json.decode("utf-8")

    metadata = json.loads(metadata_json)[0]  # list with one dict

    for tag, value in metadata.items():
        print(f"{tag}: {value}")
