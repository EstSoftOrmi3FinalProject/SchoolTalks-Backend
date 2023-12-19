# Basic Django Modules
from django.urls import path

# Custom Views
from .views import UserCreateView, UserDetailView

# Rest Framework Modules
from rest_framework_simplejwt.views import (
    TokenObtainPairView as get_token,
    TokenRefreshView as refresh_token,
    token_verify,
)

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    # jwt 토큰 발급
    path("token/", get_token.as_view(), name="token_obtain_pair"),
    # jwt 토큰 갱신
    path("token/refresh/", refresh_token.as_view(), name="token_refresh"),
    path("token/verify/", token_verify, name="token_verify"),
]
