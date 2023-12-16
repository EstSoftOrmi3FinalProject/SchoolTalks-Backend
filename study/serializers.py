#study/serializers.py
from rest_framework import serializers
from .models import StudyComment, StudyLike, StudyPost


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()  # 뎃글에 대한 유저의 이름을 보여주기 위해 추가

    class Meta:
        model = StudyComment
        fields = ["id", "post", "author", "author_username", "text", "created_at"]
        read_only_fields = ["author"]

    def get_author_username(self, obj):
        """
        get_author_username 함수가 serializers.SerializerMethodField()의 반환값이 되어author_username 에 삽입
        Django REST Framework는 해당 필드에 대한 값을 얻기 위해 get_<field_name> 형식의 메서드를 호출
        """
        return obj.author.username  # 댓글 작성자의 사용자 이름 반환

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    likesCount = serializers.IntegerField(source="likes.count", read_only=True)
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
