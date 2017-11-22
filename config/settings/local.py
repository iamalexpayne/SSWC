from .base import *

SECRET_KEY = 'xH8C6GEsGiYZXRb9NjKFfysi1jNhAUKpuBnj2nABsGjPhCChM2'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
	}
}

# Static Files

STATIC_URL = '/static/'

# Email Backend

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Google ReCaptcha

RECAPTCHA_SECRET_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

RECAPTCHA_SITE_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'

# 2017.11.22-DEA
