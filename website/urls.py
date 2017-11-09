from django.conf.urls import url

from . import views

# Application URLs

app_name = 'website'

urlpatterns = [

	# Home Page
	url(r'^$', views.home_page, name='home_page'),
]
