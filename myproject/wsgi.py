"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
settings_path = '/var/www/wt2/myproject'
sys.path.insert(0, settings_path)

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings.dev")

application = get_wsgi_application()
