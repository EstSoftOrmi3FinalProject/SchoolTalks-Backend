# Basic Django Modules
from rest_framework import serializers

# Custom Models
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "author",
            "author_name",
            "content",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author", "post"]

    def get_author_name(self, obj):
        """
        user객체인 author에서 이름을 걸러내기 위함\n
        기본적으로 닉네임을 출력하고 없으면 이름, 없으면 아이디를 출력한다.
        """
        return obj.author.nickname or obj.author.name or obj.author.username

    def create(self, validated_data):
        validated_data["post_id"] = self.context["view"].kwargs.get("post_id")
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    is_like = serializers.SerializerMethodField()
    likecount = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "author_name",
            "is_notice",
            "created_at",
            "updated_at",
            "hits",
            "comments",
            "likecount",
            "is_like",
        ]
        read_only_fields = [
            "author",
            "is_notice",
            "hits",
        ]

    def get_author_name(self, obj):
        return obj.author.nickname or obj.author.name or obj.author.username

    def get_is_like(self, obj):
        user = self.context["request"].user
        print(Like.objects.filter(user=user))
        if user.is_authenticated:
            return Like.objects.filter(post=obj, user=user).exists()
        return False

    def get_likecount(self, obj):
        return Like.objects.filter(post=obj).count()

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
