from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Toxic
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
  return render(request, 'home.html')

@login_required
def profile(request):
  return render(request, 'profile.html')

@login_required
def toxics_index(request):
  toxics = Toxic.objects.all()
  return render(request, 'toxics/index.html', { 'toxics': toxics })

@login_required
def toxics_detail(request, toxic_id):
  toxic = Toxic.objects.get(id=toxic_id)
  return render(request, 'toxics/detail.html', { 'toxic': toxic })

class ToxicCreate(LoginRequiredMixin, CreateView):
  model = Toxic
  fields = '__all__'
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