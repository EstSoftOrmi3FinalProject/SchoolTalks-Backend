# Basic Django Modules
from rest_framework import serializers

# Custom Models
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "is_notice",
            "created_at",
            "updated_at",
            "hits",
        ]
        read_only_fields = [
            "author",
            "is_notice",
            "hits",
        ]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
