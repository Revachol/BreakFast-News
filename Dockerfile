FROM python:3.12

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN ["chmod", "a+x", "./docker/app.sh"]
RUN ["chmod", "a+x", "./docker/celery.sh"]

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000" ]