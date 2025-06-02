import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # YOLOv5 small

img_path = 'sample.jpg'  # Replace with your image file
img = cv2.imread(img_path)
results = model(img)

results.print()
results.show()