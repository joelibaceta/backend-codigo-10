from rest_framework.viewsets import ViewSet

from rest_framework import status

from rest_framework.response import Response

from culqi.client import Culqi

class PaymentViewSet(ViewSet):

    def create(self, request):

        data = request.data

        public_key = "pk_test_gFhvKSALDrVdVo85"
        private_key = "sk_test_gEoUP2liniTAqEws"

        culqi = Culqi(public_key=public_key, private_key=private_key)

        response = culqi.charge.create({
            "amount": data["amount"],
            "capture": False, # Solo reservar el dinero
            "currency_code": "PEN",
            "description": data["description"],
            "email": "prueba@gmail.com",
            "installments": 0,
            "source_id": data["token"],
        })

        # Para capturar el pago :
        # culqi.charge.capture(id: _id)

        print(response["data"])

        return Response(status=status.HTTP_201_CREATED)