#!/bin/bash
set -e
echo -e "\n>>> Stopping Gunicorn"
cd /app/
. env/bin/activate
./scripts/super.sh stop gunicorn

echo -e "\n>>> Deleting old files"
rm -rf /app/django-deployment
rm -rf /app/config
rm -rf /app/scripts
rm requirements.txt

echo -e "\n>>> Copying new files"
cp -r /root/deploy/django-deployment /app/
cp -r /root/deploy/django-deployment/config /app/
cp -r /root/deploy/django-deployment/scripts /app/
cp /root/deploy/django-deployment/requirements.txt /app/

echo -e "\n>>> Installing Python packages"
pip install -r /app/requirements.txt

echo -e "\n>>> Running Django migrations"
cd /app/django-deployment/

echo -e "\n>>> Collecting static files"
/app/django-deployment/manage.py collectstatic

echo -e "\n>>> Re-reading Supervisord config"
/app/scripts/super.sh reread

echo -e "\n>>> Starting Gunicorn"
/app/scripts/super.sh start gunicorn