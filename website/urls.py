from django.conf.urls import url

from . import views

app_name = 'website'
urlpatterns = [

	# Home Page
    url(r'^$', views.home_page, name='home_page'),

    # Contact Page
    url(r'^contact$', views.contact_page, name='contact_page'),
]