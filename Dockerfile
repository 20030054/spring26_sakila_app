FROM python:3.9-slim

LABEL maintainer="Fizza Mahmood"
LABEL version="1.0"
LABEL description="Optimized Docker image for Sakila Flask app"

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of app
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

# Only expose needed port
EXPOSE 5000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s \
CMD curl --fail http://localhost:5000 || exit 1

# Run app
CMD ["python", "app.py"]