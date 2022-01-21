from customer.serializers import CustomerSerializer
from django.shortcuts import render
from .models import Customer
from rest_framework import serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['code']