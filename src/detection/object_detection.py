from ultralytics import YOLO


def detection():
    model = YOLO("yolov8n.pt")

    results = model.predict("src/image/image.jpg")

    result = results[0]

    bboxes = []

    for box in result.boxes:
        class_name = result.names[box.cls[0].item()]
        coordinates = box.xyxy[0].tolist()
        coordinates = [round(x) for x in coordinates]
        confidence = round(box.conf[0].item(), 2)

        print("Object type:", class_name)
        print("Coordinates:", coordinates)
        print("Confidence:", confidence)
        print("___")

        dic = {
            "Object type": class_name,
            "Coordinates": coordinates,
            "Confidence": confidence
        }
        bboxes.append(dic)

    return bboxes
