# Generated by Django 5.0 on 2023-12-13 11:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                ("is_notice", models.BooleanField(default=False, verbose_name="공지글")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일자"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정일자"),
                ),
                ("hits", models.PositiveIntegerField(default=0, verbose_name="조회수")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="글쓴이",
                    ),
                ),
            ],
            options={
                "verbose_name": "자유게시판",
                "verbose_name_plural": "자유게시판",
            },
        ),
    ]
