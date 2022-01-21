from issue.serializers import IssueSerializer
from station.models import Station
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

class StationViewSet(viewsets.ModelViewSet):
  queryset = Station.objects.all()
  serializer_class = IssueSerializer