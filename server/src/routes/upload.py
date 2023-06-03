from fastapi import APIRouter, UploadFile, File
from src.utils.detection import process_image
import uuid
import traceback

import os
import io

from PIL import Image


IMAGEDIR = "src/images/uploaded/"

router = APIRouter()


@router.post("/upload")
async def upload_file(image: bytes = File(...)):

    image_stream = io.BytesIO(image)

    print(image_stream.getvalue())

    # try:

    #     image.filename = f"{uuid.uuid4()}.jpg"
    #     contents = await image_stream.read()
    #     image_path = os.path.join(IMAGEDIR, image.filename)

    #     with open(f"{IMAGEDIR}{image.filename}", 'wb') as f:
    #         f.write(contents)
    #     annotated_filename = process_image(image_path)
    #     return {"message": f"Successfully uploaded and processed {image.filename}",
    #             "annotated_filename": annotated_filename}
    # except Exception as e:
    #     traceback.print_exc()
    #     return {"message": f"There was an error uploading or processing the file: {str(e)}"}
