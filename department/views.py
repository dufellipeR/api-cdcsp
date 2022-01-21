from department.serializers import DepartmentSerializer
from django.shortcuts import render
from .models import Department
from rest_framework import viewsets

class DepartmentViewSet(viewsets.ModelViewSet):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer