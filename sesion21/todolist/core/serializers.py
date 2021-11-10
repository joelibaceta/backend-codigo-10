from typing import ParamSpecArgs
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from core.models import Task

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])

        if not user:
            raise serializers.ValidationError("Invalid Credentials!")
        
        self.context["user"] = user
        return attrs

    
    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context['user'], token.key



class TaskSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    user_id = serializers.IntegerField()
    status = serializers.ReadOnlyField()

    def create(self, data):
        task = Task(**data)
        task.save()
        return task

    