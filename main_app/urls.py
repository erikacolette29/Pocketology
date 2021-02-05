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
path('ratings/<int:pk>/delete/', views.RatingDelete.as_view(), name='ratings_delete'),
path('toxics/<int:toxic_id>/add_photo/', views.add_photo, name='add_photo'),
path('accounts/signup/', views.signup, name='signup'),
path('herbs/', views.herbs_index, name='index_herbs'),
path('herbs/<int:herb_id>/', views.herbs_detail, name='detail_herbs'),
path('herbs/create/', views.HerbCreate.as_view(), name='herbs_create'),
path('herbs/<int:pk>/update/', views.HerbUpdate.as_view(), name='herbs_update'),
path('herbs/<int:pk>/delete/', views.HerbDelete.as_view(), name='herbs_delete'),
]