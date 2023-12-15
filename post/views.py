# Basic Django Modules
from django.shortcuts import render
from django.contrib.auth import get_user_model

# Rest Framework Modules
from rest_framework import generics
from rest_framework import permissions

# Custom Models
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

# User 모델을 가져옵니다.
User = get_user_model()


class PostListCreateView(generics.ListCreateAPIView):
    """
    글 목록과 글 작성을 하는 View입니다.

    method:
    - GET: 글 목록을 출력합니다.
    - CREATE: 글을 작성합니다.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    글 자세히보기와 수정, 삭제를 합니다.

    method:
    - GET: 글 자세히보기입니다.
    - PATCH: 글을 수정합니다.
    - DELETE: 글을 삭제합니다.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    """
    댓글 목록과 댓글 작성을 하는 View입니다.

    method:
    - GET: 댓글 목록을 출력합니다.
    - CREATE: 댓글을 작성합니다.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs["post_id"])
