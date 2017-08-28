from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives

# Send Contact Email
def send_contact_email(contact_data):
	from_email = 'website@spiffy-django-template.dev'
	subject = '[spiffy-django-template.dev] Contact Page'
	text_content = render_to_string('website/emails/contact_email.txt', contact_data)
	html_content = render_to_string('website/emails/contact_email.html', contact_data)
	to_email = 'website@spiffy-django-template.dev'
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
