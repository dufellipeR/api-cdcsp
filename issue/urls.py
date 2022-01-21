from django.urls import path
from django.urls import include, path
from .views import IssueViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', IssueViewSet)


urlpatterns = [ 
  path('', include(router.urls))
]