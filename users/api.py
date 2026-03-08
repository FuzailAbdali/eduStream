from ninja import Router, Schema
from users.models import User


router = Router(tags=["users"])


class UserOut(Schema):
    id: int
    username: str
    email: str
    role: str


@router.get("/", response=list[UserOut])
def list_users(request):
    return User.objects.all()
