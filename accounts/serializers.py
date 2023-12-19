# Basic Django Modules
from django.contrib.auth import get_user_model

# Rest Framework Modules
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    view_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "nickname",
            "school_name",
            "name",
            "grade",
            "about_me",
            "profile_picture",
            "id",
            "view_name",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def get_view_name(self, obj):
        """
        기본적으로 닉네임을 출력하고 없으면 이름, 없으면 아이디를 출력한다.
        """
        return obj.nickname or obj.name or obj.username

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
