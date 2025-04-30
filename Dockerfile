FROM python:3.10-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim
WORKDIR /app

RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY server.py db_init.py entrypoint.sh ./

RUN chmod +x entrypoint.sh

VOLUME ["/app/data"]

ENTRYPOINT ["./entrypoint.sh"]
