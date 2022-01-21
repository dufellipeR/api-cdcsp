from django.forms import fields
from .models import Protocol
from rest_framework import serializers

class ProtocolSerializer(serializers.ModelSerializer):
  class Meta:
    model = Protocol
    fields = '__all__'