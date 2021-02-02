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

def toxics_detail(request, toxic_id):
  toxic = Toxic.objects.get(id=toxic_id)
  return render(request, 'toxics/detail.html', { 'toxic': toxic })