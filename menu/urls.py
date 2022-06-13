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
from ctypes import alignment
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', returhomeview),
    path('home/', HomePageView.as_view(), name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('contact/', DashboardCreatNotificationsView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('product-info/<int:product_id>/', ProductInfoView.as_view(), name='product_info'),
    
    path('dashboard/', senddashboardview),
    path('dashboard/dashboard/', DashboardPageView.as_view()),
    path('dashboard/dashboard-products/', DashboardProductsView.as_view()),
    path('dashboard/products-list/', DashboardProductsListPageView.as_view()),
    path('dashboard/notifications/', DashboardNotificationsView.as_view()),
    path('dashboard/type-list/', DashboardTypeView.as_view()),

    path('dashboard/create-product/', CreateProductsView.as_view()),
    path('dashboard/create-type/', CreateTypeView.as_view()),

    path('dashboard/edit-product/<int:id>', UpdateProductsView.as_view()),
    path('dashboard/type-edit/<int:id>', UpdateTypeView.as_view()),

    path('dashboard/delete-product/<int:id>', DeleteProductsView.as_view()),
    path('dashboard/type-delete/<int:id>', DeleteTypeView.as_view()),
]

