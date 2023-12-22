from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ChatMessage

class ChatMessageListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/chat-messages/"  # API 엔드포인트 URL

    def test_list_chat_messages(self):
        # ChatMessage 생성
        ChatMessage.objects.create(message="Test Message 1")
        ChatMessage.objects.create(message="Test Message 2")

        # API 엔드포인트에 GET 요청 보내기
        response = self.client.get(self.url)

        # 응답 상태 코드 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 응답 데이터 확인
        self.assertEqual(len(response.data), 2)

    def test_create_chat_message(self):
        # 유효한 데이터로 POST 요청 보내기
        data = {"message": "Test Message"}
        response = self.client.post(self.url, data, format="json")

        # 응답 상태 코드 확인
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 데이터베이스에 메시지가 생성되었는지 확인
        self.assertEqual(ChatMessage.objects.count(), 1)

    def test_create_invalid_chat_message(self):
        # 잘못된 데이터로 POST 요청 보내기
        data = {"message": ""}  # 빈 메시지
        response = self.client.post(self.url, data, format="json")

        # 응답 상태 코드 확인
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 데이터베이스에 메시지가 생성되지 않았는지 확인
        self.assertEqual(ChatMessage.objects.count(), 0)
