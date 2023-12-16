#study/permissions.py
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    게시물 작성자만 수정 및 삭제할 수 있도록 권한을 설정합니다.
    """

    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS 요청은 항상 허용합니다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 다른 요청에 대해서는 작성자만 허용합니다.
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS 요청은 항상 허용합니다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 다른 요청에 대해서는 작성자만 허용합니다.
        return obj.author == request.user
