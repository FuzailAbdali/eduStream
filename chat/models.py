from django.conf import settings
from django.db import models
from streaming.models import LiveStreamSession


class ChatMessage(models.Model):
    stream_session = models.ForeignKey(LiveStreamSession, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="chat_messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.sender.username}: {self.message[:30]}"
