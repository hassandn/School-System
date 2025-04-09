from django.urls import path
from .views import CustomUserCreateView, CustomUserListView, CustomUserDetailView

urlpatterns = [
    path('create-user/', CustomUserCreateView.as_view(), name='create-user'),
    path('list-users/', CustomUserListView.as_view(), name='list-users'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
]