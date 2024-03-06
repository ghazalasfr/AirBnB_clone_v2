#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

# Update package lists
apt update

# Install Nginx
apt install -y nginx

# - Create the folders

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file 
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n" | 
tee /data/web_static/releases/test/index.html 

# Create a symbolic link 
ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give permission
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration 
loc_header="location \/hbnb\_static\/ {"
loc_content="alias \/data\/web\_static\/current\/;"
new_location="\n\t$loc_header\n\t\t$loc_content\n\t}\n"
sed -i "37s/$/$new_location/" /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
