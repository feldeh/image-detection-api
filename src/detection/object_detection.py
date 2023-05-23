from ultralytics import YOLO

def YOLOO():
    model = YOLO("yolov8n.pt")

    results = model.predict("../image/image.jpg")

    result = results[0]


    print(result.boxes)
    box = result.boxes[0]


    print("Object type:", box.cls)
    print("Coordinates:", box.xyxy)
    print("Probability:", box.conf)
    # print("Inference speed:", )

    return results
