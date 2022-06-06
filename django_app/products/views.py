from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from products.models import Product
from products.permissions import ReadOnlyPermission, LogRetrieves
from products.serializers import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    permission_classes = [
        LogRetrieves & (permissions.IsAdminUser | ReadOnlyPermission)
    ]
