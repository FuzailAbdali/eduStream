import json
from channels.generic.websocket import AsyncWebsocketConsumer


class LectureChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["session_id"]
        self.room_group_name = f"lecture_chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        payload = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": payload.get("message", ""),
                "sender": payload.get("sender", "anonymous"),
            },
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"sender": event["sender"], "message": event["message"]}))
