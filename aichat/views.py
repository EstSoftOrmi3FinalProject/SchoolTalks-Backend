from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation
from .serializers import ConversationSerializer
from dotenv import load_dotenv
from openai import OpenAI
from django.conf import settings

api_key = settings.OPENAI_API_KEY
client = OpenAI(api_key=api_key)

load_dotenv()


class ChatViewSet(viewsets.ModelViewSet):
    """
    AI와 채팅을 할 수 있는 Class View 입니다.

    method:
    - GET: 현재 접속된 유저의 채팅 목록을 보여줍니다.
    - POST: prompt를 작성하고 ai의 답변을 받습니다.
    - DELETE: 현재 접속된 유저의 채팅을 모두 삭제합니다.
    """

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(author=user)

    def create(self, request, *args, **kwargs):
        prompt = request.data.get("prompt")
        author = self.request.user

        if not Conversation.objects.filter(author=author).exists():
            # 이전 대화 데이터가 없는 경우
            if "문제" in prompt:
                system_prompt = f"SYSTEM: 너는 고등학생들의 질문을 받아주는 선생님 AI야. 학생이 {prompt}라는 질문을 했을 때 고등학교 입시 수준 맞게 적절하게 답변해줘."
            elif "면접" in prompt:
                system_prompt = f"SYSTEM: 너는 학생의 대입 면접을 도와주는 대학 면접관 AI야. 학생이 {prompt}라는 질문을 했을 때 대학교를 들어가는 입시 면접에 적절하게 답변해줘."
            else:
                system_prompt = (
                    "SYSTEM: 너는 고등학생들의 질문을 받아주는 AI야. 교육 및 입시 정보에서 벗어나지 않는 범위에서 답변을 해줘."
                )
            prompt_with_system = f"{system_prompt}\nUser: {prompt}\nAI:"
        else:
            # 이전 대화 데이터가 있는 경우
            previous_conversations = Conversation.objects.filter(author=author)
            conversation_text = "\n".join(
                [f"User: {c.prompt}\nAI: {c.response}" for c in previous_conversations]
            )
            prompt_with_system = f"{conversation_text}\nUser: {prompt}\nAI:"

        model_engine = "text-davinci-003"
        completions = client.completions.create(
            model=model_engine,
            prompt=prompt_with_system,
            max_tokens=1024,
            n=5,
            stop=None,
            temperature=0.5,
        )
        response = completions.choices[0].text.strip()

        conversation_data = {
            "prompt": prompt,
            "response": response,
            "author": author.pk,
        }
        serializer = self.get_serializer(data=conversation_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        conversations_to_delete = Conversation.objects.filter(author=user)
        conversations_to_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
