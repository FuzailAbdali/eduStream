from ninja import NinjaAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth

from users.api import router as users_router
from courses.api import router as courses_router
from chapters.api import router as chapters_router
from streaming.api import router as streaming_router
from articles.api import router as articles_router
from quizzes.api import router as quizzes_router
from chat.api import router as chat_router
from notifications.api import router as notifications_router

api = NinjaAPI(title="EduStream API", version="1.0.0")
api.register_controllers(NinjaJWTDefaultController)

api.add_router("/users", users_router, auth=JWTAuth())
api.add_router("/courses", courses_router, auth=JWTAuth())
api.add_router("/chapters", chapters_router, auth=JWTAuth())
api.add_router("/streaming", streaming_router, auth=JWTAuth())
api.add_router("/articles", articles_router, auth=JWTAuth())
api.add_router("/quizzes", quizzes_router, auth=JWTAuth())
api.add_router("/chat", chat_router, auth=JWTAuth())
api.add_router("/notifications", notifications_router, auth=JWTAuth())
