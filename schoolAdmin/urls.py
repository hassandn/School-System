from django.urls import path, include
from .views import AdminModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    r"models/(?P<app_label>[\w-]+)/(?P<model_name>[\w-]+)",
    AdminModelViewSet,
    basename="admin-model",
)

urlpatterns = [
    path("", include(router.urls)),
]
