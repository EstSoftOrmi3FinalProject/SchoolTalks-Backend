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
