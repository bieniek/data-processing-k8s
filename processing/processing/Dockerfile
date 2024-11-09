FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update -y && apt-get install -y build-essential sqlite3 libsqlite3-dev poppler-utils

RUN mkdir ~/.aws && echo "[default]\n" \
         "output = json\n" > ~/.aws/config

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install -r /app/requirements.txt

COPY ./app /workspace/app

WORKDIR /workspace

COPY ./.env /workspace/.env


