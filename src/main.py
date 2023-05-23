from fastapi import FastAPI, status

from detection.object_detection import YOLOO

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return "Ready"

@app.get("/api", status_code=status.HTTP_200_OK)
async def YOLOO_get():
    result = YOLOO()

    return result