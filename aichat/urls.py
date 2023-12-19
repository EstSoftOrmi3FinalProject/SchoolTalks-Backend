from django.urls import path
from .views import ChatViewSet

urlpatterns = [
    path("", ChatViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='aichat-list'),
]