"""buymeacoffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import PaymentButtonView
 
from core.views import function_success, function_pending, function_fail

from core.viewsets import PaymentViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaymentButtonView.as_view()),
    path('create_button/', PaymentButtonView.as_view()),
    path('payment/success', function_success),
    path('payment/pending', function_pending),
    path('payment/fail', function_fail),
    path('process_payment/', PaymentViewset.as_view({
        'post': 'create'
    }))
]
