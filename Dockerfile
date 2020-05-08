FROM python:3.7

ENV PORT

ARG PIP_REQ_FILE=requirements.txt

COPY PIP_REQ_FILE .

RUN pip install -r dev_requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8080

