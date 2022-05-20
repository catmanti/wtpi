from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-oc3%qi(6*4!decaan87yy&-2b=d0g1#7d3!!wx23dh!gke&5&&"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["192.168.1.11"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass