FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY analytics_app.py .
COPY data.csv .

LABEL maintainer="BDAT1008 DevOps Group 7"
LABEL description="Big Data Analytics Application"

CMD ["python", "analytics_app.py"]