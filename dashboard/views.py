# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from soc.settings import STATIC_URL


class Dashboard(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        kwargs['STATIC_URL'] = STATIC_URL
        return super(Dashboard, self).get_context_data(**kwargs)

dashboard = Dashboard.as_view()
