FROM python:3.9-alpine AS prod

LABEL org.opencontainers.image.title="NiFi Exporter" \
      org.opencontainers.image.description="NiFi Exporter exposes Apache NiFi metrics for Prometheus, enabling simplified monitoring and observability with support for multi-architecture Docker images." \
      org.opencontainers.image.url="https://hub.docker.com/r/sakkiii/nifi_exporter" \
      org.opencontainers.image.source="https://github.com/sakkiii/nifi_exporter" \
      org.opencontainers.image.licenses="Apache License 2.0"

RUN mkdir /app/
WORKDIR /app/

COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /app/

ENV FLASK_APP=server.py
CMD ["python", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]