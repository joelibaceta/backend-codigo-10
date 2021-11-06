from rest_framework import serializers, viewsets
from rest_framework import response
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from rest_framework import status

from core.models import Booking
from core.serializers import BookingsSerializer
from core.serializers import UserLoginSerializer

class BookingViewSet(viewsets.ViewSet):
    """API de reservas"""

    def list(self, request):
        if request.user.is_anonymous:
            return Response({}, status.HTTP_403_FORBIDDEN)

        bookings = Booking.objects.filter(user_id=request.user.id)
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        if "user_id" in data:
            return Response({
                "error": "user_id param is not allowed"
            }, status.HTTP_400_BAD_REQUEST)
        if not request.user.is_anonymous:
            data["user_id"] = request.user.id

        serializer = BookingsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserViewSet(viewsets.ViewSet):

    def login(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user, token = serializer.save()
            data = {
                'user': user.first_name,
                'access_token': token
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    def logout(self, request):
        user = request.user
        if user.is_anonymous:
            return Response({}, status.HTTP_401_UNAUTHORIZED)
        token = Token.objects.filter(user_id=user.id)
        token.delete()
        return Response({
            "status": "OK"
        })