FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install redis
CMD ["python", "apps/worker/worker.py"]
