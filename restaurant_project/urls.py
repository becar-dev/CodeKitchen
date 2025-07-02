from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# JWT Swagger generator
from core.utils.swagger import JWTSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant API",
        default_version='v1',
        description="Kafe jamoasi uchun avtomatlashtirilgan buyurtma va ombor API hujjatlari",
        terms_of_service="https://t.me/+nuai8f4eqm9jOWYy",
        contact=openapi.Contact(
            name="Becar Dev",
            url="https://t.me/becar_dev"
        ),
        license=openapi.License(name="beca_cr"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=JWTSchemaGenerator,  # JWT bilan Swagger ishlashi uchun
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),

    # JWT tokenlar uchun endpointlar
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger UI va ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
