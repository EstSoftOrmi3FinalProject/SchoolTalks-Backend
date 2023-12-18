from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatViewSet

router = DefaultRouter()
router.register(r"", ChatViewSet, basename="aichat")

urlpatterns = [
    path("", include(router.urls)),
]
