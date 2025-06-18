import cv2 
from ultralytics import YOLO 
import time

model = YOLO('yolov8n.pt') 
cap = cv2.VideoCapture(0)  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    success, frame = cap.read()
    
    if success:
        results = model(frame)        
        annotated_frame = results[0].plot()
        cv2.imshow("Real-time Object Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()