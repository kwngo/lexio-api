FROM python:3.7

ENV PORT 80

ARG PIP_REQ_FILE=requirements.txt

COPY $PIP_REQ_FILE .

RUN pip install -r $PIP_REQ_FILE

COPY . /app

WORKDIR /app

EXPOSE 8080

