from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from src.routes import upload

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return "Ready"

app.include_router(upload.router)
