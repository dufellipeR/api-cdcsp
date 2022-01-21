from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProtocolListApiView.as_view(), name="protocols"),
    path('<int:id>', views.ProtocolDetailApiView.as_view(), name="protocol"),
]