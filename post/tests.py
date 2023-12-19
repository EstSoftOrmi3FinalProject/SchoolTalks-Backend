# Basic Django Modules
from django.contrib.auth.models import User
from django.urls import reverse

# Rest Framework Modules
from rest_framework.test import APITestCase
from rest_framework import status

# Custom Models
from .models import Post
from .serializers import PostSerializer


class PostListCreateViewTests(APITestCase):
    def setUp(self):
        # 테스트에 필요한 초기 데이터 설정
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.post_data = {
            "title": "Test Title",
            "content": "Test Content",
            "author": self.user.id,
            "is_notice": False,
        }

    def test_create_post(self):
        # 새로운 게시글 생성 테스트
        self.client.force_authenticate(user=self.user)  # 인증된 사용자로 설정
        url = reverse("post-list")
        response = self.client.post(url, self.post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 생성된 게시글이 데이터베이스에 있는지 확인
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.get()
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")

    def test_get_post_list(self):
        # 게시글 목록 조회 테스트
        Post.objects.create(title="Post 1", content="Content 1", author=self.user)
        Post.objects.create(title="Post 2", content="Content 2", author=self.user)

        url = reverse("post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 응답 데이터와 실제 데이터 비교
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
