#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # check manage env
    env = os.environ.get('TODO_ENV', 'production')
    print("manage.py env: {}".format(env))

    if env == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deploy')
    elif env == 'development':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.debug')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
