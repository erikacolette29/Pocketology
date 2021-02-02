from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('profile/', views.profile, name='profile'),
path('toxics/', views.toxics_index, name='index'),
path('toxics/<int:toxic_id>/', views.toxics_detail, name='detail'),
]