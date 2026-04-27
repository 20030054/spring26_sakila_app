# Dockerfile (optimized)
# Maintainer: Hania
# Version: 1.0.0
# Description: Sakila Flask Application

FROM python:3.9-slim

LABEL maintainer="Hania"
LABEL version="1.0.0"
LABEL description="Sakila Flask Application"

RUN groupadd -r flaskuser && useradd -r -g flaskuser flaskuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R flaskuser:flaskuser /app

USER flaskuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app.py"]
