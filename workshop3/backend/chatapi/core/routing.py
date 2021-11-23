
from django.conf.urls import url
from core.consumers import ChatConsumer

websocket_urlpatterns = [
    url(r'^ws/chatroom/$', ChatConsumer.as_asgi())
]