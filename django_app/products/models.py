from django.db import models
from django.utils.functional import cached_property


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    sku = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    retrieve_count = models.IntegerField(default=0)

    @cached_property
    def log_event(self):
        """
            Making this as a cached property allow to be triggered many times in the same request but only adding one
            change
        :return:
        """
        self.retrieve_count += 1
        self.save(update_fields=['retrieve_count'])
        return True
