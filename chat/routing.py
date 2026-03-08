from django.urls import re_path
from chat.consumers import LectureChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<session_id>\d+)/$", LectureChatConsumer.as_asgi()),
]
