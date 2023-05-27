from fastapi import FastAPI, status

from .detection.detect_objects import detect_objects

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return "Ready"


@app.get("/api", status_code=status.HTTP_200_OK)
async def objects_get():
    result = detect_objects()
    return result
