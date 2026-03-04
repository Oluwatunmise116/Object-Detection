from ultralytics import YOLO
import cv2

# Load model from local file
model = YOLO("yolo26n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame,imgsz=320)

    # Draw results
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO26 Offline Webcam", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
