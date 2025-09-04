import json
import cv2
import pytesseract
import exiftool

exiftool_path = r"C:\Users\Abhay\OneDrive\Desktop\HacKP-Tasks\task1_image_metadata_analysis\exiftool.exe"
image_path = r"C:\Users\Abhay\OneDrive\Desktop\HacKP-Tasks\task1_image_metadata_analysis\dataset\5.jpg"

# --- METADATA EXTRACTION ---
with exiftool.ExifTool(exiftool_path) as et:
    metadata_json = et.execute("-json", image_path)

if metadata_json.strip():
    try:
        metadata = json.loads(metadata_json)[0]
        print("\n=== METADATA INFO ===")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    except Exception as e:
        print("Error parsing metadata:", e)
        print("Raw output:", metadata_json)
else:
    print("\n=== METADATA INFO ===")
    print("No metadata found for this image.")
