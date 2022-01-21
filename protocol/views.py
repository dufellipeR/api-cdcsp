from protocol.serializers import ProtocolSerializer
from protocol.models import Protocol
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
# Create your views here.

class ProtocolListApiView(ListCreateAPIView):
  queryset = Protocol.objects.all()
  serializer_class = ProtocolSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def perform_create(self, serializer):
    return serializer.save(clerk=self.request.user)

class ProtocolDetailApiView(RetrieveUpdateDestroyAPIView):
  queryset = Protocol.objects.all()
  serializer_class = ProtocolSerializer
  permission_classes = [permissions.IsAuthenticated]
  lookup_field = 'id'

