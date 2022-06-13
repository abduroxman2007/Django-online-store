"""onlineshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import *
from django.urls import include, path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('<int:id>/', ProfilePageView.as_view(), name='profile'),
    path('edit_user_profile/<int:id>/', EditProfileView.as_view(), name='edit_user_profile'),
    path('delete_user_profile/<int:id>/', DeleteProfileView.as_view(), name='delete'),

    path('register/', SignUpView.as_view(), name='sign_up'),
    path('register/email-verification/<int:id>', verificate_view, name='verifiy'),
    path('login/', LoginView.as_view(), name='log_in'),
    path('logout/', LogoutView.as_view(), name='log_out'),
    path('accounts/', include('social_django.urls', namespace='social'), name='google'),

    path('seller-products/<int:id>/', SellerProducts.as_view(), name='seller_products'),
    path('seller-add-product/', SellerAddProduct.as_view(), name='seller_add_product'),
    path('seller-update-product/<int:user_id>/<int:pk>/', SellerUpdateProduct.as_view(), name='seller_update_product'),
    path('seller-delete-product/<int:user_id>/<int:pk>/', SellerDeleteProduct.as_view(), name='seller_delete_product'),
    
    path('seller-types/<int:id>/', SellerTypes.as_view(), name='seller_types'),
    path('seller-add-type/', SellerAddType.as_view(), name='seller_add_type'),
    path('seller-update-type/<int:user_id>/<int:pk>/', SellerUpdateType.as_view(), name='seller_update_type'),
    path('seller-delete-type/<int:user_id>/<int:pk>/', SellerDeleteType.as_view(), name='seller_delete_type'),
    
]