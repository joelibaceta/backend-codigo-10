from django.shortcuts import render
from django.views import View

from core.models import Category, Product, CartItem

import functools

# Create your views here.
class CatalogView(View):

    def get(self, request):

        items = CartItem.objects.all()
        counter = functools.reduce(lambda x, y: y.quantity + x, items, 0)

        category_id=request.GET.get("category")

        categories = Category.objects.all()
        if category_id != None:
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()
        context = {
            "categories": categories,
            "products": products,
            "counter": counter
        }
        return render(request, 'main.html', context)

class ProductView(View):

    def get(self, request, pk):

        items = CartItem.objects.all()
        counter = functools.reduce(lambda x, y: y.quantity + x, items, 0)


        product = Product.objects.get(pk=pk)

        context = {
            "product": product,
            "stars": range(product.rating),
            "counter": counter
        }

        return render(request, 'detail.html', context)

class KartView(View):

    def get(self, request):
        items = CartItem.objects.all() 
        counter = functools.reduce(lambda x, y: y.quantity + x, items, 0)


        context={
            "items": items, 
            "counter": counter
        }

        return render(request, "cart.html", context)

    def post(self, request):
        data = request.POST
        print(data)
        quantity = int(data["quantity"])
        product_id = data["product_id"]
        
        item = CartItem.objects.filter(product_id=product_id).first()

        if item == None:
            item = CartItem(quantity=quantity, product_id=product_id)
        else:
            item.quantity = item.quantity + quantity

        item.save()

        items = CartItem.objects.all() 
        counter = functools.reduce(lambda x, y: y.quantity + x, items, 0)


        context={
            "items": items, 
            "counter": counter
        }

        return render(request, "cart.html", context)
