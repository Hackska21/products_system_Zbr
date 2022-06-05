from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    sku = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
