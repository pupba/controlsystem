# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from apps.moduleprocessing import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('ws/controlsystem/', consumers.ControlSystemConsumer.as_asgi()),
    ]),
})
