from .base import *

SECRET_KEY = '1j)x_rtq2f)ve_o&a%*^63ggwvsqrr*srs(rx0%n=feh^ke5z*'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
	}
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

RECAPTCHA_SECRET_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

RECAPTCHA_SITE_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
