from ninja import ModelSchema, Router
from courses.models import Course


router = Router(tags=["courses"])


class CourseIn(ModelSchema):
    class Meta:
        model = Course
        fields = ["title", "description", "teacher"]


class CourseOut(ModelSchema):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "teacher", "created_at", "updated_at"]


@router.get("/", response=list[CourseOut])
def list_courses(request):
    return Course.objects.select_related("teacher").all()


@router.post("/", response=CourseOut)
def create_course(request, payload: CourseIn):
    return Course.objects.create(**payload.dict())
