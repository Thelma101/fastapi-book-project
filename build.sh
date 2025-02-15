# #!/bin/bash
# # Install Nginx using Nix
# nix-env -iA nixpkgs.nginx

# # Copy the Nginx configuration file
# cp nginx.conf /etc/nginx/nginx.conf

#!/bin/bash

# Install nginx
apt-get update & apt-get install -y nginx

# Start nginx
nginx

# Start FastAPI with Uvicorn
uvicorn main:app --host 0.0.0.0 --port=8000
