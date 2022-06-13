from django.contrib.auth.models import User
from django.db import models
# from menu.models import *
# from menu.models import Product
# Create your models here.


class Seller(models.Model):
    GENDERS = [
        ('m', 'Man'),
        ('w', 'Woman'),
    ]
    
    AGE = [(r, r) for r in range(15, 61)]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    gender = models.CharField('Paul', max_length=1, choices=GENDERS)
    phone_number = models.IntegerField('Phone Number', null=True)
    age = models.IntegerField('Age', choices=AGE)

    class Meta:
        ordering = ['id']


    def __str__(self) -> str:
        return str(self.user)


class Customer(models.Model):

    AGE = [(r, r) for r in range(12, 61)]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.IntegerField('Phone Number', null=True)
    age = models.IntegerField('Age', choices=AGE)

    def __str__(self) -> str:
        return str(self.user)

class EmailActivateCodes(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    code = models.CharField(blank=True, max_length=7, null=False)