"""
Fetch YOLO weights for AeroVision brand detection model.
This script downloads the pre-trained model weights from your storage.
"""

import os
import urllib.request
from pathlib import Path

MODEL_URL = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
MODEL_PATH = "best.pt"

def download_weights():
    """Download YOLO model weights if not present."""
    if os.path.exists(MODEL_PATH):
        print(f"✅ Model weights already exist at {MODEL_PATH}")
        return
    
    print(f"📥 Downloading model weights from {MODEL_URL}...")
    try:
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print(f"✅ Model weights downloaded successfully to {MODEL_PATH}")
    except Exception as e:
        print(f"❌ Error downloading model weights: {e}")
        print("Please manually download your trained model and save as 'best.pt'")

if __name__ == "__main__":
    download_weights()
