from django.urls import path
from .views import ChatRoomListView, ChatRoomDetailView

urlpatterns = [
    path("rooms/", ChatRoomListView.as_view(), name="room-list"),
    path("rooms/<int:pk>/", ChatRoomDetailView.as_view(), name="room-detail"),
]
