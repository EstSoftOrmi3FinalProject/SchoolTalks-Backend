from .models import StudyPost
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class TokenAuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            grade=1,  # 유효한 학년 값으로 변경하세요.
        )

    def test_token_authentication(self):
        # 사용자의 토큰을 얻어옵니다.
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # 받아온 토큰을 사용하여 요청을 보냅니다.
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.post(reverse('post-create'), {'title': 'Test Post', 'caption': 'Test Caption'})
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class StudyPostViewsTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            grade=1,  # 유효한 학년 값으로 변경하세요.
        )

        # Create a sample StudyPost
        self.post = StudyPost.objects.create(
            author=self.user,
            title='Test Post',
            caption='This is a test post.',
        )

    def test_post_detail_view(self):
        response = self.client.get(reverse('post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-create'), {
            'title': 'New Test Post',
            'caption': 'This is a new test post.',
        })
        self.assertEqual(response.status_code, 302)  # 리디렉션 확인
        new_post = StudyPost.objects.latest('id')
        self.assertEqual(new_post.title, 'New Test Post')
        self.assertEqual(new_post.caption, 'This is a new test post.')
        self.assertEqual(new_post.author, self.user)
