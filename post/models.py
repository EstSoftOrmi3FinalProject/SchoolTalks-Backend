# Basic Django Modules
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(_("제목"), max_length=50)
    content = models.TextField(_("내용"))
    author = models.ForeignKey(User, verbose_name=_("글쓴이"), on_delete=models.CASCADE)
    is_notice = models.BooleanField(_("공지글"), default=False)
    created_at = models.DateTimeField(_("작성일자"), auto_now_add=True)
    updated_at = models.DateTimeField(_("수정일자"), auto_now=True)
    hits = models.PositiveIntegerField(_("조회수"), default=0)

    class Meta:
        verbose_name = _("자유게시판 게시글")
        verbose_name_plural = _("자유게시판 게시글들")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name=_("원본 글"),
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        verbose_name=_("글쓴이"),
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.TextField(_("내용"))
    created_at = models.DateTimeField(_("작성일자"), auto_now_add=True)
    updated_at = models.DateTimeField(_("수정일자"), auto_now=True)

    class Meta:
        verbose_name = _("자유게시판 게시글 댓글")
        verbose_name_plural = _("자유게시판 게시글 댓글들")

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("좋아요")
        verbose_name_plural = _("좋아요들")

    def __str__(self):
        return f"{self.user}가 누른 {self.post}의 좋아요"
