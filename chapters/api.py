from ninja import ModelSchema, Router
from chapters.models import Chapter, LectureVideo


router = Router(tags=["chapters"])


class ChapterIn(ModelSchema):
    class Meta:
        model = Chapter
        fields = ["course", "title", "content", "order"]


class ChapterOut(ModelSchema):
    class Meta:
        model = Chapter
        fields = ["id", "course", "title", "content", "order"]


class LectureVideoIn(ModelSchema):
    class Meta:
        model = LectureVideo
        fields = ["chapter", "title", "video_url", "duration_seconds"]


class LectureVideoOut(ModelSchema):
    class Meta:
        model = LectureVideo
        fields = ["id", "chapter", "title", "video_url", "duration_seconds", "created_at"]


@router.get("/", response=list[ChapterOut])
def list_chapters(request):
    return Chapter.objects.select_related("course").all()


@router.post("/", response=ChapterOut)
def create_chapter(request, payload: ChapterIn):
    return Chapter.objects.create(**payload.dict())


@router.get("/videos", response=list[LectureVideoOut])
def list_lecture_videos(request):
    return LectureVideo.objects.select_related("chapter").all()


@router.post("/videos", response=LectureVideoOut)
def create_lecture_video(request, payload: LectureVideoIn):
    return LectureVideo.objects.create(**payload.dict())
