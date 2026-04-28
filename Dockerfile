FROM python:3.9-slim
RUN apt-get update && apt-get install -y curl

LABEL maintainer="yameena"
LABEL version="1.0"
LABEL description="Optimized Sakila Flask App"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

ENV MYSQL_HOST=mysql
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV MYSQL_DB=sakila

EXPOSE 5000

HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1

CMD ["python", "app.py"]
