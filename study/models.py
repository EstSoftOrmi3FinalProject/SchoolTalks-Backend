from django.db import models
from accounts.models import User  # User 모델 임포트


class StudyPost(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="study_posts"
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    caption = models.TextField()
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    attachment = models.FileField(upload_to="post_attachments/", null=True, blank=True)
    views = models.PositiveIntegerField(default=0)  # 조회수 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # self.author와 self.author.username은 같은 값을 반환합니다.
        # 다만 시리얼라이저에서는 self.author.username을 사용해야 합니다.
        # 시리얼라이저에서 author는 pk 값을 보여줍니다.
        return f"{self.author} - {self.caption[:10]}"

    def increment_views(self):
        self.views += 1
        self.save()


class StudyComment(models.Model):
    post = models.ForeignKey(
        StudyPost, on_delete=models.CASCADE, related_name="study_comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="study_comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.text}"


class StudyLike(models.Model):
    post = models.ForeignKey(
        StudyPost, on_delete=models.CASCADE, related_name="study_likes"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="study_likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return f"{self.user.username} likes {self.post.caption}"
