from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate, logout as auth_logout
from django.conf import settings
from django.core.exceptions import SuspiciousOperation

from .utils import recaptcha_validation
from django.utils.dateparse import parse_date

from .models import	Flowers, Features, Sightings
from .forms import FlowerForm, SightingForm

from django.utils.text import slugify




# Home
def home(request):
	flowers = Flowers.objects.using('sswc').all().order_by('comname')
	context = {'flowers': flowers}
	return render(request, 'website/home.html', context)



# Details
def details(request):
	if (request.method != "POST"):
		return redirect('website:home')

	name = request.POST.get('flower', request.POST.get('comname'))
	flower = Flowers.objects.using('sswc').get(comname=name)

	sightings = Sightings.objects.using('sswc').values_list('name', 'person', 'location', 'sighted').filter(name=name).order_by('-sighted')[:10]

	if ('save_flower' in request.POST):
		flower.comname = request.POST.get('comname')
		flower.genus = request.POST.get('genus')
		flower.species = request.POST.get('species')
		flower.save()

	context = {'flower': flower, 'sightings': sightings }
	
	if ('edit_flower' in request.POST):
		return render(request, 'website/edit_flower.html', context)

	return render(request, 'website/details.html', context)


# Add New Sighting
def add_sighting(request):
	if (request.method == "POST"):
		form = SightingForm(request.POST)


		name = request.POST.get('name')
		person = request.POST.get('person')
		location = request.POST.get('location')
		date = request.POST.get('year') + '-' + request.POST.get('month') + '-' + request.POST.get('day')
		
		sighted = parse_date(date)


		print(name, person, location, sighted)
		
		sighting = Sightings(name, person, location, sighted)

		sighting.save()

		return redirect('website:home')


	else:
		flowers = Flowers.objects.using('sswc').all().order_by('comname')
		features = Features.objects.using('sswc').all().order_by('location')
		context = {'flowers': flowers, 'features': features}
		form = SightingForm()

		return render(request, 'website/add_sighting.html', context)









