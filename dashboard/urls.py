# -*- coding: utf-8 -*-

from django.conf.urls import url
from dashboard.views import dashboard

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', dashboard, name='index'),
]
