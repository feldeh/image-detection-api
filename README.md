# Image Detection API

This is a program that leverages the Ultralytics YOLOv8 object detection model to accurately identify and locate objects within an image. It provides a user interface for uploading an image and obtaining an annotated version that highlights and classifies various objects.

## Features

- Image upload and processing
- Object detection using YOLOv8 model
- Annotates images with detected object classes, their bounding boxes and confidence scores using OpenCV (Open Source Computer Vision Library)

## Getting Started

### Prerequisites

- Docker

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/feldeh/image-detection-api
```

Navigate to the project's root directory:

```bash
cd image-detection-api
```

### Running the Application

To run the application, you need to spin up the Docker containers for both the server and the app:

```bash
docker-compose up
```

### App Usage

1.  Open your browser and navigate to `localhost:3000`.
2.  Upload an image.
3.  Wait a few seconds until the processed image appears on the screen with the detected objects annotated.

## API Reference

You can interact with the API endpoints using the Swagger UI documentation. The Swagger UI is automatically generated and can be accessed from the /docs endpoint.

#### Health check

```
  GET /
```

Returns "Ready" if the server is running.

#### Upload image

```
  POST /upload
```

| Form Field | Type   | Description                        |
| :--------- | :----- | :--------------------------------- |
| `file`     | `file` | **Required**. Image file to upload |

Upload an image file for processing. The image file should be in the form-data format with the key 'file'.

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework used to build the API.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Object detection model.
- [OpenCV](https://opencv.org/) - Used for image processing.

## Roadmap

- [x] Enhance the object detection API endpoint to return the processed image.
- [x] Integrate a front-end user interface to interactively use the API and visualize the results.
