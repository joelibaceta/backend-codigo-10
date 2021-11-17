from rest_framework import serializers
from rest_framework.decorators import authentication_classes
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core.serializers import UserSerializer, SignUpSerializer

class UserViewSet(ViewSet):

    def retrieve(self, request, pk):

        if request.user.is_anonymous:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(pk=pk).first()

        if user == None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.user.pk == user.pk:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        

    def list(self, request):

        if request.user.is_anonymous:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user = User.objects.filter(pk=request.user.id).first()
        if user == None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def sign_up(self, request):

        data = request.data

        serializer = SignUpSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
         

class CustomObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["email"] = user.email
        return token

class AuthViewSet(ViewSet):

    def post(self, request):

        data = request.data

        email = data["email"]
        password = data["password"]

        user = User.objects.filter(email__exact=email).first()

        if user == None:
            return Response({
                "status": "Ups, Credenciales invalidas, intente nuevamente"
            }, status=status.HTTP_400_BAD_REQUEST)


        user_authenticated = authenticate(username=user.username, password=password)

        if user_authenticated != None:
            
            token = CustomObtainPairSerializer.get_token(user_authenticated)

            return Response({
                "status": "ok",
                "token": str(token.access_token)
            })

        else:

            return Response({
                "status": "error"
            })