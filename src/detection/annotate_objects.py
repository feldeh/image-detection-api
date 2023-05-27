from ultralytics import YOLO
import cv2 as cv
import numpy as np


def annotate_objects():
    model = YOLO("yolov8m.pt")

    img = cv.imread("../image/image.jpg")

    results = model.predict("../image/image.jpg")
    result = results[0]

    classes = np.array(result.boxes.cls, dtype="int")
    class_names = np.array([x.upper() for x in list(result.names.values())])


    bboxes = np.array(result.boxes.xyxy, dtype="int")
    confidences = np.array(result.boxes.conf, dtype="float")
    rounded_confs = np.round(confidences, 2)

    for cls, bbox, conf in zip(classes, bboxes, rounded_confs):

        (x, y, x2, y2) = bbox
        cv.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
        cv.putText(img, str(class_names[cls]), (x, y - 5), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        cv.putText(img, str(conf), (x2 - 30, y - 5), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)


    cv.imwrite('bboxed_img.jpg', img)