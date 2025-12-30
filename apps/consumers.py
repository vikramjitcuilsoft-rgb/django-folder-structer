import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        print("✅ WebSocket connected")

    async def disconnect(self, close_code):
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
            print("❌ WebSocket disconnected")

    async def receive(self, text_data):
        data = json.loads(text_data)
        msg_type = data.get("type")

        # JOIN ROOM
        if msg_type == "join":
            room = data["room"]
            self.room_group_name = f"chat_{room}"

            # Add this socket to group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            # Notify room
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "author": "system",
                    "content": f"{data['username']} joined {room}",
                    "timestamp": "",
                }
            )

        # SEND MESSAGE
        elif msg_type == "message":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "author": data["author"],
                    "content": data["content"],
                    "timestamp": data["timestamp"],
                }
            )

    # RECEIVE MESSAGE FROM GROUP
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "author": event["author"],
            "content": event["content"],
            "timestamp": event["timestamp"],
        }))
