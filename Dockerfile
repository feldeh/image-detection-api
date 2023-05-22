FROM python:3.9

WORKDIR /image-detection

COPY ./requirements.txt /image-detection/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /image-detection/requirements.txt

COPY ./src /image-detection/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]