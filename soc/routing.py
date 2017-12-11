# -*- coding: utf-8 -*-

from channels.routing import route


channel_routing = [
    route("websocket.connect", 'soc.consumers.ws_add', path=r"^/dashboard/$"),
    route("websocket.receive", 'soc.consumers.ws_message', path=r"^/dashboard/$"),
    route("websocket.disconnect", 'soc.consumers.ws_disconnect', path=r"^/dashboard/$"),


    route("websocket.connect", 'soc.consumers.skipass_add', path=r"^/skipass/$"),
    route("websocket.receive", 'soc.consumers.skipass_message', path=r"^/skipass/$"),
    route("websocket.disconnect", 'soc.consumers.skipass_disconnect', path=r"^/skipass/$"),


]
