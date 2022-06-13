from django import forms
from .models import Product

class ProductCreateForm(forms.Form):
    product_title = forms.CharField(max_length=250)  
    type = forms.CharField(max_length=250)
    description = forms.Textarea()
    price = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['product_title', 'type','description',
              'price']
    