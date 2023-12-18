# study > views.py

# Basic Django Modules
from django.shortcuts import get_object_or_404

# Rest Framework Modules
from rest_framework import generics, views, status, response, permissions
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer, CommentSerializer, CommentUpdateSerializer
from .models import StudyComment, StudyPost, StudyLike
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.views.generic import View
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import CommentSerializer
from .permissions import IsCommentAuthorOrReadOnly

class CommentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudyComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return CommentUpdateSerializer
        return CommentSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"detail": "권한이 없습니다."},
                status=status.HTTP_403_FORBIDDEN
            )
class CustomPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = "page_size"
    max_page_size = 1000


class PostListView(generics.ListCreateAPIView):
    queryset = StudyPost.objects.order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title", "author__username"]
    search_fields = ["title", "caption", "author__username"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    queryset = StudyPost.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increment_views()
        serializer = self.get_serializer(
            instance, context={"request": request}
        )  # 요청 객체를 context에 전달
        return response.Response(serializer.data)


class PostCreateView(generics.CreateAPIView):
    queryset = StudyPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateView(generics.UpdateAPIView):
    queryset = StudyPost.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data)


class PostDeleteView(generics.DestroyAPIView):
    queryset = StudyPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]  # 인증된 사용자만 접근 가능하며, 작성자만 삭제 가능

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user:
            instance.delete()
            return Response(status=status.HTTP_200_OK)  # 상태 코드를 200으로 변경
        else:
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)


class CommentCreateView(generics.CreateAPIView):
    queryset = StudyComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListView(generics.ListAPIView):
    queryset = StudyComment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs["post_id"])


class LikeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(StudyPost, id=post_id)
        like, created = StudyLike.objects.get_or_create(post=post, user=request.user)

        # 좋아요를 검색한 후 좋아요가 없으면 생성(like 생성된 객체, created가 생성 여부 판단)
        # created == True : 좋아요가 클릭이 안되어 있어서 새로 생성했다.
        # created == False : 좋아요가 클릭이 되어서 생성하지 못했다.

        if created:
            # 좋아요가 생성되었으면 게시물의 likeCount를 1 증가시킴
            post.likesCount += 1
            post.save()

            # 좋아요가 생성되었으면 201 응답
            return response.Response(status=status.HTTP_201_CREATED)

        # 이미 좋아요가 존재하는 경우, 409 Conflict 반환
        return response.Response(status=status.HTTP_409_CONFLICT)

    def delete(self, request, post_id):
        post = get_object_or_404(StudyPost, id=post_id)  # 게시물이 존재하지 않으면 404 에러
        like = get_object_or_404(
            StudyLike, post=post, user=request.user
        )  # 좋아요가 존재하지 않으면 404 에러

        # 좋아요가 삭제되기 전에 게시물의 likeCount를 1 감소시킴
        post.likesCount -= 1
        post.save()

        like.delete()
        return response.Response(
            status=status.HTTP_204_NO_CONTENT
        )  # 좋아요가 삭제되었으면 204 응답
