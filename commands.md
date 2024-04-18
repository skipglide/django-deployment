python manage.py runserver --settings=dploy.settings.dev
gunicorn dploy.wsgi:application -b 0.0.0.0:80
find . -type f -print0 | xargs -0 dos2unix

# Lists all processes
ps aux
# Lists all processes and filters them by name
pas aux | grep supervisor
# Kill process by PID Number
kill -9 PID#

supervisord -c /app/config/supervisord.conf

rm -rf /root/folder/
scp -r deploy root@45.55.40.138:/root/

tail -n 10 -f /app/config/gunicorn.access.log

chmod +x ./script.sh