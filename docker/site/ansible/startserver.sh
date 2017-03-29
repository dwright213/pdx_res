#! /usr/bin/env bash

echo 'replace nginx configs'

rm /etc/nginx/sites-enabled/default
# above: fails all the time anyway. perhaps not needed?

ln -s /opt/site/current/configs/site_nginx.conf /etc/nginx/conf.d/
# above: handled in ansible?

echo 'run ansible stuff..'
# ansible-playbook ansible/main.yml --tags 'server,pip'
ansible-playbook ansible/main.yml -v

echo 'start nginx'
/etc/init.d/nginx start
nginx -t


echo 'start server'
/opt/site/current/venv/bin/uwsgi --ini /opt/site/current/configs/site_uwsgi.ini