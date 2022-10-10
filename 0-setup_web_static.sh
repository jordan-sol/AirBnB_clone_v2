#!/usr/bin/env bash
# Configure server at ngnix
apt update
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p  /data/web_static/shared
basicHtml='<html>
<head>
</head>
<body>
holberton school
</body>
</html>'
echo "$basicHtml" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
