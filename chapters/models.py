from django.db import models
from courses.models import Course


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"{self.course.title}: {self.title}"


class LectureVideo(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    duration_seconds = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
