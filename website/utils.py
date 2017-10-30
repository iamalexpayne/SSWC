import requests

from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings


# Application Utils

# Send Contact Email
def send_contact_email(contact_data):
	from_email = 'website@django-template.dev'
	subject = '[django-template.dev] Contact Page'
	text_content = render_to_string('website/emails/contact_email.txt', contact_data)
	html_content = render_to_string('website/emails/contact_email.html', contact_data)
	to_email = 'website@django-template.dev'
	reply_to = contact_data['email']

	email = EmailMultiAlternatives(
		subject,
		text_content,
		from_email,
		[to_email],
		reply_to=[reply_to]
	)

	email.attach_alternative(html_content, "text/html")

	email.send(fail_silently=True)

# Adapted from: https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html
# Validate reCAPTCHA
def recaptcha_validation(post_data):
	''' Begin reCAPTCHA validation '''
	recaptcha_response = post_data.get('g-recaptcha-response')
	data = {
		'secret': settings.RECAPTCHA_SECRET_KEY,
		'response': recaptcha_response
	}
	r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
	result = r.json()
	''' End reCAPTCHA validation '''

	if result['success']:
		return True

	return False
