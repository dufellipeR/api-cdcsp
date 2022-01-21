
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="CDCSP",
      default_version='v1',
      description="Controle de Chamados do Suporte",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="eduardo.fellipe30@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('customer/', include('customer.urls')),
   path('department/', include('department.urls')),
   path('issue/', include('issue.urls')),
   # path('protocol/', include('protocol.urls')),
   path('station/', include('station.urls')),
   # path('status/', include('status.urls')),
]
