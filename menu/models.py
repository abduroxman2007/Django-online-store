from django.db import models
from datetime import date
from django.contrib.auth.models import User
from users.models import *
from users.models import Seller
# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField(auto_now=True)
    seller = models.ForeignKey(
        Seller, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products_img')
    product_title = models.CharField(max_length=25)
    description = models.TextField()
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()
    publication_date = models.DateField(auto_now_add=True)
    seller = models.ForeignKey(
        Seller, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['publication_date']

    def __str__(self) -> str:
        return str(self.product_title)


class Contact(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now=True)
    text = models.TextField(unique=False)

    class Meta:
        ordering = ['date']

    def __str__(self) -> str:
        return self.name


class Basket(models.Model):
    product = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return self.id
