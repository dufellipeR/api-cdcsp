from status.serializers import StatusSerializer
from status.models import Status
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

class StatusViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer
