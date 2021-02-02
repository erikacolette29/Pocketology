from django.shortcuts import render
from .models import Toxic

# Create your views here.

def home(request):
  return render(request, 'home.html')

def profile(request):
  return render(request, 'profile.html')

def toxics_index(request):
  toxics = Toxic.objects.all()
  return render(request, 'toxics/index.html', { 'toxics': toxics })