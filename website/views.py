from django.shortcuts import render

# Create your views here.

# Home View
def home_page(request):
    return render(request, 'website/home_page.html')