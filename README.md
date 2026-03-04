# Object Detection using YOLO on Raspberry Pi 

This project runs real-time object detection on a **Raspberry Pi** using a **YOLO model** and a connected **webcam**. The script loads a local YOLO model file, opens the camera feed, performs detection frame by frame, and displays the annotated results in a live window.

The current implementation:
- loads the local model file `yolo26n.pt`
- opens the default camera with OpenCV
- runs inference at `imgsz=320`
- draws detections on each frame
- shows the live annotated result until you press `q` 

## Project Overview

This setup is useful for:
- basic real-time object detection on edge devices
- Raspberry Pi computer vision experiments
- lightweight offline AI inference with a local YOLO model
- webcam-based detection demos and prototypes

## Project Structure

```text
project-folder/
├── detect.py        # Main Python script
├── yolo26n.pt       # YOLO model weights
└── README.md        # Project documentation
```

## How It Works

The script follows this flow:

1. Import **Ultralytics YOLO** and **OpenCV**.
2. Load the YOLO model from `yolo26n.pt`.
3. Start the webcam using `cv2.VideoCapture(0)`.
4. Read frames continuously.
5. Run object detection on each frame.
6. Draw the detection results on the frame.
7. Display the live output window.
8. Exit when `q` is pressed. fileciteturn1file0L1-L2 fileciteturn1file0L5-L5 fileciteturn1file0L8-L8 fileciteturn1file0L14-L31

## Requirements

You will need:
- Raspberry Pi
- Raspberry Pi OS
- Python 3
- USB webcam or compatible camera
- `ultralytics`
- `opencv-python`

## Installation

Create a virtual environment if you want an isolated setup:

```bash
python3 -m venv yolo_object
source yolo_object/bin/activate
```

Install the required packages:

```bash
pip install ultralytics opencv-python
```

If OpenCV GUI support gives issues on Raspberry Pi, you may also need system OpenCV or desktop packages depending on your OS image.

## Running the Project

Make sure these files are in the same folder:
- `detect.py`
- `yolo26n.pt`

Then run:

```bash
python3 detect.py
```

A webcam window titled **YOLO26 Offline Webcam** should open and show live detections. The display window name is defined directly in the script. 
Press:

```text
q
```

to stop the program safely. fileciteturn1file0L27-L28

## Main Script

Your script is:

```python
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
    results = model(frame, imgsz=320)

    # Draw results
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO26 Offline Webcam", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

This matches the uploaded project script. fileciteturn1file0L1-L31

## Notes

- The model file must be present in the same directory as the script unless you change the path in `YOLO("yolo26n.pt")`.
- The script uses camera index `0`, which usually means the default webcam.
- Detection image size is set to `320`, which helps reduce processing load on Raspberry Pi hardware. fileciteturn1file0L5-L5 fileciteturn1file0L8-L8 fileciteturn1file0L20-L20

## Troubleshooting

### Camera not detected
If you see:

```text
Camera not detected
```

then OpenCV could not open the webcam. Check that:
- the camera is properly connected
- the correct camera index is being used
- no other application is using the camera
- your Raspberry Pi has permission to access the device fileciteturn1file0L10-L12

### Model file not found
Make sure `yolo26n.pt` exists in the same folder as `detect.py`, or update the model path in the code.

### Slow performance
On Raspberry Pi, performance depends on:
- model size
- input resolution
- camera resolution
- CPU load
- whether hardware acceleration is available

Reducing inference size or using a lighter exported model can improve speed.

## Possible Improvements

You can extend this project by adding:
- custom classes only filtering
- confidence threshold control
- FPS counter
- saving output video
- support for Raspberry Pi Camera Module
- full-screen display mode
- optimized exported model formats for faster inference

## Use Cases

This project can be adapted for:
- smart surveillance
- robot vision
- classroom AI demos
- smart home monitoring
- object counting prototypes
- embedded computer vision research

## License

You can add your preferred license here, for example MIT.

## Author

@Oluwatunmise116
