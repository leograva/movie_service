FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN python3 -m pip install -r /app/requirements.txt

COPY . /app/