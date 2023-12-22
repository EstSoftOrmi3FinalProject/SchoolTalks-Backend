# study/urls.py
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView,
    CommentListView,
    LikeView,
    PostUpdateView,
    PostDeleteView,
    CommentUpdateView,  # 댓글 수정 및 삭제를 위한 View 추가
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("comments/", CommentCreateView.as_view(), name="comment-create"),
    path("<int:post_id>/comments/", CommentListView.as_view(), name="comment-list"),
    path(
        "comments/<int:pk>/", CommentUpdateView.as_view(), name="comment-update"
    ),  # 댓글 수정 및 삭제를 위한 URL 패턴
    path("<int:post_id>/like/", LikeView.as_view(), name="post-like"),
]
