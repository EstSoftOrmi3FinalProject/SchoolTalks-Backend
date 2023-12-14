# Rest Framework Modules
from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    읽기는 전체 허용, 나머지는 작성자만 허용해주는 permissions이다.

    method:
    - GET: True
    - HEAD: True
    - OPTIONS: True
    - PUT: obj.author == request.user
    - PATCH: obj.author == request.user
    - DELETE: obj.author == request.user
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return obj.author == request.user
