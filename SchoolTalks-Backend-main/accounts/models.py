from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # 추가 필드 예시
    about_me = models.TextField(blank=True)  # 사용자의 간단한 자기 소개 정보
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # 사용자 프로필 사진을 저장하는 필드