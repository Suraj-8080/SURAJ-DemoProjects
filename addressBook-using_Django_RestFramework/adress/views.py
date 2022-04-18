from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from adress.apps import AdressConfig
from .models import Address, User
from .serializers import AddressSerializer, UserSeralizer

class UserViewSet(ModelViewSet):
    serializer_class = UserSeralizer
    queryset = User.objects.all()

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
