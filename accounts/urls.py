from django.urls import path
from .views import UserCreateView, UserDetailView

# 로그인은 JWT를 사용하므로, 회원가입과 유저 정보 조회만 구현
urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),  # 회원가입 API 뷰
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # 유저 정보 조회 API 뷰
]