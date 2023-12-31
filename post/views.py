# Basic Django Modules
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Rest Framework Modules
from rest_framework import generics, views, permissions, response, status
from rest_framework.filters import SearchFilter

# Custom Models
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from .filters import PostFilter
from .pagenation import CustomPagination

# Django Filter
from django_filters.rest_framework import DjangoFilterBackend

# User 모델을 가져옵니다.
User = get_user_model()


class PostListCreateView(generics.ListCreateAPIView):
    """
    글 목록과 글 작성을 하는 View입니다.

    method:
    - GET: 글 목록을 출력합니다.
    - POST: 글을 작성합니다.
    """

    queryset = Post.objects.all().order_by("-pk")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PostFilter
    pagination_class = CustomPagination
    search_fields = ["title", "content"]


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

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.increase_hits()
        return super().get(request, *args, **kwargs)


class CommentListCreateView(generics.ListCreateAPIView):
    """
    댓글 목록과 작성을 하는 View입니다.

    method:
    - GET: 댓글 목록을 출력합니다.
    - POST: 댓글을 작성합니다.
    """
    
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post=post_id)


class CommentDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    댓글 자세히보기와 수정, 삭제를 합니다.

    method:
    - GET: 댓글 자세히보기입니다.
    - PATCH: 댓글을 수정합니다.
    - DELETE: 댓글을 삭제합니다.
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

        return response.Response(
            status=status.HTTP_201_CREATED,
            data={"likecount": Like.objects.filter(post=post_id).count()},
        )

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
        return response.Response(
            status=status.HTTP_200_OK,
            data={"likecount": Like.objects.filter(post=post_id).count()},
        )
