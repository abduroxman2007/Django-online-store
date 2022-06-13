from dataclasses import fields
from rest_framework import serializers
from menu.models import Product, Type

# class ProductModel:
#     def __init__(self, image, product_title, description, type, price, publication_date):
#         self.image = image
#         self.product_title =product_title
#         self.description = description
#         self.type = type
#         self.price = price
#         self.publication_date = publication_date

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image', 'product_title', 'description', 'type', 'price']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']


