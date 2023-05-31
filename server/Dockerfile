FROM python:3.9

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

RUN pip install --no-cache-dir --upgrade opencv-python-headless

COPY ./src /server/src
