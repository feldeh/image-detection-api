from fastapi import FastAPI, status, UploadFile, File
from src.routes import upload

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return "Ready"

app.include_router(upload.router)
