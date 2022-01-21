from customer.serializers import CustomerSerializer
from django.shortcuts import render
from .models import Customer
from rest_framework import serializers, viewsets

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer