import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import AccessToken
from .models import RoomMember, Message, ChatRoom
from django.core.exceptions import ValidationError

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        token = None
        for header in self.scope['headers']:
            if header[0] == b'authorization':
                token = header[1].decode('utf-8').split(' ')[1]
                break
        if token:
            self.user = await self.get_user_from_token(token)
            is_chatmemeber = await self.check_if_user_exist_in_chatroom(self.user, self.room_name)
            if is_chatmemeber:
                if self.user:
                    await self.accept()
                    await self.channel_layer.group_add(
                        self.room_group_name,
                        self.channel_name
                    )
                else:
                    await self.close()
            else:
                await self.close()
        else:
            await self.close()

    @database_sync_to_async
    def check_if_user_exist_in_chatroom(self, user, room):
        """
        check if user have access to chatRoom
        """
        try:
            
            if RoomMember.objects.get(user=user, room=room):
                return True
        except ObjectDoesNotExist:
            # return None
            return False
        
        
    @database_sync_to_async
    def get_user_from_token(self, token):
        """
        check if user is valid   
        """
        try:
            accessToekn = AccessToken(token)
            user_id = accessToekn['user_id']  
            user = get_user_model().objects.get(id=user_id) 
            return user
        except ObjectDoesNotExist:
            return None
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        is_data_saved = await self.save_message(text_data=data)
        if is_data_saved:

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': self.channel_name  
                }
            )
    
    @database_sync_to_async
    def save_message(self, text_data):
        """
        Save the message to the database
        """
        try:
            room = ChatRoom.objects.get(pk=self.room_name)  # اگر نام اتاق را به عنوان رشته می‌فرستید
        except ChatRoom.DoesNotExist:
          raise ValidationError(f"Room with name '{self.room_name}' does not exist.")
        message = Message(
            sender = self.user,
            room = room,
            content = text_data['message']
        )
        message.save()
        return True
    
        
    async def chat_message(self, event):
        message = event['message']

        sender = event.get('sender', None)  

        if sender != self.channel_name:  
            await self.send(text_data=json.dumps({
                'message': message
            }))

    




