from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

import mercadopago

class PaymentViewset(ViewSet):

    def create(self, request):
        sdk = mercadopago.SDK("TEST-6424002280491362-112519-5b8aae3159fff5d0e6ce857bd9a900fd__LB_LA__-112585375")
 
        print(request.data)
 
        payment_data = {
            "transaction_amount": float(request.data.get("transaction_amount")),
            "token": request.data.get("token"), 
            "installments": int(request.data.get("installments")),
            "payment_method_id": request.data.get("payment_method_id"),
            "payer": {
                "email": request.data.get("email"),
                "identification": {
                    "type": request.data.get("type"), 
                    "number": request.data.get("number")
                }
            }
        }

        payment_response = sdk.payment().create(payment_data)
        payment = payment_response["response"]

        print(payment)

        return Response({})
