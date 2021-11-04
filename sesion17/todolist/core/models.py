from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True)
    finished = models.BooleanField(null=True) 
    attachtment = models.ImageField(upload_to="attachments", null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)

    def __str__(self):
        return f"Title: {self.title}"

