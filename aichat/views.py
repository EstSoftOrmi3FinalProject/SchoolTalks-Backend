from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation
from .serializers import ConversationSerializer
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatViewSet(viewsets.ModelViewSet):
    """
    AI와 채팅을 할 수 있는 Class View 입니다.

    method:
    - GET: 현재 접속된 유저의 채팅 목록을 보여줍니다.
    - POST: prompt를 작성하고 ai의 답변을 받습니다.
    """

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(author=self.request.user)

    def create(self, request, *args, **kwargs):
        print(request.data)
        prompt = request.data.get("prompt")
        if prompt:
            author = self.request.user
            previous_conversations = "\n".join(
                [
                    f"User: {c['prompt']}\nAI: {c['response']}"
                    for c in request.data.get("conversations", [])
                ]
            )
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
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

        return Response(status=status.HTTP_400_BAD_REQUEST)
