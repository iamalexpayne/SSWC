from django.conf.urls import url

from . import views

app_name = 'website'

urlpatterns = [

	# Home Page
	url(r'^$', views.home_page, name='home_page'),

	# Login
	url(r'^login/$', views.login, name='login'),

	# Logout
	url(r'^logout/$', views.logout, name='logout'),
]
