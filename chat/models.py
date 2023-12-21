from django.db import models

class ChatMessage(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatMessage {self.id}"