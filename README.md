# AI Object Detector
This project uses **OpenCV** and a YOLOv8 model to detect objects through your camera in real-time scenerio

## Features
- Real-time camera access
- Object detection using YOLOv8
- Cross-platform (macOS, Windows, Linux)

## Requirements
- Python 3.8+
- OpenCV
- `ultralytics` or any library you're using for YOLO

## Project Structure
- ai_object_detector/
- camera_test.py
- detection.py
- yolov8n.pt
- venv/
- .gitignore

## Installation
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install opencv-python
pip install ultralytics
```
License: MIT License
