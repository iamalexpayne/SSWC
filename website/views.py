from django.shortcuts import render
from django.conf import settings

from .forms import ContactForm
from .utils import send_contact_email, recaptcha_validation


# Create your views here.

# Home View
def home_page(request):
    return render(request, 'website/home_page.html')

# Contact Page
def contact_page(request):
	if (request.method == "POST"):
		form = ContactForm(request.POST)
		if form.is_valid() and recaptcha_validation(request.POST):
			send_contact_email(form.cleaned_data)
			return render(request, 'website/contact_page_message_sent.html')
	else:
		form = ContactForm()

	return render(request, 'website/contact_page.html', { 'form': form, 'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY } )