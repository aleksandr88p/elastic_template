FROM python:3.11-slim

WORKDIR /app

COPY scripts/ ./scripts/
COPY config.py .
COPY data/ ./data/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]