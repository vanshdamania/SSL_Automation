from flask import Flask, request
import subprocess

app = Flask(__name__)

def generate_ssl_certificate(domain):
    # Run Certbot command to generate SSL certificate
    subprocess.run(["certbot", "certonly", "--nginx", "-d", domain, "--non-interactive", "--agree-tos", "-m", "manavj.tanikatech@gmail.com"])

def create_nginx_configuration(domain):
    # Create a separate configuration file for the domain
    nginx_conf_path = f"/etc/nginx/conf.d/{domain}.conf"
    nginx_ssl_conf = f"""
    server {{
        listen 80;
        server_name {domain} www.{domain};
        return 301 https://{domain}$request_uri;
    }}

    server {{
        listen         443 ssl;
        http2          on;
        server_name    www.{domain};
        ssl_certificate /etc/letsencrypt/live/{domain}/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/{domain}/privkey.pem;
        return         https://www.{domain}$request_uri;

        root /usr/share/nginx/html;
        index index.html index.htm;
    }}

    server {{
        listen         443 ssl;
        http2          on;
        server_name    {domain};
        ssl_certificate /etc/letsencrypt/live/{domain}/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/{domain}/privkey.pem;

        root /usr/share/nginx/html;
        index index.html index.htm;
    }}
    """

    # Write the server block to the configuration file
    with open(nginx_conf_path, "w") as nginx_conf:
        nginx_conf.write(nginx_ssl_conf)

    # Restart Nginx to apply changes
    subprocess.run(["service", "nginx", "restart"])

@app.route('/configure', methods=['POST'])
def configure_reverse_proxy():
    domain = request.form['domain']
    generate_ssl_certificate(domain)
    create_nginx_configuration(domain)
    return 'Reverse proxy configuration completed.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
