from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from menu.models import Product
from .serializers import ProductSerializer, TypeSerializer
from menu.models import Type
# Create your views here.

# class ProductAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer 

class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    


class TypeAPIView(ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer