from rest_framework import generics, permissions
from .models import ChatRoom
from .serializers import ChatRoomSerializer, ChatRoomDetailSerializer
from rest_framework.pagination import PageNumberPagination

class MessagePaginationNumber(PageNumberPagination):
    page_size = 5

class ChatRoomListView(generics.ListAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(members__user=self.request.user)


class ChatRoomDetailView(generics.RetrieveAPIView):
    serializer_class = ChatRoomDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ChatRoom.objects.all()


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request  
        return context
