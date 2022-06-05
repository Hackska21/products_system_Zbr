from django.urls import path, include
from rest_framework import routers

from users.views import UsersViewSet

router = routers.SimpleRouter()

router.register(r'', UsersViewSet)

urlpatterns = [
    # Using include to maintain flexibility to change anytime the path
    path('', include(router.urls)),
]
