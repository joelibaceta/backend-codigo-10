
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from core.models import Booking

from django.contrib.auth import password_validation, authenticate

class BookingsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nro_mesa = serializers.IntegerField()
    fec_reserva = serializers.DateTimeField()
    estado = serializers.CharField()
    nro_personas = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def create(self, data):
        booking = Booking(**data)
        booking.save()
        return booking


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

   
    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
           raise serializers.ValidationError('Las credenciales no son validas')
        
        self.context["user"] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key