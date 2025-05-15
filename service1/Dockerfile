FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir \
    Flask==3.0.0 \
    pika==1.3.2 \
    python-json-logger==2.0.7 \
    requests==2.25.1
CMD ["python", "app.py"]
