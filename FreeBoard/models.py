# Basic Django Modules
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class FreePost(models.Model):
    title = models.CharField(_("제목"), max_length=50)
    content = models.TextField(_("내용"))
    author = models.ForeignKey(User, verbose_name=_("글쓴이"), on_delete=models.CASCADE)
    is_notice = models.BooleanField(_("공지글"), default=False)
    created_at = models.DateTimeField(_("작성일자"), auto_now_add=True)
    updated_at = models.DateTimeField(_("수정일자"), auto_now=True)
    hits = models.PositiveIntegerField(_("조회수"), default=0)

    class Meta:
        verbose_name = _("자유게시판")
        verbose_name_plural = _("자유게시판")

    def __str__(self):
        return self.title
