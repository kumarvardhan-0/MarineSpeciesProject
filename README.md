# Marine Species Detection with YOLOv8

This project uses YOLOv8 (You Only Look Once) for detecting and counting marine species in images and videos.

## Dataset
The dataset consists of images of various marine species, annotated with bounding boxes collected from Kaggle (sea-animals-image-dataset). You can use datasets like this or create your own.

## Technologies Used
- **YOLOv8**: For real-time object detection.
- **Python**: Programming language.
- **PyTorch**: Deep learning framework.
- **OpenCV**: For image and video processing.

## Setup Instructions
1. Clone the repository
   
2. Create and activate a virtual environment:

       python -m venv venv


       .\venv\Scripts\activate  # Windows


        source venv/bin/activate  # Mac/Linux


3. Training
   Train the model with:

       python train.py --data data.yaml --cfg yolov8.yaml --weights yolov8n.pt --epochs 3 --img-size 416


4.Testing:


    python detect.py --weights runs/train/exp/weights/best.pt --img-size 416 --source data/test/image.jpg

  To test the model on a video:

    python detect.py --weights runs/train/exp/weights/best.pt --img-size 416 --source data/test/v
