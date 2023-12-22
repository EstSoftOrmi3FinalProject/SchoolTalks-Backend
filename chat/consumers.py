# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage

from asgiref.sync import sync_to_async


@sync_to_async
def create_chat_message(message):
    return ChatMessage.objects.create(message=message)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # 새로운 메시지를 저장
        chat_message = ChatMessage.objects.create(message=message)

        # WebSocket으로 메시지 전송
        await self.send(
            text_data=json.dumps(
                {
                    "message": chat_message.message,
                    "timestamp": chat_message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
        )
