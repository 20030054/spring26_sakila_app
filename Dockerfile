# 1. Use a slim base image for size reduction
FROM python:3.9-slim

# 2. Metadata labels
LABEL maintainer="Sheikh Muhammad Ibrahim" \
      version="1.0" \
      description="Optimized Sakila App for BNU DevOps Assignment"

# 3. Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 4. Security: Create a non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# 5. Optimization: Leverage Layer Caching for dependencies
# Ensure you have a requirements.txt file in your repo!
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code
COPY . .

# 7. Security: Change ownership to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# 8. Expose only the application port
EXPOSE 5000

# 9. Healthcheck to verify app status
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

CMD ["python", "app.py"]