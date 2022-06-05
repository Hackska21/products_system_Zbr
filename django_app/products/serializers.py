from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'price',
            'sku',
            'brand'
        )
        read_only_fields = (
            'id',
        )