from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    editorial = models.CharField(max_length=45, null=True)
    pub_date = models.DateField(null=True)

