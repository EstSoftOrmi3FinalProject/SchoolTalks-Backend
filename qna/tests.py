from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Inquiry
class InquiryViewSetTestCase(APITestCase):
    def setUp(self):
        self.inquiry_data = {
            "email": "test@example.com",
            "subject": "Test Subject",
            "content": "Test Content",
        }
        self.inquiry = Inquiry.objects.create(**self.inquiry_data)

    def test_create_inquiry(self):
        response = self.client.post("/inquiry/", self.inquiry_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inquiry.objects.count(), 2)  
