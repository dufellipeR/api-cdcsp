from django.urls import path
from django.urls import include, path
from .views import StatusViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StatusViewSet)


urlpatterns = [ 
  path('', include(router.urls))
]