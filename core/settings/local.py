from .base import *
from decouple import config

SECRET_KEY = config("SECRET_KEY", default="###", cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
