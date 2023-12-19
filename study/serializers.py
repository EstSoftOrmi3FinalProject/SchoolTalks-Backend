# study/serializers.py
from rest_framework import serializers
from .models import StudyComment, StudyLike, StudyPost


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    deleted = serializers.BooleanField(default=False, read_only=True)


    class Meta:
        model = StudyComment
        fields = ["id", "post", "author", "author_username", "text", "created_at", "deleted"]
        read_only_fields = ["author"]

    def get_author_username(self, obj):
        return obj.author.username

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get("text", instance.text)
        instance.deleted = validated_data.get("deleted", instance.deleted)
        instance.save()
        return instance

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyComment
        fields = ["text"]

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    likesCount = serializers.SerializerMethodField()
    isLiked = serializers.SerializerMethodField()

    class Meta:
        model = StudyPost
        fields = [
            "id",
            "author",
            "author_username",
            "title",
            "caption",
            "image",
            "attachment",
            "views",
            "created_at",
            "comments",
            "likesCount",
            "isLiked",
        ]
        read_only_fields = ["author", "views"]

    def get_likesCount(self, obj):
        return StudyLike.objects.filter(post=obj).count()  # 게시물에 대한 실제 좋아요 개수 반환

    def get_isLiked(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            # Like 모델을 사용하여 현재 사용자가 게시물에 좋아요를 눌렀는지 확인
            return StudyLike.objects.filter(post=obj, user=user).exists()
        return False

    def get_author_username(self, obj):
        return obj.author.username  # 댓글 작성자의 사용자 이름 반환

    def create(self, validated_data):
        # 현재 요청을 보낸 사용자를 게시물의 저자로 설정
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)

    def increment_views(self, obj):
        obj.increment_views()
