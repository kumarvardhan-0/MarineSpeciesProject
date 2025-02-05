from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("runs/detect/train/weights/best.pt")

# Open a video file or webcam (0 for webcam)
cap = cv2.VideoCapture("C:\MarineSpeciesProject\data\Fish_video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLO inference
    results = model(frame)

    # Show results
    for r in results:
        frame = r.plot()  # Draws bounding boxes

    cv2.imshow("YOLO Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
