#! /usr/bin/env bash

echo 'Make some log files'
touch /var/log/site_uwsgi.log
touch /var/log/access.log
mkdir /var/log/nginx/
touch /var/log/nginx/access.log
touch /var/log/nginx/error.log
touch /var/log/pip.log
chmod -R 755 /var/log