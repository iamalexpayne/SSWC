from django.conf.urls import url

from . import views

app_name = 'website'

urlpatterns = [

	# Home
	url(r'^$', views.home, name='home'),

	# Details
	url(r'^details$', views.details, name='details'),

	# Add New Sighting
	url(r'^add-sighting$', views.add_sighting, name='add_sighting'),

]
