# Python import:
import json

# Django import:
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


# Consumers classes:
class NotificationConsumer(AsyncWebsocketConsumer):

    # Join to channel group:
    async def connect(self):
        self.group_name = 'notifications'
        # Join to channel group:
        await self.channel_layer.group_add(
            self.group_name, self.channel_name)
        await self.accept()
    
    # Leave to channel group:
    async def disconnect(self, event):
        # Leave to channel group:
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name)

    # Receive message from group:
    async def send_collect(self, event):
        # Convert Python dictionary into Json:
        json_message = json.dumps(event)
        # Send message to channel:
        await self.send(json_message)
