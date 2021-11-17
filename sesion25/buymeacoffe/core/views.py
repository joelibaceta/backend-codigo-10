from django.shortcuts import redirect, render

import mercadopago

from django.views import View

def function_success(request):
    payment_id = request.GET.get("payment_id")
    context = {
        "payment_id": payment_id
    }
    return render(request, "success.html", context)

def function_pending(request):
    return render(request, "pending.html")

def function_fail(request):
    return render(request, "fail.html")
 


# Create your views here.
class PaymentButtonView(View):

    def post(self, request):
        amount = request.POST.get("amount")

        sdk = mercadopago.SDK("TEST-6424002280491362-112519-5b8aae3159fff5d0e6ce857bd9a900fd__LB_LA__-112585375")

        preference_data = {
            "items": [
                {
                    "title": "Donation",
                    "quantity": 1,
                    "unit_price": float(amount),
                }
            ],
            "auto_return": "approved",
            "back_urls": {
                "success": "http://localhost:8000/payment/success",
                "pending": "http://localhost:8000/payment/pending",
                "fail": "http://localhost:8000/payment/fail"
            }
        }
        print(preference_data)

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        
        payment_url = preference["sandbox_init_point"] 
        
        return redirect(payment_url)

    def get(self, request):

        sdk = mercadopago.SDK("TEST-6424002280491362-112519-5b8aae3159fff5d0e6ce857bd9a900fd__LB_LA__-112585375")

        preference_data = {
            "items": [
                {
                    "title": "Coffe",
                    "quantity": 1,
                    "unit_price": 12,
                }
            ]
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]

        context = {
            "payment_url": preference["sandbox_init_point"] 
        }

        return render(request, "index.html", context)