from django.urls import path
from django.urls import include, path
from .views import StationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StationViewSet)


urlpatterns = [ 
  path('', include(router.urls))
]