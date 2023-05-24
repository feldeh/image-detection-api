# Image Detection using YOLO and FastAPI

This project aims to provide a REST API server for detecting objects in an image using the YOLOv8 (You Only Look Once) algorithm implemented by Ultralytics. It uses a pre-trained model to recognize objects in images, then outputs the object type, its coordinates and confidence score.

## Getting Started

### Prerequisites

- Docker

### Installing

Clone the repository to your local machine.

```bash
git clone https://github.com/feldeh/image-detection-api
```

Navigate to the project's root directory.

```bash
cd image-detection-api
```

Build and start the docker container.

```bash
docker-compose up
```

### API Usage

The FastAPI server is exposed at port 80. You can interact with it using the following endpoints:

- **/** - Health check. Returns "Ready" if the server is running.
- **/api** - Runs the detection function and returns the result.

### Detection Result

The detection function returns a list of detected objects in the image. Each object contains:

- Object type: class of the detected object.
- Coordinates: the bounding box coordinates of the detected object.
- Confidence: the model's confidence score for the detected object.

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework used to build the API.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Object detection model.
- [OpenCV](https://opencv.org/) - Used for image processing.
