from django.urls import re_path, path

from .consumers import Proctor

websocket_urlpatterns = [
	path('ws/live-proctoring', Proctor.as_asgi()),
]
