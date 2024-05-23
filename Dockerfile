FROM python:3.11-slim-buster

WORKDIR /app

# Copy the application files
COPY . /app

# Install AWS CLI, install Python dependencies, and clean up
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r /app/requirements.txt


# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the application
CMD ["python3", "app.py"]
