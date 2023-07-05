# configures a brand new Ubuntu machine
exec { 'command':
     provider => shell,
     command  => 'sudo apt-get -y update;
     sudo apt-get -y install nginx;
     sudo sed -i "listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
     service nginx restart',
     }