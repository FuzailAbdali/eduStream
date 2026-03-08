from django.db import models
from courses.models import Course


class LiveStreamSession(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        LIVE = "live", "Live"
        ENDED = "ended", "Ended"

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="live_sessions")
    title = models.CharField(max_length=255)
    stream_key = models.CharField(max_length=128, unique=True)
    rtmp_url = models.URLField(help_text="RTMP ingest URL (e.g., MediaMTX endpoint)")
    playback_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.course.title} - {self.title}"
