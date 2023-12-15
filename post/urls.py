# Basic Django Modules
from django.urls import path

# Custom Models
from . import views

urlpatterns = [
    path("", views.PostListCreateView.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailUpdateDeleteView.as_view(), name="post_detail"),
    path(
        "<int:post_id>/comment/create",
        views.CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "<int:post_id>/comment/<int:pk>/update",
        views.CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "<int:post_id>/comment/<int:pk>/delete",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
]
