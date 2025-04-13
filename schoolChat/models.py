from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pk}"


class Message(models.Model):
    room = models.ForeignKey(
        ChatRoom, related_name="messages", on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content}"

    def clean(self):
        if not RoomMember.objects.filter(user=self.sender, room=self.room).exists():
            raise ValidationError(
                f"{self.sender.username} is not a member of this chat room."
            )


class RoomMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, related_name="members", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} in {self.room.name}"
