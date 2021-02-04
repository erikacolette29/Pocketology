from django.contrib import admin
from .models import Toxic, Rating
# Register your models here.

admin.site.register(Toxic)
admin.site.register(Rating)
