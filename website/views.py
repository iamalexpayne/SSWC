from django.shortcuts import render

# Application Views

# Home View
def home_page(request):
	return render(request, 'website/home_page.html')
