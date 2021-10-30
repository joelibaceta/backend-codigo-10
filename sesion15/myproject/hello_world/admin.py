from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, ModelAdmin)