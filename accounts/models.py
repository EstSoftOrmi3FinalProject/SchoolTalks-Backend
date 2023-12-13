from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.utils.translation import gettext as _


class User(AbstractUser):
    # 추가 필드 예시
    username = models.CharField(max_length=30, unique=True, verbose_name="아이디")
    about_me = models.TextField(blank=True, verbose_name="자기소개")  # 사용자의 간단한 자기 소개 정보
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True
    )  # 사용자 프로필 사진을 저장하는 필드
    nickname = models.CharField(max_length=20, verbose_name="닉네임")
    school_name = models.CharField(max_length=20, verbose_name="학교명")
    name = models.CharField(max_length=20, verbose_name="이름")
    grade = models.PositiveSmallIntegerField(verbose_name="학년")
