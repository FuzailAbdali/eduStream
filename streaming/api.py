from ninja import ModelSchema, Router
from streaming.models import LiveStreamSession


router = Router(tags=["streaming"])


class LiveStreamSessionIn(ModelSchema):
    class Meta:
        model = LiveStreamSession
        fields = [
            "course",
            "title",
            "stream_key",
            "rtmp_url",
            "playback_url",
            "status",
            "scheduled_for",
        ]


class LiveStreamSessionOut(ModelSchema):
    class Meta:
        model = LiveStreamSession
        fields = [
            "id",
            "course",
            "title",
            "stream_key",
            "rtmp_url",
            "playback_url",
            "status",
            "scheduled_for",
            "started_at",
            "ended_at",
        ]


@router.get("/sessions", response=list[LiveStreamSessionOut])
def list_live_sessions(request):
    return LiveStreamSession.objects.select_related("course").all()


@router.post("/sessions", response=LiveStreamSessionOut)
def create_live_session(request, payload: LiveStreamSessionIn):
    return LiveStreamSession.objects.create(**payload.dict())
