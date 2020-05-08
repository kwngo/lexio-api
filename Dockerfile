FROM python:3.7

COPY dev_requirements.txt .

RUN pip install -r dev_requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8080

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]



