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

SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
	}
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

RECAPTCHA_SECRET_KEY = get_secret('RECAPTCHA_SECRET_KEY')

RECAPTCHA_SITE_KEY = get_secret('RECAPTCHA_SITE_KEY')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
