from django.urls import re_path
from .consumers import TrainConsumer

websocket_urlpatterns = [
    re_path("ws/simulator", TrainConsumer.as_asgi()),
]