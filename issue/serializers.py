from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Issue

class IssueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Issue
    fields = '__all__'