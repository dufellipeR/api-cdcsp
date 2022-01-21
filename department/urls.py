from django.urls import path
from rest_framework import urlpatterns, views
from django.urls import include, path
from .views import DepartmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', DepartmentViewSet)


urlpatterns = [ 
  path('', include(router.urls))
]