from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User


class UserCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse("signup")
        self.user_data = {
            "username": "testuser",
            "password": "testpassword",
            "nickname": "testnickname",
            "school_name": "testschool",
            "name": "testname",
            "grade": 10,
        }

    def test_create_user(self):
        response = self.client.post(self.signup_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_with_existing_username(self):
        User.objects.create_user(**self.user_data)
        response = self.client.post(self.signup_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_weak_password(self):
        weak_password_data = {
            "username": "weakuser",
            "password": "12345",  # 약한 비밀번호
            "nickname": "weaknickname",
            "school_name": "weakschool",
            "name": "weakname",
            "grade": 11,
        }
        response = self.client.post(self.signup_url, weak_password_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_required_fields(self):
        missing_fields_data = {
            "username": "missinguser",
            "password": "missingpassword",
            # 필수 필드인 nickname, school_name, name이 누락됨
            "grade": 12,
        }
        response = self.client.post(self.signup_url, missing_fields_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
