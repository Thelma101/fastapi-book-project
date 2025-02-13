# Base Python image
FROM python:3.10

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80 8000

# Start Nginx and FastAPI together
CMD service nginx start && uvicorn main:app --host 127.0.0.1 --port 8000
