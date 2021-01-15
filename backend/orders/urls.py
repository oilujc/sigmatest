from django.contrib import admin
from django.urls import path

from .views import (OrderViewset, ProductView)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', OrderViewset, basename='orders')

app_name = 'api_orders'
urlpatterns = [
    path('product/', ProductView.as_view(), name='product')
] + router.urls
