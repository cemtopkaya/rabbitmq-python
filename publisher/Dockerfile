# publisher/Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY publisher.py .
CMD ["python", "publisher.py"]

