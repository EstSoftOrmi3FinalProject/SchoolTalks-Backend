from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InquiryViewSet

router = DefaultRouter()
router.register(r"inquiry", InquiryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
