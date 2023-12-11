from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from rest_framework import generics
from rest_framework import permissions

# User 모델을 가져옵니다.
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    # CreateAPIView는 post요청을 받아서 새로운 user를 만들어주는 역할을 합니다.
    queryset = User.objects.all() # 사용자 쿼리셋을 설정합니다.
    serializer_class = UserSerializer  # 사용자 정보를 직렬화하는 Serializer 클래스를 설정합니다.
    permission_classes = [permissions.AllowAny]  # 모든 사용자가 접근 가능하도록 권한을 설정합니다.
    # settings.py에 REST_FRAMEWORK의 DEFAULT_PERMISSION_CLASSES를 덮어쓰기 하기 위함입니다.


class UserDetailView(generics.RetrieveAPIView):
    # RetrieveAPIView는 GET 요청을 받아서 사용자의 세부 정보를 반환하는 역할을 합니다.
    queryset = User.objects.all()  # 사용자 쿼리셋을 설정합니다.
    serializer_class = UserSerializer  # 사용자 정보를 직렬화하는 Serializer 클래스를 설정합니다.