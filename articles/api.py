from ninja import ModelSchema, Router
from articles.models import Article


router = Router(tags=["articles"])


class ArticleIn(ModelSchema):
    class Meta:
        model = Article
        fields = ["course", "author", "title", "content", "status", "teacher_feedback", "approved_by"]


class ArticleOut(ModelSchema):
    class Meta:
        model = Article
        fields = [
            "id",
            "course",
            "author",
            "title",
            "content",
            "status",
            "teacher_feedback",
            "approved_by",
            "created_at",
            "updated_at",
        ]


@router.get("/", response=list[ArticleOut])
def list_articles(request):
    return Article.objects.select_related("course", "author", "approved_by").all()


@router.post("/", response=ArticleOut)
def create_article(request, payload: ArticleIn):
    return Article.objects.create(**payload.dict())
