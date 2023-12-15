# Basic Django Modules
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Rest Framework Modules
from rest_framework import generics, views, permissions, response, status

# Custom Models
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

# User 모델을 가져옵니다.
User = get_user_model()


class PostListCreateView(generics.ListCreateAPIView):
    """
    글 목록과 글 작성을 하는 View입니다.

    method:
    - GET: 글 목록을 출력합니다.
    - POST: 글을 작성합니다.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    글 자세히보기와 수정, 삭제를 합니다.

    method:
    - GET: 글 자세히보기입니다. 조회수를 1 증가시킵니다.
    - PATCH: 글을 수정합니다.
    - DELETE: 글을 삭제합니다.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentCreateView(generics.CreateAPIView):
    """
    댓글 작성을 하는 View입니다.

    method:
    - POST: 댓글을 작성합니다.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentUpdateView(generics.UpdateAPIView):
    """
    댓글 수정을 하는 View입니다.

    method:
    - PATCH: 댓글을 작성합니다.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentDeleteView(generics.DestroyAPIView):
    """
    댓글 삭제를 하는 View입니다.

    method:
    - DELETE: 댓글을 작성합니다.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


class LikeView(views.APIView):
    """
    좋아요를 관리하는 View입니다.

    method:
    - POST: 좋아요가 있으면 생성하고 없으면 409를 냅니다.
    - POST: 좋아요를 삭제합니다.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        """
        좋아요를 생성하는 메서드입니다.

        args:
        - post_id: 좋아요를 생성할 글의 id를 주소창의 <int:post_id>로 받아옵니다.

        return:
        - HTTP 201 created

        error:
        - HTTP 409 conflict
        """
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            return response.Response(status=status.HTTP_409_CONFLICT)

        return response.Response(status=status.HTTP_201_CREATED)

    def delete(self, request, post_id):
        """
        좋아요를 삭제하는 메서드입니다.

        args:
        - post_id: 좋아요를 삭제할 글의 id를 주소창의 <int:post_id>로 받아옵니다.

        return:
        - HTTP 204 no content

        error:
        - HTTP 404 not found
        """
        post = get_object_or_404(Post, id=post_id)
        like = get_object_or_404(Like, post=post, user=request.user)
        like.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
