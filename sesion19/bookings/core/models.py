from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Booking(models.Model):
    nro_mesa = models.IntegerField(null=True)
    fec_reserva = models.DateTimeField(null = True)
    estado = models.CharField(max_length=100, null = True)
    nro_personas = models.IntegerField(null=True)
    user = models.ForeignKey(User, related_name="bookings", on_delete=CASCADE, null=True)