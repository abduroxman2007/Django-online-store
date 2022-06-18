from django.test import TestCase
from menu.models import Product, Type
from users.models import Seller
from django.contrib.auth.models import User
# Create your tests here.

class ModelTest(TestCase):
    
    def setUp(self):
        pass

    def test_create(self):
        user = User(
            username = 'abdu2007',
            first_name = 'Abduraxmon',
            last_name = 'Abduraxmonov',
            email = 'abduraxmonov@gmail.com'
        )
        user.save()
        self.assertEquals(User.objects.all().count(), 1, msg="The User objects not created") 


    # seller_create:
        seller = Seller(
            user = user,
            gender = 'm',
            phone_number = 908989753,
            age = 17,
        )
        seller.save()
        self.assertEquals(Seller.objects.all().count(), 1, msg="The Seller objects not created")


    # type_create:
        type = Type(
            name = 'Test',
            date = '2022-06-17',
            seller = seller,
        )
        type.save()       
        self.assertEquals(Type.objects.all().count(), 1, msg="The Type objects not created")


    # product_create:
        product = Product(
            image = 'media/products_img/product_default.png',
            product_title = 'Test',
            description = 'its test product',
            type = type,
            price = '360.0',
            publication_date = '2022-06-17',
            seller = seller,
        )
        product.save()        

        self.assertEqual(Product.objects.all().count(), 1, msg="The Product objects not created")
    
    
    # user_update:
        user.username = 'update_2007'
        user.save()
        self.assertEquals(User.objects.filter(username='update_2007').count(), 1, msg="The user not updated")


    # seller_update:
        seller.age = 20
        seller.save()
        self.assertEquals(Seller.objects.filter(age=20).count(), 1, msg="The seller not updated")  
    
    
    # seller_update:
        type.name = 'update'
        type.save()
        self.assertEquals(Type.objects.filter(name='update').count(), 1, msg="The type not updated")
    
    # product_update:
        product.product_title = 'update'
        product.save()
        self.assertEquals(Product.objects.filter(product_title='update').count(), 1, msg="The product not updated")
    

    # product_delete:
        product.delete()
        self.assertEquals(Product.objects.all().count(), 0, msg="The Product not deleted")
        type.delete()
        self.assertEquals(Type.objects.all().count(), 0, msg="The Type not deleted")
        seller.delete()
        self.assertEquals(Seller.objects.all().count(), 0, msg="The Seller not deleted")
        user.delete()
        self.assertEquals(User.objects.all().count(), 0, msg="The Users not deleted")

    
    
    # def test_type_model_update(self):
    #     type = Type.objects.get(pk=1)
    #     type.type_title = 'update'
    #     type.save()
    
    #     print(type)        
    #     self.assertEquals(Type.objects.filter(title='update').count(), 1, msg="The count objects incorrect add")
    

    # def test_type_model_delete(self):
    #     type = Type.objects.get(pk=1)
    #     type.delete()
    
    #     self.assertEquals(Type.objects.all().count(), 0, msg="The Type objects not deleted")
      