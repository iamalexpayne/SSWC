from .base import *

import json

from django.core.exceptions import ImproperlyConfigured

# JSON-based secrets module
with open(os.path.join(BASE_DIR, 'secrets.json')) as f:
	secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
	'''Get the secret variable or return explicit exception.'''
	try:
		return secrets[setting]
	except KeyError:
		error_msg = 'Set the {0} environment variable'.format(setting)
		raise ImproperlyConfigured(error_msg)

ALLOWED_HOSTS = ['*']

SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
