import cv2
import sys
import time
import platform

print("\n===== CAMERA TEST DIAGNOSTIC =====")
print(f"Python version: {sys.version}")
print(f"OpenCV version: {cv2.__version__}")
print(f"Platform: {platform.system()} {platform.release()}")
print("==================================\n")

print("Attempting to open camera...")

for camera_index in [0, 1]:
    try:
        print(f"Trying camera index: {camera_index}")
        cap = cv2.VideoCapture(camera_index)
        time.sleep(2)  
        
        if not cap.isOpened():
            print(f"  Failed to open camera with index {camera_index}")
            cap.release()
            continue
            
        print(f"  SUCCESS: Camera {camera_index} opened!")
        print("  Attempting to read a frame...")
        ret, frame = cap.read()
        
        if not ret or frame is None:
            print("  ERROR: Could not read frame from camera!")
            cap.release()
            continue
            
        print("  SUCCESS: Frame captured!")
        
        height, width = frame.shape[:2]
        print(f"  Frame dimensions: {width}x{height}")
        
        filename = f"test_camera_{camera_index}.jpg"
        print(f"  Saving image as {filename}...")
        cv2.imwrite(filename, frame)
        print(f"  Image saved as {filename}")
        
        cap.release()
        print(f"  Camera {camera_index} released")
        print(f"  SUCCESS with camera index {camera_index}")
        
        break
        
    except Exception as e:
        print(f"  Error with camera {camera_index}: {str(e)}")
        try:
            cap.release()
        except:
            pass

print("\n===== TEST COMPLETE =====")