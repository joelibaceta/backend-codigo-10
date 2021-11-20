from django.conf.urls import url

from core.consumer import TicTacToeConsumer


websocket_urlpatterns = [
    url(r'^ws/play/$', TicTacToeConsumer.as_asgi())
]