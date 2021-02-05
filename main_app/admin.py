from django.contrib import admin
from .models import Toxic, Rating, Photo, Herb
# Register your models here.

admin.site.register(Toxic)
admin.site.register(Rating)
admin.site.register(Photo)
admin.site.register(Herb)