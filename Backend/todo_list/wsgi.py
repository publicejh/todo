"""
WSGI config for todo_list project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# check wsgi env
env = os.environ.get('TODO_ENV', 'production')
print("manage.py env: {}".format(env))

if env == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deploy')
elif env == 'development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.debug')

application = get_wsgi_application()
