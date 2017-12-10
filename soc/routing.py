# -*- coding: utf-8 -*-

from channels.routing import route


channel_routing = [
    route("websocket.connect", 'soc.consumers.ws_add', path=r"^/dashboard/$"),
    route("websocket.receive", 'soc.consumers.ws_message', path=r"^/dashboard/$"),
    route("websocket.disconnect", 'soc.consumers.ws_disconnect', path=r"^/dashboard/$"),
]
