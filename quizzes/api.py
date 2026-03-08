from ninja import ModelSchema, Router
from quizzes.models import Question, Quiz


router = Router(tags=["quizzes"])


class QuizIn(ModelSchema):
    class Meta:
        model = Quiz
        fields = ["course", "title", "description", "time_limit_minutes", "is_active"]


class QuizOut(ModelSchema):
    class Meta:
        model = Quiz
        fields = ["id", "course", "title", "description", "time_limit_minutes", "is_active"]


class QuestionIn(ModelSchema):
    class Meta:
        model = Question
        fields = ["quiz", "prompt", "options", "correct_option"]


class QuestionOut(ModelSchema):
    class Meta:
        model = Question
        fields = ["id", "quiz", "prompt", "options", "correct_option"]


@router.get("/", response=list[QuizOut])
def list_quizzes(request):
    return Quiz.objects.select_related("course").all()


@router.post("/", response=QuizOut)
def create_quiz(request, payload: QuizIn):
    return Quiz.objects.create(**payload.dict())


@router.get("/questions", response=list[QuestionOut])
def list_questions(request):
    return Question.objects.select_related("quiz").all()


@router.post("/questions", response=QuestionOut)
def create_question(request, payload: QuestionIn):
    return Question.objects.create(**payload.dict())
