# 1. Use a slim base image
FROM python:3.9-slim

# 8. Add Labels
LABEL maintainer="M Zakriya Ahmed"
LABEL description="Optimized Sakila Flask App"
LABEL version="1.0"

# 6. Create a non-root user
RUN useradd -m appuser

WORKDIR /app

# 2 & 3. Leverage caching and requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Change ownership of the files to the non-root user
RUN chown -R appuser:appuser /app

# 4. Remove hardcoded secrets (they will be passed at runtime)
ENV MYSQL_HOST=sakila-db
ENV MYSQL_USER=root
ENV MYSQL_DB=sakila
# Note: MYSQL_PASSWORD is intentionally omitted here

# 5. Expose ONLY the necessary port
EXPOSE 5000

# 7. Add a Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/ || exit 1

# Switch to the non-root user before running the app
USER appuser

CMD ["python", "app.py"]