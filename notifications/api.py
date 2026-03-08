from ninja import ModelSchema, Router
from notifications.models import Notification


router = Router(tags=["notifications"])


class NotificationIn(ModelSchema):
    class Meta:
        model = Notification
        fields = ["user", "title", "message", "is_read"]


class NotificationOut(ModelSchema):
    class Meta:
        model = Notification
        fields = ["id", "user", "title", "message", "is_read", "created_at"]


@router.get("/", response=list[NotificationOut])
def list_notifications(request):
    return Notification.objects.select_related("user").all()


@router.post("/", response=NotificationOut)
def create_notification(request, payload: NotificationIn):
    return Notification.objects.create(**payload.dict())
