from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # jwt 토큰 발급
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # jwt 토큰 갱신
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # 스키마
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # 스웨거
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # 문서화
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
