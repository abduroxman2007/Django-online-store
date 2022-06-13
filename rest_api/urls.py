from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    path('v1/productlist/', ProductAPIView.as_view(), name='api1_productlist'),
    path('v1/productlist/<int:pk>', ProductAPIUpdate.as_view(), name='api1_productupdate'),
    path('v1/typelist/', TypeAPIView.as_view(), name='api1_typelist'),
    path('v1/typelist/<int:pk>', TypeAPIUpdate.as_view(), name='api1_typeupdate'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]