# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # DRF 뷰 URL 패턴
    path('api/chat-messages/', views.ChatMessageListCreateView.as_view(), name='chat-message-list-create'),
]
