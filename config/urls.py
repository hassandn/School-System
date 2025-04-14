from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view as get_yasg_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_yasg_schema_view(
   openapi.Info(
      title="school systekm",
      default_version='v1',
      description="this is a school-system project",
      terms_of_service="",
      contact=openapi.Contact(email="hassandn6350@gmail.com"),
   ),
    permission_classes=[AllowAny],
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('',include('accounts.urls')),
    path('school/',include('schools.urls')),
    path('chat/',include('schoolChat.urls')),
    path('school-admin/', include('schoolAdmin.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    
]
