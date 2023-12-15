from django.urls import path
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
        "comment/<int:pk>/update",
        views.CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "comment/<int:pk>/delete",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
]
