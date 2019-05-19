from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = config_secret_debug['django']['databases']
