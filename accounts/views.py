# Basic Django Modules
from django.contrib.auth import get_user_model

# Rest Framework Modules
from rest_framework import generics
from rest_framework import permissions

# Custom Models
from .serializers import UserSerializer

# User 모델을 가져옵니다.
User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    """
    새로운 User를 만들어주는 역할을 합니다.

    function
    - create: 회원가입
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveAPIView):
    """
    특정 사용자의 프로필을 보여줍니다.

    function
    - get: 프로필
        - args:
            - pk: user_id
        - return:
            - name
            - nickname
            - profile_picture
            - about_me
            - school_name
            - grade
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
