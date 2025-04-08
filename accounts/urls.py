from django.urls import path
from .views import CustomUserCreateView

urlpatterns = [
    path('create-user/', CustomUserCreateView.as_view(), name='create-user'),
]