from ultralytics import YOLO
import cv2 as cv
import numpy as np
import uuid

import os

ANNOTATEDDIR = "src/images/annotated/"

def process_image(image_path):

    model = YOLO("src/models/yolov8m.pt")

    results = model.predict(image_path)
    result = results[0]

    img = cv.imread(image_path)


    classes = np.array(result.boxes.cls, dtype="int")
    class_names = np.array(list(result.names.values()))


    bboxes = np.array(result.boxes.xyxy, dtype="int")
    confidences = np.array(result.boxes.conf, dtype="float")
    rounded_confs = np.round(confidences, 2)

    for cls, bbox, conf in zip(classes, bboxes, rounded_confs):

        (x, y, x2, y2) = bbox
        cv.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
        cv.putText(img, str(class_names[cls]), (x, y - 5), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        cv.putText(img, str(conf), (x2 - 30, y - 5), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)


    annotated_filename = f"{uuid.uuid4()}.jpg"
    annotated_path = os.path.join(ANNOTATEDDIR, annotated_filename)
    cv.imwrite(annotated_path, img)
    return annotated_filename