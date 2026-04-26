FROM python:3.9-slim

# Metadata
LABEL maintainer="Saad Asim"
LABEL version="1.0"
LABEL description="Sakila Flask Application"

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Create non-root user
RUN useradd -m appuser

# Switch to non-root user
USER appuser

# Expose Flask port
EXPOSE 5000

# Healthcheck to verify app is running
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1

# Run app
CMD ["python", "app.py"]