import json

from asgiref.sync import sync_to_async

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.exceptions import Throttled

from core.models import Message
from core.serializer import MessageSerializer

class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = "lobby"

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()
    

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )  

    def _save_message(username, content):
        new_message =Message(username=username, text=content)
        new_message.save()

    def _get_messages(self):
        messages = Message.last_messages()
        serializer = MessageSerializer(messages, many=True)
        return serializer.data

    async def receive(self, text_data=None):
        
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)

        if event == "GET_MESSAGES":
            
            get_messages = sync_to_async(self._get_messages)
            messages = await get_messages()

            await self.channel_layer.group_send(self.room_name, {
                "type": "send_message",
                "message": messages,
                "event": "GET_MESSAGES"
            })

        if event == "NEW_MESSAGE":
            username = message["username"]
            content = message["content"]
            await self.channel_layer.group_send(self.room_name, {
                "type": "send_message",
                "message": message,
                "event": "NEW_MESSAGE"
            })
            
            save_message = sync_to_async(self._save_message) 
            save_message(username, content)
    
    
    async def send_message(self, res):
        await self.send(text_data=json.dumps({
            "payload": res
        }))