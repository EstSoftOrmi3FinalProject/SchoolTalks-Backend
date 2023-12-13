# Basic Django Modules
from django.urls import path

# Custom Views
from .views import UserCreateView, UserDetailView


urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
