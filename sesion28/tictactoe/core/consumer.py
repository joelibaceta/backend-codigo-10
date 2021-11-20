import json
from os import close
import channels

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TicTacToeConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = "Juego1vs1"

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        print("connected")
        await self.accept()

    
    async def receive(self, text_data):
        response = json.loads(text_data)

        event = response.get("event", None)
        message = response.get("message", None)

        if event == 'MOVE':
            await self.channel_layer.group_send(self.room_name, {
                "type": "send_message",
                "message": message,
                "event": "MOVE"
            })
        

    async def send_message(self, res):
        await self.send(text_data=json.dumps({"payload": res,}))
