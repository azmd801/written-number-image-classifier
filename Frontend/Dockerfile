FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r /app/requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Set the entry point
ENTRYPOINT ["streamlit", "run", "client.py"]

# Default command
CMD ["--server.port", "8501"]