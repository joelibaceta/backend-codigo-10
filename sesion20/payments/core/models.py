from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Token(models.Model):

    uuid = models.UUIDField()
    card_number = models.CharField(max_length=16)
    card_holder = models.CharField(max_length=100)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    active = models.BooleanField(default=True)

class Payment(models.Model):

    amount = models.FloatField()
    token = models.OneToOneField(Token, on_delete=CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
