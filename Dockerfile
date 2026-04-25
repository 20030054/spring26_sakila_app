# Use an official Python runtime as a base image
FROM python:3.9

LABEL maintainer="Abdul Hadi Jalal" \
      version="1.0.0" \
      description="Sakila Flask Application"

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' appuser
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000')" || exit 1

CMD ["python", "app.py"]