from django.contrib import admin

from core.models import Product
from core.models import Category
from core.models import CartItem

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'main_picture')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'subtotal')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)