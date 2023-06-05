from fastapi import APIRouter, File, Response
from src.utils.detection import process_image
from PIL import Image
import io
import uuid


IMAGEDIR = "src/images/uploaded/"

router = APIRouter()


@router.post("/upload")
async def upload_file(file: bytes = File(...)):

    image = Image.open(io.BytesIO(file))
    image_rgb = image.convert("RGB")
    image_format = image.format.lower()

    filename = f"{uuid.uuid4()}.{image_format}"

    image_rgb.save(f"{IMAGEDIR}{filename}")

    processed_image_array = process_image(image_rgb)
    processed_image = Image.fromarray(processed_image_array)

    processed_image_stream = io.BytesIO()
    processed_image.save(processed_image_stream, format=f"{image_format}")

    return Response(content=processed_image_stream.getvalue(), media_type=f"image/{image_format}")
