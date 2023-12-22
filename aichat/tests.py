from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AIChatTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_create_conversation(self):
        self.client.force_authenticate(user=self.user)
        prompt = "일반적인 사용자 질문"
        data = {"prompt": prompt}
        response = self.client.post("/aichat/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_conversation_with_exam(self):
        self.client.force_authenticate(user=self.user)
        prompt = "모의고사 문제"
        data = {"prompt": prompt}
        response = self.client.post("/aichat/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_conversation_with_interview(self):
        self.client.force_authenticate(user=self.user)
        prompt = "면접 질문"
        data = {"prompt": prompt}
        response = self.client.post("/aichat/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_conversations(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete("/aichat/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.force_authenticate(user=self.user)
        self.chat_url = "/aichat/"

    def test_list_conversations(self):
        Conversation.objects.create(
            prompt="Prompt 1", response="Response 1", author=self.user
        )
        Conversation.objects.create(
            prompt="Prompt 2", response="Response 2", author=self.user
        )

        response = self.client.get(self.chat_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_conversation(self):
        data = {"prompt": "User Prompt"}
        response = self.client.post(self.chat_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversation.objects.count(), 1)
        self.assertEqual(Conversation.objects.first().prompt, "User Prompt")

    def test_create_conversation_without_prompt(self):
        response = self.client.post(self.chat_url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_conversations(self):
        Conversation.objects.create(
            prompt="Prompt 1", response="Response 1", author=self.user
        )
        Conversation.objects.create(
            prompt="Prompt 2", response="Response 2", author=self.user
        )

        response = self.client.delete(self.chat_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Conversation.objects.count(), 0)
