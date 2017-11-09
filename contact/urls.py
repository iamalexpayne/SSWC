from django.conf.urls import url

from . import views

# Application URLs

app_name = 'contact'

urlpatterns = [

	# Contact Page
	url(r'^$', views.contact_page, name='contact_page'),
]
