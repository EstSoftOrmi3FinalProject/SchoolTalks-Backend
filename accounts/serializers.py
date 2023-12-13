# Basic Django Modules
from django.contrib.auth import get_user_model

# Rest Framework Modules
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
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
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
