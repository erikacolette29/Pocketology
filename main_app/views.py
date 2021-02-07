from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Toxic, Photo, Rating, Herb, Addon, HerbPhoto
from .forms import RatingForm
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'catcollector29'
# Create your views here.

def home(request):
  return render(request, 'home.html')

@login_required
def toxics_index(request):
  # Toxic.objects.filter(user=request.user) // only user can see
  toxics = Toxic.objects.all()
  return render(request, 'toxics/index.html', { 'toxics': toxics })

@login_required
def herbs_index(request): #Herb.objects.all(), make not private
  # Herb.objects.filter(user=request.user)
  herbs = Herb.objects.all()
  return render(request, 'herbs/index.html', { 'herbs': herbs })

@login_required
def herbs_detail(request, herb_id):
  herb = Herb.objects.get(id=herb_id)
  addons_herb_doesnt_have = Addon.objects.exclude(id__in = herb.addons.all().values_list('id'))
  return render(request, 'herbs/detail.html', { 'herb': herb, 'addons': addons_herb_doesnt_have})  

@login_required
def toxics_detail(request, toxic_id):
  toxic = Toxic.objects.get(id=toxic_id)
  comment = Rating.objects.filter(toxic=toxic_id)
  rating_form = RatingForm()
  return render(request, 'toxics/detail.html', { 'toxic': toxic, 'rating_form': rating_form, 'comment': comment })


@login_required
def add_rating(request, toxic_id):
  form = RatingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_rating = form.save(commit=False)
    new_rating.toxic_id = toxic_id
    new_rating.save()
  return redirect('detail', toxic_id=toxic_id)


class ToxicCreate(LoginRequiredMixin, CreateView):
  model = Toxic
  fields = ['name', 'description', 'funfact', 'howtoxic']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ToxicUpdate(LoginRequiredMixin, UpdateView):
  model = Toxic
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['description', 'funfact', 'howtoxic']

class ToxicDelete(LoginRequiredMixin, DeleteView):
  model = Toxic
  success_url = '/toxics/'


class RatingDelete(LoginRequiredMixin, DeleteView):
  model = Rating
  success_url = '/toxics/'


class HerbCreate(LoginRequiredMixin, CreateView):
  model = Herb
  fields = ['name', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HerbUpdate(LoginRequiredMixin, UpdateView):
  model = Herb
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'description']

class HerbDelete(LoginRequiredMixin, DeleteView):
  model = Herb
  success_url = '/herbs/'

class AddonList(LoginRequiredMixin, ListView):
  model = Addon

class AddonDetail(LoginRequiredMixin, DetailView):
  model = Addon

class AddonCreate(LoginRequiredMixin, CreateView):
  model = Addon
  fields = '__all__'

class AddonUpdate(LoginRequiredMixin, UpdateView):
  model = Addon
  fields = ['name', 'color', 'description']

class AddonDelete(LoginRequiredMixin, DeleteView):
  model = Addon
  success_url = '/addons/'

@login_required
def assoc_addon(request, herb_id, addon_id):
  # Note that you can pass a toy's id instead of the whole object
  Herb.objects.get(id=herb_id).addons.add(addon_id)
  return redirect('detail_herbs', herb_id=herb_id)

def add_photo(request, toxic_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, toxic_id=toxic_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', toxic_id=toxic_id)
    


def addherb_photo(request, herb_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = HerbPhoto(url=url, herb_id=herb_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail_herbs', herb_id=herb_id)



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


