#!/bin/bash

# 1. Python installation
sudo apt update
sudo apt install python3 python3-venv -y

# 2. Python pip installation
sudo apt install python3-pip -y

# 3. Certbot installation
sudo apt install libaugeas0 -y
sudo python3 -m venv /opt/certbot/
sudo /opt/certbot/bin/pip install --upgrade pip
sudo /opt/certbot/bin/pip install certbot certbot-nginx
sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot

# 4. Flask Python package installation
sudo pip3 install flask

# 5. Nginx installation
sudo apt install nginx -y

#6. Add nginx user
sudo adduser --system --no-create-home --disabled-login --disabled-password --group nginx
