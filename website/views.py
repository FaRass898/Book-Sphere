
from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def about_us(request):
    return render(request, 'website/about-us.html')

def contacts(request):
    return render(request, 'website/contacts.html')

# Create your views here.
