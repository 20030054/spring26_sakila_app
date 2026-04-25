FROM python:3.9-slim

LABEL maintainer="Hassan Aslam" \
      version="1.0" \
      description="Optimized Sakila Flask App"

# Set non-root user
RUN useradd -m appuser

WORKDIR /app

# Layer caching: copy reqs first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app.py"]