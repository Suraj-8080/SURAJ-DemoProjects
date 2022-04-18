from django.test import TestCase
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, UserViewSet

router = DefaultRouter()
router.register('address',AddressViewSet)
router.register('user',UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]