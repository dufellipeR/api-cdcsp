from django.db.models import query
from django.shortcuts import render
from .serializers import IssueSerializer
from .models import Issue
from rest_framework import viewsets

# Create your views here.
class IssueViewSet(viewsets.ModelViewSet):
  queryset = Issue.objects.all()
  serializer_class = IssueSerializer