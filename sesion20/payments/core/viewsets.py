from rest_framework import serializers, viewsets
from rest_framework.response import Response

from core.serializers import TokenSerializer
from core.serializers import PaymentSerializer
from core.serializers import PaymentSearchSerializer

from core.models import Token, Payment

class TokenViewSet(viewsets.ViewSet):
    """API de Tokenizacion"""

    def create(self, request):
        print(request)
        data = request.data
        serializer = TokenSerializer(data=data)
        if serializer.is_valid():
            token = serializer.save()
            return Response({"token": token.uuid})
        else:
            return Response(serializer.errors)

class PaymentViewSet(viewsets.ViewSet):
    """API de Pagos"""

    def create(self, request):
        data = request.data
        token = data["token"]
        data.pop('token')
        payment_token = Token.objects.filter(uuid = token, active=True).first()
        print(payment_token)
        if payment_token != None:
            data["token_id"] = payment_token.id
            serializer = PaymentSerializer(data=data)
            if serializer.is_valid():
                payment = serializer.save()
                payment_token.active = False
                payment_token.save()
                return Response({
                    "payment_id": payment.id,
                    "status": "approved",
                    "payment_date": payment.created_at
                })
            else:
                return Response(serializer.errors)
        else:
            return Response({"error": "Invalid Token!"})

    def list(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSearchSerializer(payments, many=True)
        return Response(serializer.data)