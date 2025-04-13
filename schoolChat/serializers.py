from rest_framework import serializers
from .models import ChatRoom, Message, RoomMember

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']


class ChatRoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'last_message']

    def get_last_message(self, obj):
        last_msg = obj.messages.order_by('-timestamp').first()
        if last_msg:
            return MessageSerializer(last_msg).data
        return None


class ChatRoomDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)


    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'messages']

    def to_representation(self, instance):
        user = self.context['request'].user
        if not RoomMember.objects.filter(user=user, room=instance).exists():
            raise serializers.ValidationError("You are not a member of this chat room.")
        return super().to_representation(instance)


