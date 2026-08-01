FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Cloud Run routes requests to $PORT (default 8080). Gunicorn serves the Flask
# app; exec makes gunicorn PID 1 so it receives Cloud Run's shutdown signals.
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 --timeout 30 app:app