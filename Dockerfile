FROM python:3.9-slim
LABEL maintainer="Urwah Taj"
LABEL version="1.0"
LABEL description="Optimized Sakila Flask App"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN adduser --disabled-password --gecos "" appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1
CMD ["python", "app.py"]
