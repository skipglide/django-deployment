import os
from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0', 'janus-vault.com', 'www.janus-vault.com']
