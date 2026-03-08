from ninja import ModelSchema, Router
from chat.models import ChatMessage


router = Router(tags=["chat"])


class ChatMessageIn(ModelSchema):
    class Meta:
        model = ChatMessage
        fields = ["stream_session", "sender", "message"]


class ChatMessageOut(ModelSchema):
    class Meta:
        model = ChatMessage
        fields = ["id", "stream_session", "sender", "message", "created_at"]


@router.get("/messages", response=list[ChatMessageOut])
def list_messages(request):
    return ChatMessage.objects.select_related("stream_session", "sender").all()


@router.post("/messages", response=ChatMessageOut)
def create_message(request, payload: ChatMessageIn):
    return ChatMessage.objects.create(**payload.dict())
