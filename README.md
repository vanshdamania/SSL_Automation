# SSL_Automation
This repository contains a python script that allows you to automate configure a reverse proxy and generate SSL certificates for your domain using Certbot and Nginx. 

# Overview
This Flask application provides an API endpoint to configure a reverse proxy and generate SSL certificates for a specified domain. When a POST request is made to the '/configure' endpoint with the domain name, the application performs the following steps:-
1. Calls Certbot to generate SSL certificates for the domain using the Nginx plugin.
2. Creates a separate Nginx configuration file for the domain, defining server blocks for both HTTP and HTTPS traffic.
3. Writes the Nginx configuration to the appropriate location.
4. Restarts Nginx to apply the changes and enable the reverse proxy and SSL for the domain.

# Prerequisites
To run this application, you need:-
1. Python, Nginx installed on the system.
2. Install necessary packages by running the following command:-                                                                         
        pip install -r requirements.txt or pip3 install -r requirements.txt

# Usage 
1. Clone this repository: https://github.com/vanshdamania/SSL_Automation
2. Execute the Python script with elevated privileges using the sudo command.
3. Send a POST request to http://<<Your IP>>:5000/configure with the domain name as a form parameter.
4. The application will configure the reverse proxy and generate SSL certificates for the specified domain.

# Note
Please ensure that you customize the Nginx configuration file provided. Take a look at the uploaded file to verify the changes. Additionally, make sure to correctly specify the appropriate directory in the program, aligning it with the requirements of Certbot and Nginx. Also make sure you have the necessary privileges.

# Pro Tip
You can run a python script as a service in the background as well.
https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267
