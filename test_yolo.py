from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO('yolov8n.pt')

# Test it on an example image
results = model.predict(source='https://ultralytics.com/images/zidane.jpg', show=True)

print("✅ YOLO is set up and running!")
