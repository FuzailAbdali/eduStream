from django.contrib import admin
from quizzes.models import Question, Quiz

admin.site.register(Quiz)
admin.site.register(Question)
