# Basic Django Modules
from rest_framework import serializers

# Custom Models
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    likesCount = serializers.IntegerField(source="likes.count", read_only=True)
    isLiked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "author_username",
            "caption",
            "image",
            "created_at",
            "comments",
            "likesCount",
            "isLiked",
        ]
        read_only_fields = ["author"]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
