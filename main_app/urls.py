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
path('herbs/<int:herb_id>/assoc_addon/<int:addon_id>/', views.assoc_addon, name='assoc_addon'),
path('herbs/<int:herb_id>/addherb_photo/', views.addherb_photo, name='addherb_photo'),
path('addons/', views.AddonList.as_view(), name='addons_index'),
path('addons/<int:pk>/', views.AddonDetail.as_view(), name='addons_detail'),
path('addons/create/', views.AddonCreate.as_view(), name='addons_create'),
path('addons/<int:pk>/update/', views.AddonUpdate.as_view(), name='addons_update'),
path('addons/<int:pk>/delete/', views.AddonDelete.as_view(), name='addons_delete'),
]