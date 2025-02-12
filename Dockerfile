# # # Use an official Python base image
# # FROM python:3.10

# # # Set working directory
# # WORKDIR /app

# # # Copy and install dependencies
# # COPY requirements.txt .
# # RUN pip install --no-cache-dir -r requirements.txt

# # # Copy app files
# # COPY . .

# # # Install NGINX
# # RUN apt update && apt install -y nginx

# # # Copy NGINX config
# # COPY nginx.conf /etc/nginx/nginx.conf

# # # Expose ports (NGINX runs on 80, FastAPI on 8080)
# # EXPOSE 80 8080

# # # Start both NGINX and FastAPI
# # # CMD service nginx start && uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
# # CMD uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4 & nginx -g 'daemon off;'

# # Use the official Python image
# FROM python:3.10-slim

# # Set the working directory
# WORKDIR /app

# # Install Nginx
# RUN apt-get update && apt-get install -y nginx

# # Copy the Nginx configuration file
# COPY nginx.conf /etc/nginx/nginx.conf

# # Copy the requirements file and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Expose port 80 for Nginx
# EXPOSE 80

# # Start Nginx and FastAPI
# CMD service nginx start && uvicorn main:app --host 0.0.0.0 --port=8000


# Use an official Nginx image as the base
FROM nginx:latest

# Copy the custom Nginx configuration to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
