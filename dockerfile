FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
