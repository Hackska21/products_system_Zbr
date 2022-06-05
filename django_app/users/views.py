from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from users.serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]

