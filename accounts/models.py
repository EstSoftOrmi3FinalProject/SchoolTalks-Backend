# Basic Django Modules
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, verbose_name="아이디")
    about_me = models.TextField(blank=True, verbose_name="자기소개")
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        verbose_name="프로필 사진",
    )
    nickname = models.CharField(max_length=20, verbose_name="닉네임")
    school_name = models.CharField(max_length=20, verbose_name="학교명")
    name = models.CharField(max_length=20, verbose_name="이름")
    grade = models.PositiveSmallIntegerField(verbose_name="학년")

    REQUIRED_FIELDS = ["grade"]
