from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='tasks')

