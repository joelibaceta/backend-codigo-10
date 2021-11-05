from rest_framework import serializers

from core.models import Category, Product

class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    sku = serializers.CharField(max_length=11)
    exp_date = serializers.DateField()
    category_name = serializers.ReadOnlyField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, product, data):
        product = Product.objects.filter(pk=product.id)
        product.update(**data) 
        return product


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products']