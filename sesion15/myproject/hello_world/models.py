from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=45)
    director = models.CharField(max_length=45)