#!/bin/bash
# Install Nginx using Nix
nix-env -iA nixpkgs.nginx

# Copy the Nginx configuration file
cp nginx.conf /etc/nginx/nginx.conf