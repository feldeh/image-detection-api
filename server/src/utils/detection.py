from ultralytics import YOLO
import cv2 as cv
import numpy as np
import uuid
import os

ANNOTATEDDIR = "src/images/annotated/"


def process_image(image):

    model = YOLO("src/weights/yolov8m.pt")

    results = model.predict(image)
    result = results[0]

    image_array = np.array(image)

    classes = np.array(result.boxes.cls, dtype="int")
    class_names = np.array(list(result.names.values()))
    bboxes = np.array(result.boxes.xyxy, dtype="int")
    confidences = np.array(result.boxes.conf, dtype="float")
    rounded_confs = np.round(confidences, 2)

    for cls, bbox, conf in zip(classes, bboxes, rounded_confs):

        (x, y, x2, y2) = bbox
        cv.rectangle(image_array, (x, y), (x2, y2), (0, 0, 255), 4)
        cv.putText(image_array, str(class_names[cls]).capitalize(), (x, y - 15),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv.putText(image_array, str(conf), (x + 115, y - 15),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    return image_array
