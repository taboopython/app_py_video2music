# Dockerfile

FROM python:3.9

RUN apt-get update \
    && apt-get install -y ffmpeg \
    && pip install moviepy

WORKDIR /app

COPY videotomusic.py /app/

ENTRYPOINT ["python", "/app/videotomusic.py"]