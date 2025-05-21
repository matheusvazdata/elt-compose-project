# Etapa 1: build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
COPY . .

# Etapa 2: runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:$PATH"
CMD ["python", "main.py"]