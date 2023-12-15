from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListCreateView.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailUpdateDeleteView.as_view(), name="post_detail"),
    path(
        "<int:pk>/comment",
        views.CommentListCreateView.as_view(),
        name="comment_create",
    ),
]
