bind = "0.0.0.0:8000"
workers = 4
accesslog = "/app/logs/gunicorn.access.log"
errorlog = "/app/logs/gunicorn.app.log"
capture_output = True
loglevel = "info"