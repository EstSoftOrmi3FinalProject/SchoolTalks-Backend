#study/urls.py  
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
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("comments/", CommentCreateView.as_view(), name="comment-create"),
    path("<int:post_id>/comments/", CommentListView.as_view(), name="comment-list"),
    path("<int:post_id>/like/", LikeView.as_view(), name="post-like"),
]
