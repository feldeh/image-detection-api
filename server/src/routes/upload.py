from fastapi import APIRouter, UploadFile, File, Response
from src.utils.detection import process_image
from PIL import Image
import io


IMAGEDIR = "src/images/uploaded/"

router = APIRouter()


@router.post("/upload")
async def upload_file(file: bytes = File(...)):

    image = Image.open(io.BytesIO(file))
    image.save("img.jpg")

    processed_image_array = process_image(image)
    processed_image = Image.fromarray(processed_image_array)

    processed_image_stream = io.BytesIO()
    processed_image.save(processed_image_stream, format="JPEG")

    return Response(content=processed_image_stream.getvalue(), media_type="image/jpeg")
