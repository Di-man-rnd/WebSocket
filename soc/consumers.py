# -*- coding: utf-8 -*-

from channels import Group
from channels.sessions import channel_session


@channel_session
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("dashboard").add(message.reply_channel)


@channel_session
def ws_message(message):
    text = message.content['text']
    # Инициализация компонента "термометр"
    if text == 'init':
        Group("dashboard").send({
            'text': '0',
        })
    else:
        Group("dashboard").send({
            'text': text,
        })


@channel_session
def ws_disconnect(message):
    Group("dashboard").discard(message.reply_channel)
