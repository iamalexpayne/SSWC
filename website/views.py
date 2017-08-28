from django.shortcuts import render

from .forms import ContactForm
from .utils import send_contact_email


# Create your views here.

# Home View
def home_page(request):
    return render(request, 'website/home_page.html')

# Contact Page
def contact_page(request):
	if (request.method == "POST"):
		form = ContactForm(request.POST)
		if (form.is_valid()):
			send_contact_email(form.cleaned_data)
			return render(request, 'website/contact_page_message_sent.html')
	else:
		form = ContactForm()

	return render(request, 'website/contact_page.html', { 'form': form } )