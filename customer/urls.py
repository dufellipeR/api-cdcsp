from django.urls import path
from rest_framework import urlpatterns, views
from django.urls import include, path
from .views import CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CustomerViewSet)


urlpatterns = [ 
  path('', include(router.urls))
]