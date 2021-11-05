from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):

    name=models.CharField(max_length=100)
    price = models.FloatField()
    sku=models.CharField(max_length=11)
    exp_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="products")

    @property
    def category_name(self):
        if self.category:
            return self.category.name
        else:
            return "-"
