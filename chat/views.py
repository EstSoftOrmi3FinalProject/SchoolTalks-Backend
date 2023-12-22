from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from rest_framework.permissions import AllowAny  # 임포트 추가


class ChatMessageListCreateView(APIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [AllowAny]  # 권한 설정 추가

    def get(self, request):
        chat_messages = ChatMessage.objects.all().order_by("-timestamp")[:50]
        serializer = self.serializer_class(chat_messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
