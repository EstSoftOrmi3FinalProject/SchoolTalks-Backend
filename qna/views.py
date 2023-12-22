from rest_framework import viewsets, permissions
from .models import Inquiry
from .serializers import InquirySerializer


class InquiryViewSet(viewsets.ModelViewSet):
    """
    새로운 문의 사항을 생성합니다.
    return:
    - 생성된 문의 사항 정보
    """

    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [permissions.AllowAny]
