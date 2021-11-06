from django.db import models
from django.db.models import query
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    main_picture = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    main_picture = models.ImageField(upload_to="products/")
    description=models.TextField(null=True)
    brand = models.CharField(max_length=100, null=True)
    stock=models.IntegerField(null=True)
    page_info = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name="products")

    def __str__(self):
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField()

    @property
    def subtotal(self):
        return self.quantity * self.product.price

    