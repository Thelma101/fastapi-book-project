# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 8080 for NGINX
EXPOSE 8080

# Start NGINX and FastAPI
CMD service nginx start && uvicorn main:app --host 0.0.0.0 --port 8000