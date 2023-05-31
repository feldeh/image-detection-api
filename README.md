# Image Detection API

Image Detection API is a FastAPI based application that enables users to upload images and performs object detection on the uploaded images. The application uses the Ultralytics YOLOv8 model for object detection.

## Features

- Image upload and processing
- Object detection using YOLOv8 model
- Annotates images with detected object classes, their bounding boxes and confidence scores using OpenCV (Open Source Computer Vision Library)

## Getting Started

### Prerequisites

- Docker
- Python

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
| `image`    | `file` | **Required**. Image file to upload |

Upload an image file for processing. The image file should be in the form-data format with the key 'image'. After uploading, the image will be processed and a new image with detected object classes, their bounding boxes and their confidence scores will be written in the annotated folder. The endpoint returns the name of the processed image file.

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework used to build the API.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Object detection model.
- [OpenCV](https://opencv.org/) - Used for image processing.

## Roadmap

- [ ] Enhance the object detection API endpoint to return the processed image.
- [ ] Integrate a front-end user interface to interactively use the API and visualize the results.
