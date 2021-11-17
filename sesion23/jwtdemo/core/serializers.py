from django.contrib.auth.hashers import make_password
from django.db import models
from rest_framework import serializers

from core.models import User

class SignUpSerializer(serializers.Serializer):
 
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()


    def create(self, data):
        password = data["password"]
        cipher_password = make_password(password)
        data["password"] = cipher_password

        user = User(**data)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role']