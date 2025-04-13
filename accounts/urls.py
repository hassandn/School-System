from django.urls import path
from .views import CustomUserCreateView, CustomUserListView, CustomUserDetailView, CutomUserUpdateView, LogoutView

urlpatterns = [
    path('create-user/', CustomUserCreateView.as_view(), name='create-user'),
    path('list-users/', CustomUserListView.as_view(), name='list-users'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('update-user/<int:pk>/', CutomUserUpdateView.as_view(), name='update-user'),
    path('logout/', LogoutView.as_view(), name='logout' ),
]