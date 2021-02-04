from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('profile/', views.profile, name='profile'),
path('toxics/', views.toxics_index, name='index'),
path('toxics/<int:toxic_id>/', views.toxics_detail, name='detail'),
path('toxics/create/', views.ToxicCreate.as_view(), name='toxics_create'),
path('toxics/<int:pk>/update/', views.ToxicUpdate.as_view(), name='toxics_update'),
path('toxics/<int:pk>/delete/', views.ToxicDelete.as_view(), name='toxics_delete'),
path('toxics/<int:toxic_id>/add_rating/', views.add_rating, name='add_rating'),
path('accounts/signup/', views.signup, name='signup'),
]