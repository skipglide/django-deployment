import os
from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1','localhost','45.55.40.138']
