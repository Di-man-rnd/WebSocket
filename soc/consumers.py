# -*- coding: utf-8 -*-

from json import loads
from channels import Group
from channels.sessions import channel_session
from skipass.models import Skipass

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
        derty(text)


@channel_session
def ws_disconnect(message):
    Group("dashboard").discard(message.reply_channel)



#  ------------SKIPASS--------------------
@channel_session
def skipass_add(message):
    message.reply_channel.send({"accept": True})
    Group("skipass").add(message.reply_channel)

@channel_session
def skipass_disconnect(message):
    Group("skipass").discard(message.reply_channel)

@channel_session
def skipass_message(message):
    text = message.content['text']
    if text == 'init':
        Group("skipass").send({
            'text': '0',
        })
    else:
        derty(text)



def derty(param):
    json_load = loads(param)
    Skipass.objects.create(**json_load)
    Group("skipass").send({'text': param,})
