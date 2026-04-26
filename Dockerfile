# 1. Use a slim base image
FROM python:3.9-slim

# Add Labels
LABEL maintainer="M. Abdullah Abbas f2023-871@gmail.com"
LABEL version="1.0"
LABEL description="Optimized Sakila Flask Application"

# Set working directory
WORKDIR /app

# 2. Create a non-root user
RUN adduser --disabled-password --gecos "" appuser

# 3. Leverage caching: Copy only requirements first
COPY requirements.txt .

# Install dependencies (no-cache-dir keeps image small)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Change ownership of the app files to the new user
RUN chown -R appuser:appuser /app

# 4. Use the non-root user
USER appuser

# 5. Expose ONLY the necessary port
EXPOSE 5000

# 6. Add a Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# Start the application
CMD ["python", "app.py"]