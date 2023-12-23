# Basic Django Modules
from django.urls import path

# Custom Models
from . import views

urlpatterns = [
    path("", views.PostListCreateView.as_view(), name="post"),
    path("<int:pk>/", views.PostDetailUpdateDeleteView.as_view(), name="post_detail"),
    path(
        "<int:post_id>/comment/",
        views.CommentListCreateView.as_view(),
        name="comment",
    ),
    path(
        "<int:post_id>/comment/<int:pk>/",
        views.CommentDetailUpdateDeleteView.as_view(),
        name="comment_detail",
    ),
    path("<int:post_id>/like/", views.LikeView.as_view(), name="like"),
]
