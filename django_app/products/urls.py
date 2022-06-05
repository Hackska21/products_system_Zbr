from django.urls import path, include
from rest_framework import routers

from products.views import ProductsViewSet

router = routers.SimpleRouter()

router.register(r'', ProductsViewSet)


urlpatterns = [
    # Using include to maintain flexibility to change anytime the path
    path('', include(router.urls)),
]
