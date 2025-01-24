from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Importaciones para la documentación con Swagger
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Fake API de Productos",
        default_version='v1',
        description="API para pruebas y simulaciones",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fake_api.urls')),  # Ruta de tu API principal
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Ruta de Swagger
]

# Configuración para servir archivos estáticos y de medios en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
