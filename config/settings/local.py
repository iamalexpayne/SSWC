from .base import *

SECRET_KEY = ')ix79dl)=)^ru_!1h+oi=^4hm9_a_=$mj_3vv1&79(aia%8*em'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
