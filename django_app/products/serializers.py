from django.contrib.auth import get_user_model
from rest_framework import serializers

from products.models import Product
from products.services import ChangedPerformedNotification, MailNotificationService


class LogUpdateMixin:
    def update(self, instance, validated_data):
        previous_state = self.__class__(instance).data
        obj = super().update(instance, validated_data)
        self.log_changes(previous_state, validated_data)
        return obj

    def log_changes(self, previous_state, validated_data):
        pass


class ProductSerializer(LogUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'price',
            'sku',
            'brand',
            'retrieve_count'
        )
        read_only_fields = (
            'id',
        )

    def log_changes(self, previous_state, validated_data):
        ChangedPerformedNotification(
            subject='Product Was changed',
            users=get_user_model().objects.filter(is_staff=True),
            notification_service=MailNotificationService()
        ).notify(self.context['request'].user, previous_state, next_state=validated_data)
